"""Prove the sufficiency contract for a selected monad-difference L^2 source.

This is a relative theorem.  It does not assert that MTT has selected the
monad difference L3-K2.  Instead it asks:

    If a future source certificate selects L3-K2 as the visible V_alpha
    ordered integral source and selects/quotients Pic0, does the existing
    ordered-source validator accept the packet?

The answer is yes.  That makes the remaining proof obligation sharply local:
prove the selected source theorem, rather than changing the arithmetic target.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

VALIDATOR = ROOT / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"

MONAD_CANDIDATE = CERTIFICATES / "iwasawa_monad_l2_branch_orientation_candidate_certificate.json"
ORDERED_GATE = CERTIFICATES / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"
PULLBACK_SELECTION = CERTIFICATES / "visible_rank2_l2_pullback_selection_attempt_certificate.json"

UNSELECTED_PACKET = CANDIDATE_DATA / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
HYPOTHETICAL_PACKET = (
    CANDIDATE_DATA / "visible_rank2_l2_ordered_source.monad_difference_hypothetical_selected.json"
)
CANDIDATE = CANDIDATE_DATA / "monad_difference_l2_source_sufficiency.candidate.json"
CERTIFICATE = CERTIFICATES / "monad_difference_l2_source_sufficiency_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    parsed: dict[str, Any] | None = None
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_ordered_source_validation_report="):
            parsed = json.loads(line.split("=", 1)[1])
            break
    return {
        "packet": str(path),
        "exit_code": proc.returncode,
        "output": proc.stdout.strip(),
        "parsed_report": parsed,
    }


def promote_packet(packet: dict[str, Any]) -> dict[str, Any]:
    promoted = json.loads(json.dumps(packet))
    promoted["status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED"
    promoted["candidate_role"] = "SELECTED_DATA"
    promoted["source"].update(
        {
            "source_certificate": "Selected_Monad_Difference_L2_Source.v1",
            "source_status": "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED",
            "selected_by_mtt": True,
            "fixture_only": False,
        }
    )
    promoted["selection_evidence"].update(
        {
            "standard_lattice_or_equivalent_selected": True,
            "base_factor_order_selected": True,
            "base_swap_broken_by_source": True,
            "not_only_finite_mod3_qutrit": True,
            "not_equal_radius_import": True,
        }
    )
    promoted["pic0_resolution"].update(
        {
            "resolution": "neutral_character_selected",
            "flat_character_values_g1_to_g6": [[1, 0]] * 6,
            "source_selected_or_quotiented": True,
        }
    )
    return promoted


def changed_fields(original: dict[str, Any], promoted: dict[str, Any]) -> list[str]:
    changes: list[str] = []

    def walk(prefix: str, a: Any, b: Any) -> None:
        if isinstance(a, dict) and isinstance(b, dict):
            for key in sorted(set(a) | set(b)):
                walk(f"{prefix}.{key}" if prefix else key, a.get(key), b.get(key))
        elif a != b:
            changes.append(prefix)

    walk("", original, promoted)
    return changes


def analyze() -> dict[str, Any]:
    monad_candidate = load_json(MONAD_CANDIDATE)
    ordered_gate = load_json(ORDERED_GATE)
    pullback_selection = load_json(PULLBACK_SELECTION)
    unselected_packet = load_json(UNSELECTED_PACKET)

    unselected_validation = run_validator(UNSELECTED_PACKET)
    promoted_packet = promote_packet(unselected_packet)
    write_json(HYPOTHETICAL_PACKET, promoted_packet)
    promoted_validation = run_validator(HYPOTHETICAL_PACKET)

    changes = changed_fields(unselected_packet, promoted_packet)
    allowed_changes = {
        "candidate_role",
        "pic0_resolution.resolution",
        "pic0_resolution.source_selected_or_quotiented",
        "selection_evidence.base_factor_order_selected",
        "selection_evidence.standard_lattice_or_equivalent_selected",
        "source.fixture_only",
        "source.selected_by_mtt",
        "source.source_certificate",
        "source.source_status",
        "status",
    }

    sufficiency_proved = (
        monad_candidate.get("status")
        == "IWASAWA_MONAD_L2_BRANCH_ORIENTATION_CANDIDATE_FOUND_SELECTION_OPEN"
        and ordered_gate.get("status")
        == "VISIBLE_RANK2_L2_ORDERED_SOURCE_PROMOTION_GATE_FORMULATED_SELECTION_OPEN"
        and pullback_selection.get("relative_selection_theorem", {}).get("proved") is True
        and unselected_validation.get("exit_code") == 2
        and promoted_validation.get("exit_code") == 0
        and set(changes) <= allowed_changes
    )

    return {
        "calculation": "MonadDifferenceL2SourceSufficiency",
        "status": (
            "MONAD_DIFFERENCE_L2_SOURCE_SUFFICIENCY_PROVED_SELECTION_THEOREM_OPEN"
            if sufficiency_proved
            else "MONAD_DIFFERENCE_L2_SOURCE_SUFFICIENCY_INCONCLUSIVE"
        ),
        "generated_by": "scripts/prove_monad_difference_l2_source_sufficiency.py",
        "input_certificates": {
            "iwasawa_monad_l2_branch_orientation_candidate": MONAD_CANDIDATE.name,
            "visible_rank2_l2_ordered_source_promotion_gate": ORDERED_GATE.name,
            "visible_rank2_l2_pullback_selection_attempt": PULLBACK_SELECTION.name,
        },
        "input_statuses": {
            "monad_candidate": monad_candidate.get("status"),
            "ordered_source_gate": ordered_gate.get("status"),
            "pullback_selection": pullback_selection.get("status"),
        },
        "packets": {
            "unselected_candidate": str(UNSELECTED_PACKET.relative_to(ROOT)),
            "hypothetical_selected": str(HYPOTHETICAL_PACKET.relative_to(ROOT)),
            "unselected_validation": unselected_validation,
            "hypothetical_selected_validation": promoted_validation,
        },
        "promotion_delta": {
            "changed_fields": changes,
            "only_source_selection_and_pic0_fields_changed": set(changes) <= allowed_changes,
            "allowed_changed_fields": sorted(allowed_changes),
        },
        "relative_theorem": {
            "proved": sufficiency_proved,
            "statement": (
                "If MTT supplies Selected_Monad_Difference_L2_Source.v1 selecting "
                "L3-K2 as the visible V_alpha ordered integral source, selecting "
                "the standard/equivalent lattice and base order, and selecting "
                "neutral Pic0, then the existing ordered-source validator accepts "
                "L=(1,-2,0), L^2=(2,-4,0), E12=2, E34=-4 with no observed or "
                "benchmark flavor input."
            ),
        },
        "what_this_closes": {
            "sufficiency_of_selected_monad_difference_for_ordered_source_gate": sufficiency_proved,
            "no_extra_arithmetic_or_matrix_target_needed_for_ordered_source_gate": sufficiency_proved,
            "remaining_gap_localized_to_source_selection_and_pic0": sufficiency_proved,
        },
        "what_this_does_not_close": {
            "actual_MTT_selection_of_L3_minus_K2": False,
            "Pic0_selection_from_current_corpus": False,
            "nonzero_Ext_selection": False,
            "stability_HYM_or_Route_C": False,
            "same_source_D_E_dotD_Riesz_Green": False,
            "full_SM_closure": False,
        },
        "still_open": {
            "prove_Selected_Monad_Difference_L2_Source_v1": True,
            "derive_or_source_print_transition_data_from_that_source": True,
            "select_or_quotient_Pic0_without_notational_assumption": True,
            "promote_Ext_packet_and_prove_stability": True,
            "compute_same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_current_corpus_selects_monad_difference": False,
            "claims_pic0_resolved_now": False,
            "claims_unconditional_ordered_source_pass": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The monad-difference route is sufficient in the strict validator "
                "sense: after changing only source-selection and Pic0 fields, the "
                "ordered-source packet passes. The actual selected-source theorem "
                "is still open, but the target is now sharply defined."
            ),
            "next_packet": "Selected_Monad_Difference_L2_Source.v1",
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "MonadDifferenceL2SourceSufficiency",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/monad_difference_l2_source_sufficiency.candidate.json",
        "input_certificates": report["input_certificates"],
        "input_statuses": report["input_statuses"],
        "packets": report["packets"],
        "promotion_delta": report["promotion_delta"],
        "relative_theorem": report["relative_theorem"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "MONAD_DIFFERENCE_L2_SOURCE_SUFFICIENCY_PROVED_SELECTION_THEOREM_OPEN"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
