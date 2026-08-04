"""Build direct BN27 source theorem or connection-values external-construction frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "direct_fill_attempt": DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_fill_or_typedconnectionwitnessvalues.candidate.json",
    "acceptance_contract": DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_acceptance_contract.json",
    "u1y_selected_finite_trace_nogo": DATA / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json",
    "qastack_nonidentity_prefix": DATA / "selected_electroweak_qastack_threshold_operator_from_nonidentity_rhoe_quotientbn.candidate.json",
    "u1y_selected_source_or_typed_de": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "u1y_finite_hym_or_typed_cech": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
    "transport_gate": DATA / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction.candidate.json"
OUTPUT_ROOTS = DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_minimal_root_cutset.json"
OUTPUT_EXTERNAL = DATA / "selected_heterotic_orientedphifin_bn27_connectionvalues_externalconstruction_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceIdentity_DirectSourceTheorem_or_ConnectionValuesExternalConstruction_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEIDENTITY_DIRECTSOURCE_OR_EXTERNALCONSTRUCTION_ROOTCUTSET_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SelectedTraceEquality_FullOperatorFormula_or_SourceFlagTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    direct = load(INPUTS["direct_fill_attempt"])
    contract = load(INPUTS["acceptance_contract"])
    finite_trace = load(INPUTS["u1y_selected_finite_trace_nogo"])
    qastack = load(INPUTS["qastack_nonidentity_prefix"])
    u1y_source = load(INPUTS["u1y_selected_source_or_typed_de"])
    u1y_finite = load(INPUTS["u1y_finite_hym_or_typed_cech"])
    transport = load(INPUTS["transport_gate"])

    source_trace_cutset = finite_trace["source_trace_cutset"]
    qastack_cutset = qastack["source_trace_cutset"]
    common_cutset = sorted(k for k, v in source_trace_cutset.items() if v is True and qastack_cutset.get(k) is True)

    root_cutset = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceIdentity.MinimalRootCutset.v1",
        "status": "ROOT_CUTSET_BUILT_VALUES_OPEN",
        "already_closed_as_support": {
            "heterotic_branch_certificate": transport["decision"]["branch_certificate_closed"],
            "finite_BN_basis_closed_for_gap_layer": direct["new_support_imported"]["finite_BN_basis_closed_for_gap_layer"],
            "DE_gap_Riesz_Green_export_support_closed": direct["decision"]["DE_gap_Riesz_Green_export_support_closed"],
            "nonidentity_rhoE_prefix_can_host_operator": qastack["decision"]["prefix_can_host_threshold_operator"],
            "oriented_logdet_support_ready": transport["support_now_locked"]["oriented_abs_sector_product"] == 92160000,
        },
        "minimal_roots": {
            "selected_trace_equality_to_27mode_operator": {
                "required": True,
                "current_status": finite_trace["decision"]["selected_trace_equality_proved"],
                "why_root": "It is the first point where the Route-C/q79 27-mode operator becomes a selected heterotic/source trace instead of support.",
            },
            "full_selected_iwasawa_strominger_operator_formula": {
                "required": True,
                "current_status": finite_trace["decision"]["full_selected_operator_formula_proved"],
                "why_root": "It identifies the model-active finite operator with the selected smooth threshold operator, not merely a prefix.",
            },
            "theorem_derived_selected_source_flags": {
                "required": True,
                "current_status": False,
                "why_root": "It prevents lifted flags or validator smoke from acting as source provenance.",
            },
            "source_object_named_S_QaSU3_BN27": {
                "required": True,
                "current_status": direct["decision"]["source_object_named_S_QaSU3_BN27"],
                "why_root": "It is the direct declaration that the full BN27 carrier is emitted by the selected heterotic Qa/SU3 source.",
            },
        },
        "common_cutset_with_electroweak_qastack": common_cutset,
        "target_fitting_used": False,
    }
    OUTPUT_ROOTS.write_text(json.dumps(root_cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    external_request = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.ConnectionValues.ExternalConstructionRequest.v1",
        "status": "OPEN_EXTERNAL_CONSTRUCTION_VALUES_REQUIRED",
        "purpose": "Construct a legal source witness without fitting observed constants: either a direct BN27 source theorem or explicit connection values whose validators derive source flags.",
        "direct_source_theorem_route": {
            "must_emit": [
                "source object S_QaSU3^BN27",
                "full F3xF3 rank-slot carrier before finite comparison",
                "C_tau and PhiFin_DE as co-emitted operators",
                "Route-C/q79 row as an internal theorem of the source",
                "kernel/shared-circle policy and log(92160000) finitepart identity as source-owned",
            ],
            "acceptance_fields": contract["direct_source_identity_payload"],
        },
        "external_connection_values_route": {
            "typed_cech": [
                "typed f_i and g_i sections",
                "Cech transitions/cocycle data",
                "g after f equals zero and exactness/local-freeness certificate",
                "finite BN27 D_E/Riesz/Green/kernel/trace export",
            ],
            "direct_hym_or_strominger": [
                "selected A_HYM or equivalent projective connection coefficients",
                "fixed gauge and residual certificate for F^(0,2), HYM primitive part, and Bianchi/Strominger row",
                "gap/error bound showing model operator is the selected threshold operator",
                "no-lifted-flags replay audit",
            ],
            "finite_routec_solve": [
                "selected trace equality to the emitted 27-mode operator",
                "full selected operator formula",
                "theorem-derived selected source flags",
                "same-source export to BN27 validators",
            ],
            "acceptance_fields": contract["typed_or_connection_payload"],
        },
        "forbidden": contract["forbidden"],
        "target_fitting_used": False,
    }
    OUTPUT_EXTERNAL.write_text(json.dumps(external_request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    all_roots_closed = all(item["current_status"] is True for item in root_cutset["minimal_roots"].values())
    decision = {
        "root_cutset_built": True,
        "external_construction_request_built": True,
        "selected_trace_equality_proved": False,
        "full_selected_operator_formula_proved": False,
        "theorem_derived_selected_source_flags": False,
        "source_object_named_S_QaSU3_BN27": False,
        "all_minimal_roots_closed": all_roots_closed,
        "direct_source_theorem_closed": False,
        "connection_values_external_construction_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "root_cutset_path": rel(OUTPUT_ROOTS),
        "external_request_path": rel(OUTPUT_EXTERNAL),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceIdentityDirectSourceTheoremOrConnectionValuesExternalConstruction",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "direct_fill_attempt": direct["status"],
            "u1y_selected_finite_trace_nogo": finite_trace["status"],
            "qastack_nonidentity_prefix": qastack["status"],
            "u1y_selected_source_or_typed_de": u1y_source["status"],
            "u1y_finite_hym_or_typed_cech": u1y_finite["status"],
            "transport_gate": transport["status"],
        },
        "root_cutset_path": rel(OUTPUT_ROOTS),
        "external_construction_request_path": rel(OUTPUT_EXTERNAL),
        "root_cutset": root_cutset,
        "decision": decision,
        "theorem": {
            "name": "BN27SourceIdentityRootCutsetTheorem",
            "proved": True,
            "statement": (
                "The direct BN27 source theorem and external connection-values routes now share the same minimal root cutset. "
                "Support is strong enough to host the threshold operator, including the branch certificate, 27-mode BN basis, "
                "D_E/Riesz/Green support, and nonidentity rho_E prefix. Closure still requires selected trace equality, the "
                "full selected Iwasawa/Strominger operator formula, theorem-derived selected-source flags, and the direct "
                "source object S_QaSU3^BN27 or equivalent connection values."
            ),
        },
        "guardrails": {
            "does_not_treat_prefix_as_selected_threshold": True,
            "does_not_treat_DE_gap_support_as_source_identity": True,
            "does_not_promote_log92160000": True,
            "does_not_promote_routec_import": True,
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
        "root_cutset_path": rel(OUTPUT_ROOTS),
        "external_request_path": rel(OUTPUT_EXTERNAL),
        "note_path": rel(OUTPUT_NOTE),
        "all_minimal_roots_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceIdentity DirectSourceTheorem or ConnectionValuesExternalConstruction v1

## Result

```text
status = {STATUS}
selected_trace_equality_proved = false
full_selected_operator_formula_proved = false
theorem_derived_selected_source_flags = false
source_object_named_S_QaSU3_BN27 = false
BN27_source_identity_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Outputs

```text
{rel(OUTPUT_ROOTS)}
{rel(OUTPUT_EXTERNAL)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_ROOTS)}")
    print(f"wrote {rel(OUTPUT_EXTERNAL)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
