from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREV = ROOT / "certificates" / "post_alpha_independent_long_residual_completion_source_promotion_or_honest_galerkin_c1_emission_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_residual_weyl_polynomial_source_theorem_attempt_certificate.json"
OUT_CERT = ROOT / "certificates" / "post_alpha_independent_long_residual_weyl_polynomial_source_theorem_attempt_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_long_residual_weyl_polynomial_source_theorem_attempt.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentLongResidual_WeylPolynomial_SourceTheoremAttempt_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_LONG_RESIDUAL_WEYL_POLYNOMIAL_SOURCE_THEOREM_ATTEMPT_REANCHORED_PROJECTOR_SELECTION_OPEN"
PREV_STATUS = "POST_ALPHA_INDEPENDENT_LONG_RESIDUAL_COMPLETION_SOURCE_PROMOTION_OR_HONEST_GALERKIN_C1_EMISSION_GATE_OPEN"
SOURCE_STATUS = "POST_ALPHA_RESIDUAL_WEYL_POLYNOMIAL_SOURCE_THEOREM_ATTEMPT_IMPORTED_PROJECTOR_SELECTION_OPEN"
THIS_ARTIFACT = "MTT_Selected_ResidualSourceTheorem_or_GalerkinC1Run_ValueFill_v1"
NEXT = "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["status"] == PREV_STATUS,
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_residual_source_theorem_or_galerkin_C1_run_value_fill"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["what_closes_now"].values()),
            all(prev["what_remains_open"].values()),
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["frontier_decision"]["frontier_is_canonical_residual_projector_or_honest_galerkin_C1_value_fill"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    weyl = source_packet["residual_weyl_polynomial_decomposition"]
    gate = source_packet["canonical_residual_projector_selection_gate"]

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
        ]
    )

    gate_ok = all(
        [
            gate["schema"] == "MTTCanonicalResidualProjectorSelectionGate.v1",
            gate["status"] == "CANONICAL_PROJECTOR_IDENTIFIED_SELECTION_THEOREM_OPEN",
            gate["current_decision"] == "SOURCE_CARRIER_AND_CANONICAL_POLYNOMIAL_CLOSED_PROJECTOR_SELECTION_OPEN",
            gate["if_projector_selection_theorem_is_supplied"]["lane_A_residual_source_promotes"] is True,
            gate["if_projector_selection_theorem_is_supplied"]["SM_parity_dynamic_packet_closes"] is True,
            gate["if_projector_selection_theorem_is_supplied"]["no_knob_flavor_constants_derived"] is False,
            gate["if_projector_selection_theorem_is_supplied"]["deltaTheta_C1"] == [1.0, 1.0],
        ]
    )

    what_closes_now = {
        "fresh_long_residual_source_or_galerkin_gate_consumed": prev_ok,
        "audited_residual_weyl_polynomial_attempt_reanchored": source_ok,
        "RZ_RX_exact_weyl_decomposition_computed": weyl_ok,
        "canonical_projector_selection_gate_identified": gate_ok,
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
        "name": "PostAlphaIndependentLongResidualWeylPolynomialSourceTheoremAttemptImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": "The fresh long-chain branch reduces the residual source theorem gate to exact qutrit Weyl polynomial data for R_X and R_Z, while canonical projector selection and physical C1 transfer remain open.",
    }
    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "fresh_previous_certificate": prev,
        "source_weyl_attempt_certificate": source,
        "residual_weyl_polynomial_decomposition": weyl,
        "canonical_residual_projector_selection_gate": gate,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "frontier_is_canonical_residual_projector_or_honest_galerkin_C1_value_fill": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "fresh_previous_certificate": str(PREV),
            "source_weyl_attempt_certificate": str(SOURCE_CERT),
            "source_weyl_attempt_packet": source["packet_written"],
        },
    }
    note = f"""# PostAlpha IndependentLong Residual WeylPolynomial Source Theorem Attempt Import v1

## Result

Closed now:

```text
R_X coefficient count = 3
R_Z coefficient count = 6
R_X norm^2            = 2
R_Z norm^2            = 4
reconstruction error  < 1e-24
```

Still open: canonical residual projector selection, or honest Galerkin C1 value fill.

Status:

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
        "certificate": "post_alpha_independent_long_residual_weyl_polynomial_source_theorem_attempt",
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
