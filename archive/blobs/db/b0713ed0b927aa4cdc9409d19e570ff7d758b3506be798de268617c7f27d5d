"""Audit q79 reduced-AH global destabilizer enumeration."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_stability_hym_or_routec_residual_source.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_global_destabilizer_enumeration_or_selected_residual.py"
CERT = ROOT / "certificates" / "q79_global_destabilizer_enumeration_or_selected_residual_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_global_destabilizer_enumeration_or_selected_residual.candidate.json"
TABLE = ROOT / "candidate_data" / "q79_global_destabilizer_enumeration_or_selected_residual" / "reduced_ah_global_enumeration_table.json"
PAPER = ROOT / "proof_corpus" / "Q79_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1.md"

STATUS = "Q79_SELECTED_ROUTEC_REDUCED_AH_GLOBAL_DESTABILIZER_ENUMERATION_PROVED_PROMOTION_OPEN"
NEXT = "Q79_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1"
EXPECTED_SIX = [[-4, 2, 0], [-3, 2, 0], [-2, 1, 0], [-2, 2, 0], [-1, 1, 0], [-1, 2, 0]]
EXPECTED_SM = "MTT_SELECTED_ROUTEC_REDUCED_AH_GLOBAL_DESTABILIZER_ENUMERATION_PROVED_PROMOTION_OPEN"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, TABLE, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate JSON differ", failures)
    require(table == cert["reduced_AH_global_rank_one_enumeration"], "enumeration table mismatch", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)
    require(
        cert["sm_input_statuses"]["global_enumeration_candidate"]["status"] == EXPECTED_SM,
        "SM global status mismatch",
        failures,
    )

    enum = cert["reduced_AH_global_rank_one_enumeration"]
    theorem = cert["conditional_global_stability_theorem"]
    gap = cert["promotion_gap"]
    shared = cert["shared_circle_handling"]
    routec = cert["route_c_residual_lane"]
    remaining = cert["what_remains_open"]

    require(enum["finite_without_cutoff"] is True, "enumeration should be cutoff-free", failures)
    require(enum["hom_to_L_nonnegative_candidates"] == [], "Hom-to-L candidates not empty", failures)
    require(enum["hom_to_Q_nonnegative_candidates"] == EXPECTED_SIX, "Hom-to-Q candidates changed", failures)
    require(enum["candidate_list_equals_prior_six"] is True, "prior-six equality missing", failures)
    require(enum["all_candidates_previously_obstructed"] is True, "prior obstruction missing", failures)
    require(enum["all_boundaries_previously_injective"] is True, "prior injectivity missing", failures)
    require(enum["sm_global_enumeration_agrees"] is True, "SM/q79 enumeration mismatch", failures)
    require(enum["bounded_sanity_scan"]["hom_to_L_matches_symbolic_empty"] is True, "bounded L scan mismatch", failures)
    require(enum["bounded_sanity_scan"]["hom_to_Q_matches_symbolic"] is True, "bounded Q scan mismatch", failures)
    require(theorem["proved"] is True, "reduced AH theorem not proved", failures)
    require(gap["full_stability_proved"] is False, "full stability overclaimed", failures)
    require(gap["hym_existence_proved"] is False, "HYM overclaimed", failures)
    require(shared["central_circle_not_used_as_global_subsheaf_axiom"] is True, "shared circle overused", failures)
    require(routec["selected_operator_source_still_required"] is True, "operator source overclosed", failures)

    for key in (
        "selected_AH_representative_or_literal_good_cover_table",
        "rank_one_torsion_free_reflexive_hull_representation_theorem",
        "selected_HYM_or_Strominger_existence_certificate",
        "selected_RouteC_residual_values",
        "same_source_D_E_Riesz_Green_dotD",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"open flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for phrase in (
        "reduced Appell-Humbert",
        "still not a full HYM certificate",
        "SM global enumeration agrees",
        "Q79ReducedAHGlobalRankOneVAlphaStabilityTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 global destabilizer enumeration audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 global destabilizer enumeration audit PASS")
    print(f"status: {cert['status']}")
    print(f"hom_to_Q: {enum['hom_to_Q_nonnegative_candidates']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
