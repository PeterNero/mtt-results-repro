from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralphysicalunitornilanchorprojector"
STATUS = "MTT_SELECTED_NEUTRAL_COMMON_SCALE_ROUTE_REJECTED_SPECTRAL_ACTION_OR_SEESAW_REQUIRED"
NEXT = "MTT_Selected_NeutralSpectralActionSlopeOrSeesawSource_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_scale_invariant_obstruction_and_spectral_repair.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralPhysicalUnitOrNilAnchorProjector_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem not proved")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    obstruction = packet["scale_invariant_obstruction"]
    require(obstruction["selected_internal_hermitian_spectrum"] == [1.0, 4.0, 7.0], "spectrum changed")
    require(obstruction["nil_shifted_spectrum"] == [0.0, 3.0, 6.0], "nil spectrum changed")
    require(obstruction["direct_nil_shift_ratio"] == 0.5, "direct ratio changed")
    require(0.029 < obstruction["normal_ordering_postcheck_ratio"] < 0.031, "postcheck ratio changed")
    require(obstruction["common_rescaling_changes_ratio"] is False, "rescaling invariant lost")
    require(obstruction["simple_M_D_equals_common_scale_times_selected_orbit_rejected"] is True, "simple route not rejected")

    repair = packet["minimal_nonlinear_repair_contract"]
    require(repair["free_dimensionless_shape_parameters"] == 1, "shape count changed")
    require(repair["free_dimensionful_scale_parameters"] == 1, "scale count changed")
    require(abs(repair["reconstructed_ratio_diagnostic"] - obstruction["normal_ordering_postcheck_ratio"]) < 1e-15, "repair algebra failed")
    require(repair["exact_source_beta_emitted"] is False and repair["physical_scale_C_emitted"] is False, "diagnostic overpromoted")
    require(repair["accepted_as_prediction"] is False, "diagnostic accepted as prediction")

    closes = packet["what_closes_here"]
    for key in ["common_scale_invariance_theorem", "nil_shifted_selected_orbit_ratio", "simple_scale_only_physical_route_rejected", "minimal_two_parameter_spectral_repair_contract"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["selected_spectral_action_slope_beta", "selected_physical_scale_C", "nil_boundary_source_promotion", "Dirac_only_action_completeness", "selected_Majorana_seesaw_blocks"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["neutral_overlap_OK_gates_closed"] == 6 and packet["neutral_overlap_OK_gates_total"] == 9, "OK count changed")
    require(packet["readiness_subfields_closed"] == 9 and packet["readiness_subfields_total"] == 14, "readiness changed")
    require(packet["new_physical_value_fields_closed_here"] == 0, "physical values overclosed")
    require(packet["accepted_route_exit_count"] == 0, "route overaccepted")
    for phrase in ["`[1,4,7]`", "`[0,3,6]`", "one common", "one dimensionless action slope", "diagnostic values, not selected source rows", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"selected_spectrum": [1,4,7], "nil_shifted": [0,3,6], "direct_ratio": 0.5, "postcheck_ratio": obstruction["normal_ordering_postcheck_ratio"], "minimal_repair_parameters": "1 shape + 1 scale", "accepted_physical_rows": 0, "next": NEXT}, indent=2))
    print("selected neutral physical-unit / nil-anchor obstruction audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
