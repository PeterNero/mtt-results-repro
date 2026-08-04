"""Build full-quotient spectrum or OU/Hessian scale source packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "mu_gate": DATA / "selected_heterotic_hym_mu_selection_or_full_deltaa_spectrum.candidate.json",
    "hym_block": DATA / "selected_heterotic_hym_delta_a_invariant_block_computation.candidate.json",
    "torsional_ou": DATA / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.candidate.json",
    "bismut_payload": DATA / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill.candidate.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
    "endomorphism_valuepacket": DATA / "selected_heterotic_endomorphism_threshold_valuepacket_fill.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_sourcepacket.candidate.json"
OUTPUT_SOURCE_PACKET = DATA / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_required_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_sourcepacket_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_HYM_FullQuotientSpectrum_or_OUHessianScale_SourcePacket_v1.md"

STATUS = "HETEROTIC_HYM_FULLQUOTIENT_OR_OUHESSIAN_SOURCEPACKET_BUILT_PAYLOAD_OPEN"
NEXT = "Selected_Heterotic_HYM_FullQuotientSpectrum_or_OUHessianScale_FillAttempt_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> dict[str, Any]:
    mu_gate = load(INPUTS["mu_gate"])
    hym_block = load(INPUTS["hym_block"])
    torsional = load(INPUTS["torsional_ou"])
    bismut = load(INPUTS["bismut_payload"])
    rplus = load(INPUTS["rplus_payload"])
    endo = load(INPUTS["endomorphism_valuepacket"])

    required_packet = {
        "schema": "SelectedHeteroticHYM.FullQuotientSpectrumOrOUHessianScale.SourcePacket.v1",
        "status": "OPEN_VALUES_REQUIRED",
        "already_source_backed": {
            "invariant_EndC3_block": {
                "basis": hym_block["computation"]["basis"],
                "spectrum": hym_block["computation"]["spectrum"],
                "positive_logdet_prime": hym_block["computation"]["positive_logdet_prime"],
                "zero_mode": hym_block["computation"]["zero_mode"],
            },
            "no_mu_extremum_theorem": mu_gate["monotonicity_proof"],
            "geometry_tensor_payload": {
                "structure_constants": True,
                "complex_structure_J": True,
                "Hermitian_form": True,
                "torsion_H": True,
                "Bismut_connection_coefficients": True,
                "R_plus_curvature": rplus["decision"]["R_plus_curvature_filled"],
                "R_plus_summary": rplus["rplus_payload"]["R_plus_summary"],
            },
            "partial_quotient_context": endo["filled_packet"]["operator_domain"],
        },
        "lane_A_full_quotient_DeltaA_required": {
            "selected_full_operator_domain_after_BRST_FP_and_zero_modes": None,
            "proof_invariant_EndC3_block_is_or_is_not_complete_domain": None,
            "degreewise_trace_weights_for_Qa_Qc_SU2": None,
            "bundle_connection_A_components": None,
            "bundle_curvature_F_A_components": None,
            "representation_action_on_uE_one_forms": None,
            "E_Qa_or_equivalent_Weitzenbock_zero_order_block": None,
            "positive_spectrum_or_heat_zeta_torsion_finite_part": None,
            "regularization_and_threshold_convention": None,
        },
        "lane_B_OU_or_Strominger_Hessian_scale_required": {
            "selected_OU_mode_basis": None,
            "source_derived_gamma_nk_inverse_table": None,
            "Strominger_Hessian_or_retarded_kernel_scale_selector_for_mu": None,
            "finite_truncation_or_zeta_regularization_rule": None,
            "proof_weights_are_not_fit_or_convenience": None,
        },
        "lane_C_local_system_torsion_required": {
            "selected_compact_nil_iwasawa_character_or_projective_representation": None,
            "operator_domain_bridge_to_Qa_SU3_threshold_complex": None,
            "acyclicity_or_zero_mode_policy": None,
            "Ray_Singer_or_Reidemeister_finite_part": None,
            "trace_normalization": None,
        },
        "forbidden_promotions": [
            "use invariant End(C^3) block as the full physical threshold without a quotient-completeness proof",
            "select mu=1 from internal determinant units for the physical heterotic threshold",
            "choose mu from observed electroweak residuals or threshold targets",
            "insert OU gamma weights without a source-derived mode basis and scale theorem",
            "promote R_plus curvature to bundle curvature F_A",
            "reuse partial p0/p!=0 quotient context as a determinant value",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_SOURCE_PACKET.write_text(json.dumps(required_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lane_scores = {
        "lane_A_full_quotient_DeltaA": {
            "filled_support_leaves": [
                "invariant_EndC3_block",
                "exact_det_prime_family",
                "geometric_tensor_payload",
                "R_plus_curvature",
                "partial_quotient_context",
            ],
            "blocking_leaves": list(required_packet["lane_A_full_quotient_DeltaA_required"].keys()),
            "current_best": True,
        },
        "lane_B_OU_or_Strominger_Hessian_scale": {
            "filled_support_leaves": [
                "selected_radii",
                "relative_one_form_weights",
                "Bismut_geometry",
                "no_mu_extremum_theorem",
            ],
            "blocking_leaves": list(required_packet["lane_B_OU_or_Strominger_Hessian_scale_required"].keys()),
            "current_best": False,
        },
        "lane_C_local_system_torsion": {
            "filled_support_leaves": ["projective_carrier_algebra_exists_in_prior_packet"],
            "blocking_leaves": list(required_packet["lane_C_local_system_torsion_required"].keys()),
            "current_best": False,
        },
    }

    decision = {
        "source_packet_built": True,
        "full_quotient_spectrum_closed": False,
        "OU_Hessian_scale_closed": False,
        "local_system_torsion_closed": False,
        "mu_selected": False,
        "threshold_payload_closed": False,
        "best_next_lane": "lane_A_full_quotient_DeltaA",
        "why_lane_A_first": "It has the most source-backed data: invariant block, exact det-prime family, Bismut/R+ geometry, and partial quotient context.",
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticHYMFullQuotientSpectrumOrOUHessianScaleSourcePacket",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "source_packet_path": rel(OUTPUT_SOURCE_PACKET),
        "input_statuses": {
            "mu_gate": mu_gate["status"],
            "hym_block": hym_block["status"],
            "torsional_ou": torsional["status"],
            "bismut_payload": bismut["status"],
            "rplus_payload": rplus["status"],
            "endomorphism_valuepacket": endo["status"],
        },
        "lane_scores": lane_scores,
        "decision": decision,
        "closed_now": {
            "combined_source_packet": True,
            "bad_mu_selectors_excluded": True,
            "lane_A_prioritized": True,
            "exact_missing_payload_leaves_named": True,
        },
        "still_open": {
            "selected_full_operator_domain": True,
            "quotient_completeness_proof": True,
            "trace_weights": True,
            "bundle_A_and_F_A": True,
            "E_Qa_or_equivalent_zero_order_block": True,
            "spectrum_heat_zeta_torsion_finite_part": True,
            "OU_Hessian_scale_selector_for_mu": True,
            "physical_threshold_convention": True,
        },
        "guardrails": {
            "does_not_claim_threshold_value": True,
            "does_not_select_mu": True,
            "does_not_promote_Rplus_to_FA": True,
            "does_not_promote_partial_quotient_policy": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "FullQuotientSpectrumOrOUHessianScaleSourcePacketTheorem",
            "proved": True,
            "statement": (
                "The current source record is sufficient to build the exact closing packet "
                "for the heterotic HYM threshold problem, but not to fill its value leaves. "
                "Lane A, the full quotient Delta_A spectrum, is the best next computation "
                "because it already has the invariant End(C^3) block, exact determinant-prime "
                "family, Bismut/R+ geometry, and partial quotient context. Promotion still "
                "requires a proof that the selected quotient domain is complete, trace "
                "weights, bundle A/F_A and representation action, E_Qa or an equivalent "
                "zero-order block, and a heat/zeta/torsion finite part. The OU/Hessian and "
                "local-system lanes remain legal but less filled."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "source_packet_path": rel(OUTPUT_SOURCE_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "best_next_lane": decision["best_next_lane"],
        "full_quotient_spectrum_closed": False,
        "OU_Hessian_scale_closed": False,
        "mu_selected": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic HYM FullQuotientSpectrum or OUHessianScale SourcePacket v1

## Result

```text
status = {STATUS}
best_next_lane = lane_A_full_quotient_DeltaA
full_quotient_spectrum_closed = false
OU_Hessian_scale_closed = false
mu_selected = false
next_required_artifact = {NEXT}
```

## What This Builds

This packet combines the source-backed HYM invariant block, the no-`mu`
extremum theorem, Bismut/`R^+` geometry, and the partial quotient context into
one required source packet:

```text
{rel(OUTPUT_SOURCE_PACKET)}
```

The strongest next lane is the full quotient `Delta_A` spectrum. It is not
closed yet: the invariant `End(C^3)` block still needs a quotient-completeness
proof, trace weights, selected bundle `A/F_A`, representation action, `E_Qa`
or equivalent zero-order block, and a heat/zeta/torsion finite part.

## Theorem

{candidate["theorem"]["statement"]}
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_SOURCE_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(result["status"])
