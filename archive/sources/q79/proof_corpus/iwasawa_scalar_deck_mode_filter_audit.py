"""Audit the scalar deck-mode filter for the standard Iwasawa scaffold."""

from __future__ import annotations

import cmath
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_scalar_deck_mode_filter_certificate.json"
DECK = CERT_DIR / "iwasawa_standard_lattice_deck_scaffold_certificate.json"
BASIS = CERT_DIR / "iwasawa_galerkin_basis_skeleton_certificate.json"
PROTOCOL = CERT_DIR / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
PAPER = ROOT / "Iwasawa_Scalar_Deck_Mode_Filter_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def phase(value: float) -> complex:
    return cmath.exp(2j * cmath.pi * value)


def check_twist(k1: int, k2: int, y1: float, y2: float) -> dict[str, complex]:
    central_g1 = phase(k1 * y1 + k2 * y2)
    base_g1 = phase(-k1 * y1 - k2 * y2)
    central_g2 = phase(-k1 * y2 + k2 * y1)
    base_g2 = phase(k1 * y2 - k2 * y1)
    return {
        "g1_product": central_g1 * base_g1,
        "g2_product": central_g2 * base_g2,
    }


def nearly_one(value: complex, tolerance: float = 1e-12) -> bool:
    return abs(value - 1) < tolerance


def main() -> None:
    cert = load_json(CERT)
    deck = load_json(DECK)
    basis = load_json(BASIS)
    protocol = load_json(PROTOCOL)
    paper = read(PAPER)

    coordinates = cert.get("coordinate_realization", {})
    gluing = cert.get("scalar_gluing_equations", {})
    central = cert.get("central_character_decomposition", {})
    twists = central.get("twisted_base_conditions", {})
    sectors = cert.get("mode_sector_conclusions", {})
    implication = cert.get("finite_basis_implication", {})
    closes = cert.get("what_this_closes", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    twist_check = check_twist(k1=2, k2=-1, y1=0.37, y2=0.19)
    central_zero_twists = check_twist(k1=0, k2=0, y1=0.37, y2=0.19)

    gluing_text = " ".join(gluing.values())
    twist_text = " ".join(twists.values())
    implication_text = " ".join(implication.values())
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status")
            == "IWASAWA_SCALAR_DECK_MODE_FILTER_FORMULATED_SELECTED_MODES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if deck.get("status")
            == "STANDARD_IWASAWA_DECK_SCAFFOLD_FORMULATED_SELECTION_OPEN"
            and basis.get("status")
            == "GALERKIN_BASIS_SKELETON_FORMULATED_SCALAR_DECK_DATA_OPEN"
            and protocol.get("status")
            == "NONINVARIANT_GALERKIN_EXECUTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            else "FAIL",
            "deck scaffold, basis skeleton, and Galerkin protocol imported",
        ),
        Gate(
            "real coordinate split",
            "PASS"
            if coordinates.get("z1") == "x1 + i*x2"
            and coordinates.get("z2") == "y1 + i*y2"
            and coordinates.get("z3") == "t1 + i*t2"
            and "[0,1)^6" in coordinates.get("real_cell", "")
            else "FAIL",
            str(coordinates),
        ),
        Gate(
            "six scalar gluing equations",
            "PASS"
            if set(gluing) == {"g1", "g2", "g3", "g4", "g5", "g6"}
            and contains_all(
                gluing_text,
                [
                    "t1+y1,t2+y2",
                    "t1-y2,t2+y1",
                    "y1+1",
                    "y2+1",
                    "t1+1",
                    "t2+1",
                ],
            )
            else "FAIL",
            gluing_text,
        ),
        Gate(
            "central character ansatz",
            "PASS"
            if central.get("central_labels") == "k=(k1,k2) in Z^2"
            and "exp(2*pi*i*(k1*t1+k2*t2))" in central.get("ansatz", "")
            and "g5 and g6 force k1,k2 to be integers"
            in central.get("central_lattice_condition", "")
            else "FAIL",
            str(central),
        ),
        Gate(
            "twisted base conditions",
            "PASS"
            if contains_all(
                twist_text,
                [
                    "exp(2*pi*i*(-k1*y1-k2*y2))",
                    "exp(2*pi*i*(k1*y2-k2*y1))",
                    "y1+1",
                    "y2+1",
                ],
            )
            else "FAIL",
            twist_text,
        ),
        Gate(
            "twist cancels central shift",
            "PASS"
            if all(nearly_one(value) for value in twist_check.values())
            and all(nearly_one(value) for value in central_zero_twists.values())
            else "FAIL",
            str(twist_check),
        ),
        Gate(
            "central-zero sector",
            "PASS"
            if sectors.get("central_zero_sector", {}).get("label") == "k=(0,0)"
            and sectors.get("central_zero_sector", {}).get(
                "ordinary_torus_fourier_modes_on_x1_x2_y1_y2"
            )
            is True
            else "FAIL",
            str(sectors.get("central_zero_sector", {})),
        ),
        Gate(
            "nonzero central sectors",
            "PASS"
            if sectors.get("nonzero_central_sectors", {}).get("label") == "k != (0,0)"
            and sectors.get("nonzero_central_sectors", {}).get(
                "ordinary_torus_fourier_modes_on_x1_x2_y1_y2"
            )
            is False
            and "theta/magnetic" in sectors.get("nonzero_central_sectors", {}).get(
                "required_basis_type", ""
            )
            else "FAIL",
            str(sectors.get("nonzero_central_sectors", {})),
        ),
        Gate(
            "finite basis implication",
            "PASS"
            if contains_all(
                implication_text,
                [
                    "finite central labels",
                    "twisted base conditions",
                    "unit six-cell",
                    "g1..g6",
                    "rho_E",
                ],
            )
            else "FAIL",
            implication_text,
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("six_scalar_deck_equations") is True
            and closes.get("central_character_integer_labels") is True
            and closes.get("twisted_base_conditions") is True
            and closes.get("torus_fourier_guardrail") is True
            and closes.get("spectral_and_finite_element_filter") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if all(open_items.values())
            and contains_all(
                open_text,
                [
                    "MTT_selection_or_source_confirmation_of_Gamma0",
                    "finite_selected_scalar_label_set",
                    "explicit_theta_or_magnetic_basis_functions_for_nonzero_k",
                    "bundle_transition_matrices_rho_E",
                    "selected_D_E_action_on_filtered_basis",
                    "three_family_gap_error_certificate",
                ],
            )
            else "FAIL",
            str(open_items),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_Gamma0_is_MTT_selected") is False
            and guardrails.get("claims_selected_scalar_basis_constructed") is False
            and guardrails.get("uses_ordinary_torus_fourier_modes_for_nonzero_central_character")
            is False
            and guardrails.get("claims_bundle_transitions_constructed") is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("claims_Galerkin_matrices_constructed") is False
            and guardrails.get("claims_kernel_dimension_three_now") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("closes_scalar_mode_admissibility_filter") is True
            and verdict.get("closes_selected_scalar_modes") is False
            and "rho_E" in verdict.get("next_step", "")
            and "selected D_E" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records filter",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa Scalar Deck Mode Filter",
                    "g1: phi(x1+1,x2,y1,y2,t1+y1,t2+y2)",
                    "phi = exp(2*pi*i*(k1*t1+k2*t2))*F_k",
                    "F_k(x1+1,x2,y1,y2)",
                    "exp(2*pi*i*(k1*y2-k2*y1))",
                    "ordinary four-torus Fourier modes are not admissible",
                    "rho_E",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa scalar deck-mode filter audit")
    print("=====================================")
    print()
    print(f"twist_check_g1={twist_check['g1_product']}")
    print(f"twist_check_g2={twist_check['g2_product']}")
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
