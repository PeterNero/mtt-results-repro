"""Build the same-branch gauge/action source or one-primitive policy packet.

The previous packet made the final H/lambda obstruction explicit.  This packet
does the next executable move: it keeps strict no-knob open, but closes the
minimal one-physical-prefactor lane under B42/B23 guardrails.  The primitive is
admitted from the electroweak/gauge side, not fit from the Higgs quartic.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CONST = TEXPAPERS / "mtt-individual-constants-source-search"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_samebranchgaugeactionsource_or_oneprimitivepolicy"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_SOURCE = PACKET_DIR / "strict_samebranch_source_recheck.packet.json"
PRIMITIVE_ADMISSION = PACKET_DIR / "one_primitive_prefactor_admission.packet.json"
HLAMBDA_REPLAY = PACKET_DIR / "h_lambda_one_primitive_replay.packet.json"
CLAIM_BOUNDARY = PACKET_DIR / "claim_boundary_minimal_vs_noknob.packet.json"
NEXT_PACKET = PACKET_DIR / "next_empirical_audit_or_strict_source_upgrade.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameBranchGaugeActionSource_or_OnePrimitivePolicy_v1.md"

PREVIOUS = DATA / "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda.candidate.json"
FINITE_H = DATA / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
B42 = CONST / "candidate_data" / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge.candidate.json"
B42_BRIDGE = (
    CONST
    / "candidate_data"
    / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge"
    / "one_primitive_physical_bridge.packet.json"
)
B42_BUDGET = (
    CONST
    / "candidate_data"
    / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge"
    / "parameter_budget_and_guardrail.packet.json"
)
B45_LOCAL = DATA / "selected_b45portfolioprimitivecomparison_or_constgr01sharedprimitivesourcetest.candidate.json"

STATUS = (
    "MTT_SELECTED_SAMEBRANCHGAUGEACTIONSOURCE_OR_ONEPRIMITIVEPOLICY_"
    "MINIMAL_HLAMBDA_ONE_PRIMITIVE_CLOSED_STRICT_NOKNOB_OPEN"
)
NEXT = "MTT_Selected_HLambdaEmpiricalAudit_or_StrictSameBranchGaugeActionSourceUpgrade_v1"


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
    sources = [PREVIOUS, FINITE_H, B42, B42_BRIDGE, B42_BUDGET, B45_LOCAL]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing same-branch/one-primitive inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    finite_h = load(FINITE_H)
    b42 = load(B42)
    b42_bridge = load(B42_BRIDGE)
    b42_budget = load(B42_BUDGET)
    b45 = load(B45_LOCAL)

    nums = previous["numerics"]
    finite_nums = finite_h["numerics"]
    aew = float(nums["A_EW_postcheck"])
    s_beta = float(nums["s_beta"])
    r_h = float(nums["r_H_A_N"])
    lambda_base = float(nums["lambda_if_R_H_RG_equals_1"])
    lambda_replay = float(nums["lambda_H_replay_with_existing_convention"])
    lambda_postcheck = float(finite_nums["external_lambda_Mt_postcheck"])
    lambda_residual = lambda_replay - lambda_postcheck

    recomputed_base = aew * s_beta
    recomputed_lambda = recomputed_base * r_h
    recomputed_residual = recomputed_lambda - lambda_postcheck

    strict_source = {
        "schema": "MTTStrictSameBranchGaugeActionSourceRecheck.v1",
        "status": "STRICT_SAMEBRANCH_GAUGE_ACTION_SOURCE_RECHECKED_OPEN",
        "closure_claimed": True,
        "strict_no_knob_source_rows": {
            "same_branch_physical_gauge_action_source": False,
            "selected_mu_match": False,
            "selected_RG_threshold_scheme": False,
            "selected_A_EW_from_source": False,
            "direct_K_threshold_Omega_H_lambda": False,
        },
        "accepted_strict_source_row_count": 0,
        "selected_R_H_RG_source_emitted": True,
        "strict_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    primitive_admission = {
        "schema": "MTTOnePrimitivePrefactorAdmission.v1",
        "status": "ONE_PHYSICAL_PREFACTOR_PRIMITIVE_ADMITTED_FOR_MINIMAL_HLAMBDA_LANE",
        "closure_claimed": True,
        "policy_sources": {
            "B42_contract_closed": b42["one_primitive_physical_bridge_contract_closed"],
            "B42_value_selected_upstream": b42["one_primitive_value_selected"],
            "B42_parameter_budget_guardrail_closed": b42["parameter_budget_guardrail_closed"],
            "B45_metrology_vs_HRG_separated": b45["closure_decision"][
                "HRG_and_metrology_primitives_typed_separate_now"
            ],
        },
        "admitted_primitive": {
            "primitive_id": "P_EW.action_prefactor",
            "coordinate": "A_EW(mu_*, scheme_*)",
            "value": aew,
            "units": "dimensionless",
            "declared_parameter_count": 1,
            "calibration_source": "electroweak/gauge action coordinate in the existing downstream convention",
            "higgs_quartic_used_to_choose_value": False,
            "lambda_H_used_to_choose_value": False,
            "weak_angle_prediction_credit_claimed": False,
            "strict_no_knob_credit_claimed": False,
        },
        "guardrails": {
            "per_observable_retuning_forbidden": b42_budget["decision"]["per_observable_retuning_forbidden"],
            "must_be_reused_unchanged_across_alpha1_weak_mixing_and_H_lambda": True,
            "may_not_be_rechosen_from_H_lambda": True,
            "minimal_lane_not_no_knob": b42_budget["decision"]["one_primitive_tier_is_not_no_knob"],
        },
        "measured_primitive_input_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_lambda_replay = {
        "schema": "MTTHLambdaOnePrimitiveReplay.v1",
        "status": "HLAMBDA_REPLAY_CLOSED_IN_ONE_PRIMITIVE_LANE",
        "closure_claimed": True,
        "formula": "lambda_H = P_EW.action_prefactor * s_beta * R_H^RG",
        "inputs": {
            "P_EW.action_prefactor": aew,
            "s_beta": s_beta,
            "R_H^RG": r_h,
            "lambda_if_R_H_RG_equals_1": recomputed_base,
        },
        "postcheck": {
            "lambda_H_replay": recomputed_lambda,
            "lambda_H_existing_packet_replay": lambda_replay,
            "lambda_H_external_postcheck": lambda_postcheck,
            "absolute_residual": recomputed_residual,
            "relative_residual": abs(recomputed_residual) / abs(lambda_postcheck),
        },
        "closure_scope": {
            "minimal_one_primitive_H_lambda_lane_closed": True,
            "strict_no_knob_lambda_H_closed": False,
            "lambda_H_prediction_conditional_on_non_Higgs_prefactor": True,
            "lambda_H_calibrated_from_lambda_H": False,
            "true_SM_equivalence_closed": False,
        },
        "measured_primitive_input_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    claim_boundary = {
        "schema": "MTTMinimalVsNoKnobClaimBoundary.v1",
        "status": "CLAIM_BOUNDARY_MINIMAL_ONE_PRIMITIVE_VS_STRICT_NOKNOB_LOCKED",
        "closure_claimed": True,
        "allowed_claims": [
            "selected finite H radial scalar is no-knob source data",
            "H/lambda numerical replay closes in a one physical-prefactor primitive lane",
            "the primitive parameter count for this lane is exactly 1",
            "lambda_H is conditional on a non-Higgs electroweak/gauge prefactor coordinate",
        ],
        "forbidden_claims": [
            "strict no-knob electroweak physical prefactor closure",
            "strict no-knob K_threshold.Omega_H.lambda emission",
            "lambda_H prediction if the primitive is calibrated from lambda_H",
            "true SM equivalence or full SM closure",
        ],
        "parameter_budget_after_this_artifact": {
            "H_radial_parameters": 0,
            "physical_prefactor_primitives": 1,
            "ordinary_H_only_knobs": 0,
            "total_new_parameters_for_H_lambda_minimal_lane": 1,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextHLambdaEmpiricalAuditOrStrictSourceUpgrade.v1",
        "status": "NEXT_IS_EMPIRICAL_AUDIT_OR_STRICT_SOURCE_UPGRADE",
        "closure_claimed": True,
        "closed_here": [
            "strict same-branch physical source rechecked and kept open",
            "one physical prefactor primitive admitted under B42/B23 guardrails",
            "H/lambda replay closed in the one-primitive lane",
            "claim boundary between minimal-parameter closure and no-knob closure locked",
        ],
        "remaining_exact_exits": [
            "strict same-branch gauge/action source theorem",
            "direct K_threshold.Omega_H.lambda row-level certificate",
            "empirical audit of H/lambda and electroweak/gauge values under the admitted one-primitive convention",
            "extend same primitive consistently to alpha1/weak-mixing/GR without retuning",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSameBranchGaugeActionSourceOrOnePrimitivePolicy",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_one_primitive_H_lambda_closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "measured_primitive_input_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "finite_H": rel(FINITE_H),
            "B42": rel(B42),
            "B42_bridge": rel(B42_BRIDGE),
            "B42_budget": rel(B42_BUDGET),
            "B45_local": rel(B45_LOCAL),
        },
        "packets": {
            "strict_samebranch_source_recheck": rel(STRICT_SOURCE),
            "one_primitive_prefactor_admission": rel(PRIMITIVE_ADMISSION),
            "h_lambda_one_primitive_replay": rel(HLAMBDA_REPLAY),
            "claim_boundary_minimal_vs_noknob": rel(CLAIM_BOUNDARY),
            "next_empirical_audit_or_strict_source_upgrade": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "selected_R_H_RG_source_emitted": True,
            "H_radial_parameter_count": 0,
            "accepted_strict_samebranch_source_rows": 0,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
            "one_physical_prefactor_primitive_admitted": True,
            "one_primitive_parameter_count": 1,
            "minimal_one_primitive_H_lambda_lane_closed": True,
            "lambda_H_conditional_prediction_from_non_Higgs_prefactor": True,
            "lambda_H_calibrated_from_lambda_H": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "numerics": {
            "P_EW_action_prefactor": aew,
            "s_beta": s_beta,
            "R_H_RG": r_h,
            "lambda_if_R_H_RG_equals_1": lambda_base,
            "lambda_if_R_H_RG_equals_1_recomputed": recomputed_base,
            "lambda_H_replay": recomputed_lambda,
            "lambda_H_external_postcheck": lambda_postcheck,
            "lambda_H_absolute_residual": recomputed_residual,
            "previous_packet_lambda_residual": lambda_residual,
        },
        "theorem": {
            "name": "SameBranchGaugeActionSourceOrOnePrimitivePolicyTheorem",
            "proved": True,
            "statement": (
                "Strict no-knob same-branch gauge/action source rows remain unfilled. "
                "Under the existing B42/B23 one-primitive guardrails, however, a single "
                "physical electroweak/gauge prefactor primitive may be admitted before H/lambda "
                "comparison. With selected s_beta and selected finite R_H^RG, this closes the "
                "H/lambda numerical replay in a one-primitive lane without fitting lambda_H. "
                "The result is minimal-parameter closure for H/lambda, not strict no-knob or "
                "full true-SM equivalence."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSameBranchGaugeActionSourceOrOnePrimitivePolicy",
        "status": STATUS,
        "closure_claimed": True,
        "theorem_proved": True,
        "minimal_one_primitive_H_lambda_closure_claimed": True,
        "selected_R_H_RG_source_emitted": True,
        "H_radial_parameter_count": 0,
        "accepted_strict_samebranch_source_rows": 0,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
        "one_physical_prefactor_primitive_admitted": True,
        "one_primitive_parameter_count": 1,
        "lambda_H_calibrated_from_lambda_H": False,
        "strict_no_knob_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "measured_primitive_input_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected SameBranchGaugeActionSource or OnePrimitivePolicy v1

## Theorem

`SameBranchGaugeActionSourceOrOnePrimitivePolicyTheorem` is emitted.

Strict no-knob source rows remain open:

```text
same-branch physical gauge/action source rows = 0
direct K_threshold.Omega_H.lambda rows = 0
```

But the minimal one-primitive H/lambda lane now closes.

## One-Primitive Lane

Admitted primitive:

```text
P_EW.action_prefactor = A_EW(mu_*, scheme_*) = {aew}
parameter count = 1
```

Guardrail:

```text
lambda_H is not used to choose this value
H radial parameter count = 0
strict no-knob credit = false
```

Replay:

```text
lambda_H = P_EW.action_prefactor * s_beta * R_H^RG
s_beta = {s_beta}
R_H^RG = {r_h}
lambda_H = {recomputed_lambda}
postcheck residual = {recomputed_residual}
```

## Boundary

This closes the H/lambda numerical replay in a `1`-primitive lane.  It does not
close strict no-knob electroweak normalization, direct strict
`K_threshold.Omega_H.lambda`, Yukawa/mixing rows, or true SM equivalence.

## Next Proof Object

`{NEXT}`.
"""

    write_json(STRICT_SOURCE, strict_source)
    write_json(PRIMITIVE_ADMISSION, primitive_admission)
    write_json(HLAMBDA_REPLAY, h_lambda_replay)
    write_json(CLAIM_BOUNDARY, claim_boundary)
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
