"""Build H-response spectrum source rows or R_H^RG logdet value execution packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROW_TABLE = PACKET_DIR / "hresponse_source_row_execution_table.packet.json"
SPECTRUM_PACKET = PACKET_DIR / "hresponse_spectrum_from_rows_attempt.packet.json"
RHRG_PACKET = PACKET_DIR / "rhrg_logdet_value_execution_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hresponse_source_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HResponseSpectrumSourceRows_or_RHRGLogDetValueExecution_v1.md"

PREVIOUS = DATA / "selected_hsectorlogdeterminantkernel_or_selectedhresponsespectrum.candidate.json"
HRESPONSE_GATE = (
    DATA
    / "selected_hsectorlogdeterminantkernel_or_selectedhresponsespectrum"
    / "selected_hresponse_spectrum_gate.packet.json"
)
RHRG_PREVIOUS = (
    DATA
    / "selected_hsectorlogdeterminantkernel_or_selectedhresponsespectrum"
    / "rhrg_value_execution_after_logdet_gate.packet.json"
)
STRICT_MH_GATE = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "strict_mh_table_value_gate.packet.json"
)
SOURCE_FUNCTIONAL_GATE = (
    DATA
    / "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues"
    / "source_functional_acceptance_gate.packet.json"
)
MH_THREE_ROW = DATA / "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution.candidate.json"
DYNAMIC_HESSIAN = DATA / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission.candidate.json"
HSECTOR_OPERATOR = (
    DATA
    / "selected_hsectordeterminantrgoperatordefinition_or_targetindependentvalidationrun"
    / "hsector_determinant_rg_operator_definition.packet.json"
)

STATUS = (
    "MTT_SELECTED_HRESPONSESPECTRUMSOURCEROWS_OR_RHRGLOGDETVALUEEXECUTION_"
    "ROW_TABLE_EXECUTED_ZERO_ACCEPTED_ROWS"
)
NEXT = "MTT_Selected_HResponseValueSourceFunctional_or_DirectHerm2Rows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H-response row inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        HRESPONSE_GATE,
        RHRG_PREVIOUS,
        STRICT_MH_GATE,
        SOURCE_FUNCTIONAL_GATE,
        MH_THREE_ROW,
        DYNAMIC_HESSIAN,
        HSECTOR_OPERATOR,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    hresponse_gate = load(HRESPONSE_GATE)
    rhrg_previous = load(RHRG_PREVIOUS)
    strict_mh = load(STRICT_MH_GATE)
    source_gate = load(SOURCE_FUNCTIONAL_GATE)
    mh_three_row = load(MH_THREE_ROW)
    dynamic_hessian = load(DYNAMIC_HESSIAN)
    hsector_operator = load(HSECTOR_OPERATOR)

    hrg = previous["key_numbers"]["UP_RET_OVERLAP_HRG_diagnostic_only"]
    static_logdet = previous["key_numbers"]["static_H_sector_log_pseudodeterminant"]
    required = strict_mh["required_values"]

    source_rows = [
        {
            "row_id": "Huu",
            "required_value": required["Huu"],
            "certificate_required": "source_ownership_certificate",
            "emitted": required["Huu"] is not None,
            "accepted": False,
        },
        {
            "row_id": "Hud_re",
            "required_value": required["Hud_re"],
            "certificate_required": "Hdu_equals_conj_Hud_certificate",
            "emitted": required["Hud_re"] is not None,
            "accepted": False,
        },
        {
            "row_id": "Hud_im",
            "required_value": required["Hud_im"],
            "certificate_required": "Hdu_equals_conj_Hud_certificate",
            "emitted": required["Hud_im"] is not None,
            "accepted": False,
        },
        {
            "row_id": "Hdd",
            "required_value": required["Hdd"],
            "certificate_required": "source_ownership_certificate",
            "emitted": required["Hdd"] is not None,
            "accepted": False,
        },
        {
            "row_id": "source_ownership_certificate",
            "required_value": required["source_ownership_certificate"],
            "certificate_required": None,
            "emitted": required["source_ownership_certificate"] is not None,
            "accepted": False,
        },
        {
            "row_id": "same_source_exactness_or_error_certificate",
            "required_value": required["same_source_exactness_or_error_certificate"],
            "certificate_required": None,
            "emitted": required["same_source_exactness_or_error_certificate"] is not None,
            "accepted": False,
        },
        {
            "row_id": "quotient_admissibility_certificate",
            "required_value": required["quotient_admissibility_certificate"],
            "certificate_required": None,
            "emitted": required["quotient_admissibility_certificate"] is not None,
            "accepted": False,
        },
    ]

    row_table = {
        "schema": "MTTHResponseSourceRowExecutionTable.v1",
        "status": "HRESPONSE_SOURCE_ROW_TABLE_EXECUTED_ZERO_ACCEPTED_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "domain_closed": strict_mh["domain_closed"],
        "acceptance_tests": strict_mh["acceptance_tests"],
        "source_rows": source_rows,
        "support_imports": {
            "MH_three_row_source_functional_contract_closed": mh_three_row["closure_decision"][
                "MH_three_row_source_functional_contract_closed"
            ],
            "second_variation_source_gate_closed": source_gate["status"]
            == "SECOND_VARIATION_SOURCE_GATE_CLOSED_VALUES_OPEN",
            "dynamic_Hessian_domain_closed": dynamic_hessian["closure_decision"][
                "dynamic_Hessian_domain_on_BHuv_closed"
            ],
            "strict_mh_current_packet_passes": strict_mh["current_packet_passes"],
        },
        "decision": {
            "required_row_count": len(source_rows),
            "emitted_row_count": sum(1 for row in source_rows if row["emitted"]),
            "accepted_source_row_count": 0,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "source_ownership_certificate_emitted": False,
            "same_source_exactness_or_error_certificate_emitted": False,
        },
    }

    spectrum_packet = {
        "schema": "MTTHResponseSpectrumFromRowsAttempt.v1",
        "status": "HRESPONSE_SPECTRUM_FROM_ROWS_NOT_EXECUTABLE_ZERO_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "formula": {
            "Herm2_matrix": "[[Huu, Hud_re+i Hud_im], [Hud_re-i Hud_im, Hdd]]",
            "spectrum": "eigenvalues of Herm2_matrix after same-source exactness certificate",
            "logdet": "sum(log positive eigenvalues) after zero-mode/positivity policy",
        },
        "execution_inputs": {
            "accepted_source_row_count": 0,
            "required_numeric_rows": ["Huu", "Hud_re", "Hud_im", "Hdd"],
            "required_certificates": [
                "Hdu_equals_conj_Hud_certificate",
                "source_ownership_certificate",
                "same_source_exactness_or_error_certificate",
                "quotient_admissibility_certificate",
            ],
        },
        "decision": {
            "selected_H_response_spectrum_emitted": False,
            "selected_logdet_from_H_response_emitted": False,
            "positive_spectrum_certificate_emitted": False,
            "H_response_logdet_executable": False,
        },
    }

    rhrg_packet = {
        "schema": "MTTRHRGLogdetValueExecutionAttempt.v1",
        "status": "RHRG_LOGDET_VALUE_EXECUTION_NOT_RUN_HRESPONSE_ROWS_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "operator_contract_ref": rel(HSECTOR_OPERATOR),
        "diagnostic_values_not_used_as_source": {
            "UP_RET_OVERLAP_HRG": hrg,
            "static_H_logdet": static_logdet,
            "previous_static_logdet_used_as_R_H_RG": rhrg_previous["execution_decision"][
                "static_logdet_used_as_R_H_RG"
            ],
        },
        "blocked_by": [
            "zero accepted H-response source rows",
            "no selected H-response spectrum",
            "no selected mu0/mu1 logdet difference",
            "no selected source-owned threshold/RG index term",
        ],
        "decision": {
            "R_H_RG_value_emitted": False,
            "R_H_RG_logdet_value_executed": False,
            "accepted_R_H_RG_source_count": 0,
            "lambda_H_predicted": False,
            "target_independent_validation_run_executed": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHResponseSourceRows.v1",
        "status": "NEXT_FRONTIER_HRESPONSE_VALUE_SOURCE_FUNCTIONAL_OR_DIRECT_HERM2_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "H-response source row table executed",
            "minimal direct Herm(2) row/certificate set fixed",
            "R_H^RG logdet execution blocked by zero accepted source rows",
        ],
        "still_open": [
            "selected finite H-sector functional F_H",
            "direct source-owned Herm(2) rows Huu,Hud,Hdd",
            "source ownership and exactness/error certificates",
            "selected H-response spectrum/logdet",
            "numeric R_H^RG value execution",
            "K_threshold.Omega_H.lambda and ten-K antecedent",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHResponseSpectrumSourceRowsOrRHRGLogDetValueExecution",
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
            "name": "HResponseSpectrumSourceRowsOrRHRGLogDetValueExecutionTheorem",
            "proved": True,
            "statement": (
                "The minimal selected H-response row table is now explicit. "
                "Current support closes the B_Huv/P_H domain and source-functional "
                "contract, but emits zero H-response numeric rows and zero value "
                "certificates; therefore no selected spectrum, logdet, or R_H^RG "
                "value can be executed."
            ),
        },
        "packets": {
            "row_table": rel(ROW_TABLE),
            "spectrum_packet": rel(SPECTRUM_PACKET),
            "rhrg_packet": rel(RHRG_PACKET),
            "cutset": rel(CUTSET),
        },
        "closure_decision": {
            "hresponse_source_row_table_executed": True,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "selected_logdet_from_H_response_emitted": False,
            "R_H_RG_logdet_value_executed": False,
            "R_H_RG_value_emitted": False,
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "required_H_response_row_count": len(source_rows),
            "emitted_H_response_row_count": sum(1 for row in source_rows if row["emitted"]),
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "UP_RET_OVERLAP_HRG_diagnostic_only": hrg,
            "static_H_logdet_support": static_logdet,
            "selected_K_source_rows": previous["key_numbers"]["selected_K_source_rows"],
            "selected_K_rows_required": previous["key_numbers"]["selected_K_rows_required"],
        },
    }

    cert = {
        "certificate": "MTTSelectedHResponseSpectrumSourceRowsOrRHRGLogDetValueExecution",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "hresponse_source_row_table_executed": True,
        "direct_Herm2_rows_emitted": False,
        "selected_H_response_spectrum_emitted": False,
        "R_H_RG_logdet_value_executed": False,
        "R_H_RG_value_emitted": False,
        "accepted_H_response_source_row_count": 0,
        "accepted_R_H_RG_source_count": 0,
        "lambda_H_predicted": False,
    }

    note = f"""# MTT Selected H-Response Spectrum Source Rows or R_H^RG Logdet Value Execution v1

Status: `{STATUS}`

## Theorem

The minimal H-response source row table is now explicit.  The selected
`B_Huv/P_H` domain and row-functional contract are closed, but no source-owned
numeric `H_response` rows or value certificates are emitted.

## Required Rows

- `Huu`
- `Hud_re`
- `Hud_im`
- `Hdd`
- Hermitian certificate
- source ownership certificate
- same-source exactness/error certificate
- quotient admissibility certificate

Accepted H-response source rows: `0`.

## Consequence

No selected H-response spectrum, no H-response logdet, and no `R_H^RG` value
execution are emitted here.

Next artifact: `{NEXT}`
"""

    write_json(ROW_TABLE, row_table)
    write_json(SPECTRUM_PACKET, spectrum_packet)
    write_json(RHRG_PACKET, rhrg_packet)
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
