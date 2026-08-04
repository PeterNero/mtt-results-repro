from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THETA = ROOT / "revised_tex_vnext"
FIXED = ROOT.parent / "4 Fixed Points" / "revised_tex_vnext"
AUDIT = ROOT / "FIXED_POINTS_THETA_GEOMETRY_RECONCILIATION_AUDIT_2026-07-15.md"

THETA_PROJECTS = {
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

FIXED_PROJECTS = {
    "Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v6",
    "Fixed_Points_II__Fixed_Points_in_a_10D_Modal_Model_v3",
    "Fixed_Points_III__Disturbance___Damping_Balance_and_Stability_v4",
    "Fixed_Points_IV__Curvature__Centroid_Motion__and_Structural_Transitions_on_Bundle_Manifolds_v4",
    "Fixed_Points_V__Curvature_Coupling__Multi_Structure_Dynamics_and_Drivers_v6",
    "Fixed_Points_VI__Formal_Synthesis_and_Physical_Interpretations_v4",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def read(project_root: Path, project: str) -> str:
    path = project_root / project / "main.tex"
    require(path.exists(), f"missing paper: {path}")
    return path.read_text(encoding="utf-8")


def check_tex(path: Path, text: str) -> None:
    require(text.count("\\begin{document}") == 1, f"bad begin document count: {path}")
    require(text.count("\\end{document}") == 1, f"bad end document count: {path}")
    require("\t" not in text, f"tab character found: {path}")

    stack: list[str] = []
    for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
        action, environment = match.groups()
        if action == "begin":
            stack.append(environment)
        else:
            require(bool(stack), f"orphan end{{{environment}}}: {path}")
            require(stack.pop() == environment, f"misnested {environment}: {path}")
    require(not stack, f"unclosed environment {stack[-1] if stack else '?'}: {path}")


def main() -> None:
    require(AUDIT.exists(), "local reconciliation audit is missing")
    audit = AUDIT.read_text(encoding="utf-8")
    require("Scope: only the revised Fixed Points I--VI" in audit, "audit scope guard missing")
    require("20.0706400 R_1^3` survives only as auxiliary" in audit, "Theta IV tier change missing")
    require("No fixed-point estimate" in audit, "fixed-point survival statement missing")

    theta_projects = {p.name for p in THETA.iterdir() if p.is_dir() and p.name != "packages"}
    fixed_projects = {p.name for p in FIXED.iterdir() if p.is_dir()}
    require(theta_projects == THETA_PROJECTS, "Theta project inventory changed")
    require(fixed_projects == FIXED_PROJECTS, "Fixed Point project inventory changed")

    theta_text = {p: read(THETA, p) for p in THETA_PROJECTS}
    fixed_text = {p: read(FIXED, p) for p in FIXED_PROJECTS}
    for project, text in {**theta_text, **fixed_text}.items():
        base = THETA if project in theta_text else FIXED
        check_tex(base / project / "main.tex", text)

    fp1 = fixed_text["Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v6"]
    require("nested structures after\nexplicit inclusion maps" in fp1, "FP I nesting guard missing")

    fp2 = fixed_text["Fixed_Points_II__Fixed_Points_in_a_10D_Modal_Model_v3"]
    require("Current q79 carrier" in fp2, "FP II q79 carrier guard missing")
    require("not globally ordered sheets" in fp2, "FP II direct-lane statement missing")
    require("rank labels alone do not do so" in fp2, "FP II nesting premise guard missing")
    require("auxiliary\nLens--Nil model" in fp2, "FP II auxiliary Lens--Nil status missing")
    require("not identify\n$L(3,1)\\times\\Nilthree$" in fp2, "FP II topology distinction missing")
    require("S^1_{\\mathrm{cen}}\\times T_1^2\\times T_2^2\\times T_3^2" not in fp2, "FP II seven-dimensional example returned")

    fp3 = fixed_text["Fixed_Points_III__Disturbance___Damping_Balance_and_Stability_v4"]
    require("rank labels alone do not establish nesting" in fp3, "FP III nesting guard missing")

    fp6 = fixed_text["Fixed_Points_VI__Formal_Synthesis_and_Physical_Interpretations_v4"]
    require("Circle--lens--nil labels" in fp6, "FP VI operator-level CLN guard missing")
    require("not identified with the\nq79/Fu--Yau compactification" in fp6, "FP VI topology distinction missing")
    require("constructed from the nil, lens, and shared-circle data" not in fp6, "FP VI old manifold-like wording returned")

    p1 = theta_text["Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry_v2"]
    require("Sector gauge-kinetic coefficient" in p1, "Theta I weighted coefficient definition missing")
    require("w_a\\,\\langle \\omega_a,\\omega_a\\rangle" in p1, "Theta I gauge-kinetic weight missing")
    require("doing so would make\n$I_a=1$" in p1, "Theta I unit-normalization guard missing")
    require("Auxiliary coefficient ansatz" in p1, "Theta I auxiliary ansatz status missing")
    require("Existence of an auxiliary calibrated" in p1, "Theta I existence tier missing")
    require("\\|\\omega_a\\|_{L^2(B_a)}=1" not in p1, "Theta I contradictory unit norm returned")
    require("B_n|_y \\simeq S^1_{\\mathrm{cen}}" not in p1, "Theta I shared-circle product returned")
    require("= \\mathrm{Vol}(\\Sigma_a)" not in p1, "Theta I normalized-norm volume identity returned")

    p2 = theta_text["Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps_v2"]
    require("not asserted to be simultaneous Cartesian factors" in p2, "Theta II support guard missing")
    require("not the q79\nFu--Yau compactification" in p2, "Theta II topology distinction missing")
    require("with $B_a \\simeq S^1_{\\mathrm{cen}}" not in p2, "Theta II repeated-circle product returned")

    p3 = theta_text["Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization_v2"]
    require("It does not use the\nseven-dimensional product" in p3, "Theta III seven-dimensional rejection missing")
    require("identification\nwith the selected q79/Fu--Yau compactification" in p3, "Theta III topology distinction missing")
    require("w_a^{(0)}\\langle" in p3, "Theta III weighted overlap missing")

    p4 = theta_text["Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale_v2"]
    require("X_{\\mathrm{aux}}" in p4, "Theta IV auxiliary space missing")
    require("required identification $X_{\\mathrm{int}}=X_{\\mathrm{aux}}$ is not established" in p4, "Theta IV physical-volume guard missing")
    require("the internal space is the product" not in p4, "Theta IV old physical-product assertion returned")
    require("selected q79/Fu--Yau compactification" in p4, "Theta IV q79 distinction missing")

    execution1 = theta_text["Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v3"]
    require("not an identification with the auxiliary" in execution1, "Execution I topology distinction missing")
    require("world-in-world/strain-to-q79" in execution1, "Execution I globalization target missing")

    manifest = (THETA / "REVISION_MANIFEST.md").read_text(encoding="utf-8")
    require("Date: 2026-07-15" in manifest, "Theta manifest date not updated")
    require("Foundational Geometry Reconciliation" in manifest, "Theta manifest reconciliation missing")
    require("forced every overlap to one" in manifest, "Theta normalization repair not documented")

    print(json.dumps({
        "fixed_point_papers_checked": len(fixed_text),
        "theta_execution_papers_checked": len(theta_text),
        "fixed_point_analytic_results": "survive_with_carrier_guards",
        "theta_profile_ratios": "survive_as_calibrated_targets",
        "theta_auxiliary_volume": "not_promoted_to_q79_physical_volume",
        "theta_normalization": "weighted_gauge_kinetic_coefficients",
        "tex_environment_checks": "pass",
    }, indent=2))
    print("Fixed Points/Theta foundational geometry reconciliation audit passed")


if __name__ == "__main__":
    main()
