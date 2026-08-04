"""Audit F_K action-functional attempt and empirical K import boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_kthresholdfunctionalfromhymthresholdaction_or_controlledempiricalkimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INVENTORY = PACKET_DIR / "hym_threshold_action_source_inventory.packet.json"
ATTEMPT = PACKET_DIR / "fk_action_functional_attempt.packet.json"
NOGO = PACKET_DIR / "action_rank_insufficiency_nogo.packet.json"
EMPIRICAL_DECISION = PACKET_DIR / "controlled_empirical_k_import_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_fk_action_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_KThresholdFunctionalFromHYMThresholdAction_or_ControlledEmpiricalKImport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_KTHRESHOLDFUNCTIONALFROMHYMTHRESHOLDACTION_OR_CONTROLLEDEMPIRICALKIMPORT_"
    "BUILT_ACTION_SOURCE_TEST_NO_INTERNAL_FK_ROWS"
)
NEXT = "MTT_Selected_PhysicalDotDAlpha1SectorTransferRetardedOverlapKernel_or_EmpiricalKParityImport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    inventory = load(INVENTORY)
    attempt = load(ATTEMPT)
    nogo = load(NOGO)
    empirical = load(EMPIRICAL_DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("inventory", inventory),
        ("attempt", attempt),
        ("nogo", nogo),
        ("empirical decision", empirical),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "certificate true SM overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "certificate full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["selected_HYM_threshold_action_inventory_built"] is True, "inventory not built")
    require(decision["FK_action_functional_attempted"] is True, "F_K not attempted")
    require(decision["selected_FK_functional_proved"] is False, "F_K overproved")
    require(decision["action_rank_insufficiency_nogo_proved"] is True, "rank no-go missing")
    require(decision["accepted_selected_K_source_row_count"] == 0, "K rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["lambda_H_value_row_emitted"] is False, "lambda_H overemitted")
    require(decision["controlled_empirical_K_import_available"] is True, "empirical K import unavailable")
    require(
        decision["controlled_empirical_K_import_selected_for_no_knob"] is False,
        "empirical K imported as no-knob",
    )
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob closure overclaimed")

    require(
        inventory["status"] == "SELECTED_DIAGONAL_HYM_ACTION_AVAILABLE_FULL_FK_SOURCE_NOT_AVAILABLE",
        "inventory status mismatch",
    )
    for key in [
        "closed_K_grammar_rows",
        "conditional_K_to_Omega_theorem",
        "diagonal_expS_HYM_replay_solved",
        "selected_A_HYM_payload_emitted",
        "full_diagonal_End0_Green_closed",
        "overlap_quadrature_functional_defined",
        "threshold_scheme_source_gate_built",
    ]:
        require(inventory["closed_source_inputs"][key] is True, f"closed source input missing {key}")
    for key in [
        "selected_projector_values_promoted",
        "selected_physical_dotD_alpha1",
        "selected_retarded_overlap_derivative_rows_emitted",
        "selected_threshold_response_functional_instantiated",
        "generation_resolved_threshold_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
    ]:
        require(inventory["open_source_inputs"][key] is False, f"open input overclaimed {key}")
    require(inventory["selected_numerical_FK_functional_present"] is False, "inventory overaccepted F_K")
    require(inventory["selected_action_payload_summaries"]["hym_final_residual_l2"] < 1e-9, "HYM residual too large")
    require(inventory["selected_action_payload_summaries"]["current_rowlocal_distinct_model_active_L_values"] == 1, "degeneracy changed")

    require(attempt["status"] == "ACTION_FUNCTIONAL_TESTED_NO_SELECTED_NUMERICAL_FK_ROWS", "attempt status mismatch")
    require(attempt["candidate_functional"]["proved_now"] is False, "attempt overproved F_K")
    require(attempt["row_count"] == 10, "attempt row count mismatch")
    require(attempt["accepted_selected_K_source_row_count"] == 0, "attempt overaccepted K rows")
    require(attempt["accepted_internal_scalar_value_row_count"] == 0, "attempt overaccepted scalar rows")
    require(attempt["lambda_H_value_row_emitted"] is False, "attempt emitted lambda_H")
    require(attempt["controlled_empirical_K_import_selected_for_no_knob"] is False, "attempt promoted empirical K")
    require(attempt["controlled_empirical_K_rows_available"] == 10, "empirical K count mismatch")
    for row in attempt["attempt_rows"]:
        require(row["selected_FK_value_emitted"] is False, f"{row['omega_id']} F_K overemitted")
        require(row["emitted_K_threshold_value"] is None, f"{row['omega_id']} K value emitted")
        require(row["accepted_as_no_knob_source_row"] is False, f"{row['omega_id']} no-knob overaccepted")
        require(row["accepted_as_controlled_empirical_row"] is True, f"{row['omega_id']} empirical row missing")
        require(row["empirical_K_import_available"] is True, f"{row['omega_id']} empirical K unavailable")
        require(row["observed_data_used_as_selector"] is False, f"{row['omega_id']} observed selector")
        require(row["target_fitting_used"] is False, f"{row['omega_id']} target fitting")
        require(
            "empirical K row may be replayed only as controlled parity import" in row["blocking_reasons"],
            f"{row['omega_id']} missing empirical guard",
        )

    require(nogo["theorem"]["proved"] is True, "rank no-go theorem missing")
    require(nogo["required_selected_K_row_count"] == 10, "required K count mismatch")
    require(nogo["accepted_selected_K_source_row_count"] == 0, "rank no-go overaccepted K")
    require(nogo["selected_action_class_upper_bound"] == 2, "action class upper bound changed")
    require(nogo["rank_sufficient_for_ten_K_rows"] is False, "rank sufficiency overclaimed")
    require(nogo["current_model_active_degeneracy_nogo_imported"] is True, "prior degeneracy no-go not imported")
    require(nogo["current_source_degeneracy_details"]["charged_basis_degenerate"] is True, "charged degeneracy not preserved")

    require(
        empirical["status"] == "CONTROLLED_EMPIRICAL_K_IMPORT_AVAILABLE_FOR_PARITY_NOT_NO_KNOB",
        "empirical status mismatch",
    )
    require(empirical["empirical_K_row_count"] == 10, "empirical row count mismatch")
    require(empirical["can_replay_ten_scalar_slots_under_empirical_layer"] is True, "empirical replay unavailable")
    require(empirical["selected_for_no_knob_closure"] is False, "empirical no-knob overclaim")
    require(empirical["selected_for_true_SM_equivalence"] is False, "empirical true SM overclaim")
    require(empirical["allowed_use"] == "controlled parity replay/postcheck only", "empirical allowed use mismatch")
    for phrase in [
        "define F_K by empirical residual lookup",
        "promote empirical K rows as selected source rows",
        "claim no-knob scalar closure from imported K values",
    ]:
        require(phrase in empirical["forbidden_use"], f"empirical forbidden use missing {phrase}")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "selected HYM/threshold-action source inventory assembled for F_K",
        "current action functional attempt executed against all ten K rows",
        "rank/separation no-go proved for current selected action data",
        "controlled empirical K import decision typed as parity-only and non-no-knob",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed_here missing {phrase}")
    for phrase in [
        "selected physical dotD_alpha1 and sector-transfer functor",
        "selected retarded overlap derivative row kernel",
        "selected threshold-scheme rows T_scheme.*",
        "selected lambda_H H-sector value/quartic payload",
        "ten selected K_threshold rows",
    ]:
        require(phrase in cutset["still_open"], f"cutset still_open missing {phrase}")
    for phrase in [
        "use empirical K import as F_K",
        "reuse theta/D_fin factors after they have already been factored out of K",
        "promote model-active projectors without selected source flags",
    ]:
        require(phrase in cutset["forbidden_routes"], f"cutset forbidden route missing {phrase}")

    for phrase in [
        "F_K action-functional attempt            : executed",
        "current action rank no-go                : true",
        "selected numerical F_K functional        : false",
        "accepted selected K rows                 : 0",
        "empirical K selected for no-knob         : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
