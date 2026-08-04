from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralcommoncirclefactorizationandholonomyscalarreduction"
STATUS = "MTT_SELECTED_NEUTRAL_COMMON_CIRCLE_FACTORIZATION_CLOSED_CENTRAL_HOLONOMY_AND_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralCentralHolonomyValueAndAnchoredHessianScale_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_common_circle_factorization.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralCommonCircleFactorizationAndHolonomyScalarReduction_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    h = packet["selected_common_circle_operator"]
    require(h["symbolic"] == "diag(1, zeta_3, zeta_3^2)", "Hcen changed")
    require(h["order"] == 3 and h["source_level_emitted"] is True, "Hcen source missing")
    factor = packet["neutral_factorization"]
    require(factor["transfer_functor_closed"] is True, "transfer not closed")
    require(factor["independent_shape_scalar_count"] == 1, "shape count changed")
    witness = packet["numeric_identity_witness"]
    require(all(abs(a-b)<1e-12 for a,b in zip(witness["real_parts_of_expiphi_Hcen"], witness["cosine_orbit"])), "cosine identity failed")
    require(abs(witness["recovered_phi_mod_2pi_over_3"] - witness["phi_test"]) < 1e-12, "det phase recovery failed")
    boundary = packet["value_boundary"]
    require(boundary["Hcen_supplies_relative_family_offsets"] is True, "relative orbit missing")
    for key in ["Hcen_supplies_common_neutral_phase", "neutral_operator_Hnu_emitted", "neutral_determinant_emitted", "phi_nu_value_emitted", "anchored_Hessian_scale_mu_nu_emitted"]:
        require(boundary[key] is False, f"overclosed: {key}")
    require(packet["reduced_physical_cutset"]["count"] == 2, "cutset count changed")
    closes = packet["what_closes_here"]
    for key in ["selected_Z3_common_circle_family_operator", "common_circle_to_proto_spinor_three_basin_transfer", "single_scalar_nil_holonomy_reduction"]:
        require(closes[key] is True, f"not closed: {key}")
    for key in ["phi_nu_value", "mu_nu_value", "dimensionful_neutral_masses"]:
        require(closes[key] is False, f"overclosed: {key}")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    for phrase in ["H_cen = diag", "H_nu(phi_nu)", "det H_nu", "Setting `phi_nu=0`", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"Hcen_order": cert["Hcen_order"], "transfer_closed": cert["common_circle_to_three_basin_transfer_closed"], "shape_scalars": cert["independent_shape_scalar_count"], "next": NEXT}, indent=2))
    print("neutral common-circle factorization audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
