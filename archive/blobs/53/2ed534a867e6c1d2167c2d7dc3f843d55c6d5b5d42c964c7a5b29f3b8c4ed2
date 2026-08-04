"""Audit the Iwasawa invariant Galerkin zero-mode slot attempt."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_galerkin_zero_mode_slot_attempt_certificate.json"
PAPER = ROOT / "Iwasawa_Invariant_Galerkin_Zero_Mode_Slot_Attempt_v1.md"
FLUX = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def rank3(matrix: list[list[int | float]]) -> int:
    rows = [[float(value) for value in row] for row in matrix]
    rank = 0
    col = 0
    while rank < 3 and col < 3:
        pivot = None
        for row in range(rank, 3):
            if abs(rows[row][col]) > 1e-12:
                pivot = row
                break
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][col]
        rows[rank] = [value / scale for value in rows[rank]]
        for row in range(3):
            if row == rank:
                continue
            factor = rows[row][col]
            rows[row] = [
                rows[row][idx] - factor * rows[rank][idx]
                for idx in range(3)
            ]
        rank += 1
        col += 1
    return rank


def c33(matrix: list[list[int | float]]) -> float:
    return float(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    flux = read(FLUX)
    seed = load_json(CERT_DIR / "iwasawa_rank_one_yukawa_seed_certificate.json")
    rplus = load_json(CERT_DIR / "c1_iwasawa_rplus_support_certificate.json")
    dictionary = load_json(CERT_DIR / "e6_to_sm_yukawa_operator_dictionary_certificate.json")
    interface = load_json(CERT_DIR / "selected_zero_mode_basis_dotd_interface_certificate.json")

    matrix = cert.get("available_iwasawa_invariant_data", {}).get("rank_one_seed", {}).get(
        "matrix", []
    )
    witness = cert.get("rank_one_collapse_witness", {})
    missing = cert.get("missing_for_valid_slot_fill", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    computed_rank = rank3(matrix) if len(matrix) == 3 else -1
    computed_c33 = c33(matrix) if len(matrix) == 3 else None
    has_expected_missing = all(
        key in missing
        for key in [
            "sector_projection_maps",
            "slot_operators",
            "slot_dotD_operators",
            "projector_green_data",
            "higgs_internal_representative",
            "primitive_contractions",
        ]
    )

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status")
            == "IWASAWA_GALERKIN_SLOT_ATTEMPT_BLOCKED_BY_SECTOR_PROJECTION_AND_DOTD_DATA"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "flux source has Iwasawa frame",
            "PASS"
            if "d}\\omega^1=\\mathrm{d}\\omega^2=0" in flux
            and "\\mathrm{d}\\omega^3=\\omega^1\\wedge\\omega^2" in flux
            and "\\alpha_1:=a\\wedge b" in flux
            else "FAIL",
            str(FLUX),
        ),
        Gate(
            "flux source has normalized seed",
            "PASS"
            if "\\Psi_i\\in H^1(X,E)" in flux
            and "\\lambda_{123}" in flux
            and "rank one" in flux
            else "FAIL",
            "Iwasawa source supplies E6 rank-one seed",
        ),
        Gate(
            "closed seed agrees",
            "PASS"
            if seed.get("tree_level_seed", {}).get("rank") == 1
            and seed.get("tree_level_seed", {}).get("lambda_123_after_rephasing") == 1
            else "FAIL",
            str(seed.get("tree_level_seed", {})),
        ),
        Gate(
            "alpha1 driver agrees",
            "PASS"
            if rplus.get("rplus_support", {}).get("alpha_2_component") == 0
            and rplus.get("rplus_support", {}).get("alpha_3_component") == 0
            and "alpha_1" in cert.get("available_iwasawa_invariant_data", {})
            .get("c1_curvature_driver", {})
            .get("formula", "")
            else "FAIL",
            str(rplus.get("rplus_support", {})),
        ),
        Gate(
            "SM dictionary not projection maps",
            "PASS"
            if dictionary.get("closed", {}).get("sm_yukawa_operator_forms") is True
            and dictionary.get("open", {}).get("rank_one_seed_sector_assignment") is True
            and cert.get("attempted_universal_slot_fill", {}).get("valid_completed_fill")
            is False
            else "FAIL",
            "representation labels are not zero-mode slot projectors",
        ),
        Gate(
            "interface still requires slots",
            "PASS"
            if interface.get("completion_gates", {}).get("all_D_operators_supplied") is False
            and interface.get("completion_gates", {}).get(
                "all_dotD_alpha1_operators_supplied"
            )
            is False
            else "FAIL",
            str(interface.get("completion_gates", {})),
        ),
        Gate(
            "E33 rank witness",
            "PASS" if computed_rank == witness.get("rank") == 1 else "FAIL",
            f"rank={computed_rank}",
        ),
        Gate(
            "E33 C33 witness",
            "PASS" if computed_c33 == witness.get("C33") == 0 else "FAIL",
            f"C33={computed_c33}",
        ),
        Gate(
            "universal orientation witness",
            "PASS"
            if witness.get("Delta_v_if_universal_up_down_orientation") == [0, 0]
            else "FAIL",
            str(witness),
        ),
        Gate(
            "missing data listed",
            "PASS" if has_expected_missing else "FAIL",
            ", ".join(sorted(missing)),
        ),
        Gate(
            "guardrails forbid overclaim",
            "PASS"
            if guardrails.get("uses_execution_ii_entries") is False
            and guardrails.get("uses_observed_masses_or_mixings") is False
            and guardrails.get("promotes_pre_sm_seed_to_all_slots") is False
            and guardrails.get("claims_primitive_contractions_filled") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict blocks fill",
            "PASS"
            if verdict.get("attempted_galerkin_fill") is True
            and verdict.get("filled_selected_zero_mode_dotD_interface") is False
            and verdict.get("computed_c1_primitive_contractions") is False
            and "Dolbeault" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records attempt",
            "PASS"
            if "Attempted Slot Fill" in paper
            and "Rank-One Collapse Witness" in paper
            and "Iwasawa Monad Dolbeault Complex Extraction" in paper
            else "FAIL",
            "paper contains attempt, witness, and next computation",
        ),
        Gate(
            "paper refuses shortcut",
            "PASS"
            if "not a valid completed fill" in paper
            and "not to guess primitive C1" in paper
            and "matrices" in paper
            else "FAIL",
            "pre-SM seed is not promoted to all slots",
        ),
    ]

    print("Iwasawa invariant Galerkin zero-mode slot attempt audit")
    print("=======================================================")
    print()
    print(f"computed_rank={computed_rank}")
    print(f"computed_C33={computed_c33}")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
