"""Audit the projective twist cocycle and corpus source hunt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "iwasawa_projective_twist_source_hunt_certificate.json"
PROJECTIVE_CERT = CERT_DIR / "iwasawa_projective_magnetic_carrier_certificate.json"
VALIDATOR_CERT = CERT_DIR / "iwasawa_projective_rhoE_mesh_validator_certificate.json"
Z7_CERT = CERT_DIR / "z7_fuyau_mukai_charge_sector_certificate.json"
PROMOTION_CERT = CERT_DIR / "iwasawa_selected_source_promotion_gate_certificate.json"
PAPER = ROOT / "Iwasawa_Projective_Twist_Source_Hunt_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_projective_twist_cocycle.py"

STROMINGER = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)
FLUX = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)
SELECTION = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
)
TWISTED_Z64 = ROOT / "Twisted_Equivariant_Central_Circle_Z64_CP_Sector_Candidate_v1.md"
MUKAI_DESCENT = ROOT / "Mukai_Fixed_Sector_Descent_to_Order_448_CP_v1.md"


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


def run_cocycle_script() -> dict[str, Any]:
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
    projective_cert = load_json(PROJECTIVE_CERT)
    validator_cert = load_json(VALIDATOR_CERT)
    z7_cert = load_json(Z7_CERT)
    promotion_cert = load_json(PROMOTION_CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    strominger = read(STROMINGER)
    flux = read(FLUX)
    selection = read(SELECTION)
    twisted_z64 = read(TWISTED_Z64)
    mukai_descent = read(MUKAI_DESCENT)
    cocycle_report = run_cocycle_script()

    found_alignment = cert.get("found_alignment", {})
    missing = cert.get("missing_for_projective_carrier_selection", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    arithmetic = cert.get("cocycle_arithmetic", {})

    gates = [
        Gate(
            "certificate status",
            "OPEN"
            if cert.get("status")
            == "IWASAWA_PROJECTIVE_TWIST_SOURCE_HUNT_ALIGNED_SOURCE_MAP_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "projective dependencies",
            "PASS"
            if projective_cert.get("verdict", {}).get(
                "projective_route_is_live_but_requires_new_selected_twist_data"
            )
            is True
            and validator_cert.get("verdict", {}).get("projective_validator_ready")
            is True
            else "FAIL",
            "projective carrier plus validator",
        ),
        Gate(
            "closed charge branch intact",
            "PASS"
            if z7_cert.get("status") == "CLOSED_CHARGE_SECTOR"
            and z7_cert.get("geometry", {}).get("green_schwarz_bianchi_identity_verified")
            is True
            else "FAIL",
            str(z7_cert.get("geometry", {})),
        ),
        Gate(
            "cocycle script present",
            "PASS"
            if contains_all_ci(
                script_text,
                [
                    "c((a,b),(a',b')) = -a' b mod 3",
                    "finite Heisenberg group H_3",
                    "ordinary_bundle_coboundary_possible",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "cocycle arithmetic",
            "PASS"
            if cocycle_report.get("cocycle_identity_violations") == 0
            and cocycle_report.get("commutator_rank_over_F3") == arithmetic.get(
                "commutator_rank_over_F3"
            )
            and cocycle_report.get("central_extension", {}).get("order")
            == arithmetic.get("finite_heisenberg_extension_order")
            and cocycle_report.get("central_extension", {}).get("center_order")
            == arithmetic.get("center_order")
            and cocycle_report.get("interpretation", {}).get(
                "ordinary_bundle_coboundary_possible"
            )
            is False
            else "FAIL",
            str(cocycle_report),
        ),
        Gate(
            "strominger gerbe source",
            "PASS"
            if contains_all_ci(
                strominger,
                [
                    "deligne 2-gerbe",
                    "widehat{H}",
                    "Chern--Simons",
                    "fixed differential cohomology class",
                    "Bianchi",
                ],
            )
            else "FAIL",
            str(STROMINGER),
        ),
        Gate(
            "flux gerbe quantization source",
            "PASS"
            if contains_all_ci(
                flux,
                [
                    "Flux quantization and the heterotic gerbe",
                    "field gerbe is globally well-defined",
                    "Bianchi identity is solved componentwise",
                    "support only on",
                ],
            )
            else "FAIL",
            str(FLUX),
        ),
        Gate(
            "selection global gate source",
            "PASS"
            if contains_all_ci(
                selection,
                [
                    "Global issues: Bianchi identity and Freed--Witten",
                    "gerbe curvature",
                    "Freed--Witten consistency",
                    "Fu--Yau class",
                ],
            )
            else "FAIL",
            str(SELECTION),
        ),
        Gate(
            "twisted projector guardrail",
            "PASS"
            if contains_all_ci(
                twisted_z64,
                [
                    "Twisted Bundle Carrier",
                    "spectral projector",
                    "selected character sector",
                ],
            )
            else "FAIL",
            str(TWISTED_Z64),
        ),
        Gate(
            "ambient family Z3 clue",
            "PASS"
            if contains_all_ci(
                mukai_descent,
                [
                    "family factor",
                    "SNF=[1344]",
                    "family kernel",
                ],
            )
            else "FAIL",
            str(MUKAI_DESCENT),
        ),
        Gate(
            "alignment recorded",
            "PASS" if all(found_alignment.values()) else "FAIL",
            str(found_alignment),
        ),
        Gate(
            "missing selected source map",
            "OPEN" if all(missing.values()) else "FAIL",
            str(missing),
        ),
        Gate(
            "promotion gate dependency",
            "PASS"
            if promotion_cert.get("verdict", {}).get("promotion_gate_ready") is True
            or promotion_cert.get("status") == "IWASAWA_SELECTED_SOURCE_PROMOTION_GATE_FORMULATED"
            else "FAIL",
            str(promotion_cert.get("status")),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("projective_route_corpus_aligned") is True
            and verdict.get("selected_projective_twist_source_found") is False
            and verdict.get("does_not_disturb_closed_q79_branch") is True
            and "twisted-source promotion gate" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records hunt",
            "PASS"
            if contains_all_ci(
                paper,
                [
                    "finite Heisenberg central extension",
                    "selected map",
                    "not yet selected",
                    "twisted-source promotion gate",
                    "closed q79 branch remains untouched",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa projective twist source-hunt audit")
    print("==========================================")
    print()
    print(f"cocycle_nontrivial={cocycle_report.get('cocycle_nontrivial')}")
    print(f"commutator_rank_over_F3={cocycle_report.get('commutator_rank_over_F3')}")
    print(f"selected_projective_twist_source_found={verdict.get('selected_projective_twist_source_found')}")
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
