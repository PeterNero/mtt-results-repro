"""Audit the Iwasawa flat-torsion gerbe selection-gap theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_flat_torsion_selection_gap_certificate.json"
GERBE_CERT = REPO / "certificates" / "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json"
SOURCE_HUNT = REPO / "certificates" / "iwasawa_projective_twist_source_hunt_certificate.json"
Z7_CERT = REPO / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json"
PAPER = ROOT / "Iwasawa_Flat_Torsion_Gerbe_Selection_Gap_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_flat_torsion_selection_gap.py"

STROMINGER = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)
SELECTION = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all_ci(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return all(needle.lower() in lowered for needle in needles)


def run_script() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def main() -> None:
    cert = load_json(CERT)
    gerbe = load_json(GERBE_CERT)
    source_hunt = load_json(SOURCE_HUNT)
    z7 = load_json(Z7_CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    strominger = read(STROMINGER)
    selection = read(SELECTION)
    report = run_script()

    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    visibility = report.get("current_selection_functional_visibility", {})
    gap = report.get("selection_gap", {})
    labels = {entry.get("torsion_label"): entry for entry in report.get("torsion_labels", [])}

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "IWASAWA_FLAT_TORSION_GERBE_SELECTION_GAP_PROVED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script formula",
            "PASS"
            if contains_all_ci(
                script_text,
                [
                    "flat torsion changes holonomy but not curvature",
                    "B_",
                    "can_select_between_Z3_flat_labels_from_current_curvature_data",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "finite gerbe dependency",
            "PASS"
            if gerbe.get("verdict", {}).get("candidate_holonomy_map_closed") is True
            and gerbe.get("verdict", {}).get("selection_remains_open") is True
            else "FAIL",
            str(gerbe.get("verdict", {})),
        ),
        Gate(
            "source hunt dependency",
            "PASS"
            if source_hunt.get("verdict", {}).get("projective_route_corpus_aligned") is True
            and source_hunt.get("verdict", {}).get("selected_projective_twist_source_found")
            is False
            else "FAIL",
            str(source_hunt.get("verdict", {})),
        ),
        Gate(
            "closed Fu-Yau curvature sector",
            "PASS"
            if z7.get("status") == "CLOSED_CHARGE_SECTOR"
            and z7.get("geometry", {}).get("green_schwarz_bianchi_identity_verified") is True
            else "FAIL",
            str(z7.get("geometry", {})),
        ),
        Gate(
            "corpus Hhat visibility",
            "PASS"
            if contains_all_ci(
                strominger,
                [
                    "field is a Deligne 2-gerbe",
                    "fixed differential cohomology class",
                    "depends on",
                    "only via",
                    "large gauge transformations",
                ],
            )
            else "FAIL",
            str(STROMINGER),
        ),
        Gate(
            "corpus global gate",
            "PASS"
            if contains_all_ci(
                selection,
                [
                    "Global issues: Bianchi identity and Freed--Witten",
                    "integral cohomology class",
                    "topological sector",
                    "Bianchi identity is solved componentwise",
                ],
            )
            else "FAIL",
            str(SELECTION),
        ),
        Gate(
            "all flat labels",
            "PASS"
            if report.get("all_flat_torsion_labels_have_zero_discrete_bianchi") is True
            and report.get("all_flat_torsion_labels_leave_Hhat_curvature_unchanged") is True
            and set(labels) == {0, 1, 2}
            else "FAIL",
            str(report),
        ),
        Gate(
            "qutrit labels",
            "PASS"
            if labels.get(0, {}).get("qutrit_projective_cocycle_role") == "trivial"
            and labels.get(1, {}).get("qutrit_projective_cocycle_role")
            == "matches_current_zeta_3^2_orientation"
            and labels.get(2, {}).get("qutrit_projective_cocycle_role")
            == "matches_conjugate_zeta_3^1_orientation"
            else "FAIL",
            str(labels),
        ),
        Gate(
            "selection invisibility",
            "PASS"
            if visibility.get("sees_Green_Schwarz_curvature_Hhat") is True
            and visibility.get("sees_flat_torsion_holonomy_without_extra_topological_label")
            is False
            and visibility.get("can_select_between_Z3_flat_labels_from_current_curvature_data")
            is False
            and gap.get("selected_torsion_label_supplied_by_current_certificates") is False
            else "FAIL",
            str({"visibility": visibility, "gap": gap}),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("all_flat_torsion_labels_have_zero_discrete_bianchi") is True
            and calc.get("all_flat_torsion_labels_leave_Hhat_curvature_unchanged") is True
            and calc.get("nontrivial_labels_match_qutrit_or_conjugate") is True
            and calc.get("current_curvature_selection_can_choose_Z3_label") is False
            and calc.get("selected_torsion_label_supplied_by_current_certificates") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closed fields",
            "PASS" if all(value is True for value in closed.values()) else "FAIL",
            str(closed),
        ),
        Gate(
            "still open",
            "PASS" if all(value is True for value in still_open.values()) else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("finite_gerbe_arithmetic_ready") is True
            and verdict.get("selected_source_promotion_closed") is False
            and verdict.get("full_closure_blocked_by_flat_torsion_selector") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all_ci(
                paper,
                [
                    "flat torsion changes holonomy",
                    "does not change Hhat",
                    "present curvature functional cannot distinguish",
                    "selected flat differential-cohomology torsion label",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa flat-torsion gerbe selection-gap audit")
    print("==============================================")
    print()
    print(f"torsion_labels={sorted(labels)}")
    print(
        "can_select_between_Z3_flat_labels="
        f"{visibility.get('can_select_between_Z3_flat_labels_from_current_curvature_data')}"
    )
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
