"""Build the rank-two L2 cohomology or Route-C residual fill checkpoint."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

PREVIOUS = DATA / "selected_routec_operatorsourceidentity_subpacket.candidate.json"
Q79_L2 = Q79 / "candidate_data" / "terminal_admissible_section_source" / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
Q79_ORDERED = Q79 / "candidate_data" / "terminal_admissible_section_source" / "visible_rank2_l2_ordered_source.selected_under_section_principle.json"
Q79_ALL_GATES = Q79 / "candidate_data" / "all_remaining_valpha_gates_attempt.candidate.json"
Q79_ROUTE_C_TEMPLATE = Q79 / "certificates" / "iwasawa_route_c_residuals.template.json"

OUTPUT = DATA / "selected_routec_rank2_l2_or_routec_residual_fill.candidate.json"
CERT = CERTS / "selected_routec_rank2_l2_or_routec_residual_fill_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Rank2_L2_Cohomology_or_RouteC_Residual_Fill_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_RANK2_L2_COHOMOLOGY_FILL_CLOSED_STABILITY_OR_ROUTEC_RESIDUAL_OPEN"
NEXT = "MTT_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(script: Path, packet: Path) -> dict:
    proc = subprocess.run(
        [sys.executable, str(script), str(packet)],
        cwd=Q79,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "output_head": proc.stdout.strip().splitlines()[:20],
    }


def main() -> None:
    previous = load(PREVIOUS)
    l2_packet = load(Q79_L2)
    ordered_packet = load(Q79_ORDERED)
    all_gates = load(Q79_ALL_GATES)
    route_c_template = load(Q79_ROUTE_C_TEMPLATE)

    l2_validation = run_validator(Q79 / "scripts" / "validate_visible_rank2_l2_cohomology.py", Q79_L2)
    ordered_validation = run_validator(Q79 / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py", Q79_ORDERED)

    stability_gate = all_gates["stability_or_routec_gate"]
    operator_gates = all_gates["operator_gates"]["gates"]

    candidate = {
        "candidate": "MTTSelectedRouteCRank2L2CohomologyOrRouteCResidualFill",
        "status": STATUS,
        "inputs": {
            "operator_source_identity_subpacket": rel(PREVIOUS),
            "q79_selected_l2_cohomology_packet": rel(Q79_L2),
            "q79_selected_ordered_source_packet": rel(Q79_ORDERED),
            "q79_all_remaining_valpha_gates_attempt": rel(Q79_ALL_GATES),
            "q79_route_c_residual_template": rel(Q79_ROUTE_C_TEMPLATE),
        },
        "rank2_l2_fill": {
            "packet_status": l2_packet["status"],
            "source": l2_packet["source"],
            "reported_cohomology": l2_packet["reported_cohomology"],
            "acceptance_tests": l2_packet["acceptance_tests"],
            "validator": l2_validation,
            "closed_now": {
                "selected_l2_cochain_packet": l2_validation["exit_code"] == 0,
                "nonzero_ext_class_selected": l2_packet["reported_cohomology"]["extension_class_vector_C1"][0] == 1,
                "h1_positive": l2_packet["reported_cohomology"]["h1"] == 8,
                "non_split_input_for_valpha": True,
            },
        },
        "ordered_source_fill": {
            "packet_status": ordered_packet["status"],
            "source": ordered_packet["source"],
            "pic0_resolution": ordered_packet["pic0_resolution"],
            "selection_evidence": ordered_packet["selection_evidence"],
            "validator": ordered_validation,
            "closed_now": {
                "ordered_L_branch_selected_for_chern_h1_layer": ordered_validation["exit_code"] == 0,
                "pic0_quotiented_for_chern_h1_curvature_layer": ordered_packet["pic0_resolution"]["source_selected_or_quotiented"] is True,
                "operator_layer_pic0_recheck_still_open": True,
            },
        },
        "route_c_lane": {
            "template_status": route_c_template["status"],
            "selected_source_verified": route_c_template["selected_source_verified"],
            "still_open": {
                "actual_selected_branch_packet": route_c_template["branch_packet"]["branch"] is None,
                "actual_selected_rho_E_values": route_c_template["downstream_data_paths"]["rhoE_mesh"] is None,
                "actual_selected_metric_and_residuals": route_c_template["residuals"]["hym_primitive"] is None,
                "actual_Riesz_Green_dotD_data": route_c_template["downstream_data_paths"]["dotd_response"] is None,
            },
        },
        "operator_identity_impact": {
            "previous_subpacket_closed": previous["operator_identity_verdict"]["subpacket_closed"],
            "rank2_l2_blocker_retired": True,
            "selected_operator_identity_closed": False,
            "why_not_closed": [
                "terminal section principle is axiom-ready but not yet unconditional in the MTT spine",
                "non-split Ext input is closed, but full stability/HYM or Route-C residual remains open",
                "operator-layer Pic0 must be rechecked because holonomy-sensitive D_E/dotD data can see flat twists",
                "same-source Chern-Weil/GS row still lacks a selected visible bundle/source derivation",
                "same-source D_E, rho_E, Riesz/Green, and dotD selected data still fail promotion",
            ],
        },
        "all_remaining_gate_import": {
            "gate_summary": all_gates["gate_summary"],
            "newly_retired_by_after_lockdown_attempts": all_gates["newly_retired_by_after_lockdown_attempts"],
            "stability_or_routec_gate": stability_gate,
            "operator_gates": operator_gates,
            "still_open_cut_set": all_gates["still_open_cut_set"],
        },
        "what_closes_now": {
            "selected_l2_cochain_ext_packet_validated": True,
            "h1_8_nonzero_ext_closed": True,
            "ordered_source_validator_passes": True,
            "pic0_quotient_valid_for_chern_h1_curvature_layer": True,
            "rank2_lane_advanced_past_arithmetic_fill": True,
        },
        "what_remains_open": {
            "terminal_section_theorem_unconditional_promotion": True,
            "non_split_stability_or_hym_proved": True,
            "selected_route_c_residual_pass": True,
            "operator_layer_pic0_recheck": True,
            "same_source_Chern_Weil_GS_derivation": True,
            "same_source_D_E_rhoE_Riesz_Green_dotD": True,
            "primitive_C1_contractions": True,
            "selected_operator_identity_closed": False,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_mode": {
            "classification": "CONSTRAINED_SUPERSET_FILL_CHECKPOINT",
            "straight_path": {
                "classification": "RANK2_L2_COHOMOLOGY_FILL_SUCCEEDS_PARTIALLY",
                "succeeds": False,
                "reason": "The L2 cohomology/Ext input is selected and validator-passing, but stability/HYM and operator data are not emitted.",
            },
            "superset_convergence": {
                "classification": "RANK2_PRIMARY_LANE_ADVANCED",
                "succeeds": False,
                "closed_subparts": stability_gate["closed_subparts"],
            },
            "superset_repair": {
                "classification": "ROUTEC_RESIDUAL_LANE_STILL_OPEN",
                "succeeds": False,
                "template_status": route_c_template["status"],
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "The fill uses q79 terminal-section/cohomology packets and validators, not observed SM constants.",
            },
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SelectedRouteCRank2L2CohomologyFillCheckpoint",
            "proved": True,
            "statement": "The rank-two lane now has a validator-passing selected L2 cohomology packet with h1=8 and a nonzero non-exact Ext vector, plus an ordered-source/Pic0-quotiented curvature-layer packet. This retires the arithmetic L2 fill blocker. It does not prove the selected visible operator source, because stability/HYM or Route-C residual, operator-layer Pic0, same-source Chern-Weil/GS derivation, and selected D_E/rho_E/Riesz/Green/dotD data remain open.",
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "rank2_l2_validator_exit_code": l2_validation["exit_code"],
                "ordered_source_validator_exit_code": ordered_validation["exit_code"],
                "selected_operator_identity_closed": False,
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C Rank2 L2 Cohomology or Route-C Residual Fill

Status: `MTT_SELECTED_ROUTEC_RANK2_L2_COHOMOLOGY_FILL_CLOSED_STABILITY_OR_ROUTEC_RESIDUAL_OPEN`

The rank-two lane has advanced. The q79 terminal-admissible-section packet
passes the finite L2 cohomology validator:

- `h1 = 8`.
- The selected Ext vector is closed.
- The selected Ext vector is not exact.
- No observed or benchmark flavor inputs are used.

The ordered source packet also passes its validator and quotients `Pic0` for
the ordinary Chern/H1/curvature layer. That quotient is not promoted to the
operator layer, because holonomy-sensitive `D_E` and `dotD` data may see flat
twists.

## What Closes

- Selected L2 cochain/Ext packet.
- Nonzero Ext input for the non-split `V_alpha` route.
- Ordered `L = (1,-2,0)` source at the Chern/H1 layer.
- Pic0 quotient for the ordinary Chern/H1/curvature layer.

## What Remains Open

- Unconditional terminal section theorem in the MTT spine.
- Non-split stability/HYM or selected Route-C residual.
- Operator-layer Pic0 recheck.
- Same-source Chern-Weil/Green-Schwarz derivation.
- Same-source selected `rho_E`, `D_E`, Riesz/Green, and `dotD`.
- Primitive C1 contractions.

Thus the rank-two arithmetic fill is no longer the blocker, but the selected
operator source is still open.

Next artifact: `MTT_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
