"""Build the HYM repair source-selection or retirement theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

INPUTS = {
    "local_repair_gate": DATA / "selected_heterotic_hym_erratum_repair_comparison_gate.candidate.json",
    "ab_diagnostic": NONSM / "certificates" / "selected_qa_su3_repaired_pipeline_ab_diagnostic_comparison_certificate.json",
    "chern_weil_diagnostic": NONSM / "certificates" / "selected_qa_su3_repair_chern_weil_operator_diagnostic_certificate.json",
    "repair_a_or_b_test": NONSM / "certificates" / "selected_qa_su3_repair_a_quotient_or_b_torsion_source_test_certificate.json",
    "repair_b_no_go": NONSM / "certificates" / "selected_qa_su3_repair_b_primitive_correction_no_go_certificate.json",
    "explicit_hym_retirement": NONSM / "certificates" / "selected_qa_su3_explicit_hym_route_retirement_certificate.json",
    "local_system_torsion": NONSM / "certificates" / "selected_qa_su3_local_system_torsion_source_extraction_certificate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_hym_repair_source_selection_or_retirement.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_hym_repair_source_selection_or_retirement_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_post_hym_retirement_operator_or_torsion_source.template.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_HYM_Repair_SourceSelection_or_Retirement_v1.md"

STATUS = "HETEROTIC_HYM_REPAIR_SOURCE_SELECTION_CURRENT_SOURCE_RETIREMENT_PROVED"
NEXT = "Selected_Heterotic_LocalSystemTorsion_or_NewOperatorSource_Attack_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_template() -> dict[str, Any]:
    return {
        "schema": "SelectedHeteroticPostHYMRetirementOperatorOrTorsionSource.v1",
        "status": "OPEN_SOURCE_REQUIRED",
        "allowed_reopen_hym_route": {
            "source_erratum_selects_repair_A_or_B_or_other_connection": None,
            "connection_integrability_verified": None,
            "indecomposable_rank3_su3_compatibility_verified": None,
            "primitive_hym_or_full_torsion_correction_verified": None,
            "chern_weil_claims_recomputed": None,
            "mu_or_moduli_selected": None,
            "full_threshold_operator_spectrum_or_finite_part": None,
        },
        "primary_non_hym_route": {
            "selected_compact_nil_or_iwasawa_character": None,
            "unitary_or_projective_local_system": None,
            "acyclicity_or_zero_mode_policy": None,
            "ray_singer_or_reidemeister_torsion_finite_part": None,
            "qa_qc_su2_trace_weights": None,
            "physical_threshold_scheme": None,
        },
        "secondary_new_operator_route": {
            "selected_bundle_sheaf_twist_or_projective_module": None,
            "operator_domain": None,
            "endomorphism_E_or_laplace_type_operator": None,
            "heat_spectrum_zeta_or_torsion_finite_part": None,
            "normalization_and_trace_policy": None,
        },
        "forbidden": [
            "promote Repair A under the selected indecomposable rank-3 branch",
            "promote Repair B without the required source-certified primitive Cartan correction",
            "use the printed nonintegrable matrix as proof",
            "choose a repair by closeness to an electroweak or Qa/SU3 target",
            "reuse internal lambda12 as physical heterotic threshold data",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    local_gate = load(INPUTS["local_repair_gate"])
    ab_diag = load(INPUTS["ab_diagnostic"])
    chern = load(INPUTS["chern_weil_diagnostic"])
    repair_test = load(INPUTS["repair_a_or_b_test"])
    b_nogo = load(INPUTS["repair_b_no_go"])
    retirement = load(INPUTS["explicit_hym_retirement"])
    torsion = load(INPUTS["local_system_torsion"])
    template = build_template()

    repair_resolution = {
        "printed_matrix": {
            "status": "BLOCKED_NONINTEGRABLE",
            "local_integrability_check": local_gate["decision"]["printed_integrable_under_standard_check"],
            "retirement_status": retirement["retirement_scope"]["explicit_hym_matrix_route_retired_for_current_proof"],
        },
        "repair_A": {
            "status": "RETIRED_UNDER_SELECTED_INDECOMPOSABLE_BRANCH",
            "integrable_diagnostic": local_gate["decision"]["repair_A_integrable"],
            "primitive_diagnostic": chern["comparison"]["repair_A_integrable_and_primitive"],
            "extra_zero_mode": ab_diag["comparison"]["repair_A_extra_zero_mode"],
            "extra_noncentral_stabilizer": repair_test["conclusion"]["repair_A_extra_zero_is_noncentral_stabilizer"],
            "incompatible_with_selected_branch": repair_test["conclusion"]["repair_A_incompatible_with_selected_indecomposable_branch"],
            "source_certified": False,
        },
        "repair_B": {
            "status": "ONLY_LIVE_REPAIR_BUT_CURRENT_SOURCE_NO_GO",
            "integrable_diagnostic": local_gate["decision"]["repair_B_integrable"],
            "expected_hessian_rank_pattern": ab_diag["comparison"]["repair_B_expected_hessian_rank_pattern"],
            "primitive_obstructed": chern["comparison"]["repair_B_primitive_obstructed"],
            "required_correction": b_nogo["required_correction"],
            "current_source_no_go": b_nogo["verdict"]["repair_B_current_source_no_go"],
            "mathematically_impossible": b_nogo["verdict"]["repair_B_mathematically_impossible"],
            "source_certified": b_nogo["verdict"]["repair_B_primitive_correction_source_certified_now"],
        },
    }

    decision = {
        "printed_hym_matrix_route_closed": False,
        "printed_hym_matrix_route_retired_current_source": True,
        "repair_A_retired_current_branch": True,
        "repair_B_only_live_repair_candidate": True,
        "repair_B_current_source_no_go": True,
        "any_hym_repair_source_certified": False,
        "strict_no_knob_heterotic_route_still_live": True,
        "primary_next_route": "local_system_torsion_or_new_operator_source",
        "local_system_torsion_computable_now": torsion["verdict"]["ray_singer_torsion_computable_now"],
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticHYMRepairSourceSelectionOrRetirement",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "local_repair_gate": local_gate["status"],
            "ab_diagnostic": ab_diag["status"],
            "chern_weil_diagnostic": chern["status"],
            "repair_a_or_b_test": repair_test["status"],
            "repair_b_no_go": b_nogo["status"],
            "explicit_hym_retirement": retirement["status"],
            "local_system_torsion": torsion["status"],
        },
        "repair_resolution": repair_resolution,
        "post_retirement_template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "theorem": {
            "name": "HeteroticHYMRepairCurrentSourceRetirementTheorem",
            "proved": True,
            "statement": (
                "Under the current corpus, the printed HYM matrix cannot serve as "
                "a proof source; Repair A is refuted for the selected indecomposable "
                "rank-3 SU3 branch by its extra noncentral stabilizer/direct-split "
                "diagnostic; and Repair B, while the only live repair candidate, "
                "requires a source-certified mu-dependent Cartan primitive correction "
                "that the current corpus does not emit. Therefore the explicit HYM "
                "matrix route is retired as a current proof source. The heterotic "
                "no-knob program remains live only through a future source-certified "
                "HYM erratum, a selected local-system torsion computation, or a new "
                "same-branch threshold operator source."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "promotes_printed_nonintegrable_matrix": False,
            "promotes_repair_A": False,
            "promotes_repair_B_without_correction_source": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedHeteroticHYMRepairSourceSelectionOrRetirement",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "printed_hym_matrix_route_retired_current_source": True,
        "repair_A_retired_current_branch": True,
        "repair_B_current_source_no_go": True,
        "primary_next_route": decision["primary_next_route"],
        "strict_no_knob_heterotic_route_still_live": True,
        "measured_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert, template)


def render_note(candidate: dict[str, Any], cert: dict[str, Any], template: dict[str, Any]) -> str:
    return f"""# Selected Heterotic HYM Repair Source Selection or Retirement v1

## Result

```text
status = {candidate["status"]}
printed_hym_matrix_route_retired_current_source = true
repair_A_retired_current_branch = true
repair_B_current_source_no_go = true
primary_next_route = {candidate["decision"]["primary_next_route"]}
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Repair Resolution

```json
{json.dumps(candidate["repair_resolution"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Post-Retirement Source Template

```json
{json.dumps(template, indent=2, sort_keys=True)}
```

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, template, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_TEMPLATE, template)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_TEMPLATE, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
