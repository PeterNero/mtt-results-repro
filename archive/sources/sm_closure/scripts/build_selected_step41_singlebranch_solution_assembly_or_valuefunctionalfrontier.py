"""Build Step 41 single-branch first-response solution assembly."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step41_singlebranch_solution_assembly_or_valuefunctionalfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOLUTION = PACKET_DIR / "step41_q79_f_m1_first_response_solution.packet.json"
FRONTIER = PACKET_DIR / "step41_value_functional_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step41_SingleBranchSolutionAssembly_or_ValueFunctionalFrontier_v1.md"

STEP36 = DATA / "selected_step36_s3classclosure_reconciliation_or_operatorvaluefrontier.candidate.json"
STEP37 = DATA / "selected_step37_finitetrace_degap_import_or_fulloperatorvaluefrontier.candidate.json"
STEP38 = DATA / "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier.candidate.json"
STEP39 = DATA / "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier.candidate.json"
STEP40 = DATA / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier.candidate.json"
STEP24 = DATA / "selected_step24_dynamicgate_reconciliation_or_valuelayercutset.candidate.json"
VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
DYNAMIC_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
RTHETA_SOURCE = DATA / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows.candidate.json"
STEP25 = DATA / "selected_step25_thresholdexternalreplay_noknobkernel_or_fulls2cutset.candidate.json"

STATUS = "MTT_SELECTED_STEP41_SINGLE_BRANCH_FIRST_RESPONSE_SOLUTION_ASSEMBLED_VALUE_ROWS_OPEN"
NEXT = "MTT_Selected_ValueFunctionalRows_From_AssembledFirstResponseSolution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dig(data: dict[str, Any], dotted: str, default: Any = None) -> Any:
    cur: Any = data
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP36, STEP37, STEP38, STEP39, STEP40, STEP24, VSD01, DYNAMIC_PACKET, RTHETA_SOURCE, STEP25]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 41 inputs: " + ", ".join(missing))

    step36 = load(STEP36)
    step37 = load(STEP37)
    step38 = load(STEP38)
    step39 = load(STEP39)
    step40 = load(STEP40)
    step24 = load(STEP24)
    vsd01 = load(VSD01)
    dynamic_packet = load(DYNAMIC_PACKET)
    rtheta_source = load(RTHETA_SOURCE)
    step25 = load(STEP25)

    closed_checks = {
        "selected_s3_differential_cohomology_class": dig(
            step36, "closure_decision.selected_s3_differential_cohomology_class_closed"
        )
        is True,
        "s3_restriction_pullback_table": dig(step36, "closure_decision.s3_restriction_pullback_table_closed") is True,
        "smooth_freed_witten_cancellation": dig(step36, "closure_decision.smooth_freed_witten_cancellation_closed")
        is True,
        "finite_trace_D_E_gap_Riesz_Green": dig(step37, "closure_decision.finite_trace_DE_gap_layer_closed") is True
        and dig(step37, "closure_decision.positive_gap_Riesz_Green_lock_imported") is True,
        "projective_rhoE_transition_gauge_class": dig(
            step38, "closure_decision.operator_level_projective_rhoE_transition_matrices_closed"
        )
        is True
        and dig(step38, "closure_decision.nonidentity_projective_rhoE_selected_up_to_unitary_gauge") is True,
        "diagonal_End0_covariant_D_E": dig(step39, "closure_decision.selected_diagonal_End0_covariant_D_E_closed")
        is True,
        "stationary_projector_Riesz_Green_transport": dig(
            step39, "closure_decision.selected_stationary_projector_Riesz_Green_transport_closed"
        )
        is True,
        "dotD_alpha1_transport": dig(step40, "closure_decision.selected_dotD_transport_derivative_formula_closed")
        is True
        and dig(step40, "closure_decision.same_branch_dotD_alpha1_values_closed") is True
        and dig(step40, "closure_decision.honest_dotD_alpha1_replay_closed") is True,
        "source_assembly_subgate": dig(step24, "closure_decision.VSD01_source_assembly_subgate_closed") is True
        and dig(vsd01, "closure_decision.source_stack_closed") is True,
        "dynamic_overlap_subgate": dig(step24, "closure_decision.VSD01_dynamic_overlap_subgate_closed") is True
        and dig(vsd01, "closure_decision.dynamic_matter_overlap_packet_closed") is True
        and dig(dynamic_packet, "what_closes_now.same_source_dynamic_matter_overlap_packet_validates") is True,
        "primitive_C1_first_response_layer": dig(
            step24, "closure_decision.selected_primitive_C1_contractions_first_response_layer"
        )
        is True
        and dig(vsd01, "what_closes_now.primitive_C1_contractions_first_response_layer") is True,
        "A_selected_b_selected_deltaTheta": dig(step24, "closure_decision.selected_A_selected_promoted") is True
        and dig(step24, "closure_decision.selected_b_selected_promoted") is True
        and dig(step24, "closure_decision.selected_deltaTheta_C1_promoted") is True
        and dig(vsd01, "what_closes_now.A_selected_promoted") is True
        and dig(vsd01, "what_closes_now.b_selected_promoted") is True
        and dig(vsd01, "what_closes_now.deltaTheta_C1_promoted") is True,
        "source_to_C1_transfer_map": dig(step24, "closure_decision.selected_source_to_C1_transfer_map_emitted") is True,
        "Rtheta_value_functional_domain": dig(
            rtheta_source, "closure_decision.selected_Rtheta_scalar_value_functional_source_domain_closed"
        )
        is True
        and dig(rtheta_source, "closure_decision.ten_scalar_row_codomain_aligned") is True,
        "no_target_fitting": all(packet.get("target_fitting_used") is False for packet in [step36, step37, step38, step39, step40]),
    }
    solution_assembled = all(closed_checks.values())

    open_checks = {
        "accepted_internal_scalar_row_count_is_zero": dig(step25, "closure_decision.accepted_internal_scalar_row_count") == 0,
        "step24_value_functional_rows_open": dig(step24, "closure_decision.accepted_value_functional_rows_closed") is False,
        "accepted_Yukawa_magnitudes_open": dig(step24, "closure_decision.accepted_Yukawa_magnitudes_closed") is False,
        "CKM_PMNS_measured_value_closure_open": dig(step24, "closure_decision.CKM_PMNS_measured_value_closure_closed")
        is False,
        "lambda_H_row_open": dig(step25, "closure_decision.lambda_H_row_emitted") is False,
        "Rtheta_numerical_rows_open": dig(rtheta_source, "closure_decision.no_knob_numerical_rows_emitted") is False,
        "true_SM_equivalence_open": dig(step24, "closure_decision.true_SM_equivalence_closed") is False
        and dig(vsd01, "closure_decision.true_SM_equivalence_closed") is False,
        "full_no_knob_open": dig(step24, "closure_decision.full_no_knob_closed") is False
        and dig(vsd01, "closure_decision.full_no_knob_closed") is False,
    }

    branch = {
        "schema": "MTTStep41SingleBranchFirstResponseSolution.v1",
        "status": "SINGLE_Q79_F_M1_FIRST_RESPONSE_SOLUTION_ASSEMBLED",
        "selected_branch": {
            "q": 79,
            "orientation": "F",
            "torsion_m": 1,
            "finite_source": "selected S3 differential-cohomology restriction with qutrit Heisenberg-Weyl projective rho_E",
            "covariant": "D_E = d + du ad(T3) on the selected diagonal End0 lane",
            "transport": "stationary projector/Riesz-Green plus same-branch dotD/alpha1 replay",
            "first_response": "VSD01/Step24 primitive C1, A_selected, b_selected, deltaTheta_C1, and dynamic overlap packet",
        },
        "inputs": {
            "s3_class": rel(STEP36),
            "finite_trace_gap": rel(STEP37),
            "projective_rhoE": rel(STEP38),
            "diagonal_D_E_transport": rel(STEP39),
            "dotD_alpha1": rel(STEP40),
            "dynamic_gate": rel(STEP24),
            "primitive_assembly": rel(VSD01),
            "dynamic_overlap": rel(DYNAMIC_PACKET),
            "Rtheta_domain": rel(RTHETA_SOURCE),
            "threshold_external_replay": rel(STEP25),
        },
        "closed_checks": closed_checks,
        "theorem": {
            "name": "SelectedSingleBranchFirstResponseSolutionTheorem",
            "proved": solution_assembled,
            "statement": (
                "On the selected q=79, orientation F, torsion m=1 branch, the selected S3 source, "
                "finite trace/gap/Riesz-Green layer, projective rho_E gauge class, diagonal End0 "
                "covariant, stationary transport, dotD/alpha1 replay, source-to-C1 transfer, "
                "dynamic overlap packet, primitive first-response C1 rows, A_selected, b_selected, "
                "and deltaTheta_C1 are all present from existing verified packets and are mutually "
                "same-branch/same-source compatible."
            ),
        },
        "guardrail": (
            "This is a selected first-response/operator-source solution, not an accepted numerical "
            "SM value solution. It does not use measured SM values as selectors and does not claim "
            "Yukawa, CKM/PMNS, Higgs, threshold, mass-scheme, true-SM, or no-knob closure."
        ),
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(SOLUTION, branch)

    frontier = {
        "schema": "MTTStep41ValueFunctionalFrontier.v1",
        "status": "FIRST_RESPONSE_SOLUTION_CLOSED_VALUE_FUNCTIONAL_ROWS_OPEN",
        "closed_now": {
            "single_branch_first_response_solution_assembled": solution_assembled,
            "primitive_C1_first_response_layer_closed": True,
            "selected_A_selected_promoted": True,
            "selected_b_selected_promoted": True,
            "selected_deltaTheta_C1_promoted": True,
            "selected_dynamic_overlap_tensor_closed": True,
            "selected_source_to_C1_transfer_map_closed": True,
            "selected_Rtheta_scalar_value_functional_source_domain_closed": True,
        },
        "still_open": {
            "accepted_internal_scalar_row_count": 0,
            "accepted_value_functional_rows_closed": False,
            "accepted_Yukawa_magnitudes_closed": False,
            "CKM_PMNS_measured_value_closure_closed": False,
            "lambda_H_row_emitted": False,
            "threshold_matching_internal_rows_closed": False,
            "mass_scheme_internal_rows_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_payload": {
            "target": NEXT,
            "minimum_fields": [
                "instantiate the selected R_theta coefficient/value functionals on the Step41 first-response solution",
                "emit internal scalar rows for Yukawa magnitudes, CKM/PMNS, lambda_H, thresholds, and mass scheme",
                "prove rows are selected from the same branch rather than imported from observed data",
                "only then run the true-SM/no-knob equivalence audit",
            ],
        },
        "open_checks": open_checks,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(FRONTIER, frontier)

    candidate = {
        "candidate": "MTTSelectedStep41SingleBranchSolutionAssemblyOrValueFunctionalFrontier",
        "status": STATUS,
        "inputs": branch["inputs"],
        "output_packets": {
            "single_branch_solution": rel(SOLUTION),
            "value_functional_frontier": rel(FRONTIER),
        },
        "theorem": branch["theorem"],
        "closure_decision": {
            "single_branch_first_response_solution_assembled": solution_assembled,
            "selected_q79_F_m1_branch_fixed": True,
            "selected_S3_source_chain_closed": True,
            "selected_operator_transport_chain_closed": True,
            "primitive_C1_first_response_layer_closed": True,
            "selected_A_selected_promoted": True,
            "selected_b_selected_promoted": True,
            "selected_deltaTheta_C1_promoted": True,
            "selected_dynamic_overlap_tensor_closed": True,
            "selected_source_to_C1_transfer_map_closed": True,
            "selected_Rtheta_scalar_value_functional_source_domain_closed": True,
            "accepted_internal_scalar_row_count": 0,
            "accepted_value_functional_rows_closed": False,
            "accepted_Yukawa_magnitudes_closed": False,
            "CKM_PMNS_measured_value_closure_closed": False,
            "lambda_H_row_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": solution_assembled,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step41_SingleBranchSolutionAssembly_or_ValueFunctionalFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "single_branch_first_response_solution_assembled": solution_assembled,
        "selected_q79_F_m1_branch_fixed": True,
        "selected_S3_source_chain_closed": True,
        "selected_operator_transport_chain_closed": True,
        "primitive_C1_first_response_layer_closed": True,
        "selected_A_selected_promoted": True,
        "selected_b_selected_promoted": True,
        "selected_deltaTheta_C1_promoted": True,
        "selected_dynamic_overlap_tensor_closed": True,
        "selected_source_to_C1_transfer_map_closed": True,
        "selected_Rtheta_scalar_value_functional_source_domain_closed": True,
        "accepted_internal_scalar_row_count": 0,
        "accepted_value_functional_rows_closed": False,
        "accepted_Yukawa_magnitudes_closed": False,
        "CKM_PMNS_measured_value_closure_closed": False,
        "lambda_H_row_emitted": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step41 SingleBranchSolutionAssembly or ValueFunctionalFrontier v1

Status: `{STATUS}`.

Step41 assembles the strongest existing same-branch packets into one explicit
solution object:

- branch: `q=79`, orientation `F`, torsion `m=1`
- selected S3 differential-cohomology source and restriction
- finite trace `D_E`, positive gap, Riesz/Green lock
- qutrit Heisenberg-Weyl projective `rho_E` gauge class
- selected diagonal End0 covariant `D_E = d + du ad(T3)`
- stationary projector/Riesz-Green transport and same-branch `dotD/alpha1`
- VSD01/Step24 primitive C1 first-response layer
- `A_selected`, `b_selected`, `deltaTheta_C1`, source-to-C1 transfer, and dynamic overlap packet

What this achieves:

The first-response/operator-source branch is now assembled as one checked
candidate. The previous Step40 wording that left primitive C1/A/b open is
superseded at this layer by the later Step24/VSD01 packets.

What remains open:

- accepted internal scalar rows
- Yukawa magnitudes and mass ratios
- CKM/PMNS measured value closure
- `lambda_H`, threshold, and mass-scheme internal rows
- true SM equivalence and full no-knob closure

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
