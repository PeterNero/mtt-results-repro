"""Build common-scale Jacobian or Rtheta threshold response execution artifact."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_commonscalejacobian_or_rthetathresholdresponseexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ALGEBRAIC = PACKET_DIR / "bct_mz_mass_to_yukawa_v_jacobian.packet.json"
MZMT_GAP = PACKET_DIR / "mz_to_mt_common_scale_jacobian_gap.packet.json"
RTHETA = PACKET_DIR / "rtheta_threshold_response_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_common_scale_jacobian.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CommonScaleJacobian_or_RThetaThresholdResponseExecution_v1.md"

PREVIOUS = DATA / "selected_crossblockcovariancevalues_or_rthetacoefficientexecution.candidate.json"
PREVIOUS_CUTSET = (
    DATA
    / "selected_crossblockcovariancevalues_or_rthetacoefficientexecution"
    / "next_cutset_after_interim_covariance_values.packet.json"
)
BCT_ASSEMBLY = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "all_bct_external_rows_assembly.packet.json"
)
BCT_MATRIX = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "huang_zhou_eft_fullsm_reconciliation_matrix.packet.json"
)
REFERENCE = DATA / "sm_equivalence_reference_data_values_fill.candidate.json"
COMMON_SCALE = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
TRANSPORT_KERNEL = (
    DATA
    / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
    / "yukawa_higgs_common_scale_transport_kernel.packet.json"
)
RTHETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
RTHETA_PREVIOUS = (
    DATA
    / "selected_crossblockcovariancevalues_or_rthetacoefficientexecution"
    / "rtheta_coefficient_execution_gate.packet.json"
)

STATUS = (
    "MTT_SELECTED_COMMONSCALEJACOBIAN_OR_RTHETATHRESHOLDRESPONSEEXECUTION_"
    "BUILT_BCT_YUKAWA_JACOBIAN_MZMT_RTHETA_OPEN"
)
NEXT = "MTT_Selected_MZtoMtJacobianExecution_or_SelectedThresholdResponseFunctionalFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing common-scale Jacobian sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_CUTSET,
        BCT_ASSEMBLY,
        BCT_MATRIX,
        REFERENCE,
        COMMON_SCALE,
        TRANSPORT_KERNEL,
        RTHETA_CONTRACT,
        RTHETA_PREVIOUS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    bct_assembly = load(BCT_ASSEMBLY)
    bct_matrix = load(BCT_MATRIX)
    reference = load(REFERENCE)
    common_scale = load(COMMON_SCALE)
    transport_kernel = load(TRANSPORT_KERNEL)
    rtheta_contract = load(RTHETA_CONTRACT)
    rtheta_previous = load(RTHETA_PREVIOUS)

    v = reference["reference_values"]["constants"]["v_from_G_F"]["central_value"]
    v_sigma = reference["reference_values"]["constants"]["v_from_G_F"]["uncertainty"]["plus"]
    sqrt2 = math.sqrt(2.0)
    bct_rows = []
    for row in bct_assembly["rows"]:
        row_id = row["id"]
        mass = row["running_mass_MZ_GeV"]
        table_sigma = bct_matrix["matrix_rows"][row_id]["EFT_QCDxQED_5q3l_MZ"]["table_uncertainty_GeV"]
        yukawa = sqrt2 * mass / v
        bct_rows.append(
            {
                "id": row_id,
                "target_yukawa_row": {
                    "bottom_MSbar_native_scale_transport": "y_b_MZ_from_BCT",
                    "charm_MSbar_native_scale_transport": "y_c_MZ_from_BCT",
                    "tau_pole_rest_to_running_lepton": "y_tau_MZ_from_BCT",
                }[row_id],
                "mass_MZ_GeV": mass,
                "mass_sigma_GeV": table_sigma,
                "v_GeV": v,
                "v_sigma_GeV": v_sigma,
                "yukawa_MZ": yukawa,
                "dy_dm": sqrt2 / v,
                "dy_dv": -sqrt2 * mass / (v * v),
                "variance_from_mass": (sqrt2 / v * table_sigma) ** 2,
                "variance_from_v": ((sqrt2 * mass / (v * v)) * v_sigma) ** 2,
                "accepted_as_algebraic_common_scale_jacobian_row": True,
                "accepted_as_MZ_to_Mt_RG_jacobian_row": False,
                "accepted_as_Rtheta_source_row": False,
            }
        )

    algebraic_packet = {
        "schema": "MTTBCTMZMassToYukawaVJacobian.v1",
        "status": "BCT_MZ_MASS_TO_YUKAWA_V_JACOBIAN_BUILT_MZ_TO_MT_OPEN",
        "formula": "y_f(M_Z)=sqrt(2)*m_f(M_Z)/v",
        "bct_source": rel(BCT_ASSEMBLY),
        "reference_source": rel(REFERENCE),
        "row_jacobians": bct_rows,
        "jacobian_domain": ["m_b(M_Z)", "m_c(M_Z)", "m_tau(M_Z)", "v_from_G_F"],
        "jacobian_codomain": ["y_b(M_Z)", "y_c(M_Z)", "y_tau(M_Z)"],
        "matrix_shape": [3, 4],
        "matrix_rows": [
            [row["dy_dm"] if i == j else (row["dy_dv"] if j == 3 else 0.0) for j in range(4)]
            for i, row in enumerate(bct_rows)
        ],
        "closes_common_scale_algebraic_yukawa_map": True,
        "closes_MZ_to_Mt_RG_transport_jacobian": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ALGEBRAIC, algebraic_packet)

    mzmt_gap = {
        "schema": "MTTMZToMtCommonScaleJacobianGap.v1",
        "status": "ALGEBRAIC_MZ_YUKAWA_JACOBIAN_BUILT_MZ_TO_MT_RG_JACOBIAN_OPEN",
        "algebraic_jacobian_source": rel(ALGEBRAIC),
        "common_scale_value_source": rel(COMMON_SCALE),
        "transport_kernel_source": rel(TRANSPORT_KERNEL),
        "common_scale_values_status": common_scale["status"],
        "transport_kernel_status": transport_kernel["status"],
        "accepted_common_scale_values_for_profile_input": common_scale["accepted_for_profile_execution_input"],
        "accepted_for_true_precision_equivalence": common_scale["accepted_for_true_precision_equivalence"],
        "why_MZ_to_Mt_jacobian_still_open": [
            "available common-scale values are M_Z first-pass SM-parity inputs, not true precision transport",
            "transport kernel explicitly says values were not emitted in that earlier kernel spec",
            "M_Z-to-M_t Yukawa/Higgs RG Jacobian needs selected loop order, thresholds, and mass-scheme policy",
            "BCT-to-weak/Higgs cross-block covariance requires derivatives through the common-scale transport, not only y=sqrt(2)m/v",
        ],
        "closes_common_scale_convention_map": False,
        "closes_common_scale_MZ_to_Mt_jacobian": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(MZMT_GAP, mzmt_gap)

    rtheta_packet = {
        "schema": "MTTRThetaThresholdResponseExecutionGate.v1",
        "status": "RTHETA_THRESHOLD_RESPONSE_EXECUTION_RECHECKED_CONTRACT_ONLY",
        "contract_source": rel(RTHETA_CONTRACT),
        "previous_rtheta_gate_source": rel(RTHETA_PREVIOUS),
        "functional_symbol": rtheta_contract["functional_symbol"],
        "contract_emitted": rtheta_contract["closure_claimed"],
        "acceptance_equations_available": rtheta_contract["acceptance_equations"],
        "row_outputs_required": rtheta_contract["row_outputs_required"],
        "algebraic_jacobian_can_validate_future_Rtheta": True,
        "algebraic_jacobian_selects_Rtheta": False,
        "Rtheta_coefficient_values_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "selected_Rtheta_source_rows_closed": False,
        "accepted_Rtheta_source_row_count": rtheta_previous["accepted_Rtheta_source_row_count"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA, rtheta_packet)

    cutset = {
        "schema": "MTTNextCutsetAfterCommonScaleJacobian.v1",
        "status": "NEXT_ATTACK_MZ_TO_MT_JACOBIAN_OR_SELECTED_THRESHOLD_RESPONSE_FILL",
        "previous_cutset_source": rel(PREVIOUS_CUTSET),
        "closed_now": {
            "BCT_MZ_mass_to_yukawa_v_jacobian": True,
            "common_scale_algebraic_yukawa_map": True,
            "Rtheta_threshold_response_contract_rechecked": True,
        },
        "still_open": {
            "MZ_to_Mt_common_scale_RG_jacobian": True,
            "common_scale_convention_map_for_precision": True,
            "numeric_cross_block_covariance_values": True,
            "Rtheta_coefficient_values": True,
            "selected_threshold_response_functional": True,
            "selected_Rtheta_source_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "differentiate the accepted first-pass RG transport kernel or rebuild a selected MZ-to-Mt transport Jacobian",
            "route_B": "execute selected threshold response coefficients for threshold::W_Z_H and BCT mass-scheme rows",
            "route_C": "emit first nonzero cross-block covariance entries using the algebraic BCT-yukawa-v Jacobian plus shared v/G_F covariance",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedCommonScaleJacobianOrRThetaThresholdResponseExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "bct_mz_mass_to_yukawa_v_jacobian": rel(ALGEBRAIC),
            "mz_to_mt_common_scale_jacobian_gap": rel(MZMT_GAP),
            "rtheta_threshold_response_execution_gate": rel(RTHETA),
            "next_cutset_after_common_scale_jacobian": rel(CUTSET),
        },
        "theorem": {
            "name": "BCTCommonScaleAlgebraicJacobianTheorem",
            "proved": True,
            "statement": (
                "The BCT M_Z mass rows determine an exact algebraic common-scale Jacobian to M_Z "
                "Yukawa coordinates through y=sqrt(2)m/v, including v(G_F) dependence. This closes "
                "the algebraic BCT-to-yukawa common-scale map, but not the M_Z-to-M_t RG/threshold "
                "Jacobian, selected Rtheta threshold response, full cross-block covariance, true SM "
                "equivalence, or no-knob closure."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "BCT_MZ_mass_to_yukawa_v_jacobian_closed": True,
            "MZ_to_Mt_common_scale_RG_jacobian_closed": False,
            "numeric_cross_block_covariance_values_closed": False,
            "Rtheta_coefficient_values_closed": False,
            "selected_threshold_response_functional_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "previous_status": previous["status"],
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_CommonScaleJacobian_or_RThetaThresholdResponseExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "BCT_MZ_mass_to_yukawa_v_jacobian_closed": True,
        "MZ_to_Mt_common_scale_RG_jacobian_closed": False,
        "Rtheta_coefficient_values_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected CommonScaleJacobian or RThetaThresholdResponseExecution v1

Status: `{STATUS}`.

This artifact closes the exact algebraic `M_Z` BCT mass-to-Yukawa Jacobian:
`y_f(M_Z)=sqrt(2)m_f(M_Z)/v`.

```text
BCT M_Z mass-to-yukawa Jacobian : true
M_Z -> M_t RG Jacobian           : false
R_theta coefficient values       : false
full covariance/profile          : false
true SM equivalence              : false
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
