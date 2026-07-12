"""Hunt for a selected SU(5)/qutrit sector-transport theorem in the corpus.

The preceding candidate calculation shows that B_10=I_3, B_bar5=F would supply
an exact nonzero CKM heavy-link direction.  This script checks whether the
current proof package or local MTT corpus already contains a selector for that
relative transport.  It deliberately excludes the newly generated SU5/qutrit
candidate files so that it cannot certify itself.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
EXTERNAL_CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SUFFIXES = {".md", ".txt", ".json", ".tex", ".py"}
MAX_HITS = 12
EXCLUDE_SUBSTRINGS = (
    "su5_qutrit_basis_transport",
    "su5_qutrit_transport_selector",
    "qutrit_polarization_transport_lemma",
    "prove_qutrit_polarization_transport",
    "su5_qutrit_polarization_selection",
    "selected_su5_qutrit_polarization",
    "su5_projection_tensor_derivation",
    "selected_su5_source_proof_attempt",
    "attempt_selected_su5_source_proof",
    "selected_fourier_transport_proof_attempt",
    "attempt_selected_fourier_transport_proof",
    "selected_gerbe_fourier_type",
    "prove_selected_gerbe_fourier_type",
    "time_oriented_conjugate_branch_selection",
    "prove_time_oriented_conjugate_branch_selection",
    "su5_matter_slot_transversality",
    "prove_su5_matter_slot_transversality",
    "selected_matter_slot_transversality_source",
    "validate_selected_matter_slot_transversality_source",
    "attempt_fill_selected_matter_slot_transversality_source",
    "selected_matter_source_two_path_exploration",
    "explore_selected_matter_source_two_paths",
    "selected_hym_operator_source",
    "validate_selected_hym_operator_source",
    "attempt_selected_hym_operator_source",
    "visible_operator_source_blocker_resolution",
    "resolve_visible_operator_source_blocker",
    "q79_theorem_change_list_for_paper_updates",
)


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def should_scan(path: Path) -> bool:
    name = path.as_posix().lower()
    return (
        path.is_file()
        and path.suffix.lower() in SUFFIXES
        and path.name.lower() != "readme.md"
        and not any(token in name for token in EXCLUDE_SUBSTRINGS)
        and ".git/" not in name
        and "reports/" not in name
    )


def contains_any(text: str, needles: tuple[str, ...]) -> bool:
    lower = text.lower()
    return any(needle in lower for needle in needles)


def find_hits(root: Path, predicate: Callable[[str], bool], max_hits: int = MAX_HITS) -> list[str]:
    if not root.exists():
        return []
    hits: list[str] = []
    for path in root.rglob("*"):
        if len(hits) >= max_hits:
            break
        if not should_scan(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if predicate(text):
            hits.append(rel(path))
    return hits


def su5_split_predicate(text: str) -> bool:
    lower = text.lower()
    return ("10_m" in lower and "bar5" in lower) or ("su(5)" in lower and "yukawa" in lower)


def qutrit_tool_predicate(text: str) -> bool:
    return contains_any(text, ("qutrit", "clock/shift", "clock-shift", "finite heisenberg"))


def fourier_guardrail_predicate(text: str) -> bool:
    lower = text.lower()
    return "fourier" in lower and (
        "pure gauge" in lower
        or "simultaneously diagonalizable" in lower
        or "not physical family mixing" in lower
    )


def zero_mode_route_predicate(text: str) -> bool:
    lower = text.lower()
    return "selected zero-mode" in lower or "monad" in lower and "h^1" in lower


def direct_selector_predicate(text: str) -> bool:
    lower = text.lower()
    matter_split = (
        "10_m" in lower
        or "bar5" in lower
        or "b_10" in lower
        or "b_bar5" in lower
    )
    qutrit_or_fourier = (
        "qutrit" in lower
        or "fourier unitary" in lower
        or "clock/shift" in lower
        or "clock-shift" in lower
    )
    selector = (
        "basis transport" in lower
        or "sector transport" in lower
        or "b_10" in lower
        or "b_bar5" in lower
        or "selected zero-mode" in lower
    )
    return matter_split and qutrit_or_fourier and selector


def analyze() -> dict[str, object]:
    roots = [ROOT]
    if EXTERNAL_CORPUS.exists():
        roots.append(EXTERNAL_CORPUS)

    def gather(predicate: Callable[[str], bool]) -> list[str]:
        hits: list[str] = []
        for root in roots:
            hits.extend(find_hits(root, predicate, max_hits=max(1, MAX_HITS - len(hits))))
            if len(hits) >= MAX_HITS:
                break
        return hits

    su5_hits = gather(su5_split_predicate)
    qutrit_hits = gather(qutrit_tool_predicate)
    fourier_guardrail_hits = gather(fourier_guardrail_predicate)
    zero_mode_route_hits = gather(zero_mode_route_predicate)
    direct_selector_hits = gather(direct_selector_predicate)

    selector_found = len(direct_selector_hits) > 0
    return {
        "calculation": "SU5QutritTransportSelectorHunt",
        "scanned_roots": [str(root) for root in roots],
        "external_corpus_available": EXTERNAL_CORPUS.exists(),
        "exclusions": list(EXCLUDE_SUBSTRINGS),
        "supporting_ingredients": {
            "su5_yukawa_split_hits": su5_hits,
            "qutrit_clock_shift_hits": qutrit_hits,
            "fourier_common_gauge_guardrail_hits": fourier_guardrail_hits,
            "zero_mode_or_monad_route_hits": zero_mode_route_hits,
        },
        "direct_selector_contract": {
            "requires_10_bar5_or_basis_transport_token": True,
            "requires_qutrit_or_fourier_token": True,
            "requires_basis_or_sector_transport_selection_token": True,
        },
        "direct_selector_hits": direct_selector_hits,
        "selector_found": selector_found,
        "verdict": {
            "ingredients_present_separately": all(
                len(hits) > 0
                for hits in (
                    su5_hits,
                    qutrit_hits,
                    fourier_guardrail_hits,
                    zero_mode_route_hits,
                )
            ),
            "selected_B10_Bbar5_transport_found": selector_found,
            "candidate_status": "conditional" if not selector_found else "ready_for_manual_review",
            "next_required_source": (
                "a selected zero-mode/monad/Galerkin theorem deriving the "
                "relative 10_M/bar5_M qutrit Fourier transport"
            ),
        },
        "guardrails": {
            "promotes_candidate_to_selected_data": False,
            "uses_observed_flavor_data": False,
            "claims_full_SM_closure": False,
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
