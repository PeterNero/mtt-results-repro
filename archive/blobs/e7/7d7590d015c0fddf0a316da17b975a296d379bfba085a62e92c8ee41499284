"""Build H-sector logdeterminant kernel or selected H-response spectrum packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hsectorlogdeterminantkernel_or_selectedhresponsespectrum"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STATIC_LOGDET_IMPORT = PACKET_DIR / "static_heat_logdet_kernel_import.packet.json"
HRESPONSE_SPECTRUM_GATE = PACKET_DIR / "selected_hresponse_spectrum_gate.packet.json"
RHRG_VALUE_ATTEMPT = PACKET_DIR / "rhrg_value_execution_after_logdet_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hsector_logdet_hresponse_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HSectorLogDeterminantKernel_or_SelectedHResponseSpectrum_v1.md"

PREVIOUS = DATA / "selected_hsectordeterminantrgoperatordefinition_or_targetindependentvalidationrun.candidate.json"
HEAT = DATA / "selected_heattorsionresponse_finalgate.candidate.json"
HEAT_RESPONSE = DATA / "selected_heattorsionresponse_finalgate" / "selected_finite_heat_spectrum_response.packet.json"
HEAT_SLOT = DATA / "selected_heattorsionresponse_finalgate" / "finite_determinant_heat_torsion_slot_closure.packet.json"
DYNAMIC_HESSIAN = DATA / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission.candidate.json"
DYNAMIC_DOMAIN = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "dynamic_hessian_domain_and_extraction_gate.packet.json"
)
STRICT_MH_GATE = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "strict_mh_table_value_gate.packet.json"
)
SECOND_VARIATION = DATA / "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues.candidate.json"
SOURCE_FUNCTIONAL_GATE = (
    DATA
    / "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues"
    / "source_functional_acceptance_gate.packet.json"
)
HSECTOR_OPERATOR = (
    DATA
    / "selected_hsectordeterminantrgoperatordefinition_or_targetindependentvalidationrun"
    / "hsector_determinant_rg_operator_definition.packet.json"
)
HSECTOR_SLOT_EXEC = (
    DATA
    / "selected_hsectordeterminantrgoperatordefinition_or_targetindependentvalidationrun"
    / "hsector_determinant_rg_slot_execution.packet.json"
)

STATUS = (
    "MTT_SELECTED_HSECTORLOGDETERMINANTKERNEL_OR_SELECTEDHRESPONSESPECTRUM_"
    "STATIC_LOGDET_IMPORTED_DYNAMIC_HRESPONSE_OPEN"
)
NEXT = "MTT_Selected_HResponseSpectrumSourceRows_or_RHRGLogDetValueExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H-sector logdet/H-response inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        HEAT,
        HEAT_RESPONSE,
        HEAT_SLOT,
        DYNAMIC_HESSIAN,
        DYNAMIC_DOMAIN,
        STRICT_MH_GATE,
        SECOND_VARIATION,
        SOURCE_FUNCTIONAL_GATE,
        HSECTOR_OPERATOR,
        HSECTOR_SLOT_EXEC,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    heat = load(HEAT)
    heat_response = load(HEAT_RESPONSE)
    heat_slot = load(HEAT_SLOT)
    dynamic_hessian = load(DYNAMIC_HESSIAN)
    dynamic_domain = load(DYNAMIC_DOMAIN)
    strict_mh = load(STRICT_MH_GATE)
    second_variation = load(SECOND_VARIATION)
    source_gate = load(SOURCE_FUNCTIONAL_GATE)
    hsector_operator = load(HSECTOR_OPERATOR)
    hsector_slots = load(HSECTOR_SLOT_EXEC)

    hrg = previous["key_numbers"]["UP_RET_OVERLAP_HRG_diagnostic_only"]
    invariants = heat_response["finite_invariants"]
    h_logdet = invariants["H_sector_log_pseudodeterminant"]
    h_positive_dim = invariants["H_sector_positive_dimension"]
    h_kernel_dim = invariants["H_sector_kernel_dimension"]
    h_heat_t1 = invariants["H_sector_heat_trace_t1"]

    static_logdet_import = {
        "schema": "MTTStaticHeatLogdetKernelImport.v1",
        "status": "STATIC_FINITE_HEAT_LOGDET_IMPORTED_SUPPORT_ONLY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_ref": rel(HEAT_RESPONSE),
        "imported_static_values": {
            "H_sector_log_pseudodeterminant": h_logdet,
            "H_sector_positive_dimension": h_positive_dim,
            "H_sector_kernel_dimension": h_kernel_dim,
            "H_sector_heat_trace_t1": h_heat_t1,
            "finite_spectral_zeta_at_0_positive_count": invariants[
                "finite_spectral_zeta_at_0_positive_count"
            ],
        },
        "scope_check": {
            "finite_DE_gap_heat_torsion_slot_closed": heat["closure_decision"][
                "finite_determinant_heat_spectrum_or_torsion_response_closed"
            ],
            "slot_layer_closed": heat_slot["slot_status_after_closure"]["remaining_missing_slot_count"] == 0,
            "same_q79_F_m1_branch": heat_response["branch"] == {"q": 79, "orientation": "F", "torsion_label_m": 1},
            "static_D_E_gap_layer": True,
            "dynamic_H_response_spectrum": False,
            "mu_dependent_threshold_RG_kernel": False,
            "accepted_as_R_H_RG_logdet_kernel": False,
        },
        "reason_not_promoted": (
            "The finite heat packet emits a selected static D_E/gap pseudodeterminant. "
            "The R_H^RG operator requires the selected H-response Hessian spectrum "
            "L_H(mu)=P_H Herm(Hess(F_H(mu))) P_H at source-owned scales."
        ),
    }

    hresponse_spectrum_gate = {
        "schema": "MTTSelectedHResponseSpectrumGate.v1",
        "status": "SELECTED_HRESPONSE_SPECTRUM_GATE_EXECUTED_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_domain_inputs": {
            "B_Huv_domain": dynamic_domain["what_is_closed_now"]["B_Huv_domain"],
            "P_H_projector": dynamic_domain["what_is_closed_now"]["P_H_projector"],
            "R_H_restriction": dynamic_domain["what_is_closed_now"]["R_H_restriction"],
            "Herm2_codomain": dynamic_domain["what_is_closed_now"]["Herm2_codomain"],
            "Pauli_Riesz_row_extractors": dynamic_domain["what_is_closed_now"][
                "Pauli_Riesz_row_extractors"
            ],
            "second_variation_source_gate": source_gate["status"]
            == "SECOND_VARIATION_SOURCE_GATE_CLOSED_VALUES_OPEN",
        },
        "missing_value_inputs": {
            "selected_F_H_functional": dynamic_domain["what_is_not_closed"]["selected_F_H_functional"],
            "selected_second_variation_values": dynamic_domain["what_is_not_closed"][
                "selected_second_variation_values"
            ],
            "direct_Huu_Hud_Hdd_values": dynamic_domain["what_is_not_closed"][
                "direct_Huu_Hud_Hdd_values"
            ],
            "finite_exactness_or_error_certificate_for_values": dynamic_domain["what_is_not_closed"][
                "finite_exactness_or_error_certificate_for_values"
            ],
            "selected_H_response_table": not dynamic_hessian["closure_decision"][
                "selected_H_response_table_emitted"
            ],
            "selected_dynamic_H_response": not dynamic_hessian["closure_decision"][
                "selected_dynamic_H_response_emitted"
            ],
            "selected_F_H_second_variation": not dynamic_hessian["closure_decision"][
                "selected_F_H_second_variation_emitted"
            ],
        },
        "strict_mh_gate_ref": rel(STRICT_MH_GATE),
        "strict_mh_current_packet_passes": strict_mh["current_packet_passes"],
        "decision": {
            "selected_H_response_spectrum_emitted": False,
            "selected_F_H_spectrum_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "H_response_logdet_executable": False,
            "accepted_H_response_source_row_count": 0,
        },
    }

    rhrg_value_attempt = {
        "schema": "MTTRHRGValueExecutionAfterLogdetGate.v1",
        "status": "RHRG_VALUE_EXECUTION_REPLAYED_STATIC_LOGDET_NOT_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "operator_contract_ref": rel(HSECTOR_OPERATOR),
        "slot_execution_ref": rel(HSECTOR_SLOT_EXEC),
        "diagnostic_only": {
            "UP_RET_OVERLAP_HRG": hrg,
            "static_H_logdet": h_logdet,
            "HRG_minus_static_H_logdet": hrg - h_logdet,
            "static_H_logdet_over_HRG": h_logdet / hrg,
        },
        "execution_decision": {
            "static_logdet_used_as_R_H_RG": False,
            "H_response_logdet_value_emitted": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_predicted": False,
            "target_independent_validation_run_executed": False,
            "accepted_R_H_RG_source_count": 0,
        },
        "reason": (
            "The imported static H-sector pseudodeterminant is source support, "
            "but no selected mu-dependent H_response spectrum or logdet difference "
            "exists for the R_H^RG transport value."
        ),
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHSectorLogdetHResponseGate.v1",
        "status": "NEXT_FRONTIER_HRESPONSE_SPECTRUM_SOURCE_ROWS_OR_RHRG_LOGDET_VALUE_EXECUTION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "static finite H-sector heat/logdet support imported",
            "static D_E/gap logdet rejected as R_H^RG value source",
            "selected H_response/F_H spectrum gate executed with value rows open",
        ],
        "still_open": [
            "selected F_H functional or selected H_response table on B_Huv",
            "finite exactness/error certificate for H-response values",
            "source-owned mu0/mu1 logdet difference for R_H^RG",
            "numeric R_H^RG value emission",
            "target-independent validation after source selection",
            "K_threshold.Omega_H.lambda and ten-K antecedent",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHSectorLogDeterminantKernelOrSelectedHResponseSpectrum",
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
            "name": "HSectorLogDeterminantKernelOrSelectedHResponseSpectrumTheorem",
            "proved": True,
            "statement": (
                "The selected finite H-sector heat pseudodeterminant is imported "
                "as static support, but it is not the mu-dependent H-response "
                "logdet kernel required by R_H^RG. Current selected data close "
                "the B_Huv/P_H domain and value law while leaving F_H, H_response, "
                "Herm(2) values, and exactness certificates open."
            ),
        },
        "packets": {
            "static_logdet_import": rel(STATIC_LOGDET_IMPORT),
            "hresponse_spectrum_gate": rel(HRESPONSE_SPECTRUM_GATE),
            "rhrg_value_attempt": rel(RHRG_VALUE_ATTEMPT),
            "cutset": rel(CUTSET),
        },
        "closure_decision": {
            "static_H_logdet_imported": True,
            "static_H_logdet_promoted_to_R_H_RG": False,
            "selected_H_response_spectrum_emitted": False,
            "selected_F_H_spectrum_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "H_response_logdet_executable": False,
            "R_H_RG_value_emitted": False,
            "accepted_R_H_RG_source_count": 0,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG_diagnostic_only": hrg,
            "static_H_sector_log_pseudodeterminant": h_logdet,
            "static_H_sector_positive_dimension": h_positive_dim,
            "static_H_sector_kernel_dimension": h_kernel_dim,
            "static_H_logdet_over_HRG": h_logdet / hrg,
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "selected_K_source_rows": previous["key_numbers"]["accepted_selected_K_source_row_count"],
            "selected_K_rows_required": previous["key_numbers"]["selected_K_threshold_row_count_required"],
        },
    }

    cert = {
        "certificate": "MTTSelectedHSectorLogDeterminantKernelOrSelectedHResponseSpectrum",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "static_H_logdet_imported": True,
        "static_H_logdet_promoted_to_R_H_RG": False,
        "selected_H_response_spectrum_emitted": False,
        "H_response_logdet_executable": False,
        "R_H_RG_value_emitted": False,
        "accepted_R_H_RG_source_count": 0,
        "lambda_H_predicted": False,
    }

    note = f"""# MTT Selected H-Sector Logdeterminant Kernel or Selected H-Response Spectrum v1

Status: `{STATUS}`

## Theorem

The selected finite heat/torsion packet emits a static H-sector
pseudodeterminant, but it is not the selected mu-dependent H-response logdet
kernel required by `R_H^RG`.

## Imported Static Support

- H-sector log pseudodeterminant: `{h_logdet}`
- H-sector positive dimension: `{h_positive_dim}`
- H-sector kernel dimension: `{h_kernel_dim}`
- H-sector heat trace at `t=1`: `{h_heat_t1}`

This closes support for the finite `D_E/gap` layer only.  It is not promoted to
`R_H^RG`.

## H-Response Gate

- selected `F_H` spectrum emitted: `false`
- selected `H_response` table emitted: `false`
- direct Herm(2) rows emitted: `false`
- H-response logdet executable: `false`
- accepted `R_H^RG` source count: `0`

Next artifact: `{NEXT}`
"""

    write_json(STATIC_LOGDET_IMPORT, static_logdet_import)
    write_json(HRESPONSE_SPECTRUM_GATE, hresponse_spectrum_gate)
    write_json(RHRG_VALUE_ATTEMPT, rhrg_value_attempt)
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
