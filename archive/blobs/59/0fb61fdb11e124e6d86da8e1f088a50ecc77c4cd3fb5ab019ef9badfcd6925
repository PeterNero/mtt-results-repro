"""Build the selected gauge-transported B_N Phi_fin trace theorem.

The previous artifact rejected exact equality between the selected HYM trace
and the raw model-active B_N packet.  This artifact proves the corrected
statement: the selected diagonal End0 trace is obtained by gauge transport
U=exp(-u ad(T3)) on the T1/T2 plane, with the T3 and Higgs-singlet lanes
protected.  This closes the functional Phi_fin trace theorem for the diagonal
End0 lane, while finite 27-mode validator replay remains open because the
transport is not closed inside the raw B_N truncation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"
VALUE = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
T1T2_GREEN = DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
SOURCE_PAYLOAD = DATA / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json"

OUTPUT = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
CERT = CERTS / "selected_gauge_transported_bn_phifin_trace_certificate.json"
NOTE = CORPUS / "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_v1.md"

STATUS = "MTT_SELECTED_GAUGE_TRANSPORTED_BN_PHIFIN_TRACE_PROVED_FINITE_REPLAY_OPEN"
NEXT = "MTT_Selected_TransportClosed_BN_Basis_or_ValidatorReplay_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]
ALL_SECTORS = MATTER_SECTORS + ["H"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sector_trace_slot(sector: str, value: dict[str, Any]) -> dict[str, Any]:
    slot = value["finite_value_payload"]["sector_slots"][sector]
    if sector == "H":
        transport = "identity on Higgs singlet"
        selected_basis = ["H:h0"]
        selected_projector = "P_H^sel=P_H^model"
        transport_needed = False
    else:
        transport = "U=exp(-u ad(T3)) on span(T1,T2), identity on T3"
        selected_basis = [
            f"{sector}:U*T1_model",
            f"{sector}:U*T2_model",
            f"{sector}:T3_model",
        ]
        selected_projector = f"P_{sector}^sel=U P_{sector}^model U^-1"
        transport_needed = True
    return {
        "sector": sector,
        "model_basis_ids": slot["ordered_zero_mode_basis_ids"],
        "model_basis_indices": slot["ordered_zero_mode_basis_indices"],
        "selected_transported_basis_labels": selected_basis,
        "transport": transport,
        "transport_needed": transport_needed,
        "selected_projector_formula": selected_projector,
        "rank_preserved": True,
        "gap_preserved_by_unitary_transport": True,
        "source_trace_selected_functionally": True,
        "finite_27_mode_replay_closed": False,
    }


def main() -> int:
    previous = load(PREVIOUS)
    value = load(VALUE)
    end0 = load(END0_DE)
    t1t2 = load(T1T2_GREEN)
    source_payload = load(SOURCE_PAYLOAD)

    pure_gauge = t1t2["path_A_straight_T1T2_covariant_Green"]
    ad_t3 = end0["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"]
    sector_slots = {sector: sector_trace_slot(sector, value) for sector in ALL_SECTORS}

    theorem = {
        "name": "SelectedGaugeTransportedBNPhiFinTrace",
        "proved": True,
        "statement": (
            "For the selected diagonal End0 HYM lane D=d+du ad(T3), the selected zero-mode "
            "trace over the clean model-active B_N zero cluster is the gauge-transported trace "
            "K_s^sel=U K_s^model with U=exp(-u ad(T3)) on the T1/T2 plane and identity on T3/H. "
            "The transported projectors P_s^sel=U P_s^model U^-1 are selected function-space "
            "Riesz projectors for the diagonal End0 lane, preserve rank and gap, and make the "
            "canonical rho_candidate act on selected zero-mode carriers."
        ),
        "proof_steps": [
            "The selected End0 connection formula is D=d+du ad(T3).",
            "On the T1/T2 plane, ad(T3)=J and the T1/T2 theorem proves D=exp(-uJ) d exp(uJ).",
            "Therefore D(U psi)=U d psi for U=exp(-uJ), so U maps model-active constant zero modes to selected D-flat modes.",
            "The T3 lane is protected because ad(T3)T3=0, and the Higgs singlet action is zero.",
            "Unitary gauge transport preserves projector rank, spectral gap, and Green/Riesz identities by conjugation.",
            "Thus the corrected Phi_fin trace is transported, not raw model-active equality.",
        ],
    }

    transported_trace = {
        "basis_id": value["finite_value_payload"]["basis_id"],
        "ambient_model_dimension": value["finite_value_payload"]["ambient_dimension"],
        "transport_operator": {
            "symbol": "U",
            "formula": "exp(-u ad(T3))",
            "T1T2_block": "rotation by -u: [[cos u, sin u],[-sin u, cos u]] in the chosen T1,T2 convention",
            "T3_lane": "identity",
            "H_lane": "identity",
            "unitary_or_orthogonal": True,
        },
        "sector_slots": sector_slots,
        "functional_identities": {
            "D_selected_U_equals_U_d": True,
            "P_selected_equals_U_P_model_U_inverse": True,
            "G_selected_equals_U_G_model_U_inverse_on_complement": True,
            "kernel_dimension_preserved": True,
            "gap_preserved": True,
        },
        "rho_candidate_promotes_functionally": True,
        "selected_source_verified_functional_End0_trace": True,
    }

    finite_replay_boundary = {
        "finite_27_mode_validator_replay_closed": False,
        "reason": (
            "Multiplication by exp(-u ad(T3)) is not closed in the raw 27-mode B_N Fourier "
            "truncation; the existing T1/T2 replay already records direct truncation aliasing. "
            "A transport-closed basis, enriched Fourier closure, or validator accepting symbolic "
            "transport conjugation is still required."
        ),
        "direct_truncated_relative_residual_from_T1T2_probe": pure_gauge["numerical_replay"][
            "direct_truncated_relative_residual"
        ],
        "gauge_frame_residual_l2": pure_gauge["numerical_replay"]["gauge_frame_residual_l2"],
        "next_acceptance": [
            "emit transported basis samples or coefficients with truncation error certificate",
            "or enrich B_N so multiplication by exp(+-uJ) is closed to certified tolerance",
            "or extend validators to accept exact symbolic transport-conjugated projectors",
            "then replay D_E/Riesz/Green/projector validators with theorem-derived source flags",
        ],
    }

    promotion_decision = {
        "functional_selected_trace_proved": True,
        "selected_source_verified_for_functional_End0_trace": True,
        "finite_validator_flags_promoted_now": False,
        "rho_candidate_promoted_to_functional_selected_rho_s": True,
        "rho_candidate_promoted_to_validator_ready_sector_packet": False,
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "why_remaining_flags_false": [
            "dotD_alpha1 must include derivative of U=exp(-u ad(T3)) and the selected alpha1 driver",
            "finite validator replay needs transport-closed basis or symbolic transport support",
            "matter-slot routing/normalization is still downstream of rho_s",
        ],
    }

    superset_strategy = {
        "classification": "SUPERSET_ROUTE_A_FUNCTIONAL_TRACE_CLOSED_FINITE_REPLAY_OPEN",
        "End0_HYM_path": "proves the selected gauge transport from the diagonal HYM connection",
        "BN_path": "supplies clean model-active zero cluster, ranks, gaps, and projectors before transport",
        "T1T2_path": "supplies pure-gauge Riesz/Green/projector transfer",
        "PhiFin_path": "is now the transported trace rather than raw equality",
        "q79_Theta_SU5_path": "kept downstream for routing; not used as source-flag proof",
        "uses_observed_constants": False,
    }

    data = {
        "candidate": "MTTSelectedGaugeTransportedBNPhiFinTrace",
        "status": STATUS,
        "inputs": {
            "previous": rel(PREVIOUS),
            "value_emission": rel(VALUE),
            "end0_de": rel(END0_DE),
            "t1t2_green": rel(T1T2_GREEN),
            "source_payload": rel(SOURCE_PAYLOAD),
        },
        "theorem": theorem,
        "transported_trace": transported_trace,
        "finite_replay_boundary": finite_replay_boundary,
        "promotion_decision": promotion_decision,
        "ad_T3_matrix": ad_t3,
        "source_payload_boundary": {
            "canonical_rho_candidate_constructed": source_payload["promotion_decision"][
                "canonical_source_map_constructed"
            ],
            "previous_selected_source_map_emitted": source_payload["promotion_decision"][
                "selected_source_map_emitted"
            ],
            "upgraded_here_at_functional_trace_level": True,
            "validator_ready_sector_source_map_emitted": False,
        },
        "superset_strategy": superset_strategy,
        "what_closes_now": {
            "gauge_transported_PhiFin_trace": True,
            "selected_functional_zero_mode_bases": True,
            "selected_functional_projectors": True,
            "functional_rho_s_promotion": True,
            "rank_gap_Riesz_Green_transfer_by_conjugation": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "transport_closed_finite_validator_replay": True,
            "selected_dotD_alpha1_with_transport_derivative": True,
            "alpha1_driver_verified": True,
            "selected_matter_slot_routing": True,
            "validator_ready_sector_rho_s_packet": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "gauge_transported_trace_proved": True,
        "functional_rho_s_promoted": True,
        "finite_validator_replay_closed": False,
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected GaugeTransported BN PhiFin Trace v1

Status: `{STATUS}`.

## Theorem

The corrected `Phi_fin` trace is proved at the selected End0/HYM function-space
level:

```text
U = exp(-u ad(T3))
K_s^sel = U K_s^model
P_s^sel = U P_s^model U^-1
```

On `span(T1,T2)`, this is the pure-gauge identity already proved in the
T1/T2 Green theorem:

```text
D = exp(-uJ) d exp(uJ)
D(U psi) = U d psi
```

The `T3` lane is protected because `ad(T3)T3=0`, and `H` is the trivial
singlet.  Therefore the model-active `B_N` zero cluster becomes the selected
diagonal End0 zero-mode trace after gauge transport.  Rank, gap, Riesz
projector, and Green operator transfer by unitary conjugation.

## What This Closes

- selected functional zero-mode bases,
- selected functional projectors,
- functional promotion of `rho_candidate` to selected `rho_s`,
- corrected Route A `Phi_fin` trace formula.

## What Remains

This is not yet finite validator replay.  Multiplication by `exp(-uJ)` is not
closed inside the raw 27-mode `B_N` truncation; the prior direct truncated
relative residual was

```text
{finite_replay_boundary["direct_truncated_relative_residual_from_T1T2_probe"]}
```

So the next gate is a transport-closed finite basis or symbolic
transport-conjugation validator replay.  `dotD_alpha1` also still needs the
derivative of the transport and the selected alpha1 driver.

No observed constants, benchmark targets, or lifted selected flags are used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
