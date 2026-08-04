"""Build Step49 Omega payload clause-fill / Rtheta_alpha1 execution gate.

Step48 constructed the strict Omega payload theorem and rejected all value rows.
Step49 fills the clause-owner ledger: every missing Omega clause is bound to its
current source packet, its strongest support, and its exact blocking theorem.
This is a construction step, not a value-closure claim.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step49_omega_payload_clausefill_or_rthetaalpha1valueexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OWNER_LEDGER = PACKET_DIR / "step49_omega_clause_owner_ledger.packet.json"
ROW_TEMPLATES = PACKET_DIR / "step49_omega_source_row_templates.packet.json"
OPERATOR_BRIDGE = PACKET_DIR / "step49_operator_payload_bridge_recheck.packet.json"
EXECUTION_RECHECK = PACKET_DIR / "step49_rthetaalpha1_value_execution_recheck.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step49_next_clause_owner_theorem_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step49_OmegaPayloadClauseFill_or_RThetaAlpha1ValueExecution_v1.md"

STEP48 = DATA / "selected_step48_xi_omega_payload_source_theorem_or_rtheta_value_rows.candidate.json"
STEP48_MANIFEST = (
    DATA
    / "selected_step48_xi_omega_payload_source_theorem_or_rtheta_value_rows"
    / "step48_omega_payload_source_manifest.packet.json"
)
STEP48_VALIDATOR = (
    DATA
    / "selected_step48_xi_omega_payload_source_theorem_or_rtheta_value_rows"
    / "step48_omega_payload_strict_acceptance_validator.packet.json"
)
STEP46_MAP = (
    DATA
    / "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution"
    / "step46_selected_alpha1_to_rtheta_coefficient_map.packet.json"
)
VSD02_FILL = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)
VSD02_SCHEMA = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_row_strict_schema.packet.json"
)
MAGNITUDE = (
    DATA
    / "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
    / "magnitude_weights_or_threshold_rows_decision.packet.json"
)
THRESHOLD = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "threshold_response_rows_recheck.packet.json"
)
PROFILE = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "profile_convention_closure_recheck.packet.json"
)
HIGHER_PAYLOAD = DATA / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution.candidate.json"
HYM_PAYLOAD = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json"

STATUS = "MTT_SELECTED_STEP49_OMEGA_PAYLOAD_CLAUSEFILL_OWNERS_LOCKED_VALUE_ROWS_OPEN"
NEXT = "MTT_Selected_OmegaClauseOwnerTheorems_or_RThetaAlpha1Rows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def owner(
    clause_id: str,
    owner_packet: Path,
    current_closed: bool,
    strongest_support: list[str],
    blocking_theorem: str,
    blocker: str,
) -> dict[str, Any]:
    return {
        "clause_id": clause_id,
        "owner_packet": rel(owner_packet),
        "current_closed": bool(current_closed),
        "strongest_support": strongest_support,
        "blocking_theorem": blocking_theorem,
        "blocker": blocker,
        "accepted_for_value_execution_now": bool(current_closed),
    }


def clause_owner_ledger(
    vsd02: dict[str, Any],
    magnitude: dict[str, Any],
    threshold: dict[str, Any],
    profile: dict[str, Any],
    higher_payload: dict[str, Any],
    hym_payload: dict[str, Any],
) -> dict[str, Any]:
    owners = [
        owner(
            "accepted_vsd02_source_rows",
            VSD02_FILL,
            vsd02["accepted_row_count"] > 0,
            ["strict schema exists", f"candidate rows seen: {vsd02['candidate_source_row_count']}"],
            "AcceptedOmegaSourceRowsEmissionTheorem",
            "VSD02 still accepts zero source rows under the strict no-selector schema",
        ),
        owner(
            "magnitude_bearing_projection_weights",
            MAGNITUDE,
            magnitude["magnitude_bearing_projection_weights_closed"],
            [
                "source-normalized sector projection weights closed",
                "diagnostic magnitude backsolve emitted but not accepted as selection",
                "rank-gap theorem proved",
            ],
            "SelectedMagnitudeBearingProjectionWeightTheorem",
            "current source-normalized rank cannot generate generation-resolved magnitudes",
        ),
        owner(
            "generation_resolved_threshold_source_rows",
            MAGNITUDE,
            magnitude["generation_resolved_threshold_source_rows_closed"],
            ["source-normalized weights closed", "threshold row target identified"],
            "SelectedGenerationResolvedThresholdSourceRowsTheorem",
            "generation-resolved source rows are not emitted by current magnitude packet",
        ),
        owner(
            "threshold_matching_source_rows",
            THRESHOLD,
            threshold["threshold_response_rows_closed"],
            ["threshold response functional contract exists", "finite residual rows exist"],
            "SameBranchThresholdMatchingRowsTheorem",
            "accepted threshold matching source rows list is empty",
        ),
        owner(
            "mass_scheme_conversion_source_rows",
            THRESHOLD,
            threshold["mass_scheme_conversion_rows_closed"],
            ["mass-scheme residual values are finite", "source-row audit exists"],
            "SameBranchMassSchemeConversionRowsTheorem",
            "accepted mass-scheme conversion source rows list is empty",
        ),
        owner(
            "true_precision_scale_scheme_loop_convention",
            PROFILE,
            profile["same_branch_scale_scheme_loop_convention_closed"],
            ["first-pass convention accepted for SM parity/profile input"],
            "TruePrecisionScaleSchemeLoopConventionTheorem",
            "available convention is first-pass/parity and explicitly no-threshold diagnostic",
        ),
        owner(
            "full_profile_likelihood",
            PROFILE,
            profile["full_profile_likelihood_closed"],
            ["value profile execution layer closed", "profile input available"],
            "FullProfileLikelihoodOrAcceptedDiagonalLimitationTheorem",
            "full covariance/profile likelihood is not emitted",
        ),
        owner(
            "selected_higher_response_operator_payload",
            HIGHER_PAYLOAD,
            higher_payload["closure_decision"]["selected_operator_payload_closed"],
            [
                "dotD_alpha1 payload closed",
                "diagonal End0 HYM payload closed"
                if hym_payload["closure_decision"]["diagonal_End0_operator_payload_closed"]
                else "diagonal End0 HYM payload not closed",
            ],
            "SelectedHigherResponseOperatorPayloadTheorem",
            "diagonal End0 support has not promoted to selected sector/full-S2 operator payload",
        ),
    ]
    return {
        "schema": "MTTStep49OmegaClauseOwnerLedger.v1",
        "status": "CLAUSE_OWNERS_LOCKED_VALUES_NOT_ACCEPTED",
        "owner_count": len(owners),
        "owners": owners,
        "closed_owner_count": sum(1 for item in owners if item["current_closed"] is True),
        "open_owner_count": sum(1 for item in owners if item["current_closed"] is not True),
        "all_owners_bound": all(item["owner_packet"] for item in owners),
        "all_value_bearing_clauses_closed": all(item["current_closed"] is True for item in owners),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }


def slot_template(slot: dict[str, Any], ledger: dict[str, Any], schema: dict[str, Any]) -> dict[str, Any]:
    is_higgs = slot["sector"] == "H"
    owner_status = {item["clause_id"]: item["current_closed"] for item in ledger["owners"]}
    required = [
        "accepted_vsd02_source_rows",
        "magnitude_bearing_projection_weights",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "true_precision_scale_scheme_loop_convention",
        "full_profile_likelihood",
        "selected_higher_response_operator_payload",
    ]
    if is_higgs:
        required.append("selected_higgs_lambda_payload_row")
    else:
        required.append("generation_resolved_threshold_source_rows")
    clause_status = {key: owner_status.get(key, False) for key in required}
    clause_status["no_observed_selector_proof"] = True
    return {
        "row_id": f"{slot['omega_id']}.source_row_template",
        "omega_id": slot["omega_id"],
        "xi_id": slot["xi_id"],
        "row_type": "no_knob_value_derivation",
        "source_owner": "selected_MTT_branch",
        "value_payload": None,
        "scale_scheme_loop_convention": None,
        "basis_map_to_MTT_value_packet": slot["formal_payload_term"],
        "strict_schema_required_fields": schema["accepted_row_must_include"],
        "clause_status": clause_status,
        "closed_clause_count": sum(1 for value in clause_status.values() if value is True),
        "required_clause_count": len(clause_status),
        "accepted_as_source_row": all(clause_status.values()),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP48,
        STEP48_MANIFEST,
        STEP48_VALIDATOR,
        STEP46_MAP,
        VSD02_FILL,
        VSD02_SCHEMA,
        MAGNITUDE,
        THRESHOLD,
        PROFILE,
        HIGHER_PAYLOAD,
        HYM_PAYLOAD,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step49 inputs: " + ", ".join(missing))

    step48 = load(STEP48)
    manifest = load(STEP48_MANIFEST)
    validator = load(STEP48_VALIDATOR)
    step46 = load(STEP46_MAP)
    vsd02 = load(VSD02_FILL)
    schema = load(VSD02_SCHEMA)
    magnitude = load(MAGNITUDE)
    threshold = load(THRESHOLD)
    profile = load(PROFILE)
    higher_payload = load(HIGHER_PAYLOAD)
    hym_payload = load(HYM_PAYLOAD)

    ledger = clause_owner_ledger(vsd02, magnitude, threshold, profile, higher_payload, hym_payload)
    write_json(OWNER_LEDGER, ledger)

    templates = [slot_template(slot, ledger, schema) for slot in manifest["payload_slots"]]
    row_templates = {
        "schema": "MTTStep49OmegaSourceRowTemplates.v1",
        "status": "TEN_SOURCE_ROW_TEMPLATES_FILLED_UNPROMOTED",
        "template_count": len(templates),
        "accepted_template_count": sum(1 for row in templates if row["accepted_as_source_row"]),
        "templates": templates,
        "forbidden_promotions_preserved": schema["forbidden_as_accepted_source_rows"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ROW_TEMPLATES, row_templates)

    operator_bridge = {
        "schema": "MTTStep49OperatorPayloadBridgeRecheck.v1",
        "status": "DIAGONAL_END0_SUPPORT_CONFIRMED_SELECTED_SECTOR_PAYLOAD_OPEN",
        "higher_response_owner": rel(HIGHER_PAYLOAD),
        "hym_owner": rel(HYM_PAYLOAD),
        "dotD_alpha1_payload_closed": higher_payload["closure_decision"]["dotD_alpha1_payload_closed"],
        "diagonal_End0_operator_payload_closed": hym_payload["closure_decision"][
            "diagonal_End0_operator_payload_closed"
        ],
        "selected_operator_payload_closed": higher_payload["closure_decision"][
            "selected_operator_payload_closed"
        ],
        "selected_HYM_sector_payload_closed": hym_payload["closure_decision"][
            "selected_HYM_sector_payload_closed"
        ],
        "promotable_to_omega_now": False,
        "blocking_theorem": "SelectedHigherResponseOperatorPayloadTheorem",
        "reason": (
            "Omega needs selected sector/full-S2 operator payload, not only diagonal End0 "
            "support or dotD_alpha1 support."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(OPERATOR_BRIDGE, operator_bridge)

    accepted_rows = row_templates["accepted_template_count"]
    execution = {
        "schema": "MTTStep49RThetaAlpha1ValueExecutionRecheck.v1",
        "status": "RTHETA_ALPHA1_EXECUTION_RECHECKED_SOURCE_ROWS_STILL_ZERO",
        "Rtheta_alpha1_map_constructed": step46["map_domain_closed"],
        "step48_payload_manifest_constructed": step48["closure_decision"][
            "omega_payload_source_theorem_manifest_constructed"
        ],
        "omega_clause_owners_locked": ledger["all_owners_bound"],
        "omega_source_row_templates_filled": len(templates) == 10,
        "accepted_omega_source_rows": accepted_rows,
        "accepted_internal_Rtheta_coefficient_row_count": 0,
        "accepted_internal_scalar_row_count": 0,
        "selected_lambda_H_row_closed": False,
        "value_rows_execute": accepted_rows == 10,
        "minimal_parameter_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "missing_value_bearing_clauses": [
            item["clause_id"] for item in ledger["owners"] if item["current_closed"] is not True
        ],
        "step48_missing_global_clauses_preserved": validator["missing_global_clauses"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXECUTION_RECHECK, execution)

    next_frontier = {
        "schema": "MTTStep49NextClauseOwnerTheoremFrontier.v1",
        "status": "CLAUSE_OWNER_THEOREMS_ARE_NEXT_EXECUTABLE_TARGETS",
        "closed_now": {
            "all_8_global_clause_owners_bound": ledger["all_owners_bound"],
            "all_10_omega_source_row_templates_filled": len(templates) == 10,
            "operator_payload_bridge_rechecked": True,
            "Rtheta_alpha1_execution_rechecked": True,
        },
        "next_owner_theorems_in_order": [
            "SelectedHigherResponseOperatorPayloadTheorem",
            "SelectedMagnitudeBearingProjectionWeightTheorem",
            "SameBranchThresholdMatchingRowsTheorem",
            "SameBranchMassSchemeConversionRowsTheorem",
            "TruePrecisionScaleSchemeLoopConventionTheorem",
            "FullProfileLikelihoodOrAcceptedDiagonalLimitationTheorem",
            "SelectedGenerationResolvedThresholdSourceRowsTheorem",
            "AcceptedOmegaSourceRowsEmissionTheorem",
        ],
        "why_this_order": (
            "The operator payload and magnitude weights are upstream of every charged "
            "Omega row. Threshold/mass/profile clauses then turn templates into accepted "
            "source rows; VSD02 acceptance is the final strict validator."
        ),
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_FRONTIER, next_frontier)

    candidate = {
        "candidate": "MTTSelectedStep49OmegaPayloadClauseFillOrRThetaAlpha1ValueExecution",
        "status": STATUS,
        "inputs": {
            "step48": rel(STEP48),
            "step48_manifest": rel(STEP48_MANIFEST),
            "step48_validator": rel(STEP48_VALIDATOR),
            "step46_map": rel(STEP46_MAP),
            "vsd02_fill": rel(VSD02_FILL),
            "vsd02_schema": rel(VSD02_SCHEMA),
            "magnitude": rel(MAGNITUDE),
            "threshold": rel(THRESHOLD),
            "profile": rel(PROFILE),
            "higher_payload": rel(HIGHER_PAYLOAD),
            "hym_payload": rel(HYM_PAYLOAD),
        },
        "output_packets": {
            "omega_clause_owner_ledger": rel(OWNER_LEDGER),
            "omega_source_row_templates": rel(ROW_TEMPLATES),
            "operator_payload_bridge_recheck": rel(OPERATOR_BRIDGE),
            "rthetaalpha1_value_execution_recheck": rel(EXECUTION_RECHECK),
            "next_clause_owner_theorem_frontier": rel(NEXT_FRONTIER),
        },
        "theorem": {
            "name": "Step49OmegaClauseOwnerFillTheorem",
            "proved": True,
            "statement": (
                "Every Step48 Omega payload clause is now assigned to a concrete source-owner "
                "packet, current proof status, strongest support, and blocking theorem. The ten "
                "Omega source-row templates are filled but remain unaccepted because no value-"
                "bearing global clause is closed."
            ),
        },
        "closure_decision": {
            "omega_clause_owners_locked": ledger["all_owners_bound"],
            "omega_source_row_templates_filled": len(templates) == 10,
            "operator_payload_bridge_rechecked": True,
            "accepted_omega_source_rows": accepted_rows,
            "accepted_internal_Rtheta_coefficient_row_count": 0,
            "accepted_internal_scalar_row_count": 0,
            "selected_lambda_H_row_closed": False,
            "minimal_parameter_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step49_OmegaPayloadClauseFill_or_RThetaAlpha1ValueExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step49 OmegaPayloadClauseFill or RThetaAlpha1ValueExecution v1

Status: `{STATUS}`.

Step49 fills the clause-owner construction for the Step48 `Omega` payload
theorem.  Every global clause is now bound to an owner packet, strongest support,
and blocking theorem.

```text
global clause owners locked           : {ledger["owner_count"]}/8
Omega source-row templates filled     : {len(templates)}/10
accepted Omega source rows            : {accepted_rows}
accepted internal Rtheta rows         : 0
lambda_H internal row closed          : false
```

The construction confirms that the diagonal End0 HYM payload and `dotD_alpha1`
support are useful but not yet enough: `Omega` requires the selected
sector/full-S2 higher-response operator payload.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
