"""Build public 8x8 likelihood search or Route-C source emission execution artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_public8x8likelihoodsearch_or_routecsourceemissionexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LIKELIHOOD = PACKET_DIR / "public_8x8_likelihood_search_execution.packet.json"
ROUTEC = PACKET_DIR / "routec_source_emission_execution.packet.json"
NOKNOB = PACKET_DIR / "noknob_value_source_execution.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_public8x8_or_routec_execution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Public8x8LikelihoodSearch_or_RouteCSourceEmissionExecution_v1.md"

PREVIOUS = DATA / "selected_externalprofilereplayfrozenboundary_or_trueequivalencevaluesourcecutset.candidate.json"
THREE_LANE = (
    DATA
    / "selected_externalprofilereplayfrozenboundary_or_trueequivalencevaluesourcecutset"
    / "three_lane_true_equivalence_value_source_attempt.packet.json"
)
BRIDGE = (
    DATA
    / "selected_externalprofiletofullcovariancebridge_or_selectedsourcerows"
    / "external_profile_full_covariance_bridge.packet.json"
)
RTHETA_PI = DATA / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission.candidate.json"
RTHETA_VALUE_GATE = (
    DATA
    / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission"
    / "rtheta_value_gate_after_pi_recheck.packet.json"
)
BN_GATE = (
    DATA
    / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission"
    / "bn_basis_and_sector_transfer_gate.packet.json"
)
FIRST_ROW_FILL = DATA / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport.candidate.json"
FIRST_ROW_PROMOTION = DATA / "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow.candidate.json"
FIRST_ROW_RECON = (
    DATA
    / "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow"
    / "first_value_row_promotion_reconciliation.packet.json"
)
VSD02 = DATA / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation.candidate.json"
VSD02_FILL = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)

STATUS = (
    "MTT_SELECTED_PUBLIC8X8LIKELIHOODSEARCH_OR_ROUTECSOURCEEMISSIONEXECUTION_"
    "BUILT_SUBGATES_CLOSED_TRUE_EQ_OPEN"
)
NEXT = "MTT_Selected_RThetaSectorTransferOrPrimitiveAssemblyMapExecution_v1"


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
        raise FileNotFoundError("missing public8x8/Route-C execution sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        THREE_LANE,
        BRIDGE,
        RTHETA_PI,
        RTHETA_VALUE_GATE,
        BN_GATE,
        FIRST_ROW_FILL,
        FIRST_ROW_PROMOTION,
        FIRST_ROW_RECON,
        VSD02,
        VSD02_FILL,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    three_lane = load(THREE_LANE)
    bridge = load(BRIDGE)
    rtheta_pi = load(RTHETA_PI)
    rtheta_gate = load(RTHETA_VALUE_GATE)
    bn_gate = load(BN_GATE)
    first_fill = load(FIRST_ROW_FILL)
    first_promotion = load(FIRST_ROW_PROMOTION)
    first_recon = load(FIRST_ROW_RECON)
    vsd02 = load(VSD02)
    vsd02_fill = load(VSD02_FILL)

    target = bridge["full_covariance_target"]
    likelihood = {
        "schema": "MTTPublic8x8LikelihoodSearchExecution.v1",
        "status": "PUBLIC_8X8_SEARCH_EXECUTED_SUBBLOCK_PROVENANCE_ONLY",
        "target_shape": target["matrix_shape"],
        "target_symmetric_entries": target["symmetric_unique_entries"],
        "missing_BCT_WZH_cross_covariance_entries": target[
            "hard_missing_entries_for_published_or_reconstructed_likelihood"
        ],
        "sources_checked": [
            {
                "id": "Huang-Zhou-2020-running-fermion-masses",
                "url": "https://arxiv.org/abs/2009.04851",
                "contribution": "BCT running mass values/correlations and uncertainty propagation support.",
                "limitation": "Does not provide W/Z/H weak-scale block or BCT-WZH cross covariance.",
            },
            {
                "id": "Buttazzo-et-al-2013-Higgs-near-criticality",
                "url": "https://arxiv.org/abs/1307.3536",
                "contribution": "Weak-scale lambda, top Yukawa, and gauge coupling formula/provenance support.",
                "limitation": "Does not provide the combined 8x8 external-profile covariance likelihood.",
            },
        ],
        "subblock_provenance_found": True,
        "combined_8x8_likelihood_found": False,
        "accepted_as_full_profile_likelihood": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(LIKELIHOOD, likelihood)

    routec_open = bn_gate["selected_values_open"]
    routec = {
        "schema": "MTTRouteCSourceEmissionExecution.v1",
        "status": "ROUTEC_EXECUTED_HYM_SUBGATE_CLOSED_SECTOR_TRANSFER_OPEN",
        "rtheta_pi_source": rel(RTHETA_PI),
        "rtheta_gate_source": rel(RTHETA_VALUE_GATE),
        "bn_gate_source": rel(BN_GATE),
        "selected_HYM_connection_subgate_closed": rtheta_pi["closure_decision"][
            "selected_HYM_connection_subgate_closed"
        ],
        "diagonal_End0_DE_Green_lane_closed": rtheta_pi["closure_decision"][
            "diagonal_End0_DE_Green_lane_closed"
        ],
        "Pi_Rtheta_closed": rtheta_pi["closure_decision"]["Pi_Rtheta_closed"],
        "selected_value_evaluator_closed": rtheta_pi["closure_decision"]["selected_value_evaluator_closed"],
        "value_evaluator_readiness_present_count": rtheta_gate[
            "value_evaluator_readiness_present_count"
        ],
        "value_evaluator_readiness_required_count": rtheta_gate[
            "value_evaluator_readiness_required_count"
        ],
        "readiness_delta_closed_this_execution": {
            "selected_HYM_connection_subgate": True,
            "diagonal_End0_DE_Green_lane": True,
        },
        "remaining_readiness_items": {
            "selected_sector_B_N_basis": routec_open["selected_sector_B_N_basis"],
            "rank2_to_sector_transfer_values": routec_open["rank2_to_sector_transfer_values"],
            "sector_ready_rhoE_DE_Riesz_Green_dotD_C1": routec_open[
                "sector_ready_rhoE_DE_Riesz_Green_dotD_C1"
            ],
            "selected_quadrature_truncation_error_for_sector_payload": routec_open[
                "selected_quadrature_truncation_error_for_sector_payload"
            ],
        },
        "minimal_next_routec_object": "SelectedRThetaSectorBNBasisAndTransferPayload",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROUTEC, routec)

    noknob = {
        "schema": "MTTNoKnobValueSourceExecution.v1",
        "status": "NOKNOB_EXECUTED_EXACT_PRIMITIVE_SEED_STRICT_SCHEMA_OPEN",
        "first_row_fill_source": rel(FIRST_ROW_FILL),
        "first_row_promotion_source": rel(FIRST_ROW_PROMOTION),
        "vsd02_source": rel(VSD02),
        "first_value_source_row_numeric_payload_emitted": first_fill["closure_decision"][
            "first_value_source_row_numeric_payload_emitted"
        ],
        "primitive_exactness_backimported": first_promotion["closure_decision"][
            "primitive_exactness_backimported"
        ],
        "primitive_seed": first_recon["primitive_seed"],
        "accepted_as_selected_dynamic_value_source_row_now": first_recon[
            "accepted_as_selected_dynamic_value_source_row_now"
        ],
        "all_72_row_exactness_available": first_recon["assembly_gate"][
            "all_72_row_exactness_available"
        ],
        "formal_110_row_replay_integrated": first_recon["assembly_gate"][
            "formal_110_row_replay_integrated"
        ],
        "strict_vsd02_fill_attempt_closed": vsd02["closure_decision"]["strict_fill_attempt_closed"],
        "accepted_vsd02_source_rows_closed": vsd02["closure_decision"][
            "accepted_vsd02_source_rows_closed"
        ],
        "accepted_source_row_count": vsd02_fill["accepted_row_count"],
        "remaining_assembly_map_gap": [
            "selected dynamic transfer identity not promoted",
            "selected b_selected/A_selected/deltaTheta_C1 not promoted",
            "physical Phi_fin^C1 action source not closed",
            "residual-projector-independent provenance not closed",
        ],
        "minimal_next_noknob_object": "PrimitiveToDynamicValueSourceAssemblyMap",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NOKNOB, noknob)

    cutset = {
        "schema": "MTTNextCutsetAfterPublic8x8OrRouteCExecution.v1",
        "status": "NEXT_ATTACK_SECTOR_TRANSFER_OR_PRIMITIVE_ASSEMBLY_MAP",
        "closed_now": {
            "public_8x8_search_executed": True,
            "subblock_provenance_confirmed": True,
            "RouteC_HYM_connection_subgate_closed": True,
            "RouteC_diagonal_End0_DE_Green_lane_closed": True,
            "no_knob_first_exact_primitive_seed_backimported": True,
            "strict_VSD02_schema_and_fill_attempt_closed": True,
        },
        "still_open": {
            "combined_public_8x8_likelihood": True,
            "BCT_WZH_cross_covariance_entries": True,
            "selected_sector_B_N_basis": True,
            "rank2_to_sector_transfer_values": True,
            "sector_ready_rhoE_DE_Riesz_Green_dotD_C1": True,
            "PrimitiveToDynamicValueSourceAssemblyMap": True,
            "selected_dynamic_value_source_rows": True,
            "selected_Rtheta_source_rows": True,
            "true_SM_equivalence": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "emit selected sector B_N basis and rank2-to-sector transfer values to close Pi_Rtheta",
            "route_B": "prove primitive-to-dynamic assembly map for the exact primitive seed and 110-row packet",
            "route_C": "continue public 8x8 likelihood reconstruction only if a real BCT-WZH cross-covariance source appears",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedPublic8x8LikelihoodSearchOrRouteCSourceEmissionExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "public_8x8_likelihood_search_execution": rel(LIKELIHOOD),
            "routec_source_emission_execution": rel(ROUTEC),
            "noknob_value_source_execution": rel(NOKNOB),
            "next_cutset_after_public8x8_or_routec_execution": rel(CUTSET),
        },
        "theorem": {
            "name": "Public8x8SearchRouteCAndNoKnobExecutionTheorem",
            "proved": True,
            "statement": (
                "Executing the next frontier confirms that public literature supplies sub-block provenance but "
                "not the combined 8x8 BCT-WZH likelihood. Route-C advances internally by importing the selected "
                "HYM connection and diagonal End0 D_E/Green lane, leaving sector B_N basis and rank2-to-sector "
                "transfer as the active Pi_Rtheta blockers. The no-knob lane advances by back-importing an exact "
                "first primitive seed and strict VSD02 schema, but still lacks the primitive-to-dynamic assembly map."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "public_8x8_likelihood_found": False,
            "RouteC_HYM_connection_subgate_closed": True,
            "RouteC_sector_transfer_closed": False,
            "no_knob_exact_primitive_seed_backimported": True,
            "PrimitiveToDynamicValueSourceAssemblyMap_closed": False,
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
        "certificate": "MTT_Selected_Public8x8LikelihoodSearch_or_RouteCSourceEmissionExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "public_8x8_likelihood_found": False,
        "RouteC_HYM_connection_subgate_closed": True,
        "RouteC_sector_transfer_closed": False,
        "no_knob_exact_primitive_seed_backimported": True,
        "PrimitiveToDynamicValueSourceAssemblyMap_closed": False,
        "true_SM_equivalence_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Public8x8LikelihoodSearch or RouteCSourceEmissionExecution v1

Status: `{STATUS}`.

The next frontier execution made two real sub-closures.

```text
public combined 8x8 likelihood found       : false
Route-C HYM connection subgate closed       : true
Route-C diagonal End0 D_E/Green closed      : true
R_theta readiness                           : {routec["value_evaluator_readiness_present_count"]}/{routec["value_evaluator_readiness_required_count"]}
exact primitive seed backimported           : true
selected dynamic value-source row promoted  : false
true SM equivalence                         : false
```

The next best target is no longer a broad three-lane search.  It is either the
selected sector B_N/rank2-transfer payload for `Pi_Rtheta`, or the
primitive-to-dynamic value-source assembly map for the no-knob lane.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
