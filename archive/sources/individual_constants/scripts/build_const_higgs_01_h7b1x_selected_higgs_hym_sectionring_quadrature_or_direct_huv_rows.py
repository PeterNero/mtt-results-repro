"""Build CONST-HIGGS-01 H7B1X Higgs section-ring/quadrature or direct-Huv gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPRO = TEXPAPERS / "mtt-q79-proof-repro"
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

SLUG = "const_higgs_01_h7b1x_selected_higgs_hym_sectionring_quadrature_or_direct_huv_rows"
STATUS = "MTT_CONST_HIGGS_01_H7B1X_ORDERED_HIGGS_CHANNEL_LABELS_FILLED_OPERATOR_QUADRATURE_OPEN"
ACTIVE_LABEL = "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1X-SELECTED-HIGGS-HYM-SECTION-RING-QUADRATURE-OR-DIRECT-HUV-ROWS"
NEXT_ARTIFACT = "MTT_CONST_HIGGS_01_H7B1Y_SelectedEHUvSectionBasisQuadratureOrHerm2RowValues_v1"
NEXT_LABEL = "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1Y-SELECTED-EHUV-SECTION-BASIS-QUADRATURE-OR-HERM2-ROW-VALUES"

OUT_DIR = ROOT / "candidate_data" / SLUG
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1X_SelectedHiggsHYMSectionRingQuadratureOrDirectHuvRows_v1.md"

INPUTS = {
    "H7B1T": ROOT / "candidate_data" / "const_higgs_01_h7b1t_uv_higgs_plane_binding_or_minimal_lift_theorem.candidate.json",
    "H7B1W": ROOT / "candidate_data" / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload.candidate.json",
    "H7B1W_trace_attempt": ROOT
    / "candidate_data"
    / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
    / "finite_trace_binding_attempt.packet.json",
    "H7B1W_direct_attempt": ROOT
    / "candidate_data"
    / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
    / "direct_huv_payload_attempt.packet.json",
    "q79_single_higgs_projection": Q79_REPRO / "certificates" / "single_higgs_channel_projection_certificate.json",
    "q79_e6_yukawa_dictionary": Q79_REPRO / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json",
    "qa_terminal_baseorder_slotmap": QA_SU3
    / "candidate_data"
    / "selected_u1y_routec_terminalmonad_baseorder_ahbinding_smslotmap.candidate.json",
    "qa_terminal_orientation_bridge": QA_SU3
    / "candidate_data"
    / "selected_u1y_routec_terminal_orientation_branchcoherence_bridge.candidate.json",
    "sm_primitive_kernel_slot_coverage": SM_PARITY
    / "candidate_data"
    / "selected_primitivekernelslotcoverage_or_variationhessiangap.candidate.json",
}


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def guarded(schema: str, status: str, label: str, payload: dict[str, object]) -> dict[str, object]:
    return {
        "schema": schema,
        "status": status,
        "active_label": label,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        **payload,
    }


def write_note(payload: dict[str, object]) -> None:
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    NOTE.write_text(
        f"""# MTT CONST HIGGS 01 H7B1X Selected Higgs HYM Section Ring Quadrature Or Direct Huv Rows v1

Status: `{payload["status"]}`

Label: `{payload["active_label"]}`

## Result

```text
ordered Hu/Hd channel scaffold closed        {payload["ordered_Hu_Hd_channel_scaffold_closed"]}
E_H^UV exact sequence scaffold closed        {payload["E_H_UV_exact_sequence_scaffold_closed"]}
selected E_H^UV finite section basis emitted {payload["selected_E_H_UV_section_basis_emitted"]}
selected HYM metric/connection emitted       {payload["selected_HYM_metric_or_connection_emitted"]}
quadrature weights emitted                   {payload["quadrature_weights_emitted"]}
trace-to-H7B1U grid identity emitted         {payload["trace_to_H7B1U_grid_identity_emitted"]}
direct Herm2 Huv payload emitted             {payload["direct_Herm2_Huv_payload_emitted"]}
s_beta / lambda_H promoted                   {payload["selected_s_beta_value_found"]}
new Higgs-specific parameters                {payload["new_Higgs_specific_parameters"]}
```

## What Changed

H7B1X imports the terminal section-ring/base-order/AH-binding result from the
Qa/SU3 branch, the q79 E6/SU5 Yukawa dictionary, the single-Higgs projection,
and the H7B1T UV Higgs exact-sequence scaffold.  This fills the ordered
channel-label part of the Higgs plane:

```text
5_H    -> H_u       -> H
bar5_H -> H_d       -> H^dagger
E_H^UV = span(H_u, H_d^dagger)
q(H_u)=q(H_d^dagger)=H
```

The fill is intentionally scoped.  It is an ordered source-label/channel
scaffold, not an emitted finite operator basis, HYM metric, quadrature rule,
projection measure, or Herm(2) row payload.

## Remaining Boundary

The next object is:

`SelectedEHUvSectionBasisQuadratureOrHerm2RowValues`

It must emit either the actual finite `E_H^UV` section basis plus selected HYM
metric/quadrature/trace-to-grid certificate, or direct `B_Huv+M_source` /
`Huu,Hud,Hdd` rows.

Next label:

`{NEXT_LABEL}`
""",
        encoding="utf-8",
    )


def main() -> int:
    h7b1t = load_json(INPUTS["H7B1T"])
    h7b1w = load_json(INPUTS["H7B1W"])
    h7b1w_trace = load_json(INPUTS["H7B1W_trace_attempt"])
    h7b1w_direct = load_json(INPUTS["H7B1W_direct_attempt"])
    single_higgs = load_json(INPUTS["q79_single_higgs_projection"])
    e6 = load_json(INPUTS["q79_e6_yukawa_dictionary"])
    qa_slotmap = load_json(INPUTS["qa_terminal_baseorder_slotmap"])
    qa_orientation = load_json(INPUTS["qa_terminal_orientation_bridge"])
    primitive_slot = load_json(INPUTS["sm_primitive_kernel_slot_coverage"])

    ordered_higgs_labels = guarded(
        "MTTConstHiggs01H7B1XOrderedHiggsChannelLabelImport.v1",
        "ORDERED_HIGGS_CHANNEL_LABEL_SCAFFOLD_FILLED_OPERATOR_LAYER_OPEN",
        f"{ACTIVE_LABEL} / ORDERED-HIGGS-LABELS",
        {
            "input_sources": {name: rel(path) for name, path in INPUTS.items()},
            "closed_support": {
                "H7B1T_E_H_UV_exact_sequence": h7b1t["formal_UV_exact_sequence_scaffold_closed"],
                "H7B1T_conditional_minimal_lift_formula": h7b1t["conditional_G_minimal_lift_formula_proved"],
                "q79_single_higgs_channel_projection": single_higgs["closed"]["single_higgs_channel_projection"],
                "q79_low_energy_higgs_doublet_embedding": single_higgs["closed"]["low_energy_higgs_doublet_embedding"],
                "E6_SM_yukawa_operator_forms": e6["closed"]["sm_yukawa_operator_forms"],
                "qa_terminal_lane_selected_at_ordered_source_layer_under_explicit_principle": qa_slotmap[
                    "decision"
                ]["terminal_lane_selected_at_ordered_source_layer_under_explicit_principle"],
                "qa_AH_goodcover_binding_selected_at_ordered_source_layer": qa_slotmap["decision"][
                    "AH_or_Cech_transition_binding_selected_at_ordered_source_layer"
                ],
                "qa_slot_map_support_complete": qa_slotmap["decision"]["slot_map_support_complete"],
                "Hdagger_conjugate_basis_policy": primitive_slot["what_closes_now"]["Hdagger_conjugate_basis_policy"],
            },
            "ordered_channel_map": {
                "up": e6["representation_dictionary"]["operator_channels"]["up"],
                "down": e6["representation_dictionary"]["operator_channels"]["down"],
                "charged_lepton": e6["representation_dictionary"]["operator_channels"]["charged_lepton"],
                "dirac_neutrino": e6["representation_dictionary"]["operator_channels"]["dirac_neutrino"],
                "low_energy_projection": single_higgs["higgs_doublet_embedding"],
                "E_H_UV_basis_labels": ["H_u", "H_d^dagger"],
                "quotient": {
                    "q_Hu": "H",
                    "q_Hd_dagger": "H",
                    "kernel": "span(H_u-H_d^dagger)",
                },
            },
            "scope_guardrail": {
                "ordered_source_label_layer_only": True,
                "principle_unconditional_in_mtt_axioms": qa_slotmap["baseorder_binding"][
                    "principle_unconditional_in_mtt_axioms"
                ],
                "same_branch_selected_operator_emission": qa_slotmap["slot_map"]["same_branch_complete"],
                "operator_layer_Pic0_closed": qa_slotmap["decision"]["operator_layer_Pic0_closed"],
                "selected_overlap_normalization_emitted": qa_slotmap["decision"][
                    "selected_overlap_normalization_emitted"
                ],
            },
            "decision": {
                "ordered_Hu_Hd_channel_scaffold_closed": True,
                "E_H_UV_exact_sequence_scaffold_closed": True,
                "selected_E_H_UV_section_basis_emitted": False,
                "selected_HYM_metric_or_connection_emitted": False,
                "quadrature_weights_emitted": False,
                "trace_to_H7B1U_grid_identity_emitted": False,
                "selected_s_beta_promoted": False,
            },
        },
    )

    validator = guarded(
        "MTTConstHiggs01H7B1XBridgeValidatorReplay.v1",
        "HIGGS_HYM_QUADRATURE_BRIDGE_VALIDATOR_FIRST_CLAUSE_FILLED_REST_OPEN",
        f"{ACTIVE_LABEL} / BRIDGE-VALIDATOR",
        {
            "validator_name": "SelectedHiggsHYMSectionRingQuadratureBridgeValidator",
            "clauses": {
                "C1_branch_and_ordered_channel_labels": {
                    "closed": True,
                    "evidence": [
                        "H7B1T E_H^UV exact sequence",
                        "q79 single-Higgs projection",
                        "E6/SU5 operator dictionary",
                        "QA/SU3 ordered terminal source-layer slot map support",
                    ],
                },
                "C2_typed_E_H_UV_section_basis_or_finite_quotient": {
                    "closed": False,
                    "required": "typed sections or finite quotient basis for H^0(X,E_H^UV tensor L^k)",
                },
                "C3_selected_HYM_metric_or_connection_fixed_point": {
                    "closed": False,
                    "required": "selected HYM/balanced metric or full connection on the E_H^UV basis",
                },
                "C4_quadrature_weights_and_trace_normalization": {
                    "closed": False,
                    "required": "finite weights and trace normalization attached to the selected basis",
                },
                "C5_trace_to_H7B1U_grid_and_projection_measure_identity": {
                    "closed": False,
                    "required": "identity between H7B1U diagonal HYM grid and selected Higgs projection measure",
                },
                "C6_no_extra_boundary_or_source_term": {
                    "closed": False,
                    "required": "same-source boundary/source cancellation for the Higgs reduction",
                },
                "B_direct_Herm2_Huv_rows": {
                    "closed": False,
                    "required": "B_Huv+M_source or direct Huu,Hud,Hdd with exactness/residual certificate",
                },
            },
            "decision": {
                "first_clause_filled": True,
                "bridge_validator_complete": False,
                "uniform_mean_can_be_promoted_now": False,
                "direct_Herm2_Huv_payload_emitted": False,
                "selected_s_beta_promoted": False,
            },
        },
    )

    section_basis_request = guarded(
        "MTTConstHiggs01H7B1XSectionBasisQuadraturePayloadRequest.v1",
        "E_H_UV_SECTION_BASIS_QUADRATURE_PAYLOAD_REQUEST_SHARPENED",
        f"{ACTIVE_LABEL} / SECTION-BASIS-QUADRATURE-REQUEST",
        {
            "filled_now": {
                "ordered_Hu_Hd_channel_scaffold": True,
                "E_H_UV_exact_sequence_scaffold": True,
                "terminal_source_layer_AH_binding_support": True,
                "Hdagger_conjugate_basis_policy": True,
            },
            "must_emit_next": {
                "E_H_UV_typed_sections_or_finite_basis": None,
                "selected_HYM_metric_or_connection_on_E_H_UV": None,
                "quadrature_weights": None,
                "trace_normalization": None,
                "trace_to_H7B1U_grid_identity": None,
                "Higgs_projection_measure_equality": None,
                "no_extra_boundary_source_term": None,
            },
            "forbidden_promotions": [
                "do not treat ordered Hu/Hd labels as finite basis vectors",
                "do not treat QA/SU3 ordered source-layer support as operator-layer metric data",
                "do not treat the H7B1U uniform mean as selected s_beta without C2-C6",
                "do not use measured Higgs mass, v, tan beta, or lambda_H as selectors",
            ],
            "decision": {
                "payload_request_complete": True,
                "selected_E_H_UV_section_basis_emitted": False,
                "quadrature_weights_emitted": False,
                "trace_to_H7B1U_grid_identity_emitted": False,
            },
        },
    )

    direct_rows = guarded(
        "MTTConstHiggs01H7B1XDirectHerm2HuvRowsSearch.v1",
        "DIRECT_HERM2_HUV_ROWS_SEARCHED_VALUES_ABSENT_AFTER_LABEL_FILL",
        f"{ACTIVE_LABEL} / DIRECT-HUV-ROWS",
        {
            "imported_H7B1W_direct_attempt_status": h7b1w_direct["status"],
            "actual_outputs": {
                "B_Huv": None,
                "M_source": None,
                "Huu": None,
                "Hud": None,
                "Hdd": None,
                "Delta": None,
                "Omega": None,
                "P_L": None,
                "s_beta": None,
                "lambda_H": None,
            },
            "decision": {
                "direct_Herm2_Huv_payload_emitted": False,
                "B_Huv_value_emitted": False,
                "M_source_value_emitted": False,
                "direct_Huu_Hud_Hdd_emitted": False,
                "selected_s_beta_promoted": False,
                "numeric_lambda_H_derived": False,
            },
        },
    )

    no_cycle = guarded(
        "MTTConstHiggs01H7B1XNonCirculationLedger.v1",
        "NO_CIRCULATION_LEDGER_UPDATED_H7B1X",
        f"{ACTIVE_LABEL} / NO-CYCLE",
        {
            "new_information_added": [
                "ordered Hu/Hd channel scaffold imported from q79 single-Higgs, E6/SU5 dictionary, H7B1T, and QA/SU3 terminal source-layer support",
                "H7B1W bridge criterion first clause is filled while C2-C6 remain open",
                "section-basis/quadrature payload request is now exact and minimal",
                "direct Herm2 Huv row search remains value-absent after label fill",
            ],
            "retired_or_do_not_reopen": {
                "Higgs_channel_label_identity_as_blocker": True,
                "ordered_Hu_Hd_labels_as_metric_or_quadrature_values": True,
                "uniform_H7B1U_mean_as_selected_s_beta_without_C2_to_C6": True,
                "abstract_HYM_or_terminal_source_support_as_direct_Huv_rows": True,
            },
            "active_not_retired": {
                "typed_E_H_UV_section_basis_or_finite_quotient": True,
                "selected_HYM_metric_or_connection_on_E_H_UV": True,
                "quadrature_weights_and_trace_to_grid_identity": True,
                "direct_B_Huv_M_source_or_Huu_Hud_Hdd_rows": True,
            },
            "circulation_test": {
                "is_reopening_H7B1T_sequence": False,
                "is_reopening_H7B1W_bridge_criterion": False,
                "is_promoting_label_scaffold_as_operator_payload": False,
                "is_using_measured_Higgs_or_beta": False,
            },
        },
    )

    next_work = guarded(
        "MTTConstHiggs01H7B1XNextWork.v1",
        "NEXT_WORKORDER_H7B1Y_SELECTED_EHUV_SECTION_BASIS_QUADRATURE_OR_HERM2_ROW_VALUES",
        f"{ACTIVE_LABEL} / NEXT",
        {
            "primary_next": {
                "label": NEXT_LABEL,
                "task": "Emit the actual selected E_H^UV finite section basis plus HYM metric/quadrature/trace-to-grid identity, or direct Herm2 Huv rows.",
            },
            "legal_exits": [
                {
                    "id": "H7B1Y-A",
                    "label": "E_H^UV section-basis plus quadrature payload",
                    "must_emit": "typed E_H^UV sections or finite quotient basis, selected HYM metric/connection, quadrature weights, trace normalization, trace-to-H7B1U-grid identity, and projection-measure equality",
                },
                {
                    "id": "H7B1Y-B",
                    "label": "direct Herm2 Huv row payload",
                    "must_emit": "B_Huv+M_source or Huu,Hud,Hdd with exactness/residual and quotient-admissibility certificates",
                },
            ],
            "superset_strategy": {
                "combining_paths": True,
                "using_one_straight_way": False,
                "straight_path": "terminal section-ring ordered labels plus selected HYM section-basis/quadrature emission",
                "support_path": "direct Herm2 Huv rows remain independent exit",
                "locked_target": "source-selected Higgs projection payload, not fitted lambda_H or tan beta",
            },
        },
    )

    candidate = {
        "candidate": "MTTConstHiggs01H7B1XSelectedHiggsHYMSectionRingQuadratureOrDirectHuvRows",
        "status": STATUS,
        "active_label": ACTIVE_LABEL,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "theorem": {
            "name": "H7B1XOrderedHiggsChannelScaffoldTheorem",
            "proved": True,
            "statement": (
                "H7B1X fills the ordered Higgs channel-label part of the H7B1W bridge. "
                "Using H7B1T, q79 single-Higgs projection, the E6/SU5 Yukawa dictionary, "
                "SM primitive slot typing, and QA/SU3 terminal source-layer support, the "
                "branch now has E_H^UV=span(H_u,H_d^dagger) with the correct low-energy "
                "H/H^dagger projection and ordered channel roles. This is not an operator "
                "or quadrature payload: selected E_H^UV sections, HYM metric/connection, "
                "quadrature weights, trace-to-grid identity, projection-measure equality, "
                "and direct Herm2 rows remain open."
            ),
        },
        "H7B1W_imported": True,
        "H7B1T_imported": True,
        "q79_single_higgs_projection_imported": True,
        "q79_E6_SU5_dictionary_imported": True,
        "qa_terminal_ordered_source_layer_imported": True,
        "sm_Hdagger_conjugate_basis_policy_imported": True,
        "ordered_Hu_Hd_channel_scaffold_closed": True,
        "E_H_UV_exact_sequence_scaffold_closed": True,
        "bridge_validator_first_clause_filled": True,
        "selected_E_H_UV_section_basis_emitted": False,
        "selected_HYM_metric_or_connection_emitted": False,
        "quadrature_weights_emitted": False,
        "trace_to_H7B1U_grid_identity_emitted": False,
        "Higgs_projection_measure_equality_emitted": False,
        "same_source_no_extra_boundary_source_proof_emitted": False,
        "same_branch_selected_operator_emission": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": NEXT_ARTIFACT,
        "output_packets": {
            "ordered_higgs_channel_label_import": rel(OUT_DIR / "ordered_higgs_channel_label_import.packet.json"),
            "bridge_validator_replay": rel(OUT_DIR / "bridge_validator_replay.packet.json"),
            "section_basis_quadrature_payload_request": rel(
                OUT_DIR / "section_basis_quadrature_payload_request.packet.json"
            ),
            "direct_herm2_huv_rows_search": rel(OUT_DIR / "direct_herm2_huv_rows_search.packet.json"),
            "non_circulation_ledger": rel(OUT_DIR / "non_circulation_ledger.packet.json"),
            "next_labeled_workorder": rel(OUT_DIR / "next_labeled_workorder.packet.json"),
        },
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1X_SelectedHiggsHYMSectionRingQuadratureOrDirectHuvRows_v1",
        "status": STATUS,
        "active_label": ACTIVE_LABEL,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "ordered_Hu_Hd_channel_scaffold_closed": True,
        "E_H_UV_exact_sequence_scaffold_closed": True,
        "bridge_validator_first_clause_filled": True,
        "selected_E_H_UV_section_basis_emitted": False,
        "selected_HYM_metric_or_connection_emitted": False,
        "quadrature_weights_emitted": False,
        "trace_to_H7B1U_grid_identity_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "candidate_path": rel(DATA),
        "note_path": rel(NOTE),
    }

    write_json(OUT_DIR / "ordered_higgs_channel_label_import.packet.json", ordered_higgs_labels)
    write_json(OUT_DIR / "bridge_validator_replay.packet.json", validator)
    write_json(OUT_DIR / "section_basis_quadrature_payload_request.packet.json", section_basis_request)
    write_json(OUT_DIR / "direct_herm2_huv_rows_search.packet.json", direct_rows)
    write_json(OUT_DIR / "non_circulation_ledger.packet.json", no_cycle)
    write_json(OUT_DIR / "next_labeled_workorder.packet.json", next_work)
    write_json(DATA, candidate)
    write_json(CERT, cert)
    write_note(candidate)

    print(json.dumps({"candidate": rel(DATA), "status": STATUS}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
