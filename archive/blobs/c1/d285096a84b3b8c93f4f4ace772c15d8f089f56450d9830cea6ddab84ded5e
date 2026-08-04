"""Audit same-source dynamic transfer identity / Galerkin C1 contractions emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
CERT = ROOT / "certificates" / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.py"

STATUS = (
    "MTT_SELECTED_SAMESOURCE_DYNAMICTRANSFERIDENTITY_OR_GALERKINC1CONTRACTIONS_"
    "EMISSION_BUILT_NORMAL_FORM_IDENTITY_OPEN"
)
NEXT = "MTT_Selected_PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_v1"


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
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    support = data["closed_support"]
    for key in [
        "source_level_Z_X_carrier",
        "active_shift_1_1",
        "static_Z_to_u_e",
        "static_trace_normalization",
        "conditional_transfer_exact",
        "conditional_Gram_exact",
    ]:
        require(support[key] is True, f"support not closed: {key}")

    identity = data["normal_form_identity"]
    require(identity["name"] == "SelectedSameSourceDynamicTransferIdentityNormalForm", "identity name mismatch")
    require(identity["coordinate_system"]["codomain_real_dimension"] == 72, "coordinate dimension mismatch")
    require(len(identity["identity_equations"]) == 7, "identity equation count mismatch")
    require(identity["finite_values_if_identity_proved"]["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Gram mismatch")
    require(identity["finite_values_if_identity_proved"]["A_transpose_b"] == [12.0, 12.0], "rhs mismatch")
    require(identity["finite_values_if_identity_proved"]["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(identity["proved_conditionally"] is True, "conditional theorem missing")
    require(identity["selected_identity_proved_now"] is False, "identity overproved")

    lane_a = data["lane_A_same_source_dynamic_transfer"]
    require(lane_a["can_promote_now"] is False, "Lane A overpromoted")
    require(len(lane_a["minimal_missing_equations"]) == 4, "Lane A missing equations mismatch")
    for key, value in lane_a["selected_status"].items():
        require(value is False, f"selected status overclaimed: {key}")

    lane_b = data["lane_B_honest_Galerkin_C1_contractions"]
    require(lane_b["can_promote_now"] is False, "Lane B overpromoted")
    require(lane_b["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "Galerkin status mismatch")
    require(lane_b["selected_source_verified"] is False, "Galerkin source oververified")
    require(lane_b["coordinate_compatibility_required"]["codomain_real_dimension"] == 72, "Galerkin coordinate mismatch")

    falsifier = data["falsifier_contract"]
    for key in [
        "if_selected_dynamic_transfer_emits_different_Gram",
        "if_selected_b_selected_differs_from_phase_plus_shift",
        "if_honest_Galerkin_emits_different_response_matrices",
        "if_observed_flavor_data_selects_any_equation",
    ]:
        require(key in falsifier, f"falsifier missing: {key}")

    decision = data["promotion_decision"]
    require(decision["identity_normal_form_built"] is True, "identity normal form not built")
    for key in [
        "selected_dynamic_transfer_identity_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_deltaTheta_C1_promoted",
        "honest_Galerkin_C1_contractions_promoted",
        "full_no_knob_flavor_closure_promoted",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    closes = data["what_closes_now"]
    for key in [
        "same_source_identity_normal_form_built",
        "conditional_promotion_theorem_formalized",
        "falsifier_contract_built",
        "next_proof_target_reduced_to_PhiFinC1_identity_or_Galerkin_run",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "prove_PhiFinC1_selected_dynamic_transfer_identity",
        "emit_selected_Hessian_blocks",
        "emit_selected_b_selected",
        "emit_selected_A_selected",
        "run_honest_Galerkin_C1_contraction_emission",
        "full_SM_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    for key in [
        "closure_claimed",
        "observed_data_used",
        "target_fitting_used",
        "selected_dynamic_transfer_identity_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "Galerkin_C1_contractions_claimed",
    ]:
        require(data[key] is False, f"guardrail overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
