from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_residual_completion_source_promotion_or_honest_galerkin_c1_emission_certificate.json"
SLUG = "selected_residual_weylpolynomial_source_theorem_attempt"
SM_CERT = SM_ROOT / "certificates" / f"{SLUG}_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / f"{SLUG}.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / SLUG
WEYL_PACKET = SM_DIR / "residual_weyl_polynomial_decomposition.packet.json"
PROJECTOR_GATE = SM_DIR / "canonical_residual_projector_selection_gate.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_residual_weyl_polynomial_source_theorem_attempt_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_residual_weyl_polynomial_source_theorem_attempt.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_Residual_WeylPolynomial_Source_Theorem_Attempt_Import_v1.md"

STATUS = "POST_ALPHA_RESIDUAL_WEYL_POLYNOMIAL_SOURCE_THEOREM_ATTEMPT_IMPORTED_PROJECTOR_SELECTION_OPEN"
NEXT = "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    weyl = load(WEYL_PACKET)
    projector_gate = load(PROJECTOR_GATE)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_residual_source_theorem_or_galerkin_C1_run_value_fill"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_ResidualSourceTheorem_or_GalerkinC1Run_ValueFill_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_Residual_WeylPolynomial_Source_Theorem_Attempt_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["SM_parity_dynamic_packet_closure_claimed"] is False,
            cert["no_knob_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "ResidualWeylPolynomialReductionTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["Lane_A_promoted"] is False,
            candidate["promotion_decision"]["canonical_residual_projector_promoted"] is False,
            candidate["promotion_decision"]["residual_weyl_polynomial_selected_as_dynamic_response"] is False,
            candidate["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["no_knob_flavor_constants_closed"] is False,
        ]
    )

    weyl_ok = all(
        [
            weyl["schema"] == "MTTResidualWeylPolynomialDecomposition.v1",
            weyl["status"] == "EXACT_LOW_DEGREE_WEYL_POLYNOMIAL_DECOMPOSITION_COMPUTED",
            weyl["source_level_weyl_carrier_selected"] is True,
            weyl["static_source_selector_selected"] is True,
            weyl["active_shift_selected"] is True,
            weyl["observed_data_used"] is False,
            weyl["target_fitting_used"] is False,
            weyl["decompositions"]["R_X"]["coefficient_count"] == 3,
            weyl["decompositions"]["R_Z"]["coefficient_count"] == 6,
            weyl["decompositions"]["R_X"]["norm_sq"] == 2.0,
            weyl["decompositions"]["R_Z"]["norm_sq"] == 4.0,
            weyl["decompositions"]["R_X"]["reconstruction_error_norm_sq"] < 1e-24,
            weyl["decompositions"]["R_Z"]["reconstruction_error_norm_sq"] < 1e-24,
            weyl["exact_polynomial_form"]["R_X"] == "(1/3) I + (1/3) X - (2/3) X^2",
            "(2/3) Z" in weyl["exact_polynomial_form"]["R_Z"],
        ]
    )

    projector_gate_ok = all(
        [
            projector_gate["schema"] == "MTTCanonicalResidualProjectorSelectionGate.v1",
            projector_gate["status"] == "CANONICAL_PROJECTOR_IDENTIFIED_SELECTION_THEOREM_OPEN",
            projector_gate["current_decision"]
            == "SOURCE_CARRIER_AND_CANONICAL_POLYNOMIAL_CLOSED_PROJECTOR_SELECTION_OPEN",
            projector_gate["if_projector_selection_theorem_is_supplied"]["lane_A_residual_source_promotes"] is True,
            projector_gate["if_projector_selection_theorem_is_supplied"]["SM_parity_dynamic_packet_closes"] is True,
            projector_gate["if_projector_selection_theorem_is_supplied"]["no_knob_flavor_constants_derived"] is False,
            projector_gate["if_projector_selection_theorem_is_supplied"]["A_selected_available"] is True,
            projector_gate["if_projector_selection_theorem_is_supplied"]["b_selected_available"] is True,
            projector_gate["if_projector_selection_theorem_is_supplied"]["deltaTheta_C1"] == [1.0, 1.0],
            "Weyl carrier Z/X is selected at source level" in projector_gate["what_is_now_canonical"],
            "the C1 transfer functor applying that residual projector as physical dynamic response"
            in projector_gate["what_is_not_yet_selected"],
        ]
    )

    what_closes_now = {
        "previous_residual_promotion_gate_consumed": prev_ok,
        "residual_weyl_polynomial_reduction_imported": imported_ok,
        "RZ_RX_exact_weyl_decomposition_computed": weyl_ok,
        "canonical_projector_selection_gate_identified": projector_gate_ok,
    }

    what_remains_open = {
        "canonical_residual_projector_selection_theorem": True,
        "selected_PhiFinC1_transfer_functor_on_residual_polynomial": True,
        "honest_selected_Galerkin_C1_value_run": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "SM_parity_dynamic_packet_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_promote_Lane_A": True,
        "does_not_promote_weyl_polynomial_as_dynamic_response": True,
        "does_not_promote_canonical_projector": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaResidualWeylPolynomialSourceTheoremAttemptImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The residual source theorem gate is reduced to a canonical Weyl-polynomial "
            "problem: R_X and R_Z decompose exactly in the selected qutrit Weyl basis. "
            "This closes source-carrier compression but leaves open the theorem that "
            "Phi_fin^C1 applies the canonical residual projector as physical dynamic response."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_candidate_summary": {
            "status": candidate["status"],
            "theorem": candidate["theorem"],
            "promotion_decision": candidate["promotion_decision"],
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "residual_weyl_polynomial_decomposition": weyl,
        "canonical_residual_projector_selection_gate": projector_gate,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "exact_named_previous_artifact_not_present_but_specialized_continuation_imported": True,
            "frontier_is_canonical_residual_projector_or_honest_galerkin_C1_value_fill": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "residual_weyl_polynomial_decomposition": str(WEYL_PACKET),
            "canonical_residual_projector_selection_gate": str(PROJECTOR_GATE),
        },
    }

    note = f"""# PostAlpha Residual WeylPolynomial Source Theorem Attempt Import v1

## Result

The residual source gate is compressed to exact qutrit Weyl polynomials:

```text
R_X = (1/3) I + (1/3) X - (2/3) X^2
R_Z = (2/3) I + (2/3) Z - (1/3) X - (1/3) X^2
      + (e^(i*pi/3)/3) Z X + (e^(-i*pi/3)/3) Z X^2
```

Closed now:

```text
R_X Weyl coefficient count = 3
R_Z Weyl coefficient count = 6
R_X norm^2                 = 2
R_Z norm^2                 = 4
```

Still open: the selected physical C1 transfer functor must apply the canonical residual projector, or an honest Galerkin C1 value run must replace it.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_residual_weyl_polynomial_source_theorem_attempt",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
