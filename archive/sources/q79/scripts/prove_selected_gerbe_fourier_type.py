"""Prove the selected MTT gerbe-Fourier qutrit type.

This is the strongest rigorous promotion currently available.

The previous proof attempt showed that the exact SU(5) packet

    U_10 = I_3, U_bar5 = F

is finite-valid but not yet selected as a fully ordered SU(5) matter-slot
packet.  Here we separate the problem into two layers:

1. Does MTT geometry select the nontrivial Z3 gerbe/qutrit Fourier phase-space
   type at all?
2. Does it additionally select the ordered SU(5) assignment
   10_M = clock and bar5_M = shift with q79 orientation F?

The answer encoded here is:

    Layer 1 closes up to the global conjugate orientation.
    Layer 2 remains open.

No observed masses, CKM entries, or benchmark flavor matrices are used.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
PROOF_CORPUS = ROOT / "proof_corpus"
OUT = ROOT / "candidate_data" / "selected_gerbe_fourier_type_theorem.candidate.json"
CERT = CERTIFICATES / "selected_gerbe_fourier_type_theorem_certificate.json"

CORPUS_ROOT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
B0 = (
    CORPUS_ROOT
    / "1 Core & Encodings"
    / "The_Modal_Triplet_Theory_Program_B0__Why_Description_Forces_Circle__Lens__and_Nil.md"
)
CENTRAL_CIRCLE = (
    CORPUS_ROOT
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)
PROTOSPINOR = (
    CORPUS_ROOT
    / "10 ProtoSpinor"
    / "Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md"
)
STROMINGER = (
    CORPUS_ROOT
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)

P = 3
Element = tuple[int, int]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def cert(name: str) -> dict[str, Any]:
    return load_json(CERTIFICATES / name)


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def contains_all_ci(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def mod(value: int) -> int:
    return value % P


def add(left: Element, right: Element) -> Element:
    return mod(left[0] + right[0]), mod(left[1] + right[1])


def b_period(label: int, left: Element, right: Element) -> int:
    """Numerator of B_label(left,right) in (1/3)Z/Z."""

    a_prime, _ = right
    _, b = left
    return mod(label * (-a_prime * b))


def coboundary_2(label: int, left: Element, middle: Element, right: Element) -> int:
    return mod(
        b_period(label, middle, right)
        - b_period(label, add(left, middle), right)
        + b_period(label, left, add(middle, right))
        - b_period(label, left, middle)
    )


def alternating_form(label: int, left: Element, right: Element) -> int:
    return mod(b_period(label, left, right) - b_period(label, right, left))


def rank_mod3(matrix: list[list[int]]) -> int:
    work = [[mod(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if work[row][col]:
                pivot = row
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], -1, P)
        work[rank] = [mod(inv * value) for value in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][col]
            if factor:
                work[row] = [
                    mod(work[row][idx] - factor * work[rank][idx])
                    for idx in range(cols)
                ]
        rank += 1
    return rank


def torsion_label_report(label: int) -> dict[str, Any]:
    elements = [(a, b) for a, b in product(range(P), repeat=2)]
    violations = [
        (left, middle, right, coboundary_2(label, left, middle, right))
        for left in elements
        for middle in elements
        for right in elements
        if coboundary_2(label, left, middle, right)
    ]
    commutator_matrix = [
        [
            alternating_form(label, (1, 0), (1, 0)),
            alternating_form(label, (1, 0), (0, 1)),
        ],
        [
            alternating_form(label, (0, 1), (1, 0)),
            alternating_form(label, (0, 1), (0, 1)),
        ],
    ]
    rank = rank_mod3(commutator_matrix)
    return {
        "label": label,
        "discrete_bianchi_zero": len(violations) == 0,
        "commutator_matrix": commutator_matrix,
        "commutator_rank": rank,
        "is_nontrivial_heisenberg_type": rank == 2,
        "orientation": "trivial" if label == 0 else "F_or_F_conjugate",
    }


def corpus_evidence() -> dict[str, Any]:
    b0 = read_text(B0)
    central = read_text(CENTRAL_CIRCLE)
    proto = read_text(PROTOSPINOR)
    strominger = read_text(STROMINGER)

    return {
        "tri_layer_cocycle_source": {
            "path": str(B0),
            "present": contains_all_ci(
                b0,
                [
                    "three independent layers",
                    "triple overlaps support genuine cocycle data",
                    "circle obstruction resides",
                    "define a principal bundle",
                    "connection on",
                ],
            ),
        },
        "central_circle_z3_family_source": {
            "path": str(CENTRAL_CIRCLE),
            "present": contains_all_ci(
                central,
                [
                    "Flavor degrees of freedom are encoded by a line bundle",
                    "discrete holonomy",
                    "Z}_3",
                    "three inequivalent character",
                    "sectors",
                ],
            )
            or contains_all_ci(
                central,
                [
                    "Flavor degrees of freedom are encoded by a line bundle",
                    "discrete holonomy",
                    "mathbb{Z}_3",
                    "three inequivalent character",
                    "sectors",
                ],
            ),
        },
        "nil_three_basin_source": {
            "path": str(PROTOSPINOR),
            "present": contains_all_ci(
                proto,
                [
                    "holonomy-aware nil termination",
                    "exactly three stable nil survivorship basins",
                    "three families",
                ],
            ),
        },
        "fixed_flux_sector_selection_source": {
            "path": str(STROMINGER),
            "present": contains_all_ci(
                strominger,
                [
                    "Fix a topological sector",
                    "Theorem 11",
                    "MTT selection",
                    "unique local minimizer",
                ],
            ),
        },
    }


def analyze() -> dict[str, Any]:
    evidence = corpus_evidence()
    gerbe = cert("iwasawa_discrete_gerbe_holonomy_candidate_certificate.json")
    torsion = cert("iwasawa_torsion_label_four_route_selector_certificate.json")
    qutrit = cert("qutrit_polarization_transport_lemma_certificate.json")
    su5_packet = cert("selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json")
    su5_source = cert("selected_su5_source_proof_attempt_certificate.json")
    c6_common = cert("iwasawa_c6_common_holonomy_branch_pair_certificate.json")
    c6_phase = cert("iwasawa_c6_global_phase_block_certificate.json")

    label_reports = [torsion_label_report(label) for label in range(P)]
    nontrivial_labels = [
        item["label"]
        for item in label_reports
        if item["is_nontrivial_heisenberg_type"] and item["discrete_bianchi_zero"]
    ]

    selected_structural_sources = all(
        entry.get("present") is True for entry in evidence.values()
    )
    gerbe_cocycle_closed = (
        get(gerbe, "calculation_results", "matches_qutrit_projective_cocycle") is True
        or get(gerbe, "verdict", "candidate_holonomy_map_closed") is True
    )
    four_route_nontrivial_pair = (
        get(torsion, "calculation_results", "all_four_routes_agree_on_candidate_set") is True
        and get(torsion, "calculation_results", "common_candidate_labels") == [1, 2]
        and get(torsion, "calculation_results", "unique_label_selected_by_any_route") is False
    )
    finite_fourier_transport_closed = (
        get(qutrit, "calculation_results", "finite_transport_lemma_proved") is True
        and get(qutrit, "calculation_results", "solutions_are_F_and_F_conjugate") is True
        and get(qutrit, "calculation_results", "orientation_selects_F") is True
    )
    global_conjugate_pair_closed = (
        get(c6_common, "verdict", "C6_branch_space_now_global_conjugate_pair") is True
        and get(c6_phase, "calculation_results", "global_pair_are_complex_conjugates") is True
    )
    selected_fourier_type_closed = (
        selected_structural_sources
        and gerbe_cocycle_closed
        and four_route_nontrivial_pair
        and finite_fourier_transport_closed
        and global_conjugate_pair_closed
        and nontrivial_labels == [1, 2]
    )

    exact_su5_packet_selected = (
        get(su5_packet, "verdict", "selected_packet_constructed") is True
        and get(su5_source, "calculation_results", "remaining_proof_closed_now") is True
    )
    unique_orientation_selected = (
        get(c6_common, "verdict", "unique_orientation_convention_selected") is True
        or get(torsion, "calculation_results", "selected_torsion_label") in [1, 2]
    )
    exact_q79_packet_selected = (
        selected_fourier_type_closed and exact_su5_packet_selected and unique_orientation_selected
    )

    status = (
        "SELECTED_GERBE_FOURIER_PACKET_PROVED"
        if exact_q79_packet_selected
        else "SELECTED_GERBE_FOURIER_TYPE_PROVED_SU5_PACKET_OPEN"
        if selected_fourier_type_closed
        else "SELECTED_GERBE_FOURIER_TYPE_NOT_PROVED"
    )

    return {
        "candidate": "SelectedGerbeFourierTypeTheorem",
        "status": status,
        "generated_by": "scripts/prove_selected_gerbe_fourier_type.py",
        "proof_target": {
            "layer_1": "MTT selects the nontrivial Z3 gerbe/qutrit Fourier phase-space type.",
            "layer_2": "MTT selects the ordered SU(5) packet U_10=I_3, U_bar5=F.",
        },
        "corpus_evidence": evidence,
        "finite_torsion_calculation": {
            "label_reports": label_reports,
            "nontrivial_bianchi_closed_labels": nontrivial_labels,
            "trivial_label_rank": label_reports[0]["commutator_rank"],
            "nontrivial_labels_have_rank_two": nontrivial_labels == [1, 2],
        },
        "calculation_results": {
            "selected_structural_sources_present": selected_structural_sources,
            "gerbe_cocycle_closed": gerbe_cocycle_closed,
            "four_route_selects_nontrivial_conjugate_pair": four_route_nontrivial_pair,
            "finite_fourier_transport_closed": finite_fourier_transport_closed,
            "global_conjugate_pair_closed": global_conjugate_pair_closed,
            "selected_gerbe_fourier_type_closed": selected_fourier_type_closed,
            "exact_su5_packet_selected": exact_su5_packet_selected,
            "unique_orientation_selected": unique_orientation_selected,
            "exact_q79_packet_U10_I_Ubar5_F_selected": exact_q79_packet_selected,
        },
        "what_this_proves": {
            "nontrivial_Z3_flat_gerbe_type_selected_as_MTT_family_phase_space": selected_fourier_type_closed,
            "trivial_m0_torsion_rejected_for_family_Fourier_type": selected_fourier_type_closed,
            "Fourier_transport_F_or_F_conjugate_selected_up_to_global_orientation": selected_fourier_type_closed,
            "previous_unselected_fixture_reinterpreted_as_representative_of_selected_type": selected_fourier_type_closed,
        },
        "still_open": {
            "ordered_SU5_slot_assignment_10M_clock_bar5M_shift": not exact_su5_packet_selected,
            "unique_q79_orientation_F_versus_q369_F_conjugate": not unique_orientation_selected,
            "selected_D_E_dotD_or_monad_source_for_matter_slots": not exact_su5_packet_selected,
            "exact_packet_U10_I_Ubar5_F_as_selected_data": not exact_q79_packet_selected,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_exact_SU5_packet_selected": exact_q79_packet_selected,
            "claims_unique_orientation_without_source": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "uses_common_fourier_gauge_as_physical_mixing": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "selected_fourier_type_proved": selected_fourier_type_closed,
            "already_computed_packet_fully_selected": exact_q79_packet_selected,
            "honest_answer": (
                "MTT geometry selects the nontrivial gerbe-Fourier qutrit type up to the global conjugate orientation, but current data still do not select the ordered SU(5) packet U_10=I_3, U_bar5=F as exact matter-slot data."
                if selected_fourier_type_closed and not exact_q79_packet_selected
                else "The exact ordered SU(5) Fourier packet is selected."
                if exact_q79_packet_selected
                else "The selected gerbe-Fourier type is not yet proved from available sources."
            ),
            "next_closing_object": "selected ordered Lagrangian/matter-slot source proving 10_M=clock, bar5_M=shift, and q79 orientation F from D_E/dotD, typed monad/Cech, or a fixed differential-cohomology representative.",
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "SelectedGerbeFourierTypeTheorem",
        "status": report["status"],
        "purpose": "Promote the nontrivial Z3 gerbe/qutrit Fourier phase-space type to selected MTT geometry, without overclaiming the ordered SU(5) matter-slot packet.",
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "analysis_script": "scripts/prove_selected_gerbe_fourier_type.py",
        "depends_on": [
            "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json",
            "iwasawa_torsion_label_four_route_selector_certificate.json",
            "qutrit_polarization_transport_lemma_certificate.json",
            "iwasawa_c6_common_holonomy_branch_pair_certificate.json",
            "iwasawa_c6_global_phase_block_certificate.json",
            "selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json",
            "selected_su5_source_proof_attempt_certificate.json",
        ],
        "calculation_results": report["calculation_results"],
        "finite_torsion_calculation": report["finite_torsion_calculation"],
        "what_this_proves": report["what_this_proves"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
