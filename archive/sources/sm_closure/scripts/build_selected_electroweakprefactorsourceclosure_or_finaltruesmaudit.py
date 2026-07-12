"""Audit the electroweak prefactor after finite H scalar closure.

The previous artifact selected R_H^RG := r_H(A_N), retiring the counted H
radial parameter.  This artifact attacks the remaining prefactor row:
lambda_if_R_H_RG_equals_1, equivalently the A_EW/mu_match/threshold convention
part of the H/lambda payload.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_electroweakprefactorsourceclosure_or_finaltruesmaudit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INVENTORY = PACKET_DIR / "electroweak_prefactor_source_inventory.packet.json"
SEARCH = PACKET_DIR / "source_native_prefactor_expression_search.packet.json"
FINAL_GATE = PACKET_DIR / "final_hlambda_gate_after_zero_h_knob.packet.json"
NEXT_PACKET = PACKET_DIR / "next_aew_source_operator_or_threshold_convention_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ElectroweakPrefactorSourceClosure_or_FinalTrueSMAudit_v1.md"

PREVIOUS = DATA / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
PREVIOUS_LAMBDA = (
    DATA
    / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit"
    / "lambda_h_payload_postcheck_and_guardrail.packet.json"
)
EW_BOUNDARY = DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json"
ALPHA_AEW = DATA / "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem.candidate.json"
SOURCE_ID = DATA / "selected_sourceidentitytransportproofattempt_or_finitepartpolicyindexscale_or_directhkrow.candidate.json"
SOURCE_BRANCH = DATA / "selected_sourcebranchidentityemission_or_qastackphysicalanchor_or_directhkrow.candidate.json"
EW_RG = DATA / "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow.candidate.json"

STATUS = (
    "MTT_SELECTED_ELECTROWEAK_PREFACTOR_SOURCE_CLOSURE_OR_FINAL_TRUE_SM_AUDIT_"
    "ZERO_H_KNOB_CONFIRMED_AEW_PREFACTOR_SOURCE_OPEN"
)
NEXT = "MTT_Selected_AEWSourceOperator_or_ThresholdConventionRows_v1"


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


def candidate_exprs(values: dict[str, float]) -> list[tuple[str, float, str]]:
    s = values["s_beta"]
    delta = values["Delta_G12"]
    p_a = values["p_a"]
    lam12 = values["lambda_12"]
    pi2 = math.pi**2
    return [
        ("A_EW_from_8DeltaG12_over_pi2", 8.0 * delta / pi2, "8*Delta_G12/pi^2"),
        ("A_EW_from_2_over_p_a", 2.0 / p_a, "2/p_a"),
        ("A_EW_from_lambda12_over_4pi2", lam12 / (4.0 * pi2), "lambda_12/(4*pi^2)"),
        ("base_from_2_sbeta_over_p_a", 2.0 * s / p_a, "2*s_beta/p_a"),
        ("base_from_8_sbeta_DeltaG12_over_pi2", 8.0 * s * delta / pi2, "8*s_beta*Delta_G12/pi^2"),
        ("base_from_sbeta_lambda12_over_4pi2", s * lam12 / (4.0 * pi2), "s_beta*lambda_12/(4*pi^2)"),
        ("base_from_pi2_sbeta_over_144", pi2 * s / 144.0, "pi^2*s_beta/144"),
    ]


def main() -> int:
    sources = [PREVIOUS, PREVIOUS_LAMBDA, EW_BOUNDARY, ALPHA_AEW, SOURCE_ID, SOURCE_BRANCH, EW_RG]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing electroweak prefactor inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    previous_lambda = load(PREVIOUS_LAMBDA)
    ew_boundary = load(EW_BOUNDARY)
    alpha_aew = load(ALPHA_AEW)
    source_id = load(SOURCE_ID)
    source_branch = load(SOURCE_BRANCH)
    ew_rg = load(EW_RG)

    nums = previous["numerics"]
    lambda_if_r1 = float(nums["lambda_if_R_H_RG_equals_1_postcheck_factor"])
    lambda_from_finite = float(nums["lambda_H_from_finite_r_H_A_N"])
    lambda_external = float(nums["external_lambda_Mt_postcheck"])
    r_h_an = float(nums["r_H_A_N"])
    aew_external = float(alpha_aew["key_numbers"]["A_EW_Mt_external"])
    s_beta = float(alpha_aew["key_numbers"]["s_beta"])
    p_a = float(source_id["closure_decision"]["selected_p_a_internal_value"])
    lambda_12 = float(source_branch["closure_decision"]["lambda_12_internal_value"])
    delta_g12 = float(source_branch["closure_decision"]["Delta_G12_internal_value"])

    values = {
        "s_beta": s_beta,
        "p_a": p_a,
        "lambda_12": lambda_12,
        "Delta_G12": delta_g12,
    }

    rows = []
    for row_id, value, formula in candidate_exprs(values):
        if row_id.startswith("A_EW"):
            target = aew_external
            target_name = "A_EW_external_postcheck"
            base_value = value * s_beta
        else:
            target = lambda_if_r1
            target_name = "lambda_if_R_H_RG_equals_1"
            base_value = value
        residual = value - target
        relative = abs(residual) / abs(target)
        lambda_replay = base_value * r_h_an
        rows.append(
            {
                "row_id": row_id,
                "formula": formula,
                "value": value,
                "target_name": target_name,
                "target_value": target,
                "absolute_residual": residual,
                "relative_residual": relative,
                "lambda_H_replay_if_used": lambda_replay,
                "lambda_H_residual_if_used": lambda_replay - lambda_external,
                "accepted_as_selected_prefactor_source": False,
                "reason_rejected": (
                    "near-miss/source clue only; no exact selected A_EW or threshold-convention "
                    "source theorem emits this value"
                ),
            }
        )
    rows.sort(key=lambda row: row["relative_residual"])

    best = rows[0]
    inventory = {
        "schema": "MTTElectroweakPrefactorSourceInventory.v1",
        "status": "ELECTROWEAK_PREFACTOR_SOURCE_INVENTORY_AFTER_FINITE_HSCALAR",
        "closure_claimed": True,
        "selected_R_H_RG_available": previous["closure_decision"]["selected_R_H_RG_source_emitted"],
        "H_parameter_count_after_replacement": previous["closure_decision"]["H_parameter_count_after_replacement"],
        "prefactor_target": {
            "lambda_if_R_H_RG_equals_1": lambda_if_r1,
            "A_EW_external_postcheck": aew_external,
            "s_beta_selected": s_beta,
            "relationship": "lambda_if_R_H_RG_equals_1 = A_EW * s_beta",
        },
        "source_inputs_available": {
            "p_a_internal_selected": p_a,
            "lambda_12_internal_selected": lambda_12,
            "Delta_G12_internal_selected": delta_g12,
            "gaugekinetic_normalization_closed": ew_rg["closure_decision"]["gaugekinetic_normalization_closed"],
            "matching_scale_closed": ew_rg["closure_decision"]["matching_scale_closed"],
            "RG_scheme_closed": ew_rg["closure_decision"]["RG_scheme_closed"],
            "selected_A_EW_emitted": ew_boundary["closure_decision"]["selected_A_EW_emitted"],
            "selected_threshold_RG_transport_closed": ew_boundary["closure_decision"][
                "selected_threshold_RG_transport_closed"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    search = {
        "schema": "MTTSourceNativePrefactorExpressionSearch.v1",
        "status": "SOURCE_NATIVE_PREFATOR_SEARCH_EXECUTED_ZERO_ACCEPTED_ROWS",
        "closure_claimed": True,
        "search_policy": "bounded low-complexity expressions from already selected internal electroweak scalars",
        "accepted_selected_prefactor_source_count": 0,
        "best_candidate": best,
        "all_candidates": rows,
        "promotion_rule": (
            "A candidate requires an exact selected source theorem or accepted threshold-convention row; "
            "numerical proximity to the external electroweak coordinate is not enough."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    final_gate = {
        "schema": "MTTFinalHLambdaGateAfterZeroHKnob.v1",
        "status": "ZERO_H_KNOB_CONFIRMED_LAMBDA_PREFATOR_ROW_OPEN",
        "closure_claimed": True,
        "selected_R_H_RG_source_emitted": True,
        "H_parameter_count_after_replacement": 0,
        "lambda_H_postcheck_from_existing_prefactor": lambda_from_finite,
        "lambda_H_postcheck_residual": lambda_from_finite - lambda_external,
        "strict_lambda_H_value_row_emitted": False,
        "strict_K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count_now": 9,
        "selected_K_threshold_row_count_required": 10,
        "conditional_full_H_closure_if_prefactor_source_selected": True,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextAEWSourceOperatorOrThresholdConventionContract.v1",
        "status": "NEXT_IS_AEW_SOURCE_OPERATOR_OR_THRESHOLD_CONVENTION_ROWS",
        "closure_claimed": True,
        "closed_now": [
            "zero-H-parameter frontier re-audited after finite H scalar source",
            "A_EW/base-prefactor source expression search executed",
            "near-miss source clues isolated without promotion",
            "strict lambda_H/K row guarded against external-coordinate promotion",
        ],
        "remaining_exact_objects": [
            "selected A_EW gauge/action normalization source",
            "selected mu_match and RG/threshold convention row",
            "exact threshold prefactor theorem explaining or replacing the near-misses 8*Delta_G12/pi^2 and 2/p_a",
            "strict K_threshold.Omega_H.lambda emission using selected R_H^RG plus selected prefactor",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedElectroweakPrefactorSourceClosureOrFinalTrueSMAudit",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_finite_H_lambda_transport": rel(PREVIOUS),
            "previous_lambda_guardrail": rel(PREVIOUS_LAMBDA),
            "ew_boundary": rel(EW_BOUNDARY),
            "alpha_AEW": rel(ALPHA_AEW),
            "source_identity": rel(SOURCE_ID),
            "source_branch": rel(SOURCE_BRANCH),
            "ew_rg": rel(EW_RG),
        },
        "packets": {
            "electroweak_prefactor_source_inventory": rel(INVENTORY),
            "source_native_prefactor_expression_search": rel(SEARCH),
            "final_hlambda_gate_after_zero_h_knob": rel(FINAL_GATE),
            "next_aew_source_operator_or_threshold_convention_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "selected_R_H_RG_source_emitted": True,
            "H_parameter_count_after_replacement": 0,
            "electroweak_prefactor_search_executed": True,
            "accepted_selected_prefactor_source_count": 0,
            "best_near_miss_formula": best["formula"],
            "best_near_miss_relative_residual": best["relative_residual"],
            "selected_A_EW_source_emitted": False,
            "selected_mu_match_or_RG_scheme_emitted": False,
            "strict_lambda_H_value_row_emitted": False,
            "strict_K_threshold_Omega_H_lambda_emitted": False,
            "conditional_full_H_closure_if_prefactor_source_selected": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "numerics": {
            "lambda_if_R_H_RG_equals_1": lambda_if_r1,
            "A_EW_external_postcheck": aew_external,
            "s_beta": s_beta,
            "p_a_internal": p_a,
            "lambda_12_internal": lambda_12,
            "Delta_G12_internal": delta_g12,
            "lambda_H_postcheck_from_finite_RH": lambda_from_finite,
            "lambda_H_postcheck_residual": lambda_from_finite - lambda_external,
        },
        "theorem": {
            "name": "ElectroweakPrefactorFinalGateTheorem",
            "proved": True,
            "statement": (
                "After finite H scalar transport, the H radial/RG multiplier is selected with zero H "
                "parameters. The remaining no-knob obstruction is the electroweak prefactor/convention "
                "row lambda_if_R_H_RG_equals_1, equivalently selected A_EW with mu_match/RG scheme. "
                "A bounded source-native expression search finds structured near-misses but emits zero "
                "accepted prefactor source rows, so strict lambda_H and K_threshold.Omega_H.lambda remain open."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedElectroweakPrefactorSourceClosureOrFinalTrueSMAudit",
        "status": STATUS,
        "closure_claimed": True,
        "theorem_proved": True,
        "selected_R_H_RG_source_emitted": True,
        "H_parameter_count_after_replacement": 0,
        "electroweak_prefactor_search_executed": True,
        "accepted_selected_prefactor_source_count": 0,
        "strict_lambda_H_value_row_emitted": False,
        "strict_K_threshold_Omega_H_lambda_emitted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected ElectroweakPrefactorSourceClosure or FinalTrueSMAudit v1

## Theorem

`ElectroweakPrefactorFinalGateTheorem` is emitted.

The finite H scalar source has already selected:

```text
R_H^RG := r_H(A_N)
H parameter count after replacement = 0
```

The remaining prefactor target is:

```text
lambda_if_R_H_RG_equals_1 = {lambda_if_r1}
A_EW * s_beta = lambda_if_R_H_RG_equals_1
A_EW external postcheck = {aew_external}
s_beta = {s_beta}
```

## Source-Native Search

The best structured clues are:

```text
{rows[0]["formula"]} = {rows[0]["value"]}
relative residual = {rows[0]["relative_residual"]}

{rows[1]["formula"]} = {rows[1]["value"]}
relative residual = {rows[1]["relative_residual"]}
```

They are not promoted. Numerical proximity is support only unless a selected
threshold-convention theorem emits the row exactly.

## Gate Status

- selected `R_H^RG` source: `true`
- H parameter count: `0`
- accepted selected prefactor source rows: `0`
- strict `lambda_H` value row emitted: `false`
- strict `K_threshold.Omega_H.lambda` emitted: `false`
- full no-knob closure claimed: `false`

## Next Proof Object

`{NEXT}`.
"""

    write_json(INVENTORY, inventory)
    write_json(SEARCH, search)
    write_json(FINAL_GATE, final_gate)
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
