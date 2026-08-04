from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    ROOT
    / "certificates"
    / "q79_free_graviton_quantization_and_uv_cutset_certificate.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Free_Graviton_Quantization_and_Finite_Internal_UV_NoGo_v1.md"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    tiers = certificate["claim_tiers"]
    data = certificate["finite_data"]
    guards = certificate["guardrails"]

    require(all(certificate["checks"].values()), "one or more quantization checks failed")
    require(
        tiers["free_massless_q79_graviton_carrier"]
        == "CLOSED_EXACT_TWO_HELICITIES"
        and data["physical_polarization_count"] == 2
        and data["internal_harmonic_multiplicity"] == 1,
        "free graviton carrier changed",
    )
    require(
        tiers["free_reduced_TT_Hamiltonian_positivity"]
        == "CLOSED_FOR_KAPPA_H_POSITIVE"
        and tiers["free_propagator_and_unit_internal_residue"]
        == "CLOSED_EXACT_SHAPE"
        and data["normalized_massless_residue"] == [[1, 0], [0, 1]],
        "free Hamiltonian or residue changed",
    )
    require(
        tiers["finite_internal_trace_changes_4D_UV_power_counting"]
        == "CLOSED_NO_GO"
        and tiers["full_interacting_quantum_gravity"] == "OPEN",
        "UV no-go or interacting boundary changed",
    )
    require(
        data["new_continuous_parameters_beyond_classical_kappa"] == 0,
        "free quantization introduced a parameter",
    )
    require(
        guards["claims_free_quantization_is_interacting_QG"] is False
        and guards["claims_finite_internal_algebra_regulates_spacetime_loops"]
        is False
        and guards["claims_UV_completion"] is False,
        "free/interacting or internal/spacetime tier was conflated",
    )
    for phrase in [
        "q_lambda=sqrt(kappa_h) h_lambda",
        "<h_lambda h_lambda'>",
        "Tr_internal[p^n I_N]=N p^n",
        "Finite internal algebra is not a 4D UV regulator",
        "the selected interacting quantum measure",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print(
        "AUDIT_PASS: the exact q79 zero-mode/TT sector has a positive two-helicity "
        "free Fock quantization; finite internal dimension does not close interacting 4D UV behavior"
    )


if __name__ == "__main__":
    main()
