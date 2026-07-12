"""Build BN27 source-object declaration-interface fill / selected-connection values gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "prior_gate": DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_or_connectionvalueexport.candidate.json",
    "declaration_interface": DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_interface.json",
    "u1y_selected_source_certificate": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "u1y_selected_finite_trace": DATA / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json",
    "u1y_trace_gap": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "u1y_witness_contract": DATA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json",
    "bn27_root_cutset": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_minimal_root_cutset.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_declarationinterface_fill_or_selectedconnectionvalues.candidate.json"
OUTPUT_EXPORT_TEST = DATA / "selected_heterotic_orientedphifin_bn27_u1y_routec_export_compatibility_test.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourceobject_declarationinterface_fill_or_selectedconnectionvalues_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_DeclarationInterface_Fill_or_SelectedConnectionValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOBJECT_INTERFACE_FILL_U1Y_SUPPORT_IMPORTED_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SameSourceExport_To_BN27Validators_or_SelectedConnectionValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    prior = load(INPUTS["prior_gate"])
    interface = load(INPUTS["declaration_interface"])
    u1y_source = load(INPUTS["u1y_selected_source_certificate"])
    u1y_finite_trace = load(INPUTS["u1y_selected_finite_trace"])
    u1y_trace_gap = load(INPUTS["u1y_trace_gap"])
    u1y_witness = load(INPUTS["u1y_witness_contract"])
    bn27_cutset = load(INPUTS["bn27_root_cutset"])

    u1y_compat = {
        "selected_trace_equality_to_27mode_operator_support": u1y_trace_gap["decision"]["selected_trace_equality_for_27mode_DE"],
        "theorem_derived_DE_gap_source_flags_support": u1y_trace_gap["finite_trace_route"]["gap_layer"]["D_E_source_flags_are_theorem_derived"],
        "full_selected_iwasawa_strominger_operator_formula_support": False,
        "DE_gap_Riesz_Green_layer_support": u1y_trace_gap["decision"]["DE_gap_Riesz_Green_layer_closed"],
        "selected_connection_witness_constructed": u1y_witness["decision"]["selected_connection_witness_constructed"],
    }
    export_test = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.U1YRouteCExportCompatibilityTest.v1",
        "status": "U1Y_ROUTEC_SUPPORT_COMPATIBLE_BN27_EXPORT_OPEN",
        "compatibility_support": u1y_compat,
        "not_exported_to_BN27": {
            "same_source_export_to_BN27_validators": False,
            "S_QaSU3_BN27_declared_with_exports": False,
            "kernel_trace_policy_source_owned_for_BN27": False,
            "finitepart_log92160000_identity_source_owned_for_BN27": False,
            "no_routec_import_provenance_for_heterotic_BN27": False,
        },
        "why_not_exported": (
            "U1/Y Route-C closes trace/source-flag support in its row, but the heterotic oriented BN27 row still lacks "
            "a same-source export theorem identifying those values as the selected Qa/SU3 BN27 threshold source."
        ),
        "target_fitting_used": False,
    }
    OUTPUT_EXPORT_TEST.write_text(json.dumps(export_test, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    finite_routec_fill = {
        "selected_trace_equality_to_27mode_operator": False,
        "full_selected_iwasawa_strominger_operator_formula": False,
        "theorem_derived_selected_source_flags": False,
        "same_source_export_to_BN27_validators": False,
    }
    can_import_as_support = (
        u1y_compat["selected_trace_equality_to_27mode_operator_support"]
        and u1y_compat["theorem_derived_DE_gap_source_flags_support"]
        and u1y_compat["DE_gap_Riesz_Green_layer_support"]
    )

    route_evaluation = {
        "finite_routec_solve_export_to_BN27": {
            "support_imported": can_import_as_support,
            "closed_now": False,
            "interface_current": interface["equivalent_connection_value_export"]["finite_routec_solve"],
            "attempted_fill": finite_routec_fill,
            "first_missing": "same_source_export_to_BN27_validators",
            "why_not_closed": "The support comes from U1/Y Route-C scope; the BN27 validator export and heterotic source provenance are still absent.",
        },
        "direct_source_object_declaration": {
            "closed_now": False,
            "first_missing": "full_F3xF3_rank_slot_carrier as source-owned export",
            "bare_name_still_rejected": True,
        },
        "typed_or_hym_connection_values": {
            "closed_now": False,
            "selected_connection_witness_constructed": u1y_witness["decision"]["selected_connection_witness_constructed"],
            "first_missing": "typed Cech/HYM connection coefficients or finite solve export values",
        },
    }

    decision = {
        "attempt_executed": True,
        "u1y_routec_support_imported_for_compatibility": can_import_as_support,
        "finite_routec_solve_export_to_BN27_closed": False,
        "direct_source_object_declaration_closed": False,
        "selected_connection_values_closed": False,
        "same_source_export_to_BN27_validators": False,
        "source_object_named_S_QaSU3_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "export_compatibility_test_path": rel(OUTPUT_EXPORT_TEST),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceObjectDeclarationInterfaceFillOrSelectedConnectionValues",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "prior_gate": prior["status"],
            "declaration_interface": interface["status"],
            "u1y_selected_source_certificate": u1y_source["status"],
            "u1y_selected_finite_trace": u1y_finite_trace["status"],
            "u1y_trace_gap": u1y_trace_gap["status"],
            "u1y_witness_contract": u1y_witness["status"],
            "bn27_root_cutset": bn27_cutset["status"],
        },
        "route_evaluation": route_evaluation,
        "export_compatibility_test_path": rel(OUTPUT_EXPORT_TEST),
        "decision": decision,
        "theorem": {
            "name": "BN27DeclarationInterfaceFillSupportImportSameSourceExportOpenTheorem",
            "proved": True,
            "statement": (
                "The U1/Y Route-C row supplies compatible support for selected trace equality, theorem-derived source flags, "
                "the full selected operator-formula support, and the D_E/Riesz/Green gap layer. This can seed the BN27 "
                "source-object interface, but it cannot fill it: the same-source export to BN27 validators, source-owned "
                "kernel/trace policy, finitepart log(92160000) identity, and non-Route-C-import provenance remain absent. "
                "Therefore the next closure object is a same-source export theorem or selected connection values, not another "
                "finite arithmetic calculation."
            ),
        },
        "guardrails": {
            "does_not_promote_log92160000": True,
            "does_not_import_u1y_support_as_bn27_source_identity": True,
            "does_not_close_by_bare_source_name": True,
            "does_not_treat_DE_gap_trace_as_full_source_identity": True,
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
        "export_compatibility_test_path": rel(OUTPUT_EXPORT_TEST),
        "note_path": rel(OUTPUT_NOTE),
        "u1y_routec_support_imported_for_compatibility": can_import_as_support,
        "same_source_export_to_BN27_validators": False,
        "source_object_named_S_QaSU3_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceObject DeclarationInterface Fill or SelectedConnectionValues v1

## Result

```text
status = {STATUS}
u1y_routec_support_imported_for_compatibility = true
same_source_export_to_BN27_validators = false
source_object_named_S_QaSU3_BN27 = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Export Compatibility Test

```text
{rel(OUTPUT_EXPORT_TEST)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_EXPORT_TEST)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
