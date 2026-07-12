from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_protospinoralignmenttodiracmassreadout"
STATUS = "MTT_SELECTED_PROTOSPINOR_FINITE_DIRAC_READOUT_CLOSED_RADIAL_SECOND_VARIATION_OPEN"
NEXT = "MTT_Selected_NeutralRadialSecondVariationAndVEVCoordinateTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "protospinor_finite_dirac_and_alignment_readout.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_ProtoSpinorAlignmentToDiracMassReadout_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    finite = packet["finite_dirac_encoding"]
    require(finite["operator_dimension"] == 6, "Dirac dimension changed")
    require(finite["self_adjoint"] is True and finite["chirally_odd"] is True, "Dirac axioms failed")
    require(finite["selected_transfer_rank"] == 3 and abs(finite["selected_transfer_determinant"] - 2.0) < 1e-14, "transfer changed")
    require(finite["finite_Dirac_encoding_exists"] is True, "finite Dirac encoding open")
    require(finite["Dirac_only_action_completeness"] is False, "Dirac-only overclosed")
    alignment = packet["alignment_response_typing"]
    require(alignment["H1_positive_semidefinite"] is False, "H1 signature changed")
    require(alignment["H1_can_be_physical_mass_squared_Hessian"] is False, "H1 overpromoted")
    require(alignment["H2_positive_semidefinite"] is True, "H2 positivity failed")
    trial = packet["coefficient_matched_alignment_trial"]
    require(trial["nil_anchored_zero_mode"] is True, "nil mode lost")
    require(abs(trial["splitting_ratio"] - 0.25) < 1e-14, "matched ratio changed")
    require(trial["accepted_as_physical_prediction"] is False, "trial overpromoted")
    closes = packet["what_closes_here"]
    for key in ["finite_proto_spinor_to_Dirac_encoding", "left_right_Weyl_block_realization", "finite_stabilized_transfer_realization", "H1_not_mass_squared_Hessian_no_go", "coefficient_matched_nil_mode_diagnostic"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["Dirac_only_action_completeness", "selected_radial_second_variation", "selected_VEV_coordinate", "dimensionless_Y_nu_physical_readout", "dimensionful_M_D"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    require(packet["new_physical_value_fields_closed_here"] == 0, "physical value overclosed")
    for phrase in ["proto-spinor-to-Dirac encoding", "indefinite", "nil-anchored zero mode", "radial second variation", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"finite_Dirac": "closed", "H1_eigenvalues": cert["H1_eigenvalues"], "matched_singular_values": cert["coefficient_matched_singular_values"], "matched_ratio": cert["coefficient_matched_ratio"], "next": NEXT}, indent=2))
    print("selected proto-spinor alignment-to-Dirac readout audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
