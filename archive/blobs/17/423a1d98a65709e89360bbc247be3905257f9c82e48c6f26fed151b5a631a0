"""Audit finite channel sets for the rank-one lift."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "finite_channel_sets_certificate.json"
LEDGER_CERT = ROOT.parent / "certificates" / "rank_one_lift_correction_channel_ledger_certificate.json"
DICT_CERT = ROOT.parent / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"
HIGGS_CERT = ROOT.parent / "certificates" / "single_higgs_channel_projection_certificate.json"
Q79_RESTRICTION_CERT = ROOT.parent / "certificates" / "q79_channel_restriction_certificate.json"

EXPECTED_SOURCES = {
    "C0_tree_rank_one_seed",
    "C1_alpha_prime_curvature",
    "C2_nonperturbative_instanton",
    "C3_flux_quantized_lens_nil",
    "C4_retained_non_invariant_modes",
    "C6_q79_holonomy_insertion",
    "C7_closure_strain_basin_deformation",
}

EXPECTED_OPERATORS = {
    "Gamma_u": "Q u^c H",
    "Gamma_d": "Q d^c H^dagger",
    "Gamma_e": "L e^c H^dagger",
    "Gamma_nuD": "L N^c H",
}


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def channel_sources(channels: list[dict]) -> set[str]:
    return {channel.get("source_class", "") for channel in channels}


def main() -> None:
    cert = load_json(CERT)
    ledger_cert = load_json(LEDGER_CERT)
    dict_cert = load_json(DICT_CERT)
    higgs_cert = load_json(HIGGS_CERT)
    q79_restriction_cert = load_json(Q79_RESTRICTION_CERT)
    paper = read(ROOT / "Finite_Channel_Sets_for_Rank_One_Lift_v1.md")

    sets = cert.get("finite_channel_sets", {})
    set_lengths = {name: len(sets.get(name, [])) for name in EXPECTED_OPERATORS}
    source_checks = {
        name: channel_sources(sets.get(name, [])) == EXPECTED_SOURCES
        for name in EXPECTED_OPERATORS
    }
    operator_checks = {
        name: all(channel.get("operator") == expected for channel in sets.get(name, []))
        for name, expected in EXPECTED_OPERATORS.items()
    }
    unique_id_checks = {
        name: len({channel.get("id") for channel in sets.get(name, [])}) == len(sets.get(name, []))
        for name in EXPECTED_OPERATORS
    }

    excluded = cert.get("excluded_from_gamma", {})

    gates = [
        Gate(
            "Ledger input",
            "FORMULATED" if ledger_cert.get("status") == "CHANNEL_LEDGER_FORMULATED_COEFFICIENTS_OPEN" else "FAIL",
            str(ledger_cert.get("status")),
        ),
        Gate(
            "E6/SM dictionary input",
            "FORMULATED" if dict_cert.get("status") == "REPRESENTATION_DICTIONARY_CLOSED_HIGGS_SELECTION_OPEN" else "FAIL",
            str(dict_cert.get("status")),
        ),
        Gate(
            "Single-Higgs input",
            "FORMULATED"
            if higgs_cert.get("status") == "SINGLE_HIGGS_CHANNEL_PROJECTION_FORMULATED_TRIPLET_DECOUPLING_OPEN"
            else "FAIL",
            str(higgs_cert.get("status")),
        ),
        Gate(
            "Certificate status",
            "FORMULATED" if cert.get("status") == "FINITE_CHANNEL_SETS_FORMULATED_WEIGHTS_OPEN" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "Gamma set names",
            "PASS" if set(sets.keys()) == set(EXPECTED_OPERATORS.keys()) else "FAIL",
            ", ".join(sorted(sets.keys())),
        ),
        Gate(
            "Gamma set finiteness",
            "PASS" if all(length == 7 for length in set_lengths.values()) else "FAIL",
            str(set_lengths),
        ),
        Gate(
            "Source classes",
            "PASS" if all(source_checks.values()) else "FAIL",
            str(source_checks),
        ),
        Gate(
            "SM operator labels",
            "PASS" if all(operator_checks.values()) else "FAIL",
            str(operator_checks),
        ),
        Gate(
            "Unique channel ids",
            "PASS" if all(unique_id_checks.values()) else "FAIL",
            str(unique_id_checks),
        ),
        Gate(
            "Kinetic metrics excluded",
            "PASS" if excluded.get("C5_kinetic_metrics") == "normalization_not_overlap_channel" else "FAIL",
            "C5 remains a separate canonical-normalization input",
        ),
        Gate(
            "Weights remain open",
            "OPEN" if cert.get("open", {}).get("channel_weights") is True else "FAIL",
            "A_gamma and S_gamma are not computed",
        ),
        Gate(
            "q79 restriction follow-up",
            "FORMULATED"
            if q79_restriction_cert.get("status") == "Q79_CHANNEL_RESTRICTION_FORMULATED_WEIGHTS_OPEN"
            and cert.get("open", {}).get("q79_channel_restriction") is False
            else "OPEN",
            "C6 q79/conjugate support is supplied by follow-up certificate",
        ),
        Gate(
            "Paper records theorem",
            "PASS" if "Finite Sets" in paper and "Gamma_u" in paper and "Gamma_nuD" in paper else "FAIL",
            "finite channel-set theorem is written",
        ),
    ]

    print("Finite channel sets audit")
    print("=========================")
    print()
    print(f"set_lengths={set_lengths}")
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
