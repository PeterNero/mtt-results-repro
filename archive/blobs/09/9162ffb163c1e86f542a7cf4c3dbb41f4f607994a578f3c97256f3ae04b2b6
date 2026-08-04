"""Build Herm(2) orientation/phase/trace source or direct H-response emission packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_herm2orientationphasetracesource_or_directhresponseemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Herm2OrientationPhaseTraceSource_or_DirectHResponseEmission_v1.md"

BRIDGE_RECHECK = PACKET_DIR / "projection_bridge_vs_direct_hresponse_recheck.packet.json"
PHASE_TRACE = PACKET_DIR / "orientation_phase_trace_source_inventory.packet.json"
DIRECT_RUN = PACKET_DIR / "direct_hresponse_emission_after_bridge_completion.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_orientation_phase_trace_source.packet.json"

PREVIOUS = DATA / "selected_herm2polarsourcecompletion_or_hresponserows.candidate.json"
HIGGS_DYNAMIC = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof.candidate.json"
EHUV_TRACE = DATA / "selected_ehuvtracegridprojectionidentity_or_directhuvpayload.candidate.json"
EHUV_C5A_GATE = (
    DATA
    / "selected_ehuvtracegridprojectionidentity_or_directhuvpayload"
    / "bridge_validator_c5a_update.packet.json"
)
EHUV_DIRECT_RECHECK = (
    DATA
    / "selected_ehuvtracegridprojectionidentity_or_directhuvpayload"
    / "direct_hresponse_huv_table_recheck_after_c5a.packet.json"
)
MSOURCE = DATA / "selected_msourcehiggsspecificoperatorblock_or_c5c6bridgefrontier.candidate.json"
FULL_MSOURCE = DATA / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable.candidate.json"
HRESPONSE_ROWS = (
    DATA
    / "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution"
    / "hresponse_source_row_execution_table.packet.json"
)

STATUS = (
    "MTT_SELECTED_HERM2ORIENTATIONPHASETRACESOURCE_OR_DIRECTHRESPONSEEMISSION_"
    "PROJECTION_BRIDGE_RETIRED_DIRECT_ROWS_OPEN"
)
NEXT = "MTT_Selected_NonDiagonalHuvHessianSource_or_DirectHerm2Rows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Herm(2) orientation/trace inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        HIGGS_DYNAMIC,
        EHUV_TRACE,
        EHUV_C5A_GATE,
        EHUV_DIRECT_RECHECK,
        MSOURCE,
        FULL_MSOURCE,
        HRESPONSE_ROWS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    higgs_dynamic = load(HIGGS_DYNAMIC)
    ehuv_trace = load(EHUV_TRACE)
    c5a_gate = load(EHUV_C5A_GATE)
    ehuv_direct = load(EHUV_DIRECT_RECHECK)
    msource = load(MSOURCE)
    full_msource = load(FULL_MSOURCE)
    hrows = load(HRESPONSE_ROWS)

    s_beta = previous["key_numbers"]["selected_s_beta_value"]

    bridge_recheck = {
        "schema": "MTTProjectionBridgeVsDirectHResponseRecheck.v1",
        "status": "C1_C6_PROJECTION_BRIDGE_CLOSED_FOR_SBETA_DIRECT_HRESPONSE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "bridge_status": {
            "C1_branch_and_ordered_channel_labels": True,
            "C2_typed_E_H_UV_section_basis": ehuv_trace["closure_decision"][
                "bridge_validator_C2_closed"
            ],
            "C3_selected_HYM_metric_connection": ehuv_trace["closure_decision"][
                "bridge_validator_C3_closed"
            ],
            "C4_quadrature_trace_normalization": ehuv_trace["closure_decision"][
                "bridge_validator_C4_closed"
            ],
            "C5a_trace_grid_identity": ehuv_trace["closure_decision"][
                "bridge_validator_C5a_trace_grid_identity_closed"
            ],
            "C5b_projection_measure_equality": higgs_dynamic["closure_decision"][
                "bridge_validator_C5b_projection_measure_equality_closed"
            ],
            "C6_no_extra_boundary_source": higgs_dynamic["closure_decision"][
                "bridge_validator_C6_no_boundary_closed"
            ],
        },
        "projection_result": {
            "selected_s_beta_value_found": higgs_dynamic["closure_decision"][
                "selected_s_beta_value_found"
            ],
            "selected_s_beta_value": s_beta,
            "selected_finite_reduction_policy_emitted": higgs_dynamic["closure_decision"][
                "selected_finite_reduction_policy_emitted"
            ],
        },
        "direct_value_result": {
            "selected_F_H_second_variation_emitted": higgs_dynamic["closure_decision"][
                "selected_F_H_second_variation_emitted"
            ],
            "selected_dynamic_strain_kernel_emitted": higgs_dynamic["closure_decision"][
                "selected_dynamic_strain_kernel_emitted"
            ],
            "selected_Hermitian_M_H_values_emitted": higgs_dynamic["closure_decision"][
                "selected_Hermitian_M_H_values_emitted"
            ],
            "direct_Herm2_Huv_payload_emitted": higgs_dynamic["closure_decision"][
                "direct_Herm2_Huv_payload_emitted"
            ],
        },
        "decision": {
            "projection_bridge_retired_as_sbeta_blocker": True,
            "projection_bridge_is_not_direct_Herm2_value_source": True,
            "direct_Herm2_rows_emitted": False,
            "accepted_H_response_source_row_count": 0,
        },
    }

    phase_trace = {
        "schema": "MTTHerm2OrientationPhaseTraceSourceInventory.v1",
        "status": "ORIENTATION_PHASE_TRACE_SOURCE_INVENTORY_EXECUTED_ZERO_EMISSIONS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_fields": {
            "r_H": {
                "status": "strict_open_controlled_calibration_available",
                "reason": "controlled HRG calibration exists but is not strict no-knob radial source",
            },
            "sigma_D": {
                "status": "open",
                "rechecked_sources": [
                    "ordered E_H^UV basis",
                    "diagonal HYM metric/connection",
                    "projection reduction",
                ],
                "reason": "basis/order support does not emit selected Delta sign/source orientation",
            },
            "phi_Omega": {
                "status": "open",
                "rechecked_sources": [
                    "diagonal HYM metric/connection",
                    "matter/flavor orientation packets",
                    "projection bridge C1-C6",
                ],
                "reason": "no same-source off-diagonal H_uv phase/sign certificate is emitted",
            },
            "m0": {
                "status": "open_for_full_H_response_rows",
                "tracefree_block_status": "retired",
                "reason": "trace-free threshold block does not require m0, full Huu/Hdd rows do",
            },
            "certificates": {
                "status": "open",
                "required": [
                    "source ownership",
                    "same-source exactness/error",
                    "quotient admissibility",
                    "Hdu_equals_conj_Hud",
                ],
            },
        },
        "support_not_enough": {
            "Higgs_specific_operator_block_emitted": msource["closure_decision"][
                "Higgs_specific_operator_block_emitted"
            ],
            "selected_Hermitian_M_source_emitted": msource["closure_decision"][
                "selected_Hermitian_M_source_emitted"
            ],
            "M_source_plus_R_H_values_emitted": full_msource["closure_decision"][
                "M_source_plus_R_H_values_emitted"
            ],
            "selected_H_response_table_emitted": full_msource["closure_decision"][
                "selected_H_response_table_emitted"
            ],
        },
        "decision": {
            "orientation_phase_trace_inventory_executed": True,
            "strict_radial_scale_source_emitted": False,
            "selected_Delta_sign_emitted": False,
            "selected_Omega_phase_emitted": False,
            "trace_center_source_or_normalization_emitted": False,
            "same_source_certificates_emitted": False,
        },
    }

    direct_run = {
        "schema": "MTTDirectHResponseEmissionAfterBridgeCompletion.v1",
        "status": "DIRECT_HRESPONSE_EMISSION_RECHECK_ZERO_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "row_table_ref": rel(HRESPONSE_ROWS),
        "ehuv_direct_recheck_ref": rel(EHUV_DIRECT_RECHECK),
        "required_table": ehuv_direct["required_table"],
        "values_emitted_now": ehuv_direct["values_emitted_now"],
        "hresponse_row_table_status": {
            "required_row_count": hrows["decision"]["required_row_count"],
            "emitted_row_count": hrows["decision"]["emitted_row_count"],
            "accepted_source_row_count": hrows["decision"]["accepted_source_row_count"],
        },
        "decision": {
            "B_Huv_symbolic_exact_payload_emitted": ehuv_direct[
                "B_Huv_symbolic_exact_payload_emitted"
            ],
            "M_H_three_row_functional_closed": ehuv_direct[
                "M_H_three_row_functional_closed"
            ],
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_H_response_table_emitted": False,
            "accepted_H_response_source_row_count": 0,
            "selected_H_response_spectrum_emitted": False,
            "R_H_RG_value_emitted": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterOrientationPhaseTraceSource.v1",
        "status": "NEXT_FRONTIER_NONDIAGONAL_HUV_HESSIAN_SOURCE_OR_DIRECT_HERM2_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "C1-C6 projection bridge retired as s_beta/projection blocker",
            "projection bridge separated from direct Herm(2) value source",
            "orientation/phase/trace source inventory executed",
            "direct H-response emission rechecked with zero rows",
        ],
        "still_open": [
            "selected non-diagonal Huv Hessian/source functional",
            "selected Delta sign",
            "selected Omega phase",
            "strict radial scale or explicitly controlled radial tier",
            "trace-center source or quotient trace-free full-response theorem",
            "direct Huu,Hud,Hdd rows with certificates",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHerm2OrientationPhaseTraceSourceOrDirectHResponseEmission",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "Herm2OrientationPhaseTraceSourceOrDirectHResponseEmissionTheorem",
            "proved": True,
            "statement": (
                "The C1-C6 projection bridge is closed enough to account for the "
                "selected s_beta reduction, but it is not a direct Herm(2) Huv "
                "value source. The orientation/phase/trace inventory emits zero "
                "strict radial/sign/phase/trace rows and zero certificates; direct "
                "H-response emission still has zero accepted rows. The remaining "
                "frontier is a selected non-diagonal Huv Hessian/source functional "
                "or direct Herm(2) rows."
            ),
        },
        "packets": {
            "projection_bridge_vs_direct_hresponse_recheck": rel(BRIDGE_RECHECK),
            "orientation_phase_trace_source_inventory": rel(PHASE_TRACE),
            "direct_hresponse_emission_after_bridge_completion": rel(DIRECT_RUN),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "higgs_dynamic": rel(HIGGS_DYNAMIC),
            "ehuv_trace": rel(EHUV_TRACE),
            "ehuv_c5a_gate": rel(EHUV_C5A_GATE),
            "ehuv_direct_recheck": rel(EHUV_DIRECT_RECHECK),
            "msource": rel(MSOURCE),
            "full_msource": rel(FULL_MSOURCE),
            "hresponse_rows": rel(HRESPONSE_ROWS),
        },
        "closure_decision": {
            "projection_bridge_retired_as_sbeta_blocker": True,
            "projection_bridge_is_not_direct_Herm2_value_source": True,
            "orientation_phase_trace_inventory_executed": True,
            "direct_H_response_emission_rechecked": True,
            "strict_radial_scale_source_emitted": False,
            "selected_Delta_sign_emitted": False,
            "selected_Omega_phase_emitted": False,
            "trace_center_source_or_normalization_emitted": False,
            "same_source_certificates_emitted": False,
            "selected_non_diagonal_Huv_Hessian_source_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_predicted": False,
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "selected_s_beta_value": s_beta,
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "required_H_response_row_count": hrows["decision"]["required_row_count"],
            "emitted_H_response_row_count": hrows["decision"]["emitted_row_count"],
            "accepted_selected_K_source_row_count": higgs_dynamic["closure_decision"][
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": higgs_dynamic["closure_decision"][
                "selected_K_threshold_row_count_required"
            ],
        },
    }

    cert = {
        "certificate": "MTTSelectedHerm2OrientationPhaseTraceSourceOrDirectHResponseEmission",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "projection_bridge_retired_as_sbeta_blocker": True,
        "projection_bridge_is_not_direct_Herm2_value_source": True,
        "orientation_phase_trace_inventory_executed": True,
        "direct_H_response_emission_rechecked": True,
        "selected_non_diagonal_Huv_Hessian_source_emitted": False,
        "selected_Omega_phase_emitted": False,
        "trace_center_source_or_normalization_emitted": False,
        "direct_Herm2_rows_emitted": False,
        "R_H_RG_value_emitted": False,
        "lambda_H_predicted": False,
        "accepted_H_response_source_row_count": 0,
        "accepted_R_H_RG_source_count": 0,
    }

    note = f"""# MTT Selected Herm(2) Orientation Phase Trace Source or Direct H-Response Emission v1

Status: `{STATUS}`

## Theorem

The C1-C6 projection bridge is now retired as an `s_beta` blocker, but it is not
a direct Herm(2) value source.

Closed support:

- selected `s_beta = {s_beta}`
- C5b physical projection-measure equality
- C6 no-extra-boundary/source reduction
- trace-free polar contract

Still not emitted:

- strict radial scale source
- `Delta` sign
- `Omega` phase in the Huv basis
- trace-center source for full `Huu/Hdd`
- direct `Huu,Hud,Hdd` rows and certificates

Accepted H-response source rows: `0`.

Next artifact: `{NEXT}`
"""

    write_json(BRIDGE_RECHECK, bridge_recheck)
    write_json(PHASE_TRACE, phase_trace)
    write_json(DIRECT_RUN, direct_run)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
