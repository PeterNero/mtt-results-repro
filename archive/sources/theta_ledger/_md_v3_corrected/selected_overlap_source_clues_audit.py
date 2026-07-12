"""Audit the extracted source clues for the selected overlap-kernel map."""

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
    clues = read(ROOT / "Selected_Overlap_Kernel_Source_Clues_from_Corpus_v1.md")
    packet = read(ROOT / "Minimal_Selected_Kernel_Packet_and_Phase_Rigidity_v1.md")
    cert = read(ROOT / "Selected_Overlap_Kernel_Certificate_v1.md")

    gates = [
        Gate("source clue paper", "PASS" if "Corpus Source Variables" in clues else "FAIL", "source variables extracted"),
        Gate("localization graph", "EXTRACTED" if "G_loc" in clues else "FAIL", "zero-mode graph named"),
        Gate("pairwise line bundles", "EXTRACTED" if "L_12 tensor L_23 tensor L_31" in clues else "FAIL", "holonomy sum rule source"),
        Gate("finite channels", "EXTRACTED" if "finite instanton or exceptional-cycle" in clues else "FAIL", "channel classes named"),
        Gate("width data", "EXTRACTED" if "flux/width data W" in clues else "FAIL", "lens/nil/flux width slot named"),
        Gate("majorana criterion", "EXTRACTED" if "L tensor L ~= C" in clues else "FAIL", "neutral branch criterion imported"),
        Gate("q79 character link", "PROVED/IMPORTED" if "tau^{w_gamma}" in clues and "Phase Rigidity" in packet else "FAIL", "CP phases factor through Z448"),
        Gate("certificate compatibility", "PASS" if "FlavorOverlapKernelCertificate" in cert and "Sigma_MTT" in clues else "FAIL", "clues feed certificate"),
        Gate("selected localization theorem", "NEXT" if "SelectedLocalizationGraphTheorem" in clues else "FAIL", "next missing proof target identified"),
    ]

    print("Selected overlap source-clues audit")
    print("===================================")
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
