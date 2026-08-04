#!/usr/bin/env python3
"""Verify current-version delta notes across all revised TeX papers."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

GROUPS = {
    "Foundation": TEXPAPERS / "3 Core Foundations" / "revised_tex_vnext",
    "Fixed Points": TEXPAPERS / "4 Fixed Points" / "revised_tex_vnext",
    "ProtoSpinor": TEXPAPERS / "10 ProtoSpinor" / "revised_tex_vnext",
    "Theta/Execution": ROOT / "revised_tex_vnext",
}

EXPECTED_COUNTS = {
    "Foundation": 6,
    "Fixed Points": 6,
    "ProtoSpinor": 5,
    "Theta/Execution": 10,
}

PAPER_SPECIFIC_MARKERS = {
    "Modal_Triplet_Theory__Foundation_v8": "universal q79 flat differential line",
    "The_Projection__Admissibility_Principle__Descent__Recovery__and_Structural_Constraints_v2": "factor-through",
    "Lorentzian_Base_Compatibility_and_Signature_Stability_in_the_MTT_Fixed_Point_Realization_v2": "principal symbol",
    "Baseline_Scales_and_Phenomenological_Consistency_in_Modal_Triplet_Theory_v2": "common parameter witness",
    "Coherent_Kinematics_in_Modal_Triplet_Theory_v2": "hyperbolic",
    "Modal_Triplet_Theory__A_Typed_Relationship_Atlas_v3": "containment checklist",
    "Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v6": "Cea-type Galerkin",
    "Fixed_Points_II__Fixed_Points_in_a_10D_Modal_Model_v3": "strict Lyapunov",
    "Fixed_Points_III__Disturbance___Damping_Balance_and_Stability_v4": "Green--Kubo",
    "Fixed_Points_IV__Curvature__Centroid_Motion__and_Structural_Transitions_on_Bundle_Manifolds_v4": "Karcher",
    "Fixed_Points_V__Curvature_Coupling__Multi_Structure_Dynamics_and_Drivers_v6": "canonical-correlation",
    "Fixed_Points_VI__Formal_Synthesis_and_Physical_Interpretations_v4": "local-mediator",
    "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry_v2": "weighted gauge-kinetic",
    "Theta_Closure_in_Modal_Triplet_Theory_II__Direct_Geometric_Realization_of_Nonabelian_Overlaps_v2": "round-$S^2$/nil",
    "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization_v2": "shared input",
    "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale_v2": "20.07064R_1^3",
    "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle_v2": "non-circularity",
    "Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v3": "Cech--HYM",
    "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v3": "$27\\times27$",
    "Superset_Determinations_in_Modal_Triplet_Theory_v3": "classifies every",
    "Geometry__Light_Relations_in_Modal_Triplet_Theory__MTT__v3": "principal symbols",
    "A_Tiered_Roadmap_for_Calculations_in_Modal_Triplet_Theory__MTT__v3": "12/12",
    "The_Proto_Spinor__Conditional_Spinorial_Closure_and_q79_Interface_v6": "$J_{\\rm FM}^2=-I$",
    "World_in_World_Genesis__Local_Comparison_Geometry_and_Globalization_Program_v5": "$Q_{\\rm WW}",
    "Closure_Strain_Geometry__Local_Normal_Forms_and_Conditional_Matter_Encodings_v7": "finite Reynolds projector",
    "Proto_Spinor_Closure_and_Worldsheet_Encoding_in_Modal_Triplet_Theory_v4": "cubic error",
    "Closure_Geometry_and_a_Regime_Local_Ten_Dimensional_Action_Ansatz_v4": "compact-resolvent",
}

LABELS = (
    "Supersedes.",
    "Reason.",
    "Resolution.",
    "Retained result.",
    "Remaining boundary.",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_note(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    heading = r"\section*{Revision note for this edition}"
    require(text.count(heading) == 1, f"{path}: expected exactly one revision-note heading")
    require(
        text.count(r"\addcontentsline{toc}{section}{Revision note for this edition}") == 1,
        f"{path}: revision note is not added to the table of contents",
    )

    abstract_end = text.find(r"\end{abstract}")
    note_start = text.find(heading)
    first_numbered_section = text.find(r"\section{")
    require(abstract_end >= 0, f"{path}: abstract end missing")
    require(abstract_end < note_start, f"{path}: revision note is not after the abstract")
    require(
        first_numbered_section < 0 or note_start < first_numbered_section,
        f"{path}: revision note is not before the paper body",
    )

    note_end = text.find(r"\end{description}", note_start)
    require(note_end > note_start, f"{path}: revision-note description is unclosed")
    note = text[note_start:note_end]
    for label in LABELS:
        token = rf"\item[{label}]"
        require(note.count(token) == 1, f"{path}: expected one {label} field")

    require("version" in note.lower() or "first edition" in note.lower(), f"{path}: superseded edition is not identified")
    require(len(re.sub(r"\\[A-Za-z@]+|[{}$]", "", note).split()) >= 65, f"{path}: revision note is too terse")
    require(not re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", note), f"{path}: placeholder remains in revision note")

    marker = PAPER_SPECIFIC_MARKERS.get(path.parent.name)
    require(marker is not None, f"{path}: no paper-specific verification marker registered")
    require(marker in note, f"{path}: paper-specific resolution marker absent: {marker}")


def main() -> int:
    all_files: list[Path] = []
    for group, root in GROUPS.items():
        files = sorted(root.rglob("main.tex"))
        require(len(files) == EXPECTED_COUNTS[group], f"{group}: found {len(files)} papers, expected {EXPECTED_COUNTS[group]}")
        all_files.extend(files)

    require(len(all_files) == 27, f"found {len(all_files)} revised papers, expected 27")
    require(len(PAPER_SPECIFIC_MARKERS) == 27, "paper-specific marker ledger is not 27 entries")

    for path in all_files:
        verify_note(path)

    print("PASS: 27/27 revised papers contain one current-version delta note")
    print("PASS: every note identifies superseded edition, reason, resolution, retained result, and remaining boundary")
    print("PASS: every note follows the abstract and contains a paper-specific resolution marker")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
