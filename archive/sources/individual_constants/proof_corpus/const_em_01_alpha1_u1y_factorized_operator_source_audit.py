"""Audit const_em_01_alpha1_u1y_factorized_operator_source."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_u1y_factorized_operator_source"
CANDIDATE = DATA / "const_em_01_alpha1_u1y_factorized_operator_source.candidate.json"
MATRIX = BASE / "factorized_operator_matrix_replay.packet.json"
SOURCE_DECISION = BASE / "source_emission_decision.packet.json"
LAMBDA_GATE = BASE / "lambda12_gate.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_u1y_factorized_operator_source_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_U1YFactorizedOperatorSource_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_u1y_factorized_operator_source.py"
STATUS = "MTT_CONST_EM_01_U1Y_FACTORIZED_OPERATOR_REPLAY_CLOSED_SOURCE_EMISSION_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    matrix = load(MATRIX)
    source = load(SOURCE_DECISION)
    lambda_gate = load(LAMBDA_GATE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["factorized_operator_matrix_replay"] is True, "matrix replay not closed")
    require(candidate["what_closes_now"]["A_base_tensor_I3_constructed"] is True, "raw factorized operator missing")
    require(candidate["what_closes_now"]["quotient_operator_on_V_mod_s_constructed"] is True, "quotient operator missing")
    require(candidate["what_closes_now"]["Pperp_binding_available"] is True, "Pperp binding unavailable")
    require(candidate["what_closes_now"]["quotient_logdet_replayed"] is True, "logdet not replayed")
    require(candidate["what_remains_open"]["selected_source_emission_of_A_base_tensor_I3"] is True, "source emission closed too early")
    require(candidate["what_remains_open"]["lambda_12"] is True, "lambda12 closed too early")
    require(candidate["what_remains_open"]["C_Y_value"] is True, "CY closed too early")

    checks = matrix["matrix_checks"]
    require(all(checks.values()), "one or more matrix replay checks failed")
    payload = matrix["closed_replay_payload"]
    require(payload["raw_operator"] == "A_base tensor I_3", "raw operator mismatch")
    require(payload["quotient_operator"] == "A_base tensor I_(V_3/<s>)", "quotient operator mismatch")
    require(payload["raw_dimension"] == 24, "raw dimension mismatch")
    require(payload["quotient_dimension"] == 16, "quotient dimension mismatch")
    require(payload["positive_quotient_multiplicities"] == [8, 8], "multiplicity mismatch")
    require(abs(payload["quotient_logdet"] - 29.201650332199108) < 1e-12, "quotient logdet mismatch")

    decision = source["decision"]
    require(decision["matrix_replay_closed"] is True, "source decision matrix replay not closed")
    require(decision["source_emission_promoted"] is False, "source emission overpromoted")
    require(decision["selected_source_emission_closed"] is False, "selected source emission overpromoted")
    require(decision["factorized_matrix_emitted_by_prior_source"] is False, "prior source emission overpromoted")
    require(decision["C_Y_value_claimed"] is False, "CY overclaim")
    require(decision["physical_alpha_value_claimed"] is False, "physical alpha overclaim")

    conditional = lambda_gate["conditional_values_from_QA"]
    require(abs(conditional["conditional_p_a_if_source_emitted"] - 29.201650332199108) < 1e-12, "conditional p_a mismatch")
    require(lambda_gate["promoted_now"]["p_a"] is False, "p_a promoted")
    require(lambda_gate["promoted_now"]["p_Y"] is False, "p_Y promoted")
    require(lambda_gate["promoted_now"]["lambda_12"] is False, "lambda12 promoted")
    require(lambda_gate["promoted_now"]["Delta_G12"] is False, "Delta_G12 promoted")

    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-U1Y-ROW / A6-SOURCE-EMISSION-THEOREM", "next primary mismatch")
    require(cert["matrix_replay_closed"] is True, "cert matrix replay mismatch")
    require(cert["source_emission_promoted"] is False, "cert source overclaim")
    require(cert["lambda_12_claimed"] is False, "cert lambda12 overclaim")
    require(cert["C_Y_value_claimed"] is False, "cert CY overclaim")
    require("quotient logdet: `29.201650332199108`" in note, "note logdet missing")
    require("A6-SOURCE-EMISSION-THEOREM" in note, "note next label missing")

    for packet in [candidate, matrix, source, lambda_gate, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
