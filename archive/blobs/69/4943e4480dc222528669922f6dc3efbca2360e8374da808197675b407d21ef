"""Audit primitive source-selection/fiber-rule reduction."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_primitive_source_selection_audit.candidate.json"
CERT = REPO / "certificates" / "selected_routec_primitive_source_selection_audit_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Primitive_Source_Selection_Theorem_or_FiberRule_Audit_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    active = data["active_shift_theorem"]["enumeration"]
    fixed = data["fiber_class_theorem"]["fixed_fiber_shifts"]
    envelope = data["fiber_class_theorem"]["all_fiber_envelope"]
    source = data["source_implication"]

    fixed_all_rank3 = all(
        rank == 3
        for by_sector in fixed["ranks"].values()
        for rank in by_sector.values()
    )
    fixed_equivalent = all(
        item["equivalent"] is True
        for item in fixed["equivalence_to_shift_0_on_u"].values()
    )
    all_rank1 = all(rank == 1 for rank in envelope["rank"].values())

    checks = [
        check(
            "status",
            data["status"]
            == "MTT_SELECTED_ROUTEC_PRIMITIVE_SOURCE_SELECTION_AUDIT_BUILT_ACTIVE_SHIFT_FORCED_FIBER_CLASS_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "active shift forced",
            active["active_shift_necessary_and_sufficient_for_nonzero"] is True
            and active["nonzero_active_shifts"] == [[1, 1]],
            active,
        ),
        check("fixed fiber shifts rank three", fixed_all_rank3, fixed["ranks"]),
        check("fixed fiber shifts gauge equivalent", fixed_equivalent, fixed["equivalence_to_shift_0_on_u"]),
        check(
            "all envelope structurally different",
            all_rank1 and envelope["not_gauge_equivalent_to_fixed_fiber_class"] is True,
            envelope,
        ),
        check(
            "absolute fiber still unselected",
            source["absolute_fiber_shift_selected"] is False
            and source["selected_noninvariant_primitive_source_proved"] is False,
            source,
        ),
        check(
            "no closure claim or target fit",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_FiberClass_Observable_Invariance_or_GaugeFix_v1",
            data["next_required_artifact"],
        ),
        check(
            "note records theorem and guardrails",
            "Active shift `(1,1)` is forced" in note
            and "one fiber class" in note
            and "No observed flavor data were used" in note
            and "no full SM/no-knob closure is claimed" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C primitive source-selection/fiber-rule audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
