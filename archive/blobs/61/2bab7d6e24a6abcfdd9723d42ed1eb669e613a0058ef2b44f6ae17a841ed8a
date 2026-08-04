"""Analyze the Gauduchon wall needed for visible L^2 branch selection.

The previous orientation gate identified the target selector as a
source-certified slope wall

    p1:p2 = 1:2.

This script translates that abstract slope wall into the Iwasawa metric radii.
For

    J = r1^2 a + r2^2 b + r3^2 c,

the Gauduchon slope of l=x a+y b+z c is proportional to

    x r2^2 r3^2 + y r1^2 r3^2 + z r1^2 r2^2.

After a positive common rescaling this is the same p-vector used in the
split-line HYM no-go:

    p = (r2^2/r3^2, r1^2/r3^2, r1^2/r2^2).

Thus p1:p2=1:2 means r2^2:r1^2=1:2, i.e. r1:r2=sqrt(2):1.
Current selected Iwasawa source packets only support the symmetric/equal-radius
specialization r1=r2, while the flux corpus says the invariant Iwasawa shape
modulus is not fully fixed at first order.  So this gate remains open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

ORIENTATION_GATE = CERTIFICATES / "selected_pullback_l2_branch_orientation_source_gate_certificate.json"
RPLUS_SUPPORT = CERTIFICATES / "c1_iwasawa_rplus_support_certificate.json"
CHERN_GATE = CERTIFICATES / "visible_chern_weil_quantization_gate_certificate.json"
SPLIT_NO_GO = CERTIFICATES / "visible_split_line_hym_no_go_certificate.json"

FLUX_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)
SELECTION_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
)

CANDIDATE = CANDIDATE_DATA / "selected_gauduchon_wall_radius_gate.candidate.json"
CERTIFICATE = CERTIFICATES / "selected_gauduchon_wall_radius_gate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def slope_value(branch: list[int], p1: int, p2: int, p3: int = 1) -> int:
    return branch[0] * p1 + branch[1] * p2 + branch[2] * p3


def chamber(branches: list[list[int]], p1: int, p2: int) -> dict[str, Any]:
    values = [{"branch": branch, "slope": slope_value(branch, p1, p2)} for branch in branches]
    return {
        "p": [p1, p2, 1],
        "negative": [entry["branch"] for entry in values if entry["slope"] < 0],
        "zero": [entry["branch"] for entry in values if entry["slope"] == 0],
        "positive": [entry["branch"] for entry in values if entry["slope"] > 0],
        "values": values,
    }


def analyze() -> dict[str, Any]:
    orientation = load_json(ORIENTATION_GATE)
    rplus = load_json(RPLUS_SUPPORT)
    chern = load_json(CHERN_GATE)
    split = load_json(SPLIT_NO_GO)
    flux_text = read(FLUX_SOURCE)
    selection_text = read(SELECTION_SOURCE)

    branches = [[-2, 1, 0], [-1, 2, 0], [1, -2, 0], [2, -1, 0]]
    target = [1, -2, 0]
    swapped = [-2, 1, 0]

    source_clues = {
        "flux_source_present": FLUX_SOURCE.exists(),
        "selection_source_present": SELECTION_SOURCE.exists(),
        "iwasawa_shape_modulus_open_in_flux_source": (
            "radii $(r_1,r_2,r_3)$ and bundle moduli enter continuously" in flux_text
            and "an overall volume/shape modulus remains" in flux_text
        ),
        "selection_source_equal_radius_specialization": "With $r_1=r_2=:R$" in selection_text,
        "selection_source_iwasawa_fixes_r3_not_r1_over_r2": (
            "Iwasawa fixes $r_3$" in selection_text
            and "Lens" in selection_text
            and "fixes $R_1/R$" in selection_text
        ),
    }

    slope_radius_map = {
        "J": "J = r1^2 a + r2^2 b + r3^2 c",
        "line_class": "l = x a + y b + z c",
        "raw_slope_pairing": "int_X l wedge J^2 = 2*(x*r2^2*r3^2 + y*r1^2*r3^2 + z*r1^2*r2^2)",
        "normalized_p_vector": [
            "p1 = r2^2/r3^2",
            "p2 = r1^2/r3^2",
            "p3 = r1^2/r2^2",
        ],
        "p1_over_p2": "r2^2/r1^2",
        "matches_split_no_go_p_vector": split.get("algebraic_no_go", {}).get("slope_vector")
        == "p=(r2^2/r3^2, r1^2/r3^2, r1^2/r2^2), all entries positive",
    }

    walls = {
        "target_wall": {
            "p1:p2": "1:2",
            "radius_condition": "r2^2:r1^2 = 1:2",
            "equivalent_radius_ratio": "r1:r2 = sqrt(2):1",
            "chamber": chamber(branches, 1, 2),
            "selects_target_as_unique_negative": chamber(branches, 1, 2)["negative"]
            == [target],
        },
        "swapped_wall": {
            "p1:p2": "2:1",
            "radius_condition": "r2^2:r1^2 = 2:1",
            "equivalent_radius_ratio": "r2:r1 = sqrt(2):1",
            "chamber": chamber(branches, 2, 1),
            "selects_swapped_as_unique_negative": chamber(branches, 2, 1)["negative"]
            == [swapped],
        },
        "symmetric_source": {
            "p1:p2": "1:1",
            "radius_condition": "r1 = r2",
            "chamber": chamber(branches, 1, 1),
            "selects_unique_branch": len(chamber(branches, 1, 1)["negative"]) == 1,
        },
    }

    current_source_status = {
        "rplus_status": rplus.get("status"),
        "chern_gate_status": chern.get("status"),
        "orientation_gate_status": orientation.get("status"),
        "rplus_equal_radius_assumption": rplus.get("rplus_support", {})
        .get("equal_radius_specialization", {})
        .get("assumption"),
        "chern_equal_radius_assumption": chern.get("existing_flux_row_consistency", {})
        .get("equal_radius_specialization", {})
        .get("assumption"),
        "source_certified_target_wall_present": False,
        "source_certified_integral_lift_present": False,
        "split_line_hym_can_select_wall": False,
        "reason_split_line_hym_cannot_select_wall": split.get("verdict", {}).get("honest_answer"),
    }

    route_evaluation = [
        {
            "id": "derive_target_wall_from_existing_iwasawa_flux_packets",
            "status": "BLOCKED",
            "reason": (
                "Current selected Iwasawa packets either keep the shape modulus open "
                "or specialize to r1=r2. They do not select r1:r2=sqrt(2):1."
            ),
        },
        {
            "id": "derive_target_wall_from_split_line_hym_primitivity",
            "status": "REJECTED_AS_VISIBLE_SOURCE_SELECTOR",
            "reason": (
                "The split line/Cartan HYM route is already ruled out for the "
                "positive alpha1 visible source row. It may diagnose walls but "
                "cannot serve as the selected visible source."
            ),
        },
        {
            "id": "construct_new_nonabelian_or_route_c_wall_source",
            "status": "LIVE",
            "reason": (
                "A genuinely nonabelian stable/sheaf source or Route-C residual "
                "could in principle select r1:r2=sqrt(2):1 and supply D_E/dotD."
            ),
        },
        {
            "id": "integral_cech_de_lift_of_finite_qutrit_class",
            "status": "LIVE",
            "reason": (
                "This bypasses metric-wall selection by lifting the finite (1,1) "
                "qutrit class to the integer branch (1,-2,0)."
            ),
        },
    ]

    return {
        "calculation": "SelectedGauduchonWallRadiusGate",
        "status": "GAUDUCHON_WALL_REDUCED_TO_RADIUS_RATIO_SOURCE_OPEN",
        "generated_by": "scripts/analyze_selected_gauduchon_wall_radius_gate.py",
        "input_certificates": {
            "orientation_gate": ORIENTATION_GATE.name,
            "c1_iwasawa_rplus_support": RPLUS_SUPPORT.name,
            "visible_chern_weil_quantization_gate": CHERN_GATE.name,
            "visible_split_line_hym_no_go": SPLIT_NO_GO.name,
        },
        "corpus_sources": {
            "flux_compactifications": str(FLUX_SOURCE),
            "mtt_selection_principle_for_flux": str(SELECTION_SOURCE),
        },
        "source_clues": source_clues,
        "slope_radius_map": slope_radius_map,
        "wall_dictionary": walls,
        "current_source_status": current_source_status,
        "route_evaluation": route_evaluation,
        "what_this_closes": {
            "abstract_p_wall_translated_to_iwasawa_radii": True,
            "target_wall_requires_r1_over_r2_sqrt2": True,
            "current_equal_radius_sources_do_not_select_target_wall": True,
            "iwasawa_flux_corpus_does_not_currently_close_shape_ratio": True,
            "split_line_hym_wall_shortcut_rejected_for_visible_source": True,
        },
        "still_open": {
            "source_certified_r1_over_r2_sqrt2_wall": True,
            "nonabelian_or_route_c_derivation_of_target_wall": True,
            "integral_cech_or_de_lift_selecting_L_1_minus2_0": True,
            "flat_pic0_or_torsion_character_selection": True,
            "non_split_extension_stability": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_target_wall_selected": False,
            "claims_L_branch_selected": False,
            "claims_equal_radius_selects_target": False,
            "claims_split_line_hym_source_reopened": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "next_required_packet": {
            "name": "Selected_Iwasawa_Gauduchon_Wall_or_Integral_Lift.v1",
            "minimal_success_criteria": [
                "derive r1:r2=sqrt(2):1 from selected nonabelian/Route-C source data, or",
                "derive an integral Cech/D_E lift of the finite qutrit class to L=(1,-2,0)",
                "select or eliminate the flat Pic0/torsion character",
                "prove non-split extension stability in the selected source chamber",
                "supply same-source D_E/dotD/Riesz/Green data",
            ],
        },
        "verdict": {
            "honest_answer": (
                "The target slope wall p1:p2=1:2 is equivalent on Iwasawa to "
                "r1:r2=sqrt(2):1. Current audited source data do not select this "
                "wall: they either use the symmetric r1=r2 specialization or leave "
                "the Iwasawa shape ratio open. Therefore the wall route remains "
                "live but not closed. The parallel live route is an integral "
                "Cech/D_E lift of the finite qutrit class to L=(1,-2,0)."
            ),
            "next_action": (
                "Attempt a selected nonabelian/Route-C source that outputs "
                "r1:r2=sqrt(2):1, or attempt the integral Cech/D_E lift directly."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "SelectedGauduchonWallRadiusGate",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/selected_gauduchon_wall_radius_gate.candidate.json",
        "input_certificates": report["input_certificates"],
        "corpus_sources": report["corpus_sources"],
        "source_clues": report["source_clues"],
        "slope_radius_map": report["slope_radius_map"],
        "wall_dictionary": report["wall_dictionary"],
        "current_source_status": report["current_source_status"],
        "route_evaluation": report["route_evaluation"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "next_required_packet": report["next_required_packet"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
