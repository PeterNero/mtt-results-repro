"""Audit the reduced AH global destabilizer enumeration artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_routec_global_destabilizer_enumeration_or_selected_residual.py"
DATA = REPO / "candidate_data" / "selected_routec_global_destabilizer_enumeration_or_selected_residual.candidate.json"
CERT = REPO / "certificates" / "selected_routec_global_destabilizer_enumeration_or_selected_residual_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_REDUCED_AH_GLOBAL_DESTABILIZER_ENUMERATION_PROVED_PROMOTION_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1"
EXPECTED_SIX = [[-4, 2, 0], [-3, 2, 0], [-2, 1, 0], [-2, 2, 0], [-1, 1, 0], [-1, 2, 0]]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> bool:
    print(f"{'PASS' if condition else 'FAIL'}: {label} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    enum = data["reduced_AH_global_rank_one_enumeration"]
    theorem = data["conditional_global_stability_theorem"]
    gap = data["promotion_gap"]
    shared = data["shared_circle_handling"]
    routec = data["route_c_residual_lane"]
    remaining = data["what_remains_open"]

    checks = [
        check("script exits 0", proc.returncode == 0, proc.stdout[:500]),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("no closure overclaim", data["closure_claimed"] is False and gap["full_stability_proved"] is False, gap),
        check("no target fitting", data["target_fitting_used"] is False, data["superset_strategy"]),
        check(
            "global reduced AH enumeration closes",
            enum["finite_without_cutoff"] is True
            and enum["hom_to_L_nonnegative_candidates"] == []
            and enum["hom_to_Q_nonnegative_candidates"] == EXPECTED_SIX
            and enum["candidate_list_equals_prior_six"] is True
            and enum["all_candidates_previously_obstructed"] is True
            and enum["proves_no_extra_reduced_AH_rank_one_line_destabilizers"] is True,
            enum,
        ),
        check(
            "bounded sanity scan agrees",
            enum["bounded_sanity_scan"]["hom_to_L_matches_symbolic_empty"] is True
            and enum["bounded_sanity_scan"]["hom_to_Q_matches_symbolic"] is True,
            enum["bounded_sanity_scan"],
        ),
        check(
            "theorem scoped to reduced AH model",
            theorem["proved"] is True
            and "reduced AH rank-one line model" in theorem["statement"]
            and gap["hym_existence_proved"] is False,
            theorem,
        ),
        check(
            "shared circle handled without global overuse",
            shared["central_circle_filter_inside_terminal_lane"] is True
            and shared["central_circle_not_used_as_global_subsheaf_axiom"] is True
            and shared["nonneutral_destabilizers_in_full_good_cover_still_need_promotion"] is True,
            shared,
        ),
        check(
            "Route-C residual still open",
            routec["selected_operator_source_still_required"] is True
            and routec["still_open"]["HYM_or_RouteC_selected_values"] is True,
            routec,
        ),
        check(
            "remaining promotion gates explicit",
            remaining["selected_AH_representative_or_literal_good_cover_table"] is True
            and remaining["rank_one_torsion_free_reflexive_hull_representation_theorem"] is True
            and remaining["selected_HYM_or_Strominger_existence_certificate"] is True,
            remaining,
        ),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records reduced theorem and promotion gap",
            "stable in the reduced AH rank-one line model" in note
            and "still needs promotion" in note
            and NEXT in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C reduced AH global destabilizer enumeration audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
