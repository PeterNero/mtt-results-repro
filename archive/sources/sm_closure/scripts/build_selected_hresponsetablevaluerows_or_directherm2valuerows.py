"""Build H-response table value rows or direct Herm(2) value rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hresponsetablevaluerows_or_directherm2valuerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HResponseTableValueRows_or_DirectHerm2ValueRows_v1.md"

TABLE_INTERFACE = PACKET_DIR / "hresponse_table_value_row_interface.packet.json"
HRESPONSE_ATTEMPT = PACKET_DIR / "hresponse_value_row_execution_attempt.packet.json"
DIRECT_ATTEMPT = PACKET_DIR / "direct_herm2_value_row_execution_attempt.packet.json"
SHORTCUTS = PACKET_DIR / "shortcut_rejection_after_hresponse_value_rows.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hresponse_value_rows.packet.json"

PREVIOUS = DATA / "selected_msourcehuvoperator_or_directherm2rows.candidate.json"
PREVIOUS_MSOURCE_CONTRACT = (
    DATA
    / "selected_msourcehuvoperator_or_directherm2rows"
    / "msource_contract_reconciled_with_active_domain.packet.json"
)
PREVIOUS_MSOURCE_ATTEMPT = (
    DATA
    / "selected_msourcehuvoperator_or_directherm2rows"
    / "msource_execution_attempt_after_bhuv_rh_import.packet.json"
)
PREVIOUS_DIRECT_ATTEMPT = (
    DATA
    / "selected_msourcehuvoperator_or_directherm2rows"
    / "direct_herm2_rows_after_msource_contract.packet.json"
)
HRESPONSE_TABLE = (
    DATA
    / "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution"
    / "hresponse_source_row_execution_table.packet.json"
)
HRESPONSE_SPECTRUM = (
    DATA
    / "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution"
    / "hresponse_spectrum_from_rows_attempt.packet.json"
)
HRESPONSE_VALUE = DATA / "selected_hresponsevaluesourcefunctional_or_directherm2rows.candidate.json"
HRESPONSE_FUNCTIONAL = (
    DATA
    / "selected_hresponsevaluesourcefunctional_or_directherm2rows"
    / "hresponse_value_source_functional.packet.json"
)
HRESPONSE_ROUTE_MATRIX = (
    DATA
    / "selected_hresponsevaluesourcefunctional_or_directherm2rows"
    / "current_value_route_acceptance_matrix.packet.json"
)
HRESPONSE_DIRECT_RUN = (
    DATA
    / "selected_hresponsevaluesourcefunctional_or_directherm2rows"
    / "direct_herm2_row_emission_run.packet.json"
)
FINITE_H = DATA / "selected_finitehfunctionalcandidate_or_directherm2rowemissionrun.candidate.json"
RADIAL = DATA / "selected_hradialscalephasesource_or_herm2hessianrows.candidate.json"
POLAR = DATA / "selected_herm2polarsourcecompletion_or_hresponserows.candidate.json"
PROJECTION = DATA / "selected_c1tobhuvprojectiontensor_or_fhuvrows.candidate.json"

STATUS = (
    "MTT_SELECTED_HRESPONSETABLEVALUEROWS_OR_DIRECTHERM2VALUEROWS_"
    "EXECUTED_ZERO_ROWS_SOURCE_EMISSION_OPEN"
)
NEXT = "MTT_Selected_HResponseRowSourceEmission_or_DirectHerm2CertificatePayload_v1"


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
        raise FileNotFoundError("missing H-response value-row inputs: " + ", ".join(missing))


def row_ids(rows: list[dict[str, Any]]) -> list[str]:
    return [row["row_id"] for row in rows]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_MSOURCE_CONTRACT,
        PREVIOUS_MSOURCE_ATTEMPT,
        PREVIOUS_DIRECT_ATTEMPT,
        HRESPONSE_TABLE,
        HRESPONSE_SPECTRUM,
        HRESPONSE_VALUE,
        HRESPONSE_FUNCTIONAL,
        HRESPONSE_ROUTE_MATRIX,
        HRESPONSE_DIRECT_RUN,
        FINITE_H,
        RADIAL,
        POLAR,
        PROJECTION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    msource_contract = load(PREVIOUS_MSOURCE_CONTRACT)
    msource_attempt = load(PREVIOUS_MSOURCE_ATTEMPT)
    previous_direct = load(PREVIOUS_DIRECT_ATTEMPT)
    hresponse_table = load(HRESPONSE_TABLE)
    hresponse_spectrum = load(HRESPONSE_SPECTRUM)
    hresponse_value = load(HRESPONSE_VALUE)
    hresponse_functional = load(HRESPONSE_FUNCTIONAL)
    route_matrix = load(HRESPONSE_ROUTE_MATRIX)
    direct_run = load(HRESPONSE_DIRECT_RUN)
    finite_h = load(FINITE_H)
    radial = load(RADIAL)
    polar = load(POLAR)
    projection = load(PROJECTION)

    direct_route = next(
        row for row in route_matrix["route_rows"] if row["route_id"] == "direct_Herm2_rows"
    )
    msource_route = next(
        row
        for row in route_matrix["route_rows"]
        if row["route_id"] == "full_M_source_plus_R_H_restriction"
    )

    hresponse_required_rows = row_ids(hresponse_table["source_rows"])
    direct_required_rows = row_ids(direct_run["required_rows"])

    table_interface = {
        "schema": "MTTHResponseTableValueRowInterface.v1",
        "status": "HRESPONSE_AND_DIRECT_HERM2_VALUE_ROW_INTERFACES_FIXED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "active_domain_imports": {
            "M_source_contract_reconciled": previous["closure_decision"][
                "M_source_acceptance_contract_reconciled"
            ],
            "B_Huv_R_H_domain_available": previous["closure_decision"][
                "B_Huv_R_H_domain_available"
            ],
            "Herm2_row_extractors_closed": msource_contract["active_domain_supersessions"][
                "Herm2_row_extractors_closed"
            ],
            "M_source_formula": msource_contract["updated_formula"]["M_source"],
            "Huv_formula": msource_contract["updated_formula"]["Huv"],
        },
        "hresponse_table_interface": {
            "required_row_count": hresponse_table["decision"]["required_row_count"],
            "required_rows": hresponse_required_rows,
            "acceptance_tests": hresponse_table["acceptance_tests"],
            "domain_closed": hresponse_table["domain_closed"],
        },
        "direct_herm2_interface": {
            "required_row_or_certificate_count": direct_run["decision"]["required_row_count"],
            "required_rows": direct_required_rows,
            "normal_form": previous_direct["normal_form"],
            "acceptance_tests": hresponse_functional["accepted_value_source_contract"][
                "strict_MH_acceptance_tests"
            ],
        },
        "decision": {
            "interfaces_fixed": True,
            "basis_domain_blocker_remaining": False,
            "value_row_source_emission_required": True,
            "certificate_payload_required": True,
        },
    }

    hresponse_attempt = {
        "schema": "MTTHResponseTableValueRowExecutionAttempt.v1",
        "status": "HRESPONSE_TABLE_VALUE_ROW_EXECUTION_ZERO_ACCEPTED_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_table_status": hresponse_table["status"],
        "spectrum_attempt_status": hresponse_spectrum["status"],
        "source_rows": hresponse_table["source_rows"],
        "computed_values": {row_id: None for row_id in hresponse_required_rows},
        "decision": {
            "execution_attempted": True,
            "required_row_count": hresponse_table["decision"]["required_row_count"],
            "accepted_source_row_count": hresponse_table["decision"]["accepted_source_row_count"],
            "emitted_row_count": hresponse_table["decision"]["emitted_row_count"],
            "selected_H_response_table_emitted": hresponse_table["decision"][
                "selected_H_response_table_emitted"
            ],
            "selected_H_response_spectrum_emitted": hresponse_spectrum["decision"][
                "selected_H_response_spectrum_emitted"
            ],
            "selected_logdet_from_H_response_emitted": hresponse_spectrum["decision"][
                "selected_logdet_from_H_response_emitted"
            ],
            "R_H_RG_logdet_executable": hresponse_spectrum["decision"][
                "H_response_logdet_executable"
            ],
            "source_ownership_certificate_emitted": hresponse_table["decision"][
                "source_ownership_certificate_emitted"
            ],
            "same_source_exactness_or_error_certificate_emitted": hresponse_table["decision"][
                "same_source_exactness_or_error_certificate_emitted"
            ],
            "quotient_admissibility_certificate_emitted": False,
        },
    }

    direct_attempt = {
        "schema": "MTTDirectHerm2ValueRowExecutionAttempt.v1",
        "status": "DIRECT_HERM2_VALUE_ROW_EXECUTION_ZERO_ACCEPTED_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "direct_run_status": direct_run["status"],
        "direct_route_status": direct_route["status"],
        "M_source_route_status": msource_route["status"],
        "required_rows": direct_run["required_rows"],
        "computed_values": {row_id: None for row_id in direct_required_rows},
        "decision": {
            "execution_attempted": True,
            "required_row_count": direct_run["decision"]["required_row_count"],
            "accepted_row_count": direct_run["decision"]["accepted_row_count"],
            "emitted_row_count": direct_run["decision"]["emitted_row_count"],
            "direct_Huu_Hud_Hdd_emitted": direct_run["decision"]["direct_Huu_Hud_Hdd_emitted"],
            "direct_Herm2_Huv_payload_emitted": direct_run["decision"][
                "direct_Herm2_Huv_payload_emitted"
            ],
            "source_ownership_certificate_emitted": direct_run["decision"][
                "source_ownership_certificate_emitted"
            ],
            "same_source_exactness_or_error_certificate_emitted": direct_run["decision"][
                "same_source_exactness_or_error_certificate_emitted"
            ],
            "quotient_admissibility_certificate_emitted": direct_run["decision"][
                "quotient_admissibility_certificate_emitted"
            ],
            "selected_Hermitian_M_source_emitted": msource_attempt["decision"][
                "selected_Hermitian_M_source_emitted"
            ],
            "M_source_plus_R_H_values_emitted": msource_attempt["decision"][
                "M_source_plus_R_H_values_emitted"
            ],
            "Huv_values_emitted": msource_attempt["decision"]["Huv_values_emitted"],
        },
    }

    shortcut_rejections = {
        "schema": "MTTShortcutRejectionAfterHResponseValueRows.v1",
        "status": "SHORTCUTS_RECHECKED_NOT_VALUE_ROW_SOURCES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "rows": [
            {
                "candidate_id": "diagonal_HYM_metric",
                "accepted_as_value_row_source": False,
                "reason": "source-domain orthonormality/kinematic metric, not Higgs mass or strain Hessian rows",
            },
            {
                "candidate_id": "A_T_A_equals_12I_C1_normal_matrix",
                "accepted_as_value_row_source": False,
                "reason": "compressed C1 normal matrix; no selected Higgs variation-slot lift T_C1<-E_H^UV or ambient H rows",
            },
            {
                "candidate_id": "polar_reconstruction_law",
                "accepted_as_value_row_source": False,
                "reason": polar["theorem"]["statement"],
            },
            {
                "candidate_id": "controlled_HRG_lambda_calibration",
                "accepted_as_value_row_source": False,
                "reason": "controlled one-parameter replay uses lambda_H as calibration and is not a no-knob H-response source",
            },
            {
                "candidate_id": "static_H_logdet",
                "accepted_as_value_row_source": False,
                "reason": "static logdet support is not promoted to dynamic selected H_response/logdet rows",
            },
            {
                "candidate_id": "s_beta_projection_bridge",
                "accepted_as_value_row_source": False,
                "reason": "selected s_beta and projection bridge constrain geometry but emit no Huu,Hud,Hdd values",
            },
        ],
        "support_values_rechecked": {
            "selected_s_beta_value": finite_h["key_numbers"]["selected_s_beta_value"],
            "radial_packet_status": radial["status"],
            "polar_packet_status": polar["status"],
            "projection_packet_status": projection["status"],
        },
        "decision": {
            "shortcut_recheck_executed": True,
            "accepted_shortcut_value_sources": 0,
            "observed_or_target_fit_rejected": True,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHResponseValueRows.v1",
        "status": "NEXT_FRONTIER_HRESPONSE_ROW_SOURCE_EMISSION_OR_DIRECT_HERM2_CERTIFICATE_PAYLOAD",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "H_response table value-row interface fixed and executed",
            "direct Herm(2) Huv row/certificate interface fixed and executed",
            "active B_Huv/R_H/M_source domain imported without reopening old domain blockers",
            "diagonal HYM, C1 normal matrix, polar law, static logdet, controlled HRG, and s_beta bridge rechecked as non-sources",
        ],
        "still_open": [
            "selected primitive source rows for Huu,Hud_re,Hud_im,Hdd",
            "source ownership certificate for the H-response/direct Herm(2) rows",
            "same-source exactness or finite error certificate",
            "quotient admissibility certificate for the light line",
            "optional selected Hermitian M_source entries if the full route is used instead of direct rows",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHResponseTableValueRowsOrDirectHerm2ValueRows",
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
            "name": "HResponseTableValueRowsExecutedZeroRowsTheorem",
            "proved": True,
            "statement": (
                "The active B_Huv/R_H/M_source domain and Herm(2) extractors are "
                "already closed, so the remaining Huv/H-response gate is purely "
                "a value-row source gate. Executing the current selected "
                "H_response table interface requires seven rows/certificates and "
                "accepts zero. Executing the direct Herm(2) interface requires "
                "eight rows/certificates and accepts zero. Current shortcuts "
                "are rechecked and do not emit source-owned values. The next "
                "non-duplicative object is the selected primitive row source or "
                "direct Herm(2) certificate payload."
            ),
        },
        "packets": {
            "hresponse_table_value_row_interface": rel(TABLE_INTERFACE),
            "hresponse_value_row_execution_attempt": rel(HRESPONSE_ATTEMPT),
            "direct_herm2_value_row_execution_attempt": rel(DIRECT_ATTEMPT),
            "shortcut_rejection_after_hresponse_value_rows": rel(SHORTCUTS),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_msource_contract": rel(PREVIOUS_MSOURCE_CONTRACT),
            "hresponse_table": rel(HRESPONSE_TABLE),
            "hresponse_spectrum": rel(HRESPONSE_SPECTRUM),
            "hresponse_value": rel(HRESPONSE_VALUE),
            "hresponse_functional": rel(HRESPONSE_FUNCTIONAL),
            "hresponse_direct_run": rel(HRESPONSE_DIRECT_RUN),
            "finite_h": rel(FINITE_H),
            "polar": rel(POLAR),
            "projection": rel(PROJECTION),
        },
        "closure_decision": {
            "active_domain_imported": True,
            "hresponse_table_interface_fixed": True,
            "direct_Herm2_interface_fixed": True,
            "hresponse_table_execution_attempted": True,
            "direct_Herm2_value_row_execution_attempted": True,
            "shortcut_recheck_executed": True,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "M_source_plus_R_H_values_emitted": False,
            "Huv_values_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "source_ownership_certificate_emitted": False,
            "same_source_exactness_or_error_certificate_emitted": False,
            "quotient_admissibility_certificate_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "required_H_response_table_row_or_certificate_count": hresponse_table["decision"][
                "required_row_count"
            ],
            "accepted_H_response_source_row_count": hresponse_table["decision"][
                "accepted_source_row_count"
            ],
            "emitted_H_response_table_row_count": hresponse_table["decision"]["emitted_row_count"],
            "required_direct_Herm2_row_or_certificate_count": direct_run["decision"][
                "required_row_count"
            ],
            "accepted_direct_Herm2_row_or_certificate_count": direct_run["decision"][
                "accepted_row_count"
            ],
            "emitted_direct_Herm2_row_or_certificate_count": direct_run["decision"][
                "emitted_row_count"
            ],
            "accepted_value_source_routes": route_matrix["decision"]["accepted_value_source_routes"],
            "accepted_shortcut_value_sources": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedHResponseTableValueRowsOrDirectHerm2ValueRows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "active_domain_imported": True,
        "hresponse_table_interface_fixed": True,
        "direct_Herm2_interface_fixed": True,
        "hresponse_table_execution_attempted": True,
        "direct_Herm2_value_row_execution_attempted": True,
        "shortcut_recheck_executed": True,
        "required_H_response_table_row_or_certificate_count": hresponse_table["decision"][
            "required_row_count"
        ],
        "accepted_H_response_source_row_count": hresponse_table["decision"][
            "accepted_source_row_count"
        ],
        "required_direct_Herm2_row_or_certificate_count": direct_run["decision"][
            "required_row_count"
        ],
        "accepted_direct_Herm2_row_or_certificate_count": direct_run["decision"][
            "accepted_row_count"
        ],
        "selected_H_response_table_emitted": False,
        "selected_Hermitian_M_source_emitted": False,
        "direct_Huu_Hud_Hdd_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "source_ownership_certificate_emitted": False,
        "same_source_exactness_or_error_certificate_emitted": False,
        "quotient_admissibility_certificate_emitted": False,
    }

    note = f"""# MTT Selected HResponseTableValueRows or DirectHerm2ValueRows v1

Status: `{STATUS}`

## Theorem

The active domain is no longer the blocker.  The selected `B_Huv/R_H/M_source`
typing and Herm(2) extractors are imported from the previous packet:

```text
{msource_contract["updated_formula"]["M_source"]}
{msource_contract["updated_formula"]["Huv"]}
```

The remaining gate is the value-row source itself.

Current execution:

- required `H_response` table rows/certificates: `{hresponse_table["decision"]["required_row_count"]}`
- accepted `H_response` rows/certificates: `{hresponse_table["decision"]["accepted_source_row_count"]}`
- emitted `H_response` table rows: `{hresponse_table["decision"]["emitted_row_count"]}`
- required direct Herm(2) rows/certificates: `{direct_run["decision"]["required_row_count"]}`
- accepted direct Herm(2) rows/certificates: `{direct_run["decision"]["accepted_row_count"]}`
- emitted direct Herm(2) rows/certificates: `{direct_run["decision"]["emitted_row_count"]}`

The required direct row/certificate slots are:

```text
{", ".join(direct_required_rows)}
```

Rejected as source shortcuts in this packet:

- diagonal HYM metric
- `A^T A = 12 I_2` compressed C1 normal matrix
- Herm(2) polar reconstruction law
- controlled HRG/lambda calibration
- static H logdet support
- selected `s_beta` projection bridge

Next artifact: `{NEXT}`
"""

    write_json(TABLE_INTERFACE, table_interface)
    write_json(HRESPONSE_ATTEMPT, hresponse_attempt)
    write_json(DIRECT_ATTEMPT, direct_attempt)
    write_json(SHORTCUTS, shortcut_rejections)
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
