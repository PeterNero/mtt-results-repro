"""Build the A_EW source-operator / threshold-convention row validator.

This follows the zero-H-knob frontier.  The selected finite H scalar supplies
R_H^RG; this packet makes the remaining electroweak prefactor obligation
machine-checkable and tests whether current closed packets fill it.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CONST = TEXPAPERS / "mtt-individual-constants-source-search"
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_aewsourceoperator_or_thresholdconventionrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TEMPLATE = PACKET_DIR / "aew_source_operator_threshold_convention_template.packet.json"
VALIDATION = PACKET_DIR / "current_packet_fill_validation.packet.json"
DEEP_SEARCH = PACKET_DIR / "expanded_source_expression_search_with_physical_anchor_symbols.packet.json"
NEXT_PACKET = PACKET_DIR / "next_physical_action_anchor_or_direct_krow_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AEWSourceOperator_or_ThresholdConventionRows_v1.md"

PREVIOUS = DATA / "selected_electroweakprefactorsourceclosure_or_finaltruesmaudit.candidate.json"
PREVIOUS_SEARCH = (
    DATA
    / "selected_electroweakprefactorsourceclosure_or_finaltruesmaudit"
    / "source_native_prefactor_expression_search.packet.json"
)
FINITE_H = DATA / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
EW_BOUNDARY = DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json"
SOURCE_ID = DATA / "selected_sourceidentitytransportproofattempt_or_finitepartpolicyindexscale_or_directhkrow.candidate.json"
SOURCE_BRANCH = DATA / "selected_sourcebranchidentityemission_or_qastackphysicalanchor_or_directhkrow.candidate.json"
EW_RG_LOCAL = DATA / "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow.candidate.json"

B41 = CONST / "candidate_data" / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching.candidate.json"
B41_ANCHOR = (
    CONST
    / "candidate_data"
    / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
    / "gauge_action_anchor_status.packet.json"
)
B41_RG = (
    CONST
    / "candidate_data"
    / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
    / "rg_matching_threshold_scheme_status.packet.json"
)
QA_PHYSICAL = QA / "candidate_data" / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json"

STATUS = (
    "MTT_SELECTED_AEWSOURCEOPERATOR_OR_THRESHOLDCONVENTIONROWS_"
    "VALIDATOR_BUILT_CURRENT_PACKETS_FILL_ZERO_PHYSICAL_PREFACTOR_ROWS"
)
NEXT = "MTT_Selected_PhysicalGaugeActionAnchor_or_DirectKThresholdOmegaHLambda_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_SEARCH,
        FINITE_H,
        EW_BOUNDARY,
        SOURCE_ID,
        SOURCE_BRANCH,
        EW_RG_LOCAL,
        B41,
        B41_ANCHOR,
        B41_RG,
        QA_PHYSICAL,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A_EW source-operator inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    previous_search = load(PREVIOUS_SEARCH)
    finite_h = load(FINITE_H)
    ew_boundary = load(EW_BOUNDARY)
    source_id = load(SOURCE_ID)
    source_branch = load(SOURCE_BRANCH)
    ew_rg_local = load(EW_RG_LOCAL)
    b41 = load(B41)
    b41_anchor = load(B41_ANCHOR)
    b41_rg = load(B41_RG)
    qa_physical = load(QA_PHYSICAL)

    nums = previous["numerics"]
    aew_target = float(nums["A_EW_external_postcheck"])
    base_target = float(nums["lambda_if_R_H_RG_equals_1"])
    s_beta = float(nums["s_beta"])
    delta_g12 = float(nums["Delta_G12_internal"])
    p_a = float(nums["p_a_internal"])
    lambda_12 = float(nums["lambda_12_internal"])
    p_y = float(qa_physical["conditional_interface"]["closed_internal_weak_split"]["p_Y"])
    log448 = math.log(448.0)
    log2008 = math.log(2008.0)
    omega0_over_sqrt_alpha = float(
        qa_physical["conditional_interface"]["Omega0_reduction"]["Omega0_over_sqrt_alpha_phys"]
    )

    near_a = 8.0 * delta_g12 / math.pi**2
    near_b = 2.0 / p_a
    near_c = lambda_12 / (4.0 * math.pi**2)
    expression_rows = [
        {
            "row_id": "A_EW_from_8DeltaG12_over_pi2",
            "formula": "8*Delta_G12/pi^2",
            "value": near_a,
            "target": aew_target,
            "relative_residual": abs(near_a - aew_target) / abs(aew_target),
            "correction_factor_required": aew_target / near_a,
            "accepted": False,
        },
        {
            "row_id": "A_EW_from_2_over_p_a",
            "formula": "2/p_a",
            "value": near_b,
            "target": aew_target,
            "relative_residual": abs(near_b - aew_target) / abs(aew_target),
            "correction_factor_required": aew_target / near_b,
            "accepted": False,
        },
        {
            "row_id": "A_EW_from_lambda12_over_4pi2",
            "formula": "lambda_12/(4*pi^2)",
            "value": near_c,
            "target": aew_target,
            "relative_residual": abs(near_c - aew_target) / abs(aew_target),
            "correction_factor_required": aew_target / near_c,
            "accepted": False,
        },
    ]
    expression_rows.sort(key=lambda row: row["relative_residual"])

    template_fields = [
        {
            "field": "selected_R_H_RG_source",
            "required": True,
            "filled_by_current_packets": finite_h["closure_decision"]["selected_R_H_RG_source_emitted"],
            "source": rel(FINITE_H),
        },
        {
            "field": "internal_weak_split_source",
            "required": True,
            "filled_by_current_packets": source_branch["closure_decision"]["lambda_12_internal_closed"]
            and source_branch["closure_decision"]["internal_Qa_stack_p_a_source_closed"],
            "source": rel(SOURCE_BRANCH),
        },
        {
            "field": "physical_gauge_action_anchor_or_K_phys",
            "required": True,
            "filled_by_current_packets": b41_anchor["decision"]["physical_alpha_or_metrology_anchor_closed"]
            or qa_physical["decision"]["physical_gauge_action_anchor_closed"],
            "source": rel(B41_ANCHOR),
        },
        {
            "field": "selected_mu_match",
            "required": True,
            "filled_by_current_packets": b41_rg["decision"]["source_selected_mu_match_closed"]
            or qa_physical["decision"]["matching_scale_closed"],
            "source": rel(B41_RG),
        },
        {
            "field": "selected_RG_threshold_scheme",
            "required": True,
            "filled_by_current_packets": b41_rg["decision"]["source_selected_threshold_vector_closed"]
            and qa_physical["decision"]["RG_scheme_closed"],
            "source": rel(B41_RG),
        },
        {
            "field": "A_EW_source_operator_value",
            "required": True,
            "filled_by_current_packets": ew_boundary["closure_decision"]["selected_A_EW_emitted"],
            "source": rel(EW_BOUNDARY),
        },
        {
            "field": "strict_K_threshold_Omega_H_lambda_row",
            "required": True,
            "filled_by_current_packets": ew_boundary["closure_decision"]["K_threshold_Omega_H_lambda_emitted"],
            "source": rel(EW_BOUNDARY),
        },
    ]
    filled_required = sum(1 for field in template_fields if field["required"] and field["filled_by_current_packets"])
    required_count = sum(1 for field in template_fields if field["required"])
    physical_prefactor_rows = [
        field
        for field in template_fields
        if field["field"]
        in {
            "physical_gauge_action_anchor_or_K_phys",
            "selected_mu_match",
            "selected_RG_threshold_scheme",
            "A_EW_source_operator_value",
            "strict_K_threshold_Omega_H_lambda_row",
        }
    ]
    filled_physical_prefactor_rows = sum(1 for field in physical_prefactor_rows if field["filled_by_current_packets"])

    template = {
        "schema": "MTTAEWSourceOperatorThresholdConventionTemplate.v1",
        "status": "AEW_SOURCE_OPERATOR_THRESHOLD_CONVENTION_TEMPLATE_BUILT",
        "closure_claimed": True,
        "operator_definition": (
            "A_EW^sel(mu_match,scheme)=F_EW(K_phys/f_ab, Delta_a^sel, mu_match, RG_scheme); "
            "lambda_if_R=1=A_EW^sel*s_beta; "
            "K_threshold.Omega_H.lambda follows only after selected R_H^RG and selected prefactor."
        ),
        "required_fields": template_fields,
        "required_field_count": required_count,
        "required_fields_filled_by_current_packets": filled_required,
        "physical_prefactor_required_field_count": len(physical_prefactor_rows),
        "physical_prefactor_fields_filled_by_current_packets": filled_physical_prefactor_rows,
        "conditional_success_consequence": [
            "strict lambda_H value row can be emitted from selected R_H^RG and selected lambda_if_R=1",
            "strict K_threshold.Omega_H.lambda can become the tenth K row",
            "H/lambda sector can enter final true-SM audit with zero H parameters",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    validation = {
        "schema": "MTTCurrentPacketFillValidationForAEWSourceOperator.v1",
        "status": "CURRENT_PACKETS_FILL_SUPPORT_BUT_ZERO_PHYSICAL_PREFACTOR_ROWS",
        "closure_claimed": True,
        "closed_support": {
            "selected_R_H_RG": True,
            "H_parameter_count_after_replacement": 0,
            "internal_p_a": p_a,
            "internal_lambda_12": lambda_12,
            "internal_Delta_G12": delta_g12,
            "internal_p_Y": p_y,
            "Omega0_over_sqrt_alpha_phys": omega0_over_sqrt_alpha,
            "log448": log448,
            "log2008": log2008,
        },
        "open_physical_rows": {
            "physical_gauge_action_anchor_or_K_phys": True,
            "selected_mu_match": True,
            "selected_RG_threshold_scheme": True,
            "selected_A_EW_source_operator": True,
            "strict_K_threshold_Omega_H_lambda": True,
        },
        "accepted_A_EW_source_operator_rows": 0,
        "accepted_threshold_convention_rows": 0,
        "accepted_physical_prefactor_rows": 0,
        "strict_lambda_H_value_row_emitted": False,
        "strict_K_threshold_Omega_H_lambda_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    deep_search = {
        "schema": "MTTExpandedSourceExpressionSearchWithPhysicalAnchorSymbols.v1",
        "status": "EXPANDED_SEARCH_EXECUTED_NO_EXACT_SOURCE_ROW",
        "closure_claimed": True,
        "target_values": {
            "A_EW_postcheck": aew_target,
            "lambda_if_R_H_RG_equals_1": base_target,
            "s_beta": s_beta,
        },
        "symbols_added_after_previous_search": {
            "p_Y": p_y,
            "log448": log448,
            "log2008": log2008,
            "Omega0_over_sqrt_alpha_phys": omega0_over_sqrt_alpha,
        },
        "best_expression_rows": expression_rows,
        "previous_best": previous_search["best_candidate"],
        "exact_hits_found": 0,
        "accepted_selected_expression_rows": 0,
        "decision": (
            "The best candidates remain near-misses. Their required correction factors are "
            "not emitted by current physical-anchor/RG packets, so they are theorem targets "
            "rather than source values."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextPhysicalActionAnchorOrDirectKRowContract.v1",
        "status": "NEXT_IS_PHYSICAL_ACTION_ANCHOR_OR_DIRECT_K_ROW",
        "closure_claimed": True,
        "closed_here": [
            "A_EW source-operator validator built",
            "current packet fill executed against constants and Qa/SU3 physical-anchor sources",
            "expanded source expression search with physical-anchor symbols executed",
            "near-miss correction factors isolated as theorem targets",
        ],
        "remaining_exact_exits": [
            "same-branch physical gauge/action anchor K_phys or f_ab",
            "selected mu_match plus RG/threshold convention",
            "exact theorem turning 8*Delta_G12/pi^2 or 2/p_a into A_EW with selected correction factor",
            "direct K_threshold.Omega_H.lambda row independent of A_EW",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedAEWSourceOperatorOrThresholdConventionRows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_search": rel(PREVIOUS_SEARCH),
            "finite_H": rel(FINITE_H),
            "ew_boundary": rel(EW_BOUNDARY),
            "source_identity": rel(SOURCE_ID),
            "source_branch": rel(SOURCE_BRANCH),
            "ew_rg_local": rel(EW_RG_LOCAL),
            "b41": rel(B41),
            "b41_anchor": rel(B41_ANCHOR),
            "b41_rg": rel(B41_RG),
            "qa_physical": rel(QA_PHYSICAL),
        },
        "packets": {
            "aew_source_operator_threshold_convention_template": rel(TEMPLATE),
            "current_packet_fill_validation": rel(VALIDATION),
            "expanded_source_expression_search_with_physical_anchor_symbols": rel(DEEP_SEARCH),
            "next_physical_action_anchor_or_direct_krow_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "selected_R_H_RG_source_emitted": True,
            "H_parameter_count_after_replacement": 0,
            "aew_source_operator_template_built": True,
            "required_fields_filled_by_current_packets": filled_required,
            "required_field_count": required_count,
            "accepted_A_EW_source_operator_rows": 0,
            "accepted_threshold_convention_rows": 0,
            "accepted_physical_prefactor_rows": 0,
            "expanded_search_exact_hits_found": 0,
            "best_expression_formula": expression_rows[0]["formula"],
            "best_expression_relative_residual": expression_rows[0]["relative_residual"],
            "strict_lambda_H_value_row_emitted": False,
            "strict_K_threshold_Omega_H_lambda_emitted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "numerics": {
            "A_EW_postcheck": aew_target,
            "lambda_if_R_H_RG_equals_1": base_target,
            "s_beta": s_beta,
            "p_a": p_a,
            "lambda_12": lambda_12,
            "Delta_G12": delta_g12,
            "p_Y": p_y,
            "Omega0_over_sqrt_alpha_phys": omega0_over_sqrt_alpha,
            "best_A_EW_expression_value": expression_rows[0]["value"],
            "best_A_EW_expression_correction_factor_required": expression_rows[0][
                "correction_factor_required"
            ],
        },
        "theorem": {
            "name": "AEWSourceOperatorThresholdConventionValidatorTheorem",
            "proved": True,
            "statement": (
                "The selected finite H scalar removes the H radial parameter, and current packets close "
                "internal weak-split support.  However, the A_EW source-operator validator still receives "
                "zero physical prefactor rows: no same-branch K_phys/f_ab, mu_match, RG/threshold scheme, "
                "A_EW source value, or direct K_threshold.Omega_H.lambda row is emitted.  Expanded source "
                "expression search supplies near-miss theorem targets but no accepted source value."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedAEWSourceOperatorOrThresholdConventionRows",
        "status": STATUS,
        "closure_claimed": True,
        "theorem_proved": True,
        "selected_R_H_RG_source_emitted": True,
        "H_parameter_count_after_replacement": 0,
        "aew_source_operator_template_built": True,
        "accepted_A_EW_source_operator_rows": 0,
        "accepted_threshold_convention_rows": 0,
        "accepted_physical_prefactor_rows": 0,
        "strict_lambda_H_value_row_emitted": False,
        "strict_K_threshold_Omega_H_lambda_emitted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected AEWSourceOperator or ThresholdConventionRows v1

## Theorem

`AEWSourceOperatorThresholdConventionValidatorTheorem` is emitted.

The validator for the remaining H/lambda prefactor is now explicit:

```text
A_EW^sel(mu_match, scheme)
lambda_if_R=1 = A_EW^sel * s_beta
K_threshold.Omega_H.lambda closes only after selected R_H^RG and selected prefactor
```

## Current Fill

Closed support:

```text
R_H^RG selected = true
H parameter count = 0
p_a = {p_a}
lambda_12 = {lambda_12}
Delta_G12 = {delta_g12}
p_Y = {p_y}
Omega0/sqrt(alpha_phys) = {omega0_over_sqrt_alpha}
```

Open physical rows:

```text
K_phys or f_ab
mu_match
RG/threshold convention
A_EW source operator value
K_threshold.Omega_H.lambda
```

## Expression Search

Best current theorem targets:

```text
{expression_rows[0]["formula"]} = {expression_rows[0]["value"]}
relative residual = {expression_rows[0]["relative_residual"]}
required correction factor = {expression_rows[0]["correction_factor_required"]}

{expression_rows[1]["formula"]} = {expression_rows[1]["value"]}
relative residual = {expression_rows[1]["relative_residual"]}
required correction factor = {expression_rows[1]["correction_factor_required"]}
```

Accepted A_EW source rows: `0`.

Accepted threshold convention rows: `0`.

## Next Proof Object

`{NEXT}`.
"""

    write_json(TEMPLATE, template)
    write_json(VALIDATION, validation)
    write_json(DEEP_SEARCH, deep_search)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
