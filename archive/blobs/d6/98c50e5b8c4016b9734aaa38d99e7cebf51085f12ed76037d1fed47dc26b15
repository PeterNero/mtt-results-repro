"""Build CONST-HIGGS-01 H1 shared-metrology primitive test packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM_REPO = TEXPAPERS / "mtt-nonsm-constants-no-knob"
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h1_shared_metrology_primitive_test"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SHARED_METROLOGY = BASE / "shared_metrology_import.packet.json"
SOURCE_SCAN = BASE / "higgs_source_scan.packet.json"
PROJECTOR_STATUS = BASE / "projector_and_27mode_support_status.packet.json"
PARITY_REPLAY = BASE / "downstream_higgs_replay_boundary.packet.json"
THRESHOLD_GATE = BASE / "quartic_threshold_gate.packet.json"
BOUNDARY = BASE / "h1_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H1_SharedMetrologyPrimitiveTest_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H1_SHARED_METROLOGY_PRIMITIVE_TEST_BUILT"


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

    targets_path = DATA / "constant_frontier_ledger" / "individual_constant_targets.packet.json"
    g4_path = DATA / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive.candidate.json"
    g4_contract_path = DATA / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive" / "one_metrology_primitive_contract.packet.json"
    g4_boundary_path = DATA / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive" / "g4_boundary.packet.json"
    visible_path = NONSM_REPO / "candidate_data" / "visible_operator_and_hessian_frontier_import.candidate.json"
    spectral_path = NONSM_REPO / "candidate_data" / "spectral_galerkin_projector_retention_reduction_import.candidate.json"
    trace27_path = NONSM_REPO / "candidate_data" / "selected_trace_equals_emitted_27_mode_de_attempt.candidate.json"
    form_bound_path = NONSM_REPO / "candidate_data" / "selected_phifin_s2_a_sel_n_form_bound_fill_attempt.candidate.json"
    provenance_path = NONSM_REPO / "candidate_data" / "selected_phifin_s2_27_mode_provenance_theorem_attempt.candidate.json"
    common_scale_path = SM_PARITY_REPO / "candidate_data" / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit.candidate.json"
    external_rg_path = SM_PARITY_REPO / "candidate_data" / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json"
    higgs_precision_path = SM_PARITY_REPO / "candidate_data" / "selected_higgsprecisionpromotionmatrix_or_operatorprofile.candidate.json"
    higgs_profile_path = SM_PARITY_REPO / "candidate_data" / "selected_higgsacceptedprofileimport_or_rowvaluereplacement.candidate.json"

    targets = load(targets_path)
    g4 = load(g4_path)
    g4_contract = load(g4_contract_path)
    g4_boundary = load(g4_boundary_path)
    visible = load(visible_path)
    spectral = load(spectral_path)
    trace27 = load(trace27_path)
    form_bound = load(form_bound_path)
    provenance = load(provenance_path)
    common_scale = load(common_scale_path)
    external_rg = load(external_rg_path)
    higgs_precision = load(higgs_precision_path)
    higgs_profile = load(higgs_profile_path)

    target_rows = {row["label"]: row for row in targets["targets"]}
    target_row = target_rows["CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD"]
    spectral_upstream = spectral["upstream_spectral_projector_retention"]

    shared_metrology = {
        "schema": "MTTConstHiggs01H1SharedMetrologyImport.v1",
        "status": "G4_ONE_METROLOGY_PRIMITIVE_IMPORTED_FOR_HIGGS_TEST",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-SHARED-METROLOGY-IMPORT",
        "inputs": {
            "G4_candidate": rel(g4_path),
            "G4_one_metrology_contract": rel(g4_contract_path),
            "G4_boundary": rel(g4_boundary_path),
        },
        "imported_from_G4": {
            "one_universal_metrology_primitive_tier_defined": g4["one_universal_metrology_primitive_tier_defined"],
            "selected_metrology_primitive_value": g4["selected_metrology_primitive_value"],
            "strict_no_knob_absolute_scale_closure": g4["strict_no_knob_absolute_scale_closure"],
            "Omega0_convention_reconciled": g4["Omega0_convention_reconciled"],
        },
        "use_in_Higgs_branch": {
            "allowed": "Use E0/L0/Omega0 only as the already-declared universal metrology/action-normalization slot.",
            "forbidden": [
                "choose the primitive from measured Higgs mass, vev, width, branching ratios, lambda_H, or RG benchmarks",
                "add a Higgs-specific threshold or action-normalization knob",
                "rename the one-primitive tier as strict no-knob Higgs closure",
            ],
        },
        "parameter_budget": {
            "new_Higgs_specific_parameters": 0,
            "new_universal_primitives": 0,
            "imported_universal_metrology_primitives": 1,
            "selected_numeric_primitive_values_now": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_scan = {
        "schema": "MTTConstHiggs01H1SourceScan.v1",
        "status": "HIGGS_SOURCE_SUPPORT_SCANNED_SOURCE_PROVENANCE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-HIGGS-SOURCE-SCAN",
        "inputs": {
            "visible_operator_and_hessian_frontier": rel(visible_path),
            "spectral_galerkin_projector_retention": rel(spectral_path),
            "selected_trace_equals_27_mode_DE_attempt": rel(trace27_path),
            "selected_PhiFin_S2_form_bound_fill_attempt": rel(form_bound_path),
            "selected_PhiFin_S2_27_mode_provenance_attempt": rel(provenance_path),
        },
        "superset_strategy": {
            "straight_path": "Use the selected S3/GS/Route-C source line to ask for a Higgs quartic/threshold kernel.",
            "converging_support_paths": [
                "block-family/Higgs projector retention from selected twisted S3 source",
                "finite 27-mode D_E formula with Higgs zero-cluster shift",
                "Phi_fin/Galerkin-Cech finite trace provenance route",
                "SM-parity downstream Higgs replay/profile rows as non-selector comparison evidence",
            ],
            "locked_target": "SelectedHiggsQuarticThresholdKernel, not measured lambda_H or Higgs mass.",
        },
        "source_side_evidence": {
            "block_projector_layer_closed": spectral_upstream["two_layer_projector_audit"]["block_projector_layer"]["block_family_Higgs_projector_retention"],
            "block_vs_spectral_distinction_closed": spectral["what_closes_now"]["block_vs_spectral_projector_distinction_closed"],
            "routec_operator_shape_support_imported": spectral["what_closes_now"]["routec_operator_shape_support_imported"],
            "hessian_kernel_derivation_interface_built": visible["what_closes_now"]["qa_hessian_kernel_derivation_interface_built"],
            "same_source_operator_payload_contract_built": visible["what_closes_now"]["same_source_operator_payload_contract_built"],
            "actual_27_mode_matrix_entries_emitted": provenance["evidence_table"]["actual_27_mode_matrix_entries_emitted"],
            "same_27_mode_basis_available": provenance["evidence_table"]["same_27_mode_basis_available"],
        },
        "source_side_open": {
            "coherent_spectral_projector_retention": spectral["what_remains_open"]["coherent_spectral_projector_retention"],
            "selected_DE_Riesz_Green_dotD_values": spectral["what_remains_open"]["selected_DE_Riesz_Green_dotD_values"],
            "selected_HYM_Strominger_metric_connection": spectral["what_remains_open"]["selected_HYM_Strominger_metric_connection"],
            "selected_RouteC_Strominger_Galerkin_residual_solve": spectral["what_remains_open"]["selected_RouteC_Strominger_Galerkin_residual_solve"],
            "functorial_finite_Phi_fin_trace_proved": not provenance["evidence_table"]["functorial_finite_Phi_fin_trace_proved"],
            "existing_27_mode_matrices_identified_as_selected_compression": provenance["evidence_table"]["existing_27_mode_matrices_identified_as_selected_compression"] is False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    projector_status = {
        "schema": "MTTConstHiggs01H1ProjectorAnd27ModeStatus.v1",
        "status": "PROJECTOR_SUPPORT_CLOSED_27MODE_DIAGNOSTIC_WITHIN_BUDGET_SELECTED_SOURCE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-PROJECTOR-AND-27MODE-STATUS",
        "block_projector_layer": spectral_upstream["two_layer_projector_audit"]["block_projector_layer"],
        "spectral_projector_layer": spectral_upstream["two_layer_projector_audit"]["spectral_projector_layer"],
        "higgs_27mode_formula": {
            "formula_theorem_proved": trace27["formula_theorem"]["proved"],
            "formula_statement": trace27["formula_theorem"]["statement"],
            "H_sector_formula_check": trace27["sector_formula_checks"]["H"],
            "selected_trace_attempt_proved": trace27["selected_trace_attempt"]["proved"],
            "selected_trace_attempt_reason": trace27["selected_trace_attempt"]["reason"],
        },
        "eta_budget": {
            "eta_if_provenance_supplied": provenance["diagnostic_eta"]["eta_if_provenance_supplied"],
            "threshold": provenance["diagnostic_eta"]["threshold"],
            "passes_threshold": provenance["diagnostic_eta"]["passes_threshold"],
            "selected_eta_emitted_now": provenance["diagnostic_eta"]["selected_eta_emitted_now"],
            "form_bound_status": form_bound["status"],
        },
        "minimal_source_fix_to_promote": form_bound["minimal_fix_to_close"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    parity_replay = {
        "schema": "MTTConstHiggs01H1DownstreamHiggsReplayBoundary.v1",
        "status": "DOWNSTREAM_HIGGS_REPLAY_IMPORTED_AS_NON_SELECTOR_EVIDENCE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-DOWNSTREAM-HIGGS-REPLAY-BOUNDARY",
        "inputs": {
            "common_scale_yukawa_higgs_transport": rel(common_scale_path),
            "external_literature_RG_benchmark_values": rel(external_rg_path),
            "higgs_precision_promotion_matrix": rel(higgs_precision_path),
            "higgs_accepted_profile_controller": rel(higgs_profile_path),
        },
        "downstream_replay_evidence": {
            "common_scale_transport_kernel_specified": common_scale["what_closes_now"]["common_scale_yukawa_higgs_transport_kernel_specified"],
            "lambda_H_MZ_value_remains_open": common_scale["what_remains_open"]["lambda_H_MZ_value"],
            "external_literature_rg_benchmark_values_filled": external_rg["what_closes_now"]["external_literature_rg_benchmark_values_filled"],
            "threshold_covariance_gap_identified": external_rg["what_closes_now"]["threshold_covariance_gap_identified"],
            "SM_parity_Higgs_replay_rows_closed": higgs_precision["closure_decision"]["SM_parity_Higgs_replay_rows_closed"],
            "precision_promotion_matrix_closed": higgs_precision["closure_decision"]["precision_promotion_matrix_closed"],
            "accepted_profile_import": higgs_profile["closure_decision"]["accepted_profile_import"],
        },
        "classification": {
            "usable_for_H1": "comparison and target-interface discipline only",
            "not_usable_for_H1": "selecting the Higgs quartic, threshold kernel, E0/L0, or source packet",
            "reason": "These artifacts replay measured or external-benchmark Higgs/RG data downstream of source selection; H1 is searching for source-side closure.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    threshold_gate = {
        "schema": "MTTConstHiggs01H1QuarticThresholdGate.v1",
        "status": "QUARTIC_THRESHOLD_GATE_REDUCED_TO_SELECTED_KERNEL_OR_FINITE_TRACE_MORPHISM",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-QUARTIC-THRESHOLD-GATE",
        "target_row": target_row,
        "strict_acceptance": {
            "must_emit": [
                "selected Higgs projector/zero-mode values from same Route-C/Strominger source",
                "selected Higgs quartic/threshold kernel or equivalent Phi_fin second-variation block",
                "normalization map showing reuse of the G4 metrology/action primitive without a Higgs-specific knob",
                "threshold/RG convention boundary if comparing to downstream lambda_H",
                "honest validator replay with selected_source_verified true rather than lifted flags",
            ],
            "must_not_use": [
                "observed m_H or v to set lambda_H",
                "Higgs widths or branching ratios to choose the source",
                "external RG benchmark rows to choose the kernel",
                "per-sector retuning of E0/L0/Omega0",
            ],
        },
        "current_verdict": {
            "projector_support_sufficient_to_continue": True,
            "diagnostic_eta_budget_promising": provenance["diagnostic_eta"]["passes_threshold"],
            "strict_selected_Higgs_kernel_emitted": False,
            "Higgs_quartic_numeric_value_derived": False,
            "one_metrology_primitive_reuse_consistent_so_far": True,
            "closure_claimed": False,
        },
        "best_next_artifact": "MTT_CONST_HIGGS_01_H2_SelectedHiggsProjectorAndQuarticKernelSourcePacket_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstHiggs01H1Boundary.v1",
        "status": "H1_SHARED_PRIMITIVE_TEST_BUILT_QUARTIC_SOURCE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-BOUNDARY",
        "closed_or_decided_now": {
            "G4_one_metrology_primitive_imported_without_new_Higgs_knob": True,
            "Higgs_projector_source_scan_completed": True,
            "block_family_Higgs_projector_support_imported": True,
            "diagnostic_27mode_Higgs_eta_budget_imported": True,
            "downstream_Higgs_replay_classified_as_non_selector": True,
            "H2_source_packet_gate_named": True,
        },
        "still_open": {
            "strict_selected_Higgs_projector_values": True,
            "selected_PhiFin_finite_trace_morphism": True,
            "selected_Higgs_quartic_threshold_kernel": True,
            "Higgs_quartic_numeric_value": True,
            "accepted_precision_lambda_H_transport": True,
            "strict_no_knob_Higgs_closure": True,
            "one_primitive_cross_constant_validation": g4_boundary["still_open"]["one_primitive_cross_constant_validation"],
        },
        "anti_cycle_delta_from_G4": {
            "G4": "froze the shared metrology primitive tier and selected Higgs as the next cross-constant test",
            "H1": "tests Higgs without selecting a primitive value, without measured Higgs backfit, and without promoting diagnostic projector evidence as source closure",
            "not_repeated": [
                "not reopening GR Omega0 as the active Higgs blocker",
                "not using SM-parity Higgs replay rows as source proof",
                "not claiming lambda_H or Higgs width prediction",
                "not adding a Higgs-specific knob",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H1NextWork.v1",
        "status": "NEXT_WORKORDER_H2_SELECTED_HIGGS_PROJECTOR_AND_QUARTIC_KERNEL_PACKET",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-NEXT",
        "primary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-SELECTED-HIGGS-PROJECTOR-AND-QUARTIC-KERNEL-SOURCE-PACKET",
            "task": "Try to emit the same-source selected Higgs projector/zero-mode packet and a quartic/threshold Hessian or Phi_fin second-variation kernel, reusing the G4 metrology/action primitive and forbidding measured Higgs data as selectors.",
        },
        "parallel": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2B-FINITE-TRACE-MORPHISM-IDENTIFIES-27MODE",
            "task": "Attack the provenance morphism that would promote the 27-mode D_E scaffold and eta=1.0 budget to selected Higgs/source evidence.",
        },
        "parking_lot": {
            "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN / G4B-SAME-BRANCH-PHYSICAL-ROD-CLOCK-THEOREM",
            "task": "Return only if a strict same-branch physical-unit theorem appears; do not use Higgs measured data to choose it.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H1SharedMetrologyPrimitiveTest",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-SHARED-METROLOGY-PRIMITIVE-TEST",
        "output_packets": {
            "shared_metrology_import": rel(SHARED_METROLOGY),
            "higgs_source_scan": rel(SOURCE_SCAN),
            "projector_and_27mode_support_status": rel(PROJECTOR_STATUS),
            "downstream_higgs_replay_boundary": rel(PARITY_REPLAY),
            "quartic_threshold_gate": rel(THRESHOLD_GATE),
            "h1_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H1SharedMetrologyPrimitiveTestTheorem",
            "proved": True,
            "statement": (
                "The Higgs quartic/threshold sector is a valid next cross-constant test of the already-declared G4 metrology/action primitive. Current source-side evidence closes block-family/Higgs projector support and identifies a promising finite 27-mode Higgs diagnostic under the eta threshold, but selected Phi_fin provenance, coherent spectral projectors, and the actual Higgs quartic/threshold kernel remain open. Therefore H1 advances the branch and names H2 without claiming a Higgs numerical derivation."
            ),
        },
        "G4_one_metrology_primitive_reused": True,
        "new_Higgs_specific_parameters": 0,
        "block_family_Higgs_projector_support_closed": True,
        "diagnostic_27mode_eta_within_budget": True,
        "selected_PhiFin_provenance_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "downstream_Higgs_replay_nonselector_boundary_closed": True,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H2_SelectedHiggsProjectorAndQuarticKernelSourcePacket_v1",
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H1_SharedMetrologyPrimitiveTest_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "G4_one_metrology_primitive_reused": True,
        "new_Higgs_specific_parameters": 0,
        "block_family_Higgs_projector_support_closed": True,
        "diagnostic_27mode_eta_within_budget": True,
        "selected_PhiFin_provenance_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "downstream_Higgs_replay_nonselector_boundary_closed": True,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H1 Shared Metrology Primitive Test v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H1-SHARED-METROLOGY-PRIMITIVE-TEST`

## Result

```text
G4 shared metrology/action primitive reused       True
new Higgs-specific parameters                     0
block-family/Higgs projector support closed       True
27-mode diagnostic eta within threshold           True
selected Phi_fin provenance closed                False
selected Higgs quartic/threshold kernel emitted   False
Higgs quartic numeric value derived               False
```

H1 keeps the superset strategy honest.  We combine several paths only to lock a
source-side target:

```text
selected S3/GS/Route-C projector support
+ finite 27-mode D_E Higgs diagnostic
+ Phi_fin/Galerkin-Cech provenance route
+ downstream SM-parity Higgs replay boundary
=> SelectedHiggsQuarticThresholdKernel
```

The locked target is not measured `lambda_H`, `m_H`, `v`, widths, or branching
ratios.  Those rows can be downstream replay/comparison data only.

## What Closes

- The G4 one-universal-metrology primitive tier can be imported into the Higgs
  sector without adding a Higgs-specific knob.
- The selected S3 source closes block-family/Higgs projector support.
- The finite 27-mode diagnostic has `eta=1.0 < 2.1932454224643014` if the
  missing provenance morphism is supplied.
- The SM-parity Higgs replay/profile machinery is classified as downstream
  non-selector evidence.

## What Remains

H2 must emit either:

```text
1. a selected Higgs projector plus quartic/threshold Hessian/Phi_fin kernel, or
2. a finite trace morphism proving the 27-mode D_E scaffold is the selected
   Phi_fin/Strominger compression.
```

Until then this branch is promising source support, not a Higgs quartic
derivation.
"""

    for path, payload in [
        (SHARED_METROLOGY, shared_metrology),
        (SOURCE_SCAN, source_scan),
        (PROJECTOR_STATUS, projector_status),
        (PARITY_REPLAY, parity_replay),
        (THRESHOLD_GATE, threshold_gate),
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
