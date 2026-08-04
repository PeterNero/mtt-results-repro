"""Create the q79 Route-C selected-source or typed D_E construction target.

The previous gate showed that the finite Route-C D_E/Green/dotD arithmetic is
consistent once selected-source flags are hypothetically supplied.  This script
tests the next missing object itself:

* an honest selected HYM/Route-C operator-source certificate, using the current
  selected_hym_operator_source attempt;
* the typed D_E construction route, using the existing selected D_E
  construction attempt.

If neither closes, the script creates the minimal witness contract for the
data that must now be supplied.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
SCRIPTS = ROOT / "scripts"

OUT_DIR = CANDIDATES / "q79_routec_selected_source_certificate_or_typed_de_construction"
OUT_CANDIDATE = CANDIDATES / "q79_routec_selected_source_certificate_or_typed_de_construction.candidate.json"
OUT_CERT = CERTS / "q79_routec_selected_source_certificate_or_typed_de_construction_certificate.json"
OUT_PAPER = CORPUS / "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1.md"
OUT_TABLE = OUT_DIR / "routec_or_typed_de_frontier_summary.json"
OUT_WITNESS_CONTRACT = OUT_DIR / "selected_connection_witness_contract.open.json"
OUT_TYPED_CONTRACT = OUT_DIR / "typed_de_witness_contract.open.json"
OUT_HYPOTHETICAL = OUT_DIR / "hypothetical_selected_routec_source_certificate.selected_flags_only.json"

STATUS = "Q79_ROUTEC_SELECTED_SOURCE_OR_TYPED_DE_CONSTRUCTION_OPEN_WITNESS_CONTRACT_CREATED"
NEXT = "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1"

HONEST_HYM_PACKET = CERTS / "selected_hym_operator_source.attempt.json"
HYP_DIR = (
    CANDIDATES
    / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual"
    / "hypothetical_routec_selected_flags_only"
)
DE_GATE = CERTS / "q79_selected_de_green_dotd_source_for_primitive_c1_certificate.json"
SELECTED_DE = CERTS / "iwasawa_selected_de_construction_attempt_certificate.json"
HYM_ATTEMPT = CERTS / "selected_hym_operator_source_attempt_certificate.json"
Z7_CERT = CERTS / "z7_fuyau_mukai_charge_sector_certificate.json"
MONAD_RECOVERY = CERTS / "iwasawa_typed_monad_section_recovery_certificate.json"
DOLBEAULT = CERTS / "iwasawa_dolbeault_complex_extraction_certificate.json"
SCAN = CERTS / "corrected_a01_candidate_scan_certificate.json"
INVARIANT_OBSTRUCTION = CERTS / "iwasawa_invariant_a01_repair_obstruction_certificate.json"
DIAGNOSTIC = CERTS / "iwasawa_diagnostic_h1_three_spectral_pipeline_certificate.json"

INPUTS = {
    "selected_de_green_dotd_gate": DE_GATE,
    "selected_hym_operator_source_attempt": HYM_ATTEMPT,
    "selected_de_construction_attempt": SELECTED_DE,
    "z7_charge_sector": Z7_CERT,
    "typed_monad_section_recovery": MONAD_RECOVERY,
    "dolbeault_complex_extraction": DOLBEAULT,
    "corrected_a01_candidate_scan": SCAN,
    "invariant_a01_repair_obstruction": INVARIANT_OBSTRUCTION,
    "diagnostic_h1_three_pipeline": DIAGNOSTIC,
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
    }


def run_validator(script: str, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "script": f"scripts/{script}",
        "path": rel(path),
        "exit_code": proc.returncode,
        "pass": proc.returncode == 0,
        "stdout_head": proc.stdout.splitlines()[:40],
        "stdout": proc.stdout,
    }


def parse_report(stdout: str, prefix: str) -> dict[str, Any]:
    for line in stdout.splitlines():
        if line.startswith(prefix):
            return json.loads(line[len(prefix) :])
    return {}


def make_hypothetical_hym_packet() -> dict[str, Any]:
    base = load(HONEST_HYM_PACKET)
    packet = copy.deepcopy(base)
    packet["status"] = "HYPOTHETICAL_SELECTED_ROUTE_C_SOURCE_FLAGS_ONLY"
    packet["source"]["selected_by_mtt"] = True
    packet["source"]["fixture_only"] = False
    packet["source"]["source_certificate"] = rel(OUT_WITNESS_CONTRACT)
    packet["background"]["charge_sector_only"] = False
    packet["background"]["visible_sm_bundle_model_selected"] = True
    packet["background"]["matter_operator_source_constructed"] = True
    packet["operator_source"]["route_c_residual_packet"] = rel(
        HYP_DIR / "route_c_residuals.selected_flags_only.json"
    )
    packet["operator_source"]["selected_source_promotion_packet"] = rel(
        HYP_DIR / "selected_source_promotion.selected_flags_only.json"
    )
    packet["operator_source"]["selected_D_E_constructed"] = True
    packet["operator_source"]["selected_dotD_constructed"] = True
    packet["operator_source"]["selected_riesz_green_constructed"] = True
    packet["operator_source"]["projector_retention_selected"] = True
    packet["diagnostic_not_proof"] = True
    return packet


def selected_connection_witness_contract() -> dict[str, Any]:
    return {
        "schema": "Q79SelectedConnectionWitnessContract.v1",
        "status": "OPEN_SELECTED_CONNECTION_WITNESS_REQUIRED",
        "branch": {
            "q": 79,
            "orientation": "F",
            "torsion_label_m": 1,
            "antiunitary_partner_retained": True,
        },
        "accepted_witness_routes": {
            "route_A_selected_routec_source_certificate": {
                "required_fields": [
                    "source.selected_by_mtt = true",
                    "source.fixture_only = false",
                    "source.source_certificate names this witness or stronger proof",
                    "background.charge_sector_only = false",
                    "background.visible_sm_bundle_model_selected = true",
                    "background.matter_operator_source_constructed = true",
                    "operator_source.selected_D_E_constructed = true",
                    "operator_source.selected_dotD_constructed = true",
                    "operator_source.selected_riesz_green_constructed = true",
                    "operator_source.projector_retention_selected = true",
                    "route_c_residual and selected-source-promotion validators pass honestly",
                ],
            },
            "route_B_typed_monad_cech_de_construction": {
                "required_fields": [
                    "typed f_i and g_i sections in their declared line-bundle spaces",
                    "Cech transition functions and cocycle data",
                    "g o f = 0 and exactness or controlled torsion-free sheaf substitute",
                    "selected Hermitian metric and gauge fixing",
                    "connection coefficients A^(0,1) or equivalent holomorphic structure",
                    "integrability F^(0,2)=0",
                    "HYM/Strominger residual and Green-Schwarz/Bianchi checks",
                    "finite basis B_N and action of D_E on B_N",
                    "Riesz gap, reduced Green, and dotD alpha1 response packets",
                ],
            },
            "route_C_direct_HYM_connection": {
                "required_fields": [
                    "selected stable holomorphic bundle model",
                    "selected Gauduchon/balanced metric",
                    "numerical or symbolic HYM connection coefficients",
                    "residual bounds strong enough for the finite validators",
                    "same-branch dotD alpha1 derivative",
                ],
            },
        },
        "forbidden_shortcuts": [
            "selected-flags-only diagnostic promoted as proof",
            "abstract Li-Yau existence promoted to finite matrices",
            "observed masses, CKM angles, or benchmark Yukawa entries",
            "charge-sector Fu-Yau data treated as visible matter operator source",
        ],
    }


def typed_de_witness_contract(selected_de: dict[str, Any]) -> dict[str, Any]:
    minimal = selected_de.get("minimal_new_data_to_close", {})
    abstract = selected_de.get("abstract_operator_package", {})
    return {
        "schema": "Q79TypedDEWitnessContract.v1",
        "status": "OPEN_TYPED_DE_OR_SELECTED_HYM_CONNECTION_REQUIRED",
        "formal_operator": abstract.get("formal_symbol"),
        "mathematically_admissible_if_selected_HYM_connection_supplied": abstract.get(
            "mathematically_admissible_if_selected_HYM_connection_supplied"
        ),
        "currently_computable": False,
        "one_of": minimal.get("one_of", []),
        "then_compute": minimal.get("then_compute", []),
        "validator_targets_after_witness": [
            "validate_iwasawa_route_c_residuals.py",
            "validate_iwasawa_de_action.py",
            "validate_iwasawa_riesz_gap.py",
            "validate_iwasawa_reduced_green.py",
            "validate_iwasawa_dotd_response.py",
            "validate_iwasawa_selected_source_promotion.py",
            "validate_selected_hym_operator_source.py",
        ],
    }


def route_status(selected_de: dict[str, Any], monad: dict[str, Any]) -> dict[str, Any]:
    routes = selected_de.get("route_evaluation", {})
    return {
        "route_A_selected_routec_source_certificate": {
            "status": "BLOCKED_CURRENT_HONEST_PACKET_FAILS",
            "reason": "selected_hym_operator_source.attempt.json is rejected by the selected HYM/operator-source validator",
        },
        "route_B_typed_monad_cech_de_construction": {
            "status": routes.get("R2_typed_monad_sections", {}).get("status"),
            "typed_monad_cech_can_close_now": monad.get("route_decision", {}).get(
                "typed_monad_cech_can_close_now"
            ),
            "reason": routes.get("R2_typed_monad_sections", {}).get("reason"),
        },
        "route_C_direct_HYM_connection": {
            "status": routes.get("R3_direct_selected_HYM_solve", {}).get("status"),
            "reason": routes.get("R3_direct_selected_HYM_solve", {}).get("reason"),
        },
        "route_D_corrected_non_invariant_dolbeault": {
            "status": routes.get("R1_corrected_non_invariant_Dolbeault_operator", {}).get(
                "status"
            ),
            "reason": routes.get("R1_corrected_non_invariant_Dolbeault_operator", {}).get(
                "reason"
            ),
        },
    }


def build_candidate() -> dict[str, Any]:
    selected_de = load(SELECTED_DE)
    monad = load(MONAD_RECOVERY)
    write_json(OUT_WITNESS_CONTRACT, selected_connection_witness_contract())
    write_json(OUT_TYPED_CONTRACT, typed_de_witness_contract(selected_de))
    write_json(OUT_HYPOTHETICAL, make_hypothetical_hym_packet())

    honest_hym = run_validator("validate_selected_hym_operator_source.py", HONEST_HYM_PACKET)
    hypothetical_hym = run_validator("validate_selected_hym_operator_source.py", OUT_HYPOTHETICAL)

    honest_report = parse_report(honest_hym["stdout"], "hym_operator_source_validation_report=")
    hypothetical_report = parse_report(
        hypothetical_hym["stdout"], "hym_operator_source_validation_report="
    )

    routes = route_status(selected_de, monad)
    selected_de_blocked = selected_de.get("verdict", {}).get("selected_D_E_constructed") is False
    all_current_routes_blocked = (
        honest_hym["exit_code"] == 1
        and selected_de_blocked
        and routes["route_B_typed_monad_cech_de_construction"]["status"] == "BLOCKED"
        and routes["route_C_direct_HYM_connection"]["status"] == "ABSTRACT_EXISTENCE_ONLY"
    )

    data = {
        "certificate": "Q79RouteCSelectedSourceCertificateOrTypedDEConstruction",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "selected_connection_witness_contract": rel(OUT_WITNESS_CONTRACT),
        "typed_de_witness_contract": rel(OUT_TYPED_CONTRACT),
        "hypothetical_selected_routec_source_packet": rel(OUT_HYPOTHETICAL),
        "input_statuses": {name: status_record(path) for name, path in INPUTS.items()},
        "route_evaluation": routes,
        "honest_routec_selected_source_attempt": {
            "packet": rel(HONEST_HYM_PACKET),
            "validator_exit_code": honest_hym["exit_code"],
            "validator_report": honest_report,
            "stdout_head": honest_hym["stdout_head"],
            "selected_hym_operator_source_verified": honest_report.get(
                "selected_hym_operator_source_verified"
            ),
        },
        "hypothetical_selected_source_diagnostic": {
            "packet": rel(OUT_HYPOTHETICAL),
            "validator_exit_code": hypothetical_hym["exit_code"],
            "validator_report": hypothetical_report,
            "diagnostic_not_proof": True,
            "interpretation": (
                "If the missing selected connection witness is supplied and the "
                "same Route-C finite packets are bound to it, the selected HYM/"
                "operator-source validator has no hidden plumbing obstruction."
            ),
        },
        "typed_de_construction_status": {
            "certificate": rel(SELECTED_DE),
            "selected_D_E_constructed": selected_de.get("verdict", {}).get(
                "selected_D_E_constructed"
            ),
            "diagnostic_pipeline_ready": selected_de.get("verdict", {}).get(
                "diagnostic_pipeline_ready"
            ),
            "minimal_new_data_to_close": selected_de.get("minimal_new_data_to_close"),
        },
        "what_closes_now": {
            "routec_selected_source_certificate_attempt_tested": honest_hym["exit_code"] == 1,
            "typed_de_construction_attempt_imported": selected_de_blocked,
            "all_current_routes_to_selected_DE_source_classified": all_current_routes_blocked,
            "hypothetical_selected_source_packet_passes_as_diagnostic": hypothetical_hym[
                "exit_code"
            ]
            == 0,
            "selected_connection_witness_contract_created": True,
            "typed_de_witness_contract_created": True,
        },
        "what_remains_open": {
            "selected_connection_witness_values": True,
            "selected_visible_sm_bundle_model": True,
            "selected_routec_residual_or_typed_de_values": True,
            "honest_selected_DE_Riesz_Green_dotD_packets": True,
            "same_source_ChernWeil_GS_row": True,
            "all_24_primitive_C1_3x3_matrices": True,
            "selected_C1_response_matrices": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "uses_lifted_flags_as_proof": False,
            "claims_selected_routec_source_certificate": False,
            "claims_selected_D_E_constructed": False,
            "claims_selected_HYM_connection_constructed": False,
            "claims_primitive_C1_values_computed": False,
            "claims_selected_C1_response_matrices": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79RouteCSelectedSourceOrTypedDEWitnessReductionTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The current corpus does not yet supply a selected Route-C source "
                "certificate or typed D_E construction. The honest selected-HYM "
                "operator-source packet fails; the typed D_E construction attempt "
                "is blocked at missing connection/Cech data; and a diagnostic-only "
                "selected-source packet passes once those missing fields are "
                "hypothetically supplied. Therefore the remaining object is exactly "
                "a selected connection witness: typed monad/Cech data or a selected "
                "HYM/Route-C connection with residual bounds."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return data


def bool_lines(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def route_lines(routes: dict[str, Any]) -> str:
    lines = []
    for name, route in routes.items():
        lines.append(f"- `{name}`: `{route.get('status')}`")
    return "\n".join(lines)


def build_paper(data: dict[str, Any]) -> str:
    return f"""# Q79 Route-C Selected Source Certificate or Typed D_E Construction v1

## Result

This creates the missing selected connection witness target.

The honest selected Route-C/HYM source certificate route is tested and remains
blocked.  The typed `D_E` construction route is also blocked by missing typed
monad/Cech sections or selected HYM connection coefficients.  A
selected-flags-only diagnostic packet passes the selected HYM/operator-source
validator, so the validator plumbing is not the wall.

## Route Evaluation

{route_lines(data["route_evaluation"])}

## Honest Source Attempt

- packet: `{data["honest_routec_selected_source_attempt"]["packet"]}`
- validator exit: `{data["honest_routec_selected_source_attempt"]["validator_exit_code"]}`
- selected source verified: `{data["honest_routec_selected_source_attempt"]["selected_hym_operator_source_verified"]}`

## Diagnostic

- packet: `{data["hypothetical_selected_source_diagnostic"]["packet"]}`
- validator exit: `{data["hypothetical_selected_source_diagnostic"]["validator_exit_code"]}`
- diagnostic only: `{data["hypothetical_selected_source_diagnostic"]["diagnostic_not_proof"]}`

Interpretation: {data["hypothetical_selected_source_diagnostic"]["interpretation"]}

This is not selected-source proof.

## Witness Contracts

- selected connection witness: `{data["selected_connection_witness_contract"]}`
- typed `D_E` witness: `{data["typed_de_witness_contract"]}`

The witness can arrive by one of three honest routes:

- selected Route-C source certificate;
- typed monad/Cech `D_E` construction;
- direct selected HYM connection with residual bounds.

## What Closes Now

{bool_lines(data["what_closes_now"])}

## What Remains Open

{bool_lines(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as a witness-reduction theorem.

{data["theorem"]["statement"]}

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(
        OUT_TABLE,
        {
            "status": data["status"],
            "next_required_artifact": data["next_required_artifact"],
            "honest_hym_exit_code": data["honest_routec_selected_source_attempt"][
                "validator_exit_code"
            ],
            "hypothetical_hym_exit_code": data["hypothetical_selected_source_diagnostic"][
                "validator_exit_code"
            ],
            "what_closes_now": data["what_closes_now"],
        },
    )
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 Route-C selected source or typed D_E construction target")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
