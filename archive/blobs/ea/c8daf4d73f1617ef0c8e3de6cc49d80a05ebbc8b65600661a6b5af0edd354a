from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

C1_NOGO_IMPORT = ROOT / "certificates" / "routec_c1_primitive_response_on_smooth_bn_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_noninvariant_c1_primitive_search_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_noninvariant_c1_primitive_search.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_noninvariant_c1_primitive_search_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_noninvariant_c1_primitive_search_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_NonInvariant_C1_Primitive_Search_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    c1_import = load(C1_NOGO_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    candidates = src["candidate_primitives"]
    shifts = {str(item["primitive_fiber_shift"]) for item in candidates}
    nonzero_count = sum(
        1 for item in candidates if any(summary["max_abs_entry"] > 0 for summary in item["summary"].values())
    )

    closed_now = {
        "previous_canonical_C1_no_go_imported": c1_import["theorem"]["proved"],
        "canonical_zero_repaired_at_candidate_level": src_cert["what_closes"]["canonical_zero_repaired_at_candidate_level"],
        "finite_noninvariant_C1_candidate_matrices_emitted": src_cert["what_closes"]["finite_noninvariant_C1_candidate_matrices_emitted"],
        "minimal_active_shift_identified": src_cert["what_closes"]["minimal_active_shift_identified"],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    candidate_checks = {
        "minimal_active_shift_is_1_1": src["search_rule"]["minimal_active_shift_required"] == [1, 1],
        "tested_fiber_shifts_0_1_2_all": shifts == {"0", "1", "2", "all"},
        "four_nonzero_candidates_found": (
            nonzero_count == 4
            and src["calculation_results"]["nonzero_unselected_candidates_found"] == 4
            and src["calculation_results"]["all_four_tested_candidates_nonzero"] is True
        ),
        "all_candidates_unselected": all(item["selected_by_theorem"] is False for item in candidates),
        "all_candidates_use_no_observed_flavor_data": all(item["uses_observed_flavor_data"] is False for item in candidates),
        "selected_C1_not_closed": src["calculation_results"]["can_close_selected_C1_now"] is False,
    }

    still_open_checks = {
        "fiber_shift_selection_open": src["what_remains_open"]["fiber_shift_selection"] is True,
        "selected_noninvariant_C1_primitive_or_vertex_open": src["what_remains_open"]["selected_noninvariant_C1_primitive_or_vertex"] is True,
        "selected_basis_transport_theorem_open": src["what_remains_open"]["selected_basis_transport_theorem"] is True,
        "selected_dotD_source_verified_open": src["what_remains_open"]["selected_dotD_source_verified"] is True,
        "alpha1_driver_verified_open": src["what_remains_open"]["alpha1_driver_verified"] is True,
        "honest_replay_open": src["what_remains_open"]["honest_replay_without_lifted_flags"] is True,
        "yukawa_CKM_PMNS_open": src["what_remains_open"]["yukawa_CKM_PMNS_magnitudes"] is True,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
    }

    theorem = {
        "name": "RouteCNonInvariantC1PrimitiveSearchImportTheorem",
        "proved": all(closed_now.values()) and all(candidate_checks.values()) and all(still_open_checks.values()),
        "statement": (
            "The canonical C1 zero is repaired at candidate level by the minimal "
            "non-invariant active shift (1,1). Four nonzero candidate families "
            "are emitted for fiber shifts 0,1,2,all. None is selected-source "
            "proof until MTT derives the primitive, vertex correction, fiber "
            "rule, or basis transport from the q79/F,m=1 S3/GS branch."
        ),
    }

    verdict = {
        "nonzero_C1_candidates_found": True,
        "selected_C1_closed": False,
        "minimal_active_shift": [1, 1],
        "fiber_shifts_tested": [0, 1, 2, "all"],
        "fiber_rule_selected": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": src["next_required_artifact"],
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "calculation_results": src["calculation_results"],
        "search_rule": src["search_rule"],
        "candidate_summaries": [
            {
                "primitive_active_shift": item["primitive_active_shift"],
                "primitive_fiber_shift": item["primitive_fiber_shift"],
                "selected_by_theorem": item["selected_by_theorem"],
                "summary": item["summary"],
            }
            for item in candidates
        ],
        "closed_now": closed_now,
        "candidate_checks": candidate_checks,
        "still_open_checks": still_open_checks,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Non-Invariant C1 Primitive Search Import v1

## Result

The non-invariant C1 repair search has been imported.

The canonical C1 tensor vanishes because the `dotD` response has active mode
`(-1,-1)` while zero modes have `(0,0)`. The minimal repair therefore carries
active shift:

```text
(1,1)
```

The finite search emitted nonzero unselected candidates for:

```text
fiber shifts = 0, 1, 2, all
```

Each fixed fiber-shift candidate has rank-3 `u,d,e,nuD` matrices; the all-fiber
envelope has rank 1 in the emitted finite packet.

## Boundary

Selected C1 closure is still false. No observed Yukawa, CKM, PMNS, or mass data
were used.

The remaining proof object is one of:

```text
source theorem selecting the non-invariant primitive/vertex
fiber-rule audit selecting 0, 1, 2, or all from rho_E/Chan-Paton data
selected basis-transport theorem with the same finite effect
```

## Status

```text
ROUTEC_NONINVARIANT_C1_PRIMITIVE_SEARCH_IMPORTED_UNSELECTED_CANDIDATES_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_Primitive_Source_Selection_Theorem_or_FiberRule_Audit_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_noninvariant_c1_primitive_search_import",
                "status": "ROUTEC_NONINVARIANT_C1_PRIMITIVE_SEARCH_IMPORTED_UNSELECTED_CANDIDATES_OPEN",
                "input_certificates": {
                    "routec_c1_primitive_response_on_smooth_bn_import": str(C1_NOGO_IMPORT),
                    "selected_routec_noninvariant_c1_primitive_search": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "candidate_checks": candidate_checks,
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
    print("STATUS: ROUTEC_NONINVARIANT_C1_PRIMITIVE_SEARCH_IMPORTED_UNSELECTED_CANDIDATES_OPEN")


if __name__ == "__main__":
    main()
