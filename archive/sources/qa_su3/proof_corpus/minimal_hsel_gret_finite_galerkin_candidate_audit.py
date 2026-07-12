"""Audit the minimal H_sel/G_ret finite Galerkin candidate."""

from __future__ import annotations

import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "minimal_hsel_gret_finite_galerkin_candidate_certificate.json"
DATA = REPO / "candidate_data" / "minimal_hsel_gret_finite_galerkin_candidate.candidate.json"
PACKET = REPO / "candidate_data" / "hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Minimal_Hsel_Gret_Finite_Galerkin_Candidate_v1.md"
SCRIPT = REPO / "scripts" / "build_minimal_hsel_gret_finite_galerkin_candidate.py"
VALIDATOR = REPO / "scripts" / "validate_hessian_kernel_central_cocycle_derivation.py"


def parse_fraction(value: int | str) -> Fraction:
    if isinstance(value, int):
        return Fraction(value)
    return Fraction(value)


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    validator = subprocess.run(
        [sys.executable, str(VALIDATOR), str(PACKET)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    hessian = [[Fraction(x) for x in row] for row in data["hessian"]["matrix"]]
    green = [[parse_fraction(x) for x in row] for row in data["green"]["matrix"]]
    identity = matmul(hessian, green)
    expected_identity = [[Fraction(int(i == j)) for j in range(3)] for i in range(3)]
    tau = data["tau"]["values"]
    selected = data["selection_proof"]
    norms = {
        tuple(row["covector"]): parse_fraction(row["retarded_norm"])
        for row in selected["search_box_check"]
        if row["annihilates_P"]
    }
    selected_norm = parse_fraction(selected["selected_covector_retarded_norm"])
    nonconjugate_norms = [
        norm
        for covector, norm in norms.items()
        if covector not in {(0, 0, 1), (0, 0, -1)}
    ]

    checks = [
        check("status", cert["status"] == "QA_SU3_MINIMAL_HSEL_GRET_FINITE_GALERKIN_CANDIDATE_CONSTRUCTED_VALIDATOR_PASS_CONDITIONAL_SOURCE_PROMOTION_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("validator passes filled packet", validator.returncode == 0 and "passes" in validator.stdout, validator.stdout.strip()),
        check("hessian exact value", data["hessian"]["matrix"] == [[26, -3, 0], [-3, 10, 0], [0, 0, 8]], data["hessian"]["matrix"]),
        check("hessian positive", data["hessian"]["positive_definite"] is True and data["hessian"]["sylvester_minors"] == [26, 251, 2008], data["hessian"]),
        check("green inverse", identity == expected_identity and data["green"]["inverse_verified"] is True, identity),
        check("selected covector", selected["selected_covector"] == [0, 0, 1] and selected_norm == Fraction(1, 8), selected),
        check("minimal twisted covector", all(selected_norm < norm for norm in nonconjugate_norms), nonconjugate_norms),
        check("tau extracted", tau == {"F1": 1, "F2": -1, "F3": 0, "F4": -1, "F5": 1, "G1": -1, "G2": 1, "G3": 0, "G4": 1, "G5": -1, "P": 0}, tau),
        check("twists cancel", data["tau"]["all_products_cancel"] is True and all(data["tau"]["cancellation"].values()), data["tau"]),
        check("guardrails", packet["guardrails"]["no_target_fitting"] is True and packet["guardrails"]["no_q79_direct_import"] is True, packet["guardrails"]),
        check("not full closure", cert["closure_claimed"] is False and cert["what_remains_open"]["smooth_same_source_operator_promotion"] is True, cert),
        check("note records promotion gate", "Finite_Galerkin_to_Smooth_Operator_Promotion_or_NoGo" in note and "not the full smooth Qa/SU3 threshold proof" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 minimal Hsel/Gret finite Galerkin candidate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
