"""Build q79 Route-C Phi_fin source-identity packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SYNTHESIS = CERTS / "q79_selected_ah_source_or_routec_residual_synthesis_certificate.json"
S0 = CERTS / "selected_phifin_s0_source_prefix_certificate.json"
FINITE_TRACE = CERTS / "selected_phifin_finite_trace_existence_certificate.json"
S1_RHOE = CERTS / "selected_phifin_s1_rhoe_trace_fill_certificate.json"
CANONICAL_TRACE = CERTS / "selected_canonical_trace_formula_source_lemma_proof_certificate.json"
GAP_LOCK = CERTS / "selected_phifin_s2_gap_layer_honest_replay_lock_certificate.json"
DOTD_ATTEMPT = CERTS / "selected_dotd_alpha1_source_and_driver_theorem_attempt_certificate.json"
DERIVATIVE_ATTEMPT = CERTS / "selected_dotd_alpha1_source_derivative_payload_attempt_certificate.json"

OUT_PACKET = DATA / "q79_routec_phifin_source_identity.candidate.json"
OUT_CERT = CERTS / "q79_routec_phifin_source_identity_certificate.json"
OUT_NOTE = CORPUS / "Q79_Selected_RouteC_FiniteEmissionMorphism_PhiFin_SourceIdentity_v1.md"

STATUS = "Q79_ROUTEC_PHIFIN_SOURCE_IDENTITY_D_E_GAP_LAYER_CLOSED_DOTD_OPEN"
NEXT = "Q79_Selected_RouteC_PhiFin_dotD_alpha1_SourceIdentity_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def local(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build_packet() -> dict[str, Any]:
    synthesis = load(SYNTHESIS)
    s0 = load(S0)
    finite_trace = load(FINITE_TRACE)
    s1 = load(S1_RHOE)
    canonical = load(CANONICAL_TRACE)
    gap_lock = load(GAP_LOCK)
    dotd = load(DOTD_ATTEMPT)
    derivative = load(DERIVATIVE_ATTEMPT)

    checks = {
        "synthesis_names_this_artifact": synthesis["best_next_artifact"]
        == "Q79_Selected_RouteC_FiniteEmissionMorphism_PhiFin_SourceIdentity_v1",
        "S0_selected_source_prefix_closed": s0["s0_closed"] is True,
        "finite_trace_existence_proved": finite_trace["theorem_proved"] is True,
        "S1_nonidentity_rhoE_trace_filled": s1["what_closes_now"][
            "S1_nonidentity_projective_rhoE_trace_filled"
        ]
        is True
        and s1["guardrails"]["claims_full_selected_payload_emitted"] is False,
        "canonical_trace_source_lemma_proved": canonical["theorem"]["proved"] is True
        and canonical["gap_layer_consequence"]["D_E_source_flags_may_be_theorem_derived"]
        is True,
        "gap_riesz_green_locked": gap_lock["locked_contract"][
            "Riesz_Green_layer_closes"
        ]
        is True
        and gap_lock["locked_contract"]["D_E_source_flags_are_theorem_derived"] is True,
        "dotD_first_variation_still_open": dotd["theorem"]["proved"] is False
        and dotd["requirements"]["R4_selected_alpha1_deformation_parameter"] is False,
        "derivative_payload_still_open": derivative["theorem"]["proved"] is False
        and derivative["derivative_payload_checks"]["D6_retarded_overlap_derivative_formula"]
        is False,
    }
    proved = all(checks.values())

    selected_source_identity = {
        "S0_selected_smooth_source": True,
        "S1_projective_rhoE_trace": "PARTIAL_NONIDENTITY_TRACE_FILLED_SOURCE_PROMOTION_OPEN",
        "S2_D_E_trace_identity": canonical["theorem"]["statement"],
        "D_E_source_flags_may_be_theorem_derived": True,
        "Riesz_Green_source_layer_closed": True,
        "basis_id": gap_lock["locked_contract"]["basis_id"],
        "basis_dimension": gap_lock["locked_contract"]["basis_dimension"],
        "selected_eta_N": gap_lock["locked_contract"]["selected_eta_N"],
        "selected_gap_lower_bound": gap_lock["locked_contract"]["selected_gap_lower_bound"],
        "selected_green_norm_bound": gap_lock["locked_contract"]["selected_green_norm_bound"],
        "zero_cluster_indices": gap_lock["locked_contract"]["zero_cluster_indices"],
        "scope": "rho_E trace plus D_E/gap/Riesz/Green source identity only",
    }

    return {
        "packet": "Q79_Selected_RouteC_FiniteEmissionMorphism_PhiFin_SourceIdentity_v1",
        "status": STATUS if proved else "Q79_ROUTEC_PHIFIN_SOURCE_IDENTITY_FAILED",
        "inputs": {
            "synthesis": local(SYNTHESIS),
            "S0_source_prefix": local(S0),
            "finite_trace_existence": local(FINITE_TRACE),
            "S1_rhoE_trace": local(S1_RHOE),
            "canonical_trace_source_lemma": local(CANONICAL_TRACE),
            "gap_layer_lock": local(GAP_LOCK),
            "dotD_source_attempt": local(DOTD_ATTEMPT),
            "dotD_derivative_attempt": local(DERIVATIVE_ATTEMPT),
        },
        "source_identity_checks": checks,
        "theorem": {
            "name": "Q79RouteCPhiFinSourceIdentityGapLayerTheorem",
            "proved": proved,
            "closure_claimed": False,
            "statement": (
                "For the selected q79/F,m=1 Route-C Phi_fin source prefix, the "
                "nonidentity projective rho_E trace, canonical 27-mode D_E trace, "
                "and gap/Riesz/Green layer are now linked by same-source theorem "
                "data. This closes the Phi_fin source identity only through the "
                "D_E gap layer; it does not close dotD/alpha1, C1 contractions, "
                "Yukawa matrices, or full SM/no-knob closure."
            ),
        },
        "selected_source_identity": selected_source_identity,
        "what_closes_now": {
            "Phi_fin_source_identity_for_D_E_gap_layer": True,
            "D_E_source_flags_theorem_derived_for_gap_layer": True,
            "Riesz_Green_layer_closed_from_selected_gap": True,
            "identity_rhoE_smoke_rejected_for_S1": True,
            "next_blocker_reduced_to_dotD_alpha1_source_identity": True,
        },
        "what_remains_open": {
            "full_S1_rhoE_source_promotion": True,
            "selected_dotD_alpha1_source_identity": True,
            "selected_alpha1_deformation_parameter": True,
            "retarded_overlap_derivative_formula": True,
            "sector_equality_to_dotD_matrices": True,
            "primitive_C1_overlap_tensors": True,
            "A_selected_and_b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_full_S1_rhoE_promotion": False,
            "claims_selected_dotD_alpha1": False,
            "claims_selected_C1_contractions": False,
            "claims_A_selected_or_b_selected": False,
            "claims_Yukawa_or_SM_closure": False,
            "uses_lifted_selected_flags": False,
            "uses_observed_or_benchmark_inputs": False,
        },
        "verdict": {
            "source_identity_gap_layer_closed": proved,
            "full_operator_payload_closed": False,
            "next_required_artifact": NEXT,
            "why_next": (
                "The remaining gap is no longer D_E/Riesz/Green. It is the "
                "first variation: prove that the selected Phi_fin source has a "
                "selected alpha1 tangent or retarded-overlap derivative equal "
                "to the existing sector dotD matrices."
            ),
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return f"""# Q79 Selected Route-C FiniteEmissionMorphism PhiFin SourceIdentity v1

## Result

Status: `{packet["status"]}`

This closes the `Phi_fin` source identity only through the selected `D_E`
gap/Riesz/Green layer.  It does not close `dotD`, alpha1, C1, Yukawa, or full
SM/no-knob closure.

## Selected Source Identity

```json
{json.dumps(packet["selected_source_identity"], indent=2, sort_keys=True)}
```

## What Closes Now

```json
{json.dumps(packet["what_closes_now"], indent=2, sort_keys=True)}
```

## What Remains Open

```json
{json.dumps(packet["what_remains_open"], indent=2, sort_keys=True)}
```

Next: `{packet["verdict"]["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    if "--write" in sys.argv:
        OUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUT_CERT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUT_NOTE.write_text(render_note(packet), encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
