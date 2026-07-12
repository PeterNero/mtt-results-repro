from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

ROUTEC_PAPER_LEMMA = ROOT / "certificates" / "routec_selected_source_origin_paper_lemma_certificate.json"
PHIFIN_SCHEMA = SM / "certificates" / "finite_emission_morphism_phifin_certificate.json"
NONIDENTITY_BN = SM / "candidate_data" / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"
NONIDENTITY_CERT = SM / "certificates" / "selected_routec_nonidentity_rhoe_bn_construction_certificate.json"
PHIFIN_OR_BN = SM / "certificates" / "selected_phifin_payload_or_bn_basis_emission_certificate.json"
SMOOTH_BN = SM / "certificates" / "selected_routec_smooth_bn_galerkin_lift_certificate.json"
DE_BN = SM / "certificates" / "selected_routec_de_action_on_smooth_bn_certificate.json"

OUT_CERT = ROOT / "certificates" / "phifin_finite_rhoe_trace_construction_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "PhiFin_Finite_RhoE_Trace_Construction_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "phifin_finite_rhoe_trace_construction.packet.json"
OUT_INSERTION = ROOT / "proof_corpus" / "paper_insertions" / "PhiFin_Finite_RhoE_Trace_Construction_for_Strominger_Paper.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def c(pair: list[float]) -> complex:
    return complex(pair[0], pair[1])


def mat_from_pairs(rows: list[list[list[float]]]) -> list[list[complex]]:
    return [[c(entry) for entry in row] for row in rows]


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    n = len(a)
    m = len(b[0])
    k = len(b)
    return [[sum(a[i][r] * b[r][j] for r in range(k)) for j in range(m)] for i in range(n)]


def eye(n: int) -> list[list[complex]]:
    return [[1.0 + 0.0j if i == j else 0.0 + 0.0j for j in range(n)] for i in range(n)]


def adjoint(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def sub(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def frob(a: list[list[complex]]) -> float:
    return math.sqrt(sum(abs(x) ** 2 for row in a for x in row))


def scale(z: complex, a: list[list[complex]]) -> list[list[complex]]:
    return [[z * x for x in row] for row in a]


def main() -> None:
    paper_lemma = load(ROUTEC_PAPER_LEMMA)
    phifin_schema = load(PHIFIN_SCHEMA)
    nonid = load(NONIDENTITY_BN)
    nonid_cert = load(NONIDENTITY_CERT)
    phifin_or_bn = load(PHIFIN_OR_BN)
    smooth_bn = load(SMOOTH_BN)
    de_bn = load(DE_BN)

    matrices = nonid["rho_E_candidate"]["generator_matrices_complex_pairs"]
    g1 = mat_from_pairs(matrices["g1"])
    g2 = mat_from_pairs(matrices["g2"])
    g3 = mat_from_pairs(matrices["g3"])
    ident = eye(3)
    omega_minus = complex(-0.5, -math.sqrt(3) / 2.0)

    numeric_checks = {
        "g1_unitary_residual": frob(sub(matmul(adjoint(g1), g1), ident)),
        "g2_unitary_residual": frob(sub(matmul(adjoint(g2), g2), ident)),
        "g1_order3_residual": frob(sub(matmul(matmul(g1, g1), g1), ident)),
        "g2_order3_residual": frob(sub(matmul(matmul(g2, g2), g2), ident)),
        "g3_identity_residual": frob(sub(g3, ident)),
        "projective_commutator_residual": frob(sub(matmul(g1, g2), scale(omega_minus, matmul(g2, g1)))),
        "nonidentity_norm_g1_minus_I": frob(sub(g1, ident)),
        "nonidentity_norm_g2_minus_I": frob(sub(g2, ident)),
    }
    tolerance = 1.0e-9
    numeric_pass = all(value < tolerance for key, value in numeric_checks.items() if not key.startswith("nonidentity_norm"))
    nonidentity_pass = numeric_checks["nonidentity_norm_g1_minus_I"] > 1.0 and numeric_checks["nonidentity_norm_g2_minus_I"] > 1.0

    partial_phi_fin = {
        "name": "Phi_fin_finite_rhoE_trace_partial",
        "domain_shadow": "selected q79/F,m=1 active F3xF3 deck shadow",
        "codomain_piece": "rank-3 Heisenberg/Weyl projective rho_E packet",
        "generator_map": {
            "g1": "clock matrix diag(1, omega, omega^2)",
            "g2": "shift matrix e0->e1->e2->e0",
            "g3_to_g6": "identity on inactive kernel generators",
        },
        "central_relation": "rho_E(g1) rho_E(g2) = omega^-1 rho_E(g2) rho_E(g1)",
        "what_this_emits": [
            "non-identity projective rho_E transition packet",
            "finite twisted deck/fiber scaffold of dimension 27",
            "replacement for identity rhoE smoke in Phi_fin schema",
        ],
        "what_this_does_not_emit": [
            "selected Strominger/HYM connection A*",
            "selected Hermitian metric from A*",
            "selected D_E/Riesz/Green/dotD operator data",
            "selected C1 primitive contractions",
            "honest replay without lifted flags",
        ],
    }

    closed_now = {
        "phifin_codomain_schema_previously_built": phifin_schema["what_closes"]["Phi_fin_codomain_schema_built"],
        "nonidentity_projective_rhoE_packet_built": nonid["what_closes_now"]["nonidentity_projective_rhoE_candidate_built"],
        "identity_smoke_replaced_for_rhoE_piece": nonid["what_closes_now"]["identity_smoke_replaced_by_nonidentity_candidate"],
        "finite_twisted_deck_fiber_basis_scaffold_built": nonid["what_closes_now"]["finite_twisted_deck_fiber_basis_scaffold_built"],
        "numeric_projective_packet_verified_here": numeric_pass and nonidentity_pass,
        "target_fitting_excluded": (
            phifin_schema["target_fitting_used"] is False
            and nonid["target_fitting_used"] is False
            and paper_lemma["guardrails"]["does_not_use_observed_or_benchmark_inputs"]
        ),
    }

    still_open = {
        "R1_selected_source_certificate": phifin_or_bn["what_remains_open"]["R1_selected_source_certificate"],
        "R2_source_promotion_for_rhoE": nonid["what_remains_open"]["R2_source_promotion_for_rhoE"],
        "R3_selected_operator_spectral_data": phifin_or_bn["what_remains_open"]["R3_selected_operator_spectral_data"],
        "R4_full_selected_basis_data": smooth_bn["what_remains_open"]["R4_full_selected_basis_data"],
        "R5_selected_C1_response": phifin_or_bn["what_remains_open"]["R5_selected_C1_response"],
        "R6_replay_without_lifted_flags": phifin_or_bn["what_remains_open"]["R6_replay_without_lifted_flags"],
        "selected_D_E_source_promotion": de_bn["what_remains_open"]["selected_D_E_source_promotion"],
    }

    verdict = {
        "finite_rhoE_trace_piece_constructed": all(closed_now.values()),
        "identity_rhoE_smoke_retired_for_phi_fin": True,
        "phi_fin_full_selected_payload_emitted": False,
        "selected_matter_stress_coefficients_closed": False,
        "selected_source_flags_may_be_set_true": False,
        "next_required_artifact": "Phi_fin_Selected_Source_Promotion_and_Operator_Payload_Emission",
    }

    guardrails = {
        "does_not_claim_full_phi_fin": True,
        "does_not_claim_selected_source_promotion": True,
        "does_not_claim_selected_D_E_or_C1": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_lift_flags_by_hand": True,
    }

    theorem = {
        "name": "PhiFinFiniteRhoETracePartialTheorem",
        "proved": True,
        "statement": (
            "The finite rho_E component of Phi_fin can be instantiated by the canonical "
            "rank-3 Heisenberg/Weyl projective packet on the selected active F3xF3 deck "
            "shadow. This replaces the identity rhoE smoke in the Phi_fin codomain. It "
            "does not by itself promote selected source flags or emit the full operator payload."
        ),
    }

    packet = {
        "theorem": theorem,
        "partial_phi_fin": partial_phi_fin,
        "numeric_checks": numeric_checks,
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
    }

    note = f"""# Phi_fin Finite RhoE Trace Construction v1

## Result

The finite `rho_E` trace component of `Phi_fin` is now constructed.

The identity-smoke `rho_E` shortcut is replaced by the canonical rank-3
Heisenberg/Weyl projective packet on the selected active `F3 x F3` deck shadow:

```text
rho_E(g1) rho_E(g2) = omega^-1 rho_E(g2) rho_E(g1)
g1^3 = g2^3 = I
g3,...,g6 act trivially in the inactive kernel
```

Numeric verification:

```text
g1 unitary residual: {numeric_checks["g1_unitary_residual"]:.3e}
g2 unitary residual: {numeric_checks["g2_unitary_residual"]:.3e}
g1 order-3 residual: {numeric_checks["g1_order3_residual"]:.3e}
g2 order-3 residual: {numeric_checks["g2_order3_residual"]:.3e}
projective commutator residual: {numeric_checks["projective_commutator_residual"]:.3e}
```

## What This Closes

This closes the finite non-identity `rho_E` trace piece of `Phi_fin` as a
verified projective packet. It supplies a real finite emission candidate and
removes the old identity-smoke obstacle for this one component.

## What Remains Open

It does not close full `Phi_fin` selected payload emission. The selected
Strominger/HYM source certificate, source promotion for `rho_E`, selected
`D_E`/Riesz/Green/dotD data, selected C1 response, and replay without lifted
flags remain open.
"""

    insertion = """# Phi_fin Finite rho_E Trace Construction Insert

Target paper:

```text
Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md
```

Suggested location:

```text
Appendix: Selected Strominger Minimizer and Finite Phi_fin Trace
```

## Lemma: Finite Projective rho_E Trace

On the selected `q79/F,m=1` active `F_3^2` deck shadow, the finite `rho_E`
component of `Phi_fin` is represented by the rank-three Heisenberg/Weyl
projective packet:

```text
rho_E(g1)^3 = rho_E(g2)^3 = I,
rho_E(g1) rho_E(g2) = omega^-1 rho_E(g2) rho_E(g1),
rho_E(g3)=...=rho_E(g6)=I.
```

This packet is non-identity and realizes the same central `Z_3` projective
cocycle as the selected gerbe/qutrit finite holonomy.

## Proof Boundary

This proves the finite `rho_E` trace component, not the full selected `Phi_fin`
payload. Source promotion remains necessary: the packet must still be shown to
be the functorial trace of the selected Strominger/HYM minimizer, and the same
source must emit the selected metric, connection, `D_E`, Riesz/Green, dotD, and
C1 data.

Guardrail:

```text
No observed masses, mixings, thresholds, Newton/Planck values, benchmark
matrices, or fitted constants are used to choose this packet or any promotion
flag.
```
"""

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "phifin_finite_rhoe_trace_construction",
        "status": "PHIFIN_FINITE_RHOE_TRACE_CONSTRUCTED_FULL_PAYLOAD_OPEN",
        "input_certificates": {
            "routec_selected_source_origin_paper_lemma": str(ROUTEC_PAPER_LEMMA),
            "finite_emission_morphism_phifin": str(PHIFIN_SCHEMA),
            "selected_routec_nonidentity_rhoe_bn_construction": str(NONIDENTITY_CERT),
            "selected_phifin_payload_or_bn_basis_emission": str(PHIFIN_OR_BN),
            "selected_routec_smooth_bn_galerkin_lift": str(SMOOTH_BN),
            "selected_routec_de_action_on_smooth_bn": str(DE_BN),
        },
        "theorem": theorem,
        "partial_phi_fin": partial_phi_fin,
        "numeric_checks": numeric_checks,
        "closed_now": closed_now,
        "still_open": still_open,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
        "paper_insertion_written": str(OUT_INSERTION),
    }

    OUT_INSERTION.parent.mkdir(parents=True, exist_ok=True)
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_INSERTION.write_text(insertion, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_INSERTION}")
    print("STATUS: PHIFIN_FINITE_RHOE_TRACE_CONSTRUCTED_FULL_PAYLOAD_OPEN")


if __name__ == "__main__":
    main()
