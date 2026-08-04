"""Audit Step64 dynamic-coefficient source-origin / primitive-formula frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step64_dynamiccoefficient_source_origin_or_primitiveformula_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_PACKET = PACKET_DIR / "step64_dynamic_coefficient_source_origin.packet.json"
CUTSET = PACKET_DIR / "step64_primitive_formula_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step64_DynamicCoefficientSourceOrigin_or_PrimitiveFormulaFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP64_DYNAMIC_COEFFICIENT_SOURCE_ORIGIN_PINNED_PRIMITIVE_FORMULA_FRONTIER_OPEN"
NEXT = "MTT_Selected_PureWeylCoefficientRows_or_PrimitiveC1FormulaExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    source = load(SOURCE_PACKET)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")

    for item in [data, source, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    closed = source["closed_or_narrowed"]
    for key in [
        "direct_scalar_emission_tried",
        "primitive_candidate_values_emitted",
        "active_shift_1_1_selected",
        "fixed_fiber_quotient_selected",
        "current_C1_observable_layer_emitted",
        "current_C1_flavor_no_go_confirmed",
        "higher_order_algebraic_candidate_matrix_gate_closed",
        "second_order_required_rows_identified",
    ]:
        require(closed[key] is True, f"closed/narrowed flag missing: {key}")

    origin = source["where_numbers_can_come_from"]
    for forbidden in [
        "measured Yukawa/CKM/PMNS/Higgs values",
        "diagnostic profile coefficients",
        "current first-response scalar-permutation C1 layer",
        "absolute qutrit fiber origin as a hidden selector",
    ]:
        require(forbidden in origin["not_from"], f"forbidden origin missing: {forbidden}")
    require("lambda_static*Z on u,e" in origin["candidate_source"], "phase source missing")
    require("lambda_static*X on d,nuD" in origin["candidate_source"], "shift source missing")
    for row in [
        "selected zero-mode basis values",
        "selected finite Hessian C1 source blocks",
        "selected primitive C1 contractions",
        "pure Weyl coefficient rows lambda_Z and lambda_X",
    ]:
        require(row in origin["required_rows"], f"required row missing: {row}")

    counts = source["current_counts"]
    require(counts["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(counts["accepted_dynamic_payload_row_count"] == 0, "dynamic rows overaccepted")
    require(counts["second_order_coefficient_rows_emitted"] is False, "second-order rows overemitted")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    remains = cutset["still_open"]
    for key in [
        "selected_zero_mode_basis_values",
        "selected_finite_Hessian_C1_source_blocks",
        "primitive_C1_contractions",
        "pure_Weyl_coefficient_rows_lambda_Z_lambda_X",
        "selected_second_order_physical_matrix_promotion",
        "accepted_Yukawa_CKM_PMNS_RG_threshold_value_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    decision = data["closure_decision"]
    for key in [
        "dynamic_coefficient_source_origin_pinned",
        "current_C1_layer_flavor_no_go_confirmed",
        "higher_order_candidate_origin_identified",
        "second_order_required_rows_identified",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
        require(cert[key] is True, f"certificate close missing: {key}")
    for key in [
        "second_order_coefficient_rows_emitted",
        "accepted_value_layer_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "decision scalar rows overaccepted")
    require(cert["accepted_internal_scalar_row_count"] == 0, "certificate scalar rows overaccepted")

    for phrase in [
        "current C1 flavor no-go confirmed        : true",
        "second-order required rows identified    : true",
        "accepted internal scalar rows            : 0",
        "second-order coefficient rows emitted    : false",
        "phase correction : lambda_static * Z on u,e",
        "shift correction : lambda_static * X on d,nuD",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
