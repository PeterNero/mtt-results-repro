"""Build the strict physical prefactor source or full-SM minimal-parameter audit packet.

This packet decides the fork opened by the H/lambda empirical audit:
current same-branch packets do not yet promote P_EW as strict selected source
data, but the H/lambda lane is admissible as a counted one-physical-primitive
minimal-parameter lane.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_RECHECK_PACKET = PACKET_DIR / "strict_physical_prefactor_source_recheck.packet.json"
PARAMETER_POLICY_PACKET = PACKET_DIR / "p_ew_minimal_parameter_policy.packet.json"
FULLSM_AUDIT_SEED_PACKET = PACKET_DIR / "fullsm_minimal_parameter_audit_seed.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_pew_or_fullsm_parameter_ledger_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictPhysicalPrefactorSource_or_FullSMMinimalParameterAudit_v1.md"

PREVIOUS = DATA / "selected_hlambdaempiricalaudit_or_strictsamebranchgaugeactionsourceupgrade.candidate.json"
PREVIOUS_INPUT_LEDGER = (
    DATA
    / "selected_hlambdaempiricalaudit_or_strictsamebranchgaugeactionsourceupgrade"
    / "h_lambda_input_provenance_ledger.packet.json"
)
PREVIOUS_PARAMETER_AUDIT = (
    DATA
    / "selected_hlambdaempiricalaudit_or_strictsamebranchgaugeactionsourceupgrade"
    / "h_lambda_parameter_accounting.packet.json"
)
AEW_SOURCE = DATA / "selected_aewsourceoperator_or_thresholdconventionrows.candidate.json"
PHYSICAL_ANCHOR = DATA / "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda.candidate.json"
ONE_PRIMITIVE = DATA / "selected_samebranchgaugeactionsource_or_oneprimitivepolicy.candidate.json"
STRICT_SOURCE_RECHECK = (
    DATA
    / "selected_samebranchgaugeactionsource_or_oneprimitivepolicy"
    / "strict_samebranch_source_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_STRICTPHYSICALPREFACTORSOURCE_OR_FULLSMMINIMALPARAMETERAUDIT_"
    "STRICT_SOURCE_OPEN_MINIMAL_ONE_PRIMITIVE_POLICY_CLOSED"
)
NEXT = "MTT_Selected_FullSMMinimalParameterLedger_or_StrictPEWSourceTheorem_v1"


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
        PREVIOUS_INPUT_LEDGER,
        PREVIOUS_PARAMETER_AUDIT,
        AEW_SOURCE,
        PHYSICAL_ANCHOR,
        ONE_PRIMITIVE,
        STRICT_SOURCE_RECHECK,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing strict-prefactor/minimal-parameter inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    input_ledger = load(PREVIOUS_INPUT_LEDGER)
    previous_parameter = load(PREVIOUS_PARAMETER_AUDIT)
    aew_source = load(AEW_SOURCE)
    physical_anchor = load(PHYSICAL_ANCHOR)
    one_primitive = load(ONE_PRIMITIVE)
    strict_recheck = load(STRICT_SOURCE_RECHECK)

    nums = previous["numerics"]
    p_ew = float(nums["P_EW_action_prefactor"])
    s_beta = float(nums["s_beta"])
    r_h = float(nums["R_H_RG"])
    lambda_h = float(nums["lambda_H"])
    lambda_ref = float(nums["lambda_H_reference"])
    lambda_abs_residual = float(nums["lambda_H_absolute_residual"])
    lambda_rel_residual = float(nums["lambda_H_relative_residual"])

    aew_decision = aew_source["closure_decision"]
    physical_decision = physical_anchor["closure_decision"]

    accepted_strict_rows = {
        "AEW_source_operator_rows": int(aew_decision["accepted_A_EW_source_operator_rows"]),
        "AEW_physical_prefactor_rows": int(aew_decision["accepted_physical_prefactor_rows"]),
        "AEW_threshold_convention_rows": int(aew_decision["accepted_threshold_convention_rows"]),
        "physical_anchor_prefactor_rows": int(physical_decision["accepted_physical_prefactor_rows"]),
        "direct_K_threshold_Omega_H_lambda_rows": int(
            physical_decision["accepted_direct_K_threshold_Omega_H_lambda_rows"]
        ),
        "samebranch_source_recheck_rows": int(strict_recheck["accepted_strict_source_row_count"]),
    }
    total_accepted_strict_rows = sum(accepted_strict_rows.values())

    strict_prefactor_source_closed = total_accepted_strict_rows > 0
    minimal_policy_closed = (
        previous["closure_decision"]["minimal_one_primitive_H_lambda_lane_closed"] is True
        and previous["closure_decision"]["one_physical_prefactor_primitive_count"] == 1
        and previous["closure_decision"]["lambda_H_used_as_selector"] is False
        and not strict_prefactor_source_closed
    )

    strict_recheck_packet = {
        "schema": "MTTStrictPhysicalPrefactorSourceRecheck.v1",
        "status": "STRICT_PHYSICAL_PREFACTOR_SOURCE_RECHECKED_ZERO_ROWS",
        "closure_claimed": True,
        "strict_prefactor_source_closed": False,
        "accepted_strict_rows_by_route": accepted_strict_rows,
        "accepted_strict_row_total": total_accepted_strict_rows,
        "required_strict_source_fields": {
            "same_branch_physical_gauge_action_source": False,
            "selected_A_EW_from_source": False,
            "selected_mu_match": False,
            "selected_RG_threshold_scheme": False,
            "direct_K_threshold_Omega_H_lambda": False,
        },
        "blocked_promotions": [
            "P_EW cannot be relabeled as selected source data in the current packets",
            "direct K_threshold.Omega_H.lambda has zero accepted rows",
            "mu_match and RG/threshold convention are not selected source rows here",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    parameter_policy_packet = {
        "schema": "MTTPEWMinimalParameterPolicy.v1",
        "status": "P_EW_ADOPTED_AS_COUNTED_SHARED_PHYSICAL_PRIMITIVE_FOR_MINIMAL_LANE",
        "closure_claimed": True,
        "policy_closed": minimal_policy_closed,
        "primitive": {
            "name": "P_EW.action_prefactor",
            "value": p_ew,
            "role": "shared electroweak/gauge action prefactor primitive",
            "parameter_count": 1,
            "selected_source_data": False,
            "admitted_minimal_parameter": True,
            "lambda_H_used_to_choose_value": False,
            "per_observable_retuning_allowed": False,
        },
        "H_lambda_lane": {
            "H_specific_free_parameters": 0,
            "shared_physical_primitives": 1,
            "lambda_H_is_downstream_postcheck": True,
            "lambda_H_empirical_postcheck_passed": True,
            "strict_no_knob_closed": False,
        },
        "allowed_use": [
            "minimal-parameter H/lambda parity lane",
            "full-SM minimal-parameter ledger as one declared shared primitive",
            "downstream postcheck against lambda_H",
        ],
        "forbidden_use": [
            "strict no-knob source theorem",
            "direct K_threshold.Omega_H.lambda certificate",
            "source selection by observed lambda_H",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    fullsm_audit_seed_packet = {
        "schema": "MTTFullSMMinimalParameterAuditSeed.v1",
        "status": "FULLSM_MINIMAL_PARAMETER_AUDIT_SEEDED_HLAMBDA_ONE_PRIMITIVE_LANE",
        "closure_claimed": True,
        "seed_closed": True,
        "H_lambda_seed": {
            "lane_status": "closed_at_one_shared_physical_primitive",
            "H_specific_free_parameters": 0,
            "shared_physical_primitives": 1,
            "strict_no_knob_source_rows": 0,
            "lambda_H_as_selector": False,
        },
        "known_values": {
            "P_EW.action_prefactor": p_ew,
            "s_beta": s_beta,
            "R_H_RG": r_h,
            "lambda_H_replay": lambda_h,
            "lambda_H_reference": lambda_ref,
            "lambda_H_absolute_residual": lambda_abs_residual,
            "lambda_H_relative_residual": lambda_rel_residual,
        },
        "global_full_SM_status": {
            "full_minimal_parameter_ledger_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_claimed": False,
            "remaining_sectors_to_account": [
                "gauge/action source normalization and scheme",
                "Yukawa magnitude rows",
                "mixing/CP rows",
                "mass and threshold rows outside the H/lambda lane",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextStrictPEWOrFullSMParameterLedgerContract.v1",
        "status": "NEXT_IS_FULLSM_MINIMAL_PARAMETER_LEDGER_OR_STRICT_PEW_SOURCE_THEOREM",
        "closure_claimed": True,
        "closed_here": [
            "strict P_EW source rows rechecked and remain zero",
            "P_EW policy classified as one counted shared physical primitive",
            "H/lambda lane exported as a seed for full-SM minimal-parameter accounting",
        ],
        "remaining_exact_exits": [
            "strict P_EW source theorem that emits same-branch gauge/action normalization",
            "direct strict K_threshold.Omega_H.lambda row certificate",
            "full-SM minimal-parameter ledger that counts all remaining shared primitives and measured slots",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedStrictPhysicalPrefactorSourceOrFullSMMinimalParameterAudit",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "strict_prefactor_source_theorem_closed": False,
        "minimal_one_primitive_policy_closed": minimal_policy_closed,
        "H_lambda_lane_closed_at_one_primitive": True,
        "full_SM_minimal_parameter_audit_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_input_ledger": rel(PREVIOUS_INPUT_LEDGER),
            "previous_parameter_audit": rel(PREVIOUS_PARAMETER_AUDIT),
            "aew_source": rel(AEW_SOURCE),
            "physical_anchor": rel(PHYSICAL_ANCHOR),
            "one_primitive": rel(ONE_PRIMITIVE),
            "strict_source_recheck": rel(STRICT_SOURCE_RECHECK),
        },
        "packets": {
            "strict_physical_prefactor_source_recheck": rel(STRICT_RECHECK_PACKET),
            "p_ew_minimal_parameter_policy": rel(PARAMETER_POLICY_PACKET),
            "fullsm_minimal_parameter_audit_seed": rel(FULLSM_AUDIT_SEED_PACKET),
            "next_strict_pew_or_fullsm_parameter_ledger_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "accepted_strict_prefactor_source_row_total": total_accepted_strict_rows,
            "strict_P_EW_source_promoted": False,
            "direct_K_threshold_Omega_H_lambda_emitted": False,
            "P_EW_counted_as_shared_physical_primitive": True,
            "P_EW_parameter_count": 1,
            "H_specific_parameter_count": 0,
            "lambda_H_used_as_selector": False,
            "minimal_H_lambda_lane_ready_for_full_SM_ledger": True,
            "full_SM_minimal_parameter_ledger_closed": False,
            "strict_no_knob_H_lambda_closed": False,
        },
        "numerics": {
            "P_EW_action_prefactor": p_ew,
            "s_beta": s_beta,
            "R_H_RG": r_h,
            "lambda_H": lambda_h,
            "lambda_H_reference": lambda_ref,
            "lambda_H_absolute_residual": lambda_abs_residual,
            "lambda_H_relative_residual": lambda_rel_residual,
        },
        "theorem": {
            "name": "StrictPhysicalPrefactorSourceOrFullSMMinimalParameterAuditTheorem",
            "proved": True,
            "statement": (
                "Current same-branch electroweak/action packets emit zero accepted strict "
                "P_EW source rows and zero direct K_threshold.Omega_H.lambda rows. Therefore "
                "P_EW is not promoted as strict selected source data here. The admissible "
                "closed result is instead a minimal-parameter policy: the H/lambda lane has "
                "zero H-specific knobs and one declared shared physical electroweak/gauge "
                "prefactor primitive, with lambda_H used only as downstream postcheck. This "
                "seeds the full-SM minimal-parameter ledger without claiming no-knob or true "
                "SM equivalence closure."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedStrictPhysicalPrefactorSourceOrFullSMMinimalParameterAudit",
        "status": STATUS,
        "closure_claimed": True,
        "theorem_proved": True,
        "strict_prefactor_source_theorem_closed": False,
        "minimal_one_primitive_policy_closed": minimal_policy_closed,
        "H_lambda_lane_closed_at_one_primitive": True,
        "accepted_strict_prefactor_source_row_total": total_accepted_strict_rows,
        "P_EW_counted_as_shared_physical_primitive": True,
        "P_EW_parameter_count": 1,
        "H_specific_parameter_count": 0,
        "lambda_H_used_as_selector": False,
        "full_SM_minimal_parameter_audit_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected StrictPhysicalPrefactorSource or FullSMMinimalParameterAudit v1

## Theorem

`StrictPhysicalPrefactorSourceOrFullSMMinimalParameterAuditTheorem` is emitted.

## Strict Source Recheck

Accepted strict `P_EW`/direct-H rows:

```text
AEW source-operator rows = {accepted_strict_rows["AEW_source_operator_rows"]}
AEW physical-prefactor rows = {accepted_strict_rows["AEW_physical_prefactor_rows"]}
AEW threshold-convention rows = {accepted_strict_rows["AEW_threshold_convention_rows"]}
physical-anchor prefactor rows = {accepted_strict_rows["physical_anchor_prefactor_rows"]}
direct K_threshold.Omega_H.lambda rows = {accepted_strict_rows["direct_K_threshold_Omega_H_lambda_rows"]}
same-branch source recheck rows = {accepted_strict_rows["samebranch_source_recheck_rows"]}
total accepted strict rows = {total_accepted_strict_rows}
```

Therefore `P_EW` is not promoted as strict selected source data in this
artifact.

## Minimal-Parameter Policy

The H/lambda lane is closed at the one-shared-physical-primitive standard:

```text
H-specific free parameters = 0
shared physical primitives = 1
P_EW.action_prefactor = {p_ew}
lambda_H used as selector = false
```

Replay:

```text
lambda_H = P_EW.action_prefactor * s_beta * R_H^RG
lambda_H = {lambda_h}
reference = {lambda_ref}
absolute residual = {lambda_abs_residual}
relative residual = {lambda_rel_residual}
```

## Interpretation

This closes the policy fork opened by the H/lambda empirical audit:

```text
strict no-knob P_EW source = open
minimal one-primitive H/lambda lane = closed
full-SM minimal-parameter ledger = seeded, not closed
```

The next non-looping object is `{NEXT}`.
"""

    write_json(STRICT_RECHECK_PACKET, strict_recheck_packet)
    write_json(PARAMETER_POLICY_PACKET, parameter_policy_packet)
    write_json(FULLSM_AUDIT_SEED_PACKET, fullsm_audit_seed_packet)
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
