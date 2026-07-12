"""Build CONST-EW-02 B23 cross-use universal-parameter admissibility theorem.

B23 clarifies the superset strategy for provisional universal parameters:
a shared parameter may be fixed once by an independent sector and then tested
elsewhere. That is a legitimate reduced-parameter tier, not strict no-knob
closure and not per-observable fitting.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b23_cross_use_universal_parameter_admissibility"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
THEOREM_PACKET = BASE / "cross_use_admissibility_theorem.packet.json"
PROTOCOL_PACKET = BASE / "fit_once_predict_elsewhere_protocol.packet.json"
LEDGER_PACKET = BASE / "u_dyn_u_phys_cross_use_ledger.packet.json"
BOUNDARY = BASE / "weak_mixing_b23_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B23_CrossUseUniversalParameterAdmissibility_v1.md"

STATUS = "MTT_CONST_EW_02_B23_CROSS_USE_UNIVERSAL_PARAMETER_ADMISSIBILITY_BUILT"


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
    BASE.mkdir(parents=True, exist_ok=True)

    b22_path = DATA / "const_ew_02_weak_mixing_b22_parameterized_bridge_replay.candidate.json"
    b22_replay_path = DATA / "const_ew_02_weak_mixing_b22_parameterized_bridge_replay" / "symbolic_weak_angle_replay.packet.json"
    b22_strict_path = DATA / "const_ew_02_weak_mixing_b22_parameterized_bridge_replay" / "strict_source_promotion_gate.packet.json"
    b22_param_path = DATA / "const_ew_02_weak_mixing_b22_parameterized_bridge_replay" / "universal_parameter_pressure_test.packet.json"
    b21_param_path = DATA / "const_ew_02_weak_mixing_b21_dynamic_c1_or_free_parameter_bridge" / "provisional_universal_parameter_bridge.packet.json"
    global_policy_path = DATA / "constant_frontier_ledger" / "universal_parameter_policy_import.packet.json"
    alpha_frontier_path = DATA / "const_em_01_alpha1_frontier_closure_ledger.candidate.json"
    alpha_frontier_cert_path = CERTS / "const_em_01_alpha1_frontier_closure_ledger_certificate.json"

    b22 = load(b22_path)
    b22_replay = load(b22_replay_path)
    b22_strict = load(b22_strict_path)
    b22_param = load(b22_param_path)
    b21_param = load(b21_param_path)
    global_policy = load(global_policy_path)
    alpha_frontier = load(alpha_frontier_path)
    alpha_frontier_cert = load(alpha_frontier_cert_path)

    theorem_packet = {
        "schema": "MTTConstEW02B23CrossUseUniversalParameterAdmissibilityTheorem.v1",
        "status": "CROSS_USE_UNIVERSAL_PARAMETER_TIER_FORMALIZED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B23-CROSS-USE-UNIVERSAL-PARAMETER-ADMISSIBILITY",
        "inputs": {
            "B22_candidate": rel(b22_path),
            "B22_symbolic_replay": rel(b22_replay_path),
            "B22_strict_gate": rel(b22_strict_path),
            "B22_parameter_pressure_test": rel(b22_param_path),
            "B21_parameter_bridge": rel(b21_param_path),
            "global_universal_parameter_policy": rel(global_policy_path),
            "alpha1_frontier_ledger": rel(alpha_frontier_path),
            "alpha1_frontier_certificate": rel(alpha_frontier_cert_path),
        },
        "tier_definitions": {
            "strict_no_knob": {
                "definition": "Parameter is derived from selected MTT source data before empirical comparison.",
                "may_use_observed_constant_to_set_parameter": False,
                "claim_allowed": "strict no-knob closure if all other source gates close",
            },
            "cross_use_universal_parameter": {
                "definition": "Parameter is declared once globally, fixed by at most one independent sector or measurement, and then reused unchanged in other sectors as predictions/checks.",
                "may_use_one_independent_measurement_to_set_parameter": True,
                "minimum_independent_uses": 2,
                "claim_allowed": "reduced-parameter or universal-parameter closure, not no-knob closure",
            },
            "bad_fitting": {
                "definition": "Parameter is retuned per observable, sector, constant, branch, or residual.",
                "allowed": False,
                "claim_allowed": "none",
            },
        },
        "admissibility_conditions": [
            "parameter declared once with a stable name and domain",
            "parameter is global, not sector-specific",
            "source branch is selected before target comparison or fixed by an explicitly declared calibration sector",
            "at most one independent empirical calibration per parameter",
            "all other sectors receive the identical value unchanged",
            "calibration sector and prediction sectors are logged before evaluating success",
            "no no-knob claim until the parameter is derived from selected source data",
        ],
        "forbidden_shortcuts": [
            "choose u_dyn from weak angle and then also call the weak angle predicted",
            "choose u_phys from alpha and then call alpha no-knob",
            "retune u_dyn for CKM, PMNS, Yukawa, weak angle, or alpha separately",
            "use the same symbol for different numerical values in different encodings",
            "drop failed cross-use sectors after seeing results",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    protocol_packet = {
        "schema": "MTTConstEW02B23FitOncePredictElsewhereProtocol.v1",
        "status": "FIT_ONCE_PREDICT_ELSEWHERE_PROTOCOL_BUILT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B23-BRIDGE-AUDIT-NO-BACKFIT",
        "calibration_modes": {
            "source_derived": {
                "rank": 1,
                "description": "No empirical calibration; selected source theorem emits parameter value.",
                "strict_no_knob_possible": True,
            },
            "single_empirical_calibration": {
                "rank": 2,
                "description": "One independent observable fixes the parameter; all other observables are predictions conditional on that calibration.",
                "strict_no_knob_possible": False,
            },
            "multi_target_fit": {
                "rank": 3,
                "description": "Multiple observables jointly tune the same parameter.",
                "allowed_for_exploration": True,
                "claim_allowed": "diagnostic only; not closure",
            },
            "per_observable_retune": {
                "rank": 4,
                "description": "Parameter value changes per observable.",
                "allowed": False,
            },
        },
        "audit_fields_required_for_each_parameter": [
            "parameter_name",
            "domain_and_units",
            "declared_before_observable_check",
            "calibration_source_or_theorem",
            "calibration_observable_if_any",
            "prediction_observables",
            "single_value_hash_or_exact_expression",
            "failure_policy",
        ],
        "success_rule": "A cross-use parameter becomes credible only if at least one non-calibration sector is reproduced or sharply constrained without retuning.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    ledger_packet = {
        "schema": "MTTConstEW02B23UDynUPhysCrossUseLedger.v1",
        "status": "U_DYN_U_PHYS_CROSS_USE_LEDGER_INITIALIZED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B23-U-DYN-U-PHYS-CROSS-USE-LEDGER",
        "global_policy": {
            "maximum_live_universal_parameters": global_policy["maximum_live_universal_parameters"],
            "selected_parameter_count_now": global_policy["selected_parameter_count_now"],
            "current_B23_live_provisional_parameters": 2,
            "strict_no_knob_selected_parameter_count": 0,
        },
        "parameters": {
            "u_dyn": {
                "status": "PROVISIONAL_NOT_SELECTED",
                "domain": "dimensionless dynamic transfer/source-strength bridge",
                "weak_angle_role": b22_replay["no_threshold_bridge_lane"]["formula"],
                "candidate_cross_uses": [
                    "weak mixing no-threshold profile y",
                    "dynamic C1 transfer/Hessian normalization",
                    "alpha1 source-strength/retarded derivative if same-source theorem emits it",
                    "future Yukawa/CKM primitive C1 contractions only if same value is locked first",
                ],
                "may_be_calibrated_once": True,
                "recommended_calibration_priority": [
                    "selected source theorem",
                    "alpha1/source-strength theorem",
                    "one independent empirical sector, then weak angle becomes a prediction",
                ],
                "cannot_claim_no_knob": True,
            },
            "u_phys": {
                "status": "PROVISIONAL_NOT_SELECTED",
                "domain": "physical unit/metrology anchor",
                "weak_angle_role": b22_replay["u_phys_lane"]["reason"],
                "candidate_cross_uses": [
                    "alpha_phys physical normalization",
                    "rod/clock or central-circle metrology",
                    "M-theory/modal-gap physical unit",
                    "weak mixing only through shared physical-unit anchoring if later needed",
                ],
                "may_be_calibrated_once": True,
                "recommended_calibration_priority": [
                    "central-circle rod/clock theorem",
                    "M-theory/modal-gap source theorem",
                    "one independent physical-unit measurement, then alpha/weak become conditional predictions",
                ],
                "cannot_claim_no_knob": True,
            },
        },
        "current_allowed_use": "Keep B22 weak-angle replay as a function of u_dyn and use u_phys only as reserved alpha/metrology bridge until a cross-use calibration is declared.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B23Boundary.v1",
        "status": "CROSS_USE_POLICY_CLOSED_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B23-BOUNDARY",
        "closed_now": {
            "cross_use_universal_parameter_tier_formalized": True,
            "fit_once_predict_elsewhere_protocol_built": True,
            "u_dyn_u_phys_cross_use_ledger_initialized": True,
            "superset_strategy_allows_shared_parameter_cross_use": True,
            "bad_per_observable_retuning_forbidden": True,
        },
        "still_open": {
            "u_dyn_source_derivation_or_single_calibration": True,
            "u_phys_source_derivation_or_single_calibration": True,
            "weak_angle_physical_closure": True,
            "alpha_phys_physical_closure": alpha_frontier_cert["strict_no_knob_alpha_phys_closed"] is False,
            "strict_no_knob_closure": True,
            "cross_use_success_test": True,
        },
        "allowed_next_claim_if_calibrated_once": "universal-parameter conditional prediction tier",
        "forbidden_next_claim_if_calibrated_once": "strict no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B23NextWork.v1",
        "status": "NEXT_WORKORDER_CROSS_USE_TEST_OR_SOURCE_DERIVATION",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B24-CROSS-USE-TEST-OR-SOURCE-DERIVATION",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B24-U-DYN-SOURCE-DERIVATION",
            "task": "Try to derive u_dyn from selected same-source dynamic transfer, honest Galerkin C1 contractions, or alpha1/source-strength.",
        },
        "bridge": {
            "label": "CONST-EW-02 / WEAK-MIXING / B24-FIT-ONCE-PREDICT-ELSEWHERE-CROSS-USE-TEST",
            "task": "Pick one declared calibration source for u_dyn or u_phys and evaluate all other sectors without retuning.",
        },
        "paper_update": {
            "label": "CONST-EW-02 / WEAK-MIXING / B24-PAPER-CLAIM-LANGUAGE",
            "task": "Add language distinguishing no-knob, universal-parameter closure, and forbidden fitting in the later paper patch.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB23CrossUseUniversalParameterAdmissibility",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B23-RETIRE-U-DYN-OR-BRIDGE-AUDIT",
        "output_packets": {
            "cross_use_admissibility_theorem": rel(THEOREM_PACKET),
            "fit_once_predict_elsewhere_protocol": rel(PROTOCOL_PACKET),
            "u_dyn_u_phys_cross_use_ledger": rel(LEDGER_PACKET),
            "weak_mixing_b23_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B23CrossUseUniversalParameterAdmissibilityTheorem",
            "proved": True,
            "statement": (
                "A provisional parameter may be admitted in the superset strategy "
                "if it is declared once, shared across at least two independent "
                "uses, and either source-derived or calibrated once with all other "
                "uses becoming predictions. This creates a legitimate "
                "universal-parameter tier but not strict no-knob closure. "
                "Per-observable retuning remains forbidden."
            ),
        },
        "cross_use_tier_formalized": True,
        "fit_once_predict_elsewhere_protocol_built": True,
        "strict_no_knob_closed": False,
        "universal_parameter_closure_claimed": False,
        "physical_weak_angle_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B23_CrossUseUniversalParameterAdmissibility_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "cross_use_tier_formalized": True,
        "fit_once_predict_elsewhere_protocol_built": True,
        "declared_live_provisional_parameters": ["u_dyn", "u_phys"],
        "minimum_independent_uses": 2,
        "single_empirical_calibration_allowed": True,
        "per_observable_retuning_allowed": False,
        "strict_no_knob_closed": False,
        "universal_parameter_closure_claimed": False,
        "physical_weak_angle_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_bridge": next_work["bridge"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B23 Cross Use Universal Parameter Admissibility v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B23-RETIRE-U-DYN-OR-BRIDGE-AUDIT`

## Theorem

A provisional parameter is admissible under the superset strategy when it is:

```text
declared once,
global rather than sector-specific,
shared across at least two independent uses,
source-derived or calibrated once,
then reused unchanged for every other sector.
```

This is legitimate universal-parameter closure if it works, but it is not strict
no-knob closure until the parameter is derived from selected MTT source data.

## Current Ledger

```text
u_dyn  = provisional dynamic transfer/source-strength bridge
u_phys = provisional physical unit/metrology bridge
```

Allowed:

```text
fix u_dyn from one independent sector, then predict weak angle or C1 elsewhere
fix u_phys from one independent unit/anchor sector, then predict alpha/weak links
```

Forbidden:

```text
retune u_dyn per weak angle, CKM, PMNS, Yukawa, or alpha
use observed weak angle to choose u_dyn and then call weak angle predicted
call any calibrated parameter strict no-knob
```

## Next

`CONST-EW-02 / WEAK-MIXING / B24-CROSS-USE-TEST-OR-SOURCE-DERIVATION`
"""

    for path, payload in [
        (THEOREM_PACKET, theorem_packet),
        (PROTOCOL_PACKET, protocol_packet),
        (LEDGER_PACKET, ledger_packet),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
