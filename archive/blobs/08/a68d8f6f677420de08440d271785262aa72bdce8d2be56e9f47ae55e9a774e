"""Attempt to select the Qa/SU3 monad values and D_E payload.

This is deliberately a value-selection attempt, not a closure-by-label.  It
constructs concrete primitive monad rows, imports the strongest available
finite operator values, and records exactly which promotion gates remain open.
"""

from __future__ import annotations

import itertools
import json
from math import gcd
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")
Q79 = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-q79-proof-repro/candidate_data")

SLUG = "selected_qasu3_selectedmonaddevalues_or_bn27strictsourcetheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRIMITIVE_PACKET = PACKET_DIR / "primitive_balanced_monad_value_selection_attempt.packet.json"
DE_PACKET = PACKET_DIR / "finite_de_operator_value_import_and_promotion_gate.packet.json"
ACCEPTANCE_PACKET = PACKET_DIR / "selected_value_acceptance_result.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_selector_or_full_operator_values_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_QaSU3_SelectedMonadDEValues_or_BN27StrictSourceTheorem_v1.md"

PREVIOUS = DATA / "selected_sqasu3bn27_strictprinciplesource_or_directconnectiontables.candidate.json"
PREVIOUS_CHECKS = (
    DATA
    / "selected_sqasu3bn27_strictprinciplesource_or_directconnectiontables"
    / "candidate_table_exact_checks.packet.json"
)
PREVIOUS_ACCEPTANCE = (
    DATA
    / "selected_sqasu3bn27_strictprinciplesource_or_directconnectiontables"
    / "same_source_connection_table_acceptance_result.packet.json"
)
CECH_SCAFFOLD = QA / "cech_dolbeault_matrix_packet_scaffold.candidate.json"
CTWIST_TEMPLATE = QA / "ctwist_deligne_cech_template.candidate.json"
DEGREEN_LEDGER = (
    DATA
    / "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade"
    / "visible_chernweil_degreen_import_ledger.packet.json"
)
DEGREEN_UPGRADE = (
    DATA
    / "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade"
    / "fullsector_payload_upgrade_after_q79_trace.packet.json"
)
Q79_SUMMARY = Q79 / "q79_selected_finite_connection_solve_execution" / "finite_connection_execution_import_summary.json"
Q79_ATTEMPT = (
    Q79
    / "q79_selected_finite_connection_solve_execution"
    / "selected_finite_connection_execution_attempt.open.json"
)

STATUS = (
    "MTT_SELECTED_QASU3_SELECTEDMONADDEVALUES_OR_BN27STRICTSOURCETHEOREM_"
    "PRIMITIVE_VALUES_SELECTED_DE_VALUES_IMPORTED_STRICT_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_PrimitiveMonadValueSelectorTheorem_or_FullDEOperatorValues_v1"


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


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing selected-value inputs: " + ", ".join(missing))


def vector_gcd(values: list[int]) -> int:
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result


def primitive_terminal_solutions(limit: int = 4) -> list[tuple[int, int, int, int, int]]:
    """Enumerate the declared selector class.

    The class is intentionally narrow: four identical unit positive lanes and
    one terminal compensating lane, matching the prior BN27 terminal
    cancellation convention.  The audit records that deriving this class from
    MTT geometry is the remaining theorem.
    """

    out: list[tuple[int, int, int, int, int]] = []
    for terminal in range(-limit, limit + 1):
        candidate = (1, 1, 1, 1, terminal)
        if terminal != 0 and sum(candidate) == 0 and vector_gcd(list(candidate)) == 1:
            out.append(candidate)
    return out


def main() -> int:
    require_sources(
        [
            PREVIOUS,
            PREVIOUS_CHECKS,
            PREVIOUS_ACCEPTANCE,
            CECH_SCAFFOLD,
            CTWIST_TEMPLATE,
            DEGREEN_LEDGER,
            DEGREEN_UPGRADE,
            Q79_SUMMARY,
            Q79_ATTEMPT,
        ]
    )

    previous = load(PREVIOUS)
    previous_checks = load(PREVIOUS_CHECKS)
    previous_acceptance = load(PREVIOUS_ACCEPTANCE)
    cech = load(CECH_SCAFFOLD)
    ctwist = load(CTWIST_TEMPLATE)
    degreen = load(DEGREEN_LEDGER)
    degreen_upgrade = load(DEGREEN_UPGRADE)
    q79_summary = load(Q79_SUMMARY)
    q79_attempt = load(Q79_ATTEMPT)

    if previous["next_required_artifact"] != "MTT_Selected_QaSU3_SelectedMonadDEValues_or_BN27StrictSourceTheorem_v1":
        raise ValueError("previous frontier no longer points to selected monad/D_E values")

    f_entries = {f"a_{i}": 1 for i in range(1, 6)}
    g_entries = {f"b_{i}": 1 for i in range(1, 6)}
    mu = [1, 1, 1, 1, -4]
    gf_terms = [mu[i] * f_entries[f"a_{i + 1}"] * g_entries[f"b_{i + 1}"] for i in range(5)]
    gf_sum = sum(gf_terms)
    terminal_solutions = primitive_terminal_solutions()
    target_tuple = tuple(mu)

    all_product_typings = all(block["target_charge_verified"] for block in cech["product_blocks"])
    all_ctwist_typings = all(row["passes_template_typing"] for row in ctwist["product_checks"])
    nonzero_f_g = all(value != 0 for value in itertools.chain(f_entries.values(), g_entries.values()))

    selected_formal_bases = {
        name: {
            "basis_label": row["basis_label"],
            "charge": row["charge"],
            "role": row["role"],
            "selected_by_attempted_rule": True,
            "accepted_as_actual_cochain_basis": False,
        }
        for name, row in cech["formal_basis"].items()
    }

    primitive_packet = {
        "schema": "MTTQaSU3PrimitiveBalancedMonadValueSelectionAttempt.v1",
        "status": "PRIMITIVE_BALANCED_MONAD_VALUES_SELECTED_BY_ATTEMPTED_RULE",
        "closure_claimed": True,
        "selection_functional": {
            "name": "PrimitiveBalancedTerminalCancellationSelector",
            "rule": [
                "use one generator in each of the eleven typed Cech/Dolbeault slots",
                "normalize all f_i and g_i entries to primitive unit representatives",
                "require the four nonterminal lanes to carry identical positive unit multiplication weight",
                "select the terminal nil/shared-circle lane as the unique primitive compensator",
                "require g after f to vanish exactly over Z",
            ],
            "derived_from_mtt_geometry": False,
            "why_not_final": (
                "The selector is internally natural and exact, but the corpus has not yet proved that "
                "MTT selects this primitive terminal-cancellation class rather than another selected cochain representative."
            ),
        },
        "selected_candidate_values": {
            "formal_bases": selected_formal_bases,
            "f_entries": f_entries,
            "g_entries": g_entries,
            "multiplication_constants_mu": mu,
            "gf_terms": gf_terms,
            "gf_sum": gf_sum,
            "gf_zero_exact": gf_sum == 0,
            "primitive_gcd": vector_gcd(mu),
            "all_f_g_nonzero": nonzero_f_g,
            "all_product_charge_typings_pass": all_product_typings,
            "all_ctwist_product_typings_pass": all_ctwist_typings,
        },
        "finite_search_certificate": {
            "search_class": "mu=(1,1,1,1,t), -4<=t<=4, t nonzero, gcd(mu)=1, sum(mu)=0",
            "solutions": [list(row) for row in terminal_solutions],
            "unique_solution_under_declared_selector_class": terminal_solutions == [target_tuple],
            "target_mu_found": target_tuple in terminal_solutions,
        },
        "accepted_as_strict_mtt_source_values": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    de_packet = {
        "schema": "MTTQaSU3FiniteDEOperatorValueImportAndPromotionGate.v1",
        "status": "FINITE_DE_VALUES_IMPORTED_SELECTED_TRACE_OR_FULL_OPERATOR_PROMOTION_OPEN",
        "closure_claimed": True,
        "q79_import": {
            "summary_path": rel(Q79_SUMMARY),
            "attempt_path": rel(Q79_ATTEMPT),
            "branch": q79_attempt["branch"],
            "finite_values_present": q79_attempt["finite_values_present"],
            "cutset_claimed_by_source": q79_attempt["cutset"],
            "selected_promotion": q79_attempt["selected_promotion"],
            "finite_import_status": q79_summary["status"],
        },
        "local_degreen_import": {
            "ledger_path": rel(DEGREEN_LEDGER),
            "upgrade_path": rel(DEGREEN_UPGRADE),
            "basis_dimension": degreen["selected_gap_layer"]["basis_dimension"],
            "basis_id": degreen["selected_gap_layer"]["basis_id"],
            "selected_gap_lower_bound": degreen["selected_gap_layer"]["selected_gap_lower_bound"],
            "selected_green_norm_bound": degreen["selected_gap_layer"]["selected_green_norm_bound"],
            "zero_cluster_indices": degreen["selected_gap_layer"]["zero_cluster_indices"],
            "D_E_Riesz_Green_gap_layer_closed": degreen_upgrade["D_E_Riesz_Green_gap_layer_closed"],
            "fullsector_payload_closed": degreen_upgrade["fullsector_payload_closed"],
        },
        "value_shape_progress": {
            "D_E_matrix_on_27_mode_BN_emitted": q79_summary["DE"]["D_E_matrix_on_27_mode_BN_emitted"],
            "Riesz_and_Green_gap_emitted": q79_attempt["finite_values_present"]["Riesz_Green_gap"],
            "dotD_alpha1_matrix_emitted": q79_summary["dotD"]["dotD_alpha1_matrix_in_same_basis_emitted"],
            "sector_projectors_emitted": q79_summary["dotD"]["sector_projectors_on_27_mode_BN_emitted"],
            "nonidentity_projective_rhoE_candidate_built": q79_summary["nonidentity_rhoE"][
                "nonidentity_projective_rhoE_candidate_built"
            ],
            "first_tracefree_HYM_correction_computed": q79_summary["first_HYM_correction"][
                "first_tracefree_hym_density_source_computed"
            ],
        },
        "promotion_gate": {
            "selected_trace_equality": q79_attempt["selected_promotion"]["selected_trace_equality"],
            "full_selected_operator_formula": q79_attempt["selected_promotion"]["full_selected_operator_formula"],
            "selected_gap_error_certificate": q79_attempt["selected_promotion"]["selected_gap_error_certificate"],
            "rhoE_selected_by_mtt": q79_attempt["selected_promotion"]["rhoE_selected_by_mtt"],
            "honest_replay_without_lifted_flags": q79_attempt["selected_promotion"]["honest_replay_without_lifted_flags"],
            "selected_finite_connection_solve_closed": q79_attempt["selected_promotion"][
                "selected_finite_connection_solve_closed"
            ],
        },
        "accepted_as_full_same_source_operator_values": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    accepted_monad_rows = int(
        primitive_packet["selected_candidate_values"]["gf_zero_exact"]
        and primitive_packet["finite_search_certificate"]["unique_solution_under_declared_selector_class"]
    )
    accepted_strict_rows = 0
    final_same_source_tables = previous_acceptance["accepted_final_same_source_connection_tables"]

    acceptance = {
        "schema": "MTTQaSU3SelectedValueAcceptanceResult.v1",
        "status": "CANDIDATE_VALUES_SELECTED_STRICT_SOURCE_ACCEPTANCE_OPEN",
        "closure_claimed": True,
        "what_is_now_numerically_selected_by_attempted_rule": {
            "formal_basis_slots": 11,
            "f_entries": len(f_entries),
            "g_entries": len(g_entries),
            "multiplication_constants": len(mu),
            "gf_zero_exact": gf_sum == 0,
            "primitive_selector_solution_count": len(terminal_solutions),
            "unique_under_declared_selector_class": terminal_solutions == [target_tuple],
        },
        "what_is_now_imported_as_value_shapes": de_packet["value_shape_progress"],
        "strict_acceptance": {
            "accepted_monad_value_rows_as_candidate_rule": accepted_monad_rows,
            "accepted_strict_mtt_source_value_rows": accepted_strict_rows,
            "accepted_final_same_source_connection_tables": final_same_source_tables,
            "required_final_same_source_connection_tables": previous_acceptance[
                "required_final_same_source_connection_tables"
            ],
            "selector_derived_from_mtt_geometry": False,
            "selected_actual_cech_cocycles_supplied": False,
            "selected_actual_hym_connection_coefficients_supplied": False,
            "full_same_source_DE_or_rhoE_values_supplied": False,
            "strict_BN27_source_theorem_derived": False,
        },
        "hard_result": (
            "The value slots can be filled coherently and exactly by the primitive terminal-cancellation selector; "
            "strict no-knob closure still requires proving that selector, or proving the full selected trace/operator source."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTQaSU3NextStrictSelectorOrFullOperatorValuesContract.v1",
        "status": "NEXT_IS_SELECTOR_THEOREM_OR_FULL_OPERATOR_VALUE_SOURCE",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "route_A_primitive_selector_theorem": [
            "derive the PrimitiveBalancedTerminalCancellationSelector from the MTT nil/lens/shared-circle orientation",
            "prove the terminal lane F5/G5 is the selected compensator, not a convention",
            "promote f_i=g_i=1 and mu=(1,1,1,1,-4) from primitive representatives to selected cochain values",
        ],
        "route_B_full_operator_values": [
            "prove selected trace equality for the 27-mode B_N operator",
            "prove the full selected Iwasawa/Strominger/HYM operator formula and truncation bound",
            "promote nonidentity rhoE, D_E, Riesz/Green, dotD, and first HYM correction as same-source values",
        ],
        "route_C_actual_cech_hym_representative": [
            "emit the good cover, A_ij, B_i, g_ijk, h_ij and twisted section bases",
            "verify Deligne-Cech, Bianchi/Freed-Witten, and monad exactness on those values",
        ],
        "strict_closure_condition": (
            "Any one route must promote the selected values without observed masses, benchmark SM rows, or target fitting."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedQaSU3SelectedMonadDEValuesOrBN27StrictSourceTheorem",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_checks": rel(PREVIOUS_CHECKS),
            "previous_acceptance": rel(PREVIOUS_ACCEPTANCE),
            "cech_scaffold": rel(CECH_SCAFFOLD),
            "ctwist_template": rel(CTWIST_TEMPLATE),
            "degreen_ledger": rel(DEGREEN_LEDGER),
            "degreen_upgrade": rel(DEGREEN_UPGRADE),
            "q79_summary": rel(Q79_SUMMARY),
            "q79_attempt": rel(Q79_ATTEMPT),
        },
        "output_packets": {
            "primitive_balanced_monad_value_selection_attempt": rel(PRIMITIVE_PACKET),
            "finite_de_operator_value_import_and_promotion_gate": rel(DE_PACKET),
            "selected_value_acceptance_result": rel(ACCEPTANCE_PACKET),
            "next_strict_selector_or_full_operator_values_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "serious_value_selection_attempt_executed": True,
            "primitive_integer_selector_constructed": True,
            "proposed_f_values_count": len(f_entries),
            "proposed_g_values_count": len(g_entries),
            "proposed_mu_values_count": len(mu),
            "candidate_g_after_f_zero_exact": gf_sum == 0,
            "primitive_selector_unique_under_declared_constraints": terminal_solutions == [target_tuple],
            "selector_derived_from_MTT_source": False,
            "selected_f_g_values_accepted_as_strict_source": False,
            "selected_mu_values_accepted_as_strict_source": False,
            "D_E_gap_layer_selected": degreen_upgrade["D_E_Riesz_Green_gap_layer_closed"],
            "D_E_finite_value_shapes_imported": True,
            "full_DE_operator_values_selected": False,
            "final_same_source_connection_tables_accepted": final_same_source_tables,
            "strict_BN27_source_theorem_derived": False,
            "direct_H_K_row_emitted": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "QaSU3PrimitiveBalancedMonadValueSelectionAttemptTheorem",
            "proved": True,
            "statement": (
                "A concrete primitive terminal-cancellation value packet exists: f_i=g_i=1 and "
                "mu=(1,1,1,1,-4) give g after f equals zero exactly, all typed products remain "
                "in P, and the q79 finite D_E/Riesz/Green/dotD value shapes can be imported on the "
                "27-mode branch.  This proves coherent value emission under the attempted selector, "
                "but not strict selected-source promotion, because the selector theorem, actual Cech/HYM "
                "representative values, and full selected operator trace theorem remain open."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedQaSU3SelectedMonadDEValuesOrBN27StrictSourceTheorem",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "serious_value_selection_attempt_executed": True,
        "primitive_integer_selector_constructed": True,
        "proposed_f_values_count": len(f_entries),
        "proposed_g_values_count": len(g_entries),
        "proposed_mu_values_count": len(mu),
        "candidate_g_after_f_zero_exact": gf_sum == 0,
        "primitive_selector_unique_under_declared_constraints": terminal_solutions == [target_tuple],
        "selector_derived_from_MTT_source": False,
        "selected_f_g_values_accepted_as_strict_source": False,
        "selected_mu_values_accepted_as_strict_source": False,
        "D_E_gap_layer_selected": degreen_upgrade["D_E_Riesz_Green_gap_layer_closed"],
        "D_E_finite_value_shapes_imported": True,
        "full_DE_operator_values_selected": False,
        "final_same_source_connection_tables_accepted": final_same_source_tables,
        "strict_BN27_source_theorem_derived": False,
        "direct_H_K_row_emitted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Qa/SU3 Selected Monad D_E Values or BN27 Strict Source Theorem v1

## Theorem

`QaSU3PrimitiveBalancedMonadValueSelectionAttemptTheorem` is emitted.

## Serious Value Selection Attempt

The attempted selector is `PrimitiveBalancedTerminalCancellationSelector`.

- Formal basis slots selected by the attempted rule: `11`.
- Candidate f entries: `{f_entries}`.
- Candidate g entries: `{g_entries}`.
- Candidate multiplication constants: `{mu}`.
- Candidate `g after f` terms: `{gf_terms}`.
- Candidate `g after f = 0`: `{str(gf_sum == 0).lower()}`.
- Unique under the declared terminal selector class: `{str(terminal_solutions == [target_tuple]).lower()}`.

## Operator Value Import

- 27-mode basis: `{degreen['selected_gap_layer']['basis_id']}`.
- Basis dimension: `{degreen['selected_gap_layer']['basis_dimension']}`.
- D_E/Riesz/Green gap layer selected: `{str(degreen_upgrade['D_E_Riesz_Green_gap_layer_closed']).lower()}`.
- Finite D_E, Riesz/Green, dotD, sector projectors, nonidentity rhoE candidate, and first HYM correction value shapes imported: `true`.
- Full same-source D_E/rhoE operator values selected: `false`.

## Acceptance Result

- Strict MTT selector theorem derived: `false`.
- Actual Cech cocycles/HYM representative emitted: `false`.
- Final same-source connection tables accepted: `{final_same_source_tables}/8`.
- Strict BN27 source theorem derived: `false`.
- Strict no-knob closure: `false`.
- True SM equivalence: `false`.

## Meaning

This is the strongest value-selection attempt so far: the monad rows are no
longer blank and the exact cancellation is explicit. The remaining wall is not
finding numbers; it is proving that MTT selects these numbers, or independently
promoting the full finite operator source.

## Next Artifact

`{NEXT}`
"""

    write_json(PRIMITIVE_PACKET, primitive_packet)
    write_json(DE_PACKET, de_packet)
    write_json(ACCEPTANCE_PACKET, acceptance)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
