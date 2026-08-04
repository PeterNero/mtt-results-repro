"""Check whether the constants-side selected radius can select visible L^2.

The visible rank-two route needs a source-certified Gauduchon wall

    p1:p2 = 1:2,

equivalently r1:r2 = sqrt(2):1 on the Iwasawa metric

    J = r1^2 a + r2^2 b + r3^2 c.

The constants/no-knob repository has a closed selected internal radius, but it
is selected along the branch

    (r1,r2,r3) = (R,R,r3(R)).

This script imports that branch and checks what it does to the visible L^2
selector.  The result is a no-go for this particular import: it lands in the
symmetric chamber p1:p2=1:1, where target and swapped L branches remain
degenerate.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

CONSTANTS_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
CONSTANTS_CERTIFICATES = CONSTANTS_REPO / "certificates"
FINAL_RADIUS_CERT = (
    CONSTANTS_CERTIFICATES / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
)
HORIZONTAL_SCALE_CERT = CONSTANTS_CERTIFICATES / "selected_horizontal_scale_law_certificate.json"

GAUDUCHON_GATE = CERTIFICATES / "selected_gauduchon_wall_radius_gate_certificate.json"
SELECTOR_OBSTRUCTION = CERTIFICATES / "visible_rank2_l2_selector_obstruction_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_selected_radius_import_nogo.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_selected_radius_import_nogo_certificate.json"

TARGET = (1, -2, 0)
SWAPPED = (-2, 1, 0)
CONJ_TARGET = (-1, 2, 0)
CONJ_SWAPPED = (2, -1, 0)
BRANCHES = [SWAPPED, CONJ_TARGET, TARGET, CONJ_SWAPPED]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def slope(branch: tuple[int, int, int], p: tuple[float, float, float]) -> float:
    return branch[0] * p[0] + branch[1] * p[1] + branch[2] * p[2]


def chamber(name: str, p: tuple[float, float, float]) -> dict[str, Any]:
    values = [{"branch": list(branch), "slope": slope(branch, p)} for branch in BRANCHES]
    return {
        "name": name,
        "p": list(p),
        "negative": [entry["branch"] for entry in values if entry["slope"] < -1e-12],
        "zero": [entry["branch"] for entry in values if abs(entry["slope"]) <= 1e-12],
        "positive": [entry["branch"] for entry in values if entry["slope"] > 1e-12],
        "values": values,
    }


def selected_radius_geometry(final_radius: dict[str, Any]) -> dict[str, Any]:
    values = final_radius.get("selected_values", {})
    r1 = float(values.get("R_star", float("nan")))
    r2 = r1
    r3 = float(values.get("r3", float("nan")))
    p1 = (r2 * r2) / (r3 * r3)
    p2 = (r1 * r1) / (r3 * r3)
    p3 = (r1 * r1) / (r2 * r2)
    return {
        "source_branch": "(r1,r2,r3)=(R,R,r3(R))",
        "r1": r1,
        "r2": r2,
        "r3": r3,
        "p": [p1, p2, p3],
        "p1_over_p2": p1 / p2,
        "r1_over_r2": r1 / r2,
        "target_wall_r1_over_r2": math.sqrt(2.0),
        "r1_equals_r2": math.isclose(r1, r2, rel_tol=0.0, abs_tol=1e-15),
        "p1_equals_p2": math.isclose(p1, p2, rel_tol=0.0, abs_tol=1e-15),
        "matches_target_wall": math.isclose(r1 / r2, math.sqrt(2.0), rel_tol=1e-12),
    }


def analyze() -> dict[str, Any]:
    final_radius = load_json(FINAL_RADIUS_CERT)
    horizontal_scale = load_json(HORIZONTAL_SCALE_CERT)
    gauduchon_gate = load_json(GAUDUCHON_GATE)
    selector_obstruction = load_json(SELECTOR_OBSTRUCTION)

    geometry = selected_radius_geometry(final_radius)
    imported_p = tuple(float(value) for value in geometry["p"])
    chambers = {
        "target_wall": chamber("target_wall_p1_p2_1_2", (1.0, 2.0, 1.0)),
        "symmetric_import": chamber("constants_import_p1_p2_1_1", imported_p),
        "swapped_wall": chamber("swapped_wall_p1_p2_2_1", (2.0, 1.0, 1.0)),
    }

    target_negative = [list(TARGET)]
    target_and_swapped_negative = [list(SWAPPED), list(TARGET)]
    no_go_passes = (
        final_radius.get("status") == "FINAL_INTERNAL_RHO_UV_BRANCH_CLOSED"
        and horizontal_scale.get("status") == "H2_HORIZONTAL_SCALE_LAW_SELECTED"
        and geometry["r1_equals_r2"] is True
        and geometry["p1_equals_p2"] is True
        and geometry["matches_target_wall"] is False
        and chambers["target_wall"]["negative"] == target_negative
        and chambers["symmetric_import"]["negative"] == target_and_swapped_negative
    )

    return {
        "calculation": "VisibleRank2L2SelectedRadiusImportNoGo",
        "status": (
            "VISIBLE_RANK2_L2_SELECTED_RADIUS_IMPORT_NO_GO_EQUAL_RADIUS"
            if no_go_passes
            else "VISIBLE_RANK2_L2_SELECTED_RADIUS_IMPORT_CHECK_INCONCLUSIVE"
        ),
        "generated_by": "scripts/analyze_visible_rank2_l2_selected_radius_import_nogo.py",
        "imported_certificates": {
            "constants_final_radius": {
                "path": str(FINAL_RADIUS_CERT),
                "status": final_radius.get("status"),
            },
            "constants_horizontal_scale_law": {
                "path": str(HORIZONTAL_SCALE_CERT),
                "status": horizontal_scale.get("status"),
                "selected_law": horizontal_scale.get("selected_law", {}).get("id"),
            },
            "q79_gauduchon_wall_gate": {
                "path": str(GAUDUCHON_GATE),
                "status": gauduchon_gate.get("status"),
            },
            "q79_selector_obstruction": {
                "path": str(SELECTOR_OBSTRUCTION),
                "status": selector_obstruction.get("status"),
            },
        },
        "imported_selected_radius_geometry": geometry,
        "visible_slope_dictionary": {
            "line_class": "L=(x,y,z)",
            "slope_pairing": "mu_J(L) proportional to x*r2^2*r3^2 + y*r1^2*r3^2 + z*r1^2*r2^2",
            "normalized_p": [
                "p1=r2^2/r3^2",
                "p2=r1^2/r3^2",
                "p3=r1^2/r2^2",
            ],
            "target_selector_condition": "p1:p2=1:2, equivalently r1:r2=sqrt(2):1",
            "constants_import_condition": "p1:p2=1:1, equivalently r1=r2",
        },
        "branch_chambers": chambers,
        "no_go_theorem": {
            "theorem": "The closed constants selected radius cannot be the visible L2 target-wall selector.",
            "proof": [
                "The constants-side selected radius is selected on the branch (r1,r2,r3)=(R,R,r3(R)).",
                "Therefore its visible slope vector has p1=p2.",
                "When p1=p2, L=(1,-2,0) and L=(-2,1,0) both have negative slope and remain base-swap degenerate.",
                "The target visible selector requires p1:p2=1:2, equivalently r1:r2=sqrt(2):1.",
                "Since 1 is not sqrt(2), importing the closed constants radius as the visible Gauduchon metric cannot select the target branch.",
            ],
            "does_not_claim": [
                "the constants rho_UV theorem is wrong",
                "the target visible branch is impossible",
                "MTT cannot contain a separate non-equal-radius wall source",
                "full SM closure",
            ],
        },
        "what_this_closes": {
            "constants_selected_radius_import_tested": True,
            "constants_import_is_equal_horizontal_radius": geometry["r1_equals_r2"],
            "constants_import_lands_in_symmetric_visible_chamber": geometry["p1_equals_p2"],
            "constants_import_does_not_match_target_wall": not geometry["matches_target_wall"],
            "constants_import_leaves_target_and_swapped_degenerate": chambers["symmetric_import"][
                "negative"
            ]
            == target_and_swapped_negative,
        },
        "still_open": {
            "selected_non_equal_radius_wall_source_r1_over_r2_sqrt2": True,
            "selected_ordered_integral_Cech_automorphy_D_E_source": True,
            "selected_or_quotiented_Pic0_character": True,
            "same_source_D_E_dotD_Hessian_base_ordering": True,
            "non_split_extension_stability": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_constants_radius_selects_visible_target": False,
            "claims_target_wall_selected": False,
            "claims_L_branch_selected": False,
            "claims_constants_repo_invalid": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The constants/no-knob selected internal radius is compatible with "
                "an equal-horizontal Iwasawa branch, not with the visible target "
                "wall r1:r2=sqrt(2):1. Imported directly as the visible metric, it "
                "selects the symmetric chamber and leaves L=(1,-2,0) tied with "
                "L=(-2,1,0). Thus it complements the q79 work but cannot close "
                "the visible L2 selector by itself."
            ),
            "next_action": (
                "Do not use the constants R_star as the target-wall source. "
                "Continue with either a genuinely non-equal-radius selected source "
                "or the ordered integral Cech/automorphy/D_E lift."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2SelectedRadiusImportNoGo",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_selected_radius_import_nogo.candidate.json",
        "imported_certificates": report["imported_certificates"],
        "imported_selected_radius_geometry": report["imported_selected_radius_geometry"],
        "visible_slope_dictionary": report["visible_slope_dictionary"],
        "branch_chambers": report["branch_chambers"],
        "no_go_theorem": report["no_go_theorem"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"].endswith("EQUAL_RADIUS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
