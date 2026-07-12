"""Audit the first non-identity rho_E / B_N numerical construction."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"
CERT = REPO / "certificates" / "selected_routec_nonidentity_rhoe_bn_construction_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    rho = data["rho_E_candidate"]
    gates = rho["numeric_gates"]
    basis = data["B_N_scaffold"]
    straight = data["superset_mode"]["straight_path"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_NONIDENTITY_RHOE_NUMERICAL_PACKET_BUILT_BN_STILL_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("rho packet passes", gates["passes_numeric_packet_gate"] is True, gates),
        check("rho nonidentity", gates["nonidentity_norm"] > 0.1, gates["nonidentity_norm"]),
        check(
            "rho exact enough",
            gates["unitary_residual_max"] < 1e-10
            and gates["order3_residual_max"] < 1e-10
            and gates["projective_commutator_residual"] < 1e-10,
            gates,
        ),
        check(
            "selected deck used",
            gates["uses_only_selected_active_generators_g1_g2"] is True
            and gates["kernel_generators_identity"] is True,
            gates,
        ),
        check(
            "source not overclaimed",
            rho["selected_by_mtt"] is False
            and data["what_remains_open"]["R2_source_promotion_for_rhoE"] is True,
            rho,
        ),
        check(
            "BN scaffold not payload",
            basis["quotient_constraints_encoded"] is True
            and basis["passes_B_N_payload_gate"] is False
            and basis["smooth_scalar_basis_phi_m_emitted"] is False,
            basis,
        ),
        check(
            "straight partial",
            straight["nonidentity_projective_rhoE_packet_built"] is True
            and straight["BN_payload_built"] is False
            and straight["honest_replay_ready"] is False,
            straight,
        ),
        check("no target fitting", data["target_fitting_used"] is False, data["target_fitting_used"]),
        check("closure not claimed", data["closure_claimed"] is False, data["what_remains_open"]),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1",
            data["next_required_artifact"],
        ),
        check(
            "note records numerical packet",
            "Heisenberg/Weyl" in note and "Not Yet Closed" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C non-identity rhoE and BN construction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
