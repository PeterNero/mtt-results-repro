"""Audit primitive-class C1 observable / higher-order response frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
CERT = ROOT / "certificates" / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.py"

STATUS = "MTT_SELECTED_PRIMITIVECLASS_C1OBSERVABLE_OR_HIGHERORDER_FULLRESPONSE_SOURCEEMISSION_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_WeylPairSectorRouting_SourceEmission_v1"


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
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    strategy = data["superset_strategy"]
    require(strategy["mode"] == "COMBINED_PATHS_WITH_LOCKED_TARGET", "wrong superset mode")
    require(strategy["observed_data_used"] is False, "observed data used")
    require(strategy["target_fitting_used"] is False, "target fitting used")

    observable = data["primitive_class_C1_observable_packet"]
    require(observable["active_shift"] == [1, 1], "active shift mismatch")
    require(observable["fixed_fiber_quotient_class"] == [0, 1, 2], "fiber class mismatch")
    require(observable["computation_representative"] == "fiber_shift_0", "representative mismatch")
    require(observable["representative_is_physical_selector"] is False, "representative overpromoted")
    require(observable["absolute_fiber_shift_selected"] is False, "absolute fiber overselected")
    require(observable["all_representatives_scalar_identity"] is True, "not scalar identity")
    require(observable["all_representatives_same_scalar"] is True, "not same scalar")
    require(observable["flavor_splitting_possible_at_current_layer"] is False, "flavor overclaimed")

    emission = data["higherorder_or_fullresponse_source_emission_packet"]
    require(emission["alpha1_dotD_status"]["active_blocker"] is False, "alpha1 still active")
    require(emission["alpha1_dotD_status"]["alpha1_driver_verified_imported"] is True, "alpha1 not imported")
    require(emission["alpha1_dotD_status"]["selected_dotD_source_verified_imported"] is True, "dotD not imported")
    require(emission["current_layer_status"]["no_go_proved"] is True, "no-go missing")
    require(emission["current_layer_status"]["higher_order_criterion_proved"] is True, "higher criterion missing")
    require(emission["current_layer_status"]["full_response_criterion_proved"] is True, "full criterion missing")
    require(emission["current_layer_status"]["current_values_available"] is False, "values overclaimed")
    require(emission["source_emission_status"]["diagnostic_splitter_found"] is True, "diagnostic splitter missing")
    require(emission["source_emission_status"]["selected_source_emits_splitter"] is False, "splitter overpromoted")
    require(emission["source_emission_status"]["source_emission_contract_built"] is True, "contract missing")
    require(emission["deltaTheta_gate_status"]["delta_solve_gate_built"] is True, "delta gate missing")
    require(emission["deltaTheta_gate_status"]["A_selected_claimed"] is False, "A_selected overclaimed")
    require(emission["deltaTheta_gate_status"]["b_selected_claimed"] is False, "b_selected overclaimed")
    require(emission["deltaTheta_gate_status"]["rank_tests_allowed_now"] is False, "rank tests overenabled")

    promotion = data["promotion_decision"]
    require(promotion["current_primitive_class_promoted_as_valid_C1_observable_layer"] is True, "observable not promoted")
    require(promotion["current_primitive_class_promoted_as_flavor_closure"] is False, "flavor closure overclaimed")
    require(promotion["alpha1_dotD_promoted_by_crossrepo_import"] is True, "alpha1 import not promoted")
    require(promotion["higherorder_fullresponse_values_promoted"] is False, "higher values overpromoted")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["A_selected_claimed"] is False, "A_selected overclaimed")
    require(data["b_selected_claimed"] is False, "b_selected overclaimed")
    require(data["selected_values_available"] is False, "selected values overclaimed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    remains = data["what_remains_open"]
    for key in [
        "selected_higher_order_or_full_response_matrices",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1_solution",
        "sector_response_matrices_M_u_M_d_M_e_M_nuD",
        "CKM_PMNS_CP_from_selected_matrices",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
