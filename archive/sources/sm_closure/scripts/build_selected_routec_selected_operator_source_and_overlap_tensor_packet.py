"""Audit the selected operator-source and overlap-tensor packet.

The hybrid matter-slot packet reduced the frontier to selected operator-source
data plus sector-resolved overlap/transport data.  This builder consolidates
the later Weyl-pair chain and asks whether the existing corpus now supplies
that exact selected packet, without using observed SM targets.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

HYBRID = DATA / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json"
C1_EMISSION = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
C1_REBUILD = DATA / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild.candidate.json"
WEYL_GATE = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
A_ASSEMBLY = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
TRANSFER = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
SECTOR_ROUTING = DATA / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json"
SECTOR_CHARGE = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"

OUTPUT = DATA / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"
CERT = CERTS / "selected_routec_selected_operator_source_and_overlap_tensor_packet_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_OVERLAP_PACKET_AUDITED_SOURCE_LEVEL_CARRIER_CLOSED_SELECTED_C1_ROUTING_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_C1_Routing_Normalization_and_Overlap_Source_Packet_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def bool_path(data: dict[str, Any], keys: list[str]) -> bool:
    cur: Any = data
    for key in keys:
        cur = cur[key]
    return bool(cur)


def main() -> None:
    hybrid = load(HYBRID)
    c1_emission = load(C1_EMISSION)
    c1_rebuild = load(C1_REBUILD)
    weyl_gate = load(WEYL_GATE)
    a_assembly = load(A_ASSEMBLY)
    provenance = load(PROVENANCE)
    transfer = load(TRANSFER)
    sector_routing = load(SECTOR_ROUTING)
    sector_charge = load(SECTOR_CHARGE)

    selected_operator_source = {
        "selected_DE_source_verified": hybrid["attempts"]["honest_routec_galerkin_fill"]["source_flags"]["selected_DE_source_verified"],
        "selected_dotD_source_verified": hybrid["attempts"]["honest_routec_galerkin_fill"]["source_flags"]["selected_dotD_source_verified"],
        "alpha1_driver_verified": hybrid["attempts"]["honest_routec_galerkin_fill"]["source_flags"]["alpha1_driver_verified"],
        "A_selected_emitted": c1_emission["emission_audit"]["selected_operator_A_selected_emitted"],
        "b_selected_emitted": c1_emission["emission_audit"]["selected_source_vector_b_selected_emitted"],
        "same_branch_source_level_weyl_carrier_closed": provenance["source_level_weyl_carrier"]["proved"],
        "active_shift_1_1_provenance_closed": provenance["active_shift_provenance"]["proved"],
        "verdict": "source-level carrier closed; selected C1 operator source still not emitted",
    }

    selected_overlap_transport = {
        "canonical_mode_conserving_overlap_zero": c1_emission["response_lanes"]["canonical_smooth_bn_response"]["nonzero_response_found"] is False,
        "noninvariant_candidates_exist_but_unselected": c1_rebuild["supporting_facts"]["nonzero_unselected_candidates_found"] > 0,
        "primitive_only_span_insufficient": bool_path(
            load(DATA / "selected_routec_basis_transport_primitive_source_proof_or_counterexample.candidate.json"),
            ["source_attempt", "counterexample_proved"],
        ),
        "enriched_weyl_pair_span_sufficient_conditionally": weyl_gate["span_test"]["target_in_span"],
        "conditional_weylpair_solve_exact": a_assembly["locked_solve"]["consistent"],
        "conditional_source_to_C1_transfer_exact": transfer["conditional_transfer_map"]["conditional_exact"],
        "selected_sector_routing_emitted": transfer["selected_status"]["selected_sector_routing_emitted"],
        "selected_transfer_normalization_emitted": transfer["selected_status"]["selected_normalization_emitted"],
        "sector_charge_certificate_selected": sector_charge["selection_verdict"]["selected_operator_source_present"]
        if "selection_verdict" in sector_charge
        else False,
        "verdict": "conditional Weyl-pair overlap/transport is algebraically enough; selected sector routing and normalization remain open",
    }

    route_matrix = [
        {
            "route": "straight selected Hessian/operator path",
            "status": "OPEN",
            "closes_packet": False,
            "evidence": "selected finite Hessian/source/response entries are still null or source-flagged open",
        },
        {
            "route": "canonical smooth B_N overlap path",
            "status": "RETIRED_FOR_NONZERO_C1",
            "closes_packet": False,
            "evidence": "canonical mode-conserving one-response matrices vanish",
        },
        {
            "route": "non-invariant primitive-only path",
            "status": "COUNTEREXAMPLE",
            "closes_packet": False,
            "evidence": "primitive-only span does not contain the locked Weyl-pair splitter target",
        },
        {
            "route": "constrained superset Weyl-pair carrier plus conditional transfer",
            "status": "BEST_FRONTIER",
            "closes_packet": False,
            "evidence": "source-level Z/X carrier and active shift are proved; conditional A solves exactly; selected sector routing/normalization is not emitted",
        },
    ]

    missing_selected_object = {
        "name": NEXT,
        "must_emit": [
            "selected source-to-C1 transfer functor or overlap tensor T_selected",
            "selected sector routing Z -> u/e and X -> d/nuD independent of the locked target",
            "selected transfer normalization compatible with the Hessian/kernel basis",
            "selected b_selected or proof that the locked b_splitter is the emitted source vector",
            "same-branch promotion of conditional A_weylpair to A_selected",
        ],
        "forbidden_shortcuts": [
            "choosing routing because it matches the locked target columns",
            "promoting SU(5) fixture data while source.selected_by_mtt=false",
            "using observed masses, CKM, PMNS, or CP phase",
            "using lifted selected flags as proof",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedRouteCSelectedOperatorSourceAndOverlapTensorPacket",
        "status": STATUS,
        "inputs": {
            "hybrid_matter_slot_packet": rel(HYBRID),
            "selected_c1_response_operator_emission": rel(C1_EMISSION),
            "smart_c1_rebuild_iteration": rel(C1_REBUILD),
            "weylpair_source_gate": rel(WEYL_GATE),
            "conditional_A_assembly": rel(A_ASSEMBLY),
            "weylpair_source_provenance": rel(PROVENANCE),
            "source_to_c1_transfer_map": rel(TRANSFER),
            "sector_routing_source_lemma": rel(SECTOR_ROUTING),
            "sector_charge_or_chirality_certificate": rel(SECTOR_CHARGE),
        },
        "packet_goal": {
            "previous_frontier": hybrid["next_required_artifact"],
            "goal": "selected operator source plus selected sector-resolved overlap/transport tensor",
            "closed_now": False,
        },
        "selected_operator_source": selected_operator_source,
        "selected_overlap_transport": selected_overlap_transport,
        "route_matrix": route_matrix,
        "best_current_statement": {
            "source_level_ZX_carrier_closed": True,
            "active_shift_1_1_closed": True,
            "conditional_A_weylpair_exact": True,
            "selected_A_selected_closed": False,
            "selected_overlap_tensor_closed": False,
            "selected_sector_routing_closed": False,
            "full_SM_or_no_knob_closure": False,
        },
        "missing_selected_object": missing_selected_object,
        "superset_strategy": {
            "mode": "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET",
            "paths_combined": [
                "selected S3/GS source-level Weyl carrier",
                "Route-C Galerkin/projector/dotD scaffold",
                "conditional Weyl-pair C1 transfer",
                "SU(5)/E6 matter-slot clue as unpromoted support",
            ],
            "straight_path_status": "straight selected Hessian/operator path remains open",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "what_closes_now": {
            "selected_operator_source_and_overlap_frontier_consolidated": True,
            "source_level_weyl_carrier_and_active_shift_imported_as_closed": True,
            "conditional_exact_A_and_transfer_imported": True,
            "canonical_zero_and_primitive_only_failure_kept_retired": True,
            "missing_selected_C1_routing_normalization_overlap_object_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_sector_routing_Z_to_u_e_X_to_d_nuD": True,
            "selected_transfer_normalization": True,
            "selected_overlap_tensor_or_transfer_functor": True,
            "promote_conditional_A_to_A_selected": True,
            "emit_theorem_derived_b_selected": True,
            "run_honest_selected_deltaTheta_C1_solve": True,
            "full_SM_or_no_knob_closure": True,
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
        """# MTT Selected Route-C Operator Source and Overlap Tensor Packet

Status: `MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_OVERLAP_PACKET_AUDITED_SOURCE_LEVEL_CARRIER_CLOSED_SELECTED_C1_ROUTING_OPEN`

This packet consolidates the current frontier after the hybrid matter-slot
Galerkin audit.

## What Is Closed

The selected q79/F,m=1 S3/Green-Schwarz source gives a source-level qutrit Weyl
carrier: the phase-like `Z` and shift-like `X` carrier is closed at source
level, and the active deck shift `(1,1)` has provenance.

The conditional Weyl-pair operator is also algebraically sufficient.  If the
source emits the two columns

```text
u/e   <- I + Z
d/nuD <- I + X
```

then the conditional 72x2 operator solves the locked splitter equation up to
roundoff.

## What Is Not Closed

This is not yet selected `A_selected`.  Current artifacts do not emit:

- the selected source-to-C1 transfer functor or overlap tensor,
- the selected sector routing `Z -> u/e` and `X -> d/nuD`,
- the selected transfer normalization,
- the theorem-derived `b_selected`.

The canonical smooth `B_N` overlap gives zero one-response matrices, and the
primitive-only non-invariant span has a counterexample.  The live route is the
constrained superset Weyl-pair carrier plus selected C1 routing/normalization.

Next artifact: `MTT_Selected_RouteC_Selected_C1_Routing_Normalization_and_Overlap_Source_Packet_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
