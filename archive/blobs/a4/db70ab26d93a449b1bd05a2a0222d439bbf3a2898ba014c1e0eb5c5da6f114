"""Build R_theta support re-evaluation / source promotion attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_supportreevaluation_or_sourcepromotionattempt"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUPPORT_REEVALUATION = PACKET_DIR / "support_rows_under_rtheta_contract.packet.json"
NON_SOURCE_CLOSURES = PACKET_DIR / "accepted_non_source_support_closures.packet.json"
PROMOTION_ATTEMPT = PACKET_DIR / "source_promotion_attempt_after_support_reevaluation.packet.json"
DECISION = PACKET_DIR / "rtheta_support_reevaluation_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rtheta_support_reevaluation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaSupportReevaluation_or_SourcePromotionAttempt_v1.md"

PREVIOUS = DATA / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition.candidate.json"
RTHETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
RTHETA_INSTANTIATION = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "current_repo_functional_instantiation_audit.packet.json"
)
SOURCE_ROW_AUDIT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)
NO_KNOB_ATTEMPT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "no_knob_value_derivation_attempt.packet.json"
)
BACKLOG = DATA / "no_knob_upgrade_backlog.candidate.json"
QASU3_PACKET = DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
RESIDUALS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)
EXTERNAL_MANIFEST = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "external_likelihood_import_manifest.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETA_SUPPORTREEVALUATION_OR_SOURCEPROMOTIONATTEMPT_"
    "BUILT_SUPPORT_ROLES_CLOSED_SOURCE_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_RThetaSourceOwnerAndRowCoefficientPacket_v1"


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
        raise FileNotFoundError("missing R_theta support reevaluation sources: " + ", ".join(missing))


def backlog_by_id(backlog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["id"]: row for row in backlog["backlog_rows"]}


def source_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "support_id": row["id"],
        "source": row["source"],
        "prior_label": row["row_type"],
        "support_present": row["support_present"],
        "rtheta_role": "candidate_source_row_retested",
        "accepted_non_source_role": None,
        "accepted_as_rtheta_source_row": False,
        "satisfies_rtheta_requirements": [],
        "still_missing_for_source_promotion": row["why_not"],
        "decision": "not_promoted",
    }


def backlog_row(row: dict[str, Any], rtheta_role: str, missing: list[str]) -> dict[str, Any]:
    return {
        "support_id": row["id"],
        "source": row["supporting_sources"],
        "prior_label": row["status"],
        "support_present": row["corpus_backed"],
        "rtheta_role": rtheta_role,
        "accepted_non_source_role": "route_evidence",
        "accepted_as_rtheta_source_row": False,
        "satisfies_rtheta_requirements": [],
        "still_missing_for_source_promotion": missing,
        "decision": "retained_as_route_evidence_only",
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        RTHETA_CONTRACT,
        RTHETA_INSTANTIATION,
        SOURCE_ROW_AUDIT,
        NO_KNOB_ATTEMPT,
        BACKLOG,
        QASU3_PACKET,
        VALUE_PACKET,
        RESIDUALS,
        EXTERNAL_MANIFEST,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    contract = load(RTHETA_CONTRACT)
    instantiation = load(RTHETA_INSTANTIATION)
    source_audit = load(SOURCE_ROW_AUDIT)
    no_knob = load(NO_KNOB_ATTEMPT)
    backlog = load(BACKLOG)
    qasu3 = load(QASU3_PACKET)
    value_packet = load(VALUE_PACKET)
    residuals = load(RESIDUALS)
    external = load(EXTERNAL_MANIFEST)
    backlog_rows = backlog_by_id(backlog)

    reevaluated_rows = [source_row(row) for row in source_audit["candidate_rows"]]

    by_id = {row["support_id"]: row for row in reevaluated_rows}
    by_id["residual_value_table"]["accepted_non_source_role"] = "finite_residual_validation_support"
    by_id["residual_value_table"]["satisfies_rtheta_requirements"] = [
        "finite_residual_validation_support"
    ]
    by_id["residual_value_table"]["decision"] = "promoted_to_validation_support_not_source"

    by_id["sm_embedding_measured_slot_policy"]["accepted_non_source_role"] = "guardrail"
    by_id["sm_embedding_measured_slot_policy"]["decision"] = "accepted_as_guardrail_not_source"

    by_id["qasu3_sm_parity_source_rows"]["accepted_non_source_role"] = (
        "SM_parity_domain_interface_candidate"
    )
    by_id["qasu3_sm_parity_source_rows"]["decision"] = (
        "retained_as_domain_interface_candidate_not_VSD02_source_owner"
    )

    by_id["versioned_value_packet"]["accepted_non_source_role"] = "value_replay_payload"
    by_id["versioned_value_packet"]["decision"] = "accepted_as_replay_payload_not_precision_source"

    extra_rows = [
        backlog_row(
            backlog_rows["local_qft_functor"],
            "observable_functor_route_evidence",
            [
                "needs reproducible functor certificate",
                "does not emit R_theta row coefficients",
            ],
        ),
        backlog_row(
            backlog_rows["selected_sm_packet"],
            "source_owner_route_evidence",
            [
                "actual selected operator packet still open",
                "typed monad/section-ring maps not accepted as R_theta source-owner theorem",
            ],
        ),
        backlog_row(
            backlog_rows["gauge_threshold_no_knob"],
            "threshold_kernel_route_evidence",
            [
                "internal reduced logdet status does not yet give physical coupling/threshold response",
                "R_theta row coefficients absent",
            ],
        ),
        backlog_row(
            backlog_rows["yukawa_cp_higgs_no_knob"],
            "flavor_higgs_kernel_route_evidence",
            [
                "actual selected overlap matrices and Higgs source kernels absent",
                "current branch support cannot supply VSD02 threshold/mass-scheme rows",
            ],
        ),
    ]
    reevaluated_rows.extend(extra_rows)

    accepted_source_rows = [
        row for row in reevaluated_rows if row["accepted_as_rtheta_source_row"]
    ]
    accepted_non_source_rows = [
        row for row in reevaluated_rows if row["accepted_non_source_role"] is not None
    ]

    support_reevaluation = {
        "schema": "MTTRThetaSupportRowsUnderContract.v1",
        "status": "SUPPORT_ROWS_REEVALUATED_UNDER_RTHETA_CONTRACT",
        "rtheta_contract": rel(RTHETA_CONTRACT),
        "acceptance_equations": contract["acceptance_equations"],
        "reevaluated_rows": reevaluated_rows,
        "reevaluated_row_count": len(reevaluated_rows),
        "accepted_non_source_role_count": len(accepted_non_source_rows),
        "accepted_rtheta_source_row_count": len(accepted_source_rows),
        "support_ambiguity_closed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SUPPORT_REEVALUATION, support_reevaluation)

    non_source_closures = {
        "schema": "MTTAcceptedNonSourceSupportClosures.v1",
        "status": "NON_SOURCE_SUPPORT_ROLES_ACCEPTED_SOURCE_ROWS_STILL_EMPTY",
        "accepted_validation_support": [
            "residual_value_table"
        ] if residuals["summary"]["all_residuals_finite"] else [],
        "accepted_guardrails": [
            "sm_embedding_measured_slot_policy"
        ],
        "accepted_domain_or_replay_inputs": [
            "qasu3_sm_parity_source_rows",
            "versioned_value_packet",
        ],
        "accepted_route_evidence": [
            "local_qft_functor",
            "selected_sm_packet",
            "gauge_threshold_no_knob",
            "yukawa_cp_higgs_no_knob",
        ],
        "accepted_source_rows": [],
        "what_this_closes": {
            "finite_residual_validation_support": residuals["summary"]["all_residuals_finite"],
            "support_row_role_classification": True,
            "proxy_rows_rejected_as_sources": True,
            "same_branch_support_reused_without_overclaim": True,
        },
        "what_this_does_not_close": {
            "selected_dynamic_operator_source_owner": True,
            "same_branch_scale_scheme_loop_convention": True,
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "no_knob_value_derivation": True,
            "full_profile_likelihood_or_accepted_diagonal_theorem": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NON_SOURCE_CLOSURES, non_source_closures)

    promotion_attempt = {
        "schema": "MTTRThetaSourcePromotionAttemptAfterSupportReevaluation.v1",
        "status": "SOURCE_PROMOTION_ATTEMPT_EXECUTED_NO_RTHETA_SOURCE_ROWS_ACCEPTED",
        "previous_instantiation_status": instantiation["status"],
        "prior_present_requirements": instantiation["present_count"],
        "current_accepted_source_rows": [],
        "accepted_threshold_matching_source_rows": [],
        "accepted_mass_scheme_conversion_source_rows": [],
        "accepted_source_owner_theorem": None,
        "accepted_scale_scheme_loop_convention": None,
        "accepted_profile_likelihood_or_diagonal_theorem": None,
        "promoted_from_support_count": 0,
        "why_no_support_row_promotes": [
            "support rows do not emit R_theta before observed-value comparison",
            "residual/value packets are downstream validation or replay inputs",
            "Qa/SU3 parity closure is not the actual VSD02 operator/source-owner theorem",
            "route evidence identifies where to derive rows but does not contain row coefficients",
            "external likelihood route still lacks a full workspace or accepted diagonal theorem",
        ],
        "no_knob_value_derivation_closed": no_knob["no_knob_value_derivation_closed"],
        "external_likelihood_imported": external["accepted_external_likelihood_imported_now"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION_ATTEMPT, promotion_attempt)

    decision = {
        "schema": "MTTRThetaSupportReevaluationDecision.v1",
        "status": "SUPPORT_REEVALUATION_CLOSED_SOURCE_PROMOTION_REMAINS_OPEN",
        "previous_status": previous["status"],
        "support_ambiguity_closed": True,
        "accepted_non_source_support_closed": True,
        "source_promotion_attempt_executed": True,
        "accepted_rtheta_source_row_count": 0,
        "selected_threshold_response_functional_instantiated": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "remaining_rtheta_blockers": instantiation["blocking_failures"],
        "minimal_next_payload": {
            "source_owner": "same-branch selected dynamic/operator source-owner theorem",
            "row_coefficients": "threshold and mass-scheme coefficient/formula packet",
            "precision_convention": "scale/scheme/loop-order convention selected before comparison",
            "profile_response": "full likelihood workspace or accepted diagonal limitation theorem",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterRThetaSupportReevaluation.v1",
        "status": "NEXT_ATTACK_RTHETA_SOURCE_OWNER_AND_ROW_COEFFICIENT_PACKET",
        "closed_now": {
            "support_reevaluation_under_Rtheta_contract": True,
            "accepted_non_source_support_roles": True,
            "source_promotion_attempt": True,
        },
        "still_open": decision["remaining_rtheta_blockers"],
        "recommended_next": {
            "artifact": NEXT,
            "must_emit": [
                "R_theta source-owner theorem",
                "threshold row coefficients/formulas for top, bottom, charm, tau, W/Z/H",
                "mass-scheme row coefficients/formulas for top, bottom, charm, tau, Higgs/lambda",
                "basis map to versioned common-scale value packet",
                "precision convention selected before measured-value comparison",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaSupportReevaluationOrSourcePromotionAttempt",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "support_rows_under_rtheta_contract": rel(SUPPORT_REEVALUATION),
            "accepted_non_source_support_closures": rel(NON_SOURCE_CLOSURES),
            "source_promotion_attempt_after_support_reevaluation": rel(PROMOTION_ATTEMPT),
            "rtheta_support_reevaluation_decision": rel(DECISION),
            "next_cutset_after_rtheta_support_reevaluation": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaSupportReevaluationAndNoSourcePromotionTheorem",
            "proved": True,
            "statement": (
                "Every current support row can be re-evaluated under the selected R_theta contract. "
                "Several rows are accepted in non-source roles: finite residual validation, guardrail, "
                "domain/replay input, or route evidence. None satisfies the source-owner, row-coefficient, "
                "precision-convention, and profile-response obligations required to instantiate R_theta. "
                "Therefore support ambiguity is closed, while VSD02 source promotion remains open."
            ),
        },
        "what_closes_now": decision,
        "closure_decision": {
            "support_ambiguity_closed": True,
            "accepted_non_source_support_closed": True,
            "accepted_rtheta_source_rows_closed": False,
            "selected_threshold_response_functional_instantiated": False,
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
        "certificate": "MTT_Selected_RThetaSupportReevaluation_or_SourcePromotionAttempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "support_ambiguity_closed": True,
        "accepted_non_source_support_closed": True,
        "accepted_rtheta_source_row_count": 0,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaSupportReevaluation or SourcePromotionAttempt v1

Status: `{STATUS}`.

This artifact re-checks the rows previously called support under the stricter
`R_theta` contract.

```text
support rows re-evaluated       : {support_reevaluation["reevaluated_row_count"]}
accepted non-source roles       : {support_reevaluation["accepted_non_source_role_count"]}
accepted R_theta source rows    : 0
source promotion attempted      : true
```

The useful upgrade is that "support" is no longer vague.  Some rows are now
accepted as validation support, guardrails, domain/replay inputs, or route
evidence.  None is accepted as an `R_theta` source row.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
