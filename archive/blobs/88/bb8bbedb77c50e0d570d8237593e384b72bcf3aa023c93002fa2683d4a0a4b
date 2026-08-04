"""Build full-loop precision import or Qa/SU3 operator-slot fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRECISION = PACKET_DIR / "precision_observable_table_full_loop_import_attempt.packet.json"
QASU3 = PACKET_DIR / "qasu3_operator_slot_fill_attempt.packet.json"
DECISION = PACKET_DIR / "promotion_decision_after_full_loop_or_slot_fill.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrecisionObservableTable_FullLoopImport_or_QaSU3OperatorSlotFill_v1.md"

STATUS = "MTT_SELECTED_PRECISIONOBSERVABLETABLE_FULLLOOPIMPORT_OR_QASU3OPERATORSLOTFILL_BUILT_PROXY_INVENTORY_SLOTS_OPEN"
NEXT = "MTT_Selected_AcceptedPrecisionProfileImport_or_SelectedQaSU3OperatorSlotSourceValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(
        DATA / "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt.candidate.json"
    )
    qcd_proxy = load(DATA / "selected_loopqcddecayproxyvalues_or_fullprecisionqft.candidate.json")
    n3lo_proxy = load(DATA / "selected_multiloophiggsqqformula_or_fullwidthpolicy.candidate.json")
    profile_controller = load(DATA / "selected_higgsacceptedprofileimport_or_rowvaluereplacement.candidate.json")
    remaining_ew = load(DATA / "selected_higgsremainingewformularows_or_precisiontotalwidth.candidate.json")
    qasu3_value_attempt = load(
        DATA
        / "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt"
        / "qasu3_hym_operator_packet_value_attempt.packet.json"
    )

    qasu3_slots = qasu3_value_attempt["operator_slot_attempt"]

    precision = {
        "schema": "MTTPrecisionObservableTableFullLoopImportAttempt.v1",
        "input_previous_value_attempt": rel(
            DATA / "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt.candidate.json"
        ),
        "support_inventory": {
            "first_loop_QCD_proxy_layer_closed": qcd_proxy["closure_decision"][
                "first_loop_QFT_proxy_layer_closed"
            ],
            "N3LO_QCD_proxy_values_for_Hbb_Hcc": n3lo_proxy["what_closes_now"][
                "N3LO_QCD_proxy_values_for_Hbb_Hcc"
            ],
            "qq_formula_scaffold_closed": n3lo_proxy["closure_decision"]["qq_formula_scaffold_closed"],
            "remaining_EW_formula_import_gate_built": remaining_ew["closure_decision"][
                "remaining_EW_gate_built"
            ],
            "profile_acceptance_controller_built": profile_controller["closure_decision"][
                "profile_acceptance_controller_built"
            ],
            "rehearsal_profile_structurally_valid": profile_controller["closure_decision"][
                "rehearsal_profile_structurally_valid"
            ],
        },
        "accepted_precision_import_status": {
            "accepted_profile_import": profile_controller["closure_decision"]["accepted_profile_import"],
            "accepted_row_replacements": profile_controller["closure_decision"]["accepted_row_replacements"],
            "precision_total_width_closed": (
                profile_controller["closure_decision"]["precision_total_width_closed"]
                or remaining_ew["closure_decision"]["precision_total_width_closed"]
            ),
            "precision_branching_ratios_closed": profile_controller["closure_decision"][
                "precision_branching_ratios_closed"
            ],
            "full_precision_QFT_values_closed": (
                qcd_proxy["closure_decision"]["full_precision_QFT_values_closed"]
                or n3lo_proxy["closure_decision"]["full_precision_QFT_values_closed"]
            ),
        },
        "full_loop_import_attempt_result": {
            "attempted": True,
            "accepted_precision_rows_imported_now": 0,
            "proxy_or_scaffold_rows_available": 4,
            "closed_now": False,
            "reason": (
                "The repo has QCD proxy layers, an N3LO qq scaffold, an EW import gate, and a profile "
                "acceptance controller. None is accepted as the full precision observable/profile table."
            ),
        },
        "remaining_required_precision_values": {
            "accepted_external_precision_profile_packet": profile_controller["what_remains_open"][
                "accepted_external_precision_profile_packet"
            ],
            "accepted_route_A_row_value_replacements": profile_controller["what_remains_open"][
                "accepted_route_A_row_value_replacements"
            ],
            "WW_star_formula_or_precision_import": remaining_ew["what_remains_open"][
                "WW_star_formula_or_precision_import"
            ],
            "ZZ_star_formula_or_precision_import": remaining_ew["what_remains_open"][
                "ZZ_star_formula_or_precision_import"
            ],
            "Z_gamma_formula_or_precision_import": remaining_ew["what_remains_open"][
                "Z_gamma_formula_or_precision_import"
            ],
            "full_ten_channel_covariance_profile": remaining_ew["what_remains_open"][
                "full_ten_channel_covariance_profile"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    qasu3 = {
        "schema": "MTTQaSU3OperatorSlotFillAttempt.v1",
        "input_qasu3_value_attempt": rel(
            DATA
            / "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt"
            / "qasu3_hym_operator_packet_value_attempt.packet.json"
        ),
        "slot_status": {
            "required_operator_slot_count": qasu3_slots["required_operator_slot_count"],
            "filled_operator_slot_count": qasu3_slots["filled_operator_slot_count"],
            "filled_slots": qasu3_slots["filled_slots"],
            "missing_slots": qasu3_slots["missing_slots"],
        },
        "slot_fill_attempt_result": {
            "attempted": True,
            "new_slots_filled_now": 0,
            "actual_selected_operator_payload_filled": qasu3_slots[
                "actual_selected_operator_payload_filled"
            ],
            "closed_now": False,
            "reason": (
                "No selected source values were emitted for the eight operator slots. Diagonal HYM support "
                "is useful support, but it is not a sector-ready selected Qa/SU3 operator packet."
            ),
        },
        "minimal_slot_source_values_to_emit": [
            "selected source status for L3-K2 or enlarged visible source",
            "standard lattice/base ordering and base-swap-breaking evidence",
            "Pic0 selection or physical quotient theorem",
            "same-source Chern-Weil row",
            "transition rho_E or Cech/Dolbeault/D_E data",
            "selected HYM or Route-C residual",
            "Riesz/Green/dotD/projector retention",
            "finite determinant, heat, spectrum, or torsion response",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTFullLoopImportOrQaSU3SlotFillPromotionDecision.v1",
        "status": "NO_PRECISION_IMPORT_NO_OPERATOR_SLOT_PROMOTION",
        "route_A_precision": {
            "proxy_inventory_built": True,
            "accepted_precision_table_closed": False,
            "accepted_precision_rows_imported_now": 0,
            "next_blocker": "accepted precision profile import or accepted route-A row replacements",
        },
        "route_B_operator": {
            "slot_manifest_built": True,
            "actual_QaSU3_operator_packet_closed": False,
            "new_slots_filled_now": 0,
            "next_blocker": "selected source values for the eight operator slots",
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrecisionObservableTableFullLoopImportOrQaSU3OperatorSlotFill",
        "status": STATUS,
        "inputs": {
            "previous_value_attempt": rel(
                DATA / "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt.candidate.json"
            ),
            "qcd_proxy": rel(DATA / "selected_loopqcddecayproxyvalues_or_fullprecisionqft.candidate.json"),
            "n3lo_qq_proxy": rel(DATA / "selected_multiloophiggsqqformula_or_fullwidthpolicy.candidate.json"),
            "profile_controller": rel(
                DATA / "selected_higgsacceptedprofileimport_or_rowvaluereplacement.candidate.json"
            ),
            "remaining_ew_gate": rel(
                DATA / "selected_higgsremainingewformularows_or_precisiontotalwidth.candidate.json"
            ),
        },
        "output_packets": {
            "precision_observable_table_full_loop_import_attempt": rel(PRECISION),
            "qasu3_operator_slot_fill_attempt": rel(QASU3),
            "promotion_decision_after_full_loop_or_slot_fill": rel(DECISION),
        },
        "theorem": {
            "name": "FullLoopImportOrQaSU3SlotFillAttemptTheorem",
            "proved": True,
            "statement": (
                "The current repo contains substantial Route A support values and gates: first-loop QCD "
                "proxy rows, an N3LO qq scaffold, an EW formula/import gate, and a profile acceptance "
                "controller. It also contains a Route B operator-slot manifest. The attempt does not "
                "promote true SM equivalence, because no accepted precision profile/table rows and no "
                "selected Qa/SU3 operator slot values are emitted."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "precision_proxy_inventory_built": True,
            "operator_slot_manifest_built": True,
            "accepted_precision_observable_table_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "precision_proxy_inventory_consolidated": True,
            "full_loop_import_attempt_executed": True,
            "qasu3_operator_slot_fill_attempt_executed": True,
            "eight_slot_operator_manifest_locked": True,
            "accepted_precision_vs_proxy_boundary_enforced": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "accepted_precision_profile_import": True,
            "accepted_route_A_row_value_replacements": True,
            "full_precision_observable_value_table": True,
            "actual_QaSU3_operator_packet": True,
            "selected_operator_slot_source_values": True,
            "sector_ready_HYM_Riesz_Green_dotD_C1_payload": True,
            "QM_GR_measurement_response_interfaces": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "previous_candidate_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PrecisionObservableTable_FullLoopImport_or_QaSU3OperatorSlotFill_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "accepted_precision_observable_table_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected PrecisionObservableTable FullLoopImport or QaSU3OperatorSlotFill v1

This artifact consolidates the current hard true-equivalence attempt.

Route A has proxy/support material: first-loop QCD Higgs decay proxies, an N3LO
qq scaffold, the remaining EW import gate, and the profile acceptance
controller.  No accepted precision observable/profile table row is imported.

Route B has the eight-slot Qa/SU3 operator manifest.  No selected operator slot
source value is emitted in this artifact.

So the checkpoint is useful but not a closure claim: it locks the proxy-vs-
precision boundary and the operator-slot fill boundary.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (PRECISION, precision),
        (QASU3, qasu3),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
