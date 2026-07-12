from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_classlaneprojectorsandweakrealstructuresourcetheorem"
STATUS = "MTT_SELECTED_NATIVE_RANK_FLAG_AND_WEAK_REAL_STRUCTURE_CLOSED_CLASS_LANE_GAUGE_TYPE_MISMATCH_PROVED"
NEXT = "MTT_Selected_TypedFamilyGaugeCarrierAndDiagonalSMRepresentationTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "class_lane_projectors_and_weak_real_structure.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_ClassLaneProjectorsAndWeakRealStructureSourceTheorem_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    require(cert["native_rank_flag_closed_up_to_unitary_equivalence"] is True, "native flag open")
    require(cert["weak_real_structure_closed_up_to_unitary_phase_equivalence"] is True, "weak J open")
    require(cert["finite_qutrit_to_native_flag_identification_closed"] is False, "missing intertwiner hidden")
    require(cert["dirac_weyl_twistor_common_carrier_closed"] is True, "common carrier reopened")
    require(cert["dirac_weyl_twistor_strict_same_value_packet_closed"] is False, "same-value theorem overclosed")
    require((cert["same_source_fields_closed"], cert["same_source_fields_total"]) == (4, 9), "same-source count changed")
    require(packet["source_promotion"]["rank1_rank2_rank3_matrix_representatives_are_free_knobs"] is False, "basis representatives counted as knobs")
    require(packet["source_promotion"]["old_identification_premise_rejected_by_type_check"] is True, "family/gauge type mismatch hidden")
    require(packet["typed_carrier_correction"]["family_factor_must_be_preserved"] is True, "family factor not preserved")
    require(packet["typed_carrier_correction"]["A44_class_lane_assignment_as_physical_SM_representation"] is False, "A44 physical assignment overclosed")
    require(packet["epistemic_policy"]["observed_SM_values_used"] is False, "observed values entered theorem")
    for phrase in ["coordinate representatives", "not an empirical knob", "family/character index", "inequivalent gauge algebras", "same-value dynamical theorem", "4/9", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("class-lane projector and weak-real-structure source audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
