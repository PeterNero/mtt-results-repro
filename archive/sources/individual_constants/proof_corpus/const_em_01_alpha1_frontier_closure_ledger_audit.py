"""Audit const_em_01_alpha1_frontier_closure_ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_frontier_closure_ledger"
CANDIDATE = DATA / "const_em_01_alpha1_frontier_closure_ledger.candidate.json"
STATUS_PACKET = BASE / "alpha1_status.packet.json"
HANDOFF = BASE / "main_repo_handoff.packet.json"
NEXT_CONSTANT = BASE / "next_constant_template.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_frontier_closure_ledger_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_FrontierClosureLedger_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_frontier_closure_ledger.py"
STATUS = "MTT_CONST_EM_01_ALPHA1_FRONTIER_CLOSURE_LEDGER_BUILT_HANDOFF_READY"


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
    status_packet = load(STATUS_PACKET)
    handoff = load(HANDOFF)
    next_constant = load(NEXT_CONSTANT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "ledger theorem not proved")
    require(all(candidate["import_checks"].values()), "import check failed")
    require(candidate["handoff_ready_for_main_repo"] is True, "handoff not ready")
    require(candidate["next_constant_ready"] is True, "next constant not ready")

    strict = status_packet["strict_no_knob"]
    require(strict["status"] == "CURRENT_CORPUS_NO_GO_FOR_NUMERICAL_PHYSICAL_ALPHA", "strict status mismatch")
    require(strict["physical_alpha_zero_or_MZ_closed"] is False, "physical alpha closed too early")
    primitive = status_packet["one_universal_primitive"]
    require(primitive["status"] == "READY_AS_EXTENSION_NOT_NO_KNOB", "primitive status mismatch")
    require("L0" in primitive["primitive_options"] and "E0" in primitive["primitive_options"], "primitive options missing")

    vals = status_packet["internal_values"]
    require(abs(vals["tau_int"] - 0.40698621549433234) < 1e-15, "tau mismatch")
    require(abs(vals["Omega0_over_sqrt_alpha_phys"] - 1.5675093859261626) < 1e-15, "Omega coefficient mismatch")
    require(abs(vals["lambda_12_internal"] - 2.6179362173268497) < 1e-15, "lambda12 mismatch")
    require(abs(vals["Delta_G12_internal"] - 0.08450302790361214) < 1e-15, "Delta mismatch")

    require(handoff["status"] == "HANDOFF_READY", "handoff status mismatch")
    require("current-corpus no-go" in handoff["recommended_main_repo_claim"], "handoff no-go missing")
    require("one-universal-primitive extension" in handoff["recommended_main_repo_claim"], "handoff primitive missing")
    require("measured alpha(0) or alpha(M_Z) is derived" in handoff["paper_insert_section"]["claims_to_forbid"], "forbidden alpha claim missing")
    require("one primitive is no-knob closure" in handoff["paper_insert_section"]["claims_to_forbid"], "forbidden primitive claim missing")

    require(next_constant["status"] == "NEXT_CONSTANT_TEMPLATE_READY", "next constant template mismatch")
    require("choose a dimensionless or ratio-like constant first" in next_constant["recommended_sequence"], "next target guidance missing")
    require(any(item["target"] == "weak mixing angle / sin^2 theta_W" for item in next_constant["candidate_next_targets"]), "weak angle target missing")

    require(cert["handoff_ready_for_main_repo"] is True, "cert handoff not ready")
    require(cert["strict_no_knob_alpha_phys_closed"] is False, "cert strict alpha overclaim")
    require(cert["strict_current_corpus_nogo"] is True, "cert no-go missing")
    require(cert["one_universal_primitive_extension_ready"] is True, "cert primitive missing")
    require("Do not claim measured `alpha(0)` or `alpha(M_Z)` is derived" in note, "note boundary missing")

    for packet in [candidate, status_packet, handoff, next_constant, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
