"""Audit selected_physicalphifinc1action_or_independentrowkernelsource_theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TEMPLATE = PACKET_DIR / "two_exit_source_theorem.strict_template.json"
CURRENT = PACKET_DIR / "current_two_exit_source_attempt.packet.json"
CUTSET = PACKET_DIR / "remaining_source_theorem_cutset.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalPhiFinC1Action_or_IndependentRowKernelSource_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    template = load(TEMPLATE)
    current = load(CURRENT)
    cutset = load(CUTSET)
    validator_result = load(VALIDATOR_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(CURRENT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_PHYSICALPHIFINC1ACTION_OR_INDEPENDENTROWKERNELSOURCE_THEOREM_BUILT_BOTH_EXITS_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "two-exit theorem not proved")
    require(len(template["route_A_physical_action_restriction_required_fields"]) == 5, "Route A field count mismatch")
    require(len(template["route_B_independent_rowkernel_source_required_fields"]) == 5, "Route B field count mismatch")
    require(current["route_A_physical_action_restriction"]["physical_action_restricts_to_finite_weyl_quotient"] is False, "Route A overfilled")
    require(current["route_B_independent_rowkernel_source"]["selected_basis_feeds_all_72_row_functionals"] is False, "Route B overfilled")
    require(cutset["validator_rejects_current_attempt"] is True, "cutset should record rejection")
    require(cutset["route_A_minimal_new_payload"]["name"] == "same-branch physical Phi_fin^C1 action rows", "Route A payload mismatch")
    require(cutset["route_B_minimal_new_payload"]["name"] == "independent selected row-kernel source rows", "Route B payload mismatch")
    require(proc.returncode == 1, "strict two-exit validator should reject")
    require(validator_result["returncode"] == 1, "recorded validator should reject")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(cert["validator_rejects_current_attempt"] is True, "cert should record rejection")
    require("strict two-exit" in note, "note missing two-exit statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
