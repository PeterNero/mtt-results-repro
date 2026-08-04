"""Audit q79 Route-C selected-source or typed D_E construction target."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_selected_de_green_dotd_source_for_primitive_c1.py"
SCRIPT = (
    ROOT
    / "scripts"
    / "analyze_q79_routec_selected_source_certificate_or_typed_de_construction.py"
)
CERT = (
    ROOT
    / "certificates"
    / "q79_routec_selected_source_certificate_or_typed_de_construction_certificate.json"
)
CANDIDATE = (
    ROOT
    / "candidate_data"
    / "q79_routec_selected_source_certificate_or_typed_de_construction.candidate.json"
)
OUT_DIR = ROOT / "candidate_data" / "q79_routec_selected_source_certificate_or_typed_de_construction"
TABLE = OUT_DIR / "routec_or_typed_de_frontier_summary.json"
WITNESS = OUT_DIR / "selected_connection_witness_contract.open.json"
TYPED = OUT_DIR / "typed_de_witness_contract.open.json"
HYP = OUT_DIR / "hypothetical_selected_routec_source_certificate.selected_flags_only.json"
PAPER = (
    ROOT
    / "proof_corpus"
    / "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1.md"
)

STATUS = "Q79_ROUTEC_SELECTED_SOURCE_OR_TYPED_DE_CONSTRUCTION_OPEN_WITNESS_CONTRACT_CREATED"
NEXT = "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, TABLE, WITNESS, TYPED, HYP, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    witness = load(WITNESS)
    typed = load(TYPED)
    hyp = load(HYP)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate differ", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(table["status"] == STATUS, "table status mismatch", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    honest = cert["honest_routec_selected_source_attempt"]
    diagnostic = cert["hypothetical_selected_source_diagnostic"]
    routes = cert["route_evaluation"]
    closes = cert["what_closes_now"]
    remaining = cert["what_remains_open"]

    require(honest["validator_exit_code"] == 1, "honest selected source should fail", failures)
    require(
        honest["selected_hym_operator_source_verified"] is False,
        "honest selected source oververified",
        failures,
    )
    require(diagnostic["validator_exit_code"] == 0, "hypothetical source should pass", failures)
    require(diagnostic["diagnostic_not_proof"] is True, "diagnostic must be guarded", failures)
    require(hyp["diagnostic_not_proof"] is True, "hyp packet must be diagnostic only", failures)
    require(hyp["source"]["selected_by_mtt"] is True, "hyp packet should lift selected flag", failures)
    require(hyp["source"]["fixture_only"] is False, "hyp packet should lift fixture flag", failures)
    require(
        hyp["operator_source"]["selected_D_E_constructed"] is True
        and hyp["operator_source"]["selected_dotD_constructed"] is True
        and hyp["operator_source"]["selected_riesz_green_constructed"] is True,
        "hyp packet should lift operator-construction flags",
        failures,
    )

    require(
        routes["route_A_selected_routec_source_certificate"]["status"]
        == "BLOCKED_CURRENT_HONEST_PACKET_FAILS",
        "route A status wrong",
        failures,
    )
    require(routes["route_B_typed_monad_cech_de_construction"]["status"] == "BLOCKED", "route B status wrong", failures)
    require(
        routes["route_C_direct_HYM_connection"]["status"] == "ABSTRACT_EXISTENCE_ONLY",
        "route C status wrong",
        failures,
    )
    require(routes["route_D_corrected_non_invariant_dolbeault"]["status"] == "BLOCKED", "route D status wrong", failures)

    require(witness["schema"] == "Q79SelectedConnectionWitnessContract.v1", "witness schema wrong", failures)
    require(witness["status"] == "OPEN_SELECTED_CONNECTION_WITNESS_REQUIRED", "witness status wrong", failures)
    require(
        set(witness["accepted_witness_routes"])
        == {
            "route_A_selected_routec_source_certificate",
            "route_B_typed_monad_cech_de_construction",
            "route_C_direct_HYM_connection",
        },
        "witness route set wrong",
        failures,
    )
    for phrase in (
        "source.selected_by_mtt = true",
        "route_c_residual and selected-source-promotion validators pass honestly",
        "typed f_i and g_i sections",
        "integrability F^(0,2)=0",
        "numerical or symbolic HYM connection coefficients",
    ):
        require(phrase in json.dumps(witness), f"witness missing phrase: {phrase}", failures)

    require(typed["schema"] == "Q79TypedDEWitnessContract.v1", "typed schema wrong", failures)
    require(typed["status"] == "OPEN_TYPED_DE_OR_SELECTED_HYM_CONNECTION_REQUIRED", "typed status wrong", failures)
    require(typed["currently_computable"] is False, "typed witness should not be computable", failures)
    require(len(typed["one_of"]) == 3, "typed witness alternatives changed", failures)
    require("operator matrix L_N" in " ".join(typed["then_compute"]), "typed next compute missing L_N", failures)

    for key in (
        "routec_selected_source_certificate_attempt_tested",
        "typed_de_construction_attempt_imported",
        "all_current_routes_to_selected_DE_source_classified",
        "hypothetical_selected_source_packet_passes_as_diagnostic",
        "selected_connection_witness_contract_created",
        "typed_de_witness_contract_created",
    ):
        require(closes[key] is True, f"close flag false: {key}", failures)

    for key in (
        "selected_connection_witness_values",
        "selected_visible_sm_bundle_model",
        "selected_routec_residual_or_typed_de_values",
        "honest_selected_DE_Riesz_Green_dotD_packets",
        "all_24_primitive_C1_3x3_matrices",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"remaining flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for phrase in (
        "missing selected connection witness target",
        "honest selected Route-C/HYM source certificate route",
        "typed `D_E` construction route",
        "selected-flags-only diagnostic packet",
        "not selected-source proof",
        "selected connection witness",
        "typed monad/Cech `D_E` construction",
        "direct selected HYM connection",
        "Q79RouteCSelectedSourceOrTypedDEWitnessReductionTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 Route-C selected source or typed D_E construction audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 Route-C selected source or typed D_E construction audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
