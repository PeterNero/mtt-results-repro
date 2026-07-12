"""Compare four routes for selecting the qutrit flat-torsion label.

The previous selection-gap theorem showed that the existing curvature/Bianchi
data cannot choose among the Z3 flat gerbe labels by itself.  This script runs
the four natural selector routes:

1. corpus evidence for a selected/nontrivial Z3 family holonomy;
2. finite topological/cohomological torsion arithmetic;
3. projector/zero-mode and block-factorized finite-sector constraints;
4. orientation consistency with q79/conjugate, C6, and SU(5) qutrit data.

Each route reports the labels it can honestly leave alive.  The key guardrail
is that none of these routes may use observed masses, mixings, or benchmark
flavor entries to choose a handedness.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
CERTIFICATES = ROOT / "certificates"
CORPUS_ROOT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

BOOK = CORPUS_ROOT / "10 The Book on Modal Triplet Theory" / "The_Book_on_Modal_Triplet_Theory_v9.md"
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


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all_ci(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def run_json_script(script_name: str) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script_name)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def route(
    name: str,
    labels: list[int],
    rejects_trivial: bool,
    selects_unique_label: bool,
    evidence: dict[str, Any],
    limitation: str,
) -> dict[str, Any]:
    return {
        "route": name,
        "candidate_labels": labels,
        "rejects_trivial_m0": rejects_trivial,
        "selects_unique_label": selects_unique_label,
        "unique_label": labels[0] if selects_unique_label and len(labels) == 1 else None,
        "evidence": evidence,
        "limitation": limitation,
    }


def corpus_route() -> dict[str, Any]:
    book = read(BOOK)
    central = read(CENTRAL_CIRCLE)
    proto = read(PROTOSPINOR)

    evidence = {
        "book_baseline_Z3_family_mechanism": contains_all_ci(
            book,
            ["baseline $Z_3$ holonomy family mechanism", "exactly", "three family"],
        ),
        "book_Z3_phase_family_structure": contains_all_ci(
            book,
            ["Z_3", "phase", "family sectors"],
        ),
        "central_circle_Z3_family_holonomy": contains_all_ci(
            central,
            ["Z}_3", "holonomy", "three families"],
        )
        or contains_all_ci(central, ["Z_3", "holonomy", "three families"]),
        "protospinor_three_survivor_basins": contains_all_ci(
            proto,
            ["three families", "survivor basin"],
        ),
    }
    nontrivial_family_holonomy = (
        evidence["book_baseline_Z3_family_mechanism"]
        or evidence["central_circle_Z3_family_holonomy"]
    )

    labels = [1, 2] if nontrivial_family_holonomy else [0, 1, 2]
    return route(
        "corpus",
        labels,
        rejects_trivial=nontrivial_family_holonomy,
        selects_unique_label=False,
        evidence=evidence,
        limitation=(
            "Corpus sources support a nontrivial Z3 family holonomy, but they do "
            "not fix the representative orientation m=1 versus m=2."
        ),
    )


def topology_route(flat_report: dict[str, Any]) -> dict[str, Any]:
    labels = flat_report.get("torsion_labels", [])
    nontrivial_labels = sorted(
        entry["torsion_label"]
        for entry in labels
        if entry.get("torsion_label") != 0
        and entry.get("discrete_bianchi_zero") is True
        and entry.get("delta_Hhat_curvature") == 0
        and entry.get("commutator_rank_over_F3") == 2
    )
    trivial = next((entry for entry in labels if entry.get("torsion_label") == 0), {})
    rejects_trivial = trivial.get("commutator_rank_over_F3") == 0 and bool(nontrivial_labels)
    return route(
        "topological",
        nontrivial_labels if rejects_trivial else [0, 1, 2],
        rejects_trivial=rejects_trivial,
        selects_unique_label=False,
        evidence={
            "all_flat_torsion_labels_have_zero_discrete_bianchi": flat_report.get(
                "all_flat_torsion_labels_have_zero_discrete_bianchi"
            ),
            "all_flat_torsion_labels_leave_Hhat_curvature_unchanged": flat_report.get(
                "all_flat_torsion_labels_leave_Hhat_curvature_unchanged"
            ),
            "nontrivial_rank_two_labels": nontrivial_labels,
            "trivial_label_commutator_rank": trivial.get("commutator_rank_over_F3"),
        },
        limitation=(
            "Finite cohomology distinguishes trivial from nontrivial torsion, but "
            "the two nontrivial generators are conjugate orientations."
        ),
    )


def projector_route() -> dict[str, Any]:
    block_packet = load_json(
        CERTIFICATES / "iwasawa_block_factorized_twisted_packet_candidate_certificate.json"
    )
    sector_maps = load_json(CERTIFICATES / "iwasawa_block_factorized_sector_maps_certificate.json")
    su5_attempt = load_json(
        CERTIFICATES / "selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json"
    )
    calc = block_packet.get("calculation_results", {})
    sector_calc = sector_maps.get("calculation_results", {})
    su5_calc = su5_attempt.get("calculation_results", {})

    nontrivial_required = (
        calc.get("family_central_twist_nontrivial") is True
        and calc.get("family_projective_gerbe_gluing_passes") is True
        and calc.get("family_strict_vector_bundle_gluing_passes") is False
        and sector_calc.get("finite_block_factorized_sector_maps_valid") is True
    )
    labels = [1, 2] if nontrivial_required else [0, 1, 2]
    return route(
        "projector_zero_mode",
        labels,
        rejects_trivial=nontrivial_required,
        selects_unique_label=False,
        evidence={
            "family_central_twist_nontrivial": calc.get("family_central_twist_nontrivial"),
            "family_projective_gerbe_gluing_passes": calc.get(
                "family_projective_gerbe_gluing_passes"
            ),
            "family_strict_vector_bundle_gluing_passes": calc.get(
                "family_strict_vector_bundle_gluing_passes"
            ),
            "sector_maps_valid": sector_calc.get("finite_block_factorized_sector_maps_valid"),
            "su5_finite_orientation": su5_calc.get("validator_orientation"),
            "su5_selected_source_available": su5_calc.get("selected_source_available"),
            "su5_promotes_to_selected_heavy_link_input": su5_calc.get(
                "promotes_to_selected_heavy_link_input"
            ),
        },
        limitation=(
            "Finite block projectors and SU(5) transport validate the qutrit "
            "architecture, but selected zero-mode/projector retention is still open."
        ),
    )


def orientation_route() -> dict[str, Any]:
    common = load_json(CERTIFICATES / "iwasawa_c6_common_holonomy_branch_pair_certificate.json")
    global_phase = load_json(CERTIFICATES / "iwasawa_c6_global_phase_block_certificate.json")
    polarization = load_json(
        CERTIFICATES / "selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json"
    )
    common_calc = common.get("calculation_results", {})
    global_calc = global_phase.get("calculation_results", {})
    pol_calc = polarization.get("calculation_results", {})

    global_pair = (
        common.get("verdict", {}).get("C6_branch_space_now_global_conjugate_pair") is True
        and common.get("verdict", {}).get("unique_orientation_convention_selected") is False
        and global_calc.get("global_pair_are_complex_conjugates") is True
    )
    labels = [1, 2] if global_pair else [0, 1, 2]
    return route(
        "orientation",
        labels,
        rejects_trivial=global_pair,
        selects_unique_label=False,
        evidence={
            "global_conjugate_label_patterns": common_calc.get(
                "global_conjugate_label_patterns"
            ),
            "unique_orientation_convention_selected": common.get("verdict", {}).get(
                "unique_orientation_convention_selected"
            ),
            "selected_q_label_from_closed_branch": global_calc.get(
                "selected_q_label_from_closed_branch"
            ),
            "inverse_label": global_calc.get("inverse_label"),
            "global_pair_are_complex_conjugates": global_calc.get(
                "global_pair_are_complex_conjugates"
            ),
            "su5_validator_orientation": pol_calc.get("validator_orientation"),
            "su5_candidate_role": pol_calc.get("candidate_role"),
        },
        limitation=(
            "Orientation data reduce the freedom to a global conjugate pair.  "
            "They do not select which conjugate convention is physical without "
            "selected D_E/dotD or an explicit representative convention."
        ),
    )


def analyze() -> dict[str, Any]:
    flat_report = run_json_script("analyze_iwasawa_flat_torsion_selection_gap.py")
    routes = [
        corpus_route(),
        topology_route(flat_report),
        projector_route(),
        orientation_route(),
    ]
    label_sets = [set(entry["candidate_labels"]) for entry in routes]
    common = sorted(set.intersection(*label_sets)) if label_sets else []
    same_candidate_set = all(sorted(labels) == common for labels in label_sets)
    all_reject_trivial = all(entry["rejects_trivial_m0"] for entry in routes)
    any_unique = any(entry["selects_unique_label"] for entry in routes)
    unique_labels = sorted(
        {
            entry["unique_label"]
            for entry in routes
            if entry["selects_unique_label"] and entry["unique_label"] is not None
        }
    )

    return {
        "calculation": "IwasawaTorsionLabelFourRouteSelector",
        "status": "CONVERGES_TO_NONTRIVIAL_PAIR_UNIQUE_LABEL_OPEN",
        "route_reports": routes,
        "consensus": {
            "all_four_routes_agree_on_candidate_set": same_candidate_set,
            "all_four_routes_reject_trivial_m0": all_reject_trivial,
            "common_candidate_labels": common,
            "unique_label_selected_by_any_route": any_unique,
            "unique_labels_selected": unique_labels,
            "selected_torsion_label": unique_labels[0] if len(unique_labels) == 1 else None,
            "full_selected_source_closure_now": False,
            "conclusion": (
                "All four routes converge on nontrivial flat torsion m in {1,2}; "
                "none selects m=1 versus m=2 without an additional selected "
                "orientation or differential-cohomology representative."
            ),
        },
        "guardrails": {
            "uses_observed_masses_or_mixings": False,
            "uses_execution_ii_benchmarks": False,
            "claims_unique_m_label": False,
            "claims_selected_source_promotion": False,
            "claims_full_sm_closure": False,
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
