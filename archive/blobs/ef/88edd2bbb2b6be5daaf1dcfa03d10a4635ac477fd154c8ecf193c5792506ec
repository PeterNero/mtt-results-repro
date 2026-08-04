"""Audit cross-repo alpha1 driver replay import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
CERT = ROOT / "certificates" / "selected_crossrepo_alpha1_driver_replay_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CrossRepo_Alpha1DriverReplay_Import_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_crossrepo_alpha1_driver_replay_import.py"

STATUS = "MTT_SELECTED_CROSSREPO_ALPHA1_DRIVER_REPLAY_IMPORTED_PRIMITIVE_C1_OPEN"
NEXT = "MTT_Selected_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


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
    require(NEXT in note, "note does not record next artifact")

    scan = data["repo_scan"]
    for repo in [
        "mtt_protospinor_gr_response_proof",
        "mtt_q79_proof_repro",
        "mtt_nonsm_constants_no_knob",
        "mtt_qa_su3_packet_proof",
    ]:
        require(scan[repo]["useful_for_this_frontier"] is True, f"{repo} not marked useful")

    alpha = data["alpha1_driver_replay_import"]
    require(alpha["selected_N_alpha1_h_ext_value"] is True, "N_alpha1 value not imported")
    require(alpha["du_dalpha1_equals_h_ext"] is True, "du/dalpha1 import missing")
    require(alpha["selected_dotD_source_verified"] is True, "selected dotD source not imported")
    require(alpha["alpha1_driver_verified"] is True, "alpha1 driver not imported")
    require(alpha["honest_dotD_alpha1_replay"] is True, "honest dotD replay not imported")
    require(alpha["lambda_alpha1"] == 1.0, "lambda alpha1 mismatch")
    require(alpha["N_alpha1_h_ext"] == 1.0, "N alpha1 mismatch")
    require(alpha["tangent_residual_l2"] == 0.0, "tangent residual mismatch")
    require(any("PASS" in line for line in alpha["validator_output"]), "validator output lacks PASS")

    local = data["local_compatibility"]
    require(local["dotD_transport_formula_already_proved_locally"] is True, "local dotD theorem missing")
    require(local["local_source_only_failure_was_alpha1_driver"] is True, "local failure was not alpha1")
    require(
        local["primitive_fiber_quotient_already_closed_locally"] is True,
        "primitive fiber quotient was not retained",
    )
    require(local["active_shift_selected_by_current_repo"] is True, "active shift selector missing")
    require(local["absolute_fiber_shift_still_unselected"] is True, "absolute fiber overselected")
    require(local["shift0_is_computation_gauge_only"] is True, "shift0 promoted as physical selector")
    require(
        local["higher_order_full_response_criterion_already_locked"] is True,
        "higher-order/full-response criterion was not retained",
    )
    require(local["current_layer_flavor_splitting_possible"] is False, "current C1 layer incorrectly split")
    require(local["previous_typed_value_alpha1_open"] is True, "previous alpha1 was not open")
    require(local["primitive_candidates_already_emitted"] is True, "primitive candidates missing")
    require(local["conditional_A_still_not_selected"] is True, "conditional A overpromoted")
    require(local["b_selected_still_not_selected"] is True, "b_selected overpromoted")

    frontier = data["frontier_update"]
    require(frontier["alpha1_driver_no_longer_primary_blocker"] is True, "alpha1 still marked primary")
    require(frontier["selected_dotD_replay_available_by_import"] is True, "dotD replay not available")
    require(frontier["fiberclass_quotient_already_selected_locally"] is True, "fiber quotient not retained")
    require(
        frontier["absolute_fiber_origin_not_active_blocker_for_current_observables"] is True,
        "absolute fiber origin still marked active blocker",
    )
    require(frontier["next_frontier"] == NEXT, "frontier mismatch")

    require(data["closure_claimed"] is False, "full closure overclaimed")
    require(data["alpha1_driver_verified_imported"] is True, "alpha1 import flag missing")
    require(data["selected_dotD_source_verified_imported"] is True, "dotD import flag missing")
    require(data["A_selected_claimed"] is False, "A_selected overclaimed")
    require(data["b_selected_claimed"] is False, "b_selected overclaimed")
    require(data["primitive_C1_contractions_claimed"] is False, "primitive contractions overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not marked proved")
    require(cert["theorem_proved"] is True, "certificate theorem not marked proved")

    remains = data["what_remains_open"]
    for key in [
        "selected_primitive_class_C1_observable_emission",
        "absolute_fiber_origin_source_theorem",
        "selected_primitive_C1_contractions",
        "selected_higher_order_or_full_response_matrices",
        "selected_b_selected",
        "promote_conditional_A_to_A_selected",
        "honest_selected_deltaTheta_C1_solve",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
