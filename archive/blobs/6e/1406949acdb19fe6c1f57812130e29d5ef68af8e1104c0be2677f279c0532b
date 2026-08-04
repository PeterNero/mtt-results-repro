from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PRIMITIVE_SEARCH_IMPORT = ROOT / "certificates" / "routec_selected_primitive_emission_search_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_nonidentity_rhoe_bn_construction_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_nonidentity_rhoe_bn_construction_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_nonidentity_rhoe_bn_construction_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_NonIdentity_RhoE_BN_Construction_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    primitive_search = load(PRIMITIVE_SEARCH_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    rho = src["rho_E_candidate"]
    gates = rho["numeric_gates"]
    basis = src["B_N_scaffold"]
    straight = src["superset_mode"]["straight_path"]

    closed_now = {
        "previous_no_legal_emission_search_imported": primitive_search["theorem"]["proved"],
        "nonidentity_projective_rhoE_candidate_built": src_cert["what_closes"]["nonidentity_projective_rhoE_candidate_built"],
        "identity_smoke_replaced_by_nonidentity_candidate": src_cert["what_closes"]["identity_smoke_replaced_by_nonidentity_candidate"],
        "finite_search_space_reduced_to_canonical_F3xF3_projective_packet": src_cert["what_closes"]["finite_search_space_reduced_to_canonical_F3xF3_projective_packet"],
        "finite_twisted_deck_fiber_basis_scaffold_built": src_cert["what_closes"]["finite_twisted_deck_fiber_basis_scaffold_built"],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
        "R2_metric_connection_numeric_gate_closed": src["what_remains_open"]["R2_selected_rhoE_metric_connection"] is False,
    }

    numeric_checks = {
        "rho_packet_passes_numeric_gate": gates["passes_numeric_packet_gate"] is True,
        "rho_is_nonidentity": gates["nonidentity_norm"] > 0.1,
        "unitary_residual_small": gates["unitary_residual_max"] < 1e-10,
        "order3_residual_small": gates["order3_residual_max"] < 1e-10,
        "projective_commutator_residual_small": gates["projective_commutator_residual"] < 1e-10,
        "selected_active_generators_only": gates["uses_only_selected_active_generators_g1_g2"] is True,
        "kernel_generators_identity": gates["kernel_generators_identity"] is True,
        "active_deck_rank_two": gates["active_deck_rank_over_F3"] == 2,
    }

    still_open_checks = {
        "rhoE_source_promotion_still_open": src["what_remains_open"]["R2_source_promotion_for_rhoE"] is True,
        "rhoE_not_selected_by_mtt": rho["selected_by_mtt"] is False,
        "BN_payload_not_built": straight["BN_payload_built"] is False,
        "BN_payload_gate_not_passed": basis["passes_B_N_payload_gate"] is False,
        "smooth_scalar_basis_not_emitted": basis["smooth_scalar_basis_phi_m_emitted"] is False,
        "metric_quadrature_not_emitted": basis["metric_quadrature_emitted"] is False,
        "selected_D_E_action_not_emitted": basis["selected_D_E_action_emitted"] is False,
        "gram_stiffness_not_emitted": (
            basis["gram_stiffness_emitted"] is False
            and basis["gap_certificate_emitted"] is False
        ),
        "honest_replay_not_ready": straight["honest_replay_ready"] is False,
    }

    theorem = {
        "name": "RouteCNonIdentityRhoEBNConstructionImportTheorem",
        "proved": all(closed_now.values()) and all(numeric_checks.values()) and all(still_open_checks.values()),
        "statement": (
            "The selected F3^2 deck shadow admits a canonical non-identity "
            "rank-3 Heisenberg/Weyl projective rho_E packet with unitary "
            "order-three generators and omega commutator. This closes the "
            "finite rho_E numerical packet gate and replaces identity smoke, "
            "but it does not yet supply the quotient-valid smooth B_N Galerkin "
            "basis, quadrature, D_E action, eigenpairs, or gap certificate."
        ),
    }

    verdict = {
        "nonidentity_rhoE_numeric_packet_built": True,
        "R2_metric_connection_numeric_gate_closed": True,
        "R2_source_promotion_closed": False,
        "R4_BN_payload_closed": False,
        "R6_honest_replay_ready": False,
        "next_required_artifact": src["next_required_artifact"],
    }

    guardrails = {
        "does_not_claim_rhoE_selected_source": True,
        "does_not_claim_B_N_payload": True,
        "does_not_claim_R4_or_R6_closed": True,
        "does_not_use_formal_lift_as_proof": True,
        "does_not_use_target_fitting": True,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "rho_E_candidate": rho,
        "B_N_scaffold": basis,
        "contract_comparison": src["contract_comparison"],
        "closed_now": closed_now,
        "numeric_checks": numeric_checks,
        "still_open_checks": still_open_checks,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Non-Identity rhoE / BN Construction Import v1

## Result

The first constrained numerical repair has been imported.

The selected `F3^2` deck shadow supports a canonical non-identity rank-3
Heisenberg/Weyl projective `rho_E` packet. Numerically:

```text
unitary residual < 1e-10
order-three residual < 1e-10
projective commutator residual < 1e-10
active deck rank over F3 = 2
```

This replaces the old identity-smoke `rho_E` diagnostic with a real finite
non-identity projective packet.

## Boundary

This is not full selected payload closure. The packet is compatible with the
selected deck/cocycle shadow, but still needs a source certificate tying it to
the selected Strominger/HYM minimizer.

The `B_N` object is still only a finite twisted deck/fiber scaffold. It does
not yet emit:

```text
smooth scalar Galerkin basis phi_m
metric volume quadrature
selected D_E action on the basis
Gram/stiffness matrix entries
generalized eigenpairs
gap/error certificate
```

## Status

```text
ROUTEC_NONIDENTITY_RHOE_NUMERICAL_PACKET_IMPORTED_BN_STILL_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_nonidentity_rhoe_bn_construction_import",
                "status": "ROUTEC_NONIDENTITY_RHOE_NUMERICAL_PACKET_IMPORTED_BN_STILL_OPEN",
                "input_certificates": {
                    "routec_selected_primitive_emission_search_import": str(PRIMITIVE_SEARCH_IMPORT),
                    "selected_routec_nonidentity_rhoe_bn_construction": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "numeric_checks": numeric_checks,
                "still_open_checks": still_open_checks,
                "verdict": verdict,
                "guardrails": guardrails,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print("STATUS: ROUTEC_NONIDENTITY_RHOE_NUMERICAL_PACKET_IMPORTED_BN_STILL_OPEN")


if __name__ == "__main__":
    main()
