"""Audit Weyl-pair dynamic-overlap promotion / honest Galerkin C1 cutset import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill_import.candidate.json"
CERT = ROOT / "certificates" / "weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill.py"

STATUS = "WEYLPAIR_DYNAMIC_OVERLAP_PROMOTION_CUTSET_IMPORTED_OPEN"
NEXT = "Selected_U1Y_RouteC_DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    lane_a = data["lane_A_dynamic_source_promotion"]
    require(lane_a["conditional_transfer_exact"] is True, "Lane A transfer not exact")
    require(lane_a["conditional_transfer_residuals"]["phase_residual"] == 0.0, "phase residual")
    require(lane_a["conditional_transfer_residuals"]["shift_residual"] == 0.0, "shift residual")
    require(all(lane_a["conditional_packet_tests_pass"].values()), "conditional tests failed")
    require(lane_a["promoted"] is False, "Lane A overpromoted")
    require(all(value is False for value in lane_a["selected_promotion_fields"].values()), "Lane A fields emitted")

    lane_b = data["lane_B_honest_Galerkin_C1_value_fill"]
    require(
        lane_b["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
        "Lane B manifest mismatch",
    )
    require(lane_b["selected_source_verified"] is False, "Lane B source verified")
    require(lane_b["promoted"] is False, "Lane B overpromoted")
    require(all(value is False for value in lane_b["required_outputs_present"].values()), "Lane B output emitted")

    cutset = data["minimum_cutset"]
    require(cutset["static_routing_no_longer_in_cutset"] is True, "static routing still in cutset")
    require(cutset["observed_flavor_data_forbidden_as_selector"] is True, "observed selector guard missing")
    require("selected_b_selected" in cutset["lane_A_fill_all"], "Lane A missing b")
    require("linear_response_matrices" in cutset["lane_B_fill_all"], "Lane B missing linear responses")

    decision = data["promotion_decision"]
    require(decision["static_source_route_retired_as_blocker"] is True, "static route not retired")
    require(decision["conditional_non_scalar_packet_available"] is True, "packet unavailable")
    require(decision["dynamic_promotion_cutset_open"] is True, "cutset not open")
    for key in [
        "selected_dynamic_overlap_promoted",
        "selected_full_response_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
        "selected_Galerkin_C1_contractions_promoted",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    guardrails = data["guardrails"]
    require(guardrails["static_source_tier_closed"] is True, "static tier not closed")
    require(guardrails["conditional_non_scalar_transfer_exact"] is True, "conditional transfer missing")
    require(guardrails["selected_dynamic_overlap_tensor_claimed"] is False, "dynamic tensor claimed")
    require(guardrails["selected_full_response_claimed"] is False, "full response claimed")
    require(guardrails["selected_A_selected_claimed"] is False, "A selected claimed")
    require(guardrails["selected_b_selected_claimed"] is False, "b selected claimed")
    require(guardrails["honest_Galerkin_C1_contractions_claimed"] is False, "Galerkin claimed")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")
    require(guardrails["full_SM_closure_claimed"] is False, "closure claimed")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
