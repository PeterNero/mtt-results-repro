"""Audit Step72 row-local prefactor law search / strict Omega gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ACCEPTANCE_PACKET = PACKET_DIR / "step72_strict_rowlocal_omega_acceptance_predicate.packet.json"
TRIAL_PACKET = PACKET_DIR / "step72_source_only_candidate_law_trials.packet.json"
TARGET_PACKET = PACKET_DIR / "step72_required_rowlocal_prefactor_target_table.packet.json"
KNOB_PACKET = PACKET_DIR / "step72_minimal_knob_diagnostic.packet.json"
WORKORDER_PACKET = PACKET_DIR / "step72_honest_galerkin_rowlocal_workorder.packet.json"
CUTSET_PACKET = PACKET_DIR / "step72_next_rowlocal_galerkin_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step72_RowLocalPrefactorLawSearch_or_StrictOmegaAcceptance_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP72_ROWLOCAL_PREFACTOR_LAW_SEARCH_BUILT_STRICT_OMEGA_STILL_OPEN"
NEXT = "MTT_Selected_HonestRowLocalHYMGalerkinExecution_or_SelectedPrefactorSourceRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    acceptance = load(ACCEPTANCE_PACKET)
    trials = load(TRIAL_PACKET)
    targets = load(TARGET_PACKET)
    knobs = load(KNOB_PACKET)
    workorder = load(WORKORDER_PACKET)
    cutset = load(CUTSET_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    for item in [data, acceptance, trials, targets, knobs, workorder, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    predicate = acceptance["strict_acceptance_predicate"]
    for key in [
        "same_branch_selected_before_replay",
        "ten_rowlocal_overlap_rows_required",
        "ten_threshold_scheme_rows_or_single_selected_scheme_theorem_required",
        "lambda_H_value_payload_required",
        "observed_replay_matrix_may_be_used_only_after_source_selection",
        "ckm_down_sector_offdiagonal_matrix_is_separate_from_scalar_prefactor_gate",
    ]:
        require(predicate[key] is True, f"predicate missing {key}")
    strict = acceptance["strict_acceptance_result"]
    require(strict["accepted_rowlocal_source_row_count"] == 0, "rowlocal rows overaccepted")
    require(strict["accepted_threshold_scheme_row_count"] == 0, "threshold rows overaccepted")
    require(strict["accepted_full_prefactor_source_row_count"] == 0, "prefactors overaccepted")
    require(strict["accepted_omega_source_row_count"] == 0, "Omega rows overaccepted")
    require(strict["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(strict["value_rows_execute"] is False, "values executed early")

    require(targets["target_row_count"] == 10, "target row count mismatch")
    require(targets["accepted_source_row_count"] == 0, "target rows overaccepted")
    require(targets["family_prefactor_span"] > 10.0, "family span should expose row-local need")
    require(targets["all_targets_inside_order_one_window_0p1_to_10"] is True, "targets should be order one")
    omega_set = {row["omega_id"] for row in targets["target_rows"]}
    require(omega_set == {
        "Omega_u.gen1",
        "Omega_u.gen2",
        "Omega_u.gen3",
        "Omega_d.gen1",
        "Omega_d.gen2",
        "Omega_d.gen3",
        "Omega_e.gen1",
        "Omega_e.gen2",
        "Omega_e.gen3",
        "Omega_H.lambda",
    }, "Omega set mismatch")
    for row in targets["target_rows"]:
        require(row["accepted_as_source_row"] is False, f"target overaccepted {row['omega_id']}")
        require("/ D_fin." in row["rowlocal_composite_target_symbolic"], "target missing D_fin symbol")
        require(row["source_value_tier"] == "admitted_replay_postcheck_only", "target tier mismatch")

    require(trials["accepted_source_law_count"] == 0, "candidate law overaccepted")
    require(trials["strict_omega_acceptance_from_trials"] is False, "trials overclosed Omega")
    require(trials["replay_matrix_exact_but_forbidden"] is True, "replay shortcut not rejected")
    by_id = {row["trial_id"]: row for row in trials["candidate_law_trials"]}
    require(by_id["source_class_only_heat_torsion"]["source_only_without_replay_fit"] is True, "source-only trial flag missing")
    require(
        by_id["source_class_only_heat_torsion"]["fit"]["parameter_count"] == 2,
        "source-only trial should have two classes",
    )
    require(
        by_id["source_class_only_heat_torsion"]["fit"]["max_multiplicative_error_factor"] > 2.0,
        "source-only trial should fail diagnostically",
    )
    require(
        by_id["smparity_replay_exact_10_row_import"]["uses_replay_values_if_promoted"] is True,
        "replay import flag missing",
    )
    require(
        by_id["smparity_replay_exact_10_row_import"]["accepted_as_selected_source_law"] is False,
        "replay import overaccepted",
    )

    require(knobs["accepted_minimal_knob_count"] == 0, "minimal knobs overaccepted")
    require(knobs["policy"]["one_to_three_universal_parameters_can_be_scientifically_credible"] is True, "knob policy missing")
    require(knobs["policy"]["ordinary_fit_parameters_forbidden"] is True, "ordinary knobs not forbidden")
    require(knobs["policy"]["must_be_selected_before_observed_replay"] is True, "pre-replay selection missing")
    for model in knobs["diagnostic_models"]:
        require(model["accepted_as_selected_knob_policy"] is False, f"knob model overaccepted {model['model_id']}")
    three = {model["model_id"]: model for model in knobs["diagnostic_models"]}["three_family_sectors_only"]
    require(three["uncovered_row_count"] == 1, "three-sector diagnostic should leave lambda_H uncovered")

    require(workorder["status"] == "HONEST_ROWLOCAL_HYM_GALERKIN_EXECUTION_SPECIFIED", "workorder status mismatch")
    require(len(workorder["output_rows_required"]) == 10, "workorder row count mismatch")
    for phrase in [
        "selected q79/F/m=1 finite HYM/Strominger operator",
        "ordered zero-mode bases for every Omega slot",
        "retarded overlap kernel derivative on the same branch",
        "threshold/scale/scheme convention selected before replay",
    ]:
        require(phrase in workorder["required_source_inputs"], f"workorder missing {phrase}")
    for phrase in [
        "emit ten rows before reading the SM-parity replay magnitudes",
        "reject any row whose numeric value is obtained by solving against replay targets",
    ]:
        require(phrase in workorder["acceptance_tests"], f"acceptance test missing {phrase}")

    for phrase in [
        "actual selected row-local Galerkin matrix elements L_rowlocal.*",
        "actual selected threshold/scale/scheme rows T_scheme.*",
        "lambda_H H-sector source value payload",
        "strict Omega acceptance after row emission",
        "separate selected CKM/down-sector offdiagonal matrix theorem",
    ]:
        require(phrase in cutset["still_missing"], f"cutset missing {phrase}")
    for phrase in [
        "reuse the SM-parity replay matrix as source values",
        "fit one to three knobs to the replay magnitudes and call them selected",
        "claim diagonal scalar closure derives CKM/offdiagonal content",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing {phrase}")

    decision = data["closure_decision"]
    for key in [
        "strict_rowlocal_acceptance_predicate_closed",
        "source_only_candidate_law_search_closed",
        "smparity_replay_matrix_as_source_rejected",
        "diagnostic_target_table_emitted",
        "minimal_knob_diagnostic_boundary_closed",
        "honest_galerkin_workorder_emitted",
    ]:
        require(decision[key] is True, f"decision did not close {key}")
        require(cert[key] is True, f"certificate did not close {key}")
    for key in [
        "strict_omega_acceptance_closed",
        "lambda_H_value_row_emitted",
        "selected_ckm_offdiagonal_matrix_derived",
        "scalar_value_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")
    for key in [
        "accepted_source_law_count",
        "accepted_rowlocal_source_row_count",
        "accepted_threshold_scheme_row_count",
        "accepted_full_prefactor_source_row_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(decision[key] == 0, f"decision overaccepted {key}")
        require(cert[key] == 0, f"certificate overaccepted {key}")

    for phrase in [
        "strict Omega acceptance closed : False",
        "The earlier matrix is still valuable",
        "postcheck-only",
        "Y_d offdiag/frob",
        "honest same-branch Galerkin/HYM row-local",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
