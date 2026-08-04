"""Audit same-source dynamic-transfer identity normal form import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "samesource_dynamictransferidentity_or_galerkinc1contractions_emission_import.candidate.json"
CERT = ROOT / "certificates" / "samesource_dynamictransferidentity_or_galerkinc1contractions_emission_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.py"

STATUS = "SAMESOURCE_DYNAMIC_TRANSFER_IDENTITY_NORMAL_FORM_IMPORTED_OPEN"
NEXT = "Selected_U1Y_RouteC_PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    identity = data["normal_form_identity"]
    require(identity["coordinate_system"]["codomain_real_dimension"] == 72, "coordinate dimension mismatch")
    require(len(identity["identity_equations"]) == 7, "identity equation count mismatch")
    require(identity["finite_values_if_identity_proved"]["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Gram mismatch")
    require(identity["finite_values_if_identity_proved"]["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(identity["finite_values_if_identity_proved"]["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(identity["proved_conditionally"] is True, "conditional proof missing")
    require(identity["selected_identity_proved_now"] is False, "identity overproved")

    lane_a = data["lane_A_same_source_dynamic_transfer"]
    require(lane_a["can_promote_now"] is False, "Lane A overpromoted")
    require(len(lane_a["minimal_missing_equations"]) == 4, "Lane A missing-equation mismatch")
    require(all(value is False for value in lane_a["selected_status"].values()), "Lane A selected field emitted")

    lane_b = data["lane_B_honest_Galerkin_C1_contractions"]
    require(lane_b["can_promote_now"] is False, "Lane B overpromoted")
    require(lane_b["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "Galerkin status mismatch")
    require(lane_b["selected_source_verified"] is False, "Galerkin source verified")

    falsifier = data["falsifier_contract"]
    for key in [
        "if_selected_dynamic_transfer_emits_different_Gram",
        "if_selected_b_selected_differs_from_phase_plus_shift",
        "if_honest_Galerkin_emits_different_response_matrices",
        "if_observed_flavor_data_selects_any_equation",
    ]:
        require(key in falsifier, f"falsifier missing: {key}")

    guardrails = data["guardrails"]
    require(guardrails["identity_normal_form_built"] is True, "identity normal form missing")
    require(guardrails["selected_identity_proved_now"] is False, "identity proved overclaim")
    require(guardrails["selected_dynamic_transfer_identity_claimed"] is False, "transfer claimed")
    require(guardrails["selected_A_selected_claimed"] is False, "A claimed")
    require(guardrails["selected_b_selected_claimed"] is False, "b claimed")
    require(guardrails["selected_deltaTheta_C1_claimed"] is False, "delta claimed")
    require(guardrails["honest_Galerkin_C1_contractions_claimed"] is False, "Galerkin claimed")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")
    require(guardrails["full_SM_closure_claimed"] is False, "closure claimed")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
