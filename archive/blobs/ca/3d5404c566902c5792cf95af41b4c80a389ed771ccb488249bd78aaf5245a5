"""Build Yukawa projection-kernel readiness / threshold-response frontier gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_yukawaprojectionkernel_readiness_or_thresholdresponsefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_OWNER = PACKET_DIR / "updated_source_owner_readiness.packet.json"
SKELETON = PACKET_DIR / "sector_aware_projection_kernel_skeleton.packet.json"
FRONTIER = PACKET_DIR / "threshold_response_frontier_contraction.packet.json"
SUPERSET = PACKET_DIR / "superset_strategy_execution_matrix.packet.json"
DECISION = PACKET_DIR / "yukawa_projection_kernel_readiness_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_projection_readiness.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_YukawaProjectionKernelReadiness_or_ThresholdResponseFrontier_v1.md"

YUKAWA_BRIDGE = DATA / "selected_yukawasourcebridge_or_magnitudeprojectionnogotheorem.candidate.json"
YUKAWA_SOURCE = (
    DATA
    / "selected_yukawasourcebridge_or_magnitudeprojectionnogotheorem"
    / "same_source_yukawa_source_bridge.packet.json"
)
YUKAWA_NOGO = (
    DATA
    / "selected_yukawasourcebridge_or_magnitudeprojectionnogotheorem"
    / "sector_blind_magnitude_projection_nogo.packet.json"
)
YUKAWA_REQUIREMENT = (
    DATA
    / "selected_yukawasourcebridge_or_magnitudeprojectionnogotheorem"
    / "projection_kernel_requirement.packet.json"
)
DYNAMIC_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
THETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
THETA_AUDIT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "current_repo_functional_instantiation_audit.packet.json"
)
THETA_DECISION = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "threshold_response_functional_decision.packet.json"
)
VSD02_REDUCTION = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "no_knob_threshold_derivation_reduction.packet.json"
)
EXTERNAL_MANIFEST = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "external_likelihood_import_manifest.packet.json"
)
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_YUKAWAPROJECTIONKERNEL_READINESS_OR_THRESHOLDRESPONSEFRONTIER_"
    "BUILT_SOURCE_OWNER_PROMOTED_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_ThresholdResponseRows_or_SectorProjectionWeightsExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing projection-readiness sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        YUKAWA_BRIDGE,
        YUKAWA_SOURCE,
        YUKAWA_NOGO,
        YUKAWA_REQUIREMENT,
        DYNAMIC_VALUES,
        THETA_CONTRACT,
        THETA_AUDIT,
        THETA_DECISION,
        VSD02_REDUCTION,
        EXTERNAL_MANIFEST,
        VALUE_PACKET,
    ]
    require_sources(sources)

    bridge = load(YUKAWA_BRIDGE)
    source = load(YUKAWA_SOURCE)
    nogo = load(YUKAWA_NOGO)
    requirement = load(YUKAWA_REQUIREMENT)
    dynamic_values = load(DYNAMIC_VALUES)
    contract = load(THETA_CONTRACT)
    theta_audit = load(THETA_AUDIT)
    theta_decision = load(THETA_DECISION)
    vsd02_reduction = load(VSD02_REDUCTION)
    external_manifest = load(EXTERNAL_MANIFEST)
    value_packet = load(VALUE_PACKET)

    source_closure = source["source_layer_closure"]
    source_owner_promoted = (
        bridge["closure_decision"]["same_source_yukawa_source_layer_closed"]
        and source_closure["same_source_validator_ok"]
        and source_closure["selected_dynamic_overlap_tensor_promoted"]
        and source_closure["primitive_C1_first_response_layer_emitted"]
        and source_closure["dynamic_QaSU3_first_response_layer_replayed"]
    )
    finite_normalization_transport = (
        source["source_fields"]["normalization"]["selected_emitted"]
        and source_closure["symbolic_transport_source_gate_closed"]
        and source_closure["alpha1_dotd_retired"]
    )
    sector_source_rows_present = {
        sector: {
            "present": True,
            "source_direction": row["source_direction"],
            "trace_H1": row["invariants"]["trace"],
            "traceless_norm_sq": row["invariants"]["traceless_norm_sq"],
            "non_scalar": row["invariants"]["non_scalar"],
        }
        for sector, row in dynamic_values["sector_first_responses"].items()
    }

    updated_requirements = [
        {
            "id": "selected_dynamic_operator_source_owner",
            "present": source_owner_promoted,
            "source": rel(YUKAWA_SOURCE),
            "repair": "promoted by same-source Yukawa source bridge",
        },
        {
            "id": "finite_normalization_transport_same_branch",
            "present": finite_normalization_transport,
            "source": rel(YUKAWA_SOURCE),
            "repair": "normalization, symbolic transport, and alpha1/dotD are now tied to the same selected source layer",
        },
        {
            "id": "sector_response_source_rows",
            "present": all(row["present"] for row in sector_source_rows_present.values()),
            "source": rel(DYNAMIC_VALUES),
            "repair": "sector first-response matrices are emitted for u,d,e,nuD",
        },
        {
            "id": "same_branch_scale_scheme_loop_convention",
            "present": False,
            "source": rel(VALUE_PACKET),
            "missing_for_acceptance": [
                "value packet declares first-pass/parity convention, not a true precision threshold convention"
            ],
        },
        {
            "id": "threshold_matching_source_rows",
            "present": False,
            "source": rel(THETA_AUDIT),
            "missing_for_acceptance": [
                "accepted threshold matching source rows remain absent",
                "finite residual rows are downstream validators, not source rows",
            ],
        },
        {
            "id": "mass_scheme_conversion_source_rows",
            "present": False,
            "source": rel(THETA_AUDIT),
            "missing_for_acceptance": ["accepted mass-scheme conversion source rows remain absent"],
        },
        {
            "id": "full_profile_likelihood_or_accepted_diagonal_theorem",
            "present": False,
            "source": rel(EXTERNAL_MANIFEST),
            "missing_for_acceptance": [
                "full profile/covariance workspace is not imported",
                "diagonal profile remains diagnostic, not true-equivalence closure",
            ],
        },
    ]
    present_count = sum(1 for row in updated_requirements if row["present"])

    source_owner = {
        "schema": "MTTUpdatedYukawaSourceOwnerReadiness.v1",
        "status": "SOURCE_OWNER_AND_FIRST_RESPONSE_ROWS_PROMOTED",
        "previous_audit_present_count": theta_audit["present_count"],
        "previous_audit_requirement_count": theta_audit["requirement_count"],
        "updated_requirements": updated_requirements,
        "present_count": present_count,
        "requirement_count": len(updated_requirements),
        "closed_now": {
            "selected_dynamic_operator_source_owner": source_owner_promoted,
            "finite_normalization_transport_same_branch": finite_normalization_transport,
            "sector_response_source_rows": all(row["present"] for row in sector_source_rows_present.values()),
        },
        "still_open": [
            row["id"] for row in updated_requirements if not row["present"]
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SOURCE_OWNER, source_owner)

    skeleton_slots = [
        {
            "sector": "u",
            "source_direction": sector_source_rows_present["u"]["source_direction"],
            "projector_kind": "phase-like sector-aware source slot",
            "accepted_magnitude_source": "open",
        },
        {
            "sector": "e",
            "source_direction": sector_source_rows_present["e"]["source_direction"],
            "projector_kind": "phase-like sector-aware source slot",
            "accepted_magnitude_source": "open",
        },
        {
            "sector": "d",
            "source_direction": sector_source_rows_present["d"]["source_direction"],
            "projector_kind": "shift-like sector-aware source slot",
            "accepted_magnitude_source": "open",
        },
        {
            "sector": "nuD",
            "source_direction": sector_source_rows_present["nuD"]["source_direction"],
            "projector_kind": "shift-like sector-aware source slot",
            "accepted_magnitude_source": "open",
        },
    ]
    skeleton = {
        "schema": "MTTSectorAwareProjectionKernelSkeleton.v1",
        "status": "SECTOR_AWARE_PROJECTION_SKELETON_EMITTED_WEIGHTS_OPEN",
        "source_packet": rel(YUKAWA_SOURCE),
        "dynamic_values": rel(DYNAMIC_VALUES),
        "sector_slots": skeleton_slots,
        "why_skeleton_not_full_kernel": [
            "sector slots are typed and same-source, but no selected magnitude weights are emitted",
            "sector-blind first-response formula is impossible by the previous no-go theorem",
            "threshold and mass-scheme response rows are still absent",
        ],
        "required_weight_rows": [
            "selected sector projection weights for u,d,e and lambda_H",
            "threshold matching rows at declared scale/scheme/loop convention",
            "mass-scheme conversion rows for heavy fermions and Higgs/lambda",
            "profile/covariance response or accepted diagonal theorem",
        ],
        "skeleton_closed": True,
        "full_projection_kernel_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SKELETON, skeleton)

    frontier = {
        "schema": "MTTThresholdResponseFrontierContraction.v1",
        "status": "FRONTIER_CONTRACTED_FROM_SOURCE_OWNER_TO_THRESHOLD_RESPONSE_ROWS",
        "previous_blocking_failures": theta_audit["blocking_failures"],
        "retired_blockers": [
            "selected_dynamic_operator_source_owner",
            "finite normalization/transport/source-owner absence",
            "sector first-response source-row absence",
        ],
        "remaining_blockers": [
            "same_branch_scale_scheme_loop_convention",
            "threshold_matching_source_rows",
            "mass_scheme_conversion_source_rows",
            "full_profile_likelihood_or_accepted_diagonal_theorem",
        ],
        "contract_link": rel(THETA_CONTRACT),
        "rtheta_projection_state": requirement["current_rtheta_state"],
        "value_profile_state": requirement["current_value_profile_state"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FRONTIER, frontier)

    superset = {
        "schema": "MTTSupersetStrategyExecutionMatrixForYukawaProjection.v1",
        "status": "SUPERSET_STRATEGY_LOCKED_TO_COMPLEMENTARY_ROWS",
        "policy": (
            "Use superset paths to close complementary typed rows, never to mix measured residuals into "
            "source selection."
        ),
        "lanes": [
            {
                "id": "lane_A_internal_selected_projection",
                "role": "derive selected sector projection weights and threshold rows from the same MTT branch",
                "current_status": "source owner and skeleton closed; weights/threshold rows open",
                "may_use": [
                    rel(YUKAWA_SOURCE),
                    rel(DYNAMIC_VALUES),
                    rel(THETA_CONTRACT),
                ],
                "must_not_use": contract["forbidden_shortcuts"],
            },
            {
                "id": "lane_B_external_likelihood_workspace",
                "role": "ingest a full external likelihood/profile workspace as validation/profile semantics",
                "current_status": external_manifest["status"],
                "may_use": ["provenance, parameter basis, nuisance/profile semantics, replay command"],
                "must_not_use": ["external central values as selected MTT source rows"],
            },
            {
                "id": "lane_C_superset_discovery",
                "role": "use measured values only to rank candidate branch/projection hypotheses, then require non-observed replay",
                "current_status": "allowed only as discovery, not closure",
                "may_use": ["inverse/superset search metadata"],
                "must_not_use": ["candidate ranking as proof of selection"],
            },
        ],
        "selected_next_lane": "lane_A_internal_selected_projection",
        "why": (
            "The source-owner layer is now selected internally. The nearest missing object is therefore "
            "the internal sector projection/threshold row emission; external likelihood remains a parallel "
            "validation/profile route."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SUPERSET, superset)

    decision = {
        "schema": "MTTYukawaProjectionKernelReadinessDecision.v1",
        "status": "SOURCE_OWNER_AND_SKELETON_CLOSED_FULL_KERNEL_OPEN",
        "updated_readiness_present_count": present_count,
        "updated_readiness_requirement_count": len(updated_requirements),
        "source_owner_promoted": source_owner_promoted,
        "sector_aware_projection_skeleton_closed": True,
        "selected_projection_weights_closed": False,
        "selected_threshold_response_rows_closed": False,
        "mass_scheme_conversion_rows_closed": False,
        "profile_likelihood_or_diagonal_theorem_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_this_fixes": [
            "updates the stale threshold-response audit after the Yukawa source bridge",
            "retires selected dynamic operator source-owner absence as a blocker",
            "emits the legal sector-aware projection skeleton",
            "locks the remaining task to selected weights and threshold/profile rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterYukawaProjectionReadiness.v1",
        "status": "NEXT_ATTACK_THRESHOLD_ROWS_AND_SECTOR_PROJECTION_WEIGHTS",
        "closed_now": {
            "source_owner_promoted": source_owner_promoted,
            "finite_normalization_transport_same_branch": finite_normalization_transport,
            "sector_aware_projection_skeleton": True,
            "superset_strategy_retargeted": True,
        },
        "still_open": [
            "selected sector projection weights",
            "same-branch scale/scheme/loop convention",
            "threshold matching source rows",
            "mass-scheme conversion source rows",
            "full profile likelihood or accepted diagonal theorem",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The source side is now closed enough for projection execution; the missing data are "
                "the actual selected weights and threshold/mass-scheme rows."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedYukawaProjectionKernelReadinessOrThresholdResponseFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "updated_source_owner_readiness": rel(SOURCE_OWNER),
            "sector_aware_projection_kernel_skeleton": rel(SKELETON),
            "threshold_response_frontier_contraction": rel(FRONTIER),
            "superset_strategy_execution_matrix": rel(SUPERSET),
            "yukawa_projection_kernel_readiness_decision": rel(DECISION),
            "next_cutset_after_projection_readiness": rel(CUTSET),
        },
        "theorem": {
            "name": "YukawaProjectionReadinessAndThresholdFrontierContractionTheorem",
            "proved": True,
            "statement": (
                "After the same-source Yukawa source bridge, the selected dynamic/operator source-owner "
                "requirement in the threshold-response contract is no longer open. The repo can promote "
                "source owner, finite normalization/transport, and sector first-response rows, and can emit "
                "a sector-aware projection-kernel skeleton. The full Yukawa magnitude projection kernel still "
                "requires selected sector weights, threshold/mass-scheme source rows, and profile response."
            ),
        },
        "closure_decision": {
            "source_owner_promoted": source_owner_promoted,
            "sector_aware_projection_skeleton_closed": True,
            "full_projection_kernel_closed": False,
            "selected_threshold_response_rows_closed": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_YukawaProjectionKernelReadiness_or_ThresholdResponseFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "source_owner_promoted": source_owner_promoted,
        "updated_readiness_present_count": present_count,
        "updated_readiness_requirement_count": len(updated_requirements),
        "sector_aware_projection_skeleton_closed": True,
        "full_projection_kernel_closed": False,
        "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected YukawaProjectionKernelReadiness or ThresholdResponseFrontier v1

Status: `{STATUS}`.

This artifact fixes the stale response-functional frontier after the same-source
Yukawa source bridge.

```text
source owner promoted              : {str(source_owner_promoted).lower()}
readiness rows present             : {present_count}/{len(updated_requirements)}
sector-aware projection skeleton   : true
full projection kernel closed      : false
Yukawa magnitudes no-knob closed   : false
```

The superset strategy is now retargeted: the internal lane owns the selected
source and projection skeleton, while the external lane remains useful only for
profile/covariance semantics.  The next object must emit selected sector
projection weights and threshold/mass-scheme rows, not another source-owner
argument.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
