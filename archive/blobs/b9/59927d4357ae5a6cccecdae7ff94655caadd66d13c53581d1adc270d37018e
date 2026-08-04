"""Audit unpatched source-promotion replay after symbolic Phi_fin closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RESULTS = [
    PACKET_DIR / "physical_action_rowkernel_source_validator_result.packet.json",
    PACKET_DIR / "narrowed_phifinc1_emission_validator_result.packet.json",
    PACKET_DIR / "action_kernel_theorem_validator_result.packet.json",
    PACKET_DIR / "psm_c1_02_source_promotion_validator_result.packet.json",
]
SUMMARY = PACKET_DIR / "unpatched_source_promotion_replay_summary.packet.json"
FULL_SM_GATE = PACKET_DIR / "full_sm_closure_gate_after_source_promotion.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_unpatched_source_promotion_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_UnpatchedSourcePromotionReplay_or_FullSMClosureGate_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_UNPATCHEDSOURCEPROMOTIONREPLAY_OR_FULLSMCLOSUREGATE_BUILT_SOURCE_STACK_PROMOTED_FULLSM_OPEN"
NEXT = "MTT_Selected_PostSourcePromotionFullSMGapAudit_or_DotDAlpha1MatterRoutingClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    summary = load(SUMMARY)
    full_sm_gate = load(FULL_SM_GATE)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    for result_path in RESULTS:
        result = load(result_path)
        require(result["returncode"] == 0, f"validator failed: {result_path.name}")
        require(any("PASS" in line for line in result["stdout"]), f"PASS missing: {result_path.name}")

    promoted = summary["promoted_objects"]
    require(summary["status"] == "UNPATCHED_SOURCE_PROMOTION_STACK_VALIDATES", "summary did not validate")
    require(promoted["A_selected"] is True, "A_selected not promoted")
    require(promoted["b_selected"] is True, "b_selected not promoted")
    require(promoted["deltaTheta_C1"] is True, "deltaTheta_C1 not promoted")
    require(promoted["SelectedFiniteC1SourceIdentityTheorem"] is True, "source identity not promoted")

    require(full_sm_gate["source_stack_closed"] is True, "source stack not closed")
    require(full_sm_gate["full_SM_no_knob_closed"] is False, "full SM overclosed")
    require(full_sm_gate["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require("Yukawa/mass/mixing value closure without proxy fitting" in full_sm_gate["remaining_gates"], "Yukawa gap missing")
    require(data["promotion_decision"]["unpatched_source_promotion_stack_closed"] is True, "source stack not promoted")
    require(data["promotion_decision"]["full_SM_no_knob_closed"] is False, "candidate overclosed full SM")
    require(data["promotion_decision"]["Yukawa_mass_mixing_value_closure"] is False, "Yukawa overclosed")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("This is not full SM closure" in note, "note missing full SM guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
