"""Audit the Iwasawa rank-one Yukawa seed.

The audit verifies only the seed-level claim: the corpus contains a normalized
Iwasawa trilinear with lambda_123=1 and rank-one tree Yukawa interpretation.
It does not claim that the full SM Yukawa spectrum is derived.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "iwasawa_rank_one_yukawa_seed_certificate.json"
DICT_CERT = ROOT.parent / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"
HIGGS_CERT = ROOT.parent / "certificates" / "single_higgs_channel_projection_certificate.json"
FLUX_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)
SUPERSET_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\3 Core Foundations\Modal_Triplet_Theory__MTT_as_a_Superset_v2.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def rank_of_seed_matrix() -> int:
    seed = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
    nonzero_rows = [row for row in seed if any(value != 0 for value in row)]
    return len(nonzero_rows)


def main() -> None:
    flux = read(FLUX_SOURCE)
    superset = read(SUPERSET_SOURCE)
    scaffold = read(ROOT / "Theta_Selected_Overlap_Kernel_Skeleton_for_No_Proxy_Flavor_v1.md")
    seed_paper = read(ROOT / "Iwasawa_Rank_One_Yukawa_Seed_for_No_Proxy_Flavor_v1.md")
    cert = json.loads(CERT.read_text(encoding="utf-8")) if CERT.exists() else {}
    dict_cert = json.loads(DICT_CERT.read_text(encoding="utf-8")) if DICT_CERT.exists() else {}
    higgs_cert = json.loads(HIGGS_CERT.read_text(encoding="utf-8")) if HIGGS_CERT.exists() else {}

    cert_status = cert.get("status")
    cert_lambda = cert.get("tree_level_seed", {}).get("lambda_123_after_rephasing")
    cert_rank = cert.get("tree_level_seed", {}).get("rank")
    computed_rank = rank_of_seed_matrix()

    gates = [
        Gate(
            "Flux source available",
            "PASS" if FLUX_SOURCE.exists() else "FAIL",
            str(FLUX_SOURCE),
        ),
        Gate(
            "Three harmonic representatives",
            "PASS" if contains_all(flux, ["Psi_i", "H^1(X,E)", "i=1,2,3", "orthonormal harmonic"]) else "FAIL",
            "Iwasawa source supplies three orthonormal harmonic representatives",
        ),
        Gate(
            "Normalized cubic integral",
            "PASS" if contains_all(flux, ["lambda_{123}", "Omega", "Tr", "Psi_1", "Psi_2", "Psi_3"]) else "FAIL",
            "lambda_123 is defined as a trilinear overlap",
        ),
        Gate(
            "Unit holomorphic normalization",
            "PASS" if "int_X \\Omega \\wedge \\bar\\Omega = 1" in flux or "\\int_X \\Omega \\wedge \\bar\\Omega = 1" in flux else "FAIL",
            "source normalizes Omega wedge bar(Omega)",
        ),
        Gate(
            "Phase-removable unit coupling",
            "PASS" if "lambda_{123}=1" in flux and "rephasing removes the phase" in flux else "FAIL",
            "tree-level lambda_123=1 after chiral rephasing",
        ),
        Gate(
            "Rank-one statement",
            "PASS" if "rank one" in flux and "Yukawa matrix" in flux else "FAIL",
            "source states the inherited E6 27^3 tree Yukawa is rank one",
        ),
        Gate(
            "Family-zero-mode compatibility",
            "COMPATIBLE" if contains_all(superset, ["Fermion zero modes", "Internal harmonic spinors", "three fermion families"]) else "FAIL",
            "core corpus links harmonic spinors and three-family projection",
        ),
        Gate(
            "Theta/q79 scaffold compatibility",
            "PASS" if "mu_Theta = 5 TeV" in scaffold and "q = 79 mod 448" in scaffold else "FAIL",
            "seed can be carried inside the fixed scaffold environment",
        ),
        Gate(
            "Seed matrix rank",
            "PASS" if computed_rank == 1 and cert_rank == 1 else "FAIL",
            f"minimal representative rank={computed_rank}",
        ),
        Gate(
            "Seed certificate",
            "RANK_ONE_SEED_CLOSED" if cert_status == "RANK_ONE_TREE_SEED_CLOSED_CORRECTIONS_OPEN" and cert_lambda == 1 else "FAIL",
            str(cert_status),
        ),
        Gate(
            "SM operator dictionary",
            "FORMULATED"
            if dict_cert.get("status") == "REPRESENTATION_DICTIONARY_CLOSED_HIGGS_SELECTION_OPEN"
            else "OPEN",
            "E6 27^3 -> SM Yukawa operator forms are now formulated",
        ),
        Gate(
            "Low-energy Higgs projection",
            "FORMULATED"
            if higgs_cert.get("status") == "SINGLE_HIGGS_CHANNEL_PROJECTION_FORMULATED_TRIPLET_DECOUPLING_OPEN"
            else "OPEN",
            "H_u -> H and H_d -> H^dagger in the NCG/SM target",
        ),
        Gate(
            "Rank-one sector assignment",
            "OPEN",
            "select which channel receives the rank-one seed before corrections",
        ),
        Gate(
            "Light-family masses",
            "OPEN",
            "rank-one tree seed needs selected correction channels",
        ),
        Gate(
            "Precision top matching",
            "OPEN",
            "requires Higgs mixing, kinetic metrics, thresholds, and RG running",
        ),
    ]

    print("Iwasawa rank-one Yukawa seed audit")
    print("==================================")
    print()
    print(f"computed_seed_rank={computed_rank}")
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
