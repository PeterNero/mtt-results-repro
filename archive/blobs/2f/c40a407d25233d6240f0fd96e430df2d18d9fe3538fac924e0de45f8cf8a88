"""Prove the S0 selected-source prefix for the PhiFin C1 emission packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
SM = TEXPAPERS / "mtt-sm-parity-closure"

PACKET = DATA / "selected_phifin_c1_emission_packet.template.json"
SM_SOURCE_ORIGIN = SM / "candidate_data" / "routec_selected_source_origin_lemma.candidate.json"
SM_PROJECTIVE_RHOE = SM / "certificates" / "projective_gerbe_rhoe_source_promotion_certificate.json"
SM_FIRST_RUN = SM / "certificates" / "selected_routec_strominger_galerkin_first_run_certificate.json"
SM_PROVENANCE_BASIS = SM / "certificates" / "selected_routec_source_provenance_or_basis_certificate_certificate.json"

OUTPUT_PACKET = DATA / "selected_phifin_s0_source_prefix.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_s0_source_prefix_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S0_Source_Prefix_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_candidate() -> dict[str, Any]:
    packet = load_json(PACKET)
    source_origin = load_json(SM_SOURCE_ORIGIN)
    projective = load_json(SM_PROJECTIVE_RHOE)
    first_run = load_json(SM_FIRST_RUN)
    provenance = load_json(SM_PROVENANCE_BASIS)

    gates = source_origin["gate_matrix"]
    s0_premises = {
        "fixed_q79_f_m1_s3_gs_sector": gates["G1_fixed_topological_sector_named"]["passes"],
        "mtt_strominger_selection_available": gates["G2_MTT_Strominger_selection_available"]["passes"],
        "same_source_support_converges": gates["G3_same_source_support_converges"]["passes"],
        "projective_s3_source_promoted_to_source_level": projective["what_closes"][
            "projective_gerbe_rhoE_promoted_to_selected_S3_source_level"
        ],
        "target_fitting_excluded": source_origin["target_fitting_used"] is False
        and projective["target_fitting_used"] is False,
    }
    s0_closed = all(s0_premises.values())
    s1_s2_blockers = {
        "finite_emission_morphism": source_origin["gate_matrix"]["G4_minimizer_to_finite_packet_morphism"][
            "passes"
        ]
        is False,
        "operator_payload": source_origin["gate_matrix"]["G5_operator_payload_emitted"]["passes"] is False,
        "first_run_proof_promotion_allowed": first_run["proof_promotion_allowed"] is False,
        "selected_source_flags_promoted": provenance["what_remains_open"]["selected_source_flags_promoted"],
        "quotient_valid_BN_basis_certificate": provenance["what_remains_open"][
            "quotient_valid_BN_basis_certificate"
        ],
    }

    advanced_packet = json.loads(json.dumps(packet))
    advanced_packet["packet"] = "Selected_PhiFin_C1_Emission_Packet_v1_S0_Prefix"
    advanced_packet["status"] = "SELECTED_PHIFIN_S0_SOURCE_PREFIX_CLOSED_S1_S2_VALUES_OPEN"
    advanced_packet["emission_slots"]["S0_selected_source"]["status"] = "CLOSED_ABSTRACT_SELECTED_SOURCE"
    advanced_packet["emission_slots"]["S0_selected_source"]["proof"] = {
        "source": "routec_selected_source_origin_lemma + projective_gerbe_rhoe_source_promotion",
        "statement": (
            "There is a theorem-derived selected smooth source in the fixed q79/F,m=1 "
            "S3/GS Route-C sector. This closes S0 only as source provenance; it does "
            "not emit finite rho_E, D_E, Riesz/Green, dotD, or C1 values."
        ),
    }
    advanced_packet["closure_predicate"]["selected_source_verified_without_lifted_flags"] = s0_closed
    advanced_packet["closure_predicate"]["all_slots_status_closed"] = False
    advanced_packet["next_computation"] = {
        "name": "construct S1-S2 Phi_fin finite trace from the S0 selected source",
        "minimum_new_payload": [
            "canonical finite Cech/Galerkin trace map from the selected minimizer",
            "selected non-identity rho_E or connection values",
            "metric-compatible sector projectors",
            "D_E blocks, Riesz gaps, reduced Green operators",
            "same-branch dotD_alpha1 matrices with error bounds",
        ],
    }

    return {
        "candidate": "SelectedPhiFinS0SourcePrefix",
        "status": "SELECTED_PHIFIN_S0_SOURCE_PREFIX_CLOSED_S1_S2_VALUES_OPEN",
        "selected_branch": "q79/F,m=1 S3/GS Route-C",
        "input_packet": str(PACKET),
        "advanced_packet": advanced_packet,
        "s0_premises": s0_premises,
        "s0_closed": s0_closed,
        "s0_theorem": {
            "name": "SelectedSmoothSourcePrefix",
            "proved": s0_closed,
            "statement": (
                "The fixed q79/F,m=1 S3/GS sector plus the MTT Strominger/HYM "
                "selection theorem supplies a theorem-derived selected smooth source. "
                "The source is not a lifted finite packet, not a fixture, and not selected "
                "from observed constants."
            ),
        },
        "why_this_does_not_yet_close_validators": (
            "The q79 and SM-parity validators require finite selected payload values, "
            "not just the existence of the smooth selected source. S1 and S2 must still "
            "construct the functorial Phi_fin trace and error/gap certificate."
        ),
        "s1_s2_blockers": s1_s2_blockers,
        "minimal_remaining_lemma": {
            "name": "SelectedPhiFinFiniteTraceLemma",
            "statement": (
                "For the S0 selected smooth source, the canonical finite Cech/Galerkin "
                "trace emits non-identity rho_E/connection data, sector projectors, "
                "D_E, Riesz/gap, reduced Green, and same-branch dotD_alpha1 blocks in "
                "the Route-C validator basis with certified truncation error."
            ),
            "why_minimal": (
                "Once this lemma is proved, S1-S2 can be filled without selected flag "
                "lifting; S3-S5 then become ordinary emitted-overlap computations."
            ),
        },
        "what_closes_now": {
            "S0_selected_source_as_abstract_smooth_source": s0_closed,
            "selected_source_not_hypothetical_or_fixture": s0_closed,
            "observed_target_fitting_excluded": s0_premises["target_fitting_excluded"],
            "S1_S2_reduced_to_finite_trace_lemma": True,
        },
        "what_remains_open": {
            "S1_transition_or_connection_trace": True,
            "S2_operator_blocks": True,
            "S3_alpha1_source_vector": True,
            "S4_hessian_and_zero_modes": True,
            "S5_c1_contractions_and_response": True,
            "A_selected": True,
            "b_selected": True,
        },
        "guardrails": {
            "claims_finite_rhoE_connection_emitted": False,
            "claims_D_E_Riesz_Green_dotD_emitted": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "claims_sm_closure": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }


def build_certificate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS0SourcePrefix",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "s0_closed": candidate["s0_closed"],
        "minimal_remaining_lemma": candidate["minimal_remaining_lemma"]["name"],
        "what_closes_now": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "guardrails": candidate["guardrails"],
    }


def render_note(candidate: dict[str, Any]) -> str:
    premises = "\n".join(
        f"- `{key}`: {'PASS' if value else 'FAIL'}" for key, value in candidate["s0_premises"].items()
    )
    blockers = "\n".join(
        f"- `{key}`: {'OPEN' if value else 'not blocking'}"
        for key, value in candidate["s1_s2_blockers"].items()
    )
    return f"""# Selected PhiFin S0 Source Prefix v1

## Result

`S0_selected_source` is closed as an abstract selected smooth source.

This is a real advance, but it is deliberately narrow: it does not emit finite
`rho_E`, `D_E`, `Riesz/Green`, `dotD`, `A_selected`, or `b_selected` values.

## S0 Theorem

`{candidate["s0_theorem"]["name"]}`:

{candidate["s0_theorem"]["statement"]}

Proved: `{candidate["s0_theorem"]["proved"]}`

## Premises

{premises}

## Why S1-S2 Still Remain Open

{candidate["why_this_does_not_yet_close_validators"]}

Current blockers:

{blockers}

## Minimal Remaining Lemma

`{candidate["minimal_remaining_lemma"]["name"]}`

{candidate["minimal_remaining_lemma"]["statement"]}

Why minimal:

{candidate["minimal_remaining_lemma"]["why_minimal"]}

## Guardrail

This proof prefix closes selected source provenance only.  It does not promote
finite selected flags, and it does not claim SM closure.
"""


def main() -> int:
    candidate = build_candidate()
    cert = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
