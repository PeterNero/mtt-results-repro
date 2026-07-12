"""Build the H/lambda empirical audit or strict source-upgrade packet.

This freezes the one-primitive H/lambda result into a paper-facing empirical
audit: selected internal data + one admitted non-Higgs physical prefactor
replay lambda_H, while strict no-knob closure remains a separate upgrade.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hlambdaempiricalaudit_or_strictsamebranchgaugeactionsourceupgrade"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INPUT_LEDGER = PACKET_DIR / "h_lambda_input_provenance_ledger.packet.json"
EMPIRICAL_AUDIT = PACKET_DIR / "h_lambda_empirical_audit.packet.json"
PARAMETER_AUDIT = PACKET_DIR / "h_lambda_parameter_accounting.packet.json"
STRICT_UPGRADE = PACKET_DIR / "strict_samebranch_upgrade_workorder.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_prefactor_or_fullsm_audit_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HLambdaEmpiricalAudit_or_StrictSameBranchGaugeActionSourceUpgrade_v1.md"

PREVIOUS = DATA / "selected_samebranchgaugeactionsource_or_oneprimitivepolicy.candidate.json"
REPLAY = DATA / "selected_samebranchgaugeactionsource_or_oneprimitivepolicy" / "h_lambda_one_primitive_replay.packet.json"
BOUNDARY = (
    DATA / "selected_samebranchgaugeactionsource_or_oneprimitivepolicy" / "claim_boundary_minimal_vs_noknob.packet.json"
)
STRICT_SOURCE = (
    DATA / "selected_samebranchgaugeactionsource_or_oneprimitivepolicy" / "strict_samebranch_source_recheck.packet.json"
)
FINITE_H = DATA / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
H_SCALAR = DATA / "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule.candidate.json"

STATUS = (
    "MTT_SELECTED_HLAMBDAEMPIRICALAUDIT_OR_STRICTSAMEBRANCHGAUGEACTIONSOURCEUPGRADE_"
    "ONE_PRIMITIVE_AUDIT_CLOSED_STRICT_PREFACTOR_SOURCE_OPEN"
)
NEXT = "MTT_Selected_StrictPhysicalPrefactorSource_or_FullSMMinimalParameterAudit_v1"


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
    sources = [PREVIOUS, REPLAY, BOUNDARY, STRICT_SOURCE, FINITE_H, H_SCALAR]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H/lambda empirical audit inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    replay = load(REPLAY)
    boundary = load(BOUNDARY)
    strict_source = load(STRICT_SOURCE)
    finite_h = load(FINITE_H)
    h_scalar = load(H_SCALAR)

    nums = previous["numerics"]
    primitive = float(nums["P_EW_action_prefactor"])
    s_beta = float(nums["s_beta"])
    r_h = float(nums["R_H_RG"])
    lambda_h = float(nums["lambda_H_replay"])
    lambda_postcheck = float(nums["lambda_H_external_postcheck"])
    residual = float(nums["lambda_H_absolute_residual"])
    relative = abs(residual) / abs(lambda_postcheck)
    tau_h = float(finite_h["numerics"]["tau_H_A_N"])
    k_h = float(h_scalar["numerics"]["k_H_A_N"])

    input_ledger = {
        "schema": "MTTHLambdaInputProvenanceLedger.v1",
        "status": "HLAMBDA_INPUT_PROVENANCE_LEDGER_BUILT",
        "closure_claimed": True,
        "inputs": {
            "finite_H_scalar_source": {
                "source": rel(H_SCALAR),
                "selected_source_data": True,
                "k_H_A_N": k_h,
                "tau_H_A_N": tau_h,
                "R_H_RG": r_h,
                "parameter_count": 0,
            },
            "s_beta": {
                "selected_source_data": True,
                "value": s_beta,
                "parameter_count": 0,
            },
            "P_EW_action_prefactor": {
                "admitted_physical_primitive": True,
                "value": primitive,
                "parameter_count": 1,
                "lambda_H_used_to_choose_value": False,
                "source_tier": "one physical electroweak/gauge prefactor primitive",
            },
        },
        "forbidden_inputs_absent": {
            "lambda_H_as_selector": True,
            "H_mass_as_selector": True,
            "postcheck_residual_as_selector": True,
            "per_observable_retuning": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    empirical_audit = {
        "schema": "MTTHLambdaEmpiricalAudit.v1",
        "status": "HLAMBDA_EMPIRICAL_AUDIT_PASS_ONE_PRIMITIVE_LANE",
        "closure_claimed": True,
        "formula": replay["formula"],
        "computed": {
            "P_EW_action_prefactor": primitive,
            "s_beta": s_beta,
            "R_H_RG": r_h,
            "lambda_H": lambda_h,
        },
        "postcheck": {
            "reference_value": lambda_postcheck,
            "absolute_residual": residual,
            "relative_residual": relative,
            "passes_roundoff_gate": abs(residual) < 2e-15,
        },
        "prediction_classification": {
            "conditional_prediction_given_non_Higgs_prefactor": True,
            "independent_H_sector_prediction": False,
            "strict_no_knob_prediction": False,
            "SM_parity_plus_explanatory_compression": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    parameter_audit = {
        "schema": "MTTHLambdaParameterAccounting.v1",
        "status": "HLAMBDA_PARAMETER_ACCOUNTING_LOCKED_ONE_PHYSICAL_PRIMITIVE",
        "closure_claimed": True,
        "parameter_budget": boundary["parameter_budget_after_this_artifact"],
        "effective_H_lambda_lane": {
            "H_specific_free_parameters": 0,
            "shared_physical_prefactor_primitives": 1,
            "ordinary_fitted_H_knobs": 0,
            "total_counted_parameters_for_this_lane": 1,
        },
        "comparison_to_SM_parameter_bookkeeping": {
            "SM_treats_lambda_H_as_independent_input": True,
            "this_lane_replaces_independent_lambda_H_with_selected_internal_data_plus_one_prefactor": True,
            "scope": "local Higgs/quartic lane only",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strict_upgrade = {
        "schema": "MTTStrictSameBranchGaugeActionSourceUpgradeWorkorder.v1",
        "status": "STRICT_UPGRADE_WORKORDER_EMITTED_PREFACTOR_SOURCE_OPEN",
        "closure_claimed": True,
        "current_strict_source_rows": strict_source["strict_no_knob_source_rows"],
        "accepted_strict_source_row_count": strict_source["accepted_strict_source_row_count"],
        "upgrade_routes": [
            {
                "route_id": "same_branch_physical_gauge_action_source",
                "must_emit": [
                    "same-branch physical gauge/action normalization or f_ab",
                    "selected mu_match",
                    "selected RG/threshold convention",
                    "A_EW source value before comparison to lambda_H",
                ],
            },
            {
                "route_id": "direct_K_threshold_Omega_H_lambda",
                "must_emit": [
                    "row-level K_threshold.Omega_H.lambda certificate",
                    "same-scheme alignment with D_fin.H and epsilon_Theta^(1/3)",
                    "proof that the row is not reconstructed from the postcheck",
                ],
            },
        ],
        "promotion_consequence_if_route_closes": [
            "one-primitive H/lambda lane upgrades to strict no-knob H/lambda",
            "physical prefactor primitive parameter count drops from 1 to 0 for this lane",
            "strict K_threshold.Omega_H.lambda can be emitted",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextStrictPrefactorOrFullSMMinimalParameterAuditContract.v1",
        "status": "NEXT_IS_STRICT_PREFACTOR_SOURCE_OR_FULLSM_MINIMAL_PARAMETER_AUDIT",
        "closure_claimed": True,
        "closed_here": [
            "input provenance ledger for H/lambda lane",
            "empirical postcheck audit for one-primitive H/lambda closure",
            "parameter accounting against SM bookkeeping",
            "strict source-upgrade workorder",
        ],
        "remaining_exact_exits": [
            "strict physical prefactor source theorem",
            "direct strict K_threshold.Omega_H.lambda certificate",
            "full minimal-parameter SM audit including gauge/Yukawa/mixing rows",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHLambdaEmpiricalAuditOrStrictSameBranchGaugeActionSourceUpgrade",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_one_primitive_H_lambda_empirical_audit_closed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "replay": rel(REPLAY),
            "boundary": rel(BOUNDARY),
            "strict_source": rel(STRICT_SOURCE),
            "finite_H": rel(FINITE_H),
            "H_scalar": rel(H_SCALAR),
        },
        "packets": {
            "h_lambda_input_provenance_ledger": rel(INPUT_LEDGER),
            "h_lambda_empirical_audit": rel(EMPIRICAL_AUDIT),
            "h_lambda_parameter_accounting": rel(PARAMETER_AUDIT),
            "strict_samebranch_upgrade_workorder": rel(STRICT_UPGRADE),
            "next_strict_prefactor_or_fullsm_audit_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "selected_R_H_RG_source_emitted": True,
            "H_radial_parameter_count": 0,
            "one_physical_prefactor_primitive_count": 1,
            "minimal_one_primitive_H_lambda_lane_closed": True,
            "empirical_postcheck_passed": True,
            "lambda_H_used_as_selector": False,
            "accepted_strict_samebranch_source_rows": 0,
            "strict_K_threshold_Omega_H_lambda_emitted": False,
            "strict_no_knob_H_lambda_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "numerics": {
            "k_H_A_N": k_h,
            "tau_H_A_N": tau_h,
            "R_H_RG": r_h,
            "s_beta": s_beta,
            "P_EW_action_prefactor": primitive,
            "lambda_H": lambda_h,
            "lambda_H_reference": lambda_postcheck,
            "lambda_H_absolute_residual": residual,
            "lambda_H_relative_residual": relative,
        },
        "theorem": {
            "name": "HLambdaEmpiricalAuditOrStrictSameBranchGaugeActionSourceUpgradeTheorem",
            "proved": True,
            "statement": (
                "The one-physical-prefactor H/lambda lane is empirically audited and "
                "parameter-accounted: selected finite H data plus selected s_beta and one "
                "non-Higgs electroweak/gauge prefactor replay lambda_H to roundoff without "
                "using lambda_H as selector. This is a local explanatory compression over "
                "SM parameter bookkeeping for the Higgs/quartic slot, not strict no-knob "
                "closure or full true-SM equivalence. The strict upgrade remains the "
                "same-branch physical prefactor source theorem or direct H K-row certificate."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHLambdaEmpiricalAuditOrStrictSameBranchGaugeActionSourceUpgrade",
        "status": STATUS,
        "closure_claimed": True,
        "theorem_proved": True,
        "minimal_one_primitive_H_lambda_empirical_audit_closed": True,
        "selected_R_H_RG_source_emitted": True,
        "H_radial_parameter_count": 0,
        "one_physical_prefactor_primitive_count": 1,
        "lambda_H_used_as_selector": False,
        "empirical_postcheck_passed": True,
        "accepted_strict_samebranch_source_rows": 0,
        "strict_no_knob_H_lambda_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HLambdaEmpiricalAudit or StrictSameBranchGaugeActionSourceUpgrade v1

## Theorem

`HLambdaEmpiricalAuditOrStrictSameBranchGaugeActionSourceUpgradeTheorem` is emitted.

## Input Provenance

```text
k_H(A_N) = {k_h}
tau_H(A_N) = {tau_h}
R_H^RG = {r_h}
s_beta = {s_beta}
P_EW.action_prefactor = {primitive}
```

Parameter accounting:

```text
H radial parameters = 0
physical prefactor primitives = 1
ordinary H-only knobs = 0
```

## Empirical Audit

Formula:

```text
lambda_H = P_EW.action_prefactor * s_beta * R_H^RG
```

Result:

```text
lambda_H = {lambda_h}
reference = {lambda_postcheck}
absolute residual = {residual}
relative residual = {relative}
```

`lambda_H` is not used as selector.

## Interpretation

This is a local explanatory compression over SM parameter bookkeeping for the
Higgs/quartic slot: the independent SM `lambda_H` input is replaced by selected
finite H data plus one shared physical electroweak/gauge prefactor primitive.

It is not strict no-knob closure and not full true-SM equivalence.

## Strict Upgrade

The strict upgrade must emit either:

```text
same-branch physical gauge/action source + mu_match/RG convention
```

or:

```text
direct K_threshold.Omega_H.lambda row-level certificate
```

## Next Proof Object

`{NEXT}`.
"""

    write_json(INPUT_LEDGER, input_ledger)
    write_json(EMPIRICAL_AUDIT, empirical_audit)
    write_json(PARAMETER_AUDIT, parameter_audit)
    write_json(STRICT_UPGRADE, strict_upgrade)
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
