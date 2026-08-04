from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79heightfourcomplexpgl3floatingboundary"
PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "rank3_complex_PGL3_floating_boundary.packet.json"
)
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourComplexPGL3FloatingBoundary_A219_v1.md"
AUDIT = ROOT / "proof_corpus" / f"{SLUG}_audit.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    next_required = packet["next_required_artifact"]
    candidate = {
        "schema": "MTTSelectedQ79HeightFourComplexPGL3FloatingBoundary.v1",
        "artifact": "A219",
        "status": packet["status"],
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "audit": relative(AUDIT),
        "audit_sha256": sha256(AUDIT),
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "what_closes": {
            "full_complex_PGL3_Jacobian_rank_8": True,
            "realified_Jacobian_rank_16": True,
            "independent_imaginary_direction_check": True,
            "three_wall_free_same_source_nonlinear_Newton_steps": True,
            "floating_residual_reduced_to_billionth_scale": True,
            "floating_error_source_localized_to_d087_first": True,
        },
        "what_remains_open": {
            "validated_d087_and_rank3_chain_period_transport": True,
            "interval_Newton_zero_certificate": True,
            "global_height_four_completeness": True,
            "full_SM_closure": True,
        },
        "next_required_artifact": next_required,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79HeightFourComplexPGL3FloatingBoundary",
        "status": packet["status"],
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": next_required,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
