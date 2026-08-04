"""Audit Weyl-pair source emission or honest Galerkin C1 execution value-run gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
PROMOTION = PACKET_DIR / "weylpair_source_emission_promotion_attempt.packet.json"
VALUE_RUN = PACKET_DIR / "conditional_weylpair_value_run.packet.json"
HONEST = PACKET_DIR / "honest_galerkin_execution_value_run_gate.packet.json"
CERT = ROOT / "certificates" / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun.py"

STATUS = "MTT_SELECTED_WEYLPAIRSOURCEEMISSION_OR_HONESTGALERKINC1EXECUTION_VALUERUN_BUILT_PROMOTION_BLOCKED"
NEXT = "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    promotion = load(PROMOTION)
    value_run = load(VALUE_RUN)
    honest = load(HONEST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(promotion["status"] == "PROMOTION_BLOCKED_SOURCE_EMISSION_NOT_THEOREM_DERIVED", "promotion status mismatch")
    support = promotion["already_closed_support"]
    for key in [
        "source_selector_promoted",
        "source_level_weyl_carrier_proved",
        "active_shift_proved",
        "target_in_weylpair_span",
        "primitive_only_span_insufficient",
        "target_is_internal_diagnostic_not_observed_data",
    ]:
        require(support[key] is True, f"support flag missing: {key}")
    require(support["conditional_A_rank"] == 2, "conditional rank mismatch")
    missing = promotion["promotion_inputs_missing"]
    require(missing["A_selected_currently_emitted"] is False, "A_selected overemitted")
    require(missing["b_selected_currently_emitted"] is False, "b_selected overemitted")
    require(missing["least_squares_now_computable_for_selected_A"] is False, "least squares overclaimed")
    require(missing["rank_test_now_computable_for_selected_A"] is False, "rank test overclaimed")
    require(len(missing["missing_source_obligations"]) >= 4, "source obligations underreported")
    for key, value in promotion["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")
    require(promotion["observed_data_used"] is False, "promotion observed data used")
    require(promotion["target_fitting_used"] is False, "promotion target fitting used")

    require(value_run["status"] == "CONDITIONAL_VALUE_RUN_READY_NOT_PROMOTED", "value run status mismatch")
    require(value_run["operator_is_A_selected"] is False, "conditional operator overselected")
    require(value_run["rank"] == 2, "value run rank mismatch")
    require(abs(value_run["condition_number"] - 1.0) < 1e-9, "condition number mismatch")
    require(value_run["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(value_run["A_transpose_b_if_promoted"] == [12.0, 12.0], "ATb mismatch")
    require(value_run["deltaTheta_C1_if_promoted"] == [1.0, 1.0], "delta mismatch")
    require(value_run["SM_parity_dynamic_packet_would_close_if_promoted"] is True, "SM implication missing")
    require(value_run["no_knob_flavor_constants_would_close_if_promoted"] is False, "no-knob overclaim")
    require(value_run["selected_value_promotion_allowed_now"] is False, "value run overpromoted")
    require(value_run["observed_data_used"] is False, "value run observed data used")
    require(value_run["target_fitting_used"] is False, "value run target fitting used")

    require(honest["status"] == "HONEST_GALERKIN_EXECUTION_VALUES_STILL_OPEN", "honest status mismatch")
    require(honest["selected_source_verified"] is False, "honest source oververified")
    require(honest["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True, "honest SM implication missing")
    require(honest["would_close_no_knob_flavor_constants_if_values_emitted"] is False, "honest no-knob overclaim")
    require(honest["observed_flavor_data_forbidden"] is True, "honest observed data not forbidden")
    require(honest["target_fitting_forbidden"] is True, "honest target fitting not forbidden")

    closes = data["what_closes_now"]
    for key in [
        "primary_weylpair_route_attempted",
        "conditional_value_run_replayed",
        "promotion_blocker_reduced_to_source_emission_and_b_selected",
        "honest_Galerkin_execution_gate_reemitted",
        "observed_constants_excluded_as_selectors",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_phase_like_Z_or_basis_holonomy_source",
        "selected_shift_like_X_vertex_source",
        "same_branch_weyl_pair_source_provenance",
        "theorem_derived_A_selected",
        "theorem_derived_b_selected",
        "selected_deltaTheta_C1",
        "honest_selected_Galerkin_C1_execution_values",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")

    for key, value in data["promotion_decision"].items():
        require(value is False, f"candidate promotion overclaimed: {key}")
    for key in [
        "closure_claimed",
        "SM_parity_dynamic_packet_closure_claimed",
        "true_SM_equivalence_claimed",
        "no_knob_closure_claimed",
        "observed_data_used",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("conditional value run is ready" in note, "note missing conditional value run")
    require("No observed masses" in note, "note missing no-observed-data guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
