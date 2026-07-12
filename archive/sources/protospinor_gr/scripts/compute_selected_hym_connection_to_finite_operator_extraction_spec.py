from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

PREV_IMPORT = ROOT / "certificates" / "routec_hym_operator_values_gate_import_certificate.json"
OUT_CERT = ROOT / "certificates" / "selected_hym_connection_to_finite_operator_extraction_spec_certificate.json"
OUT_TEMPLATE = ROOT / "candidate_data" / "selected_hym_connection_to_finite_operator_extraction.template.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_HYM_Connection_to_Finite_Operator_Extraction_Spec_v1.md"

STATUS = "SELECTED_HYM_CONNECTION_TO_FINITE_OPERATOR_EXTRACTION_SPEC_BUILT_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_Run_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)

    required_fields = {
        "selected_connection_or_transition_representative": {
            "required": True,
            "source": "selected AH/Cech V_alpha bundle plus equal-radius Gauduchon HYM connection",
            "filled": False,
        },
        "finite_quotient_basis_truncation": {
            "required": True,
            "source": "selected good-cover/AH/Galerkin map with explicit error bound",
            "filled": False,
        },
        "rhoE_mesh_and_metric": {
            "required": True,
            "source": "derived from selected connection, not copied from smoke",
            "filled": False,
        },
        "sector_maps": {
            "required": True,
            "source": "same selected connection and visible sector bundle data",
            "filled": False,
        },
        "D_E_action": {
            "required": True,
            "source": "finite covariant operator induced by selected connection",
            "filled": False,
        },
        "Riesz_gap_and_projectors": {
            "required": True,
            "source": "spectrum of selected D_E^*D_E complement with error bounds",
            "filled": False,
        },
        "reduced_Green": {
            "required": True,
            "source": "inverse on selected complement using the selected Riesz projector",
            "filled": False,
        },
        "dotD_alpha1": {
            "required": True,
            "source": "same-branch derivative of selected D_E under alpha1 deformation",
            "filled": False,
        },
        "primitive_C1_overlap_contractions": {
            "required": True,
            "source": "same zero-mode and horizontal response bases",
            "filled": False,
        },
        "selected_source_flags": {
            "required": True,
            "source": "theorem-derived provenance, not lifted flags",
            "filled": False,
        },
    }

    validators = [
        {
            "name": "route_c_residuals",
            "script": str(Q79 / "scripts" / "validate_iwasawa_route_c_residuals.py"),
            "candidate_field": "route_c_residual",
            "must_pass_honestly": True,
        },
        {
            "name": "rhoE_mesh",
            "script": str(Q79 / "scripts" / "validate_iwasawa_rhoE_mesh.py"),
            "candidate_field": "rhoE_mesh",
            "must_pass_honestly": True,
        },
        {
            "name": "rhoE_metric",
            "script": str(Q79 / "scripts" / "validate_iwasawa_rhoE_metric.py"),
            "candidate_field": "rhoE_metric",
            "must_pass_honestly": True,
        },
        {
            "name": "sector_maps",
            "script": str(Q79 / "scripts" / "validate_iwasawa_sector_maps.py"),
            "candidate_field": "sector_maps",
            "must_pass_honestly": True,
        },
        {
            "name": "D_E_action",
            "script": str(Q79 / "scripts" / "validate_iwasawa_de_action.py"),
            "candidate_field": "de_action",
            "must_pass_honestly": True,
        },
        {
            "name": "Riesz_gap",
            "script": str(Q79 / "scripts" / "validate_iwasawa_riesz_gap.py"),
            "candidate_field": "riesz_gap",
            "must_pass_honestly": True,
        },
        {
            "name": "reduced_Green",
            "script": str(Q79 / "scripts" / "validate_iwasawa_reduced_green.py"),
            "candidate_field": "reduced_green",
            "must_pass_honestly": True,
        },
        {
            "name": "dotD_alpha1",
            "script": str(Q79 / "scripts" / "validate_iwasawa_dotd_response.py"),
            "candidate_field": "dotd_response",
            "must_pass_honestly": True,
        },
    ]

    acceptance_tests = {
        "all_required_fields_filled": False,
        "all_validators_pass_honestly": False,
        "no_lifted_flags": True,
        "no_observed_or_benchmark_inputs": True,
        "same_source_provenance_required": True,
        "can_emit_A_selected_after_pass": False,
        "can_emit_b_selected_after_pass": False,
    }

    template = {
        "candidate": "MTTSelectedHYMConnectionToFiniteOperatorExtraction",
        "status": "TEMPLATE_VALUES_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "selected_branch": "q79/F,m=1 selected equal-radius V_alpha branch",
        "required_fields": required_fields,
        "validators": validators,
        "acceptance_tests": acceptance_tests,
        "forbidden_shortcuts": [
            "copying smoke data while changing selected flags",
            "using lifted selected flags as proof",
            "using observed masses, mixings, CKM/PMNS, CP, thresholds, or benchmark matrices",
            "using abstract HYM existence as finite operator values without extraction",
        ],
        "next_after_success": "promote finite payload into A_selected/b_selected and replay C1 overlap solve",
    }

    checks = {
        "previous_import_proved": prev["theorem"]["proved"] is True,
        "previous_next_matches": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_v1",
        "ten_required_fields": len(required_fields) == 10,
        "eight_existing_validators_listed": len(validators) == 8,
        "forbids_lifted_flags": "using lifted selected flags as proof" in template["forbidden_shortcuts"],
        "forbids_observed_data": any("observed masses" in item for item in template["forbidden_shortcuts"]),
        "values_open": template["closure_claimed"] is False
        and acceptance_tests["all_required_fields_filled"] is False,
    }

    theorem = {
        "name": "SelectedHYMConnectionToFiniteOperatorExtractionSpec",
        "proved": all(checks.values()),
        "statement": (
            "The missing extraction theorem is converted into an executable "
            "contract. It enumerates the selected connection, finite quotient, "
            "rho_E/metric, sector maps, D_E, Riesz/Green, dotD, primitive C1 "
            "contractions, and source-provenance fields required before "
            "A_selected or b_selected can be emitted. This is a spec, not a "
            "value computation."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_hym_connection_to_finite_operator_extraction_spec",
        "status": STATUS,
        "input_certificate": str(PREV_IMPORT),
        "theorem": theorem,
        "checks": checks,
        "required_fields": required_fields,
        "validators": validators,
        "acceptance_tests": acceptance_tests,
        "template_written": str(OUT_TEMPLATE),
        "note_written": str(OUT_NOTE),
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = """# Selected HYM Connection to Finite Operator Extraction Spec v1

## Result

The missing extraction theorem is now an executable contract.

It must derive, from the selected equal-radius HYM connection on the selected
`V_alpha` branch:

```text
selected connection / transition representative
finite quotient, basis, truncation, and error bounds
rho_E mesh and metric tables
sector maps
D_E action matrices
Riesz projectors and complement gaps
reduced Green operators
dotD_alpha1 same-branch derivative
primitive C1 overlap contractions
theorem-derived selected-source flags
```

The existing Route-C validators are the acceptance tests. A successful packet
must pass them honestly, without lifted selected flags and without observed
flavor, mass, mixing, CP, threshold, or benchmark inputs.

This spec does not emit values yet. It makes the next run concrete.

## Status

```text
SELECTED_HYM_CONNECTION_TO_FINITE_OPERATOR_EXTRACTION_SPEC_BUILT_VALUES_OPEN
```

The next required artifact is:

```text
MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_Run_v1
```
"""

    OUT_TEMPLATE.write_text(json.dumps(template, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_TEMPLATE}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
