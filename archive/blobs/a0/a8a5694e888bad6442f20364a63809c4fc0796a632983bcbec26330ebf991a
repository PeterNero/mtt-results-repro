"""Audit Step 23 static-routing transfer-map reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step23_staticrouting_transfermapreduction"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTING_PACKET = PACKET_DIR / "step23_static_routing_reconciliation.packet.json"
TRANSFER_PACKET = PACKET_DIR / "step23_transfer_map_reduced_dynamic_overlap.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step23_to_step24_dynamic_overlap_bhessian_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step23_StaticRouting_TransferMapReduction_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP23_STATIC_ROUTING_CLOSED_TRANSFERMAP_REDUCED_DYNAMIC_OVERLAP_BHESSIAN_OPEN"
NEXT = "MTT_Selected_Step24_DynamicOverlapTensor_BHessian_or_SelectedValuesPromotion_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    routing = load(ROUTING_PACKET)
    transfer = load(TRANSFER_PACKET)
    next_workorder = load(NEXT_WORKORDER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(routing["older_attempt_superseded_for_static_routing"] is True, "old attempt not superseded")
    later = routing["later_static_routing_source_emission"]
    require(later["proved"] is True, "later routing not proved")
    require(later["phase_route"] == ["u", "e"], "phase route mismatch")
    require(later["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(later["selected_static_sector_route"] is True, "static route not selected")
    require(later["selected_static_trace_transfer_normalization"] is True, "trace norm not selected")
    closed = routing["closed_for_step23"]
    for key in [
        "phase_Z_routed_to_u_e_column",
        "shift_X_routed_to_d_nuD_column",
        "selected_static_sector_routing",
        "selected_static_trace_normalization",
    ]:
        require(closed[key] is True, f"routing closure missing: {key}")
    not_closed = routing["not_closed_by_static_routing"]
    for key in [
        "dynamic_source_to_C1_overlap_tensor",
        "primitive_C1_contractions",
        "selected_b_selected_and_Hessian_normalization",
        "selected_A_selected",
    ]:
        require(not_closed[key] is True, f"static routing overclosed: {key}")

    require(transfer["conditional_transfer_map"]["conditional_exact"] is True, "conditional map not exact")
    require(transfer["can_promote_A_selected_now"] is False, "A overpromoted")
    for key in [
        "selected_source_to_C1_transfer_map_emitted",
        "selected_dynamic_overlap_tensor_or_transfer_functor",
        "selected_primitive_C1_contractions",
        "selected_b_selected_emitted",
        "selected_Hessian_blocks_emitted",
    ]:
        require(key in transfer["step23_blockers_after"], f"missing blocker after Step23: {key}")

    decision = data["closure_decision"]
    require(decision["step23_static_routing_closed"] is True, "Step23 not closed")
    require(decision["phase_Z_routed_to_u_e_column"] is True, "candidate phase route missing")
    require(decision["shift_X_routed_to_d_nuD_column"] is True, "candidate shift route missing")
    require(decision["selected_source_to_C1_transfer_map_emitted"] is False, "transfer map overclosed")
    require(decision["selected_dynamic_overlap_tensor_or_transfer_functor"] is False, "dynamic overlap overclosed")
    require(decision["selected_b_selected_promoted"] is False, "b overclosed")
    require(decision["selected_A_selected_promoted"] is False, "A overclosed")

    require(next_workorder["next_step"] == 24, "next step mismatch")
    require(next_workorder["closed_do_not_reopen"]["static_sector_routing_Z_to_u_e_X_to_d_nuD"] is True, "routing anti-reopen missing")
    require("selected dynamic source-to-C1 overlap tensor or transfer functor" in next_workorder["must_emit_next"], "next dynamic target missing")

    for phrase in [
        "Z / phase / clock routes to u,e                         closed",
        "selected dynamic source-to-C1 overlap tensor or transfer functor",
        "dynamic overlap/b-Hessian layer",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
