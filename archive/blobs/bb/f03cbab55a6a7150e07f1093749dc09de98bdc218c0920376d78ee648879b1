r"""Audit the single-Higgs channel projection for the E6 rank-one seed.

The audit checks only the low-energy Higgs doublet embedding:
H_u -> H and H_d -> H^\dagger in the NCG/SM target.  It does not compute
Higgs mass, VEV, triplet decoupling, Yukawa coefficients, kinetic metrics, or
RG matching.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "single_higgs_channel_projection_certificate.json"
DICT_CERT = ROOT.parent / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"

NCG_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\15 Discrete & Spectral & Operator Geometric Theories"
    r"\Modal_Triplet_Theory__From_MTT_to_Noncommutative_Geometry_v3.md"
)
WORLD_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\10 ProtoSpinor"
    r"\World_in_World_Genesis__A_Proto_Geometric_Origin_of_Time__Gravity__Matter__and_Quantization_in_Modal_Triplet_Theory_v4.md"
)
CLOSURE_STRAIN_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\10 ProtoSpinor\Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


Y = {
    "Q": Fraction(1, 6),
    "u^c": Fraction(-2, 3),
    "d^c": Fraction(1, 3),
    "L": Fraction(-1, 2),
    "e^c": Fraction(1, 1),
    "N^c": Fraction(0, 1),
    "H": Fraction(1, 2),
    "H^dagger": Fraction(-1, 2),
}

CHANNELS = {
    "up": ("Q", "u^c", "H"),
    "down": ("Q", "d^c", "H^dagger"),
    "charged_lepton": ("L", "e^c", "H^dagger"),
    "dirac_neutrino": ("L", "N^c", "H"),
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def hypercharge_sum(channel: tuple[str, ...]) -> Fraction:
    return sum((Y[field] for field in channel), Fraction(0, 1))


def main() -> None:
    ncg = read(NCG_SOURCE)
    world = read(WORLD_SOURCE)
    closure = read(CLOSURE_STRAIN_SOURCE)
    paper = read(ROOT / "Single_Higgs_Channel_Projection_for_E6_Rank_One_Seed_v1.md")
    cert = load_json(CERT)
    dict_cert = load_json(DICT_CERT)

    hyper_sums = {name: hypercharge_sum(channel) for name, channel in CHANNELS.items()}
    projection = cert.get("higgs_doublet_embedding", {})

    gates = [
        Gate(
            "E6-to-SM dictionary input",
            "FORMULATED"
            if dict_cert.get("status") == "REPRESENTATION_DICTIONARY_CLOSED_HIGGS_SELECTION_OPEN"
            else "FAIL",
            str(dict_cert.get("status")),
        ),
        Gate(
            "NCG Higgs finite connection",
            "PASS" if contains_all(ncg, ["finite connection", "Higgs", "D_F", "Yukawa matrices"]) else "FAIL",
            "NCG target supplies the SM Higgs/Yukawa finite geometry",
        ),
        Gate(
            "World-origin no-second-Higgs source",
            "PASS" if contains_all(world, ["no second Higgs", "at most one", "Higgs-like radial"]) else "FAIL",
            "connected-domain alignment uniqueness is present",
        ),
        Gate(
            "Closure-strain uniqueness source",
            "PASS" if contains_all(closure, ["no second Higgs", "at most one", "radial alignment"]) else "FAIL",
            "closure-strain source repeats the uniqueness constraint",
        ),
        Gate(
            "Projection H_u",
            "PASS" if projection.get("H_u") == "H" else "FAIL",
            "up and Dirac-neutrino channels use H",
        ),
        Gate(
            "Projection H_d",
            "PASS" if projection.get("H_d") == "H^dagger" else "FAIL",
            "down and charged-lepton channels use H^dagger",
        ),
        Gate(
            "Single physical doublet",
            "PASS" if projection.get("physical_doublet") == "H" and projection.get("hypercharge") == "+1/2" else "FAIL",
            "one SM Higgs doublet is selected at low energy",
        ),
        Gate(
            "SM hypercharge neutrality",
            "PASS" if all(value == 0 for value in hyper_sums.values()) else "FAIL",
            str({name: str(value) for name, value in hyper_sums.items()}),
        ),
        Gate(
            "Projection paper",
            "PASS" if contains_all(paper, ["H_u  -> H", "H_d  -> H^\\dagger", "Q d^c H^\\dagger"]) else "FAIL",
            "projection rule is recorded",
        ),
        Gate(
            "Projection certificate",
            "FORMULATED" if cert.get("status") == "SINGLE_HIGGS_CHANNEL_PROJECTION_FORMULATED_TRIPLET_DECOUPLING_OPEN" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "Triplet decoupling",
            "OPEN",
            "high-scale color-triplet projection/decoupling remains open",
        ),
        Gate(
            "Coefficient selection",
            "OPEN",
            "weights, q79 restrictions, kinetic metrics, and RG matching remain open",
        ),
    ]

    print("Single-Higgs channel projection audit")
    print("=====================================")
    print()
    print(f"hypercharge_sums={dict((name, str(value)) for name, value in hyper_sums.items())}")
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
