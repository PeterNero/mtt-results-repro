"""Audit non-invariant C1 primitive search."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
CERT = REPO / "certificates" / "selected_routec_noninvariant_c1_primitive_search_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_NonInvariant_C1_Primitive_Search_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    candidates = data["candidate_primitives"]
    shifts = {str(item["primitive_fiber_shift"]) for item in candidates}
    nonzero = [
        item
        for item in candidates
        if any(summary["max_abs_entry"] > 0 for summary in item["summary"].values())
    ]
    all_unselected = all(item["selected_by_theorem"] is False for item in candidates)
    all_no_observed = all(item["uses_observed_flavor_data"] is False for item in candidates)

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_NONINVARIANT_C1_PRIMITIVE_SEARCH_BUILT_UNSELECTED_CANDIDATES_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "minimal active shift",
            data["search_rule"]["minimal_active_shift_required"] == [1, 1],
            data["search_rule"],
        ),
        check("four fiber candidates", shifts == {"0", "1", "2", "all"}, shifts),
        check(
            "nonzero candidates found",
            len(nonzero) == 4
            and data["calculation_results"]["nonzero_unselected_candidates_found"] == 4,
            data["calculation_results"],
        ),
        check("all candidates unselected", all_unselected, candidates),
        check("no observed flavor data", all_no_observed and data["target_fitting_used"] is False, data["search_rule"]),
        check(
            "not closed",
            data["calculation_results"]["can_close_selected_C1_now"] is False
            and data["closure_claimed"] is False,
            data["calculation_results"],
        ),
        check(
            "remaining source selection",
            data["what_remains_open"]["fiber_shift_selection"] is True
            and data["what_remains_open"]["selected_noninvariant_C1_primitive_or_vertex"] is True,
            data["what_remains_open"],
        ),
        check(
            "superset repair classification",
            data["superset_mode"]["superset_repair"]["classification"]
            == "NONINVARIANT_C1_CANDIDATES_FOUND_SELECTION_THEOREM_OPEN",
            data["superset_mode"],
        ),
        check(
            "note records guardrail",
            "No observed Yukawa, CKM, PMNS, or mass data were used" in note
            and "Selected C1 closure now: `False`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C non-invariant C1 primitive search audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
