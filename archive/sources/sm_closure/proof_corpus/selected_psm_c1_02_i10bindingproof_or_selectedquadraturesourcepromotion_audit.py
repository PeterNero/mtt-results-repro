"""Audit PSM-C1-02 I10 binding proof or selected quadrature source promotion."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_02_i10bindingproof_or_selectedquadraturesourcepromotion"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A_CURRENT = PACKET_DIR / "route_a_current_i10_binding_stack_attempt.packet.json"
ROUTE_A_CONDITIONAL = PACKET_DIR / "route_a_conditional_i10_binding_stack_witness.packet.json"
ROUTE_A_CURRENT_RESULT = PACKET_DIR / "route_a_current_i10_binding_stack_validator_result.packet.json"
ROUTE_A_CONDITIONAL_RESULT = PACKET_DIR / "route_a_conditional_i10_binding_stack_validator_result.packet.json"
ROUTE_B_CURRENT = PACKET_DIR / "route_b_current_independent_quadrature_payload_attempt.packet.json"
ROUTE_B_CONDITIONAL = PACKET_DIR / "route_b_conditional_selected_quadrature_source_promotion_witness.packet.json"
ROUTE_B_CURRENT_RESULT = PACKET_DIR / "route_b_current_independent_quadrature_payload_validator_result.packet.json"
ROUTE_B_CONDITIONAL_RESULT = PACKET_DIR / "route_b_conditional_independent_quadrature_payload_validator_result.packet.json"
REDUCTION = PACKET_DIR / "psm_c1_02_dual_validator_reduction.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_I10BindingProof_or_SelectedQuadratureSourcePromotion_v1.md"
I10_VALIDATOR = ROOT / "scripts" / "validate_selected_i10_binding_stack.py"
ROUTEB_VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_independent_quadrature_payload.py"

STATUS = "MTT_SELECTED_PSM_C1_02_I10BINDINGPROOF_OR_SELECTEDQUADRATURESOURCEPROMOTION_BUILT_SOURCE_PROMOTION_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validator_returncode(validator: Path, payload: Path) -> int:
    proc = subprocess.run(
        [sys.executable, str(validator), str(payload)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return proc.returncode


def main() -> int:
    data = load(DATA)
    route_a_current = load(ROUTE_A_CURRENT)
    route_a_conditional = load(ROUTE_A_CONDITIONAL)
    route_a_current_result = load(ROUTE_A_CURRENT_RESULT)
    route_a_conditional_result = load(ROUTE_A_CONDITIONAL_RESULT)
    route_b_current = load(ROUTE_B_CURRENT)
    route_b_conditional = load(ROUTE_B_CONDITIONAL)
    route_b_current_result = load(ROUTE_B_CURRENT_RESULT)
    route_b_conditional_result = load(ROUTE_B_CONDITIONAL_RESULT)
    reduction = load(REDUCTION)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "status mismatch")
    require(data["active_post_sm_parity_label"] == "PSM-C1-02", "active label mismatch")
    require(data["post_sm_parity_label_context"]["closed_boundary"] == "DONE-PARITY-00", "closed boundary missing")
    require(data["theorem"]["proved"] is True, "theorem not marked proved")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")

    require(route_a_current["route_label"] == "ROUTE-A", "Route A current label mismatch")
    require(route_a_conditional["route_label"] == "ROUTE-A", "Route A conditional label mismatch")
    require(route_a_current_result["passes"] is False, "current Route A should fail")
    require(route_a_conditional_result["passes"] is True, "conditional Route A should pass")
    require(validator_returncode(I10_VALIDATOR, ROUTE_A_CURRENT) == 1, "current Route A validator return changed")
    require(validator_returncode(I10_VALIDATOR, ROUTE_A_CONDITIONAL) == 0, "conditional Route A validator return changed")

    require(route_b_current["route_label"] == "ROUTE-B", "Route B current label mismatch")
    require(route_b_conditional["route_label"] == "ROUTE-B", "Route B conditional label mismatch")
    require(route_b_conditional["conditional_only"] is True, "Route B conditional must be conditional")
    require(route_b_conditional["symbolic_values_only"] is True, "Route B conditional must be symbolic")
    require(route_b_conditional["not_a_numerical_derivation"] is True, "Route B conditional overstates derivation")
    require(len(route_b_conditional["rows"]) == 110, "Route B conditional row count mismatch")
    require(route_b_current_result["passes"] is False, "current Route B should fail")
    require(route_b_conditional_result["passes"] is True, "conditional Route B should pass")
    require(validator_returncode(ROUTEB_VALIDATOR, ROUTE_B_CURRENT) == 1, "current Route B validator return changed")
    require(validator_returncode(ROUTEB_VALIDATOR, ROUTE_B_CONDITIONAL) == 0, "conditional Route B validator return changed")

    require(reduction["route_A"]["current_passes"] is False, "reduction overclaims Route A")
    require(reduction["route_A"]["conditional_passes"] is True, "reduction missing conditional Route A")
    require(reduction["route_B"]["current_passes"] is False, "reduction overclaims Route B")
    require(reduction["route_B"]["conditional_passes"] is True, "reduction missing conditional Route B")
    require(reduction["route_B"]["strict_required_row_count"] == 110, "strict Route B row count mismatch")
    require("same-branch selected C1 source-promotion packet" in reduction["common_remaining_object"], "common remaining object not sharp")

    require(next_work["active_label"] == "PSM-C1-02", "next work active label mismatch")
    require(next_work["next_required_artifact"] == data["next_required_artifact"], "next artifact mismatch")
    require(cert["closure_claimed"] is False, "certificate overclaimed closure")
    require(cert["current_route_A_passes"] is False, "certificate overclaims current Route A")
    require(cert["conditional_route_A_passes"] is True, "certificate misses conditional Route A")
    require(cert["current_route_B_passes"] is False, "certificate overclaims current Route B")
    require(cert["conditional_route_B_passes"] is True, "certificate misses conditional Route B")
    require("post-SM-parity frontier" in note, "note missing frontier language")
    require("not an SM-parity blocker" in note, "note missing boundary guardrail")
    require("not a fresh numerical search" in note, "note missing numerical-search guardrail")

    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
