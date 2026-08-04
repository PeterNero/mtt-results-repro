"""Build selected threshold response functional derivation / likelihood acquisition gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FUNCTIONAL_CONTRACT = PACKET_DIR / "selected_threshold_response_functional_contract.packet.json"
INSTANTIATION_AUDIT = PACKET_DIR / "current_repo_functional_instantiation_audit.packet.json"
LIKELIHOOD_GATE = PACKET_DIR / "profile_likelihood_acquisition_gate.packet.json"
DECISION = PACKET_DIR / "threshold_response_functional_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_response_functional_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdResponseFunctionalDerivation_or_ProfileLikelihoodAcquisition_v1.md"

PREVIOUS = DATA / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation.candidate.json"
REDUCTION = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "no_knob_threshold_derivation_reduction.packet.json"
)
FILL_DECISION = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "vsd02_accepted_rows_fill_decision.packet.json"
)
INTERNAL_WORKORDER = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "internal_threshold_response_derivation_workorder.packet.json"
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
THRESHOLD_RESIDUALS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
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
PROFILE_STATUS = (
    DATA
    / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
    / "profile_likelihood_source_import_status.packet.json"
)
QASU3_PACKET = DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"

STATUS = (
    "MTT_SELECTED_THRESHOLDRESPONSEFUNCTIONALDERIVATION_OR_PROFILELIKELIHOODACQUISITION_"
    "BUILT_CONTRACT_INSTANTIATION_OPEN"
)
NEXT = "MTT_Selected_ResponseFunctionalInstantiation_or_ExternalWorkspaceIngest_v1"


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
        raise FileNotFoundError(
            "missing threshold response functional sources: " + ", ".join(missing)
        )


def audit_requirement(requirement_id: str, present: bool, source: str, missing: list[str]) -> dict[str, Any]:
    return {
        "id": requirement_id,
        "present": present,
        "source": source,
        "missing_for_acceptance": missing if not present else [],
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        REDUCTION,
        FILL_DECISION,
        INTERNAL_WORKORDER,
        EXTERNAL_MANIFEST,
        VALUE_PACKET,
        THRESHOLD_RESIDUALS,
        SOURCE_ROW_AUDIT,
        NO_KNOB_ATTEMPT,
        PROFILE_STATUS,
        QASU3_PACKET,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    reduction = load(REDUCTION)
    fill_decision = load(FILL_DECISION)
    internal = load(INTERNAL_WORKORDER)
    external = load(EXTERNAL_MANIFEST)
    value_packet = load(VALUE_PACKET)
    residuals = load(THRESHOLD_RESIDUALS)
    source_audit = load(SOURCE_ROW_AUDIT)
    no_knob = load(NO_KNOB_ATTEMPT)
    profile_status = load(PROFILE_STATUS)
    qasu3 = load(QASU3_PACKET)

    functional_contract = {
        "schema": "MTTSelectedThresholdResponseFunctionalContract.v1",
        "status": "SELECTED_THRESHOLD_RESPONSE_FUNCTIONAL_CONTRACT_EMITTED",
        "functional_symbol": "R_theta",
        "informal_map": (
            "R_theta maps the selected MTT dynamic/operator packet, branch labels, and finite "
            "normalization data to threshold matching rows, mass-scheme conversion rows, and an "
            "accepted covariance/profile response without using observed values as selectors."
        ),
        "domain_required": [
            "selected MTT branch identifier and quotient/sector data",
            "selected dynamic/operator packet or source-owner theorem",
            "scale and scheme convention before observed-value comparison",
            "finite normalization/transport data from the same branch",
            "basis map from MTT rows to SM value packet coordinates",
        ],
        "codomain_required": internal["minimal_internal_derivation_outputs_required"],
        "row_outputs_required": {
            "threshold_matching": [
                "top",
                "bottom",
                "charm",
                "tau",
                "W_Z_H",
            ],
            "mass_scheme_conversion": [
                "top direct/pole/running convention map",
                "bottom MSbar native-scale transport",
                "charm MSbar native-scale transport",
                "tau pole/rest to running-lepton convention",
                "Higgs pole/running lambda convention",
            ],
            "profile_response": [
                "full covariance/profile likelihood payload",
                "or accepted diagonal limitation theorem with stated loss",
            ],
        },
        "acceptance_equations": [
            "R_theta is selected before comparison with measured masses, Yukawas, gauge couplings, or CKM/PMNS values.",
            "Each emitted row carries scale, scheme, loop/order convention, and basis-map metadata.",
            "Residual tables may validate R_theta outputs but cannot define R_theta.",
            "External likelihood rows must include provenance, parameter basis, nuisance/profile semantics, and replay command.",
            "The same branch must own the source rows and the value packet attachment.",
        ],
        "forbidden_shortcuts": reduction["minimal_new_theorem_required"]["must_not_use"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FUNCTIONAL_CONTRACT, functional_contract)

    instantiation_requirements = [
        audit_requirement(
            "selected_dynamic_operator_source_owner",
            False,
            rel(QASU3_PACKET),
            [
                "Qa/SU3 parity packet is present, but it is not an accepted VSD02 threshold response source-owner theorem.",
            ],
        ),
        audit_requirement(
            "same_branch_scale_scheme_loop_convention",
            value_packet["accepted_for_true_precision_equivalence"],
            rel(VALUE_PACKET),
            [
                "versioned common-scale packet exists only as first-pass/parity profile input, not true precision source convention.",
            ],
        ),
        audit_requirement(
            "threshold_matching_source_rows",
            bool(source_audit["accepted_threshold_matching_source_rows"]),
            rel(SOURCE_ROW_AUDIT),
            [
                "accepted threshold matching source rows are empty",
                "finite residuals validate downstream comparisons but do not supply the source rule",
            ],
        ),
        audit_requirement(
            "mass_scheme_conversion_source_rows",
            bool(source_audit["accepted_mass_scheme_conversion_source_rows"]),
            rel(SOURCE_ROW_AUDIT),
            [
                "accepted mass-scheme conversion source rows are empty",
            ],
        ),
        audit_requirement(
            "finite_residual_validation_support",
            residuals["summary"]["all_residuals_finite"],
            rel(THRESHOLD_RESIDUALS),
            [],
        ),
        audit_requirement(
            "no_knob_value_derivation",
            no_knob["no_knob_value_derivation_closed"],
            rel(NO_KNOB_ATTEMPT),
            no_knob["why_not_proved_now"],
        ),
        audit_requirement(
            "full_profile_likelihood_or_accepted_diagonal_theorem",
            False,
            rel(EXTERNAL_MANIFEST),
            external["required_import_payload"],
        ),
    ]
    accepted_instantiation = all(row["present"] for row in instantiation_requirements)

    instantiation_audit = {
        "schema": "MTTCurrentRepoThresholdResponseFunctionalInstantiationAudit.v1",
        "status": "CURRENT_REPO_INSTANTIATION_AUDITED_FUNCTIONAL_NOT_INSTANTIATED",
        "functional_contract": rel(FUNCTIONAL_CONTRACT),
        "requirements": instantiation_requirements,
        "requirement_count": len(instantiation_requirements),
        "present_count": sum(1 for row in instantiation_requirements if row["present"]),
        "accepted_threshold_response_functional_instantiated": accepted_instantiation,
        "positive_support": [
            "strict functional contract emitted",
            "finite residual validation support exists",
            "versioned first-pass value packet exists for parity/profile replay",
        ],
        "blocking_failures": [
            row["id"] for row in instantiation_requirements if not row["present"]
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INSTANTIATION_AUDIT, instantiation_audit)

    likelihood_gate = {
        "schema": "MTTProfileLikelihoodAcquisitionGate.v1",
        "status": "PROFILE_LIKELIHOOD_ACQUISITION_GATE_BUILT_FULL_WORKSPACE_ABSENT",
        "full_profile_likelihood_imported_now": external[
            "accepted_external_likelihood_imported_now"
        ],
        "profile_status": profile_status["status"],
        "partial_rows_present": external["partial_external_rows"],
        "required_for_acquisition": external["required_import_payload"],
        "official_likelihood_required_payload": external[
            "official_likelihood_required_payload"
        ],
        "accepted_as_external_escape_hatch": False,
        "reason_not_accepted": [
            "partial Higgs covariance and published profile replay are support rows only",
            "no full non-Higgs covariance/profile likelihood workspace is imported",
            "no official machine-readable likelihood with nuisance/profile semantics is present",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(LIKELIHOOD_GATE, likelihood_gate)

    decision = {
        "schema": "MTTThresholdResponseFunctionalDecision.v1",
        "status": "FUNCTIONAL_CONTRACT_CLOSED_INSTANTIATION_AND_LIKELIHOOD_OPEN",
        "previous_status": previous["status"],
        "fill_attempt_accepted_rows": fill_decision["accepted_row_count"],
        "functional_contract_closed": True,
        "current_repo_instantiation_audited": True,
        "selected_threshold_response_functional_instantiated": False,
        "profile_likelihood_workspace_acquired": False,
        "accepted_vsd02_source_rows_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "what_closes_now": {
            "selected_response_functional_contract": True,
            "current_repo_instantiation_audit": True,
            "profile_likelihood_acquisition_gate": True,
            "old_proxy_routes_rejected_again_under_functional_contract": True,
        },
        "remaining_hard_failures": instantiation_audit["blocking_failures"],
        "minimal_next_object": {
            "internal_route": "instantiate R_theta with same-branch source-owner theorem and row coefficients",
            "external_route": "ingest full likelihood/profile workspace with provenance and basis map",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterThresholdResponseFunctionalGate.v1",
        "status": "NEXT_ATTACK_INSTANTIATE_R_THETA_OR_INGEST_EXTERNAL_WORKSPACE",
        "closed_now": decision["what_closes_now"],
        "still_open": decision["remaining_hard_failures"],
        "recommended_next": {
            "artifact": NEXT,
            "internal_route": [
                "select the source-owner theorem for R_theta",
                "emit row coefficient/formula payloads for threshold and mass-scheme maps",
                "attach covariance response or diagonal limitation theorem",
                "run the accepted-row schema against the emitted rows",
            ],
            "external_route": likelihood_gate["required_for_acquisition"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedThresholdResponseFunctionalDerivationOrProfileLikelihoodAcquisition",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "selected_threshold_response_functional_contract": rel(FUNCTIONAL_CONTRACT),
            "current_repo_functional_instantiation_audit": rel(INSTANTIATION_AUDIT),
            "profile_likelihood_acquisition_gate": rel(LIKELIHOOD_GATE),
            "threshold_response_functional_decision": rel(DECISION),
            "next_cutset_after_threshold_response_functional_gate": rel(CUTSET),
        },
        "theorem": {
            "name": "SelectedThresholdResponseFunctionalContractAndInstantiationAuditTheorem",
            "proved": True,
            "statement": (
                "The missing VSD02 object can be sharpened to an explicit selected threshold response "
                "functional contract R_theta. The current repository can be audited against that contract. "
                "It supplies finite residual support and first-pass value packets, but it does not instantiate "
                "R_theta and does not import a full profile likelihood workspace. Therefore true SM equivalence "
                "and full no-knob closure remain open without overclaim."
            ),
        },
        "what_closes_now": decision["what_closes_now"],
        "what_remains_open": decision["remaining_hard_failures"],
        "closure_decision": {
            "functional_contract_closed": True,
            "selected_threshold_response_functional_instantiated": False,
            "external_likelihood_workspace_acquired": False,
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
        "certificate": "MTT_Selected_ThresholdResponseFunctionalDerivation_or_ProfileLikelihoodAcquisition_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdResponseFunctionalDerivation or ProfileLikelihoodAcquisition v1

Status: `{STATUS}`.

This artifact closes the contract for the missing VSD02 object.

```text
functional contract emitted       : true
current repo instantiation audited: true
R_theta instantiated              : false
external profile workspace present: false
```

What is now known: the missing object is not a vague threshold layer. It is the
selected response functional `R_theta`, mapping same-branch MTT source/operator
data to threshold matching, mass-scheme, and profile-response rows before any
observed value comparison.

The current repo does not yet instantiate `R_theta`. Finite residuals and
first-pass value packets remain useful validation support, but they are not the
source functional.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
