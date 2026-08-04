"""Audit independent C1 row-kernel source ids or physical Phi_fin^C1 action proof attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_independentc1_rowkernelsourceids_or_physicalphifinc1actionproof"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT_IDS = PACKET_DIR / "current_rowkernel_source_id_attempt.packet.json"
CONDITIONAL_IDS = PACKET_DIR / "conditional_independent_rowkernel_source_id_witness.packet.json"
CURRENT_VALIDATION = PACKET_DIR / "current_source_id_validator_result.packet.json"
CONDITIONAL_VALIDATION = PACKET_DIR / "conditional_source_id_validator_result.packet.json"
BRIDGE_VALIDATION = PACKET_DIR / "two_exit_bridge_after_source_ids_validator_result.packet.json"
DECISION = PACKET_DIR / "source_ids_or_actionproof_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_IndependentC1RowKernelSourceIds_or_PhysicalPhiFinC1ActionProof_v1.md"

STATUS = "MTT_SELECTED_INDEPENDENTC1_ROWKERNELSOURCEIDS_OR_PHYSICALPHIFINC1ACTIONPROOF_BUILT_IDS_SUPPORT_ONLY"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    current_ids = load(CURRENT_IDS)
    conditional_ids = load(CONDITIONAL_IDS)
    current_validation = load(CURRENT_VALIDATION)
    conditional_validation = load(CONDITIONAL_VALIDATION)
    bridge_validation = load(BRIDGE_VALIDATION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "unexpected candidate status")
    require(cert["status"] == STATUS, "unexpected certificate status")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["target_fitting_used"] is False, "candidate uses target fitting")
    require(len(current_ids["primitive_row_kernel_sources"]) == 72, "primitive id count mismatch")
    require(len(current_ids["hessian_b_sources"]) == 2, "hessian id count mismatch")
    require(len(current_ids["sector_assembly_sources"]) == 36, "sector id count mismatch")
    require(current_validation["ok"] is False and current_validation["exit_code"] == 1, "current ids should fail")
    require(
        any("theorem_derived must be true" in line for line in current_validation["stderr"]),
        "current validation should fail on theorem derivation",
    )
    require(conditional_validation["ok"] is True, "conditional ids should pass")
    require(conditional_ids["global_sources"]["selected_quadrature_rule"]["theorem_derived"] is True, "conditional quadrature missing")
    require(bridge_validation["ok"] is False, "actual two-exit bridge should remain open")
    require(decision["current_source_id_validator_ok"] is False, "decision overpromotes current ids")
    require(decision["conditional_source_id_validator_ok"] is True, "decision lost conditional witness")
    require(decision["counts"]["primitive_source_ids"] == 72, "decision primitive count mismatch")
    require("support-only rather than theorem-derived" in note, "note missing source-id guard")

    print(proc.stdout.strip())
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
