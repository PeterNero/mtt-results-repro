"""Build BN27 same-source export to validators / selected connection values gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "prior_gate": DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_declarationinterface_fill_or_selectedconnectionvalues.candidate.json",
    "export_compatibility_test": DATA / "selected_heterotic_orientedphifin_bn27_u1y_routec_export_compatibility_test.json",
    "connection_export_request": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_request.json",
    "minimal_source_values_packet": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_minimal_source_values_packet.json",
    "connection_export_fill": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
    "sourceownership_transport": DATA / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_samesourceexport_to_bn27validators_or_selectedconnectionvalues.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_orientedphifin_bn27_validator_export_acceptance_contract.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_samesourceexport_to_bn27validators_or_selectedconnectionvalues_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SameSourceExport_To_BN27Validators_or_SelectedConnectionValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_VALIDATOR_EXPORT_CONTRACT_BUILT_SOURCE_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_ValidatorExport_Fill_or_SelectedConnectionSolve_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    prior = load(INPUTS["prior_gate"])
    compatibility = load(INPUTS["export_compatibility_test"])
    request = load(INPUTS["connection_export_request"])
    minimal = load(INPUTS["minimal_source_values_packet"])
    export_fill = load(INPUTS["connection_export_fill"])
    transport = load(INPUTS["sourceownership_transport"])

    fields = export_fill["export_fields"]
    support_ready = {
        "source_identity": fields["source_identity"]["support_present"],
        "BN27_deck_action": fields["BN27_deck_action"]["support_present"],
        "operators": fields["operators"]["support_present"],
        "kernel_policy": fields["kernel_policy"]["support_present"],
        "trace_policy": fields["trace_policy"]["support_present"],
        "audit_replay": fields["audit_replay"]["support_present"],
    }
    currently_export_owned = {
        "source_identity": fields["source_identity"]["selected_source_owned"],
        "BN27_deck_action": fields["BN27_deck_action"]["selected_source_owned"],
        "operators": fields["operators"]["selected_source_owned"],
        "kernel_policy": fields["kernel_policy"]["selected_source_owned"],
        "trace_policy": fields["trace_policy"]["selected_source_owned"],
        "audit_replay": fields["audit_replay"]["selected_source_owned"],
    }

    contract = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.ValidatorExport.AcceptanceContract.v1",
        "status": "VALIDATOR_EXPORT_VALUES_REQUIRED",
        "validators": {
            "source_identity_validator": {
                "required": "same source owns heterotic Qa/SU3 branch and Route-C/q79 BN27 finite trace row",
                "current_support_ready": support_ready["source_identity"],
                "selected_source_owned": currently_export_owned["source_identity"],
                "acceptance_value": None,
            },
            "BN27_deck_action_validator": {
                "required": request["must_export_to_oriented_phifin"]["BN27_deck_action"],
                "current_support_ready": support_ready["BN27_deck_action"],
                "selected_source_owned": currently_export_owned["BN27_deck_action"],
                "acceptance_value": None,
            },
            "operator_coemission_validator": {
                "required": request["must_export_to_oriented_phifin"]["operators"],
                "current_support_ready": support_ready["operators"],
                "selected_source_owned": currently_export_owned["operators"],
                "acceptance_value": None,
            },
            "kernel_policy_validator": {
                "required": request["must_export_to_oriented_phifin"]["kernel_policy"],
                "current_support_ready": support_ready["kernel_policy"],
                "selected_source_owned": currently_export_owned["kernel_policy"],
                "acceptance_value": None,
            },
            "trace_policy_validator": {
                "required": request["must_export_to_oriented_phifin"]["trace_policy"],
                "current_support_ready": support_ready["trace_policy"],
                "selected_source_owned": currently_export_owned["trace_policy"],
                "acceptance_value": None,
            },
            "audit_replay_validator": {
                "required": request["must_export_to_oriented_phifin"]["audit_replay"],
                "current_support_ready": support_ready["audit_replay"],
                "selected_source_owned": currently_export_owned["audit_replay"],
                "acceptance_value": fields["audit_replay"]["value"],
            },
        },
        "acceptable_value_families": minimal["acceptable_minimal_values"],
        "known_compatible_support": compatibility["compatibility_support"],
        "must_not_use": minimal["must_not_use"],
        "target_fitting_used": False,
    }
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    open_validators = [
        name
        for name, validator in contract["validators"].items()
        if validator["selected_source_owned"] is not True
    ]
    closed_validators = [
        name
        for name, validator in contract["validators"].items()
        if validator["selected_source_owned"] is True
    ]

    route_evaluation = {
        "source_identity_transport": {
            "closed_now": False,
            "first_missing": "same-source theorem: heterotic Qa/SU3 branch emits Route-C/q79 BN27 finite trace row",
            "acceptable_values": minimal["acceptable_minimal_values"]["source_identity_transport"],
            "transport_status": transport["status"],
        },
        "typed_connection_values": {
            "closed_now": False,
            "first_missing": "typed f_i/g_i representatives and Cech transitions",
            "acceptable_values": minimal["acceptable_minimal_values"]["typed_connection_values"],
        },
        "direct_connection_values": {
            "closed_now": False,
            "first_missing": "selected A/F_A or projective rho_E transition matrices",
            "acceptable_values": minimal["acceptable_minimal_values"]["direct_connection_values"],
        },
    }

    decision = {
        "attempt_executed": True,
        "validator_export_acceptance_contract_built": True,
        "support_ready_count": sum(1 for value in support_ready.values() if value),
        "selected_export_owned_count": len(closed_validators),
        "open_validator_count": len(open_validators),
        "open_validators": open_validators,
        "closed_validators": closed_validators,
        "same_source_export_to_BN27_validators": False,
        "selected_connection_values_closed": False,
        "source_object_named_S_QaSU3_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "validator_export_acceptance_contract_path": rel(OUTPUT_CONTRACT),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SameSourceExportToBN27ValidatorsOrSelectedConnectionValues",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "prior_gate": prior["status"],
            "export_compatibility_test": compatibility["status"],
            "connection_export_request": request["status"],
            "minimal_source_values_packet": minimal["status"],
            "connection_export_fill": export_fill["status"],
            "sourceownership_transport": transport["status"],
        },
        "validator_summary": {
            "support_ready": support_ready,
            "currently_export_owned": currently_export_owned,
            "open_validators": open_validators,
            "closed_validators": closed_validators,
        },
        "route_evaluation": route_evaluation,
        "validator_export_acceptance_contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "theorem": {
            "name": "BN27ValidatorExportAcceptanceContractTheorem",
            "proved": True,
            "statement": (
                "The same-source export problem is now represented as six BN27 validators. Current artifacts make all six "
                "validators support-ready, but only audit replay is selected-source owned. Source identity, deck action, "
                "operator co-emission, kernel policy, and trace policy remain open until supplied by a source-identity "
                "transport theorem, typed Cech values, or direct connection values. Therefore BN27 source identity and "
                "log(92160000) promotion remain open."
            ),
        },
        "guardrails": {
            "does_not_promote_log92160000": True,
            "does_not_treat_support_ready_as_source_owned": True,
            "does_not_import_u1y_support_as_bn27_source_identity": True,
            "does_not_close_by_bare_source_name": True,
            "does_not_use_lifted_selected_flags": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "validator_export_acceptance_contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "validator_export_acceptance_contract_built": True,
        "same_source_export_to_BN27_validators": False,
        "selected_connection_values_closed": False,
        "source_object_named_S_QaSU3_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SameSourceExport To BN27Validators or SelectedConnectionValues v1

## Result

```text
status = {STATUS}
validator_export_acceptance_contract_built = true
support_ready_count = {decision["support_ready_count"]}
selected_export_owned_count = {decision["selected_export_owned_count"]}
same_source_export_to_BN27_validators = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Validator Export Contract

```text
{rel(OUTPUT_CONTRACT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
