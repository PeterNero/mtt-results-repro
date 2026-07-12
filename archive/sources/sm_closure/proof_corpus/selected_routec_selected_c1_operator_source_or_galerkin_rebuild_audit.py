"""Audit smart iteration of selected C1 operator-source rebuild space."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild.candidate.json"
CERT = REPO / "certificates" / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_C1_OPERATOR_SOURCE_GALERKIN_REBUILD_ITERATED_BASIS_TRANSPORT_LANE_SELECTED_AS_NEXT_PROOF_TARGET"
NEXT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    iteration = data["solution_space_iteration"]
    selected = iteration["selected_solution_kernel"]
    facts = data["supporting_facts"]
    ranked = iteration["ranked_lanes"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "ranked lanes",
            len(ranked) == 4
            and ranked[0]["lane"] == "L3_noninvariant_basis_transport_or_vertex_source"
            and ranked[0]["score"] > ranked[1]["score"],
            ranked,
        ),
        check(
            "selected solution kernel",
            selected["selected_next_lane"] == "L3_noninvariant_basis_transport_or_vertex_source"
            and selected["active_shift_unique"] is True
            and selected["forced_active_shift"] == [[1, 1]]
            and selected["fixed_fiber_shifts_gauge_equivalent"] is True,
            selected,
        ),
        check(
            "support facts",
            facts["active_shift_necessary_and_sufficient_for_nonzero"] is True
            and facts["unique_nonzero_active_shift"] == [[1, 1]]
            and facts["nonzero_unselected_candidates_found"] > 0
            and facts["canonical_response_zero"] is True
            and facts["dotd_projector_scaffold_exists"] is True,
            facts,
        ),
        check(
            "search pruned safely",
            iteration["search_space_pruned"]["observed_target_fits_removed"] is True
            and iteration["search_space_pruned"]["lifted_flag_proofs_removed"] is True
            and iteration["search_space_pruned"]["basis_transport_lane_promoted_to_next_proof_target"] is True,
            iteration["search_space_pruned"],
        ),
        check(
            "no closure claim",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check(
            "remaining proof target",
            data["what_remains_open"]["prove_selected_basis_transport_or_vertex_source_theorem"] is True
            and data["what_remains_open"]["emit_A_selected_from_promoted_primitive"] is True
            and data["what_remains_open"]["solve_or_reject_splitter_equation"] is True,
            data["what_remains_open"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records next theorem",
            "active deck shift `(1,1)`" in note
            and "fixed qutrit fiber shifts `0,1,2` form one gauge class" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C C1 operator-source rebuild iteration audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
