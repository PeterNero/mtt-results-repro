"""Attempt Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_v1."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

DERIVATIVE_PAYLOAD = DATA / "selected_dotd_alpha1_source_derivative_payload_attempt.candidate.json"
Q79_PHIFIN = Q79 / "certificates" / "q79_selected_phifin_alpha1_payload_certificate.json"
Q79_BASIS = (
    Q79 / "certificates" / "q79_routec_basis_transport_primitive_source_theorem_certificate.json"
)
Q79_WEYLPAIR = (
    Q79 / "certificates" / "q79_routec_weylpair_aselected_assembly_or_source_proof_certificate.json"
)
Q79_WEYLPAIR_SOURCE = (
    Q79 / "certificates" / "q79_routec_weylpair_source_provenance_lemma_certificate.json"
)
Q79_VALPHA_BRIDGE = (
    Q79 / "certificates" / "q79_valpha_source_origin_finite_emission_bridge_certificate.json"
)
ZERO_MODE_DOTD = Q79 / "certificates" / "selected_zero_mode_basis_dotd_interface_certificate.json"
C1_RANK = Q79 / "certificates" / "c1_alpha1_rank_lift_criterion_certificate.json"
RETARDED_UNIT_LAG = Q79 / "proof_corpus" / "Retarded_Unit_Lag_Lemma_from_Nil_Survivor_Projection_v1.md"
SCHUR_RETARDED = Q79 / "proof_corpus" / "Schur_Retarded_Coefficient_Theorem_for_CKM_q79_Lag_v1.md"

OUTPUT_PACKET = DATA / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_Attempt_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def text_contains(path: Path, needle: str) -> bool:
    return needle in path.read_text(encoding="utf-8")


def build_packet() -> dict[str, Any]:
    derivative_payload = load_json(DERIVATIVE_PAYLOAD)
    phifin = load_json(Q79_PHIFIN)
    basis = load_json(Q79_BASIS)
    weylpair = load_json(Q79_WEYLPAIR)
    weylpair_source = load_json(Q79_WEYLPAIR_SOURCE)
    valpha_bridge = load_json(Q79_VALPHA_BRIDGE)
    zero_mode = load_json(ZERO_MODE_DOTD)
    c1_rank = load_json(C1_RANK)

    retarded_kernel_transfer = {
        "ckm_nil_survivor_kernel_available": text_contains(
            RETARDED_UNIT_LAG,
            "selected kernel = raw retarded overlap followed by nil-survivor projection",
        ),
        "ckm_unit_lag_ratio_closed": text_contains(
            RETARDED_UNIT_LAG, "rho_q/kappa_q = 1"
        ),
        "schur_formula_available": text_contains(
            SCHUR_RETARDED, "rho_q   = r_u - b^T D^{-1} r_eta"
        ),
        "typed_sm_dotD_kernel_emitted": False,
        "why_not_transferable_as_proof": (
            "The CKM retarded kernel lives on the nil-survivor dyadic label "
            "selection problem.  It supplies a pattern for a Schur-reduced "
            "retarded force, but it does not emit the q79/F,m=1 B_N-sector "
            "alpha1 tangent, projector-retention derivative, or sector dotD "
            "matrix equality."
        ),
    }

    q79_source_ladder = {
        "phifin_alpha1_payload_gate": {
            "status": phifin["status"],
            "closure_claimed": phifin["closure_claimed"],
            "finite_codomain_confirmed": phifin["closed_by_this_attempt"][
                "finite_phifin_alpha1_codomain_confirmed"
            ],
            "alpha1_support_confirmed": phifin["closed_by_this_attempt"][
                "alpha1_support_and_rank_contract_confirmed"
            ],
            "selected_dotD_alpha1_derivative_open": phifin["still_open"][
                "selected_dotD_alpha1_derivative"
            ],
            "selected_payload_values_claimed": phifin["guardrails"][
                "claims_selected_phifin_alpha1_payload_values"
            ],
            "next_required_artifact": phifin["next_required_artifact"],
        },
        "basis_transport_primitive_gate": {
            "status": basis["status"],
            "closure_claimed": basis["closure_claimed"],
            "primitive_only_counterexample_closed": basis["closed_by_this_attempt"][
                "primitive_only_span_counterexample_closed"
            ],
            "same_branch_source_proof_open": basis["still_open"][
                "same_branch_source_proof_for_enriched_vertex_or_transport"
            ],
            "next_required_artifact": basis["next_required_artifact"],
        },
        "weylpair_conditional_assembly": {
            "status": weylpair["status"],
            "closure_claimed": weylpair["closure_claimed"],
            "claims_conditional_A_is_A_selected": weylpair["guardrails"][
                "claims_conditional_A_is_A_selected"
            ],
            "claims_selected_source_provenance_proved": weylpair["guardrails"][
                "claims_selected_source_provenance_proved"
            ],
            "next_required_artifact": weylpair["next_required_artifact"],
        },
        "weylpair_source_provenance": {
            "status": weylpair_source["status"],
            "closure_claimed": weylpair_source["closure_claimed"],
            "source_level_carrier_closed": weylpair_source["closed_by_this_attempt"][
                "source_level_weyl_carrier_provenance_closed"
            ],
            "selected_sector_charge_open": weylpair_source["still_open"][
                "selected_sector_charge_or_chirality_certificate"
            ],
            "selected_transfer_normalization_open": weylpair_source["still_open"][
                "selected_transfer_normalization"
            ],
            "next_required_artifact": weylpair_source["next_required_artifact"],
        },
        "valpha_finite_emission_bridge": {
            "status": valpha_bridge["status"],
            "closure_claimed": valpha_bridge["closure_claimed"],
            "same_branch_alpha1_derivative_theorem_open": valpha_bridge[
                "still_open"
            ]["same_branch_alpha1_derivative_theorem"],
        },
        "zero_mode_dotD_interface": {
            "status": zero_mode["status"],
            "closes_dotD_operator_values": zero_mode["verdict"][
                "closes_dotD_operator_values"
            ],
            "closes_zero_mode_dotD_input_contract": zero_mode["verdict"][
                "closes_zero_mode_dotD_input_contract"
            ],
        },
        "c1_alpha1_rank_lift": {
            "status": c1_rank["status"],
            "closes_C1_rank_success_test": c1_rank["verdict"][
                "closes_C1_rank_success_test"
            ],
            "closes_C1_numeric_weight": c1_rank["verdict"][
                "closes_C1_numeric_weight"
            ],
        },
    }

    transfer_checks = {
        "K0_derivative_payload_gate_is_current_next": derivative_payload["verdict"][
            "next_required_artifact"
        ]
        == "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_v1",
        "K1_ckm_retarded_kernel_pattern_available": retarded_kernel_transfer[
            "ckm_nil_survivor_kernel_available"
        ]
        and retarded_kernel_transfer["ckm_unit_lag_ratio_closed"]
        and retarded_kernel_transfer["schur_formula_available"],
        "K2_q79_phi_fin_alpha1_support_available": q79_source_ladder[
            "phifin_alpha1_payload_gate"
        ]["finite_codomain_confirmed"]
        and q79_source_ladder["phifin_alpha1_payload_gate"][
            "alpha1_support_confirmed"
        ],
        "K3_source_level_weyl_carrier_available": q79_source_ladder[
            "weylpair_source_provenance"
        ]["source_level_carrier_closed"],
        "K4_selected_sector_charge_or_chirality": False,
        "K5_selected_transfer_normalization": False,
        "K6_selected_BN_tangent_or_retarded_kernel": False,
        "K7_honest_dotD_replay_from_kernel": False,
    }

    proved = all(transfer_checks.values())
    return {
        "packet": "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_Attempt_v1",
        "status": (
            "SELECTED_ALPHA1_TANGENT_OR_RETARDED_OVERLAP_KERNEL_PROVED"
            if proved
            else "SELECTED_ALPHA1_TANGENT_OR_RETARDED_OVERLAP_KERNEL_ATTEMPT_BUILT_SECTOR_CHARGE_OPEN"
        ),
        "inputs": {
            "derivative_payload": str(DERIVATIVE_PAYLOAD.relative_to(ROOT)),
            "q79_phifin_alpha1": str(Q79_PHIFIN),
            "q79_basis_transport": str(Q79_BASIS),
            "q79_weylpair_assembly": str(Q79_WEYLPAIR),
            "q79_weylpair_source": str(Q79_WEYLPAIR_SOURCE),
            "q79_valpha_bridge": str(Q79_VALPHA_BRIDGE),
            "zero_mode_dotD": str(ZERO_MODE_DOTD),
            "c1_rank_lift": str(C1_RANK),
            "retarded_unit_lag": str(RETARDED_UNIT_LAG),
            "schur_retarded": str(SCHUR_RETARDED),
        },
        "theorem": {
            "name": "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel",
            "proved": proved,
            "statement": (
                "The selected retarded-overlap kernel or selected alpha1 "
                "tangent emits the q79/F,m=1 B_N-sector dotD derivative and "
                "therefore gives an honest no-lift dotD replay."
            ),
        },
        "transfer_checks": transfer_checks,
        "retarded_kernel_transfer": retarded_kernel_transfer,
        "q79_source_ladder": q79_source_ladder,
        "decision": {
            "retarded_ckm_kernel_is_not_enough": True,
            "basis_transport_weylpair_lane_is_primary": True,
            "reason": (
                "The retarded-overlap formalism is available for the CKM "
                "nil-survivor label and the Schur coefficient formula.  The "
                "q79 alpha1 route, however, still lacks a selected sector "
                "charge/chirality certificate and transfer normalization that "
                "would promote the Weyl-pair carrier into a B_N operator "
                "tangent.  That source theorem must precede honest dotD replay."
            ),
        },
        "next_required_artifact": {
            "name": "Q79_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1",
            "then": [
                "selected transfer normalization",
                "selected Phi_fin/B_N primitive emission",
                "selected alpha1 tangent or retarded-overlap kernel in B_N",
                "honest dotD replay without lifted flags",
            ],
        },
        "guardrails": {
            "does_not_import_ckm_retarded_kernel_as_sm_dotd_proof": True,
            "does_not_promote_conditional_A_to_A_selected": True,
            "does_not_claim_selected_sector_routing": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_C1_or_b_selected": True,
            "does_not_claim_Yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The retarded-kernel route is classified: CKM nil-survivor "
                "retardation supplies the correct type of Schur pattern, while "
                "q79 Route-C requires a selected sector-charge/chirality source "
                "before it can become a typed B_N alpha1 tangent."
            ),
            "what_remains": (
                "Prove the q79 Weyl-pair sector charge/chirality certificate "
                "and selected transfer normalization, then emit the B_N "
                "alpha1 tangent and replay dotD honestly."
            ),
            "next_required_artifact": "Q79_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedAlpha1TangentOrRetardedOverlapKernelAttempt",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "transfer_checks": packet["transfer_checks"],
        "decision": packet["decision"],
        "next_required_artifact": packet["next_required_artifact"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Selected alpha1 Tangent or Retarded Overlap Kernel Attempt v1

## Result

Status: `{cert["status"]}`

The CKM retarded-overlap/nil-survivor kernel supplies a valid Schur-pattern
analogy, but it is not itself the typed `B_N` alpha1 tangent for the q79/F,m=1
SM-sector `dotD` operator.  The q79 route now points one step earlier: prove
the Weyl-pair sector-charge/chirality source and selected transfer
normalization, then emit the `B_N` tangent and replay `dotD` honestly.

## Transfer Checks

```json
{json.dumps(packet["transfer_checks"], indent=2, sort_keys=True)}
```

## Retarded Kernel Transfer

```json
{json.dumps(packet["retarded_kernel_transfer"], indent=2, sort_keys=True)}
```

## Q79 Source Ladder

```json
{json.dumps(packet["q79_source_ladder"], indent=2, sort_keys=True)}
```

## Decision

```json
{json.dumps(packet["decision"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
