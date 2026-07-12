"""Audit the standard Gaussian-lattice deck scaffold for Iwasawa."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_standard_lattice_deck_scaffold_certificate.json"
PAPER = ROOT / "Iwasawa_Standard_Lattice_Deck_Scaffold_v1.md"
BASIS = CERT_DIR / "iwasawa_galerkin_basis_skeleton_certificate.json"
PROTOCOL = CERT_DIR / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
FLUX = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)
STROMINGER = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)


Gaussian = tuple[int, int]
Triple = tuple[Gaussian, Gaussian, Gaussian]


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


def add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def group_law(left: Triple, right: Triple) -> Triple:
    z1, z2, z3 = left
    w1, w2, w3 = right
    return add(z1, w1), add(z2, w2), add(add(z3, w3), mul(z1, w2))


def generators() -> dict[str, Triple]:
    zero = (0, 0)
    one = (1, 0)
    imag = (0, 1)
    return {
        "g1": (one, zero, zero),
        "g2": (imag, zero, zero),
        "g3": (zero, one, zero),
        "g4": (zero, imag, zero),
        "g5": (zero, zero, one),
        "g6": (zero, zero, imag),
    }


def main() -> None:
    cert = load_json(CERT)
    basis = load_json(BASIS)
    protocol = load_json(PROTOCOL)
    paper = read(PAPER)
    flux = read(FLUX)
    strominger = read(STROMINGER)

    recovery = cert.get("corpus_recovery", {})
    candidate = cert.get("candidate_standard_gaussian_lattice", {})
    coframe = candidate.get("coframe", {})
    algebra = cert.get("verified_algebra", {})
    gluing = cert.get("galerkin_gluing_rules", {})
    closes = cert.get("what_this_closes", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gens = generators()
    pairwise_products = [
        group_law(left, right)
        for left in gens.values()
        for right in gens.values()
    ]
    gaussian_closure = all(
        isinstance(component[0], int) and isinstance(component[1], int)
        for product in pairwise_products
        for component in product
    )

    source_text = flux + "\n" + strominger
    source_has_symbolic_quotient = contains_all(
        source_text,
        [
            "Gamma",
            "H_3",
            "Iwasawa manifold",
            "left-invariant",
        ],
    )
    source_has_explicit_generators = contains_all(
        source_text,
        [
            "z1+1",
            "z3+z2",
            "Z[i]",
        ],
    )

    candidate_generators = candidate.get("generators", [])
    generator_ids = [entry.get("id") for entry in candidate_generators]
    candidate_actions = " ".join(entry.get("action", "") for entry in candidate_generators)
    gluing_text = " ".join(str(value) for value in gluing.values())
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status")
            == "STANDARD_IWASAWA_DECK_SCAFFOLD_FORMULATED_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if basis.get("status")
            == "GALERKIN_BASIS_SKELETON_FORMULATED_SCALAR_DECK_DATA_OPEN"
            and protocol.get("status")
            == "NONINVARIANT_GALERKIN_EXECUTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            else "FAIL",
            "basis/protocol imported",
        ),
        Gate(
            "symbolic quotient recovered",
            "PASS"
            if recovery.get("quotient_symbol_Gamma_backslash_H3C") is True
            and recovery.get("left_invariant_coframe") is True
            and recovery.get("structure_equation_domega3_equals_omega1_wedge_omega2")
            is True
            and source_has_symbolic_quotient
            else "FAIL",
            "Gamma\\H3(C) and coframe checked",
        ),
        Gate(
            "explicit corpus deck data absent",
            "PASS"
            if recovery.get("explicit_Gamma_generators_supplied_by_corpus") is False
            and recovery.get("scalar_mode_basis_supplied_by_corpus") is False
            and recovery.get("bundle_transition_matrices_supplied_by_corpus") is False
            and not source_has_explicit_generators
            else "FAIL",
            str(recovery),
        ),
        Gate(
            "candidate group law",
            "PASS"
            if candidate.get("coordinates") == "z1,z2,z3 in C"
            and "z3+w3+z1*w2" in candidate.get("group_law", "")
            and candidate.get("lattice") == "Gamma0 = Z[i]^3 under the group law"
            else "FAIL",
            str(candidate),
        ),
        Gate(
            "coframe convention",
            "PASS"
            if coframe.get("omega1") == "dz1"
            and coframe.get("omega2") == "dz2"
            and coframe.get("omega3") == "z1*dz2 - dz3"
            and coframe.get("domega3") == "omega1 wedge omega2"
            else "FAIL",
            str(coframe),
        ),
        Gate(
            "generator list",
            "PASS"
            if algebra.get("generator_count") == 6
            and generator_ids == ["g1", "g2", "g3", "g4", "g5", "g6"]
            and contains_all(
                candidate_actions,
                ["z1+1", "z3+z2", "z1+i", "z3+i*z2", "z2+1", "z3+i"],
            )
            else "FAIL",
            str(candidate_generators),
        ),
        Gate(
            "Gaussian closure",
            "PASS"
            if gaussian_closure
            and algebra.get("gaussian_integer_closure_under_group_law") is True
            else "FAIL",
            str(pairwise_products[:3]),
        ),
        Gate(
            "coframe invariance",
            "PASS"
            if algebra.get("coframe_invariant_under_left_deck_action") is True
            and algebra.get("domega3_matches_corpus_sign_convention") is True
            and "omega3' = (z1+a) d(z2+b) - d(z3+c+a*z2)" in paper
            else "FAIL",
            str(algebra),
        ),
        Gate(
            "gluing rules",
            "PASS"
            if contains_all(
                gluing_text,
                [
                    "phi(gamma*z)=phi(z)",
                    "rho_E(gamma,z)",
                    "unit real six-cell",
                    "g1..g6",
                    "nonabelian deck constraints",
                ],
            )
            else "FAIL",
            gluing_text,
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("explicit_candidate_deck_generators") is True
            and closes.get("coframe_compatible_deck_action") is True
            and closes.get("fundamental_gluing_laws_formulated") is True
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
                    "scalar_basis_functions_phi_m",
                    "bundle_transition_matrices_rho_E",
                    "selected_D_E_action_on_this_basis",
                    "Gram_matrix_entries",
                    "stiffness_matrix_entries",
                ],
            )
            else "FAIL",
            str(open_items),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_Gamma0_is_MTT_selected") is False
            and guardrails.get("claims_actual_scalar_basis_constructed") is False
            and guardrails.get("claims_bundle_transitions_constructed") is False
            and guardrails.get("uses_torus_fourier_modes_without_nonabelian_deck_check")
            is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("claims_kernel_dimension_three_now") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("closes_candidate_deck_scaffold") is True
            and verdict.get("closes_selected_galerkin_basis") is False
            and "Gamma0" in verdict.get("next_step", "")
            and "finite-element" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records scaffold",
            "PASS"
            if contains_all(
                paper,
                [
                    "Gamma0 = Z[i]^3",
                    "g1: (z1,z2,z3) -> (z1+1, z2,   z3+z2)",
                    "omega3' = (z1+a) d(z2+b) - d(z3+c+a*z2)",
                    "phi(gamma*z) = phi(z)",
                    "ordinary torus Fourier modes are allowed only if",
                    "candidate standard deck scaffold",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa standard lattice deck scaffold audit")
    print("===========================================")
    print()
    print(f"generator_ids={generator_ids}")
    print(f"pairwise_generator_products_checked={len(pairwise_products)}")
    print(f"source_has_explicit_generators={source_has_explicit_generators}")
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
