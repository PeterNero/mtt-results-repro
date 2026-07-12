from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_selected_c1_response_operator_emission_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_selected_c1_operator_source_rebuild_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_selected_c1_operator_source_rebuild_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Selected_C1_Operator_Source_Rebuild_Import_v1.md"

STATUS = "ROUTEC_SELECTED_C1_OPERATOR_SOURCE_REBUILD_IMPORTED_BASISTRANSPORT_NEXT"
NEXT_ARTIFACT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    iteration = src["solution_space_iteration"]
    selected = iteration["selected_solution_kernel"]
    facts = src["supporting_facts"]
    ranked = iteration["ranked_lanes"]

    closed_now = {
        "previous_selected_c1_response_operator_imported": prev["theorem"]["proved"],
        "source_theorem_proved": src["theorem"]["proved"],
        "solution_space_ranked": src_cert["what_closes"]["solution_space_ranked"],
        "best_next_lane_selected": src_cert["what_closes"]["best_next_lane_selected"],
        "active_shift_forced_imported": src_cert["what_closes"]["active_shift_forced_imported"],
        "fiber_gauge_class_imported": src_cert["what_closes"]["fiber_gauge_class_imported"],
        "zero_and_unselected_lanes_separated": src_cert["what_closes"][
            "zero_and_unselected_lanes_separated"
        ],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    ranking_checks = {
        "four_lanes_ranked": len(ranked) == 4,
        "top_lane_is_basis_transport": ranked[0]["lane"] == "L3_noninvariant_basis_transport_or_vertex_source",
        "top_lane_score_exceeds_second": ranked[0]["score"] > ranked[1]["score"],
        "full_rebuild_kept_as_fallback": iteration["search_space_pruned"]["full_rebuild_kept_as_fallback"]
        is True,
        "zero_canonical_lane_retired_for_flavor": iteration["search_space_pruned"][
            "zero_canonical_lane_retired_for_flavor_splitting"
        ]
        is True,
        "observed_targets_removed": iteration["search_space_pruned"]["observed_target_fits_removed"] is True,
        "lifted_flag_proofs_removed": iteration["search_space_pruned"]["lifted_flag_proofs_removed"] is True,
    }

    selected_lane_checks = {
        "selected_next_lane_basis_transport": selected["selected_next_lane"]
        == "L3_noninvariant_basis_transport_or_vertex_source",
        "active_shift_unique": selected["active_shift_unique"] is True,
        "forced_active_shift_1_1": selected["forced_active_shift"] == [[1, 1]],
        "fixed_fiber_shifts_gauge_equivalent": selected["fixed_fiber_shifts_gauge_equivalent"] is True,
        "computation_gauge_mentions_shift0": "shift 0" in selected["computation_gauge"],
        "minimal_theorem_names_basis_transport": "basis transport" in selected[
            "minimal_theorem_to_prove_next"
        ],
    }

    support_checks = {
        "active_shift_necessary_and_sufficient": facts["active_shift_necessary_and_sufficient_for_nonzero"]
        is True,
        "unique_nonzero_active_shift_1_1": facts["unique_nonzero_active_shift"] == [[1, 1]],
        "nonzero_unselected_candidates_found": facts["nonzero_unselected_candidates_found"] > 0,
        "canonical_response_zero": facts["canonical_response_zero"] is True,
        "dotd_projector_scaffold_exists": facts["dotd_projector_scaffold_exists"] is True,
        "fixed_fiber_shifts_gauge_equivalent": facts["fixed_fiber_shifts_gauge_equivalent"] is True,
    }

    open_gate_checks = {
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "next_artifact_basis_transport": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    still_open_checks = {key: value is True for key, value in src["what_remains_open"].items()}

    theorem = {
        "name": "RouteCSelectedC1OperatorSourceRebuildImportTheorem",
        "proved": all(closed_now.values())
        and all(ranking_checks.values())
        and all(selected_lane_checks.values())
        and all(support_checks.values())
        and all(open_gate_checks.values())
        and all(still_open_checks.values()),
        "statement": (
            "The imported C1 operator-source rebuild iteration ranks the rebuild "
            "space without target fitting and selects the non-invariant basis-"
            "transport/vertex source lane as the minimal next proof target. "
            "Active shift (1,1) is forced, fixed qutrit fibers form one gauge "
            "class, and this lane is the shortest route that can promote a "
            "nonzero primitive and emit A_selected. The theorem is a strategy "
            "reduction, not the selected source proof itself."
        ),
    }

    verdict = {
        "best_next_lane": selected["selected_next_lane"],
        "forced_active_shift": [1, 1],
        "fixed_fiber_class_available": True,
        "canonical_zero_lane_retired_for_flavor": True,
        "full_rebuild_fallback_kept": True,
        "A_selected_emitted": False,
        "selected_source_theorem_proved": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "closed_now": closed_now,
        "ranking_checks": ranking_checks,
        "selected_lane_checks": selected_lane_checks,
        "support_checks": support_checks,
        "open_gate_checks": open_gate_checks,
        "still_open_checks": still_open_checks,
        "solution_space_iteration": iteration,
        "supporting_facts": facts,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Selected C1 Operator Source Rebuild Import v1

## Result

The selected C1 rebuild space is ranked and pruned.

The best next lane is:

```text
L3_noninvariant_basis_transport_or_vertex_source
```

Why it wins:

```text
active deck shift (1,1) is forced
fixed qutrit fiber shifts 0,1,2 form one gauge class
nonzero rank-3 finite candidates exist
the existing dotD/projector scaffold can be reused
no observed targets or lifted flags are needed
```

The straight selected-Hessian lane has the right schema but null finite values.
The canonical smooth B_N lane is computed but zero. The full smooth
Iwasawa/Strominger rebuild remains a rigorous fallback, but it is broader than
the next needed proof.

## Next Theorem

Prove the selected basis-transport / vertex primitive theorem:

```text
the selected q79/F,m=1 S3/GS Route-C source emits the active shift (1,1)
non-invariant primitive, while fixed qutrit fiber shifts 0,1,2 are a quotient
gauge class for downstream observables
```

If that theorem closes, shift 0 can be used as computation gauge and the
nonzero rank-3 primitive can be promoted toward `A_selected`.

## Status

```text
ROUTEC_SELECTED_C1_OPERATOR_SOURCE_REBUILD_IMPORTED_BASISTRANSPORT_NEXT
```

The next required artifact is:

```text
MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_selected_c1_operator_source_rebuild_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_selected_c1_response_operator_emission_import": str(PREV_IMPORT),
                    "selected_routec_selected_c1_operator_source_or_galerkin_rebuild": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "ranking_checks": ranking_checks,
                "selected_lane_checks": selected_lane_checks,
                "support_checks": support_checks,
                "open_gate_checks": open_gate_checks,
                "still_open_checks": still_open_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
