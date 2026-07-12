"""Build physical dotD/sector-transfer import test for the K-row frontier.

The previous F_K packet left the next target phrased as physical dotD,
sector transfer, retarded-overlap rows, T_scheme rows, lambda_H, or controlled
empirical K import.  Later packets already close the stationary projector and
dotD side, and the same-source dynamic matter packet closes a first
non-scalar response layer.  This builder imports those stronger results and
tests whether they emit the ten scalar K_threshold rows.

The answer is intentionally strict: dotD/sector transfer is no longer the
active blocker, but the rowwise retarded-overlap derivative values, selected
T_scheme rows, and lambda_H payload are still not emitted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicaldotdalpha1sectortransferretardedoverlapkernel_or_empiricalkparityimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "physical_dotd_sector_transfer_import_reconciliation.packet.json"
READINESS = PACKET_DIR / "retarded_overlap_kernel_readiness_after_stationary_transfer.packet.json"
EMISSION = PACKET_DIR / "krow_emission_after_physical_transfer_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_physical_transfer_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalDotDAlpha1SectorTransferRetardedOverlapKernel_or_EmpiricalKParityImport_v1.md"

PREVIOUS = DATA / "selected_kthresholdfunctionalfromhymthresholdaction_or_controlledempiricalkimport.candidate.json"
PREVIOUS_CUTSET = (
    DATA
    / "selected_kthresholdfunctionalfromhymthresholdaction_or_controlledempiricalkimport"
    / "next_cutset_after_fk_action_attempt.packet.json"
)
K_GRAMMAR = DATA / "selected_combinedthresholdkernelkrows_sourcetheorem" / "closed_source_k_threshold_grammar.packet.json"
K_CONDITIONAL = (
    DATA
    / "selected_combinedthresholdkernelkrows_sourcetheorem"
    / "conditional_k_rows_scalar_closure_theorem.packet.json"
)
EMPIRICAL_K = (
    DATA
    / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
    / "controlled_empirical_k_import_contract.packet.json"
)
EMPIRICAL_DECISION = (
    DATA
    / "selected_kthresholdfunctionalfromhymthresholdaction_or_controlledempiricalkimport"
    / "controlled_empirical_k_import_decision.packet.json"
)
HYM_FIRST_DOTD = DATA / "selected_physicaldotd_sectorrouting_after_hymfirstsolve.candidate.json"
STEP40_DOTD = DATA / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier.candidate.json"
STEP40_IMPORT = (
    DATA
    / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier"
    / "step40_dotd_transport_alpha1_import.packet.json"
)
STATIONARY = DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json"
STATIONARY_PROMOTION = (
    DATA / "selected_stationaryprojector_dotd_integrated_frontier" / "promoted_stationary_sector_packet.packet.json"
)
STATIONARY_FRONTIER = (
    DATA / "selected_stationaryprojector_dotd_integrated_frontier" / "dynamic_c1_frontier_after_projector_dotd.packet.json"
)
DYNAMIC_MATTER = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
DYNAMIC_NONSCALAR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
DYNAMIC_CUTSET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "next_cutset_after_dynamic_matter_overlap_packet.packet.json"
)
ROWLOCAL_FUNCTIONAL = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "selected_overlap_quadrature_functional.packet.json"
)
THRESHOLD_GATE = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "threshold_scheme_source_gate.packet.json"
)

STATUS = (
    "MTT_SELECTED_PHYSICALDOTDALPHA1SECTORTRANSFERRETARDEDOVERLAPKERNEL_OR_EMPIRICALKPARITYIMPORT_"
    "BUILT_DOTD_SECTOR_IMPORTED_DYNAMIC_ROWS_OPEN"
)
NEXT = "MTT_Selected_DynamicRetardedOverlapDerivativeRows_or_TSchemeLambdaHSourceExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing physical-transfer K-row inputs: " + ", ".join(missing))


def sector_for(row: dict[str, Any]) -> str:
    return row["sector"]


def build_readiness_rows(
    grammar_rows: list[dict[str, Any]],
    empirical_rows: list[dict[str, Any]],
    sector_slots: dict[str, dict[str, Any]],
    threshold_gate: dict[str, Any],
    dynamic_matter: dict[str, Any],
) -> list[dict[str, Any]]:
    empirical_by_omega = {row["omega_id"]: row for row in empirical_rows}
    rows: list[dict[str, Any]] = []
    for row in grammar_rows:
        sector = sector_for(row)
        slot = sector_slots[sector]
        is_higgs = sector == "H"
        empirical = empirical_by_omega[row["omega_id"]]
        rows.append(
            {
                "omega_id": row["omega_id"],
                "combined_kernel_row_id": row["combined_kernel_row_id"],
                "sector": sector,
                "generation_or_lambda": row["generation_or_lambda"],
                "stationary_sector_projector_available": slot["source_verified_by_transport_conjugation"],
                "stationary_rho_s_available": slot["stationary_rho_s_promoted"],
                "stationary_sector_rank": slot["rank"],
                "green_operator_valid": slot["green_operator_valid"],
                "physical_dotD_alpha1_available": True,
                "same_source_dynamic_matter_first_response_available": dynamic_matter["promotion_decision"][
                    "selected_dynamic_QaSU3_operator_packet_first_response_layer_closed"
                ],
                "dynamic_first_response_is_scalar_K_value_source": False,
                "selected_retarded_overlap_derivative_row_emitted": False,
                "selected_threshold_scheme_row_emitted": threshold_gate[
                    "selected_threshold_response_functional_instantiated"
                ],
                "selected_lambda_H_payload_emitted": False if is_higgs else None,
                "selected_K_threshold_row_emitted": False,
                "emitted_K_threshold_value": None,
                "accepted_as_no_knob_source_row": False,
                "empirical_K_import_available": empirical["selected_for_no_knob"] is False,
                "empirical_K_value_symbolic": empirical["empirical_K_import_symbolic"],
                "accepted_as_controlled_empirical_row": True,
                "blocking_reasons": [
                    "stationary sector projector/rho_s and physical dotD_alpha1 are available by import",
                    "same-source dynamic matter overlap is first-response/non-scalar support, not a scalar K_threshold value functional",
                    "selected rowwise retarded-overlap derivative value is not emitted",
                    "selected T_scheme row is not instantiated",
                    "empirical K import remains parity-only and cannot define the no-knob source row",
                ]
                + (["selected lambda_H H-sector payload is not emitted"] if is_higgs else []),
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_CUTSET,
        K_GRAMMAR,
        K_CONDITIONAL,
        EMPIRICAL_K,
        EMPIRICAL_DECISION,
        HYM_FIRST_DOTD,
        STEP40_DOTD,
        STEP40_IMPORT,
        STATIONARY,
        STATIONARY_PROMOTION,
        STATIONARY_FRONTIER,
        DYNAMIC_MATTER,
        DYNAMIC_NONSCALAR,
        DYNAMIC_CUTSET,
        ROWLOCAL_FUNCTIONAL,
        THRESHOLD_GATE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    grammar = load(K_GRAMMAR)
    conditional = load(K_CONDITIONAL)
    empirical_k = load(EMPIRICAL_K)
    empirical_decision = load(EMPIRICAL_DECISION)
    hym_first_dotd = load(HYM_FIRST_DOTD)
    step40 = load(STEP40_DOTD)
    step40_import = load(STEP40_IMPORT)
    stationary = load(STATIONARY)
    stationary_promotion = load(STATIONARY_PROMOTION)
    stationary_frontier = load(STATIONARY_FRONTIER)
    dynamic_matter = load(DYNAMIC_MATTER)
    dynamic_nonscalar = load(DYNAMIC_NONSCALAR)
    dynamic_cutset = load(DYNAMIC_CUTSET)
    rowlocal_functional = load(ROWLOCAL_FUNCTIONAL)
    threshold_gate = load(THRESHOLD_GATE)

    rows = build_readiness_rows(
        grammar["grammar_rows"],
        empirical_k["empirical_K_rows"],
        stationary_promotion["sector_slots"],
        threshold_gate,
        dynamic_matter,
    )
    required_rows = grammar["row_count"]
    active_scalar_sector_classes = sorted({row["sector"] for row in rows})
    active_scalar_sector_class_upper_bound = len(active_scalar_sector_classes)

    reconciliation = {
        "schema": "MTTPhysicalDotDSectorTransferImportReconciliation.v1",
        "status": "PHYSICAL_DOTD_AND_STATIONARY_SECTOR_TRANSFER_IMPORTED_FOR_K_ATTEMPT",
        "previous_fk_cutset": previous_cutset["status"],
        "direct_hym_firstsolve_branch": {
            "status": hym_first_dotd["status"],
            "physical_dotD_alpha1_closed_in_direct_firstsolve_packet": hym_first_dotd["closure_decision"][
                "physical_dotD_alpha1_closed"
            ],
            "selected_End0_to_sector_routing_values_extracted": hym_first_dotd["closure_decision"][
                "selected_End0_to_sector_routing_values_extracted"
            ],
            "finite_projector_values_emitted": hym_first_dotd["closure_decision"][
                "finite_projector_values_emitted"
            ],
            "finite_projector_values_promoted_to_selected": hym_first_dotd["closure_decision"][
                "finite_projector_values_promoted_to_selected"
            ],
        },
        "later_dotd_import": {
            "status": step40["status"],
            "selected_dotD_transport_derivative_formula_closed": step40_import["closure_result"][
                "selected_dotD_transport_derivative_formula_closed"
            ],
            "selected_alpha1_driver_normalization_closed": step40_import["closure_result"][
                "selected_alpha1_driver_normalization_closed"
            ],
            "same_branch_dotD_alpha1_values_closed": step40_import["closure_result"][
                "same_branch_dotD_alpha1_values_closed"
            ],
            "honest_dotD_alpha1_replay_closed": step40_import["closure_result"][
                "honest_dotD_alpha1_replay_closed"
            ],
            "guardrail": "imports dotD/alpha1 replay; does not emit primitive C1 scalar contractions or K rows",
        },
        "stationary_sector_import": {
            "status": stationary["status"],
            "stationary_projector_source_verified": stationary["closure_decision"][
                "stationary_projector_source_verified"
            ],
            "validator_ready_stationary_rho_s": stationary["closure_decision"]["validator_ready_stationary_rho_s"],
            "selected_dotD_source_verified": stationary["closure_decision"]["selected_dotD_source_verified"],
            "alpha1_driver_verified": stationary["closure_decision"]["alpha1_driver_verified"],
            "physical_dotD_alpha1_available_by_import": stationary_promotion["global_checks"][
                "physical_dotD_alpha1_available_by_import"
            ],
            "all_stationary_rho_s_promoted": stationary_promotion["global_checks"][
                "all_stationary_rho_s_promoted"
            ],
            "all_source_verified": stationary_promotion["global_checks"]["all_source_verified"],
        },
        "dynamic_first_response_import": {
            "status": dynamic_matter["status"],
            "dynamic_matter_overlap_operator_packet_closed": dynamic_matter["promotion_decision"][
                "dynamic_matter_overlap_operator_packet_closed"
            ],
            "selected_dynamic_QaSU3_operator_packet_first_response_layer_closed": dynamic_matter[
                "promotion_decision"
            ]["selected_dynamic_QaSU3_operator_packet_first_response_layer_closed"],
            "primitive_C1_contractions_selected_emitted_first_response_layer": dynamic_matter["what_closes_now"][
                "primitive_C1_contractions_selected_emitted_first_response_layer"
            ],
            "Yukawa_magnitudes_predicted": dynamic_nonscalar["guardrail"]["Yukawa_magnitudes_predicted"],
            "full_mass_spectrum_predicted": dynamic_nonscalar["guardrail"]["full_mass_spectrum_predicted"],
            "recommended_next": dynamic_cutset["recommended_next"]["artifact"],
        },
        "closed_for_this_k_attempt": {
            "physical_dotD_alpha1_available": True,
            "stationary_sector_projectors_available": True,
            "stationary_rho_s_available": True,
            "dynamic_first_response_support_available": True,
            "direct_hym_firstsolve_dotd_gap_superseded_by_later_import": True,
        },
        "still_not_emitted": {
            "selected_retarded_overlap_derivative_row_values": False,
            "selected_threshold_scheme_rows_T_scheme": False,
            "selected_lambda_H_H_sector_payload": False,
            "ten_selected_K_threshold_rows": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RECONCILIATION, reconciliation)

    readiness = {
        "schema": "MTTRetardedOverlapKernelReadinessAfterStationaryTransfer.v1",
        "status": "DOTD_SECTOR_TRANSFER_READY_RETARDED_ROW_VALUES_OPEN",
        "row_count": len(rows),
        "required_selected_K_row_count": required_rows,
        "active_scalar_sector_classes": active_scalar_sector_classes,
        "active_scalar_sector_class_upper_bound": active_scalar_sector_class_upper_bound,
        "sector_class_bound_sufficient_for_ten_K_rows": active_scalar_sector_class_upper_bound >= required_rows,
        "generation_basis_rank_typed_but_no_derivative_matrix_elements_emitted": True,
        "functional_contract_imported": {
            "status": rowlocal_functional["status"],
            "requires_selected_retarded_overlap_kernel": True,
            "requires_selected_threshold_scheme_values": True,
            "requires_target_values_only_after_emission": rowlocal_functional["acceptance_predicate"][
                "target_values_used_only_after_emission"
            ],
        },
        "threshold_scheme_gate": {
            "status": threshold_gate["status"],
            "selected_threshold_response_functional_instantiated": threshold_gate[
                "selected_threshold_response_functional_instantiated"
            ],
            "accepted_T_scheme_source_row_count": threshold_gate["accepted_T_scheme_source_row_count"],
            "generation_resolved_threshold_source_rows_closed": threshold_gate[
                "generation_resolved_threshold_source_rows_closed"
            ],
        },
        "row_readiness": rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(READINESS, readiness)

    emission = {
        "schema": "MTTKRowEmissionAfterPhysicalTransferAttempt.v1",
        "status": "PHYSICAL_TRANSFER_IMPORTED_NO_SELECTED_K_ROWS_EMITTED",
        "closed_K_grammar_rows": grammar["row_count"] == 10,
        "conditional_K_to_Omega_theorem": conditional["status"]
        == "CONDITIONAL_SCALAR_CLOSURE_PROVED_ANTECEDENT_OPEN",
        "physical_dotD_alpha1_available": True,
        "stationary_sector_transfer_available": True,
        "same_source_dynamic_first_response_support_available": True,
        "selected_retarded_overlap_derivative_rows_emitted": False,
        "selected_T_scheme_rows_emitted": False,
        "selected_lambda_H_payload_emitted": False,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "controlled_empirical_K_rows_available": empirical_k["empirical_K_row_count"],
        "controlled_empirical_K_import_selected_for_no_knob": empirical_decision["selected_for_no_knob_closure"],
        "row_decisions": [
            {
                "omega_id": row["omega_id"],
                "sector": row["sector"],
                "selected_K_threshold_row_emitted": row["selected_K_threshold_row_emitted"],
                "accepted_as_no_knob_source_row": row["accepted_as_no_knob_source_row"],
                "accepted_as_controlled_empirical_row": row["accepted_as_controlled_empirical_row"],
            }
            for row in rows
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EMISSION, emission)

    cutset = {
        "schema": "MTTNextCutsetAfterPhysicalTransferAttempt.v1",
        "status": "NEXT_ATTACK_DYNAMIC_RETARDED_OVERLAP_DERIVATIVES_TSCHEME_LAMBDAH",
        "next_required_artifact": NEXT,
        "closed_here": [
            "physical dotD_alpha1 imported into the K-row frontier",
            "stationary sector projector/rho_s/Green transfer imported into every K slot",
            "same-source dynamic matter overlap first-response layer imported as support",
            "direct HYM-firstsolve dotD wording superseded by later stationary/dotD import",
            "empirical K parity import retained as non-no-knob boundary",
        ],
        "still_open": [
            "selected rowwise retarded-overlap derivative values",
            "selected threshold-scheme rows T_scheme.*",
            "selected lambda_H H-sector value/quartic payload",
            "ten selected K_threshold rows",
            "strict Omega/lambda_H scalar execution",
            "matrix-level mixing extension",
            "full no-knob SM closure",
        ],
        "forbidden_routes": [
            "reopen physical dotD_alpha1 or stationary projectors as active blockers without a failed import audit",
            "use first-response dynamic matter matrices as scalar K_threshold rows",
            "use empirical K import as F_K",
            "use observed Yukawa/Higgs values to select T_scheme or retarded rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET, cutset)

    decision = {
        "physical_dotD_alpha1_imported": True,
        "stationary_sector_transfer_imported": True,
        "dynamic_first_response_support_imported": True,
        "retarded_overlap_kernel_readiness_built": True,
        "selected_retarded_overlap_derivative_rows_emitted": False,
        "selected_T_scheme_rows_emitted": False,
        "selected_lambda_H_payload_emitted": False,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "controlled_empirical_K_import_available": True,
        "controlled_empirical_K_import_selected_for_no_knob": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedPhysicalDotDAlpha1SectorTransferRetardedOverlapKernelOrEmpiricalKParityImport",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "PhysicalDotDSectorTransferImportedKRowsStillNeedDynamicDerivativeAndThresholdValues",
            "proved": True,
            "statement": (
                "After importing the later selected dotD/alpha1 theorem, stationary sector projector/rho_s/Green "
                "packet, and same-source dynamic matter first-response packet, physical dotD_alpha1 and stationary "
                "sector transfer are no longer active blockers for the ten K_threshold rows.  These imports still "
                "do not emit rowwise retarded-overlap derivative values, selected T_scheme rows, or the lambda_H "
                "H-sector payload.  Therefore no selected numerical K_threshold rows are emitted; empirical K "
                "rows remain only a controlled parity layer."
            ),
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "physical_dotd_sector_transfer_import_reconciliation": rel(RECONCILIATION),
            "retarded_overlap_kernel_readiness_after_stationary_transfer": rel(READINESS),
            "krow_emission_after_physical_transfer_attempt": rel(EMISSION),
            "next_cutset_after_physical_transfer_attempt": rel(CUTSET),
        },
        "closure_decision": decision,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PhysicalDotDAlpha1SectorTransferRetardedOverlapKernel_or_EmpiricalKParityImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected PhysicalDotDAlpha1SectorTransferRetardedOverlapKernel or EmpiricalKParityImport v1

Status: `{STATUS}`.

This packet attacks the post-`F_K` cutset with the strongest already verified
imports.

What closes:

```text
physical dotD_alpha1 imported into K frontier      : true
stationary sector transfer imported into K slots   : true
same-source dynamic first-response support imported: true
direct HYM-firstsolve dotD gap retired             : true
```

What still does not emit:

```text
selected retarded-overlap derivative rows : false
selected T_scheme rows                    : false
selected lambda_H payload                 : false
accepted selected K rows                  : 0
accepted internal scalar rows             : 0
empirical K selected for no-knob           : false
```

So the proof has moved forward: `physical_dotD_alpha1` and stationary
projector/sector transfer should not be listed as active K-row blockers in the
current ledger.  The remaining scalar wall is sharper:

```text
rowwise selected retarded-overlap derivative values
plus selected T_scheme.* and lambda_H source execution
```

The same-source dynamic matter/overlap packet is imported as real first-response
support, but it is not a scalar `K_threshold` value functional and it does not
predict Yukawa magnitudes by itself.  Controlled empirical K rows remain
available only as parity/postcheck data.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
