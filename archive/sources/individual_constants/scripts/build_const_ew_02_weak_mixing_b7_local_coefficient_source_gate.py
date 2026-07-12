"""Build CONST-EW-02 B7 local coefficient source gate.

B6 closed the K_EW contract and the exceptional trace-free projection formula.
B7 now asks whether the current corpus can source-select the local coefficients
c1,c2 or equivalent T1/T2 threshold entries.

The answer is a sharp partial result:
  * the local projection basis and SU2 flat-background support are usable;
  * diagnostic c1,c2 and near-hit operator weights are not promotable;
  * the next exact source object is either selected c1,c2 data or a selected
    flat FP quotient/normalization policy plus physical-quotient determinants.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b7_local_coefficient_source_gate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORTS = BASE / "source_imports.packet.json"
COEFF = BASE / "coefficient_source_gate.packet.json"
SU2 = BASE / "su2_quotient_policy_gate.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B7_LocalCoefficientSourceGate_v1.md"

STATUS = "MTT_CONST_EW_02_B7_LOCAL_COEFFICIENT_SOURCE_GATE_BUILT_VALUES_OPEN"


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

    b6_path = DATA / "const_ew_02_weak_mixing_b6_kew_kernel_gate.candidate.json"
    b6_projection_path = DATA / "const_ew_02_weak_mixing_b6_kew_kernel_gate" / "exceptional_projection_gate.packet.json"
    local_projection_path = NONSM / "certificates" / "selected_electroweak_local_projection_gate_certificate.json"
    execution_path = NONSM / "certificates" / "execution_i_threshold_profile_certificate.json"
    weight_gate_path = NONSM / "certificates" / "u1_su2_operator_weight_candidate_gate_certificate.json"
    stack_table_path = NONSM / "certificates" / "stack_determinant_candidate_table_certificate.json"
    su2_flat_path = NONSM / "certificates" / "selected_su2_threshold_background_flatness_or_fp_spectrum_certificate.json"
    su2_ghost_path = NONSM / "certificates" / "selected_su2_nonabelian_ghost_quotient_determinant_certificate.json"

    b6 = load(b6_path)
    b6_projection = load(b6_projection_path)
    local_projection = load(local_projection_path)
    execution = load(execution_path)
    weight_gate = load(weight_gate_path)
    stack_table = load(stack_table_path)
    su2_flat = load(su2_flat_path)
    su2_ghost = load(su2_ghost_path)

    exec_c1 = local_projection["execution_i_diagnostic"]["c1"]
    exec_c2 = local_projection["execution_i_diagnostic"]["c2"]
    exec_delta_alpha_12 = local_projection["execution_i_diagnostic"]["Delta_alpha_12_split"]
    exec_delta_g_12 = local_projection["execution_i_diagnostic"]["Delta_G_12_split"]

    near_hit = next(row for row in weight_gate["candidate_results"] if row["name"] == "two_thirds_u1_diagnostic")
    gut_norm = next(row for row in weight_gate["candidate_results"] if row["name"] == "gut_hypercharge_three_fifths_u1")
    flat_zero = next(row for row in su2_ghost["computed_branches"] if row["name"] == "flat_background_universal_or_absorbed_ghost")

    import_checks = {
        "B6_kernel_gate_proved": b6["theorem"]["proved"] is True,
        "B6_projection_coefficients_not_promoted": b6_projection["verdict"]["numeric_coefficients_promoted"] is False,
        "local_projection_formula_closed": local_projection["verdict"]["projection_algebra_closed"] is True,
        "execution_profile_structural_not_prediction": execution["verdict"]["structural_consistency_certified"] is True and execution["verdict"]["new_no_knob_prediction_certified"] is False,
        "operator_weight_gate_built_not_closed": weight_gate["verdict"]["operator_weight_gate_built"] is True and weight_gate["verdict"]["numeric_electroweak_closure"] is False,
        "stack_table_built_not_closed": stack_table["verdict"]["candidate_table_built"] is True and stack_table["verdict"]["new_no_knob_prediction_certified"] is False,
        "su2_flatness_closed_policy_open": su2_flat["proved_flatness_statement"]["closed"] is True and su2_flat["verdict"]["quotient_normalization_policy_closed"] is False,
        "su2_ghost_reduced_not_closed": su2_ghost["verdict"]["flat_zero_extra_branch_identified"] is True and su2_ghost["verdict"]["su2_ghost_quotient_closed"] is False,
    }
    imports_ok = all(import_checks.values())

    imports = {
        "schema": "MTTConstEW02B7SourceImports.v1",
        "status": "LOCAL_COEFFICIENT_IMPORTS_ACCEPTED_WITH_VALUE_BOUNDARY" if imports_ok else "LOCAL_COEFFICIENT_IMPORTS_INCOMPLETE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE",
        "inputs": {
            "B6_kernel_gate": rel(b6_path),
            "B6_projection_gate": rel(b6_projection_path),
            "local_projection_gate": rel(local_projection_path),
            "execution_i_threshold_profile": rel(execution_path),
            "u1_su2_operator_weight_gate": rel(weight_gate_path),
            "stack_determinant_candidate_table": rel(stack_table_path),
            "su2_threshold_flatness": rel(su2_flat_path),
            "su2_ghost_quotient": rel(su2_ghost_path),
        },
        "import_checks": import_checks,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    coefficient_gate = {
        "schema": "MTTConstEW02B7CoefficientSourceGate.v1",
        "status": "C1_C2_SOURCE_NOT_SELECTED_DIAGNOSTICS_CLASSIFIED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE",
        "closed_formula": {
            "exceptional_form": local_projection["source_claims"]["exceptional_form"],
            "Delta_alpha_12_split": local_projection["projection_formula"]["Delta_alpha_12_split"],
            "Delta_G_12_split": local_projection["projection_formula"]["Delta_G_12_split"],
        },
        "diagnostic_coefficients": {
            "Execution_I": {
                "c1": exec_c1,
                "c2": exec_c2,
                "Delta_alpha_12": exec_delta_alpha_12,
                "Delta_G_12": exec_delta_g_12,
                "classification": local_projection["classification"]["execution_i_coefficient_import"],
                "promoted": False,
            },
            "operator_weight_near_hit": {
                "name": near_hit["name"],
                "weights": near_hit["weights"],
                "lambda_12": near_hit["lambda_12"],
                "Delta_G_12": near_hit["Delta_G_12"],
                "classification": near_hit["status"],
                "promoted": False,
            },
            "gut_normalization_check": {
                "name": gut_norm["name"],
                "weights": gut_norm["weights"],
                "lambda_12": gut_norm["lambda_12"],
                "Delta_G_12": gut_norm["Delta_G_12"],
                "classification": gut_norm["status"],
                "promoted": False,
            },
        },
        "forbidden_promotions": {
            "reverse_engineered_weights": weight_gate["reverse_engineered_weights_forbidden_as_proof"],
            "small_rational_scan": "diagnostics only; near equality to a witness is not a source theorem",
            "Execution_I_c1_c2": "structural/profile support only; not independently derived as electroweak coefficients",
        },
        "source_gate": {
            "needed": "selected c1,c2 or equivalent T1,T2 from localized curvature, torsion, determinant, flux, or exceptional-divisor data",
            "current_source_coefficients_selected": local_projection["source_claims"]["source_coefficients_selected"],
            "topology_anomaly_constraints_fix_amplitudes": local_projection["classification"]["topology_anomaly_constraints_fix_amplitudes"],
            "curvature_torsion_response_coefficients": local_projection["classification"]["curvature_torsion_response_coefficients"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    su2_gate = {
        "schema": "MTTConstEW02B7SU2QuotientPolicyGate.v1",
        "status": "SU2_FLATNESS_CLOSED_QUOTIENT_POLICY_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B7-SU2-QUOTIENT-POLICY",
        "proved_flatness_statement": su2_flat["proved_flatness_statement"],
        "conditional_zero_extra_branch": {
            "status": flat_zero["status"],
            "lambda_12_candidate": flat_zero["values"]["lambda_12_candidate"],
            "p_SU2_selected": flat_zero["values"]["p_SU2_selected"],
            "selectable_now": flat_zero["selection"]["selectable_now"],
            "missing_single_source_statement": su2_ghost["conditional_theorem"]["missing_single_source_statement"],
        },
        "remaining_policy_options": su2_flat["remaining_policy_options"],
        "decision": {
            "flat_background_support_promoted": True,
            "flat_FP_quotient_policy_promoted": False,
            "curved_nonabelian_spectrum_required_now": su2_ghost["verdict"]["curved_branch_requires_new_spectrum"],
            "next_required_artifact": su2_flat["verdict"]["next_required_artifact"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B7NextWork.v1",
        "status": "NEXT_WORKORDER_FLAT_FP_POLICY_OR_C1C2_SOURCE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B8-FLAT-FP-POLICY-OR-C1C2-SOURCE",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B8-FLAT-FP-QUOTIENT-POLICY",
            "task": "Prove or refute the missing statement: selected SU2 threshold background is flat and the FP determinant is universal or Casimir-absorbed in the physical quotient.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B8-LOCAL-C1C2-SOURCE",
            "task": "Derive c1,c2 directly from selected exceptional/local curvature, torsion, determinant, flux, or divisor data.",
        },
        "why_primary": "The SU2 flat background is already source-supported; closing the quotient policy is a smaller gate than deriving all local coefficients from scratch.",
        "forbidden_shortcuts": [
            "use the two_thirds_u1 near hit as proof",
            "reverse-engineer operator weights from the diagnostic witness",
            "promote Execution-I c1,c2 without a source coefficient theorem",
            "choose FP sign or quotient absorption from closeness to measured sin^2(theta_W)",
        ],
    }

    candidate_out = {
        "candidate": "MTTConstEW02WeakMixingB7LocalCoefficientSourceGate",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE",
        "output_packets": {
            "source_imports": rel(IMPORTS),
            "coefficient_source_gate": rel(COEFF),
            "su2_quotient_policy_gate": rel(SU2),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "local_coefficient_source_hunt_executed": imports_ok,
            "diagnostic_c1_c2_classified": True,
            "near_hit_weight_gate_blocked": True,
            "SU2_flat_background_support_promoted": True,
            "B8_exact_next_gate_selected": True,
        },
        "what_remains_open": {
            "source_selected_c1_c2": True,
            "source_selected_T1_T2": True,
            "flat_FP_quotient_policy": True,
            "physical_quotient_stack_determinants": True,
            "low_scale_or_effective_sin2thetaW_prediction": True,
        },
        "theorem": {
            "name": "CONSTEW02B7LocalCoefficientSourceGateTheorem",
            "proved": imports_ok,
            "statement": (
                "The current corpus closes the exceptional projection formula and supplies source-supported SU2 flat-background data, "
                "but it does not source-select c1,c2, T1/T2, or the flat FP quotient normalization policy.  Execution-I coefficients, "
                "near-hit U1/SU2 weights, and reverse-engineered rational scans are diagnostic only.  The next exact gate is the flat "
                "FP quotient policy, in parallel with direct local c1,c2 source derivation."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B7_LocalCoefficientSourceGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "Execution_I_c1_c2_promoted": False,
        "two_thirds_near_hit_promoted": False,
        "SU2_flat_background_support_promoted": True,
        "flat_FP_quotient_policy_closed": False,
        "low_scale_electroweak_closure": False,
        "physical_sin2thetaW_value_claimed": False,
        "next_primary": "CONST-EW-02 / WEAK-MIXING / B8-FLAT-FP-QUOTIENT-POLICY",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B7 Local Coefficient Source Gate v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE`

## Result

B7 executes the local coefficient source hunt.

Closed now:

- exceptional projection formula `Delta_alpha_12 = 2*c1 - c2`,
- diagnostic coefficient classification,
- rejection of near-hit and reverse-engineered weights as proof,
- SU2 flat-background support,
- exact next gate selection.

Execution-I gives diagnostic coefficients

`c1 = {exec_c1}`, `c2 = {exec_c2}`,

and diagnostic split

`Delta_G_12 = {exec_delta_g_12}`.

These are not promoted as no-knob electroweak coefficients.

The strongest near-hit operator-weight diagnostic is

`two_thirds_u1_diagnostic`,

with `Delta_G_12 = {near_hit["Delta_G_12"]}`.

It is also not promoted.

## SU2 Gate

The selected SU2 leading threshold background is flat/source-supported, but the
physical quotient policy is still open.

The conditional zero-extra branch would give

`lambda_12 = {flat_zero["values"]["lambda_12_candidate"]}`,

but it requires the missing statement:

`{su2_ghost["conditional_theorem"]["missing_single_source_statement"]}`.

## Next

Next primary label:

`CONST-EW-02 / WEAK-MIXING / B8-FLAT-FP-QUOTIENT-POLICY`.

Parallel label:

`CONST-EW-02 / WEAK-MIXING / B8-LOCAL-C1C2-SOURCE`.
"""

    for path, payload in [
        (IMPORTS, imports),
        (COEFF, coefficient_gate),
        (SU2, su2_gate),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate_out),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
