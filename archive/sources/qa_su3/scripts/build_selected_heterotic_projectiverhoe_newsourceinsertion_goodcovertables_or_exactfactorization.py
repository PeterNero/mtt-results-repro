"""Build the new-source insertion interface for smooth rho_E closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "open_gate": DATA / "selected_heterotic_projectiverhoe_minimal_smooth_closure_open_gate.json",
    "direct_nogo": DATA / "selected_heterotic_projectiverhoe_minimalsmoothclosure_sourcerequest_or_directnogo.candidate.json",
    "value_packet": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_newsourceinsertion_goodcovertables_or_exactfactorization.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_newsourceinsertion_goodcovertables_or_exactfactorization_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_projectiverhoe_newsourceinsertion.template.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_NewSourceInsertion_GoodCoverTables_or_ExactFactorization_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_NEWSOURCE_INSERTION_INTERFACE_BUILT_VALUES_REQUIRED"
NEXT = "Selected_Heterotic_ProjectiveRhoE_NewSourceInsertion_FillAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    open_gate = load(INPUTS["open_gate"])
    direct_nogo = load(INPUTS["direct_nogo"])
    value_packet = load(INPUTS["value_packet"])

    template = {
        "schema": "SelectedHeteroticProjectiveRhoENewSourceInsertion.Template.v1",
        "status": "VALUES_REQUIRED",
        "source_certificate": {
            "same_branch_Qa_SU3_heterotic_projective_source": None,
            "selected_by_MTT_before_target_comparison": None,
            "no_observed_coupling_or_scale_input": True,
            "source_path_or_proof_reference": None,
        },
        "lane_A_good_cover_transition_tables": {
            "selected_cover_or_finite_quotient_cover": None,
            "Deligne_Cech_or_B_field_representative": None,
            "period_unit_map_to_primitive_c": None,
            "projective_rhoE_transition_matrices": None,
            "Z3_central_character_matches_tau": None,
            "cocycle_law_checked": None,
            "metric_unitarity_compatibility": None,
            "mapped_Freed_Witten_Bianchi_projector_retention": None,
            "bundle_operator_action_A_F_A_D_E_or_E_Qa": None,
        },
        "lane_B_exact_complement_factorization": {
            "smooth_operator_domain": None,
            "projection_to_eleven_label_quotient": None,
            "det_heat_zeta_torsion_factorization": None,
            "smooth_complement_cancels_universal_or_GR_only": None,
            "BRST_FP_gauge_quotient_counted_once": None,
            "finite_part_equals_log2008_internal_units": None,
        },
        "promotion_outputs": {
            "smooth_transition_tables_emitted": False,
            "exact_smooth_complement_quotient_closed": False,
            "E_Qa_computed": False,
            "smooth_finitepart_computed": False,
            "finite_part_value": None,
        },
        "forbidden_shortcuts": open_gate["forbidden_shortcuts"],
    }

    acceptance_predicates = {
        "lane_A_closes_if": [
            "source_certificate.same_branch_Qa_SU3_heterotic_projective_source is true",
            "source_certificate.selected_by_MTT_before_target_comparison is true",
            "selected_cover_or_finite_quotient_cover is non-null",
            "Deligne/Cech/B-field representative is non-null",
            "projective rho_E transition matrices are non-null",
            "Z3 central character matches existing tau table",
            "cocycle law and metric/unitarity checks pass",
            "mapped Freed-Witten/Bianchi/projector-retention checks pass",
            "bundle/operator action emits A/F_A/D_E or E_Qa",
        ],
        "lane_B_closes_if": [
            "source_certificate.same_branch_Qa_SU3_heterotic_projective_source is true",
            "smooth operator domain and projection to eleven-label quotient are non-null",
            "det/heat/zeta/torsion factorization is proved",
            "smooth complement is proven universal, cancelling, GR-only, or outside Qa/SU3 response",
            "BRST/FP/gauge quotient determinant is counted exactly once",
            "finite part equals log(2008) in internal units after quotient",
        ],
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoENewSourceInsertionGoodCoverTablesOrExactFactorization",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "template_path": rel(OUTPUT_TEMPLATE),
        "open_gate_status": open_gate["status"],
        "closed_prerequisites": open_gate["closed_without_new_source"],
        "acceptance_predicates": acceptance_predicates,
        "decision": {
            "interface_built": True,
            "values_filled": False,
            "goodcover_transition_tables_inserted": False,
            "exact_complement_factorization_inserted": False,
            "smooth_finitepart_computed": False,
            "E_Qa_computed": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
            "closure_claimed": False,
        },
        "guardrails": {
            "does_not_fill_values_by_template": True,
            "does_not_relax_no_go": True,
            "does_not_promote_existing_finite_packet": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "NewSourceInsertionInterfaceForSmoothRhoEClosure",
            "proved": True,
            "statement": (
                "The current direct no-go is converted into a strict insertion interface. "
                "A future source can close smooth rho_E only by filling either the "
                "good-cover transition-table lane or the exact complement-factorization "
                "lane, with same-branch source selection and no observed data. The "
                "existing finite packet remains a prerequisite, not a substitute."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "interface_built": True,
        "values_filled": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE NewSourceInsertion GoodCoverTables or ExactFactorization v1

## Result

```text
status = {STATUS}
interface_built = true
values_filled = false
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## Purpose

This turns the current-corpus no-go into a strict insertion interface. A future
source must fill one of two lanes:

- selected good-cover/projective `rho_E` transition tables,
- exact complement heat/zeta/torsion factorization.

The insertion template is:

```text
{rel(OUTPUT_TEMPLATE)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_TEMPLATE)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
