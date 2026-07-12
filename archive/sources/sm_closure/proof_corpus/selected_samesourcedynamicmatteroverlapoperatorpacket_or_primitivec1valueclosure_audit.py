"""Audit same-source dynamic matter/overlap operator packet closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BACKPROMOTION = PACKET_DIR / "dynamic_transfer_backpromotion_theorem.packet.json"
SELECTED_VALUES = PACKET_DIR / "selected_non_scalar_dynamic_overlap_values.packet.json"
MATTER_PACKET = PACKET_DIR / "same_source_matter_overlap_operator_packet.packet.json"
MATTER_RESULT = PACKET_DIR / "same_source_matter_overlap_operator_validator_result.packet.json"
FULL_SM_GUARDRAIL = PACKET_DIR / "full_sm_yukawa_guardrail_after_dynamic_overlap.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_dynamic_matter_overlap_packet.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSourceDynamicMatterOverlapOperatorPacket_or_PrimitiveC1ValueClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SAMESOURCEDYNAMICMATTEROVERLAPOPERATORPACKET_OR_PRIMITIVEC1VALUECLOSURE_"
    "BUILT_DYNAMIC_MATTER_PACKET_VALIDATES_YUKAWA_MAGNITUDES_OPEN"
)
NEXT = "MTT_Selected_DynamicQaSU3OperatorPacketReplay_or_YukawaMassMixingValueClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    backpromotion = load(BACKPROMOTION)
    values = load(SELECTED_VALUES)
    matter_packet = load(MATTER_PACKET)
    matter_result = load(MATTER_RESULT)
    guardrail = load(FULL_SM_GUARDRAIL)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(backpromotion["backpromotion_allowed"] is True, "backpromotion not allowed")
    for key in [
        "selected_source_to_C1_transfer_map_emitted",
        "selected_sector_routing_dynamic_map_emitted",
        "selected_Hessian_blocks_emitted",
        "selected_b_selected_emitted",
        "conditional_non_scalar_packet_available",
        "alpha1_dotd_driver_closed",
    ]:
        require(backpromotion["new_prerequisites_after_source_and_postsource_replay"][key] is True, f"missing prerequisite {key}")

    require(values["selected_by_MTT"] is True, "selected values not promoted")
    require(values["guardrail"]["observed_flavor_data_used"] is False, "observed flavor data used")
    require(values["guardrail"]["Yukawa_magnitudes_predicted"] is False, "Yukawa magnitudes overclaimed")
    require(values["acceptance_tests"]["current_layer_flavor_tests_pass_conditionally"] is True, "qualitative tests not preserved")

    fields = matter_packet["attempted_selected_packet"]["fields"]
    for field in [
        "source_identity",
        "matter_slot_charge",
        "singlet_neutrino_rule",
        "operator_values",
        "overlap_transfer",
        "normalization",
        "primitive_contractions",
    ]:
        require(fields[field]["selected_emitted"] is True, f"{field} not emitted")
        require(fields[field]["same_source"] is True, f"{field} not same source")
        require(fields[field]["theorem_derived"] is True, f"{field} not theorem-derived")
    flags = matter_packet["attempted_selected_packet"]["packet_flags"]
    require(flags["promote_to_A_selected"] is True, "A_selected flag not promoted")
    require(flags["promote_to_b_selected"] is True, "b_selected flag not promoted")
    require(matter_result["returncode"] == 0, "matter validator should pass")
    require(any('"ok": true' in line for line in matter_result["stdout"]), "matter validator ok missing")

    require(guardrail["dynamic_matter_overlap_packet_closed"] is True, "dynamic packet not closed in guardrail")
    for key in [
        "Yukawa_magnitudes",
        "running_mass_ratios",
        "CKM_PMNS_measured_angles",
        "Higgs_RG_precision_values",
        "true_SM_equivalence",
        "full_SM_no_knob_closure",
    ]:
        require(guardrail["not_closed_here"][key] is True, f"guardrail missing {key}")
    require(data["promotion_decision"]["Yukawa_mass_mixing_value_closure"] is False, "Yukawa closure overclaimed")
    require(data["promotion_decision"]["true_SM_equivalence_closed"] is False, "true SM overclaimed")
    require(data["promotion_decision"]["full_SM_no_knob_closed"] is False, "full SM overclaimed")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    normalized_note = " ".join(note.split())
    require("does not derive measured Yukawa magnitudes" in normalized_note, "note missing Yukawa guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
