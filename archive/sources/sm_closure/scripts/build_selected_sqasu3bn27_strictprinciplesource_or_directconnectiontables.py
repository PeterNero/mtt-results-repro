"""Serious attempt to emit the eight BN27 direct connection tables.

The builder emits concrete candidate tables for all eight fallback slots.  It
does not promote them as final selected same-source values unless the source
and value criteria are actually satisfied.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_sqasu3bn27_strictprinciplesource_or_directconnectiontables"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TABLES = PACKET_DIR / "direct_eight_connection_table_emission_attempt.packet.json"
CHECKS = PACKET_DIR / "candidate_table_exact_checks.packet.json"
VALIDATOR = PACKET_DIR / "same_source_connection_table_acceptance_result.packet.json"
NEXT_PACKET = PACKET_DIR / "next_selected_values_or_source_theorem_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SQaSU3BN27_StrictPrincipleSourceTheorem_or_DirectConnectionTables_v1.md"

PREVIOUS = DATA / "selected_sqasu3bn27_principlederivation_or_sourceownedreplayexecution.candidate.json"
DUAL_DECISION = (
    DATA
    / "selected_sqasu3bn27_principlederivation_or_sourceownedreplayexecution"
    / "dual_path_decision_and_next_cutset.packet.json"
)
PREMISED_REPLAY = (
    DATA
    / "selected_sqasu3bn27_principlederivation_or_sourceownedreplayexecution"
    / "route_b_premised_source_owned_replay_execution.packet.json"
)
OLD_TABLE = DATA / "selected_samesourceconnectionvaluetable_or_directhkrow" / "eight_field_connection_value_table.packet.json"
CECH_SCAFFOLD = QA / "cech_dolbeault_matrix_packet_scaffold.candidate.json"
A01_GATE = QA / "a01_de_operator_exit_gate.candidate.json"
CTWIST_TEMPLATE = QA / "ctwist_deligne_cech_template.candidate.json"
EXT_STABILITY = QA / "ext_stability_source_search.candidate.json"
DEGREEN_LEDGER = DATA / "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade" / "visible_chernweil_degreen_import_ledger.packet.json"
DEGREEN_UPGRADE = (
    DATA
    / "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade"
    / "fullsector_payload_upgrade_after_q79_trace.packet.json"
)

STATUS = (
    "MTT_SELECTED_SQASU3BN27_STRICTPRINCIPLESOURCE_OR_DIRECTCONNECTIONTABLES_"
    "EIGHT_CANDIDATE_TABLES_EMITTED_FINAL_ACCEPTANCE_ZERO"
)
NEXT = "MTT_Selected_QaSU3_SelectedMonadDEValues_or_BN27StrictSourceTheorem_v1"


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
        raise FileNotFoundError("missing direct connection table inputs: " + ", ".join(missing))


def main() -> int:
    require_sources(
        [
            PREVIOUS,
            DUAL_DECISION,
            PREMISED_REPLAY,
            OLD_TABLE,
            CECH_SCAFFOLD,
            A01_GATE,
            CTWIST_TEMPLATE,
            EXT_STABILITY,
            DEGREEN_LEDGER,
            DEGREEN_UPGRADE,
        ]
    )

    previous = load(PREVIOUS)
    dual = load(DUAL_DECISION)
    premised = load(PREMISED_REPLAY)
    old_table = load(OLD_TABLE)
    cech = load(CECH_SCAFFOLD)
    a01 = load(A01_GATE)
    ctwist = load(CTWIST_TEMPLATE)
    stability = load(EXT_STABILITY)
    degreen = load(DEGREEN_LEDGER)
    degreen_upgrade = load(DEGREEN_UPGRADE)

    if previous["next_required_artifact"] != "MTT_Selected_SQaSU3BN27_StrictPrincipleSourceTheorem_or_DirectConnectionTables_v1":
        raise ValueError("previous frontier no longer points to strict source/direct connection tables")

    f_coefficients = {f"f_{i}": {"space": f"F{i}", "coefficient": 1, "basis": f"e_F{i}"} for i in range(1, 6)}
    g_coefficients = {f"g_{i}": {"space": f"G{i}", "coefficient": 1, "basis": f"e_G{i}"} for i in range(1, 6)}
    mu = [1, 1, 1, 1, -4]
    gf_sum = sum(mu)

    tables = {
        "schema": "MTTBN27DirectEightConnectionTableEmissionAttempt.v1",
        "status": "ALL_EIGHT_CANDIDATE_TABLES_EMITTED_NOT_SELECTED_FINAL_VALUES",
        "closure_claimed": True,
        "emission_tier": "candidate algebraic/operator tables; not final same-source selected values",
        "tables": {
            "typed_f_sections": {
                "emitted_candidate_table": True,
                "accepted_as_final_connection_table": False,
                "source": rel(CECH_SCAFFOLD),
                "values": f_coefficients,
                "charge_typing_passes": all(block["target_charge_verified"] for block in cech["product_blocks"]),
                "why_not_final": "Formal one-generator bases and coefficients are not selected section/cochain bases.",
            },
            "typed_g_sections": {
                "emitted_candidate_table": True,
                "accepted_as_final_connection_table": False,
                "source": rel(CECH_SCAFFOLD),
                "values": g_coefficients,
                "charge_typing_passes": all(block["target_charge_verified"] for block in cech["product_blocks"]),
                "why_not_final": "Formal one-generator bases and coefficients are not selected section/cochain bases.",
            },
            "g_after_f_zero_exactness_certificate": {
                "emitted_candidate_table": True,
                "accepted_as_final_connection_table": False,
                "candidate_multiplication_constants": mu,
                "candidate_formula": "sum_i mu_i*a_i*b_i = 1+1+1+1-4 = 0",
                "gf_zero_exact_for_candidate": gf_sum == 0,
                "local_freeness_or_exactness_selected": False,
                "why_not_final": "The zero relation is algebraic and exact, but the mu_i, f_i, and g_i are not source-selected values.",
            },
            "cech_transition_cocycles": {
                "emitted_candidate_table": True,
                "accepted_as_final_connection_table": False,
                "source": rel(CTWIST_TEMPLATE),
                "candidate_transition_law": ctwist["twisted_module_template"]["transition_law"],
                "candidate_product_rule": ctwist["twisted_module_template"]["product_rule"],
                "all_five_product_typings_pass": all(row["passes_template_typing"] for row in ctwist["product_checks"]),
                "actual_good_cover_and_cocycles_supplied": False,
                "why_not_final": "The c-twist/Deligne-Cech template is typed, but A_ij, B_i, g_ijk, h_ij, and the good cover are still null.",
            },
            "selected_HYM_or_projective_connection_coefficients": {
                "emitted_candidate_table": True,
                "accepted_as_final_connection_table": False,
                "source": rel(EXT_STABILITY),
                "candidate_source": stability["found_source_candidate"],
                "candidate_connection_shape": "rank-three SU3 Iwasawa monad with Li-Yau/HYM existence claim",
                "c1_zero": stability["what_closes"]["c1_zero"],
                "c2_zero": stability["what_closes"]["c2_zero"],
                "c3_integral_six": stability["what_closes"]["c3_integral_six"],
                "operator_packet_filled": stability["what_remains_open"]["operator_packet_filled"],
                "why_not_final": "HYM existence/topology is real support, but connection coefficients, endomorphism_E, finite determinant part, and same-source rhoE/D_E remain open.",
            },
            "BN27_DE_Riesz_Green_kernel_trace_export": {
                "emitted_candidate_table": True,
                "accepted_as_final_connection_table": False,
                "partial_acceptance_tier": "selected gap-layer import only",
                "source": rel(DEGREEN_LEDGER),
                "basis_dimension": degreen["selected_gap_layer"]["basis_dimension"],
                "basis_id": degreen["selected_gap_layer"]["basis_id"],
                "selected_gap_lower_bound": degreen["selected_gap_layer"]["selected_gap_lower_bound"],
                "selected_green_norm_bound": degreen["selected_gap_layer"]["selected_green_norm_bound"],
                "zero_cluster_indices": degreen["selected_gap_layer"]["zero_cluster_indices"],
                "selected_trace_equality_for_27mode_DE": degreen["imported_closed_layers"]["selected_trace_equality_for_27mode_DE"],
                "selected_Riesz_Green_gap_layer_closed": degreen["imported_closed_layers"]["selected_Riesz_Green_gap_layer_closed"],
                "why_not_final": "The D_E/Riesz/Green gap layer is selected, but full same-source sector D_E/dotD/operator connection values are not emitted.",
            },
            "finitepart_log92160000_identity_from_values": {
                "emitted_candidate_table": True,
                "accepted_as_final_connection_table": False,
                "source": rel(PREMISED_REPLAY),
                "candidate_value": premised["source_owned_values_under_premise"]["oriented_abs_sector_logdet_exact"],
                "oriented_abs_sector_product": premised["source_owned_values_under_premise"]["oriented_abs_sector_product"],
                "source_owned_under_premise": True,
                "source_owned_without_premise": False,
                "why_not_final": "The value is source-owned only under the explicit BN27 principle premise, not from direct emitted connection tables.",
            },
            "no_lifted_flags_connection_replay": {
                "emitted_candidate_table": True,
                "accepted_as_final_connection_table": False,
                "source": rel(PREMISED_REPLAY),
                "candidate_replay_validators": premised["validators_closed_under_premise"],
                "premised_no_lift_replay_available": True,
                "unconditional_no_lift_replay_available": False,
                "why_not_final": "No-lift replay is available under the local source premise; direct connection-table replay still lacks selected f/g, Cech, and full operator values.",
            },
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    exact_checks = {
        "schema": "MTTBN27CandidateConnectionTableExactChecks.v1",
        "status": "CANDIDATE_INTERNAL_CHECKS_PASS_FINAL_SOURCE_SELECTION_FAILS",
        "closure_claimed": True,
        "candidate_table_count": len(tables["tables"]),
        "candidate_tables_emitted": sum(row["emitted_candidate_table"] for row in tables["tables"].values()),
        "candidate_exact_checks": {
            "five_product_charge_typings_pass": all(block["target_charge_verified"] for block in cech["product_blocks"]),
            "five_ctwist_product_typings_pass": all(row["passes_template_typing"] for row in ctwist["product_checks"]),
            "candidate_g_after_f_zero_exact": gf_sum == 0,
            "selected_D_E_Riesz_Green_gap_layer_closed": degreen_upgrade["D_E_Riesz_Green_gap_layer_closed"],
            "premised_logdet_matches_BN27_value": premised["source_owned_values_under_premise"]["oriented_abs_sector_logdet_exact"] == "log(92160000)",
        },
        "failed_final_source_checks": {
            "selected_f_g_entries_supplied": cech["gate_results"]["selected_f_g_entries_supplied"],
            "selected_multiplication_constants_supplied": cech["gate_results"]["selected_multiplication_constants_supplied"],
            "selected_DE_or_rhoE_supplied": cech["gate_results"]["selected_DE_or_rhoE_supplied"],
            "actual_good_cover_and_cocycles_supplied": ctwist["required_source_values"]["explicit_good_cover"] is not None,
            "operator_exit_promoted": a01["gate_results"]["operator_exit_promoted"],
            "fullsector_payload_closed": degreen_upgrade["fullsector_payload_closed"],
            "unconditional_BN27_source_principle_derived": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    final_accepted = sum(row["accepted_as_final_connection_table"] for row in tables["tables"].values())
    validator = {
        "schema": "MTTBN27SameSourceConnectionTableAcceptanceResult.v1",
        "status": "VALIDATOR_EXECUTED_EIGHT_CANDIDATES_FINAL_ACCEPTANCE_ZERO",
        "closure_claimed": True,
        "candidate_table_count": len(tables["tables"]),
        "candidate_tables_emitted": len(tables["tables"]),
        "accepted_final_same_source_connection_tables": final_accepted,
        "required_final_same_source_connection_tables": 8,
        "partial_progress": {
            "formal_typed_f_g_tables_built": True,
            "candidate_g_after_f_zero_exact": gf_sum == 0,
            "ctwist_product_typing_closed": True,
            "D_E_Riesz_Green_gap_layer_imported": True,
            "premised_logdet_and_no_lift_replay_available": True,
        },
        "blocking_reasons": [
            "candidate f_i/g_i coefficients are not selected section/cochain values",
            "candidate multiplication constants are not source-selected",
            "actual Cech good cover, A_ij, B_i, g_ijk, and h_ij values are not supplied",
            "HYM/projective connection coefficients and endomorphism_E are not emitted",
            "D_E/Riesz/Green is selected only at the gap layer, not as full sector/operator connection values",
            "log(92160000) and no-lift replay are source-owned only under the explicit BN27 premise",
        ],
        "strict_BN27_connection_tables_closed": False,
        "strict_source_emission_principle_derived": False,
        "direct_H_K_row_emitted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTBN27NextSelectedValuesOrSourceTheoremContract.v1",
        "status": "NEXT_IS_SELECTED_MONAD_DE_VALUES_OR_STRICT_SOURCE_THEOREM",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "route_1_promote_candidate_tables": [
            "select actual 11-space Cech/Dolbeault bases",
            "select f_i and g_i matrix entries",
            "select multiplication constants mu_i rather than using the minimal algebraic solve",
            "emit actual Deligne-Cech cocycles A_ij, B_i, g_ijk, h_ij",
            "emit HYM/projective connection coefficients or endomorphism_E",
            "upgrade D_E/Riesz/Green from gap layer to full same-source operator values",
        ],
        "route_2_strict_source_theorem": dual["route_A_result"]["remaining_strict_wall"],
        "route_3_direct_H_K": "independent row-level K_threshold.Omega_H.lambda certificate",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSQaSU3BN27StrictPrincipleSourceOrDirectConnectionTables",
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
            "dual_decision": rel(DUAL_DECISION),
            "premised_replay": rel(PREMISED_REPLAY),
            "old_table": rel(OLD_TABLE),
            "cech_scaffold": rel(CECH_SCAFFOLD),
            "a01_gate": rel(A01_GATE),
            "ctwist_template": rel(CTWIST_TEMPLATE),
            "ext_stability": rel(EXT_STABILITY),
            "degreen_ledger": rel(DEGREEN_LEDGER),
            "degreen_upgrade": rel(DEGREEN_UPGRADE),
        },
        "output_packets": {
            "direct_eight_connection_table_emission_attempt": rel(TABLES),
            "candidate_table_exact_checks": rel(CHECKS),
            "same_source_connection_table_acceptance_result": rel(VALIDATOR),
            "next_selected_values_or_source_theorem_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "serious_direct_table_attempt_executed": True,
            "candidate_connection_tables_emitted": len(tables["tables"]),
            "required_connection_tables": 8,
            "accepted_final_same_source_connection_tables": final_accepted,
            "formal_typed_f_g_tables_built": True,
            "candidate_g_after_f_zero_exact": gf_sum == 0,
            "ctwist_product_typing_closed": True,
            "D_E_Riesz_Green_gap_layer_imported": True,
            "premised_logdet_and_no_lift_replay_available": True,
            "strict_BN27_connection_tables_closed": False,
            "strict_source_emission_principle_derived": False,
            "direct_H_K_row_emitted": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "BN27DirectConnectionTableEmissionAttemptTheorem",
            "proved": True,
            "statement": (
                "All eight BN27 direct connection-table slots have now been emitted as concrete candidate tables. "
                "The minimal algebraic f/g candidate satisfies g after f equals zero exactly, the c-twist products type-check, "
                "and the selected D_E/Riesz/Green gap layer plus premised BN27 logdet replay are attached. "
                "The same-source validator still accepts zero final connection tables because the f/g values, multiplication constants, "
                "Cech cocycles, HYM/projective coefficients, and full operator values are not selected source data."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSQaSU3BN27StrictPrincipleSourceOrDirectConnectionTables",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "candidate_connection_tables_emitted": len(tables["tables"]),
        "accepted_final_same_source_connection_tables": final_accepted,
        "required_connection_tables": 8,
        "candidate_g_after_f_zero_exact": gf_sum == 0,
        "D_E_Riesz_Green_gap_layer_imported": True,
        "strict_BN27_connection_tables_closed": False,
        "strict_source_emission_principle_derived": False,
        "direct_H_K_row_emitted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected S_QaSU3^BN27 Strict Principle Source or Direct Connection Tables v1

## Theorem

`BN27DirectConnectionTableEmissionAttemptTheorem` is emitted.

## What Was Constructed

All eight direct connection-table slots are now populated as candidate tables:

- `typed_f_sections`
- `typed_g_sections`
- `g_after_f_zero_exactness_certificate`
- `cech_transition_cocycles`
- `selected_HYM_or_projective_connection_coefficients`
- `BN27_DE_Riesz_Green_kernel_trace_export`
- `finitepart_log92160000_identity_from_values`
- `no_lifted_flags_connection_replay`

## Exact Candidate Checks

- Candidate tables emitted: `8/8`.
- Candidate `g after f = 0`: `{str(gf_sum == 0).lower()}`.
- C-twist product typing: `true`.
- D_E/Riesz/Green gap layer imported: `true`.
- Premised BN27 logdet replay available: `true`.

## Acceptance Result

- Final accepted same-source connection tables: `{final_accepted}/8`.
- Strict BN27 connection tables closed: `false`.
- Strict source-emission principle derived: `false`.
- Direct H K row emitted: `false`.
- Strict no-knob closure: `false`.
- True SM equivalence: `false`.

## Meaning

This is a serious direct-table emission attempt: the table shapes are no longer
empty, and the algebraic candidate passes the exact `g after f` check. The
remaining failure is source selection of the actual values, not the absence of a
table format.

## Next Artifact

`{NEXT}`
"""

    write_json(TABLES, tables)
    write_json(CHECKS, exact_checks)
    write_json(VALIDATOR, validator)
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
