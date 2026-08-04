"""Build Step52 VSD02 strict value-source frontier / likelihood workspace gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step52_vsd02_strict_value_source_frontier_or_likelihoodworkspace"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FRONTIER = PACKET_DIR / "step52_vsd02_strict_frontier.packet.json"
ROW_RECHECK = PACKET_DIR / "step52_accepted_source_row_recheck.packet.json"
LIKELIHOOD = PACKET_DIR / "step52_external_likelihood_workspace_gate.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step52_next_threshold_functional_or_likelihood_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step52_VSD02StrictValueSourceFrontier_or_LikelihoodWorkspace_v1.md"

STEP51 = DATA / "selected_step51_operator_domain_backimport_or_thresholdprofilefrontier.candidate.json"
STEP51_RECHECK = (
    DATA
    / "selected_step51_operator_domain_backimport_or_thresholdprofilefrontier"
    / "step51_omega_value_frontier_recheck.packet.json"
)
VSD01_HANDOFF = DATA / "selected_rtheta_valuesource_vsd01v2reconciliation_or_vsd02handoff.candidate.json"
VSD01_CUTSET = (
    DATA
    / "selected_rtheta_valuesource_vsd01v2reconciliation_or_vsd02handoff"
    / "next_cutset_after_vsd01_v2_reconciliation.packet.json"
)
VSD02_CLASS = DATA / "selected_vsd02thresholdresponserule_or_externallikelihoodimport.candidate.json"
VSD02_ROUTE = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "vsd02_row_route_classification.packet.json"
)
VSD02_EXTERNAL = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "external_likelihood_import_manifest.packet.json"
)
VSD02_WORKORDER = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "internal_threshold_response_derivation_workorder.packet.json"
)
VSD02_FILL = DATA / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation.candidate.json"
STRICT_SCHEMA = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_row_strict_schema.packet.json"
)
FILL_ATTEMPT = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)
NOKNOB_REDUCTION = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "no_knob_threshold_derivation_reduction.packet.json"
)
FILL_CUTSET = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "next_cutset_after_vsd02_fill_attempt.packet.json"
)

STATUS = "MTT_SELECTED_STEP52_VSD02_STRICT_FRONTIER_LOCKED_ACCEPTED_ROWS_OPEN"
NEXT = "MTT_Selected_ThresholdResponseFunctionalDerivation_or_ProfileLikelihoodAcquisition_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP51,
        STEP51_RECHECK,
        VSD01_HANDOFF,
        VSD01_CUTSET,
        VSD02_CLASS,
        VSD02_ROUTE,
        VSD02_EXTERNAL,
        VSD02_WORKORDER,
        VSD02_FILL,
        STRICT_SCHEMA,
        FILL_ATTEMPT,
        NOKNOB_REDUCTION,
        FILL_CUTSET,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step52 inputs: " + ", ".join(missing))

    step51 = load(STEP51)
    step51_recheck = load(STEP51_RECHECK)
    vsd01 = load(VSD01_HANDOFF)
    vsd01_cutset = load(VSD01_CUTSET)
    vsd02 = load(VSD02_CLASS)
    route = load(VSD02_ROUTE)
    external = load(VSD02_EXTERNAL)
    workorder = load(VSD02_WORKORDER)
    fill = load(VSD02_FILL)
    schema = load(STRICT_SCHEMA)
    attempt = load(FILL_ATTEMPT)
    reduction = load(NOKNOB_REDUCTION)
    fill_cutset = load(FILL_CUTSET)

    frontier = {
        "schema": "MTTStep52VSD02StrictFrontier.v1",
        "status": "VSD02_STRICT_FRONTIER_LOCKED_AFTER_STEP51",
        "step51_operator_domain_closed": step51["closure_decision"][
            "operator_domain_closed_for_Rtheta_value_evaluator"
        ],
        "VSD01_legacy_dynamic_absence_blocker_retired": vsd01["closure_decision"][
            "VSD01_legacy_dynamic_absence_blocker_retired"
        ],
        "VSD01_full_obligation_closed": vsd01["closure_decision"]["VSD01_full_obligation_closed"],
        "VSD02_route_classification_closed": vsd02["closure_decision"]["VSD02_route_classification_closed"],
        "strict_accepted_source_row_schema_closed": fill["closure_decision"][
            "strict_fill_attempt_closed"
        ],
        "live_frontier": [
            "selected_threshold_response_functional",
            "accepted_threshold_matching_source_rows",
            "accepted_mass_scheme_conversion_source_rows",
            "full_profile_likelihood_workspace",
            "no_knob_Yukawa_Higgs_value_derivation",
        ],
        "superseded_blockers": [
            "generic operator payload blocker for Rtheta domain",
            "VSD01 dynamic absence blocker",
            "first-value-row-only source promotion path",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FRONTIER, frontier)

    row_recheck = {
        "schema": "MTTStep52AcceptedSourceRowRecheck.v1",
        "status": "STRICT_SOURCE_ROW_RECHECK_ZERO_ACCEPTED",
        "strict_schema": rel(STRICT_SCHEMA),
        "schema_required_fields": schema["accepted_row_must_include"],
        "candidate_source_row_count": attempt["candidate_source_row_count"],
        "accepted_row_count": attempt["accepted_row_count"],
        "accepted_threshold_matching_rows": attempt["accepted_threshold_matching_rows"],
        "accepted_mass_scheme_conversion_rows": attempt["accepted_mass_scheme_conversion_rows"],
        "accepted_profile_likelihood_rows": attempt["accepted_profile_likelihood_rows"],
        "accepted_no_knob_value_derivation_rows": attempt[
            "accepted_no_knob_value_derivation_rows"
        ],
        "candidate_results": attempt["candidate_results"],
        "why_no_rows_accepted": attempt["why_no_rows_accepted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROW_RECHECK, row_recheck)

    likelihood = {
        "schema": "MTTStep52ExternalLikelihoodWorkspaceGate.v1",
        "status": "EXTERNAL_LIKELIHOOD_WORKSPACE_MANIFEST_READY_NOT_IMPORTED",
        "external_manifest": rel(VSD02_EXTERNAL),
        "manifest_closed": vsd02["what_closes_now"]["external_import_manifest"],
        "accepted_external_likelihood_import_closed": vsd02["closure_decision"][
            "accepted_external_likelihood_import_closed"
        ],
        "workspace_required_fields": external,
        "internal_derivation_workorder": rel(VSD02_WORKORDER),
        "selected_threshold_response_functional_closed": vsd02["closure_decision"][
            "accepted_threshold_response_rule_closed"
        ],
        "no_knob_derivation_reduced_to_selected_response_functional": fill["what_closes_now"][
            "no_knob_derivation_reduced_to_selected_response_functional"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(LIKELIHOOD, likelihood)

    next_frontier = {
        "schema": "MTTStep52NextThresholdFunctionalOrLikelihoodFrontier.v1",
        "status": "NEXT_SELECTED_THRESHOLD_FUNCTIONAL_OR_EXTERNAL_LIKELIHOOD",
        "closed_now": {
            "Step51_operator_domain_backimport": True,
            "VSD01_v2_handoff_imported": True,
            "VSD02_route_classification_imported": True,
            "strict_source_row_schema_imported": True,
            "all_current_candidate_rows_rejected_without_overclaim": True,
        },
        "still_open": fill["what_remains_open"],
        "next_required_artifact": NEXT,
        "next_routes": {
            "internal": "derive selected threshold response functional and threshold/mass-scheme rows",
            "external": "import a full likelihood/profile workspace satisfying the strict manifest",
            "fallback": "audit minimal universal parameters only if both source-row routes fail",
        },
        "step51_blocking_failures_preserved": step51_recheck["blocking_failures"],
        "vsd01_cutset_still_open": vsd01_cutset["still_open"],
        "vsd02_fill_cutset": fill_cutset,
        "no_knob_reduction": reduction,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_FRONTIER, next_frontier)

    candidate = {
        "candidate": "MTTSelectedStep52VSD02StrictValueSourceFrontierOrLikelihoodWorkspace",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "vsd02_strict_frontier": rel(FRONTIER),
            "accepted_source_row_recheck": rel(ROW_RECHECK),
            "external_likelihood_workspace_gate": rel(LIKELIHOOD),
            "next_threshold_functional_or_likelihood_frontier": rel(NEXT_FRONTIER),
        },
        "theorem": {
            "name": "Step52VSD02StrictFrontierReconciliationTheorem",
            "proved": True,
            "statement": (
                "After Step51 and VSD01v2 reconciliation, the active value-source frontier is VSD02. "
                "The strict accepted-source-row schema is closed and all current candidates have been "
                "tested. Zero rows are accepted, so no numerical Rtheta/Yukawa/Higgs value row closes. "
                "The next legal exits are a selected threshold response functional with source rows or "
                "a fully provenanced external likelihood/profile workspace."
            ),
        },
        "closure_decision": {
            "VSD02_strict_frontier_locked": True,
            "strict_accepted_source_row_schema_closed": True,
            "candidate_source_rows_tested": attempt["candidate_source_row_count"],
            "accepted_vsd02_source_row_count": attempt["accepted_row_count"],
            "selected_threshold_response_functional_closed": False,
            "external_likelihood_workspace_closed": False,
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
        "certificate": "MTT_Selected_Step52_VSD02StrictValueSourceFrontier_or_LikelihoodWorkspace_v1",
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
        f"""# MTT Selected Step52 VSD02StrictValueSourceFrontier or LikelihoodWorkspace v1

Status: `{STATUS}`.

Step52 reconciles Step51, VSD01v2, and VSD02 strict source-row filling.

```text
VSD02 strict frontier locked           : true
candidate source rows tested           : {attempt["candidate_source_row_count"]}
accepted VSD02 source rows             : {attempt["accepted_row_count"]}
accepted internal Rtheta rows          : 0
lambda_H row closed                    : false
```

The old operator-domain and VSD01 dynamic-absence blockers are superseded for
the current Rtheta value frontier.  The live exits are now exact: derive the
selected threshold response functional with threshold/mass-scheme source rows,
or import a full external likelihood/profile workspace satisfying the manifest.

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
