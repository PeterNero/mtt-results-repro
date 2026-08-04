from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    REPO
    / "certificates"
    / "q79_selected_lorentzian_coframe_causal_closure_certificate.json"
)
EXPECTED_STATUS = (
    "SELECTED_LORENTZIAN_COFRAME_AND_CAUSAL_REPRESENTATIVE_CLOSED_"
    "AFTER_A_QG_AND_ONE_BINARY_CAUSAL_BOUNDARY_MARK"
)
EXPECTED_INPUTS = {
    "primitive_branch_axiom",
    "coframe_solder_bridge",
    "same_source_neutrality",
    "classical_gr_closure",
    "time_oriented_branch",
    "causal_separation_theorem",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    payload = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    if payload.get("certificate") != "q79_selected_lorentzian_coframe_causal_closure":
        raise AssertionError("unexpected certificate")
    if payload.get("status") != EXPECTED_STATUS:
        raise AssertionError("unexpected status")
    inputs = payload.get("inputs")
    if not isinstance(inputs, dict) or set(inputs) != EXPECTED_INPUTS:
        raise AssertionError("unexpected input set")

    for name in sorted(EXPECTED_INPUTS):
        record = inputs[name]
        if set(record) != {"path", "sha256"}:
            raise AssertionError(f"unexpected input record: {name}")
        path = (REPO / record["path"]).resolve()
        if not path.is_file():
            raise FileNotFoundError(path)
        record["sha256"] = digest(path)

    CERTIFICATE.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(f"WROTE: {CERTIFICATE}")


if __name__ == "__main__":
    main()
