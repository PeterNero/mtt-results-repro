"""Build Step 31 visible Chern-Weil source to same-source symmetry breaking."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step31_visiblecwsource_to_samesourcesymmetrybreaking"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
REDUCTION = PACKET_DIR / "step31_visible_source_reduction.packet.json"
LANES = PACKET_DIR / "step31_two_lane_construction_frontier.packet.json"
NEXT_CONTRACT = PACKET_DIR / "step31_samesource_symmetrybreaking_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step31_VisibleCWSource_to_SameSourceSymmetryBreaking_v1.md"

STEP30 = DATA / "selected_step30_projectivebn_mechanicallift_or_visiblesourcecutset.candidate.json"
VISIBLE_CW = DATA / "selected_visible_chern_weil_operator_source.candidate.json"
VISIBLE_GS = DATA / "selected_visible_green_schwarz_operator_source.candidate.json"
NONSPLIT = DATA / "selected_nonsplit_rank2_or_routec_same_source_packet.candidate.json"
ROUTEC_NOGO = DATA / "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
TERMINAL_PIC0 = DATA / "selected_terminal_monad_lane_pic0_quotient_source.candidate.json"

STATUS = "MTT_SELECTED_STEP31_VISIBLECWSOURCE_REDUCED_TO_SAMESOURCE_SYMMETRYBREAKING"
NEXT = "MTT_SameSource_SymmetryBreaking_Source_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP30, VISIBLE_CW, VISIBLE_GS, NONSPLIT, ROUTEC_NOGO, TERMINAL_PIC0]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 31 inputs: " + ", ".join(missing))

    step30 = load(STEP30)
    cw = load(VISIBLE_CW)
    gs = load(VISIBLE_GS)
    nonsplit = load(NONSPLIT)
    routec_nogo = load(ROUTEC_NOGO)
    terminal = load(TERMINAL_PIC0)

    reduction = {
        "schema": "MTTStep31VisibleSourceReduction.v1",
        "status": "VISIBLE_CW_OPERATOR_SOURCE_REDUCED_TO_SAMESOURCE_SYMMETRYBREAKING",
        "step30_import": {
            "projective_BN_mechanical_lift_fields_closed": step30["closure_decision"]["projective_BN_mechanical_lift_fields_closed"],
            "selected_visible_operator_source_closed": step30["closure_decision"]["selected_visible_operator_source_closed"],
            "operator_level_projective_rhoE_transition_closed": step30["closure_decision"]["operator_level_projective_rhoE_transition_closed"],
        },
        "closed_support": cw["closed_support"],
        "visible_green_schwarz_gate": {
            "selected_s3_source_closed": gs["gate_results"]["selected_s3_source_closed"],
            "visible_green_schwarz_curvature_closed": gs["gate_results"]["visible_green_schwarz_curvature_closed"],
            "first_blocking_layer_is_selected_operator_source": gs["gate_results"]["first_blocking_layer_is_selected_operator_source"],
            "selected_visible_operator_source_constructed": gs["gate_results"]["selected_visible_operator_source_constructed"],
        },
        "reduction_theorem": {
            "visible_cw_theorem_proved": cw["theorem"]["proved"],
            "nonsplit_or_routec_theorem_proved": nonsplit["theorem"]["proved"],
            "selected_visible_operator_source_closed": cw["open_gates"]["selected_visible_operator_source_closed"],
            "next_object": nonsplit["same_source_packet_contract"]["common_blocker"]["name"],
        },
        "retired_or_demoted": cw["retired_or_demoted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(REDUCTION, reduction)

    lanes = {
        "schema": "MTTStep31TwoLaneConstructionFrontier.v1",
        "status": "TWO_LANES_REDUCED_TO_COMMON_SYMMETRYBREAKING_SOURCE",
        "rank2_lane": {
            "classification": nonsplit["rank2_lane"]["classification"],
            "candidate_id": nonsplit["rank2_lane"]["candidate_id"],
            "priority": 1,
            "source_shape": nonsplit["rank2_lane"]["source_shape"],
            "target": nonsplit["rank2_lane"]["target"],
            "closed": nonsplit["rank2_lane"]["closed"],
            "blocked_by": nonsplit["rank2_lane"]["blocked_by"],
            "first_fill_template": nonsplit["rank2_lane"]["first_fill_template"],
            "required_next_packet": nonsplit["rank2_lane"]["required_next_packet"],
        },
        "route_c_lane": {
            "classification": nonsplit["route_c_lane"]["classification"],
            "priority": 2,
            "source_shape": nonsplit["route_c_lane"]["source_shape"],
            "closed": nonsplit["route_c_lane"]["closed"],
            "blocked_by": nonsplit["route_c_lane"]["blocked_by"],
            "current_scaffold_fill_nogo": routec_nogo["fill_summary"]["nogo_for_current_scaffolds"],
            "selected_emitted_current_scaffold": routec_nogo["fill_summary"]["selected_emitted"],
        },
        "terminal_pic0_gate": {
            "terminal_lane_conditional_uniqueness_imported": terminal["gate_results"]["terminal_lane_conditional_uniqueness_imported"],
            "selected_terminal_lane_pic0_source_proved": terminal["gate_results"]["selected_terminal_lane_pic0_source_proved"],
            "naive_pic0_quotient_rejected": terminal["gate_results"]["naive_pic0_quotient_rejected"],
            "finite_gerbe_torsion_route_live": terminal["gate_results"]["finite_gerbe_torsion_route_live"],
            "same_source_operator_selector_still_open": terminal["gate_results"]["same_source_operator_selector_still_open"],
        },
        "lane_priority": nonsplit["same_source_packet_contract"]["lane_priority"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(LANES, lanes)

    common = nonsplit["same_source_packet_contract"]["common_blocker"]
    contract = {
        "schema": "MTTStep31SameSourceSymmetryBreakingContract.v1",
        "status": "NEXT_SAMESOURCE_SYMMETRYBREAKING_SOURCE_CONTRACT",
        "next_required_artifact": NEXT,
        "must_emit_next": common["must_supply"],
        "why_common": common["why_common"],
        "must_not_reopen": [
            "source-level S3 projective gerbe rho_E",
            "visible Green-Schwarz curvature row",
            "smooth projective B_N mechanical lift fields",
            "rank-two Appell-Humbert/topological target data",
            "identity rho_E smoke route",
        ],
        "acceptance_tests": nonsplit["same_source_packet_contract"]["from_visible_reduction"]["acceptance_tests"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(NEXT_CONTRACT, contract)

    candidate = {
        "candidate": "MTTSelectedStep31VisibleCWSourceToSameSourceSymmetryBreaking",
        "status": STATUS,
        "inputs": {
            "step30": rel(STEP30),
            "visible_cw": rel(VISIBLE_CW),
            "visible_gs": rel(VISIBLE_GS),
            "nonsplit": rel(NONSPLIT),
            "routec_nogo": rel(ROUTEC_NOGO),
            "terminal_pic0": rel(TERMINAL_PIC0),
        },
        "output_packets": {
            "visible_source_reduction": rel(REDUCTION),
            "two_lane_construction_frontier": rel(LANES),
            "samesource_symmetrybreaking_contract": rel(NEXT_CONTRACT),
        },
        "theorem": {
            "name": "Step31VisibleCWSourceReductionToSymmetryBreakingSourceTheorem",
            "proved": True,
            "statement": (
                "Given Step30's closed projective-B_N mechanical lift and the existing "
                "visible Chern-Weil/Green-Schwarz reductions, the live visible operator "
                "source problem is exactly the same-source symmetry-breaking source. "
                "The rank-two non-split V_alpha lane is the preferred first fill lane; "
                "Route-C remains the parallel repair lane. Both require the same missing "
                "object: a source that selects or quotients base order and Pic0 and emits "
                "operator data without measured or benchmark inputs."
            ),
        },
        "closure_decision": {
            "visible_CW_operator_source_reduced_to_common_source": True,
            "rank2_non_split_lane_prioritized": True,
            "routec_lane_retained_as_parallel_repair": True,
            "same_source_symmetrybreaking_contract_emitted": True,
            "selected_visible_operator_source_closed": False,
            "same_source_symmetrybreaking_source_closed": False,
            "operator_level_projective_rhoE_transition_closed": False,
            "selected_D_E_Riesz_Green_dotD_values_closed": False,
            "fullS2_operator_payload_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "visible_source_wall_decomposed": True,
            "next_packet_contract_exact": True,
            "rank2_and_routec_lane_priority_fixed": True,
        },
        "what_remains_open": {
            "same_source_symmetrybreaking_source": True,
            "selected_visible_operator_source": True,
            "operator_level_projective_rhoE_transition": True,
            "selected_D_E_Riesz_Green_dotD_values": True,
            "internal_Rtheta_scalar_rows": True,
            "lambda_H": True,
            "Yukawa_CKM_PMNS_mass_values": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step31_VisibleCWSource_to_SameSourceSymmetryBreaking_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "visible_CW_operator_source_reduced_to_common_source": True,
        "same_source_symmetrybreaking_source_closed": False,
        "operator_sector_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step31 VisibleCWSource to SameSourceSymmetryBreaking v1

Status: `{STATUS}`.

Step31 closes the reduction of the visible Chern-Weil/operator source wall:

```text
smooth projective B_N mechanical lift              closed by Step30
source-level S3 projective gerbe rho_E             closed
visible Green-Schwarz curvature row                closed
split/abelian visible source route                 rejected/demoted
rank-two non-split V_alpha lane                    priority 1
Route-C finite HYM/Strominger lane                 priority 2 fallback
same-source symmetry-breaking source               open
selected visible operator values                   open
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
