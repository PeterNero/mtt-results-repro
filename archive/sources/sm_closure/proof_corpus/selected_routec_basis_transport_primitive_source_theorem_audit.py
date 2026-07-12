"""Audit Route-C basis-transport primitive source theorem slot."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_basis_transport_primitive_source_theorem.candidate.json"
CERT = REPO / "certificates" / "selected_routec_basis_transport_primitive_source_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN"
NEXT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    theorem = data["theorem_slot"]
    paper = data["paper_update_record"]
    draft_texts = {
        key: (REPO / path).read_text(encoding="utf-8")
        for key, path in paper["draft_paths"].items()
    }

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "theorem slot named",
            theorem["id"] == "I7_basis_transport_primitive_source_theorem"
            and theorem["name"] == "SelectedBasisTransportPrimitiveSourceTheorem"
            and "active deck shift (1,1)" in theorem["formal_statement"]
            and "without observed flavor targets or lifted flags" in theorem["formal_statement"],
            theorem,
        ),
        check(
            "finite lemmas packaged",
            theorem["proved_now"]["active_shift_1_1_unique_for_nonzero_response"] is True
            and theorem["proved_now"]["fixed_fiber_shifts_finite_gauge_equivalent_current_layer"] is True
            and theorem["proved_now"]["nonzero_rank3_candidates_exist"] is True
            and theorem["proved_now"]["dotd_projector_scaffold_available"] is True,
            theorem["proved_now"],
        ),
        check(
            "source proof still open",
            theorem["not_proved_now"]["selected_source_emits_basis_transport_or_vertex_primitive"] is True
            and theorem["not_proved_now"]["A_selected_assembled"] is True
            and theorem["not_proved_now"]["splitter_equation_solved"] is True,
            theorem["not_proved_now"],
        ),
        check(
            "paper update targets",
            paper["id"] == theorem["id"]
            and set(paper["target_papers"]) == {"theta_execution_flavor", "theta_nonabelian_overlaps", "strominger_system"}
            and len(paper["draft_paths"]) == 3,
            paper,
        ),
        check(
            "draft files guarded",
            all("Safe Wording Before Proof" in text for text in draft_texts.values())
            and all("No observed masses, mixings, thresholds, or fitted constants" in text for text in draft_texts.values())
            and all("does not promote" in text for text in draft_texts.values()),
            paper["draft_paths"],
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check(
            "remaining proof obligations",
            data["what_remains_open"]["prove_selected_basis_transport_or_vertex_source"] is True
            and data["what_remains_open"]["emit_A_selected_and_b_selected"] is True
            and data["what_remains_open"]["update_target_papers_after_proof"] is True,
            data["what_remains_open"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records theorem",
            "Theorem Statement" in note
            and "active deck shift `(1,1)`" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C basis-transport primitive source theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
