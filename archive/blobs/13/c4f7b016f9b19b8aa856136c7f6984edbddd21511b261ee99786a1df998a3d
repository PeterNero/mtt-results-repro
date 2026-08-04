"""Audit Route-C basis-transport primitive source proof/counterexample."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_basis_transport_primitive_source_proof_or_counterexample.candidate.json"
CERT = REPO / "certificates" / "selected_routec_basis_transport_primitive_source_proof_or_counterexample_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_COUNTEREXAMPLE_BUILT_PRIMITIVE_ONLY_SPAN_INSUFFICIENT"
NEXT = "MTT_Selected_RouteC_WeylPair_BasisTransport_or_Vertex_Source_Theorem_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    source = data["source_attempt"]
    spans = data["span_tests"]
    refined = data["refined_next_theorem"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "superset discipline",
            data["superset_strategy"]["mode"] == "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET"
            and data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["lifted_flags_used_as_proof"] is False,
            data["superset_strategy"],
        ),
        check(
            "primitive-only counterexample",
            source["counterexample_proved"] is True
            and source["selected_source_emission_proved"] is False
            and source["counterexample_scope"] == "primitive_only_span",
            source,
        ),
        check(
            "span misses target",
            spans["target_dimension"] == 72
            and spans["fixed_fiber_primitives"]["target_in_span"] is False
            and spans["fixed_plus_all_fiber_envelope"]["target_in_span"] is False
            and spans["fixed_plus_all_fiber_envelope"]["relative_residual"] > 0.1,
            spans,
        ),
        check(
            "refined theorem",
            refined["name"] == "SelectedWeylPairBasisTransportOrVertexSourceTheorem"
            and refined["status"] == "NEXT_THEOREM_REQUIRED"
            and "phase-like qutrit Z component or equivalent basis holonomy" in refined["required_new_components"]
            and "shift-like qutrit X component tied to active shift (1,1)" in refined["required_new_components"],
            refined,
        ),
        check(
            "interpretation",
            data["interpretation"]["primitive_only_theorem_sufficient"] is False
            and data["interpretation"]["basis_transport_or_vertex_still_live"] is True,
            data["interpretation"],
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check(
            "remaining refined gate",
            data["what_remains_open"]["prove_selected_weyl_pair_basis_transport_or_vertex_source"] is True
            and data["what_remains_open"]["emit_enriched_A_selected"] is True
            and data["what_remains_open"]["solve_or_reject_splitter_equation"] is True,
            data["what_remains_open"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records primitive-only insufficiency",
            "primitive-only route is not sufficient" in note
            and "SelectedWeylPairBasisTransportOrVertexSourceTheorem" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C basis-transport primitive proof/counterexample audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
