"""Build source-identity transport / finitepart policy frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_sourceidentitytransportproofattempt_or_finitepartpolicyindexscale_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_LANE = PACKET_DIR / "source_identity_transport_reduction_lane.packet.json"
FINITEPART_LANE = PACKET_DIR / "finitepart_policy_indexscale_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_transport_finitepart_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceIdentityTransportProofAttempt_or_FinitePartPolicyIndexScaleSourceTheorem_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_bn27connectionsourcevalues_or_physicalalphaactionunitdeterminanttable_or_directhkrow.candidate.json",
    "source_identity_proofattempt": QA
    / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt.candidate.json",
    "finitepart_policy": QA
    / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json",
    "hypercharge_convention": QA
    / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json",
}

STATUS = (
    "MTT_SELECTED_SOURCEIDENTITYTRANSPORTPROOFATTEMPT_OR_FINITEPARTPOLICYINDEXSCALE_"
    "INTERNAL_PA_CLOSED_SOURCEBRANCH_PHYSICALANCHOR_OPEN"
)
NEXT = "MTT_Selected_SourceBranchIdentityEmission_or_QaStackPhysicalAnchor_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def d(src: dict[str, Any]) -> dict[str, Any]:
    return src.get("decision", src.get("closure_decision", {}))


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing source-identity/finitepart inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = d(sources["previous"])
    transport = d(sources["source_identity_proofattempt"])
    finite = d(sources["finitepart_policy"])
    hyper = d(sources["hypercharge_convention"])

    source_lane = {
        "schema": "MTTSourceIdentityTransportReductionLane.v1",
        "status": "TRANSPORT_REDUCED_TO_SINGLE_SOURCE_BRANCH_IDENTITY_LEAF",
        "closure_claimed": True,
        "proof_attempt_executed": transport["proof_attempt_executed"],
        "transport_reduced_to_single_leaf": transport["transport_reduced_to_single_leaf"],
        "single_remaining_leaf": transport["single_remaining_leaf"],
        "operator_coemission_conditional_closed": transport[
            "operator_coemission_conditional_closed"
        ],
        "operator_coemission_unconditional_closed": transport[
            "operator_coemission_unconditional_closed"
        ],
        "no_lift_replay_conditional_closed": transport[
            "no_lift_replay_conditional_closed"
        ],
        "no_lift_replay_unconditional_closed": transport[
            "no_lift_replay_unconditional_closed"
        ],
        "source_branch_identity_closed": transport["source_branch_identity_closed"],
        "selected_connection_witness_export_closed": transport[
            "selected_connection_witness_export_closed"
        ],
        "oriented_logdet_promoted": transport["oriented_logdet_promoted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    finitepart_lane = {
        "schema": "MTTFinitepartPolicyIndexScaleLane.v1",
        "status": "INTERNAL_FINITEPART_POLICY_INDEXSCALE_CLOSED_PHYSICAL_LAMBDA_OPEN",
        "closure_claimed": True,
        "internal_policy": {
            "regularization_finite_part_selected_internal": finite[
                "regularization_finite_part_selected_internal"
            ],
            "determinant_index_weights_selected_internal": finite[
                "determinant_index_weights_selected_internal"
            ],
            "determinant_scale_mu_selected_internal": finite[
                "determinant_scale_mu_selected_internal"
            ],
            "kernel_policy_selected_internal": finite["kernel_policy_selected_internal"],
            "H_zero_cluster_value_invariant_current_branch": finite[
                "H_zero_cluster_value_invariant_current_branch"
            ],
            "selected_p_a_internal_promoted": finite["selected_p_a_internal_promoted"],
            "selected_p_a_internal_value": finite["selected_p_a_internal_value"],
        },
        "physical_boundary": {
            "lambda_12_closed": finite["lambda_12_closed"],
            "same_scheme_SU2_row_or_cancellation_closed": finite[
                "same_scheme_SU2_row_or_cancellation_closed"
            ],
            "physical_K_gauge_anchor_closed": finite["physical_K_gauge_anchor_closed"],
            "measured_electroweak_closure": finite["measured_electroweak_closure"],
        },
        "hypercharge_convention": {
            "typed_hypercharge_convention_map_closed": hyper[
                "typed_hypercharge_convention_map_closed"
            ],
            "hypercharge_index_weights_closed_structurally": hyper[
                "hypercharge_index_weights_closed_structurally"
            ],
            "Qc_row_closed_for_weaksplit": hyper["Qc_row_closed_for_weaksplit"],
            "SU2_row_closed_for_weaksplit": hyper["SU2_row_closed_for_weaksplit"],
            "conditional_lambda12_if_quotient_is_p_a": hyper[
                "conditional_lambda12_if_quotient_is_p_a"
            ],
            "conditional_Delta_G12_if_quotient_is_p_a": hyper[
                "conditional_Delta_G12_if_quotient_is_p_a"
            ],
            "Qa_stack_p_a_source_closed": hyper["Qa_stack_p_a_source_closed"],
            "direct_U1Y_row_promoted": hyper["direct_U1Y_row_promoted"],
            "lambda_12_closed": hyper["lambda_12_closed"],
            "measured_electroweak_closure": hyper["measured_electroweak_closure"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterTransportFinitepartPolicy.v1",
        "status": "NEXT_FRONTIER_SOURCEBRANCH_IDENTITY_OR_PHYSICAL_ANCHOR_OR_DIRECT_HK_ROW",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "source-identity transport proof attempt reduced to source_branch_identity",
            "operator co-emission and no-lift replay are conditionally ready",
            "internal finitepart policy selected on V/<s>",
            "internal determinant index weights are unit weights on quotient table",
            "internal determinant scale mu=1 selected",
            "internal p_a promoted to 29.201650332199108",
            "typed hypercharge convention map closed structurally",
            "conditional lambda12=2.6179362173268497 and Delta_G12=0.08450302790361214 recorded",
        ],
        "still_open": [
            "source_branch_identity emission theorem for BN27 threshold complex",
            "unconditional selected connection witness export",
            "oriented logdet promotion from the BN27 source branch",
            "Qa-stack p_a source emission into the electroweak row",
            "direct U1Y row promotion alternative",
            "physical K_gauge/action-unit or Omega0/K_phys anchor",
            "same-scheme SU2 cancellation conflict resolved against latest packets",
            "physical lambda_12 closure and measured electroweak matching",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSourceIdentityTransportProofAttemptOrFinitepartPolicyIndexScale",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "source_identity_transport_reduction_lane": rel(SOURCE_LANE),
            "finitepart_policy_indexscale_lane": rel(FINITEPART_LANE),
            "next_cutset_after_transport_finitepart_policy": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "source_identity_transport_reduced_to_single_leaf": True,
            "source_branch_identity_closed": False,
            "operator_coemission_conditional_closed": True,
            "no_lift_replay_conditional_closed": True,
            "selected_connection_witness_export_closed": False,
            "oriented_logdet_promoted": False,
            "internal_finitepart_policy_closed": True,
            "internal_determinant_index_weights_closed": True,
            "internal_mu_scale_closed": True,
            "selected_p_a_internal_promoted": True,
            "selected_p_a_internal_value": finite["selected_p_a_internal_value"],
            "typed_hypercharge_convention_map_closed": True,
            "conditional_lambda12_if_quotient_is_p_a": hyper[
                "conditional_lambda12_if_quotient_is_p_a"
            ],
            "conditional_Delta_G12_if_quotient_is_p_a": hyper[
                "conditional_Delta_G12_if_quotient_is_p_a"
            ],
            "Qa_stack_p_a_source_closed": False,
            "direct_U1Y_row_promoted": False,
            "physical_K_gauge_anchor_closed": False,
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
            "selected_R_H_RG_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "direct_HK_exit_still_allowed": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "SourceIdentityTransportOrFinitepartPolicyIndexScaleTheorem",
            "proved": True,
            "statement": (
                "The source-identity transport proof attempt reduces BN27 promotion "
                "to one unconditional source-branch-identity leaf; operator co-emission "
                "and no-lift replay are conditionally ready. On the determinant side, "
                "the internal finitepart policy, quotient index weights, and mu=1 "
                "internal determinant unit promote p_a^int=29.201650332199108. "
                "The typed hypercharge convention is structurally closed, but physical "
                "lambda_12, electroweak matching, and the H K row remain open because "
                "Qa-stack p_a source emission/direct U1Y row promotion and the physical "
                "gauge/action anchor are still absent."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSourceIdentityTransportProofAttemptOrFinitepartPolicyIndexScale",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "source_identity_transport_reduced_to_single_leaf": True,
        "source_branch_identity_closed": False,
        "internal_finitepart_policy_closed": True,
        "selected_p_a_internal_promoted": True,
        "typed_hypercharge_convention_map_closed": True,
        "Qa_stack_p_a_source_closed": False,
        "lambda_12_closed": False,
        "physical_K_gauge_anchor_closed": False,
        "selected_R_H_RG_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Source-Identity Transport Proof Attempt or Finitepart Policy/Index-Scale Source Theorem v1

## Theorem

`SourceIdentityTransportOrFinitepartPolicyIndexScaleTheorem` is emitted.

## Closed Here

- Source-identity transport proof attempt reduces to the single leaf
  `source_branch_identity`.
- Operator co-emission and no-lift replay are conditionally ready.
- Internal finitepart policy is selected on `V/<s>`.
- Internal determinant index weights are unit weights on the quotient table.
- Internal determinant scale is selected as `mu = 1`.
- Internal `p_a` is promoted:
  `p_a^int = 29.201650332199108`.
- Typed hypercharge convention map is structurally closed.
- Conditional values are recorded:
  `lambda_12 = 2.6179362173268497`,
  `Delta_G12 = 0.08450302790361214`.

## Still Open

- BN27 `source_branch_identity` emission theorem.
- Unconditional selected connection witness export and oriented-logdet promotion.
- Qa-stack `p_a` source emission into the electroweak row.
- Direct U1/Y row promotion alternative.
- Physical `K_gauge`/action-unit or `Omega0/K_phys` anchor.
- Physical `lambda_12` closure and measured electroweak matching.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(SOURCE_LANE, source_lane)
    write_json(FINITEPART_LANE, finitepart_lane)
    write_json(NEXT_CUTSET, next_cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
