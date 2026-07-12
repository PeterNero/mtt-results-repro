"""Audit PSM-C1-02 physical action identity or honest quadrature emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_02_physicalactionidentity_or_honestquadratureemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_i10_physical_action_identity_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_quadrature_emission_attempt.packet.json"
TWO_EXIT = PACKET_DIR / "psm_c1_02_current_two_exit_validator_payload.packet.json"
TWO_EXIT_RESULT = PACKET_DIR / "psm_c1_02_current_two_exit_validator_result.packet.json"
CONDITIONAL_A_RESULT = PACKET_DIR / "conditional_route_a_validator_result.packet.json"
CONDITIONAL_B_RESULT = PACKET_DIR / "conditional_route_b_validator_result.packet.json"
EQUIV = PACKET_DIR / "psm_c1_02_closure_equivalence.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_PhysicalActionIdentity_or_HonestQuadratureEmission_v1.md"
TWO_EXIT_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"

STATUS = "MTT_SELECTED_PSM_C1_02_PHYSICALACTIONIDENTITY_OR_HONESTQUADRATUREEMISSION_BUILT_EQUIVALENCE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    two_exit = load(TWO_EXIT)
    two_exit_result = load(TWO_EXIT_RESULT)
    conditional_a = load(CONDITIONAL_A_RESULT)
    conditional_b = load(CONDITIONAL_B_RESULT)
    equiv = load(EQUIV)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(TWO_EXIT_VALIDATOR), str(TWO_EXIT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    require(data["status"] == STATUS, "status mismatch")
    require(data["active_post_sm_parity_label"] == "PSM-C1-02", "active label mismatch")
    require(data["post_sm_parity_label_context"]["closed_boundary"] == "DONE-PARITY-00", "closed boundary missing")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["PSM_C1_02_closed_unpatched"] is False, "PSM-C1-02 overclosed")
    require(route_a["route_label"] == "ROUTE-A", "Route A label mismatch")
    require(route_a["physical_action_equals_c1_defect_functional"] is False, "Route A overclosed")
    require(route_a["admissible_differentiated_variations_fixed"] is True, "admissible variations should be fixed")
    require(route_b["route_label"] == "ROUTE-B", "Route B label mismatch")
    require(route_b["source_namespace_counts"] == {"primitive_source_ids": 72, "hessian_b_source_ids": 2, "sector_assembly_source_ids": 36}, "source-id counts mismatch")
    require(route_b["current_primitive_sources_selected"] is False, "current primitive sources overpromoted")
    require(route_b["conditional_source_ids_validate"] is True, "conditional source ids should validate")
    require(two_exit_result["passes"] is False and proc.returncode == 1, "current two-exit payload should fail")
    require(conditional_a["passes"] is True, "conditional Route A should pass")
    require(conditional_b["passes"] is True, "conditional Route B should pass")
    require(equiv["current_two_exit_validator_passes"] is False, "equiv overclaims current pass")
    require(equiv["conditional_route_A_validator_passes"] is True, "equiv missing Route A conditional pass")
    require(equiv["conditional_route_B_validator_passes"] is True, "equiv missing Route B conditional pass")
    require(next_work["active_label"] == "PSM-C1-02", "next active label mismatch")
    require(next_work["primary"]["route_label"] == "ROUTE-A", "next primary route mismatch")
    require(next_work["secondary"]["route_label"] == "ROUTE-B", "next secondary route mismatch")
    require(cert["closure_claimed"] is False, "cert overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("Active post-SM-parity label: `PSM-C1-02`" in note, "note missing active label")
    require("not an SM-parity blocker" in note, "note missing frozen boundary language")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
