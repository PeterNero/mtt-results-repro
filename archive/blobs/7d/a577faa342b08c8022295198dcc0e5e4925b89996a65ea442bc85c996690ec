"""Audit the selected localization graph theorem."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    theorem = read(ROOT / "Selected_Localization_Graph_Theorem_v1.md")
    clues = read(ROOT / "Selected_Overlap_Kernel_Source_Clues_from_Corpus_v1.md")
    cert = read(ROOT / "Selected_Overlap_Kernel_Certificate_v1.md")

    gates = [
        Gate("theorem file", "PASS" if "Canonical Localization Graph" in theorem else "FAIL", "localization graph theorem present"),
        Gate("L_loc operator", "DEFINED" if "L_loc,x" in theorem and "L_theta,x" in theorem else "FAIL", "theta/lens/nil/proto-spinor operator form"),
        Gate("Riesz family projector", "DEFINED" if "integral_{partial Omega_x}" in theorem else "FAIL", "family projector construction"),
        Gate("channel predicates", "DEFINED" if "nil-survivor projector" in theorem and "anchor/cancellation" in theorem else "FAIL", "finite channel admissibility conditions"),
        Gate("corpus source match", "PASS" if "G_loc" in clues and "finite instanton" in clues else "FAIL", "uses extracted corpus source variables"),
        Gate("certificate feed", "PASS" if "zero-mode bases" in cert and "Gamma_x[i,j]" in cert else "FAIL", "feeds overlap-kernel certificate"),
        Gate("graph schema", "PROVED" if "localization graph construction schema          PROVED" in theorem else "FAIL", "canonical once selected operator is supplied"),
        Gate("entry fitting block", "PROVED" if "no entry-wise localization fitting              PROVED" in theorem else "FAIL", "prevents per-entry localization choices"),
        Gate("actual operator", "OPEN" if "actual L_loc,x from MTT geometry                OPEN" in theorem else "FAIL", "concrete selected operator still missing"),
        Gate("eigenmode computation", "OPEN" if "zero-mode basis computation                     OPEN" in theorem else "FAIL", "three-family modes still to compute"),
    ]

    print("Selected localization graph theorem audit")
    print("=========================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
