from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REV = ROOT / "revised_tex_vnext"

EXPECTED_PROJECTS = {
    "A_Tiered_Roadmap_for_Calculations_in_Modal_Triplet_Theory__MTT__v3",
    "Superset_Determinations_in_Modal_Triplet_Theory_v3",
    "Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v3",
    "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v3",
    "Geometry__Light_Relations_in_Modal_Triplet_Theory__MTT__v3",
    "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry_v2",
    "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps_v2",
    "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization_v2",
    "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale_v2",
    "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle_v2",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def check_environments(path: Path, text: str) -> None:
    begins = re.findall(r"\\begin\{([^}]+)\}", text)
    ends = re.findall(r"\\end\{([^}]+)\}", text)
    require(len(begins) == len(ends), f"environment count mismatch: {path}")
    stack: list[str] = []
    for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
        action, environment = match.groups()
        if action == "begin":
            stack.append(environment)
        else:
            require(bool(stack), f"orphan end{{{environment}}}: {path}")
            require(stack.pop() == environment, f"misnested environment {environment}: {path}")
    if stack:
        raise AssertionError(f"unclosed environment {stack[-1]}: {path}")


def main() -> None:
    projects = {path.name for path in REV.iterdir() if path.is_dir() and path.name != "packages"}
    require(projects == EXPECTED_PROJECTS, "versioned TeX project inventory changed")
    require((REV / "REVISION_MANIFEST.md").exists(), "revision manifest missing")
    for project in sorted(projects):
        main_tex = REV / project / "main.tex"
        require(main_tex.exists(), f"main.tex missing: {project}")
        require((REV / project / "series.sty").exists(), f"series.sty missing: {project}")
        text = main_tex.read_text(encoding="utf-8")
        require("\\documentclass" in text and "\\begin{document}" in text and "\\end{document}" in text, f"incomplete TeX document: {project}")
        check_environments(main_tex, text)

    paper1 = (REV / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry_v2" / "main.tex").read_text(encoding="utf-8")
    require("SMDR~v1.3" in paper1, "Paper I lacks selected multi-loop transport")
    require("I_2/I_1=0.5110273\\pm0.0001231" in paper1, "Paper I weak-overlap target missing")
    require("I_3/I_1=0.158335\\pm0.001098" in paper1, "Paper I color-overlap target missing")
    require("correlation $-0.04578$" in paper1, "Paper I propagated ratio correlation missing")
    require("Scale separation and withdrawn legacy calibration" in paper1, "Paper I scale-separation theorem missing")
    require("One-loop renormalization group running to" not in paper1, "Paper I retains obsolete one-loop target section")
    require("Absolute scale calibration and quantum--gravity consistency" not in paper1, "Paper I retains obsolete scale calibration")
    require("0.560" not in paper1 and "0.229" not in paper1, "Paper I retains obsolete profile values")

    paper2 = (REV / "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps_v2" / "main.tex").read_text(encoding="utf-8")
    require("0.2555137R_1" in paper2, "Paper II retargeted lens value missing")
    require("0.9948493R_1" in paper2, "Paper II retargeted nil value missing")
    require("effective two-dimensional constant-curvature base" in paper2, "Paper II lens-base guard missing")
    require("calibrated existence result" in paper2, "Paper II calibration status missing")
    require(paper2.count("\\appendix") == 1, "Paper II appendix marker duplicated")
    require(paper2.count("\\section{Overlap definitions}") == 1, "Paper II overlap section duplicated")
    require("0.560" not in paper2 and "0.229" not in paper2, "Paper II retains obsolete ratios")

    paper3 = (REV / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization_v2" / "main.tex").read_text(encoding="utf-8")
    require("Conditional Twistor--Action Matching and Normalization Audit" in paper3, "Paper III title/status not revised")
    require("I_2}{I_1}=0.5110273\\pm0.0001231" in paper3, "Paper III weak-overlap target missing")
    require("I_3}{I_1}=0.158335\\pm0.001098" in paper3, "Paper III color-overlap target missing")
    require("Dependency audit" in paper3, "Paper III shared-input audit missing")
    require("dA_{\\mathrm{dir}}=2\\omega_{\\mathrm{FS}}" in paper3, "Paper III normalization bridge missing")
    require("not an independent normalization theorem" in paper3, "Paper III SU(3) limitation missing")
    require("fully independent and" not in paper3, "Paper III retains overclaim of full independence")
    require("complete Route~B normalization" not in paper3, "Paper III retains obsolete completion heading")

    paper4 = (REV / "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale_v2" / "main.tex").read_text(encoding="utf-8")
    require("Conditional Gravity Scaling and Cosmological Cutoff Audit" in paper4, "Paper IV title/status not revised")
    require("20.0706400" in paper4, "Paper IV updated volume coefficient missing")
    require("\\ell_{\\mathrm{int}}^6/G_{10}" in paper4, "Paper IV absolute-scale dependency missing")
    require("\\frac{2\\epsilon^2}{\\pi^2A_s}" in paper4, "Paper IV normalized tensor relation missing")
    require("legacy numerical tensor bound is withdrawn" in paper4, "Paper IV withdrawal missing")
    require("31.8" not in paper4 and "4.3\\times 10^{-30}" not in paper4, "Paper IV retains obsolete numerical result")
    require("model--independent upper bound" not in paper4, "Paper IV retains model-independent cosmology overclaim")

    paper5 = (REV / "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle_v2" / "main.tex").read_text(encoding="utf-8")
    require("Weak-Angle Round Trip and the Non-Circularity Criterion" in paper5, "Paper V title/status not revised")
    require("\\frac{3r_{21}(Q)}{5+3r_{21}(Q)}" in paper5, "Paper V weak-angle identity missing")
    require("s_W^2(M_t)=0.2346644\\pm0.0000433" in paper5, "Paper V selected-scale value missing")
    require("Gauge-profile round-trip theorem" in paper5, "Paper V round-trip theorem missing")
    require("cannot constitute an independent prediction" in paper5, "Paper V non-circularity result missing")
    require("earlier tree-level value near $0.2312$" in paper5, "Paper V legacy-result withdrawal missing")
    require("Explicit numerical evaluation at" not in paper5, "Paper V retains obsolete one-loop execution")

    execution1 = (REV / "Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v3" / "main.tex").read_text(encoding="utf-8")
    require("Gauge, HYM, Threshold, and Axion Status after True-SM Closure" in execution1, "Execution I title/status not revised")
    require("final audit closes 12/12 obligations" in execution1, "Execution I adopted-standard closure missing")
    require("81 table entries and all 729 cocycle" in execution1, "Execution I literal Cech witness missing")
    require("Y+Zr=0.00932703<r=0.01" in execution1, "Execution I HYM continuum certificate missing")
    require("K_{\\mathrm{threshold}}$ ledger closes 10/10" in execution1, "Execution I internal threshold closure missing")
    require("strict MTT-emitted value count remains\nzero" in execution1, "Execution I physical threshold limitation missing")
    require("\\mathcal A_{\\mathrm{total}}=0" in execution1, "Execution I complete-spectrum anomaly audit missing")
    require("Solving K\\\"ahler Moduli Ratios" not in execution1, "Execution I retains obsolete CY execution")

    execution2 = (REV / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v3" / "main.tex").read_text(encoding="utf-8")
    require("Flavor, CKM, Neutral, and Higgs Status after True-SM Closure" in execution2, "Execution II title/status not revised")
    require("27-by-27 qutrit--Weyl/minimal matrix ledger" in execution2, "Execution II matrix authority missing")
    require("2.3564680386\\times10^{-4}" in execution2, "Execution II CKM profile result missing")
    require("a_{\\mathrm{int}}=0.34195899479289005" in execution2, "Execution II neutral amplitude missing")
    require("Hermitian spectrum $[1,4,7]$" in execution2, "Execution II neutral spectrum missing")
    require("r_{\\mathrm{direct}}=\\frac{3}{6}=\\frac12" in execution2, "Execution II scale-only no-go missing")
    require("P_{\\mathrm{EW}}$ is counted once" in execution2, "Execution II shared-EW primitive status missing")
    require("Benchmark Yukawa matrices" not in execution2, "Execution II retains legacy fitted matrices")
    require("Higgs pole mass" not in execution2, "Execution II retains obsolete Higgs pole-mass claim")

    superset = (REV / "Superset_Determinations_in_Modal_Triplet_Theory_v3" / "main.tex").read_text(encoding="utf-8")
    require("Parameter Identifiability after True-SM Closure" in superset, "Superset title/status not revised")
    require("five disjoint status classes" in superset, "Superset claim taxonomy missing")
    require("final global audit closes 12/12 obligations" in superset, "Superset adopted closure missing")
    require("accepted values\nremain 0/10" in superset, "Superset strict magnitude limitation missing")
    require("Profile-standard identifiability" in superset, "Superset identifiability theorem missing")
    require("Predicted $\\alpha_s" not in superset, "Superset retains obsolete alpha_s prediction")

    geometry = (REV / "Geometry__Light_Relations_in_Modal_Triplet_Theory__MTT__v3" / "main.tex").read_text(encoding="utf-8")
    require("Exact Identities, Conditional Bounds, and Principal Symbols" in geometry, "Geometry-Light title/status not revised")
    require("Common characteristic cone" in geometry, "Geometry-Light principal-symbol theorem missing")
    require("compatible trivialization is an essential" in geometry, "Geometry-Light holonomy assumption guard missing")
    require("No internal-gap cutoff inference" in geometry, "Geometry-Light cutoff guard missing")
    require("not a numerical solar-system prediction" in geometry, "Geometry-Light PPN limitation missing")

    roadmap = (REV / "A_Tiered_Roadmap_for_Calculations_in_Modal_Triplet_Theory__MTT__v3" / "main.tex").read_text(encoding="utf-8")
    require("Audited Closure and Strict Upgrades" in roadmap, "Roadmap title/status not revised")
    require("final audit passes 12/12 obligations" in roadmap, "Roadmap adopted closure missing")
    require("The nine upgrades are" in roadmap, "Roadmap strict-upgrade ledger missing")
    require("This roadmap is intentionally non-looping" in roadmap, "Roadmap non-looping acceptance rule missing")
    require("M3: Tier~3 superset determinations (completed)" not in roadmap, "Roadmap retains obsolete Tier-3 completion")
    require("M4: Tier~4 execution" not in roadmap and "M5: Tier~4 execution" not in roadmap, "Roadmap retains obsolete Tier-4 completion")

    print(
        json.dumps(
            {
                "cloned_tex_projects": len(projects),
                "contextually_revised_projects": 10,
                "paper_I_common_scheme_transport": "closed",
                "paper_II_geometric_retargeting": "closed_at_calibrated_ansatz_tier",
                "paper_III_twistor_matching": "closed_as_conditional_cross_check",
                "paper_IV_gravity_cosmology": "closed_as_conditional_scaling_audit",
                "paper_V_weak_angle": "closed_as_round_trip_with_held_out_criterion",
                "execution_I": "closed_as_current_status_with_legacy_CY_retired",
                "execution_II": "closed_as_profile_standard_with_neutral_strict_frontier",
                "superset": "closed_as_parameter_identifiability_ledger",
                "geometry_light": "closed_with_typed_assumptions_and_principal_symbols",
                "roadmap": "closed_as_audited_non_looping_master_status",
                "remaining_projects_in_batch": 0,
                "tex_environment_checks": "pass",
            },
            indent=2,
        )
    )
    print("Theta TeX vNext revision audit passed")


if __name__ == "__main__":
    main()
