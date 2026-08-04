"""Audit the V_alpha/S3 two-block source-selector reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "valpha_s3_two_block_source_selector_reduction_certificate.json"
CANDIDATE = REPO / "candidate_data" / "valpha_s3_two_block_source_selector_reduction.candidate.json"
NOTE = REPO / "proof_corpus" / "VAlpha_S3_Two_Block_Source_Selector_Reduction_v1.md"
SCRIPT = REPO / "scripts" / "analyze_valpha_s3_two_block_source_selector_reduction.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    finite = cert["finite_rank_logic"]
    deck = cert["selected_s3_deck_limit"]
    shadow = cert["integral_shadow_match"]
    selector = cert["selector_status"]
    routes = cert["route_triage"]
    closes = cert["what_this_closes"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "VALPHA_S3_TWO_BLOCK_SOURCE_SELECTOR_REDUCED_TO_SYMMETRY_BREAKING_SOURCE",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["integral_shadow_match"] == shadow
            and computed["route_triage"] == routes,
            computed["status"],
        ),
        check(
            "one-block rejected and two-block exact",
            finite["one_block_matching_maps"] == 0
            and finite["one_block_max_pullback_rank"] == 2
            and finite["two_block_lifted_equals_full_valpha"] is True
            and finite["finite_active_blocks_required_by_rank"] == 2,
            finite,
        ),
        check(
            "selected S3 deck supplies only one block",
            deck["selected_s3_active_image_rank_over_F3"] == 2
            and deck["g3_g4_in_kernel_of_existing_selected_deck_quotient"] is True
            and deck["current_selected_s3_supplies_second_active_block"] is False,
            deck,
        ),
        check(
            "integral shadow equals two-block lift",
            shadow["integral_active_mod3_equals_two_block_lift"] is True
            and shadow["integral_active_rank_mod3"] == 4
            and shadow["shared_circle_degree_zero"] is True
            and shadow["target_degrees"] == [2, -4, 0],
            shadow,
        ),
        check(
            "selector remains open",
            selector["appell_humbert_model_exists"] is True
            and selector["h1_after_source_would_promote"] is True
            and selector["current_closed_selector_can_choose_target"] is False
            and selector["pic0_needs_holonomy_sensitive_source_or_gauge_fixing"]
            is True,
            selector,
        ),
        check(
            "route triage",
            routes["single_selected_s3_quotient"]["status"]
            == "REJECTED_BY_RANK_AND_DECK_KERNEL"
            and routes["two_s3_type_finite_blocks"]["status"]
            == "FINITE_SHAPE_CONSTRUCTED_SELECTION_OPEN"
            and routes["ordered_integral_appell_humbert_lift"]["status"]
            == "MODEL_EXISTS_SELECTOR_OPEN",
            routes,
        ),
        check(
            "correct closure",
            closes["two_block_finite_shape_is_mod3_shadow_of_ordered_integral_L2"]
            is True
            and closes[
                "current_selected_s3_deck_quotient_does_not_supply_second_block"
            ]
            is True
            and closes["full_valpha_mod3_requirement_reduced_to_source_selector"]
            is True,
            closes,
        ),
        check(
            "guardrails",
            all(value is False for value in guardrails.values()),
            guardrails,
        ),
        check(
            "note records theorem",
            "two-block finite shape" in note
            and "current selected S3 deck quotient supplies only one active F3^2 block"
            in note
            and "ordered integral source" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["status"] == cert["status"]
            and candidate["integral_shadow_match"] == cert["integral_shadow_match"],
            candidate["status"],
        ),
    ]

    print("\nV_alpha/S3 two-block source-selector reduction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
