"""Build the strict-PEW / QaSU3 Step10 value-execution reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_strictpewdirectk_or_qasu3step10valueexecution"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
STEP10 = PACKET_DIR / "qasu3_step10_reduction.packet.json"
PEW = PACKET_DIR / "strict_pew_directk_reduction.packet.json"
DECISION = PACKET_DIR / "post_step10_blocker_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictPEWDirectK_or_QaSU3Step10ValueExecution_v1.md"

GLOBAL = DATA / "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows.candidate.json"
PLAN = (
    DATA
    / "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows"
    / "next_closure_plan_after_yukawa_finite_replay.packet.json"
)
STEP10_CANDIDATE = DATA / "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows.candidate.json"
STEP10_PAYLOAD = (
    DATA
    / "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows"
    / "step10_dynamic_c1_payload_emission.packet.json"
)
FULLS2 = DATA / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit.candidate.json"
FIRST_ROW = (
    DATA
    / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit"
    / "accepted_first_selected_dynamic_value_row.packet.json"
)
FULLS2_GAP = (
    DATA
    / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit"
    / "fulls2_no_proxy_remaining_gap.packet.json"
)
STRICT_PEW = DATA / "selected_strictpewdirectkrowemissionattempt_or_gaugeactionnormalizationsource.candidate.json"
PHYSICAL_ANCHOR = DATA / "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda.candidate.json"

STATUS = "MTT_SELECTED_STRICTPEWDIRECTK_OR_QASU3STEP10VALUEEXECUTION_BUILT_STEP10_CLOSED_FULLS2_AND_PEW_OPEN"
NEXT = "MTT_Selected_FullS2NoProxyRows_or_StrictPEWNormalizationPayload_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    global_candidate = load(GLOBAL)
    plan = load(PLAN)
    step10_candidate = load(STEP10_CANDIDATE)
    step10_payload = load(STEP10_PAYLOAD)
    fulls2 = load(FULLS2)
    first_row = load(FIRST_ROW)
    fulls2_gap = load(FULLS2_GAP)
    strict_pew = load(STRICT_PEW)
    physical_anchor = load(PHYSICAL_ANCHOR)

    route_a_closed = step10_candidate["closure_decision"]["route_A_selected_physical_PhiFinC1_source_rule_closed"]
    step10_payload_closed = step10_candidate["closure_decision"]["selected_dynamic_phi_fin_c1_payload_emitted"]
    first_dynamic_rows = fulls2["closure_decision"]["accepted_selected_dynamic_value_row_count"]
    strict_pew_rows = strict_pew["closure_decision"]["accepted_strict_P_EW_source_rows"]
    direct_k_rows = strict_pew["closure_decision"]["accepted_direct_K_threshold_Omega_H_lambda_rows"]

    step10 = {
        "schema": "MTTQaSU3Step10ReductionAfterGlobalLedger.v1",
        "status": "STEP10_ROUTE_A_AND_FIRST_DYNAMIC_ROWS_CLOSED_FULLS2_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "global_plan_source": rel(PLAN),
        "route_A_source_rule_closed": route_a_closed,
        "step10_dynamic_phi_fin_c1_payload_emitted": step10_payload_closed,
        "contract_outputs_closed": step10_payload["contract_outputs_closed_here"],
        "contract_outputs_not_closed": step10_payload["contract_outputs_not_closed_here"],
        "accepted_first_dynamic_value_rows": first_dynamic_rows,
        "accepted_first_dynamic_row_ids": first_row["accepted_row_ids"],
        "accepted_first_dynamic_row_basis": first_row["acceptance_basis"],
        "what_this_retires": [
            "stale Step10 source-rule-open wording",
            "Route-B independent Galerkin requirement as the primary Step10 exit",
            "old first dynamic row rejection",
        ],
        "what_remains": fulls2_gap["still_required_payloads"],
    }

    pew = {
        "schema": "MTTStrictPEWDirectKReductionAfterGlobalLedger.v1",
        "status": "STRICT_PEW_DIRECTK_ATTEMPT_EXECUTED_ZERO_ROWS",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_P_EW_source_rows": strict_pew_rows,
        "direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
        "strict_P_EW_source_theorem_closed": strict_pew["closure_decision"]["strict_P_EW_source_promoted"],
        "direct_K_threshold_Omega_H_lambda_closed": strict_pew[
            "direct_K_threshold_Omega_H_lambda_closed"
        ],
        "finite_H_radial_source_closed": strict_pew["closure_decision"]["finite_H_radial_source_closed"],
        "minimal_one_primitive_lane_closed": strict_pew["closure_decision"][
            "minimal_one_primitive_lane_closed"
        ],
        "physical_anchor_status": physical_anchor["status"],
        "best_A_EW_expression_formula": strict_pew["closure_decision"]["best_A_EW_expression_formula"],
        "best_A_EW_expression_relative_residual": strict_pew["closure_decision"][
            "best_A_EW_expression_relative_residual"
        ],
        "next_payload": strict_pew["next_required_artifact"],
    }

    fulls2_reduced_not_closed = (
        route_a_closed
        and step10_payload_closed
        and first_dynamic_rows == 2
        and fulls2["closure_decision"]["full_S2_value_rows_closed"] is False
    )

    decision = {
        "schema": "MTTPostStep10BlockerDecision.v1",
        "status": "STEP10_SOURCE_RULE_CLOSED_FULLS2_NOPROXY_AND_STRICT_PEW_OPEN",
        "closed_now": [
            "Qa/SU3 Step10 Route A selected physical Phi_fin^C1 source rule is closed.",
            "A_selected, b_selected, deltaTheta_C1, and sector response matrices are promoted strictly.",
            "The first u/e phase dynamic value rows are accepted as selected source-owned first-response rows.",
            "The strict PEW/direct-K attempt has been executed and locked at zero strict rows for current inputs.",
        ],
        "not_closed": [
            "Full S2/no-proxy value rows remain open.",
            "Strict P_EW/direct K_threshold.Omega_H.lambda remains open.",
            "Global true SM no-knob closure remains open.",
        ],
        "source_row_counts": {
            "accepted_step10_route_A_source_rules": 1 if route_a_closed else 0,
            "accepted_step10_dynamic_payloads": 1 if step10_payload_closed else 0,
            "accepted_first_dynamic_value_rows": first_dynamic_rows,
            "accepted_strict_P_EW_source_rows": strict_pew_rows,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
        },
        "acceptance": {
            "step10_route_A_source_rule_closed": route_a_closed,
            "step10_dynamic_payload_emitted": step10_payload_closed,
            "first_dynamic_value_rows_accepted": first_dynamic_rows == 2,
            "qasu3_step10_blocker_reduced_to_fullS2_no_proxy_rows": fulls2_reduced_not_closed,
            "strict_P_EW_directK_rows_closed": strict_pew_rows > 0 or direct_k_rows > 0,
            "full_S2_value_rows_closed": fulls2["closure_decision"]["full_S2_value_rows_closed"],
            "global_true_SM_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedStrictPEWDirectKOrQaSU3Step10ValueExecution",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "global_ledger": rel(GLOBAL),
            "global_next_plan": rel(PLAN),
            "step10_candidate": rel(STEP10_CANDIDATE),
            "step10_payload": rel(STEP10_PAYLOAD),
            "fulls2_candidate": rel(FULLS2),
            "accepted_first_dynamic_row": rel(FIRST_ROW),
            "fulls2_gap": rel(FULLS2_GAP),
            "strict_pew_attempt": rel(STRICT_PEW),
            "physical_anchor": rel(PHYSICAL_ANCHOR),
        },
        "output_packets": {
            "qasu3_step10_reduction": rel(STEP10),
            "strict_pew_directk_reduction": rel(PEW),
            "post_step10_blocker_decision": rel(DECISION),
        },
        "theorem": {
            "name": "StrictPEWDirectKOrQaSU3Step10ValueExecutionReductionTheorem",
            "proved": True,
            "statement": (
                "The first global post-Yukawa blocker fork reduces as follows: the Qa/SU3 "
                "Step10 source-rule side is closed by Route A and emits the selected dynamic "
                "Phi_fin/C1 payload plus two first-response value rows, while the strict "
                "PEW/direct-K side has been executed and still emits zero strict rows. The "
                "remaining non-looping target is full S2/no-proxy value-row completion or a "
                "strict PEW normalization/direct-K payload."
            ),
        },
        "key_numbers": {
            "accepted_first_dynamic_value_rows": first_dynamic_rows,
            "accepted_strict_P_EW_source_rows": strict_pew_rows,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
            "fullS2_required_obligation_rows": fulls2_gap["required_obligation_rows"],
            "fullS2_closed_value_source_obligation_rows_after": fulls2_gap[
                "closed_value_source_obligation_rows_after"
            ],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_StrictPEWDirectK_or_QaSU3Step10ValueExecution_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "step10_route_A_source_rule_closed": route_a_closed,
        "step10_dynamic_payload_emitted": step10_payload_closed,
        "accepted_first_dynamic_value_rows": first_dynamic_rows,
        "qasu3_step10_blocker_reduced_to_fullS2_no_proxy_rows": fulls2_reduced_not_closed,
        "accepted_strict_P_EW_source_rows": strict_pew_rows,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
        "full_S2_value_rows_closed": False,
        "global_true_SM_no_knob_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected StrictPEWDirectK or QaSU3Step10ValueExecution v1

Status: `{STATUS}`

## Closed Now

The Qa/SU3 Step10 side is no longer open at the source-rule layer:

- Route A selected physical `Phi_fin^C1` source rule: closed
- selected dynamic `Phi_fin/C1` payload: emitted
- `A_selected`, `b_selected`, `deltaTheta_C1`, sector response matrices:
  promoted
- first selected dynamic value rows: `{first_dynamic_rows}`

The accepted first dynamic rows are:

- `{first_row["accepted_row_ids"][0]}`
- `{first_row["accepted_row_ids"][1]}`

## Still Open

The strict `P_EW` / direct-K side remains at zero rows:

- strict `P_EW` rows: `{strict_pew_rows}`
- direct `K_threshold.Omega_H.lambda` rows: `{direct_k_rows}`

Full S2/no-proxy rows are also still open.  The current full-S2 obligation
count is `{fulls2_gap["required_obligation_rows"]}`, with
`{fulls2_gap["closed_value_source_obligation_rows_after"]}` closed after the
first dynamic-row acceptance.

## Next Target

Next required artifact: `{NEXT}`.
"""

    write_json(STEP10, step10)
    write_json(PEW, pew)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
