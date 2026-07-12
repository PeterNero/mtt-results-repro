"""Audit physical Phi_fin^C1 action identity or independent row-source export gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalphifinc1actionidentity_or_independentrowsourceexport"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT_VALIDATION = PACKET_DIR / "current_source_export_validator_result.packet.json"
ROUTE_A_VALIDATION = PACKET_DIR / "conditional_route_a_validator_result.packet.json"
ROUTE_B_VALIDATION = PACKET_DIR / "conditional_route_b_validator_result.packet.json"
CONTRACT = PACKET_DIR / "source_export_acceptance_contract.packet.json"
CUTSET = PACKET_DIR / "remaining_export_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalPhiFinC1ActionIdentity_or_IndependentRowSourceExport_v1.md"

STATUS = "MTT_SELECTED_PHYSICALPHIFINC1_ACTIONIDENTITY_OR_INDEPENDENTROWSOURCEEXPORT_BUILT_CONDITIONAL_EXITS_VERIFIED"


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
    current = load(CURRENT_VALIDATION)
    route_a = load(ROUTE_A_VALIDATION)
    route_b = load(ROUTE_B_VALIDATION)
    contract = load(CONTRACT)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "unexpected candidate status")
    require(cert["status"] == STATUS, "unexpected cert status")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["target_fitting_used"] is False, "candidate uses target fitting")
    require(candidate["observed_data_used_as_selector"] is False, "candidate uses observed selector")
    require(current["ok"] is False and current["exit_code"] == 1, "current attempt should fail")
    require(
        any("neither Route A nor Route B validates" in line for line in current["stderr"]),
        "current validator rejection missing",
    )
    require(route_a["ok"] is True and route_a["exit_code"] == 0, "Route A conditional witness should pass")
    require(route_b["ok"] is True and route_b["exit_code"] == 0, "Route B conditional witness should pass")
    require(contract["route_A_acceptance"]["validates_when_all_fields_supplied"] is True, "Route A contract broken")
    require(contract["route_B_acceptance"]["validates_when_all_fields_supplied"] is True, "Route B contract broken")
    require(contract["shared_locked_target_policy"]["conditional_witnesses_are_not_actual_closure"] is True, "conditional guard missing")
    require(cutset["current_validator_ok"] is False, "cutset should keep current open")
    require(cutset["route_A_conditional_validator_ok"] is True, "cutset missing Route A conditional")
    require(cutset["route_B_conditional_validator_ok"] is True, "cutset missing Route B conditional")
    require("actual current packet still fails" in note, "note missing actual failure")
    require("conditional witnesses" in note, "note missing conditional guard")

    print(proc.stdout.strip())
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
