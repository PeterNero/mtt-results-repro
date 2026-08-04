"""Audit the correction-channel ledger for lifting the rank-one Yukawa seed."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "rank_one_lift_correction_channel_ledger_certificate.json"
SEED_CERT = ROOT.parent / "certificates" / "iwasawa_rank_one_yukawa_seed_certificate.json"
THETA_CERT = ROOT.parent / "certificates" / "theta_flavor_kernel_skeleton_certificate.json"
FLUX_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)
PROTO_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\10 ProtoSpinor\Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md"
)
QFT_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\7 Quantum Field Theory\Modal_Triplet_Theory__Quantum_Amplitudes_from_Modal_Geometry_v2.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    flux = read(FLUX_SOURCE)
    proto = read(PROTO_SOURCE)
    qft = read(QFT_SOURCE)
    execution = read(ROOT / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md")
    ledger = read(ROOT / "Rank_One_Lift_Correction_Channel_Ledger_for_No_Proxy_Flavor_v1.md")
    terminal = read(ROOT / "Terminal_Closure_Certificate_and_Remaining_Proof_Obligations_v1.md")
    cert = load_json(CERT)
    seed_cert = load_json(SEED_CERT)
    theta_cert = load_json(THETA_CERT)

    channels = cert.get("channels", {})
    closed_count = sum(1 for channel in channels.values() if channel.get("source_status") in {"FORMULATED", "CLOSED_SEED"})

    gates = [
        Gate(
            "Rank-one seed",
            "CLOSED" if seed_cert.get("tree_level_seed", {}).get("rank") == 1 else "FAIL",
            "Iwasawa seed certificate supplies rank(Y_tree)=1",
        ),
        Gate(
            "Theta/q79 environment",
            "CLOSED" if theta_cert.get("cp_character", {}).get("q_mod_448") == 79 else "FAIL",
            "Theta scaffold and q79 character are fixed",
        ),
        Gate(
            "C1 alpha-prime corrections",
            "FORMULATED" if contains_all(flux, ["Higher-order", "alpha", "corrections"]) or contains_all(flux, ["Higher‑order", "alpha", "corrections"]) else "FAIL",
            "flux source identifies higher-order alpha-prime corrections",
        ),
        Gate(
            "C2 nonperturbative corrections",
            "FORMULATED" if "nonperturbative corrections" in flux else "FAIL",
            "Iwasawa rank-one seed source names nonperturbative corrections",
        ),
        Gate(
            "C3 flux-quantized Lens-Nil",
            "RETIRED-FORMULATED" if contains_all(flux, ["f,h", "fix the ratio", "Flux quantization holds"]) else "FAIL",
            "support clue retained; numeric coefficient source retired until Lens-Nil repair",
        ),
        Gate(
            "C4 non-invariant modes",
            "OPEN-FORMULATED" if "non-invariant" in flux and "beyond our scope" in flux else "FAIL",
            "source explicitly leaves full non-invariant moduli analysis open",
        ),
        Gate(
            "C5 kinetic metrics",
            "FORMULATED" if contains_all(qft, ["canonically normalized gauge, fermion, and scalar kinetic terms", "No further"]) else "FAIL",
            "QFT source fixes canonical-normalization principle",
        ),
        Gate(
            "C6 q79 holonomy",
            "CLOSED" if "selected exact/charge MTT branch proves q=79 mod 448" in terminal else "FAIL",
            "finite CP character is not a tunable phase",
        ),
        Gate(
            "C7 closure-strain ordering",
            "FORMULATED" if contains_all(proto, ["D_q(g,h)", "D_\\ell(g,h)", "D_\\nu(g,h)", "PMNS", "CKM"]) else "FAIL",
            "ProtoSpinor source gives structural mixing hierarchy",
        ),
        Gate(
            "Proxy benchmark knobs detected",
            "DETECTED" if contains_all(execution, ["charm lift factor", "instanton corrections", "single holonomy phase"]) else "FAIL",
            "benchmark local inputs must be replaced by selected channels",
        ),
        Gate(
            "Ledger certificate",
            "LEDGER_CLOSED" if cert.get("status") == "CHANNEL_LEDGER_FORMULATED_COEFFICIENTS_OPEN" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "Channel source count",
            "PASS" if closed_count >= 6 else "FAIL",
            f"{closed_count} channel source entries formulated/closed",
        ),
        Gate(
            "Coefficient evaluation",
            "OPEN",
            "actions, prefactors, kinetic matrices, and corrected overlaps are not computed",
        ),
        Gate(
            "Full mass closure",
            "OPEN",
            "full Yukawa singular values and CKM/PMNS angles remain future output",
        ),
    ]

    print("Rank-one lift correction-channel ledger audit")
    print("=============================================")
    print()
    print(f"formulated_channel_sources={closed_count}")
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
