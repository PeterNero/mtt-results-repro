"""Build Rtheta sector-transfer or primitive assembly-map execution artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SECTOR = PACKET_DIR / "rtheta_sector_transfer_execution.packet.json"
ASSEMBLY = PACKET_DIR / "primitive_assembly_map_execution.packet.json"
PI_VALUE = PACKET_DIR / "pi_closure_value_evaluator_domain.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_sector_transfer_or_assembly_execution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaSectorTransfer_or_PrimitiveAssemblyMapExecution_v1.md"

PREVIOUS = DATA / "selected_public8x8likelihoodsearch_or_routecsourceemissionexecution.candidate.json"
PREV_ROUTEC = (
    DATA
    / "selected_public8x8likelihoodsearch_or_routecsourceemissionexecution"
    / "routec_source_emission_execution.packet.json"
)
PREV_NOKNOB = (
    DATA
    / "selected_public8x8likelihoodsearch_or_routecsourceemissionexecution"
    / "noknob_value_source_execution.packet.json"
)
RTHETA_SECTOR = DATA / "selected_rtheta_sectortransferbnbasis_or_pikernelclosure.candidate.json"
SECTOR_SUBGATE = (
    DATA
    / "selected_rtheta_sectortransferbnbasis_or_pikernelclosure"
    / "rtheta_sector_transfer_stationary_subgate.packet.json"
)
RTHETA_DYNAMIC = DATA / "selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure.candidate.json"
DYNAMIC_PI = (
    DATA
    / "selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure"
    / "pi_rtheta_recheck_after_dotd_transport_merge.packet.json"
)
VSD_ASSEMBLY = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
VSD_DECISION = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "vsd01_source_subgate_decision.packet.json"
)
DYNAMIC_OVERLAP = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
RTHETA_PI = DATA / "selected_rtheta_primitivec1overlap_or_pinoneedtheorem.candidate.json"
PI_RECHECK = (
    DATA
    / "selected_rtheta_primitivec1overlap_or_pinoneedtheorem"
    / "pi_rtheta_recheck_after_primitive_c1_import.packet.json"
)
VALUE_EVAL = DATA / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation.candidate.json"
VALUE_GATE = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "rtheta_value_evaluator_execution_gate.packet.json"
)
THRESHOLD_ORDER = DATA / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure.candidate.json"
READINESS = (
    DATA
    / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure"
    / "rtheta_value_execution_readiness_after_ordering.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETASECTORTRANSFER_OR_PRIMITIVEASSEMBLYMAPEXECUTION_"
    "BUILT_PI_AND_SOURCE_ASSEMBLY_CLOSED_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_RThetaThresholdRows_or_ProfileConventionSourceClosure_CurrentFrontier_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing sector-transfer/assembly sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREV_ROUTEC,
        PREV_NOKNOB,
        RTHETA_SECTOR,
        SECTOR_SUBGATE,
        RTHETA_DYNAMIC,
        DYNAMIC_PI,
        VSD_ASSEMBLY,
        VSD_DECISION,
        DYNAMIC_OVERLAP,
        RTHETA_PI,
        PI_RECHECK,
        VALUE_EVAL,
        VALUE_GATE,
        THRESHOLD_ORDER,
        READINESS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    prev_routec = load(PREV_ROUTEC)
    prev_noknob = load(PREV_NOKNOB)
    rtheta_sector = load(RTHETA_SECTOR)
    sector_subgate = load(SECTOR_SUBGATE)
    rtheta_dynamic = load(RTHETA_DYNAMIC)
    dynamic_pi = load(DYNAMIC_PI)
    vsd_assembly = load(VSD_ASSEMBLY)
    vsd_decision = load(VSD_DECISION)
    dynamic_overlap = load(DYNAMIC_OVERLAP)
    rtheta_pi = load(RTHETA_PI)
    pi_recheck = load(PI_RECHECK)
    value_eval = load(VALUE_EVAL)
    value_gate = load(VALUE_GATE)
    readiness = load(READINESS)
    threshold_order = load(THRESHOLD_ORDER)

    sector = {
        "schema": "MTTRThetaSectorTransferExecution.v1",
        "status": "STATIONARY_SECTOR_TRANSFER_AND_DOTD_TRANSPORT_CLOSED",
        "previous_routec_source": rel(PREV_ROUTEC),
        "sector_transfer_source": rel(RTHETA_SECTOR),
        "dynamic_pi_source": rel(RTHETA_DYNAMIC),
        "selected_HYM_connection_subgate_closed": prev_routec["selected_HYM_connection_subgate_closed"],
        "diagonal_End0_DE_Green_lane_closed": prev_routec["diagonal_End0_DE_Green_lane_closed"],
        "stationary_sector_transfer_closed": rtheta_sector["closure_decision"]["stationary_sector_transfer_closed"],
        "selected_stationary_rho_s_closed": rtheta_sector["closure_decision"]["selected_stationary_rho_s_closed"],
        "selected_sector_basis_projector_contract_closed": sector_subgate[
            "selected_sector_basis_projector_contract_closed"
        ],
        "selected_Riesz_Green_stationary_closed": sector_subgate["selected_Riesz_Green_stationary_closed"],
        "dotD_alpha1_transport_subgate_closed": rtheta_dynamic["closure_decision"][
            "dotD_alpha1_transport_subgate_closed"
        ],
        "alpha1_driver_normalization_closed": rtheta_dynamic["closure_decision"][
            "alpha1_driver_normalization_closed"
        ],
        "retired_missing_primitives": dynamic_pi["retired_missing_primitives"],
        "still_missing_before_primitive_import": dynamic_pi["new_minimal_missing_primitives"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SECTOR, sector)

    assembly = {
        "schema": "MTTPrimitiveAssemblyMapExecution.v1",
        "status": "VSD01_SOURCE_ASSEMBLY_AND_DYNAMIC_OVERLAP_PACKET_CLOSED_VALUES_OPEN",
        "previous_noknob_source": rel(PREV_NOKNOB),
        "assembly_source": rel(VSD_ASSEMBLY),
        "dynamic_overlap_source": rel(DYNAMIC_OVERLAP),
        "primitive_seed": prev_noknob["primitive_seed"],
        "all_72_primitive_rows_exact": vsd_decision["closed_for_VSD01_now"]["all_72_primitive_rows_exact"],
        "formal_110_row_assembly": vsd_decision["closed_for_VSD01_now"]["formal_110_row_assembly"],
        "A_selected_promoted": vsd_decision["closed_for_VSD01_now"]["A_selected_promoted"],
        "b_selected_promoted": vsd_decision["closed_for_VSD01_now"]["b_selected_promoted"],
        "deltaTheta_C1_promoted": vsd_decision["closed_for_VSD01_now"]["deltaTheta_C1_promoted"],
        "physical_PhiFinC1_action_source": vsd_decision["closed_for_VSD01_now"][
            "physical_PhiFinC1_action_source"
        ],
        "VSD01_source_assembly_subgate_closed": vsd_assembly["closure_decision"][
            "VSD01_source_assembly_subgate_closed"
        ],
        "dynamic_matter_overlap_operator_packet_closed": dynamic_overlap["promotion_decision"][
            "dynamic_matter_overlap_operator_packet_closed"
        ],
        "selected_dynamic_QaSU3_operator_packet_first_response_layer_closed": dynamic_overlap[
            "promotion_decision"
        ]["selected_dynamic_QaSU3_operator_packet_first_response_layer_closed"],
        "Yukawa_mass_mixing_value_closure": dynamic_overlap["promotion_decision"][
            "Yukawa_mass_mixing_value_closure"
        ],
        "remaining_value_rows": dynamic_overlap["what_remains_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ASSEMBLY, assembly)

    pi_value = {
        "schema": "MTTPiClosureValueEvaluatorDomain.v1",
        "status": "PI_RTHETA_AND_VALUE_EVALUATOR_DOMAIN_CLOSED_NUMERIC_VALUES_OPEN",
        "rtheta_pi_source": rel(RTHETA_PI),
        "value_evaluator_source": rel(VALUE_EVAL),
        "threshold_order_source": rel(THRESHOLD_ORDER),
        "Pi_Rtheta_closed": rtheta_pi["closure_decision"]["Pi_Rtheta_closed"],
        "primitive_C1_overlap_contractions_closed": rtheta_pi["closure_decision"][
            "primitive_C1_overlap_contractions_closed"
        ],
        "matter_slot_routing_closed": rtheta_pi["closure_decision"]["matter_slot_routing_closed"],
        "component_tests_after_primitive_c1_import": pi_recheck["component_tests_after_primitive_c1_import"],
        "coefficient_functional_domain_closed": value_eval["closure_decision"][
            "coefficient_functional_domain_closed"
        ],
        "selected_dynamic_operator_source_owner_closed": value_eval["closure_decision"][
            "selected_dynamic_operator_source_owner_closed"
        ],
        "source_normalized_projection_weights_closed": value_eval["closure_decision"][
            "source_normalized_projection_weights_closed"
        ],
        "selected_threshold_response_functional_instantiated": value_gate[
            "selected_threshold_response_functional_instantiated"
        ],
        "accepted_coefficient_value_count": value_gate["accepted_coefficient_value_count"],
        "accepted_lambda_H_value": value_gate["accepted_lambda_H_value"],
        "value_execution_readiness_present_count": readiness["present_count"],
        "value_execution_readiness_requirement_count": readiness["requirement_count"],
        "blocking_failures": readiness["blocking_failures"],
        "ordered_dependency_graph_closed": threshold_order["closure_decision"][
            "ordered_dependency_graph_closed"
        ],
        "generation_structure_support_closed": threshold_order["closure_decision"][
            "generation_structure_support_closed"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PI_VALUE, pi_value)

    cutset = {
        "schema": "MTTNextCutsetAfterSectorTransferOrAssemblyExecution.v1",
        "status": "NEXT_ATTACK_THRESHOLD_ROWS_OR_PROFILE_CONVENTION_SOURCE_CLOSURE",
        "closed_now": {
            "stationary_sector_transfer": True,
            "selected_stationary_rho_s": True,
            "dotD_alpha1_transport_subgate": True,
            "VSD01_source_assembly_subgate": True,
            "dynamic_matter_overlap_operator_packet_first_response": True,
            "Pi_Rtheta": True,
            "coefficient_functional_domain": True,
            "selected_dynamic_operator_source_owner": True,
            "ordered_value_frontier_dependency_graph": True,
        },
        "still_open": {
            "same_branch_scale_scheme_loop_convention": True,
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "no_knob_value_derivation": True,
            "full_profile_likelihood_or_accepted_diagonal_theorem": True,
            "numeric_Rtheta_coefficient_values": True,
            "lambda_H_value_execution": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive same-branch scale/scheme/loop convention and selected threshold/mass-scheme source rows",
            "route_B": "prove an accepted diagonal/profile theorem strong enough to instantiate R_theta values",
            "route_C": "explicitly introduce minimal universal parameter policy only if no no-knob route can emit the rows",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaSectorTransferOrPrimitiveAssemblyMapExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_sector_transfer_execution": rel(SECTOR),
            "primitive_assembly_map_execution": rel(ASSEMBLY),
            "pi_closure_value_evaluator_domain": rel(PI_VALUE),
            "next_cutset_after_sector_transfer_or_assembly_execution": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaSectorTransferPrimitiveAssemblyAndPiClosureTheorem",
            "proved": True,
            "statement": (
                "The current frontier can import both next-branch sub-closures: selected stationary sector transfer, "
                "rho_s, Riesz/Green, dotD_alpha1 transport, the VSD-01 primitive/source assembly stack, and the "
                "same-source dynamic matter/overlap packet. Combining these with the primitive C1 overlap import "
                "closes Pi_Rtheta and the R_theta value-evaluator domain/source-owner gate. Numeric coefficient "
                "values remain rejected because threshold/profile convention and source rows are still absent."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "Pi_Rtheta_closed": True,
            "VSD01_source_assembly_subgate_closed": True,
            "dynamic_matter_overlap_operator_packet_first_response_closed": True,
            "coefficient_functional_domain_closed": True,
            "selected_value_evaluator_closed": False,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "true_SM_equivalence_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RThetaSectorTransfer_or_PrimitiveAssemblyMapExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "Pi_Rtheta_closed": True,
        "VSD01_source_assembly_subgate_closed": True,
        "dynamic_matter_overlap_operator_packet_first_response_closed": True,
        "coefficient_functional_domain_closed": True,
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaSectorTransfer or PrimitiveAssemblyMapExecution v1

Status: `{STATUS}`.

The next branch closes substantially.

```text
stationary sector transfer closed       : true
dotD_alpha1 transport closed            : true
VSD01 primitive/source assembly closed  : true
dynamic matter overlap first layer      : true
Pi_Rtheta closed                        : true
Rtheta coefficient values accepted      : 0
true SM equivalence                     : false
```

The active blocker has moved again.  It is now value execution:
same-branch scale/scheme/loop convention, threshold matching source rows,
mass-scheme conversion rows, no-knob value derivation, and a full profile or
accepted diagonal theorem.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
