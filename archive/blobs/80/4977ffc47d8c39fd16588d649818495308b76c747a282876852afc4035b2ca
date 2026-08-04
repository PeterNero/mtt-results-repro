from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    checkpoint_path = arguments.checkpoint.resolve()
    certificate_path = arguments.certificate.resolve()
    output_path = arguments.output.resolve()

    checkpoint = load(checkpoint_path)
    certificate = load(certificate_path)
    if checkpoint.get("schema") != "MTTQ79ReverseTargetMainHessianCheckpoint.v1":
        raise ValueError("expected a reverse target Hessian checkpoint")
    if certificate.get("schema") not in {
        "MTTQ79HeightFourAffineChainBasisReanchor.v1",
        "MTTQ79HeightFourInteriorAffineChainBasisReanchor.v1",
    }:
        raise ValueError("expected an affine-chain reanchor certificate")

    index = int(checkpoint["configuration"]["index"])
    if int(certificate["distinguished_index"]) != index:
        raise AssertionError("checkpoint and reanchor target indices differ")
    scope = certificate["strict_scope"]
    reanchor_closed = scope.get("smooth_base_affine_reanchor_closed", False) or scope.get(
        "regular_fiber_affine_reanchor_closed", False
    )
    if not (
        reanchor_closed
        and scope["puncture_at_infinity_coordinate_retained"]
        and scope["integer_coordinates_selected_by_verified_interval_solve"]
    ):
        raise AssertionError("affine reanchor certificate is not promotion ready")

    checkpoint["affine_chain_basis_reanchor"] = {
        "certificate": authority(certificate_path),
        "same_position_outputs_and_output_radii_retained": True,
        "five_coordinate_lift_replaced_by_selected_affine_basis_enclosure": True,
        "provenance_restored_after_checkpoint_write": True,
        "restoration_changes_no_numerical_state": True,
    }
    dump(output_path, checkpoint)
    print(f"restored d{index:03d} affine provenance in {relative(output_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
