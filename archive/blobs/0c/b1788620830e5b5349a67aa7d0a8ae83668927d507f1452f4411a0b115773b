"""Audit Step 22 vertex-source promotion attempt and transfer-map frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step22_vertexsource_promotion_or_transfermap"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROMOTION_ATTEMPT = PACKET_DIR / "step22_vertex_source_promotion_attempt.packet.json"
READY_VALUES = PACKET_DIR / "step22_ready_to_promote_value_packet.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step22_to_step23_transfermap_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step22_VertexSourcePromotion_or_TransferMap_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP22_VERTEXSOURCE_PROMOTION_ATTEMPT_TRANSFERMAP_OPEN"
NEXT = "MTT_Selected_Step23_SourceToC1TransferMapLemma_or_SelectedValuesPromotion_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    attempt = load(PROMOTION_ATTEMPT)
    ready = load(READY_VALUES)
    next_workorder = load(NEXT_WORKORDER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    clauses = attempt["clauses"]
    for key in [
        "source_selector_emitted",
        "source_level_weyl_carrier_closed",
        "active_shift_provenance_closed",
        "sm_slot_overlap_kernel_closed",
        "conditional_atom_decomposition_exact",
    ]:
        require(clauses[key] is True, f"closed clause missing: {key}")
    for key in [
        "selected_source_to_C1_transfer_map_emitted",
        "phase_Z_routed_to_u_e_column",
        "shift_X_routed_to_d_nuD_column",
        "selected_b_selected_emitted",
        "selected_Hessian_blocks_emitted",
    ]:
        require(clauses[key] is False, f"open clause overclosed: {key}")
        require(key in attempt["blocking_clauses"], f"missing blocker: {key}")
    require(attempt["can_promote_vertex_representative_now"] is False, "promotion overclosed")

    values = ready["conditional_values"]
    require(values["A_conditional_shape"] == [72, 2], "A shape mismatch")
    require(values["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "Gram mismatch")
    require(values["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(values["deltaTheta_conditional"] == [1.0, 1.0], "delta mismatch")
    require(ready["selected_now"] is False, "ready values overpromoted")
    require(ready["if_condition_proved_then"]["selected_A_selected_promoted"] is True, "promotion consequence missing")

    decision = data["closure_decision"]
    require(decision["step22_promotion_attempt_closed"] is True, "Step22 not closed")
    require(decision["selected_source_to_C1_transfer_map_emitted"] is False, "transfer map overclosed")
    require(decision["selected_A_selected_promoted"] is False, "A overclosed")
    require(decision["selected_b_selected_promoted"] is False, "b overclosed")
    require(decision["selected_deltaTheta_C1_promoted"] is False, "delta overclosed")
    require(decision["blocking_clause_count"] == len(attempt["blocking_clauses"]), "blocker count mismatch")

    require(next_workorder["next_step"] == 23, "next step mismatch")
    require(next_workorder["closed_do_not_reopen"]["ready_to_promote_exact_values"] is True, "ready values anti-reopen missing")
    require("selected source-to-C1 response map emitted by the q79/F,m=1 branch" in next_workorder["must_prove_next"], "transfer map work item missing")

    for phrase in [
        "exact values ready to promote                        closed",
        "selected source-to-C1 transfer map",
        "A^T A = 12 I_2",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
