"""Build the Route-C basis-transport / primitive source theorem slot.

This artifact records the exact theorem to be inserted into the papers later.
It separates the finite lemmas already proved from the still-open selected
source-emission premise.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
DRAFT_DIR = CORPUS / "paper_appendix_drafts" / "selected_source"

PREVIOUS = DATA / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild.candidate.json"
PRIMITIVE_AUDIT = DATA / "selected_routec_primitive_source_selection_audit.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
PAPER_MANIFEST = DATA / "selected_source_paper_integration_manifest.candidate.json"

OUTPUT = DATA / "selected_routec_basis_transport_primitive_source_theorem.candidate.json"
CERT = CERTS / "selected_routec_basis_transport_primitive_source_theorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN"
NEXT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def paper_draft_text(paper_key: str, paper_path: str) -> str:
    return f"""# I7. Selected Basis-Transport Primitive Source Theorem

Target paper: `{paper_key}`

Target file: `{paper_path}`

## Theorem Slot

For the selected q79/F,m=1 S3/Green-Schwarz Route-C branch, the same-branch
basis transport or vertex correction emits the active deck shift `(1,1)`
non-invariant primitive.  The fixed qutrit fiber shifts `0`, `1`, and `2` form
a quotient gauge class for downstream observables, so shift `0` may be used as
the computation representative only after the quotient statement is invoked.

## What Is Already Proved

- finite momentum bookkeeping forces active shift `(1,1)` for nonzero C1 response,
- fixed qutrit fiber shifts are finite gauge-equivalent at the current C1 layer,
- the non-invariant finite candidates are nonzero rank-3 candidates,
- the canonical smooth B_N one-response lane is zero,
- observed masses, mixings, CP phase, thresholds, and benchmark entries are not used.

## Proof Obligations Still Open

- derive the basis transport or vertex primitive from the selected q79/F,m=1 source,
- lift the fixed-fiber quotient from the current C1 layer to the downstream response observables,
- emit the promoted primitive as selected source data,
- assemble `A_selected` and `b_selected`,
- solve or reject `A_selected * deltaTheta_C1 = b_splitter`.

## Safe Wording Before Proof

The finite search identifies the unique active nonzero primitive class and the
paper may use it as the next proof target.  It does not promote the primitive,
`A_selected`, or any flavor result until the selected source-emission theorem is
proved.  No observed masses, mixings, thresholds, or fitted constants are source
selectors.
"""


def main() -> None:
    previous = load(PREVIOUS)
    primitive = load(PRIMITIVE_AUDIT)
    noninv = load(NONINV)
    dotd = load(DOTD)
    paper_manifest = load(PAPER_MANIFEST)

    active = primitive["active_shift_theorem"]["enumeration"]
    fixed = primitive["fiber_class_theorem"]["fixed_fiber_shifts"]
    fixed_equivalent = all(
        item["equivalent"] is True
        for item in fixed["equivalence_to_shift_0_on_u"].values()
    )
    solution_kernel = previous["solution_space_iteration"]["selected_solution_kernel"]

    theorem_slot = {
        "id": "I7_basis_transport_primitive_source_theorem",
        "name": "SelectedBasisTransportPrimitiveSourceTheorem",
        "status": "THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN",
        "formal_statement": (
            "For the selected q79/F,m=1 S3/Green-Schwarz Route-C branch, the same-branch "
            "basis transport or vertex correction emits the active deck shift (1,1) non-invariant "
            "C1 primitive. The fixed qutrit fiber shifts 0,1,2 form a quotient gauge class for "
            "downstream response observables, so the shift-0 representative may be used as a computation "
            "gauge. Consequently the emitted primitive is eligible to assemble A_selected for the locked "
            "DeltaTheta solve, without observed flavor targets or lifted flags."
        ),
        "proved_now": {
            "active_shift_1_1_unique_for_nonzero_response": active["nonzero_active_shifts"] == [[1, 1]],
            "active_shift_necessary_and_sufficient": active["active_shift_necessary_and_sufficient_for_nonzero"] is True,
            "fixed_fiber_shifts_finite_gauge_equivalent_current_layer": fixed_equivalent,
            "nonzero_rank3_candidates_exist": noninv["calculation_results"]["nonzero_unselected_candidates_found"] > 0,
            "dotd_projector_scaffold_available": dotd["what_closes_now"]["dotD_alpha1_matrix_in_same_basis_emitted"] is True,
            "best_lane_selected_by_solution_iteration": solution_kernel["selected_next_lane"] == "L3_noninvariant_basis_transport_or_vertex_source",
        },
        "not_proved_now": {
            "selected_source_emits_basis_transport_or_vertex_primitive": True,
            "fixed_fiber_quotient_lifted_to_downstream_response_observables": True,
            "primitive_promoted_to_selected_source_data": True,
            "A_selected_assembled": True,
            "b_selected_emitted": True,
            "splitter_equation_solved": True,
        },
        "proof_obligations": [
            "Identify the same-branch geometric operation: basis transport, vertex correction, or equivalent primitive source.",
            "Derive active deck shift (1,1) from the selected q79/F,m=1 S3/GS source rather than from desired flavor output.",
            "Prove fixed qutrit fiber shifts 0,1,2 are a quotient gauge class for the downstream C1 response observables.",
            "Emit the selected primitive/transport in the same B_N, dotD, projector, and zero-mode basis.",
            "Assemble A_selected and b_selected and run the locked DeltaTheta consistency test.",
        ],
        "forbidden_shortcuts": [
            "using observed masses, CKM, PMNS, or CP phase to choose the primitive",
            "using lifted selected flags as proof",
            "choosing fiber shift 0 without the quotient/gauge-class statement",
            "treating nonzero unselected candidates as selected source data",
        ],
    }

    target_papers = ["theta_execution_flavor", "theta_nonabelian_overlaps", "strominger_system"]
    paper_update_record = {
        "id": theorem_slot["id"],
        "section_title": "Selected Basis-Transport Primitive Source Theorem",
        "status": "PAPER_PROOF_SLOT_DRAFTED_SOURCE_PROOF_OPEN",
        "target_papers": target_papers,
        "target_paths": {key: paper_manifest["papers"][key] for key in target_papers},
        "current_blockers_resolved_if_proved": [
            "selected_noninvariant_C1_primitive_or_vertex",
            "selected_basis_transport_between_zero_and_response_modes",
            "A_selected emission from promoted primitive",
            "fixed qutrit fiber representative selection/quotient",
        ],
        "safe_wording": (
            "Use this as a theorem target only until source emission is proved; finite nonzero candidates remain unselected diagnostics."
        ),
    }

    DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    draft_paths = {}
    for key, paper_path in paper_update_record["target_paths"].items():
        draft = DRAFT_DIR / f"{key}__i7_basis_transport_primitive_source_theorem.md"
        draft.write_text(paper_draft_text(key, paper_path), encoding="utf-8")
        draft_paths[key] = rel(draft)
    paper_update_record["draft_paths"] = draft_paths

    candidate = {
        "candidate": "MTTSelectedRouteCBasisTransportPrimitiveSourceTheorem",
        "status": STATUS,
        "inputs": {
            "smart_c1_rebuild_iteration": rel(PREVIOUS),
            "primitive_source_selection_audit": rel(PRIMITIVE_AUDIT),
            "noninvariant_c1_primitive_search": rel(NONINV),
            "sector_projectors_dotd": rel(DOTD),
            "paper_integration_manifest": rel(PAPER_MANIFEST),
        },
        "theorem_slot": theorem_slot,
        "paper_update_record": paper_update_record,
        "what_closes_now": {
            "named_theorem_slot_added": True,
            "finite_support_lemmas_packaged": True,
            "paper_update_targets_recorded": True,
            "appendix_drafts_written": True,
            "overclaim_guardrails_recorded": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_selected_basis_transport_or_vertex_source": True,
            "prove_downstream_fiber_quotient_or_select_fiber_origin": True,
            "emit_A_selected_and_b_selected": True,
            "solve_or_reject_splitter_equation": True,
            "update_target_papers_after_proof": True,
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
                "draft_paths": draft_paths,
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
        """# MTT Selected Route-C BasisTransport Primitive Source Theorem

Status: `MTT_SELECTED_ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN`

This artifact adds the named theorem slot needed by the selected C1 rebuild.

## Theorem Statement

For the selected q79/F,m=1 S3/Green-Schwarz Route-C branch, the same-branch
basis transport or vertex correction emits the active deck shift `(1,1)`
non-invariant C1 primitive.  The fixed qutrit fiber shifts `0`, `1`, and `2`
form a quotient gauge class for downstream response observables, so the shift-0
representative may be used as a computation gauge.  Consequently the emitted
primitive is eligible to assemble `A_selected` for the locked DeltaTheta solve,
without observed flavor targets or lifted flags.

## Proved Now

- active shift `(1,1)` is uniquely nonzero for the finite one-response C1 primitive search,
- fixed qutrit fiber shifts are gauge-equivalent at the current finite layer,
- nonzero rank-3 finite candidates exist,
- the dotD/projector scaffold exists in the same finite basis,
- the smart solution iteration selects this lane as the minimal next proof target.

## Still Open

The selected source-emission part of the theorem is not proved yet.  We still
must derive the basis transport or vertex primitive from the selected
q79/F,m=1 S3/GS source, lift the fixed-fiber quotient to downstream response
observables, emit `A_selected` and `b_selected`, then solve or reject the
splitter equation.

## Paper Update Record

Draft proof slots were written for:

- `theta_execution_flavor`,
- `theta_nonabelian_overlaps`,
- `strominger_system`.

These drafts are safe to insert only as proof slots until the source theorem is
proved.  They do not promote diagnostic candidates.

Next artifact: `MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
