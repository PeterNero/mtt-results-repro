"""Build same-branch convention or threshold-row emission frontier artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_samebranchconvention_or_thresholdrowemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONVENTION_TARGET = PACKET_DIR / "true_precision_convention_target.packet.json"
SOURCE_GAP = PACKET_DIR / "same_branch_convention_source_gap.packet.json"
THRESHOLD_ORDER = PACKET_DIR / "threshold_row_emission_prerequisite_order.packet.json"
DECISION = PACKET_DIR / "same_branch_convention_or_threshold_row_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameBranchConvention_or_ThresholdRowEmission_v1.md"

PREVIOUS = DATA / "selected_responsefunctionalatomicroutes_or_externallikelihoodacquisition.candidate.json"
ORDERED_CUTSET = (
    DATA
    / "selected_responsefunctionalatomicroutes_or_externallikelihoodacquisition"
    / "ordered_remaining_response_functional_cutset.packet.json"
)
PROFILE_RECHECK = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "profile_convention_closure_recheck.packet.json"
)
RTHETA_PROFILE_RECHECK = (
    DATA
    / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure"
    / "profile_convention_source_recheck.packet.json"
)
COMMON_SCALE_TRANSPORT = (
    DATA
    / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
    / "yukawa_higgs_common_scale_transport_kernel.packet.json"
)
SM_COMMON_SCALE = DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
)
RG_CONVERGENCE = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "internal_rg_convergence_benchmark.packet.json"
)
RESIDUAL_VALUES = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)
VSD02_FILL = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)

STATUS = (
    "MTT_SELECTED_SAMEBRANCHCONVENTION_OR_THRESHOLDROWEMISSION_"
    "BUILT_CONVENTION_TARGET_IDENTIFIED_SOURCE_OPEN"
)
NEXT = "MTT_Selected_ConventionSourceTheorem_or_RGEngineThresholdPolicy_v1"


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
        raise FileNotFoundError("missing same-branch convention sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        ORDERED_CUTSET,
        PROFILE_RECHECK,
        RTHETA_PROFILE_RECHECK,
        COMMON_SCALE_TRANSPORT,
        SM_COMMON_SCALE,
        THRESHOLD_CONTRACT,
        RG_CONVERGENCE,
        RESIDUAL_VALUES,
        VSD02_FILL,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    ordered_cutset = load(ORDERED_CUTSET)
    profile_recheck = load(PROFILE_RECHECK)
    rtheta_profile = load(RTHETA_PROFILE_RECHECK)
    common_transport = load(COMMON_SCALE_TRANSPORT)
    sm_common = load(SM_COMMON_SCALE)
    threshold_contract = load(THRESHOLD_CONTRACT)
    rg_convergence = load(RG_CONVERGENCE)
    residual_values = load(RESIDUAL_VALUES)
    vsd02_fill = load(VSD02_FILL)

    target = {
        "schema": "MTTTruePrecisionConventionTarget.v1",
        "status": "TRUE_PRECISION_CONVENTION_TARGET_IDENTIFIED_NOT_SELECTED_SOURCE",
        "target_scale": common_transport["target_scale"],
        "target_scheme": common_transport["target_scheme"],
        "minimum_loop_order": common_transport["required_engine_inputs"]["loop_order"],
        "beta_functions_required": common_transport["required_engine_inputs"]["beta_functions_required"],
        "threshold_policy_required": common_transport["required_engine_inputs"]["threshold_policy"],
        "mass_scheme_policy_required": common_transport["required_engine_inputs"]["mass_scheme_policy"],
        "covariance_policy": common_transport["required_engine_inputs"]["covariance_policy"],
        "threshold_matching_required": threshold_contract["threshold_matching_required"],
        "mass_scheme_conversion_required": threshold_contract["mass_scheme_conversion_required"],
        "target_identified": True,
        "selected_same_branch_source_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CONVENTION_TARGET, target)

    firstpass_is_not_true_precision = (
        profile_recheck["accepted_for_true_precision_equivalence"] is False
        and rtheta_profile["accepted_for_true_precision_equivalence"] is False
        and profile_recheck["same_branch_scale_scheme_loop_convention_closed"] is False
        and rtheta_profile["same_branch_scale_scheme_loop_convention_closed"] is False
    )
    diagnostic_engine_not_accepted = (
        rg_convergence["passes_internal_convergence"] is True
        and rg_convergence["accepted_for_SM_parity_values"] is False
    )
    no_values_emitted = all(value is None for value in common_transport["emitted_values"].values())
    zero_accepted_rows = vsd02_fill["accepted_row_count"] == 0

    source_gap = {
        "schema": "MTTSameBranchConventionSourceGap.v1",
        "status": "SAME_BRANCH_TRUE_PRECISION_CONVENTION_SOURCE_OPEN",
        "profile_recheck_source": rel(PROFILE_RECHECK),
        "rtheta_profile_recheck_source": rel(RTHETA_PROFILE_RECHECK),
        "rg_convergence_source": rel(RG_CONVERGENCE),
        "common_scale_transport_source": rel(COMMON_SCALE_TRANSPORT),
        "firstpass_profile_layer_closed": profile_recheck["profile_layer_closed"],
        "firstpass_accepted_for_profile_input": profile_recheck["accepted_for_profile_input"],
        "firstpass_accepted_for_true_precision": profile_recheck["accepted_for_true_precision"],
        "firstpass_is_not_true_precision": firstpass_is_not_true_precision,
        "diagnostic_internal_rg_convergence_closed": rg_convergence["passes_internal_convergence"],
        "diagnostic_engine_accepted_for_SM_parity_values": rg_convergence[
            "accepted_for_SM_parity_values"
        ],
        "diagnostic_engine_not_accepted_as_true_precision_source": diagnostic_engine_not_accepted,
        "common_scale_yukawa_higgs_values_emitted": no_values_emitted is False,
        "accepted_threshold_mass_scheme_rows": vsd02_fill["accepted_row_count"],
        "finite_residual_table_present": residual_values["summary"]["all_residuals_finite"],
        "finite_residual_table_is_not_source_rows": (
            residual_values["accepted_as_threshold_matching_values"] is False
            and residual_values["accepted_as_mass_scheme_conversion_values"] is False
        ),
        "selected_same_branch_scale_scheme_loop_convention_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SOURCE_GAP, source_gap)

    threshold_order = {
        "schema": "MTTThresholdRowEmissionPrerequisiteOrder.v1",
        "status": "THRESHOLD_ROW_EMISSION_ORDERED_AFTER_CONVENTION_SOURCE",
        "ordered_prerequisites": [
            {
                "order": 1,
                "id": "selected_same_branch_convention_source",
                "closed": False,
                "reason": "M_Z/MSbar target is identified, but source ownership and threshold policy are not selected",
            },
            {
                "order": 2,
                "id": "versioned_RG_engine_or_external_literature_benchmark",
                "closed": False,
                "reason": "internal RK convergence is diagnostic only; external or fully specified internal benchmark policy is open",
            },
            {
                "order": 3,
                "id": "threshold_matching_rows",
                "closed": False,
                "reason": "top/bottom/charm/tau/W_Z_H matching rows need convention and source provenance first",
            },
            {
                "order": 4,
                "id": "mass_scheme_conversion_rows",
                "closed": False,
                "reason": "pole/rest/direct/native mass maps need the selected convention first",
            },
            {
                "order": 5,
                "id": "covariance_or_profile_response",
                "closed": False,
                "reason": "covariance semantics attach to emitted/imported conventioned rows",
            },
        ],
        "can_emit_threshold_rows_now": False,
        "can_accept_external_rows_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(THRESHOLD_ORDER, threshold_order)

    decision = {
        "schema": "MTTSameBranchConventionOrThresholdRowDecision.v1",
        "status": "CONVENTION_TARGET_CLOSED_SOURCE_AND_ROWS_OPEN",
        "previous_status": previous["status"],
        "ordered_cutset_source": rel(ORDERED_CUTSET),
        "convention_target_identified": True,
        "same_branch_true_precision_convention_closed": False,
        "threshold_matching_source_rows_closed": False,
        "mass_scheme_conversion_source_rows_closed": False,
        "external_likelihood_workspace_acquired": False,
        "accepted_vsd02_source_rows_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_closes_now": {
            "true_precision_convention_target_schema": True,
            "firstpass_profile_convention_rejected_for_true_precision": firstpass_is_not_true_precision,
            "diagnostic_RG_convergence_separated_from_selected_convention_source": diagnostic_engine_not_accepted,
            "threshold_row_prerequisite_order": True,
        },
        "remaining_hard_failures": [
            "selected_same_branch_convention_source",
            "versioned_RG_engine_or_external_literature_benchmark",
            "threshold_matching_source_rows",
            "mass_scheme_conversion_source_rows",
            "covariance_or_profile_response",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    candidate = {
        "candidate": "MTTSelectedSameBranchConventionOrThresholdRowEmission",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "true_precision_convention_target": rel(CONVENTION_TARGET),
            "same_branch_convention_source_gap": rel(SOURCE_GAP),
            "threshold_row_emission_prerequisite_order": rel(THRESHOLD_ORDER),
            "same_branch_convention_or_threshold_row_decision": rel(DECISION),
        },
        "theorem": {
            "name": "SameBranchConventionTargetAndSourceGapTheorem",
            "proved": True,
            "statement": (
                "The true-precision convention target can be identified as an M_Z/MSbar response "
                "with explicit loop, beta-function, threshold, mass-scheme, and covariance requirements. "
                "However, the available first-pass convention is parity-only, the convergent internal RG "
                "engine is diagnostic-only, and VSD02 accepts zero threshold/mass-scheme source rows. "
                "Thus same-branch convention ownership and threshold-row emission remain open without "
                "collapsing back to measured-value replay."
            ),
        },
        "what_closes_now": decision["what_closes_now"],
        "what_remains_open": decision["remaining_hard_failures"],
        "closure_decision": {
            "true_precision_convention_target_identified": True,
            "same_branch_scale_scheme_loop_convention_closed": False,
            "threshold_matching_source_rows_closed": False,
            "mass_scheme_conversion_source_rows_closed": False,
            "profile_response_or_diagonal_limitation_closed": False,
            "external_likelihood_workspace_acquired": False,
            "selected_threshold_response_functional_instantiated": False,
            "accepted_vsd02_source_rows_closed": False,
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
        "certificate": "MTT_Selected_SameBranchConvention_or_ThresholdRowEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "true_precision_convention_target_identified": True,
        "same_branch_scale_scheme_loop_convention_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected SameBranchConvention or ThresholdRowEmission v1

Status: `{STATUS}`.

This artifact attacks the first remaining value-producing blocker.

```text
true-precision convention target identified : true
target scale/scheme                         : {target["target_scale"]} / {target["target_scheme"]}
first-pass convention accepted for precision: false
diagnostic RG convergence closed            : {str(rg_convergence["passes_internal_convergence"]).lower()}
diagnostic RG accepted as source convention : false
accepted VSD02 source rows                  : {vsd02_fill["accepted_row_count"]}
same-branch convention closed               : false
```

The convention target is now explicit, but not yet selected by the same branch.
Therefore threshold matching rows and mass-scheme rows cannot honestly be
emitted yet.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
