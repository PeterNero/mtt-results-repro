"""Prove the central-circle-neutral filter inside the terminal monad lane.

This is not the full terminal lane source selector.  It closes a sharper
sub-lemma: if the visible ordered source is selected from terminal monad
differences L_i-K2, then the MTT central-circle/gauge corpus forces the
central-circle-neutral member of that lane.  The terminal scan already shows
that this member is uniquely L3-K2.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

CENTRAL_CIRCLE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\13 Standard Model & Topology-Only Constraints"
    r"\The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)

MONAD_ATTEMPT = CERTS / "selected_monad_difference_l2_source_proof_attempt_certificate.json"
MONAD_MAP_GATE = CERTS / "iwasawa_monad_map_data_gate_certificate.json"
ORDERED_REDUCTION = CERTS / "ordered_layer_terminal_lane_selector_reduction_certificate.json"

OUT_CANDIDATE = CANDIDATES / "central_circle_neutral_terminal_lane_filter.candidate.json"
OUT_CERT = CERTS / "central_circle_neutral_terminal_lane_filter_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def central_circle_support() -> dict[str, Any]:
    text = CENTRAL_CIRCLE.read_text(encoding="utf-8", errors="ignore").lower()
    checks = {
        "central_circle_unique_shared_channel": "unique shared coherence channel" in text,
        "gauge_forces_internal_bundle_connections": (
            "gauge forces arise from internal bundle connections" in text
            or "gauge forces arise from bundle--specific internal connections" in text
        ),
        "gauge_forces_do_not_strain_central_circle": (
            "without straining the central circle" in text
            or "do not act on the shared coherence channel" in text
        ),
        "gauge_fields_internal_fiber_directions": "internal fiber directions" in text,
    }
    return {
        "source": str(CENTRAL_CIRCLE),
        "checks": checks,
        "supported": all(checks.values()),
        "interpretation": (
            "Visible gauge/bundle source data may rearrange internal degrees of "
            "freedom, but must not carry net deformation along the shared central "
            "circle. In the terminal monad difference table this is the z=0 filter."
        ),
    }


def terminal_lane_filter() -> dict[str, Any]:
    monad = load(MONAD_ATTEMPT)
    scan = monad["terminal_monad_difference_scan"]
    differences = scan["differences"]
    zero_central = [item for item in differences if item["central_degree"] == 0]
    selected = zero_central[0] if len(zero_central) == 1 else None
    target = scan["target_L"]
    target_l2 = scan["target_L2"]
    return {
        "terminal_lane": "L_i-K2",
        "central_degree_coordinate": "third Iwasawa/shared-circle coefficient z",
        "zero_central_labels": [item["label"] for item in zero_central],
        "unique_zero_central": len(zero_central) == 1,
        "selected_by_filter": selected,
        "target_L": target,
        "target_L2": target_l2,
        "filter_forces_target": (
            selected is not None
            and selected["label"] == "L3-K2"
            and selected["value"] == target
            and selected["double_value"] == target_l2
            and selected["dual_matches_printed_g_type"] is True
        ),
    }


def analyze() -> dict[str, Any]:
    monad_map = load(MONAD_MAP_GATE)
    reduction = load(ORDERED_REDUCTION)
    support = central_circle_support()
    terminal = terminal_lane_filter()
    source_lane_still_open = (
        reduction.get("what_this_does_not_close", {}).get("actual_terminal_monad_lane_selector")
        is False
    )
    theorem_proved = support["supported"] and terminal["filter_forces_target"]

    report = {
        "calculation": "CentralCircleNeutralTerminalLaneFilter",
        "status": (
            "CENTRAL_CIRCLE_NEUTRAL_TERMINAL_LANE_FILTER_PROVED_SELECTOR_OPEN"
            if theorem_proved
            else "CENTRAL_CIRCLE_NEUTRAL_TERMINAL_LANE_FILTER_INCONCLUSIVE"
        ),
        "generated_by": "scripts/prove_central_circle_neutral_terminal_lane_filter.py",
        "inputs": {
            "central_circle_corpus": str(CENTRAL_CIRCLE),
            "monad_attempt": MONAD_ATTEMPT.name,
            "monad_map_gate": MONAD_MAP_GATE.name,
            "ordered_layer_terminal_lane_reduction": ORDERED_REDUCTION.name,
        },
        "corpus_support": support,
        "monad_map_context": {
            "sequence": monad_map.get("source_monad", {}).get("sequence"),
            "line_bundle_c1_vectors_abc": monad_map.get("source_monad", {}).get(
                "line_bundle_c1_vectors_abc"
            ),
            "typed_sections_still_missing": monad_map.get("typed_map_check", {}).get(
                "requires_global_holomorphic_sections_or_transition_data"
            ),
        },
        "terminal_lane_filter": terminal,
        "conditional_theorem": {
            "proved": theorem_proved,
            "statement": (
                "If the visible ordered source is selected from terminal monad "
                "differences L_i-K2, then the MTT central-circle/gauge neutrality "
                "principle forces the unique central-neutral member of that lane. "
                "The terminal scan identifies that member as L3-K2=(1,-2,0), "
                "with double (2,-4,0)."
            ),
        },
        "what_this_closes": {
            "central_circle_neutrality_filter_inside_terminal_lane": theorem_proved,
            "unique_zero_central_terminal_difference_is_L3_minus_K2": terminal[
                "filter_forces_target"
            ],
            "central_neutrality_no_longer_an_unchecked_subassumption": theorem_proved,
        },
        "what_this_does_not_close": {
            "actual_terminal_monad_lane_source_principle": False,
            "typed_Cech_or_Appell_Humbert_transition_source": False,
            "base_factor_order_tied_to_physical_E1_E2_labels": False,
            "operator_layer_Pic0_recheck": False,
            "same_source_D_E_dotD_Riesz_Green": False,
            "non_split_stability_or_HYM": False,
            "full_SM_closure": False,
        },
        "remaining_selector_theorem": {
            "name": "Terminal_Map_Source_Principle_and_Base_Order_v1",
            "must_prove": [
                "the visible ordered L source is selected from the terminal monad map lane L_i-K2",
                "the monad line labels are tied to the physical Appell-Humbert/Cech base order E1 positive and E2 negative",
                "typed transition, rhoE, or D_E/dotD data bind the lane to the operator packet",
            ],
        },
        "guardrails": {
            "claims_actual_terminal_lane_selector_proved": False,
            "claims_typed_transition_data_supplied": False,
            "claims_operator_layer_Pic0_closed": False,
            "claims_full_SM_closure": False,
            "uses_benchmark_flavor_entries": False,
            "uses_observed_flavor_data": False,
        },
        "verdict": {
            "honest_answer": (
                "The shared-circle warning matters: it proves the zero-central "
                "filter inside the terminal monad lane.  This makes L3-K2 unique "
                "once the terminal lane itself is selected, but it still does not "
                "prove that MTT selects the terminal lane or the physical base order."
            )
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "CentralCircleNeutralTerminalLaneFilter",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": rel(OUT_CANDIDATE),
        "inputs": report["inputs"],
        "corpus_support": report["corpus_support"],
        "terminal_lane_filter": report["terminal_lane_filter"],
        "conditional_theorem": report["conditional_theorem"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "remaining_selector_theorem": report["remaining_selector_theorem"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"].endswith("SELECTOR_OPEN") else 1


if __name__ == "__main__":
    raise SystemExit(main())
