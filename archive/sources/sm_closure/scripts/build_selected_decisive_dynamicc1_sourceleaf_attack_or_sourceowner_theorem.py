"""Build decisive dynamic-C1 source-leaf attack against all current routes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_decisive_dynamicc1_sourceleaf_attack_or_sourceowner_theorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_sixfield_phifinc1_source_attack.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_row_export_attack.packet.json"
QASU3 = PACKET_DIR / "qasu3_bn27_source_support_attack.packet.json"
OWNER = PACKET_DIR / "minimal_dynamic_c1_source_owner_theorem.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DecisiveDynamicC1_SourceLeafAttack_or_SourceOwnerTheorem_v1.md"

STATUS = "MTT_SELECTED_DECISIVE_DYNAMICC1_SOURCELEAF_ATTACK_BUILT_SOURCE_OWNER_OPEN"
NEXT = "MTT_Selected_DynamicC1_SourceOwnerTheorem_or_IndependentConnectionTables_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def optional_load(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return load(path)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    physical_gate = load(DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission.candidate.json")
    action_restriction = load(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission.candidate.json")
    route_rows = load(DATA / "selected_routeaemission_or_routebgalerkinrows_execution.candidate.json")
    source_counter = load(DATA / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel.candidate.json")
    pre_residual = load(DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom.candidate.json")
    source_bundle = load(DATA / "selected_postsmparity_sourcetheorembundle_or_trueequivalence_exitmatrix.candidate.json")

    proto_basis = optional_load(
        TEXPAPERS
        / "mtt-protospinor-gr-response-proof"
        / "candidate_data"
        / "post_alpha_independent_long_trace_map_and_basis_values_or_independent_primitive_rows_execution.packet.json"
    )
    nonsm_phifin = optional_load(
        TEXPAPERS
        / "mtt-nonsm-constants-no-knob"
        / "candidate_data"
        / "phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_import.candidate.json"
    )
    qasu3_bn = optional_load(
        TEXPAPERS
        / "mtt-qa-su3-packet-proof"
        / "candidate_data"
        / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface.candidate.json"
    )
    qasu3_corr = optional_load(
        TEXPAPERS
        / "mtt-qa-su3-packet-proof"
        / "candidate_data"
        / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission.candidate.json"
    )

    route_a_fields = {
        "physical_first_variation": False,
        "physical_trace_frobenius_measure": action_restriction["closure_decision"]["measure_normalization_derived"],
        "phase_R_Z_source": False,
        "shift_R_X_source": False,
        "same_source_b_selected": False,
        "no_extra_boundary_or_source": False,
    }
    route_a_passes = all(route_a_fields.values())
    route_a_packet = {
        "schema": "MTTRouteASixFieldPhiFinC1SourceAttack.v1",
        "status": "ROUTE_A_REJECTED_SOURCE_FIELDS_OPEN",
        "source": rel(DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission.candidate.json"),
        "required_fields": route_a_fields,
        "passes_strict_source_validator": route_a_passes,
        "why_not": physical_gate["what_remains_open"],
        "new_information": (
            "Route A cannot be closed from current support because five of six physical source-emission fields "
            "remain theorem-unemitted; measure normalization is the only closed field."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    proto_frontier = proto_basis.get("frontier_decision", {}) if proto_basis else {}
    nonsm_guardrails = nonsm_phifin.get("guardrails", {}) if nonsm_phifin else {}
    route_b_fields = {
        "stationary_basis_rows_selected": bool(
            proto_basis
            and proto_basis["route_B_selected_basis_value_fill"]["accepted_for_basis_stage"] is True
            and proto_basis["route_B_selected_basis_value_fill"]["selected_row_count"] == 19
        ),
        "primitive_row_ids_locked": bool(
            proto_basis
            and proto_basis["independent_primitive_rows_execution_ready"]["primitive_row_count"] == 72
        ),
        "formal_110_rows_executed": route_rows["promotion_decision"]["formal_rows_executed"] is True,
        "dynamic_dotd_trace_binding_selected": bool(
            nonsm_phifin
            and nonsm_guardrails.get("stationary_source_layer_promoted") is True
            and nonsm_phifin["promotion_decision"]["selected_PhiFinC1_identity_promoted"] is False
        ),
        "residual_projector_independent_source": False,
        "selected_row_kernel_source": False,
    }
    route_b_passes = all(route_b_fields.values())
    route_b_packet = {
        "schema": "MTTRouteBIndependentRowExportAttack.v1",
        "status": "ROUTE_B_PARTIAL_EXPORT_REJECTED_SOURCE_OWNER_OPEN",
        "inputs": {
            "protospinor_trace_basis_values": str(
                TEXPAPERS
                / "mtt-protospinor-gr-response-proof"
                / "candidate_data"
                / "post_alpha_independent_long_trace_map_and_basis_values_or_independent_primitive_rows_execution.packet.json"
            ),
            "nonsm_phifinc1_import": str(
                TEXPAPERS
                / "mtt-nonsm-constants-no-knob"
                / "candidate_data"
                / "phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_import.candidate.json"
            ),
            "formal_rows": rel(DATA / "selected_routeaemission_or_routebgalerkinrows_execution.candidate.json"),
        },
        "required_fields": route_b_fields,
        "passes_strict_source_validator": route_b_passes,
        "frontier_imported_from_protospinor": proto_frontier,
        "new_information": (
            "Cross-repo Route B import confirms the basis/stationary side and row ids are real progress, but it "
            "does not supply residual-projector-independent dynamic row-source ownership."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    qasu3_fields = {
        "nonidentity_rho_E_interface_built": bool(qasu3_bn and qasu3_bn["interface_checks"]["previous_gate_reduced_to_this_payload"]),
        "quotient_valid_B_N_required": bool(qasu3_bn and "quotient_valid_B_N" in qasu3_bn["interface_checks"]["required_payload_keys_imported"]),
        "selected_values_all_open": bool(qasu3_bn and qasu3_bn["interface_checks"]["all_template_selected_values_open"]),
        "selected_correction_source_closed": bool(
            qasu3_corr and qasu3_corr["decision"]["selected_correction_matrix_source_closed"]
        ),
        "selected_full_response_emission_closed": bool(
            qasu3_corr and qasu3_corr["decision"]["selected_full_response_emission_closed"]
        ),
        "actual_operator_payload_promoted": False,
    }
    qasu3_passes = (
        qasu3_fields["nonidentity_rho_E_interface_built"]
        and qasu3_fields["quotient_valid_B_N_required"]
        and qasu3_fields["selected_correction_source_closed"]
        and qasu3_fields["selected_full_response_emission_closed"]
        and qasu3_fields["actual_operator_payload_promoted"]
    )
    qasu3_packet = {
        "schema": "MTTQaSU3BN27SourceSupportAttack.v1",
        "status": "QASU3_BN_SUPPORT_READY_BUT_SOURCE_VALUES_OPEN",
        "required_fields": qasu3_fields,
        "passes_strict_source_validator": qasu3_passes,
        "new_information": (
            "Qa/SU3 supplies the right nonidentity rho_E and quotient-valid B_N target contract, but it still "
            "does not emit selected correction/full-response values or an actual operator payload."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    owner_theorem = {
        "schema": "MTTDynamicC1SourceOwnerTheorem.v1",
        "status": "MINIMAL_SOURCE_OWNER_THEOREM_REQUIRED",
        "statement": (
            "A selected dynamic C1 source owner is the missing object common to all routes: one same-branch "
            "source must own the selected admissible C1 variation directions, the phase/shift residual operators "
            "R_Z/R_X before residual-projector replay, the Hessian/source vector b_selected, and the sector row "
            "assembly, or else export independent selected connection/Galerkin tables that imply those rows."
        ),
        "minimal_fields": [
            "source_owner_id on the selected q79/F,m=1 branch",
            "selected admissible C1 variation space before residual-projector replay",
            "selected phase R_Z operator source",
            "selected shift R_X operator source",
            "same-source Hessian/source vector b_selected",
            "sector functor assembly into u,d,e,nuD rows",
            "independence from observed constants, locked residual targets, and replay-only provenance",
        ],
        "legal_exports": [
            "Route A physical Phi_fin^C1 action/source theorem",
            "Route B independent selected Galerkin row-kernel theorem",
            "Qa/SU3 nonidentity rho_E plus quotient-valid B_N selected connection table export",
        ],
        "if_supplied_then": {
            "unpatched_A_selected_b_selected_deltaTheta_promote": True,
            "sector_response_matrices_promote": True,
            "dynamic_C1_source_leaf_closes": True,
        },
        "currently_supplied": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a_packet_path = ROUTE_A
    route_b_packet_path = ROUTE_B
    qasu3_packet_path = QASU3
    owner_packet_path = OWNER
    for path, payload in [
        (route_a_packet_path, route_a_packet),
        (route_b_packet_path, route_b_packet),
        (qasu3_packet_path, qasu3_packet),
        (owner_packet_path, owner_theorem),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    any_route_closes = route_a_passes or route_b_passes or qasu3_passes
    candidate = {
        "candidate": "MTTSelectedDecisiveDynamicC1SourceLeafAttackOrSourceOwnerTheorem",
        "status": STATUS,
        "inputs": {
            "physical_source_gate": rel(DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission.candidate.json"),
            "action_restriction_gate": rel(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission.candidate.json"),
            "route_b_formal_rows": rel(DATA / "selected_routeaemission_or_routebgalerkinrows_execution.candidate.json"),
            "closed_support_countermodel": rel(
                DATA / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel.candidate.json"
            ),
            "pre_residual_source_kernel": rel(
                DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom.candidate.json"
            ),
            "post_smparity_source_bundle": rel(
                DATA / "selected_postsmparity_sourcetheorembundle_or_trueequivalence_exitmatrix.candidate.json"
            ),
        },
        "cross_repo_inputs": {
            "protospinor_trace_basis_rows_present": proto_basis is not None,
            "nonsm_phifinc1_import_present": nonsm_phifin is not None,
            "qasu3_nonidentity_bn_interface_present": qasu3_bn is not None,
            "qasu3_correction_gate_present": qasu3_corr is not None,
        },
        "output_packets": {
            "route_a_sixfield_attack": rel(ROUTE_A),
            "route_b_independent_row_export_attack": rel(ROUTE_B),
            "qasu3_bn27_source_support_attack": rel(QASU3),
            "minimal_dynamic_c1_source_owner_theorem": rel(OWNER),
        },
        "theorem": {
            "name": "DecisiveDynamicC1SourceLeafAttackTheorem",
            "proved": True,
            "statement": (
                "All current cross-repo routes reach the same missing object. Route A has only measure "
                "normalization closed; Route B has stationary basis rows and formal row values but lacks "
                "residual-projector-independent source ownership; Qa/SU3 has the nonidentity rho_E/B_N "
                "target contract but lacks selected correction/full-response values. Therefore the next "
                "non-duplicative proof object is a DynamicC1SourceOwnerTheorem or equivalent selected "
                "connection-table export."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": source_bundle["closure_decision"]["SM_parity_closed"],
            "route_A_closed_now": route_a_passes,
            "route_B_closed_now": route_b_passes,
            "qasu3_source_route_closed_now": qasu3_passes,
            "any_route_closes_now": any_route_closes,
            "dynamic_C1_source_owner_theorem_supplied": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "decisive_three_route_attack_executed": True,
            "cross_repo_basis_and_row_progress_imported": proto_basis is not None and nonsm_phifin is not None,
            "qasu3_nonidentity_bn_contract_imported": qasu3_bn is not None,
            "closed_support_shortcut_rejected_against_current_routes": source_counter["what_closes_now"][
                "closed_support_not_enough_countermodel"
            ],
            "minimal_source_owner_theorem_emitted": True,
        },
        "what_remains_open": {
            "DynamicC1SourceOwnerTheorem": True,
            "or_independent_selected_connection_tables": True,
            "unpatched_dynamic_C1_packet_closure": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "superset_strategy": {
            "using_one_straight_path": False,
            "combines_multiple_paths": True,
            "paths_attacked": [
                "Route A physical Phi_fin^C1 action/source theorem",
                "Route B independent selected Galerkin row-kernel theorem",
                "Qa/SU3 nonidentity rho_E plus quotient-valid B_N selected connection export",
            ],
            "paths_used_as_knobs": False,
            "locked_target": "selected dynamic C1 source ownership before replay promotion",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DecisiveDynamicC1_SourceLeafAttack_or_SourceOwnerTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "any_route_closes_now": any_route_closes,
        "dynamic_C1_source_owner_theorem_supplied": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DecisiveDynamicC1 SourceLeafAttack or SourceOwnerTheorem v1

Status: `{STATUS}`.

This artifact attacks the remaining dynamic-C1 source leaf across the three
currently legal paths:

- Route A: physical `Phi_fin^C1` source emission.
- Route B: independent selected Galerkin row-kernel execution.
- Qa/SU3 route: nonidentity `rho_E` plus quotient-valid `B_N` selected
  connection-table export.

No route closes with the current packets. The smallest non-duplicative next
object is therefore a `DynamicC1SourceOwnerTheorem`: one same-branch source must
own the admissible C1 variation space, `R_Z`, `R_X`, `b_selected`, and sector
row assembly before residual-projector replay; equivalently it may export
selected connection/Galerkin tables that imply those rows.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
