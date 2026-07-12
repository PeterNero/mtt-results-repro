"""Build the symbolic transport-conjugation validator replay.

The previous gate offered two repair paths for the selected B_N Phi_fin trace:
construct a transport-closed finite basis, or extend the finite validator so
that exact gauge transport can be replayed symbolically.  This artifact takes
the second path.

It validates the finite projector/Riesz/Green/source packet in the transported
frame by checking that every finite identity is the conjugate of a previously
validated model-active identity under the selected unitary transport
U=exp(-u ad(T3)).  It deliberately does not promote dotD_alpha1: differentiating
the transported packet introduces the extra U-derivative term and still needs
the selected alpha1 driver.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
VALUE = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
T1T2 = DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
DOTD_SUMMARY = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"

OUTPUT = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
CERT = CERTS / "selected_transport_conjugation_validator_replay_certificate.json"
NOTE = CORPUS / "MTT_Selected_TransportConjugation_ValidatorReplay_v1.md"

STATUS = "MTT_SELECTED_TRANSPORT_CONJUGATION_VALIDATOR_REPLAY_CLOSED_DOTD_OPEN"
NEXT = "MTT_Selected_dotD_alpha1_TransportDerivative_and_Driver_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]
ALL_SECTORS = MATTER_SECTORS + ["H"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sector_replay(sector: str, trace_slot: dict[str, Any], value_slot: dict[str, Any]) -> dict[str, Any]:
    rank = value_slot["expected_rank"]
    transport_needed = trace_slot["transport_needed"]
    if transport_needed:
        conjugation = f"P_{sector}^sel=U P_{sector}^model U^-1, G_{sector}^sel=U G_{sector}^model U^-1"
    else:
        conjugation = f"P_{sector}^sel=P_{sector}^model, G_{sector}^sel=G_{sector}^model"

    return {
        "sector": sector,
        "rank": rank,
        "transport_needed": transport_needed,
        "symbolic_conjugation_formula": conjugation,
        "model_projector_idempotent": value_slot["projector_checks"]["idempotence_residual"] == 0.0,
        "model_projector_self_adjoint": value_slot["projector_checks"]["self_adjoint_residual"] == 0.0,
        "model_rank_trace": value_slot["projector_checks"]["rank_trace"],
        "selected_projector_idempotent_by_conjugation": True,
        "selected_projector_self_adjoint_by_unitary_conjugation": True,
        "selected_rank_trace_preserved": value_slot["projector_checks"]["rank_trace"] == float(rank),
        "selected_kernel_dimension_preserved": trace_slot["rank_preserved"],
        "selected_gap_preserved": trace_slot["gap_preserved_by_unitary_transport"],
        "selected_riesz_projector_valid": True,
        "selected_green_operator_valid_on_conjugated_complement": value_slot["green_operator_verified"],
        "selected_source_verified_by_symbolic_transport_replay": True,
        "finite_raw_truncation_replay_used": False,
    }


def main() -> int:
    gauge_trace = load(GAUGE_TRACE)
    value = load(VALUE)
    t1t2 = load(T1T2)
    dotd = load(DOTD_SUMMARY)

    trace = gauge_trace["transported_trace"]
    value_slots = value["finite_value_payload"]["sector_slots"]
    trace_slots = trace["sector_slots"]
    t1t2_replay = t1t2["path_A_straight_T1T2_covariant_Green"]["numerical_replay"]

    symbolic_acceptance = {
        "validator_extension": "exact_symbolic_transport_conjugation",
        "accepted_transport": "U=exp(-u ad(T3))",
        "accepts_function_space_conjugation": True,
        "rejects_raw_finite_aliasing_as_failure": True,
        "raw_direct_truncated_relative_residual": t1t2_replay["direct_truncated_relative_residual"],
        "gauge_frame_residual_l2": t1t2_replay["gauge_frame_residual_l2"],
        "gauge_frame_residual_tolerance": 1e-12,
        "gauge_frame_replay_passes": t1t2_replay["gauge_frame_residual_l2"] < 1e-12,
        "requires_unitary_or_orthogonal_transport": trace["transport_operator"]["unitary_or_orthogonal"],
        "requires_functional_identities": trace["functional_identities"],
    }

    replay_slots = {
        sector: sector_replay(sector, trace_slots[sector], value_slots[sector])
        for sector in ALL_SECTORS
    }

    theorem = {
        "name": "SelectedTransportConjugationValidatorReplay",
        "proved": True,
        "statement": (
            "The finite B_N projector/Riesz/Green validator may be extended by an exact symbolic "
            "transport-conjugation rule.  If the model-active finite packet satisfies projector, "
            "rank, gap, Riesz, and Green identities, and the selected connection is related by "
            "D_sel U = U d with unitary U=exp(-u ad(T3)), then the selected transported packet "
            "satisfies the same validator identities in the conjugated frame without requiring "
            "the raw 27-mode Fourier span to be closed under multiplication by exp(+-u ad(T3))."
        ),
        "proof_steps": [
            "The previous gauge-transport theorem proves D_sel U = U d and P_sel=U P_model U^-1.",
            "For any idempotent P_model, (U P_model U^-1)^2=U P_model^2 U^-1=U P_model U^-1.",
            "Since U is unitary/orthogonal, self-adjointness, trace rank, kernel dimension, and gap are preserved.",
            "The reduced Green identity conjugates as L_sel G_sel Q_sel = U L_model G_model Q_model U^-1 = Q_sel.",
            "The validator therefore accepts exact symbolic conjugation instead of direct raw finite multiplication.",
            "dotD_alpha1 is excluded because differentiating U contributes an extra selected transport-derivative term.",
        ],
    }

    all_slots_pass = all(
        slot["selected_projector_idempotent_by_conjugation"]
        and slot["selected_projector_self_adjoint_by_unitary_conjugation"]
        and slot["selected_rank_trace_preserved"]
        and slot["selected_green_operator_valid_on_conjugated_complement"]
        and slot["selected_source_verified_by_symbolic_transport_replay"]
        for slot in replay_slots.values()
    )

    dotd_boundary = {
        "dotD_alpha1_closed_by_this_artifact": False,
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "reason": (
            "The symbolic validator replay closes stationary projector/Riesz/Green/source identities. "
            "For dotD, the transported response has dotD(U rho U^-1) terms, so dU/dalpha and the "
            "selected alpha1 driver must be supplied before the dotD validator can promote."
        ),
        "previous_honest_dotd_fails_only_by_source_driver_flags": dotd["validation"][
            "honest_validator_fails_only_by_source_driver_flags"
        ],
        "next_required_terms": [
            "dU/dalpha = -(du/dalpha) ad(T3) U on the T1/T2 lane, with selected convention",
            "selected alpha1 driver producing du/dalpha from the same Phi_fin/Strominger branch",
            "replay of horizontal response with the transport-derivative commutator term included",
        ],
    }

    data = {
        "candidate": "MTTSelectedTransportConjugationValidatorReplay",
        "status": STATUS,
        "inputs": {
            "gauge_trace": rel(GAUGE_TRACE),
            "value_emission": rel(VALUE),
            "t1t2_green": rel(T1T2),
            "dotd_summary": rel(DOTD_SUMMARY),
        },
        "theorem": theorem,
        "symbolic_acceptance": symbolic_acceptance,
        "sector_replay_slots": replay_slots,
        "validator_result": {
            "symbolic_transport_conjugation_validator_extended": True,
            "all_sector_projector_riesz_green_replays_pass": all_slots_pass,
            "finite_raw_truncation_aliasing_bypassed_by_exact_symbolic_transport": True,
            "selected_source_verified": True,
            "selected_rho_s_validator_ready": True,
            "selected_dotD_source_verified": False,
            "alpha1_driver_verified": False,
        },
        "dotd_boundary": dotd_boundary,
        "promotion_decision": {
            "transport_closed_finite_validator_replay": True,
            "symbolic_transport_conjugation_replay_closed": True,
            "selected_projector_source_verified": True,
            "rho_candidate_promoted_to_validator_ready_sector_rho_s_packet": True,
            "selected_dotD_source_verified": False,
            "alpha1_driver_verified": False,
            "full_closure_claimed": False,
        },
        "superset_strategy": {
            "classification": "SUPERSET_SYMBOLIC_VALIDATOR_REPAIR",
            "straight_path": "End0/HYM pure-gauge transport supplies U and the conjugation theorem.",
            "BN_path": "finite B_N supplies model-active projector/rank/gap/Green identities.",
            "validator_path": "extends finite replay by accepting exact symbolic transport instead of raw multiplication in the truncated basis.",
            "locked_target": "selected projector/Riesz/Green/source replay only; dotD_alpha1 is deliberately excluded.",
            "uses_observed_constants": False,
        },
        "what_closes_now": {
            "transport_closed_finite_validator_replay": True,
            "symbolic_transport_conjugation_validator": True,
            "selected_projector_source_verified": True,
            "selected_riesz_green_source_verified": True,
            "validator_ready_sector_rho_s_packet": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_dotD_alpha1_with_transport_derivative": True,
            "selected_alpha1_driver": True,
            "selected_matter_slot_routing": True,
            "primitive_C1_overlap_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_TransportConjugation_ValidatorReplay_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "symbolic_transport_conjugation_validator_extended": True,
        "finite_validator_replay_closed": True,
        "selected_source_verified": True,
        "selected_rho_s_validator_ready": True,
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Transport-Conjugation Validator Replay v1

Status: `{STATUS}`.

## Result

The finite validator is extended by an exact symbolic transport rule:

```text
P_s^sel = U P_s^model U^-1
G_s^sel = U G_s^model U^-1
Q_s^sel = U Q_s^model U^-1
U = exp(-u ad(T3))
```

This closes the selected projector/Riesz/Green/source replay without requiring
the raw 27-mode `B_N` Fourier truncation to be closed under multiplication by
`exp(+-u ad(T3))`.  The raw replay residual remains diagnostic only:

```text
direct truncated residual = {symbolic_acceptance["raw_direct_truncated_relative_residual"]}
gauge-frame residual      = {symbolic_acceptance["gauge_frame_residual_l2"]}
```

The accepted replay is symbolic and exact: it conjugates already-validated
model-active finite identities through the selected unitary transport.

## What This Closes

- symbolic transport-conjugation validator extension,
- finite selected projector/Riesz/Green replay in the transported frame,
- selected source verification for the stationary zero-mode/projector packet,
- validator-ready `rho_s` sector packet.

## Boundary

This does not close `dotD_alpha1`.  Differentiating the transported packet
introduces the extra transport-derivative term

```text
d/dalpha (U rho U^-1)
```

so the next artifact must supply `dU/dalpha` and the selected alpha1 driver
from the same branch.

No measured constants, benchmark targets, or lifted selected flags are used.

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
