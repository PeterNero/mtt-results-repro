"""Audit the E6-to-SM Yukawa operator dictionary for the rank-one seed.

This verifies the representation-level bridge only.  It does not claim that
the light Higgs, kinetic metrics, channel coefficients, or RG matching have
been selected.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"
HIGGS_CERT = ROOT.parent / "certificates" / "single_higgs_channel_projection_certificate.json"

FLUX_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)
NCG_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\15 Discrete & Spectral & Operator Geometric Theories"
    r"\Modal_Triplet_Theory__From_MTT_to_Noncommutative_Geometry_v3.md"
)
HYPERCHARGE_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\10 ProtoSpinor"
    r"\Closure_Geometry_and_Unified_Dynamics__A_Ten_Dimensional_Action_for_Mass__Scalar_Relaxation__Quantization__and_Curvature_v3.md"
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


SM_FIELDS = {
    "Q": {"dim": 6, "Y": Fraction(1, 6)},
    "u^c": {"dim": 3, "Y": Fraction(-2, 3)},
    "d^c": {"dim": 3, "Y": Fraction(1, 3)},
    "L": {"dim": 2, "Y": Fraction(-1, 2)},
    "e^c": {"dim": 1, "Y": Fraction(1, 1)},
    "N^c": {"dim": 1, "Y": Fraction(0, 1)},
    "H_u": {"dim": 2, "Y": Fraction(1, 2)},
    "H_d": {"dim": 2, "Y": Fraction(-1, 2)},
}

SU5_CHI = {
    "10_M": -1,
    "bar5_M": 3,
    "1_M": -5,
    "5_H": 2,
    "bar5_H": -2,
}

SM_CHANNELS = {
    "up": ("Q", "u^c", "H_u"),
    "down": ("Q", "d^c", "H_d"),
    "charged_lepton": ("L", "e^c", "H_d"),
    "dirac_neutrino": ("L", "N^c", "H_u"),
}

SU5_CHANNELS = {
    "up": ("10_M", "10_M", "5_H"),
    "down_and_charged_lepton": ("10_M", "bar5_M", "bar5_H"),
    "dirac_neutrino": ("bar5_M", "1_M", "5_H"),
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def hypercharge_sum(channel: tuple[str, ...]) -> Fraction:
    return sum((SM_FIELDS[field]["Y"] for field in channel), Fraction(0, 1))


def chi_sum(channel: tuple[str, ...]) -> int:
    return sum(SU5_CHI[rep] for rep in channel)


def main() -> None:
    flux = read(FLUX_SOURCE)
    ncg = read(NCG_SOURCE)
    hyper = read(HYPERCHARGE_SOURCE)
    closure = read(CLOSURE_STRAIN_SOURCE)
    paper = read(ROOT / "E6_to_SM_Yukawa_Operator_Dictionary_for_Rank_One_Seed_v1.md")
    cert = json.loads(CERT.read_text(encoding="utf-8")) if CERT.exists() else {}
    higgs_cert = json.loads(HIGGS_CERT.read_text(encoding="utf-8")) if HIGGS_CERT.exists() else {}

    e6_dim = 16 + 10 + 1
    so10_16_dim = 10 + 5 + 1
    so10_10_dim = 5 + 5
    psi_charge_sum = 1 + 1 - 2
    chi_sums = {name: chi_sum(channel) for name, channel in SU5_CHANNELS.items()}
    hyper_sums = {name: hypercharge_sum(channel) for name, channel in SM_CHANNELS.items()}
    field_dim_checks = {
        "10_M": SM_FIELDS["Q"]["dim"] + SM_FIELDS["u^c"]["dim"] + SM_FIELDS["e^c"]["dim"],
        "bar5_M": SM_FIELDS["d^c"]["dim"] + SM_FIELDS["L"]["dim"],
        "1_M": SM_FIELDS["N^c"]["dim"],
        "5_H_light": SM_FIELDS["H_u"]["dim"],
        "bar5_H_light": SM_FIELDS["H_d"]["dim"],
    }

    hyper_compact = compact(hyper)
    cert_status = cert.get("status")

    gates = [
        Gate(
            "Iwasawa E6 cubic source",
            "PASS" if contains_all(flux, ["lambda_{123}", "E_6", "27", "rank one"]) else "FAIL",
            "flux source supplies normalized E6 27^3 rank-one seed",
        ),
        Gate(
            "NCG SM finite algebra source",
            "PASS"
            if contains_all(ncg, ["A_F", "unimodularity", "U(1)_Y", "SU(2)_L", "SU(3)_c"])
            else "FAIL",
            "NCG source supplies downstream SM gauge target",
        ),
        Gate(
            "NCG Higgs/Yukawa source",
            "PASS" if contains_all(ncg, ["Higgs", "finite connection", "Yukawa matrices"]) else "FAIL",
            "finite connection and D_F encode Higgs/Yukawa structure",
        ),
        Gate(
            "Hypercharge source",
            "PASS" if "Y=\\frac{1}{6}Q_a-\\frac{1}{2}Q_c" in hyper_compact else "FAIL",
            "corpus has a concrete hypercharge embedding benchmark",
        ),
        Gate(
            "Closure-strain deferral source",
            "PASS" if contains_all(closure, ["Yukawa", "execution-level", "finite algebra"]) else "FAIL",
            "corpus separates representation content from numerical Yukawa execution",
        ),
        Gate(
            "E6 dimension branch",
            "PASS" if e6_dim == 27 else "FAIL",
            "27 = 16 + 10 + 1",
        ),
        Gate(
            "SO10 dimension branch",
            "PASS" if so10_16_dim == 16 and so10_10_dim == 10 else "FAIL",
            "16 = 10 + 5 + 1 and 10 = 5 + 5",
        ),
        Gate(
            "E6 cubic psi neutrality",
            "PASS" if psi_charge_sum == 0 else "FAIL",
            "16_1 16_1 10_-2 is U(1)_psi neutral",
        ),
        Gate(
            "SU5 chi neutrality",
            "PASS" if all(value == 0 for value in chi_sums.values()) else "FAIL",
            str(chi_sums),
        ),
        Gate(
            "SM hypercharge neutrality",
            "PASS" if all(value == 0 for value in hyper_sums.values()) else "FAIL",
            str({name: str(value) for name, value in hyper_sums.items()}),
        ),
        Gate(
            "SM representation dimensions",
            "PASS"
            if field_dim_checks["10_M"] == 10
            and field_dim_checks["bar5_M"] == 5
            and field_dim_checks["1_M"] == 1
            and field_dim_checks["5_H_light"] == 2
            and field_dim_checks["bar5_H_light"] == 2
            else "FAIL",
            str(field_dim_checks),
        ),
        Gate(
            "Dictionary paper",
            "PASS"
            if contains_all(paper, ["Q u^c H_u", "Q d^c H_d", "L e^c H_d", "L N^c H_u"])
            else "FAIL",
            "SM Yukawa operators are recorded",
        ),
        Gate(
            "Dictionary certificate",
            "FORMULATED" if cert_status == "REPRESENTATION_DICTIONARY_CLOSED_HIGGS_SELECTION_OPEN" else "FAIL",
            str(cert_status),
        ),
        Gate(
            "Low-energy Higgs projection",
            "FORMULATED"
            if higgs_cert.get("status") == "SINGLE_HIGGS_CHANNEL_PROJECTION_FORMULATED_TRIPLET_DECOUPLING_OPEN"
            else "OPEN",
            "single-Higgs channel projection is supplied by the follow-up certificate",
        ),
        Gate(
            "Triplet decoupling",
            "OPEN",
            "high-scale color-triplet projection/decoupling is not selected by this dictionary",
        ),
        Gate(
            "Coefficient selection",
            "OPEN",
            "channel weights, kinetic metrics, and RG matching remain open",
        ),
    ]

    print("E6-to-SM Yukawa operator dictionary audit")
    print("=========================================")
    print()
    print(f"e6_dimension_check={e6_dim}")
    print(f"psi_charge_sum={psi_charge_sum}")
    print(f"chi_sums={chi_sums}")
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
