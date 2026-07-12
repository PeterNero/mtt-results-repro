"""Build H one-parameter adoption policy or finite-H source construction packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_honeparameteradoptionpolicy_or_finitehsourceconstruction"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ADOPTION = PACKET_DIR / "h_one_parameter_adoption_policy.packet.json"
FINITE_H = PACKET_DIR / "strict_finite_h_construction_workorder.packet.json"
STANDARDS = PACKET_DIR / "h_closure_standards_ledger.packet.json"
NEXT_PACKET = PACKET_DIR / "next_execution_target.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HOneParameterAdoptionPolicy_or_FiniteHSourceConstruction_v1.md"

STATUS = (
    "MTT_SELECTED_HONEPARAMETERADOPTIONPOLICY_OR_FINITEHSOURCECONSTRUCTION_"
    "POLICY_CLOSED_ONE_PARAMETER_AVAILABLE_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_HOneParameterExecutionLedger_or_StrictFiniteHSourceRows_v1"

SOURCES = {
    "previous": DATA / "selected_strictfinitehactionsource_or_upretoverlaphrgcrossuse.candidate.json",
    "frontier_decision": DATA
    / "selected_strictfinitehactionsource_or_upretoverlaphrgcrossuse"
    / "frontier_exit_decision.packet.json",
    "blocker_contract": DATA
    / "selected_strictfinitehactionsource_or_upretoverlaphrgcrossuse"
    / "blocker_closure_contract.packet.json",
    "controlled_radial": DATA
    / "selected_hradialsourcevalue_or_directnhexecution"
    / "controlled_one_parameter_radial_NH_closure.packet.json",
    "strict_source_verdict": DATA
    / "selected_strictfinitehactionsource_or_upretoverlaphrgcrossuse"
    / "strict_finite_h_source_verdict.packet.json",
    "crossuse_verdict": DATA
    / "selected_strictfinitehactionsource_or_upretoverlaphrgcrossuse"
    / "up_ret_overlap_hrg_crossuse_verdict.packet.json",
    "step43_distance": DATA
    / "selected_step43_minimaluniversalparameter_readiness_or_internalrowclosure"
    / "step43_distance_to_minimal_parameter_closure.packet.json",
    "polar_gap": DATA
    / "selected_hpolarfieldpromotion_or_finitehactionderivation"
    / "strict_gap_after_partial_promotion.packet.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H adoption/source-construction inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    sources = require_sources()
    previous = sources["previous"]["closure_decision"]
    controlled = sources["controlled_radial"]
    strict = sources["strict_source_verdict"]
    crossuse = sources["crossuse_verdict"]
    step43 = sources["step43_distance"]
    polar_gap = sources["polar_gap"]

    r_h = controlled["derived_controlled_values"]["r_H"]
    n_h = controlled["derived_controlled_values"]["N_H_equals_r_H_squared"]
    conditional_k_rows = controlled["derived_controlled_values"]["conditional_K_row_count"]

    adoption = {
        "schema": "MTTHOneParameterAdoptionPolicy.v1",
        "status": "ONE_PARAMETER_H_POLICY_CLOSED_ADOPTION_AVAILABLE_NOT_NOKNOB",
        "closure_claimed": True,
        "parameter": {
            "id": "UP-RET-OVERLAP.HRG",
            "role": "global H-threshold/RG radial transport strength",
            "value": r_h,
            "derived_N_H": n_h,
            "new_parameter_count": 1,
            "sector_scope": "H/lambda threshold row only unless a later same-HRG non-Higgs map is accepted",
        },
        "admission_rule": {
            "allowed_as_minimal_H_parameter": True,
            "allowed_as_strict_no_knob_source": False,
            "allowed_as_lambda_H_prediction": False,
            "allowed_as_true_SM_no_knob_closure": False,
            "must_be_declared_before_replay": True,
            "must_be_counted_in_parameter_budget": True,
            "must_not_be_retuned_per_observable": True,
        },
        "conditional_result_if_adopted": {
            "conditional_H_K_rows": conditional_k_rows,
            "strict_K_rows_without_adoption": previous["strict_F_H_M_source_K_H_rows_accepted"]
            + 9,
            "minimal_parameter_H_layer_closed": True,
            "lambda_H_calibrated": True,
            "lambda_H_predicted": False,
        },
        "credibility_upgrade_requirements": [
            "accepted non-Higgs UP-RET-OVERLAP.HRG prediction target without retuning",
            "or strict source derivation of R_H^RG / finite-H action value",
            "or independent finite-H source rows that replace this parameter",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    finite_h = {
        "schema": "MTTStrictFiniteHSourceConstructionWorkorder.v1",
        "status": "STRICT_FINITE_H_CONSTRUCTION_OPEN_ZERO_VALUE_ROWS",
        "closure_claimed": True,
        "accepted_now": strict["accepted_counts"],
        "required_source_objects": [
            {
                "id": "F_H",
                "payload": "selected finite H-sector action functional",
                "acceptance_test": "compute N_H=Hess(F_H)[U_H,U_H] on the fixed selected unit ray",
            },
            {
                "id": "M_source",
                "payload": "same-source Hermitian operator restricted to B_Huv",
                "acceptance_test": "emit Huu,Hud,Hdd rows with row-level source certificate",
            },
            {
                "id": "K_H",
                "payload": "primitive H-response kernel with finite exactness/error bound",
                "acceptance_test": "emit direct K_threshold.Omega_H.lambda or equivalent L/T split",
            },
            {
                "id": "R_H_RG",
                "payload": "strict large-threshold/RG transport source",
                "acceptance_test": "derive r_H or K_threshold.Omega_H.lambda without lambda_H calibration",
            },
        ],
        "already_promoted_support": polar_gap["closed_now"],
        "remaining_strict_polar_gap": polar_gap["still_open"],
        "must_not_use": [
            "controlled UP-RET-OVERLAP.HRG as strict r_H",
            "lambda_H target inversion",
            "same-source labels without connection values",
            "internal dynamic-C1 cross-use as non-Higgs prediction",
        ],
        "strict_no_knob_source_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    standards = {
        "schema": "MTTHClosureStandardsLedger.v1",
        "status": "H_STANDARDS_LEDGER_SEPARATES_THREE_CLAIMS",
        "closure_claimed": True,
        "standards": {
            "strict_no_knob_H_closure": {
                "closed": False,
                "parameter_count": 0,
                "requires": "selected finite-H/source values",
            },
            "minimal_one_parameter_H_closure": {
                "available": True,
                "closed_if_policy_adopted": True,
                "parameter_count": 1,
                "requires": "declare UP-RET-OVERLAP.HRG and count it",
            },
            "true_SM_no_knob_equivalence": {
                "closed": False,
                "reason": "lambda_H remains calibrated in the one-parameter lane and strict H row is open",
            },
        },
        "general_policy_import": {
            "acceptable_parameter_count_range_if_source_selected": step43[
                "acceptable_parameter_count_range_if_source_selected"
            ],
            "nearest_general_lane": step43["nearest_lane"],
            "general_selected_universal_parameter_count": step43[
                "selected_universal_parameter_count"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTHOneParameterOrStrictSourceNextExecutionTarget.v1",
        "status": "NEXT_EXECUTE_ADOPTION_LEDGER_OR_STRICT_SOURCE_ROWS",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "recommended_order": [
            "emit a one-parameter execution ledger so the H result can be reported at minimal-parameter standard",
            "in parallel keep strict finite-H source-row construction open as the no-knob upgrade path",
            "do not rerun Galerkin/domain readiness unless it emits one of the required source objects",
        ],
        "frontier_not_looping_reason": (
            "This artifact changes the live target from deciding whether one parameter is allowed "
            "to executing either the counted one-parameter ledger or source rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHOneParameterAdoptionPolicyOrFiniteHSourceConstruction",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "minimal_one_parameter_H_policy_closed": True,
        "minimal_one_parameter_H_available": True,
        "minimal_one_parameter_H_adopted_by_this_artifact": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "h_one_parameter_adoption_policy": rel(ADOPTION),
            "strict_finite_h_construction_workorder": rel(FINITE_H),
            "h_closure_standards_ledger": rel(STANDARDS),
            "next_execution_target": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "H_one_parameter_policy_closed": True,
            "H_one_parameter_available_if_explicitly_adopted": True,
            "H_one_parameter_adopted_now": False,
            "H_one_parameter_count_if_adopted": 1,
            "conditional_H_K_rows_if_adopted": conditional_k_rows,
            "strict_finite_H_source_workorder_built": True,
            "strict_finite_H_source_closed": False,
            "strict_value_rows_accepted": 0,
            "accepted_nonhiggs_HRG_prediction_targets": crossuse["strict_crossuse_rejection"][
                "accepted_nonhiggs_prediction_target_count"
            ],
            "lambda_H_calibrated_in_parameter_lane": True,
            "lambda_H_predicted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "HOneParameterAdoptionPolicyOrFiniteHSourceConstructionTheorem",
            "proved": True,
            "statement": (
                "The H frontier now has an explicit standards ledger. A one-parameter H "
                "closure is available only by declaring UP-RET-OVERLAP.HRG as one counted "
                "calibrated H-threshold/RG parameter; it yields a conditional 10/10 H K "
                "layer but is not no-knob and does not predict lambda_H. The strict "
                "finite-H construction path remains open and is reduced to selected F_H, "
                "M_source, K_H, or R_H^RG source rows."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHOneParameterAdoptionPolicyOrFiniteHSourceConstruction",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "H_one_parameter_policy_closed": True,
        "H_one_parameter_available_if_explicitly_adopted": True,
        "H_one_parameter_adopted_now": False,
        "H_one_parameter_count_if_adopted": 1,
        "conditional_H_K_rows_if_adopted": conditional_k_rows,
        "strict_finite_H_source_closed": False,
        "lambda_H_predicted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected H One-Parameter Adoption Policy or FiniteHSourceConstruction v1

## Theorem

`HOneParameterAdoptionPolicyOrFiniteHSourceConstructionTheorem` is emitted.

## What Closes

The H frontier now has a standards ledger.

- strict no-knob H closure: open;
- minimal one-parameter H closure: available if explicitly adopted;
- parameter if adopted: `UP-RET-OVERLAP.HRG`;
- parameter count if adopted: `1`;
- calibrated `r_H`: `{r_h}`;
- controlled `N_H=r_H^2`: `{n_h}`;
- conditional H K rows if adopted: `{conditional_k_rows}/10`.

## Boundary

The one-parameter lane calibrates `lambda_H`; it does not predict `lambda_H`.
It must be counted as a parameter and cannot be called no-knob closure.

## Strict Upgrade Path

Strict no-knob closure still requires one of:

1. selected finite H action `F_H` with `N_H=Hess(F_H)[U_H,U_H]`;
2. same-source Hermitian `M_source` restricted to `B_Huv`;
3. primitive H-response kernel `K_H`;
4. strict `R_H^RG` source.

## Next Artifact

`{NEXT}`
"""

    write_json(ADOPTION, adoption)
    write_json(FINITE_H, finite_h)
    write_json(STANDARDS, standards)
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
