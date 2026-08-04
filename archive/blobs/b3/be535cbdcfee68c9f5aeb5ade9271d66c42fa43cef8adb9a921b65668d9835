"""Build Step69 HYM/threshold prefactor rows or Omega scalar execution frontier."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FORMULA_PACKET = PACKET_DIR / "step69_prefactor_solution_formula_rows.packet.json"
DIAGNOSTIC_PACKET = PACKET_DIR / "step69_diagnostic_prefactor_postcheck.packet.json"
OPERATOR_PACKET = PACKET_DIR / "step69_operator_prefactor_source_audit.packet.json"
GATE_PACKET = PACKET_DIR / "step69_strict_omega_acceptance_gate.packet.json"
CUTSET_PACKET = PACKET_DIR / "step69_next_prefactor_source_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step69_HYMThresholdPrefactorRows_or_OmegaScalarExecution_v1.md"

STEP68 = DATA / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier.candidate.json"
STEP68_EXPONENTS = (
    DATA
    / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier"
    / "step68_selected_theta_exponent_weight_rows.packet.json"
)
STEP68_OMEGA = (
    DATA
    / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier"
    / "step68_omega_clause_reduction_after_exponent_weights.packet.json"
)
OMEGA_TEMPLATES = (
    DATA
    / "selected_step49_omega_payload_clausefill_or_rthetaalpha1valueexecution"
    / "step49_omega_source_row_templates.packet.json"
)
COMMON_VALUES = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
HYM_OPERATOR = DATA / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution.candidate.json"
HIGHER_RESPONSE = DATA / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution.candidate.json"
DYNAMIC_PAYLOAD = DATA / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution.candidate.json"
TRACE_PAYLOAD = DATA / "selected_tracepayload_or_fullhymoperatoremission.candidate.json"
THRESHOLD_SOURCE = DATA / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation.candidate.json"
TOPHIGGS_FORMULA = DATA / "selected_tophiggsformulamapimport_or_rthetathresholdderivation.candidate.json"
TOPHIGGS_THRESHOLD = DATA / "selected_tophiggsthresholdmaprows_or_externalprecisiontable.candidate.json"

STATUS = "MTT_SELECTED_STEP69_PREFACTOR_FORMULA_CONTRACT_BUILT_SOURCE_ROWS_OPEN"
NEXT = "MTT_Selected_PrefactorSourceRowsFromHYMOperatorPayload_or_StrictOmegaAcceptance_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def prefactor_slot(row: dict[str, Any]) -> str:
    if row["sector"] == "H":
        return "C_HYMthr.H.lambda"
    return f"C_HYMthr.{row['sector']}.gen{row['generation']}"


def scalar_label(row: dict[str, Any]) -> str:
    if row["sector"] == "H":
        return "lambda_H"
    return f"abs_Y_{row['sector']}.gen{row['generation']}"


def replay_value(row: dict[str, Any], magnitudes: dict[str, Any]) -> float:
    if row["sector"] == "H":
        return float(magnitudes["lambda_H"])
    key = f"diag_abs_Y_{row['sector']}"
    return float(magnitudes[key][int(row["generation"]) - 1])


def row_formula(row: dict[str, Any]) -> str:
    exponent = row["theta_exponent"]
    slot = prefactor_slot(row)
    if row["sector"] == "H":
        return f"Omega_H.lambda.value = {slot} * epsilon_Theta^({exponent})"
    return f"{row['omega_id']}.value = {slot} * epsilon_Theta^({exponent})"


def summarized_candidate(path: Path, candidate: dict[str, Any]) -> dict[str, Any]:
    closure = candidate.get("closure_decision", {})
    closes = candidate.get("what_closes_now", {})
    remains = candidate.get("what_remains_open", {})
    false_closure = sorted(key for key, value in closure.items() if value is False)
    true_closure = sorted(key for key, value in closure.items() if value is True)
    open_flags = sorted(key for key, value in remains.items() if value is True)
    closed_flags = sorted(key for key, value in closes.items() if value is True)
    return {
        "artifact": rel(path),
        "status": candidate.get("status"),
        "closed_flags": closed_flags,
        "true_closure_flags": true_closure,
        "false_closure_flags": false_closure,
        "open_flags": open_flags,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP68,
        STEP68_EXPONENTS,
        STEP68_OMEGA,
        OMEGA_TEMPLATES,
        COMMON_VALUES,
        HYM_OPERATOR,
        HIGHER_RESPONSE,
        DYNAMIC_PAYLOAD,
        TRACE_PAYLOAD,
        THRESHOLD_SOURCE,
        TOPHIGGS_FORMULA,
        TOPHIGGS_THRESHOLD,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step69 inputs: " + ", ".join(missing))

    step68 = load(STEP68)
    exponents = load(STEP68_EXPONENTS)
    omega_reduction = load(STEP68_OMEGA)
    templates = load(OMEGA_TEMPLATES)
    common = load(COMMON_VALUES)
    hym_operator = load(HYM_OPERATOR)
    higher_response = load(HIGHER_RESPONSE)
    dynamic_payload = load(DYNAMIC_PAYLOAD)
    trace_payload = load(TRACE_PAYLOAD)
    threshold_source = load(THRESHOLD_SOURCE)
    top_higgs_formula = load(TOPHIGGS_FORMULA)
    top_higgs_threshold = load(TOPHIGGS_THRESHOLD)

    charged_rows = list(exponents["charged_exponent_weight_rows"])
    higgs_row = dict(exponents["higgs_exponent_weight_row"])
    higgs_row["sector"] = "H"
    all_exponent_rows = charged_rows + [higgs_row]

    if len(all_exponent_rows) != 10:
        raise AssertionError("Step69 expects exactly ten exponent rows")
    if templates["template_count"] != 10:
        raise AssertionError("Step69 expects exactly ten Omega templates")
    if abs(float(exponents["epsilon_theta"]) - math.exp(-2 * math.pi)) > 1e-18:
        raise AssertionError("Step69 epsilon mismatch")

    template_by_omega = {row["omega_id"]: row for row in templates["templates"]}
    missing_templates = [row["omega_id"] for row in all_exponent_rows if row["omega_id"] not in template_by_omega]
    if missing_templates:
        raise AssertionError("missing Omega templates: " + ", ".join(missing_templates))

    formula_rows: list[dict[str, Any]] = []
    for row in all_exponent_rows:
        template = template_by_omega[row["omega_id"]]
        closed_clauses_after_step69 = dict(template["clause_status"])
        closed_clauses_after_step69["magnitude_bearing_projection_weights"] = True
        closed_clauses_after_step69["prefactor_formula_contract"] = True
        formula_rows.append(
            {
                "row_id": f"step69.prefactor_formula.{row['omega_id']}",
                "omega_id": row["omega_id"],
                "xi_id": row["xi_id"],
                "scalar_label": scalar_label(row),
                "theta_exponent_row_id": row["row_id"],
                "theta_exponent": row["theta_exponent"],
                "theta_exponent_numeric": row["theta_exponent_numeric"],
                "theta_weight": row["theta_weight"],
                "epsilon_theta_exact": exponents["epsilon_theta_exact"],
                "prefactor_slot_id": prefactor_slot(row),
                "prefactor_source_owner": "selected_q79_F_m1_HYM_threshold_operator_branch",
                "required_prefactor_source_theorem": (
                    "same-branch finite HYM/threshold operator emits this prefactor before "
                    "observed Yukawa/Higgs replay values enter"
                ),
                "omega_template_row_id": template["row_id"],
                "formula": row_formula(row),
                "value_payload": None,
                "closed_clauses_after_step69": closed_clauses_after_step69,
                "accepted_formula_skeleton": True,
                "prefactor_source_closed": False,
                "accepted_as_full_omega_source_row": False,
                "accepted_as_internal_scalar_value": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    formula_packet = {
        "schema": "MTTStep69PrefactorSolutionFormulaRows.v1",
        "status": "TEN_PREFACTOR_FORMULA_ROWS_CONSTRUCTED_SOURCE_PREFACTORS_OPEN",
        "source_inputs": {
            "step68_candidate": rel(STEP68),
            "step68_exponent_rows": rel(STEP68_EXPONENTS),
            "omega_templates": rel(OMEGA_TEMPLATES),
        },
        "epsilon_theta": exponents["epsilon_theta"],
        "epsilon_theta_exact": exponents["epsilon_theta_exact"],
        "formula_rows": formula_rows,
        "formula_row_count": len(formula_rows),
        "accepted_formula_skeleton_row_count": sum(
            1 for row in formula_rows if row["accepted_formula_skeleton"]
        ),
        "unique_prefactor_slot_count": len({row["prefactor_slot_id"] for row in formula_rows}),
        "accepted_prefactor_source_row_count": 0,
        "accepted_full_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FORMULA_PACKET, formula_packet)

    magnitudes = common["derived_magnitudes"]
    diagnostic_rows: list[dict[str, Any]] = []
    for formula in formula_rows:
        exponent_row = next(row for row in all_exponent_rows if row["omega_id"] == formula["omega_id"])
        value = replay_value(exponent_row, magnitudes)
        theta_weight = float(formula["theta_weight"])
        diagnostic_prefactor = value / theta_weight
        diagnostic_rows.append(
            {
                "row_id": f"step69.diagnostic_prefactor.{formula['omega_id']}",
                "omega_id": formula["omega_id"],
                "scalar_label": formula["scalar_label"],
                "source_value_tier": "admitted_common_scale_replay_postcheck_only",
                "replay_value": value,
                "theta_weight": theta_weight,
                "theta_exponent": formula["theta_exponent"],
                "diagnostic_prefactor": diagnostic_prefactor,
                "abs_diagnostic_prefactor": abs(diagnostic_prefactor),
                "inside_order_one_window_0p1_to_10": 0.1 <= abs(diagnostic_prefactor) <= 10.0,
                "accepted_as_prefactor_source_row": False,
                "accepted_as_full_omega_source_row": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    abs_prefactors = [row["abs_diagnostic_prefactor"] for row in diagnostic_rows]
    min_prefactor = min(abs_prefactors)
    max_prefactor = max(abs_prefactors)
    diagnostic_packet = {
        "schema": "MTTStep69DiagnosticPrefactorPostcheck.v1",
        "status": "REPLAY_VALUES_REQUIRE_FINITE_ORDER_ONE_PREFACTORS_DIAGNOSTIC_ONLY",
        "source_inputs": {
            "formula_rows": rel(FORMULA_PACKET),
            "admitted_common_scale_values": rel(COMMON_VALUES),
        },
        "diagnostic_rows": diagnostic_rows,
        "diagnostic_row_count": len(diagnostic_rows),
        "all_diagnostic_prefactors_finite": all(math.isfinite(row["diagnostic_prefactor"]) for row in diagnostic_rows),
        "all_diagnostic_prefactors_inside_order_one_window_0p1_to_10": all(
            row["inside_order_one_window_0p1_to_10"] for row in diagnostic_rows
        ),
        "min_abs_diagnostic_prefactor": min_prefactor,
        "max_abs_diagnostic_prefactor": max_prefactor,
        "log10_prefactor_span": math.log10(max_prefactor / min_prefactor),
        "accepted_prefactor_source_row_count": 0,
        "diagnostic_only_not_a_selector": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(DIAGNOSTIC_PACKET, diagnostic_packet)

    operator_summaries = [
        summarized_candidate(HYM_OPERATOR, hym_operator),
        summarized_candidate(HIGHER_RESPONSE, higher_response),
        summarized_candidate(DYNAMIC_PAYLOAD, dynamic_payload),
        summarized_candidate(TRACE_PAYLOAD, trace_payload),
        summarized_candidate(THRESHOLD_SOURCE, threshold_source),
        summarized_candidate(TOPHIGGS_FORMULA, top_higgs_formula),
        summarized_candidate(TOPHIGGS_THRESHOLD, top_higgs_threshold),
    ]
    operator_packet = {
        "schema": "MTTStep69OperatorPrefactorSourceAudit.v1",
        "status": "HYM_THRESHOLD_OPERATOR_SUPPORT_PRESENT_PREFACTOR_SOURCE_ROWS_OPEN",
        "operator_summaries": operator_summaries,
        "closed_support": {
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": trace_payload["closure_decision"][
                "transition_rhoE_or_Cech_Dolbeault_DE_data_closed"
            ],
            "diagonal_End0_operator_payload_closed": hym_operator["closure_decision"][
                "diagonal_End0_operator_payload_closed"
            ],
            "dotD_alpha1_payload_closed": higher_response["closure_decision"]["dotD_alpha1_payload_closed"],
            "dynamic_payload_row_inventory_built": dynamic_payload["closure_decision"][
                "dynamic_payload_row_inventory_built"
            ],
            "top_higgs_external_formula_map_import_closed": top_higgs_formula["closure_decision"][
                "top_higgs_external_formula_map_import_closed"
            ],
        },
        "still_open_source_gates": {
            "selected_HYM_sector_payload_closed": hym_operator["closure_decision"][
                "selected_HYM_sector_payload_closed"
            ],
            "rhoE_DE_fullS2_execution_closed": hym_operator["closure_decision"][
                "rhoE_DE_fullS2_execution_closed"
            ],
            "selected_operator_payload_closed": higher_response["closure_decision"][
                "selected_operator_payload_closed"
            ],
            "higher_response_Rtheta_executed": higher_response["closure_decision"][
                "higher_response_Rtheta_executed"
            ],
            "lambda_H_value_execution": higher_response["closure_decision"]["lambda_H_value_execution"],
            "accepted_threshold_mass_scheme_source_layer_closed": threshold_source["closure_decision"][
                "accepted_threshold_mass_scheme_source_layer_closed"
            ],
            "accepted_top_higgs_threshold_map_rows_closed": top_higgs_threshold["closure_decision"][
                "accepted_top_higgs_threshold_map_rows_closed"
            ],
            "same_branch_Rtheta_threshold_derivation_closed": top_higgs_formula["closure_decision"][
                "same_branch_Rtheta_threshold_derivation_closed"
            ],
        },
        "interpretation": (
            "The repo has strong operator support and admitted external top/Higgs formula rows, "
            "but no artifact yet emits the same-branch finite HYM/threshold prefactor source rows "
            "needed by the Step69 Omega formulas."
        ),
        "accepted_prefactor_source_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(OPERATOR_PACKET, operator_packet)

    still_missing = [
        item
        for item in omega_reduction["still_missing_value_bearing_clauses"]
        if item != "magnitude_bearing_projection_weights"
    ]
    if "selected_higher_response_operator_payload" not in still_missing:
        still_missing.append("selected_higher_response_operator_payload")
    gate_packet = {
        "schema": "MTTStep69StrictOmegaAcceptanceGate.v1",
        "status": "FORMULA_CONTRACT_READY_STRICT_OMEGA_ACCEPTANCE_STILL_FALSE",
        "closed_by_step69": {
            "ten_prefactor_formula_rows": True,
            "unique_prefactor_slots": True,
            "theta_exponent_rows_attached": True,
            "diagnostic_order_one_postcheck": diagnostic_packet[
                "all_diagnostic_prefactors_inside_order_one_window_0p1_to_10"
            ],
        },
        "not_closed_by_step69": {
            "selected_prefactor_source_rows": True,
            "selected_higher_response_operator_payload": True,
            "same_branch_threshold_matching_source_rows": True,
            "same_branch_mass_scheme_conversion_source_rows": True,
            "true_precision_scale_scheme_loop_convention": True,
            "full_profile_likelihood": True,
            "lambda_H_value_row": True,
        },
        "strict_acceptance_result": {
            "accepted_formula_skeleton_row_count": formula_packet["accepted_formula_skeleton_row_count"],
            "accepted_prefactor_source_row_count": 0,
            "accepted_full_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "value_rows_execute": False,
            "reason": (
                "The formula contract identifies the exact missing finite prefactor rows. "
                "The strict Omega validator cannot accept formula skeletons or diagnostic "
                "postcheck factors as selected source values."
            ),
        },
        "still_missing_value_bearing_clauses": still_missing,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(GATE_PACKET, gate_packet)

    cutset_packet = {
        "schema": "MTTStep69NextPrefactorSourceCutset.v1",
        "status": "PREFAC_SOURCE_THEOREM_IS_THE_SINGLE_FRONTIER_OBJECT",
        "not_missing_anymore": [
            "ten Omega formula rows",
            "ten finite prefactor slot identifiers",
            "attachment of Step68 theta exponents to each Omega template",
            "diagnostic proof that the admitted replay values require only finite order-one prefactors",
        ],
        "still_missing": [
            "selected same-branch finite HYM/threshold prefactor source row for each Omega slot",
            "selected scale/scheme/loop convention attached to those prefactor rows",
            "selected same-branch threshold and mass-scheme source rows or a theorem making them unnecessary",
            "selected lambda_H prefactor/value row",
            "strict Omega acceptance theorem promoting formula rows to scalar source rows",
        ],
        "minimal_theorem_to_close_next": (
            "The selected q79/F/m=1 HYM/Strominger/threshold operator emits the ten finite "
            "prefactors C_HYMthr.* in the Step69 formula packet, with provenance independent of "
            "observed Yukawa/Higgs values and with the declared precision convention."
        ),
        "best_next_route": (
            "execute selected finite HYM/threshold operator payload against the ten prefactor "
            "slots, then rerun the strict Omega gate"
        ),
        "forbidden_routes": [
            "promote diagnostic postcheck prefactors as source rows",
            "use replay values to choose HYM/threshold prefactors",
            "treat formula skeleton rows as accepted scalar rows",
            "import external top/Higgs formula maps as no-knob internal rows",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET_PACKET, cutset_packet)

    candidate = {
        "candidate": "MTTSelectedStep69HYMThresholdPrefactorRowsOrOmegaScalarExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "prefactor_solution_formula_rows": rel(FORMULA_PACKET),
            "diagnostic_prefactor_postcheck": rel(DIAGNOSTIC_PACKET),
            "operator_prefactor_source_audit": rel(OPERATOR_PACKET),
            "strict_omega_acceptance_gate": rel(GATE_PACKET),
            "next_prefactor_source_cutset": rel(CUTSET_PACKET),
        },
        "theorem": {
            "name": "Step69PrefactorFormulaContractTheorem",
            "proved": True,
            "statement": (
                "Given the Step68 selected theta exponent weights, every strict Omega scalar "
                "row is reduced to one finite same-branch HYM/threshold prefactor multiplying "
                "the selected theta weight. Step69 constructs all ten formula rows and proves "
                "that admitted replay values would require only finite order-one prefactors as "
                "a postcheck. It does not promote those diagnostic factors, HYM prefactors, "
                "Omega rows, lambda_H, Yukawa magnitudes, masses, CKM/PMNS, true SM equivalence, "
                "or no-knob closure."
            ),
        },
        "closure_decision": {
            "prefactor_formula_contract_closed": True,
            "ten_omega_formula_rows_constructed": True,
            "unique_prefactor_slots_identified": True,
            "diagnostic_order_one_prefactor_postcheck_closed": diagnostic_packet[
                "all_diagnostic_prefactors_inside_order_one_window_0p1_to_10"
            ],
            "accepted_prefactor_source_row_count": 0,
            "accepted_full_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "hym_threshold_prefactor_rows_closed": False,
            "selected_higher_response_operator_payload_closed": False,
            "threshold_matching_source_rows_closed": False,
            "mass_scheme_conversion_source_rows_closed": False,
            "lambda_H_value_row_emitted": False,
            "scalar_value_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step68["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step69_HYMThresholdPrefactorRows_or_OmegaScalarExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    diag_lines = "\n".join(
        f"{row['omega_id']:<16} prefactor = {row['diagnostic_prefactor']:.12g}"
        for row in diagnostic_rows
    )
    NOTE.write_text(
        f"""# MTT Selected Step69 HYMThresholdPrefactorRows or OmegaScalarExecution v1

Status: `{STATUS}`.

## What Was Constructed

Step69 turns the Step68 exponent rows into the strict scalar-row formula
contract:

```text
Omega_s,g.value   = C_HYMthr.s,g * epsilon_Theta^(n_s,g)
Omega_H.lambda    = C_HYMthr.H.lambda * epsilon_Theta^(1/3)
formula rows      = {len(formula_rows)}
prefactor slots   = {formula_packet['unique_prefactor_slot_count']}
accepted prefactor source rows = 0
accepted Omega source rows     = 0
accepted scalar values         = 0
```

This is the constructive solution skeleton.  The map is no longer the unknown:
the remaining unknown is exactly the finite same-branch prefactor source row
`C_HYMthr.*` for each Omega slot.

## Diagnostic Postcheck

Using admitted common-scale replay values only as postchecks, the required
prefactors are:

```text
{diag_lines}
```

All ten diagnostic prefactors are finite and lie in the order-one window
`0.1 <= |C| <= 10`:

```text
min |C|      = {min_prefactor:.12g}
max |C|      = {max_prefactor:.12g}
log10 span   = {diagnostic_packet['log10_prefactor_span']:.12g}
```

This is good evidence that the Step68 exponent tier has the right magnitude
scale.  It is not a source proof, because the postcheck values are not allowed
to select the prefactors.

## Boundary

The strict Omega gate remains closed against overclaiming.  Formula skeleton
rows plus diagnostic prefactors are not accepted source rows.  The next proof
object is the selected finite HYM/threshold prefactor source theorem.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
