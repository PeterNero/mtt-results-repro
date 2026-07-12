from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_selected_c1_operator_source_rebuild_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_basis_transport_primitive_source_theorem_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_basis_transport_primitive_source_theorem.candidate.json"
SRC_NOTE = SM / "proof_corpus" / "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1.md"

OUT_CERT = ROOT / "certificates" / "routec_basistransport_primitive_source_theorem_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_basistransport_primitive_source_theorem_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_BasisTransport_Primitive_Source_Theorem_Import_v1.md"

STATUS = "ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_THEOREM_SLOT_IMPORTED_SOURCE_PROOF_OPEN"
SOURCE_STATUS = "MTT_SELECTED_ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    src_note = SRC_NOTE.read_text(encoding="utf-8")

    theorem_slot = src["theorem_slot"]
    paper_record = src["paper_update_record"]

    input_checks = {
        "previous_rebuild_import_proved": prev["theorem"]["proved"] is True,
        "previous_next_artifact_matches": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1",
        "source_status_matches": src["status"] == SOURCE_STATUS,
        "certificate_status_matches": src_cert["status"] == SOURCE_STATUS,
        "next_artifact_matches": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    finite_support_checks = {
        "active_shift_unique": theorem_slot["proved_now"]["active_shift_1_1_unique_for_nonzero_response"]
        is True,
        "active_shift_necessary_and_sufficient": theorem_slot["proved_now"][
            "active_shift_necessary_and_sufficient"
        ]
        is True,
        "best_lane_selected": theorem_slot["proved_now"]["best_lane_selected_by_solution_iteration"]
        is True,
        "finite_fiber_gauge_class": theorem_slot["proved_now"][
            "fixed_fiber_shifts_finite_gauge_equivalent_current_layer"
        ]
        is True,
        "nonzero_rank3_candidates_exist": theorem_slot["proved_now"]["nonzero_rank3_candidates_exist"]
        is True,
        "dotd_projector_scaffold_available": theorem_slot["proved_now"][
            "dotd_projector_scaffold_available"
        ]
        is True,
    }

    theorem_slot_checks = {
        "named_theorem_slot": theorem_slot["name"] == "SelectedBasisTransportPrimitiveSourceTheorem",
        "formal_statement_names_active_shift": "active deck shift (1,1)"
        in theorem_slot["formal_statement"],
        "formal_statement_excludes_observed_targets": "without observed flavor targets or lifted flags"
        in theorem_slot["formal_statement"],
        "five_proof_obligations_recorded": len(theorem_slot["proof_obligations"]) == 5,
        "forbidden_shortcuts_recorded": len(theorem_slot["forbidden_shortcuts"]) == 4,
    }

    open_gate_checks = {
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "source_emission_open": theorem_slot["not_proved_now"][
            "selected_source_emits_basis_transport_or_vertex_primitive"
        ]
        is True,
        "fiber_quotient_lift_open": theorem_slot["not_proved_now"][
            "fixed_fiber_quotient_lifted_to_downstream_response_observables"
        ]
        is True,
        "primitive_promotion_open": theorem_slot["not_proved_now"][
            "primitive_promoted_to_selected_source_data"
        ]
        is True,
        "a_selected_open": theorem_slot["not_proved_now"]["A_selected_assembled"] is True,
        "b_selected_open": theorem_slot["not_proved_now"]["b_selected_emitted"] is True,
        "splitter_solve_open": theorem_slot["not_proved_now"]["splitter_equation_solved"] is True,
    }

    paper_checks = {
        "paper_slot_id_matches": paper_record["id"] == theorem_slot["id"],
        "three_target_papers": set(paper_record["target_papers"])
        == {"theta_execution_flavor", "theta_nonabelian_overlaps", "strominger_system"},
        "three_draft_paths": len(paper_record["draft_paths"]) == 3,
        "safe_wording_guarded": "theorem target only until source emission is proved"
        in paper_record["safe_wording"],
        "paper_status_open": paper_record["status"] == "PAPER_PROOF_SLOT_DRAFTED_SOURCE_PROOF_OPEN",
    }

    certificate_checks = {
        "what_closes_agree": all(src_cert["what_closes"].values()),
        "remaining_open_agree": all(src_cert["what_remains_open"].values()),
        "certificate_next_matches": src_cert["next_required_artifact"] == NEXT_ARTIFACT,
        "note_records_proof_open": "source-emission part of the theorem is not proved yet"
        in src_note,
    }

    theorem = {
        "name": "RouteCBasisTransportPrimitiveSourceTheoremSlotImport",
        "proved": all(input_checks.values())
        and all(finite_support_checks.values())
        and all(theorem_slot_checks.values())
        and all(open_gate_checks.values())
        and all(paper_checks.values())
        and all(certificate_checks.values()),
        "statement": (
            "The selected Route-C basis-transport primitive source theorem slot "
            "is imported with its finite support lemmas and paper insertion "
            "targets. It proves only that the theorem target is well specified "
            "and guarded: active shift (1,1) is the finite nonzero lane, fixed "
            "fiber shifts are a current finite gauge class, and no observed "
            "flavor data or lifted flags are used. It does not prove selected "
            "source emission, A_selected/b_selected emission, or the splitter "
            "equation."
        ),
    }

    verdict = {
        "theorem_slot_imported": True,
        "finite_support_lemmas_packaged": True,
        "paper_proof_slot_imported": True,
        "selected_source_emission_proved": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "splitter_equation_solved": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "input_checks": input_checks,
        "finite_support_checks": finite_support_checks,
        "theorem_slot_checks": theorem_slot_checks,
        "open_gate_checks": open_gate_checks,
        "paper_checks": paper_checks,
        "certificate_checks": certificate_checks,
        "theorem_slot": theorem_slot,
        "paper_update_record": paper_record,
        "what_closes_now": src["what_closes_now"],
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C BasisTransport Primitive Source Theorem Import v1

## Result

The selected Route-C basis-transport primitive source theorem slot is now
imported.

What is packaged:

```text
active deck shift (1,1) is the unique finite nonzero C1 lane
fixed qutrit fiber shifts 0,1,2 are a current finite gauge class
nonzero rank-3 candidates exist
dotD/projector scaffold exists in the same finite basis
the target theorem and paper insertion slots are named
```

## Boundary

This is not yet the source theorem.

Still open:

```text
derive the basis transport or vertex primitive from the selected q79/F,m=1 S3/GS source
lift the fixed-fiber quotient to downstream response observables
emit A_selected and b_selected
solve or reject A_selected * deltaTheta_C1 = b_splitter
```

No observed masses, CKM/PMNS entries, CP phase, thresholds, or lifted selected
flags are used as selectors.

## Status

```text
ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_THEOREM_SLOT_IMPORTED_SOURCE_PROOF_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_basistransport_primitive_source_theorem_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_selected_c1_operator_source_rebuild_import": str(PREV_IMPORT),
                    "selected_routec_basis_transport_primitive_source_theorem": str(SRC_CERT),
                },
                "theorem": theorem,
                "input_checks": input_checks,
                "finite_support_checks": finite_support_checks,
                "theorem_slot_checks": theorem_slot_checks,
                "open_gate_checks": open_gate_checks,
                "paper_checks": paper_checks,
                "certificate_checks": certificate_checks,
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
