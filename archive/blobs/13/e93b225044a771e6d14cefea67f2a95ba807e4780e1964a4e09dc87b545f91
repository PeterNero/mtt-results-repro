"""Audit the Iwasawa Galerkin basis skeleton."""

from __future__ import annotations

import json
from dataclasses import dataclass
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_galerkin_basis_skeleton_certificate.json"
PAPER = ROOT / "Iwasawa_Galerkin_Basis_Skeleton_v1.md"
PROTOCOL = CERT_DIR / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
DIAGNOSTIC = CERT_DIR / "iwasawa_diagnostic_h1_three_spectral_pipeline_certificate.json"
RECOVERY = CERT_DIR / "iwasawa_typed_monad_section_recovery_certificate.json"
FLUX = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)


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


def dimensions(scalar_count: int, rank: int = 3) -> dict[str, int]:
    return {str(degree): scalar_count * rank * comb(3, degree) for degree in range(4)}


def main() -> None:
    cert = load_json(CERT)
    protocol = load_json(PROTOCOL)
    diagnostic = load_json(DIAGNOSTIC)
    recovery = load_json(RECOVERY)
    paper = read(PAPER)
    flux = read(FLUX)

    skeleton = cert.get("closed_form_fiber_skeleton", {})
    options = cert.get("basis_source_options", {})
    decisions = cert.get("closed_decisions", {})
    missing = cert.get("still_missing_for_actual_B_N", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    form_counts = {str(degree): comb(3, degree) for degree in range(4)}
    invariant_dims = dimensions(1)
    first_extension_dims = dimensions(2)

    source_requirements = " ".join(
        requirement
        for option in options.values()
        for requirement in option.get("requires", [])
    )
    missing_text = " ".join(missing)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status")
            == "GALERKIN_BASIS_SKELETON_FORMULATED_SCALAR_DECK_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if protocol.get("status")
            == "NONINVARIANT_GALERKIN_EXECUTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            and diagnostic.get("what_this_achieves", {}).get(
                "proves_pipeline_can_extract_three_modes_when_valid_D_is_given"
            )
            is True
            and recovery.get("route_decision", {}).get(
                "non_invariant_spectral_galerkin_fallback_triggered"
            )
            is True
            else "FAIL",
            "upstream basis route imported",
        ),
        Gate(
            "Iwasawa source structure",
            "PASS"
            if contains_all(
                flux,
                [
                    "left-invariant",
                    "H_3",
                    "cocompact",
                    "Iwasawa manifold",
                    "d}\\omega^3",
                ],
            )
            else "FAIL",
            str(FLUX),
        ),
        Gate(
            "form counts",
            "PASS"
            if skeleton.get("anti_holomorphic_form_counts_by_degree") == form_counts
            else "FAIL",
            str(skeleton.get("anti_holomorphic_form_counts_by_degree")),
        ),
        Gate(
            "dimension formula",
            "PASS"
            if skeleton.get("rank_E") == 3
            and skeleton.get("basis_element_shape")
            == "phi_m tensor fiber_a tensor baromega_I"
            and "binomial(3,p)" in skeleton.get("degree_dimension_formula", "")
            else "FAIL",
            str(skeleton),
        ),
        Gate(
            "invariant dimensions",
            "PASS"
            if skeleton.get("invariant_scalar_count") == 1
            and skeleton.get("invariant_dimensions_by_degree") == invariant_dims
            else "FAIL",
            str(invariant_dims),
        ),
        Gate(
            "first non-invariant dimensions",
            "PASS"
            if skeleton.get("first_noninvariant_extension_scalar_count") == 2
            and skeleton.get("first_noninvariant_extension_dimensions_by_degree")
            == first_extension_dims
            else "FAIL",
            str(first_extension_dims),
        ),
        Gate(
            "basis source options",
            "PASS"
            if set(options)
            == {"deck_equivariant_spectral", "finite_element_fundamental_domain"}
            and contains_all(
                source_requirements,
                [
                    "Gamma lattice/deck generators",
                    "scalar mode functions",
                    "derivative/action matrices",
                    "fundamental-domain",
                    "periodic/deck gluing constraints",
                    "bundle transition",
                ],
            )
            and all(option.get("available_from_current_corpus") is False for option in options.values())
            else "FAIL",
            source_requirements,
        ),
        Gate(
            "closed decisions",
            "PASS"
            if decisions.get("form_fiber_tensor_bookkeeping_closed") is True
            and decisions.get("first_noninvariant_basis_must_have_scalar_count_at_least_two")
            is True
            and decisions.get("invariant_subspace_is_recovered_at_scalar_count_one")
            is True
            and decisions.get("scalar_deck_basis_not_supplied_by_current_corpus")
            is True
            and decisions.get("bundle_transition_matrices_not_supplied_by_current_corpus")
            is True
            else "FAIL",
            str(decisions),
        ),
        Gate(
            "missing actual basis data",
            "OPEN"
            if all(missing.values())
            and contains_all(
                missing_text,
                [
                    "scalar_basis_functions_phi_m",
                    "deck_or_periodic_constraints",
                    "bundle_transition_or_equivariance_matrices",
                    "selected_D_E_action_on_basis",
                    "Gram_matrix_entries",
                    "stiffness_matrix_entries",
                ],
            )
            else "FAIL",
            str(missing),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_actual_B_N_constructed") is False
            and guardrails.get("uses_coordinate_functions_as_quotient_modes_without_deck_check")
            is False
            and guardrails.get("uses_scalar_central_circle_modes_as_untwisted_zero_modes")
            is False
            and guardrails.get("uses_invariant_subspace_as_noninvariant_basis") is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("claims_kernel_dimension_three_now") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("closes_basis_skeleton") is True
            and verdict.get("closes_actual_basis_functions") is False
            and "deck-equivariant scalar basis" in verdict.get("next_step", "")
            and "finite-element" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records skeleton",
            "PASS"
            if contains_all(
                paper,
                [
                    "phi_m tensor fiber_a tensor baromega_I",
                    "dim V_N^(0,p) = s_N * 3 * binomial(3,p)",
                    "(3, 9, 9, 3)",
                    "(6, 18, 18, 6)",
                    "deck-equivariant scalar basis",
                    "finite-element mesh with deck gluing",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa Galerkin basis skeleton audit")
    print("====================================")
    print()
    print(f"form_counts={form_counts}")
    print(f"invariant_dims={invariant_dims}")
    print(f"first_extension_dims={first_extension_dims}")
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
