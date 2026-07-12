"""Audit conditional dynamic-transfer/Hessian/b-selected value-fill import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_import.candidate.json"
CERT = ROOT / "certificates" / "dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.py"

STATUS = "DYNAMIC_TRANSFER_HESSIAN_BSELECTED_VALUEFILL_IMPORTED_CONDITIONAL_GRAM_EXACT_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_v1"


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

    packet = data["conditional_dynamic_transfer_coordinate_packet"]
    require(packet["coordinate_system"]["codomain_real_dimension"] == 72, "dimension mismatch")
    require(packet["A_conditional_shape"] == [72, 2], "A shape mismatch")
    require(packet["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Gram mismatch")
    require(packet["A_transpose_b_conditional"] == [12.0, 12.0], "A^T b mismatch")
    require(packet["b_conditional_norm_sq"] == 24.0, "b norm mismatch")
    require(packet["deltaTheta_conditional_from_Gram_solve"] == [1.0, 1.0], "deltaTheta mismatch")
    require(packet["residual_norm"] == 0.0, "residual nonzero")
    require(packet["condition_number"] == 1.0, "condition number mismatch")

    hessian = data["hessian_bselected_fill_attempt"]
    require(hessian["attempted"] is True, "Hessian fill not attempted")
    require(hessian["conditional_Hessian_Gram_candidate"]["selected_by_MTT"] is False, "Hessian overselected")
    require(hessian["conditional_b_candidate"]["selected_b_selected"] is False, "b overselected")
    require(hessian["promoted"] is False, "Hessian promoted")
    require(all(value is False for value in hessian["selected_value_slots_from_C1_response_audit"].values()), "selected slot emitted")

    galerkin = data["honest_Galerkin_C1_value_fill_attempt"]
    require(galerkin["attempted"] is True, "Galerkin not attempted")
    require(galerkin["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING", "Galerkin status mismatch")
    require(galerkin["selected_source_verified"] is False, "Galerkin source verified")
    require(galerkin["promoted"] is False, "Galerkin promoted")

    gate = data["promotion_gate"]
    require(gate["conditional_dynamic_value_packet_built"] is True, "conditional packet missing")
    require(gate["no_linear_algebra_obstruction"] is True, "linear algebra obstruction remains")
    require(all(gate["qualitative_flavor_tests_pass_conditionally"].values()), "conditional flavor test failed")
    for key in [
        "selected_dynamic_transfer_identity_emitted",
        "selected_Hessian_bselected_emitted",
        "honest_Galerkin_C1_contractions_emitted",
        "promote_to_selected_A_selected",
        "promote_to_selected_b_selected",
        "promote_to_selected_deltaTheta_C1",
    ]:
        require(gate[key] is False, f"promotion overclaimed: {key}")

    guardrails = data["guardrails"]
    require(guardrails["conditional_dynamic_value_packet_built"] is True, "guardrail packet missing")
    require(guardrails["no_linear_algebra_obstruction"] is True, "guardrail linear obstruction")
    require(guardrails["selected_dynamic_transfer_identity_claimed"] is False, "transfer claimed")
    require(guardrails["selected_Hessian_blocks_claimed"] is False, "Hessian claimed")
    require(guardrails["selected_A_selected_claimed"] is False, "A claimed")
    require(guardrails["selected_b_selected_claimed"] is False, "b claimed")
    require(guardrails["selected_deltaTheta_C1_claimed"] is False, "deltaTheta claimed")
    require(guardrails["honest_Galerkin_C1_contractions_claimed"] is False, "Galerkin claimed")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")
    require(guardrails["full_SM_closure_claimed"] is False, "closure claimed")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
