"""Audit selected Phi_fin alpha1 payload attempt import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "phifin_alpha1_payload_attempt_import.candidate.json"
CERT = ROOT / "certificates" / "phifin_alpha1_payload_attempt_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "PhiFinAlpha1_Payload_Attempt_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_phifin_alpha1_payload_attempt.py"

STATUS = "PHIFIN_ALPHA1_PAYLOAD_ATTEMPT_IMPORTED_SPECTRAL_VALUES_OPEN"
NEXT = "MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    upstream = data["upstream_phifin_alpha1_payload"]
    summary = upstream["payload_summary"]
    require(summary["all_support_shapes_present"] is True, "support shapes missing")
    require(summary["all_selected_values_emitted"] is False, "selected values over-emitted")
    require(all(summary["support_candidate_present"].values()), "some support candidate missing")
    require(all(flag is False for flag in summary["selected_payload_flags"].values()), "payload flag overfilled")
    require(upstream["projective_gerbe_support"]["source_level_promoted"] is True, "source-level gerbe support missing")
    require(upstream["projective_gerbe_support"]["operator_level_projective_rhoE_promoted"] is False, "rhoE overpromoted")
    require(upstream["next_blocker"]["name"] == "SelectedSpectralGalerkinProjectorRetentionData", "wrong next blocker")

    guard = data["guardrails"]
    for key in [
        "claims_selected_PhiFin_alpha1_payload_values",
        "claims_selected_twist_or_source_verification",
        "claims_operator_level_projective_rhoE_promotion",
        "claims_coherent_spectral_projector_retention",
        "claims_selected_DE_Riesz_Green_dotD_values",
        "claims_finite_C1_Hessian_or_deltaTheta",
        "claims_zero_mode_bases_or_primitive_contractions",
        "claims_A_selected_or_b_selected",
        "claims_Yukawa_or_full_SM_closure",
        "uses_observed_constants_masses_or_CKM_phase",
        "uses_benchmark_matrices_or_target_residuals",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("Every selected payload flag remains" in note, "note missing payload guardrail")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
