"""Attempt selected C1 routing, normalization, and overlap source closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"
TRANSFER = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
SECTOR_ROUTING = DATA / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json"
SECTOR_CHARGE = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
HYBRID = DATA / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json"
A_ASSEMBLY = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"

OUTPUT = DATA / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet.candidate.json"
CERT = CERTS / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Selected_C1_Routing_Normalization_and_Overlap_Source_Packet_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_C1_ROUTING_NORMALIZATION_OVERLAP_SOURCE_ATTEMPT_BUILT_SELECTION_STILL_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    transfer = load(TRANSFER)
    routing = load(SECTOR_ROUTING)
    charge = load(SECTOR_CHARGE)
    hybrid = load(HYBRID)
    assembly = load(A_ASSEMBLY)

    target_route = routing["routing_search"]["exact_rows_relative_to_locked_columns"][0]
    source_route_selected = routing["routing_search"]["source_data_independently_selects_route"]
    conditional_exact = transfer["conditional_transfer_map"]["conditional_exact"]

    c1_routing_attempt = {
        "conditional_route": {
            "phase_Z_to": target_route["phase_route"],
            "shift_X_to": target_route["shift_route"],
            "matches_locked_columns": target_route["matches_locked_columns"],
            "phase_residual": target_route["phase_residual_to_locked_column"],
            "shift_residual": target_route["shift_residual_to_locked_column"],
        },
        "selected_source_independently_derives_route": source_route_selected,
        "selected_transfer_map_emitted": transfer["selected_status"]["selected_transfer_map_emitted"],
        "selected_sector_routing_emitted": transfer["selected_status"]["selected_sector_routing_emitted"],
        "verdict": "conditional route is unique relative to the locked C1 columns, but selected source data do not independently emit it",
    }

    normalization_attempt = {
        "conditional_deltaTheta": assembly["locked_solve"]["deltaTheta_conditional"],
        "conditional_residual_norm": assembly["locked_solve"]["residual_norm"],
        "conditional_condition_number": assembly["locked_solve"]["condition_number"],
        "selected_normalization_emitted": transfer["selected_status"]["selected_normalization_emitted"],
        "b_selected_emitted": assembly["selected_emission_status"]["b_selected_currently_emitted"],
        "verdict": "normalization is exact for the conditional solve, but not fixed by selected Hessian/kernel data",
    }

    overlap_source_attempt = {
        "selected_overlap_tensor_or_functor_emitted": False,
        "canonical_overlap_lane_retired_for_nonzero": previous["selected_overlap_transport"]["canonical_mode_conserving_overlap_zero"],
        "primitive_only_counterexample_imported": previous["selected_overlap_transport"]["primitive_only_span_insufficient"],
        "enriched_weyl_pair_conditionally_sufficient": previous["selected_overlap_transport"]["enriched_weyl_pair_span_sufficient_conditionally"],
        "required_as_selected_object": "source-to-C1 transfer functor or sector-resolved overlap tensor T_selected",
        "verdict": "the live object is a selected overlap/transfer theorem, not another algebraic target reconstruction",
    }

    matter_slot_evidence = {
        "su5_e6_structural_support": charge["selection_verdict"]["routeA_su5_e6_structural_match"]
        if "selection_verdict" in charge
        else "present_but_unselected",
        "honest_routec_uniformity_blocks_selected_split": hybrid["attempts"]["honest_routec_galerkin_fill"]["basis_transport"]["all_checked_family_bases_identical"],
        "su5_fixture_selected": hybrid["attempts"]["conditional_su5_fixture_fill"]["selected_by_mtt"],
        "singlet_1M_rule_present": hybrid["attempts"]["conditional_su5_fixture_fill"]["has_1M_singlet_neutrino_rule"],
        "verdict": "matter-slot clues point the right way but cannot yet promote sector routing",
    }

    legal_closure_routes = [
        {
            "route": "same-source matter-slot charge theorem",
            "status": "PRIMARY",
            "would_close": [
                "Z -> 10_M pair u/e",
                "X -> non-10 pair d/nuD with selected 1_M rule",
                "sector routing independent of locked target",
            ],
        },
        {
            "route": "selected overlap tensor/functor theorem",
            "status": "PRIMARY_PARALLEL",
            "would_close": [
                "T_selected(Z)=u/e I+Z",
                "T_selected(X)=d/nuD I+X",
                "normalization from trace/inner-product/Hessian kernel",
            ],
        },
        {
            "route": "full selected Galerkin source replay",
            "status": "FALLBACK",
            "would_close": [
                "selected D_E/dotD/alpha1 values",
                "non-identity matter-slot bases",
                "selected C1 matrices without conditional routing",
            ],
        },
    ]

    candidate = {
        "candidate": "MTTSelectedRouteCSelectedC1RoutingNormalizationAndOverlapSourcePacket",
        "status": STATUS,
        "inputs": {
            "previous_operator_overlap_packet": rel(PREVIOUS),
            "source_to_c1_transfer_map": rel(TRANSFER),
            "sector_routing_source_lemma": rel(SECTOR_ROUTING),
            "sector_charge_or_chirality_certificate": rel(SECTOR_CHARGE),
            "hybrid_matter_slot_packet": rel(HYBRID),
            "conditional_A_assembly": rel(A_ASSEMBLY),
        },
        "attempts": {
            "c1_routing": c1_routing_attempt,
            "normalization": normalization_attempt,
            "overlap_source": overlap_source_attempt,
            "matter_slot_evidence": matter_slot_evidence,
        },
        "legal_closure_routes": legal_closure_routes,
        "selection_verdict": {
            "selected_c1_routing_closed": False,
            "selected_transfer_normalization_closed": False,
            "selected_overlap_source_closed": False,
            "conditional_algebra_closed": conditional_exact and assembly["locked_solve"]["consistent"],
            "target_route_unique_relative_to_locked_columns": target_route["matches_locked_columns"],
            "best_next_object": NEXT,
        },
        "what_closes_now": {
            "conditional_route_Z_to_u_e_X_to_d_nuD_imported": True,
            "conditional_normalization_exactness_imported": True,
            "source_independent_selection_gap_identified": True,
            "legal_primary_routes_separated": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_same_source_matter_slot_charge_theorem": True,
            "prove_selected_overlap_transfer_functor": True,
            "fix_selected_transfer_normalization": True,
            "emit_selected_b_selected": True,
            "promote_conditional_A_to_A_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "mode": "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET",
            "using_one_straight_path": False,
            "paths_combined": [
                "source-level qutrit Weyl carrier",
                "conditional C1 transfer",
                "SU(5)/E6 matter-slot clue",
                "Route-C Galerkin identity-transport no-go",
            ],
            "locked_target_role": "localizes the only conditional route; does not select it as proof data",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
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
        """# MTT Selected Route-C C1 Routing, Normalization, and Overlap Source Packet

Status: `MTT_SELECTED_ROUTEC_C1_ROUTING_NORMALIZATION_OVERLAP_SOURCE_ATTEMPT_BUILT_SELECTION_STILL_OPEN`

This artifact tries to close the remaining selected C1 transfer gate.

## Result

The conditional calculation is exact:

```text
Z -> u/e
X -> d/nuD
deltaTheta = (1,1)
```

This is unique relative to the locked C1 columns, and the conditional residual
is numerical roundoff.

But this does not yet prove selected closure.  The selected source still does
not independently emit the sector routing, the transfer normalization, or the
overlap functor/tensor that promotes the conditional Weyl-pair operator to
`A_selected`.

## Live Routes

The primary routes are now:

- a same-source matter-slot charge theorem deriving `10_M -> u/e` and the
  non-`10_M`/`1_M` route for `d/nuD`,
- a selected overlap-transfer functor theorem deriving
  `T_selected(Z)=sector_route(u,e; I+Z)` and
  `T_selected(X)=sector_route(d,nuD; I+X)` with normalization,
- or a fallback full selected Galerkin replay emitting the same data directly.

Next artifact: `MTT_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
