from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "certificates" / "q79_fuyau_mixed_c2_hodge_admissibility_certificate.json"
NOTE = ROOT / "proof_corpus" / "q79_FuYau_Mixed_C2_Hodge_Admissibility_Theorem_v1.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    data = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    assert data["schema"] == "MTTQ79FuYauMixedC2HodgeAdmissibility.v1"
    for row in data["authority_hashes"]:
        path = Path(row["path"])
        assert path.exists()
        assert sha256(path) == row["sha256"]
    geometry = data["selected_geometry"]
    assert geometry["intersection_rows"] == {
        "H_dot_delta": 0,
        "delta_square": -4,
        "delta_primitive": True,
    }
    representatives = data["differential_representatives"]
    assert representatives["Hhat"]["fiber_integral"] == "pi_!(Hhat)=H"
    assert representatives["u"]["bidegree"] == [2, 2]
    assert representatives["u"]["closed"]
    assert representatives["u"]["integral_and_primitive"]
    assert representatives["orientation"]["bidegree"] == [3, 3]
    assert representatives["orientation"]["closed"]
    checks = data["checks"]
    assert not checks["observed_SM_values_used"]
    assert all(
        value
        for key, value in checks.items()
        if key != "observed_SM_values_used"
    )
    tiers = data["claim_tiers"]
    assert tiers["mixed_c2_9u_Hodge_admissibility"].startswith("CLOSED_EXACT")
    assert tiers["holomorphic_nonpullback_SU3_bundle"] == "OPEN"
    assert tiers["balanced_stability_and_HYM"] == "OPEN"
    assert tiers["differential_total_space_Bianchi_identity"] == "OPEN"
    assert tiers["UV_complete_q79_quantum_gravity"] == "OPEN"
    assert not any(data["guardrails"].values())
    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "explicit closed `(2,2)` representative",
        "not automatically the Chern class",
        "UV completion is",
        "not claimed",
    ):
        assert phrase in note
    print("Q79_FUYAU_MIXED_C2_HODGE_ADMISSIBILITY_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
