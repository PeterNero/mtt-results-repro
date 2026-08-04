"""Audit selected_matterslot_readout_backimport_from_smslotfunctor."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_matterslot_readout_backimport_from_smslotfunctor"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
READOUT = PACKET_DIR / "selected_static_matterslot_readout.packet.json"
DYNAMIC = PACKET_DIR / "dynamic_operator_boundary_after_readout.packet.json"
DECISION = PACKET_DIR / "readout_promotion_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MatterSlotReadout_BackimportFromSMSlotFunctor_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    readout = load(READOUT)
    dynamic = load(DYNAMIC)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_MATTERSLOT_READOUT_BACKIMPORT_BUILT_STATIC_READOUT_CLOSED_DYNAMIC_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["SM_parity_closed"] is True, "SM parity regressed")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(readout["status"] == "STATIC_SOURCE_TIER_READOUT_CLOSED", "readout not closed")
    for key in [
        "selected_10M_clock_readout",
        "selected_bar5M_shift_readout",
        "selected_1M_Dirac_shift_readout",
        "selected_phase_shift_partition",
        "selected_overlap_transfer_normalization_static",
    ]:
        require(readout["selected_readouts"][key]["closed"] is True, f"readout missing {key}")
    require(readout["selected_readouts"]["selected_phase_shift_partition"]["phase"] == ["u", "e"], "phase route mismatch")
    require(readout["selected_readouts"]["selected_phase_shift_partition"]["shift"] == ["d", "nuD"], "shift route mismatch")
    require(all(readout["forbidden_inputs_absent"].values()), "forbidden input present")

    require(dynamic["static_sm_slot_tier_closed"] is True, "static tier not closed")
    require(dynamic["dynamic_operator_c1_tier_closed"] is False, "dynamic tier overclosed")
    require(dynamic["not_promoted_by_this_artifact"]["A_selected"] is True, "A_selected overpromoted")
    require(dynamic["not_promoted_by_this_artifact"]["selected_b_selected_and_Hessian_normalization"] is True, "b_selected overpromoted")

    require(decision["all_six_smslot_arrows_closed"] is True, "SM-slot arrows not closed")
    require(decision["old_rho_s_invariant_nogo_preserved"] is True, "rho_s no-go lost")
    require(decision["selected_matter_slot_grading_readout_closed_static"] is True, "grading not promoted static")
    require(decision["dynamic_C1_promoted"] is False, "dynamic C1 overpromoted")
    require(cert["static_readout_closed"] is True, "cert readout not closed")
    require(cert["dynamic_C1_promoted"] is False, "cert dynamic overpromoted")
    require(data["next_required_artifact"] == "MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1", "wrong next artifact")
    require("That no-go still stands" in note, "note missing no-go preservation")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
