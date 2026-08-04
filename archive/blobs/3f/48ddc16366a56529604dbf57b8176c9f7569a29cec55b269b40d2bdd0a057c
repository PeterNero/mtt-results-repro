"""Build an automorphy-factor constraint solver gate for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
OUTPUT_CERT = CERTS / "automorphy_factor_constraint_solver_certificate.json"
OUTPUT_DATA = DATA / "automorphy_factor_constraint_solver.candidate.json"


REQUIRED_CHARGES = [
    [-3, 0, 1],
    [-2, 1, -1],
    [0, -1, 0],
    [0, 0, -1],
    [1, 1, 1],
    [2, 1, -1],
    [1, 0, 1],
    [-1, 2, 0],
    [-1, 1, 1],
    [-2, 0, -1],
    [-1, 1, 0],
]


def can_cover(charge: list[int], supported_axes: set[int]) -> bool:
    return all(value == 0 or index in supported_axes for index, value in enumerate(charge))


def main() -> None:
    ansatz_classes = [
        {
            "id": "flat_character",
            "description": "a_q(gamma,z)=chi_q(gamma)",
            "supported_axes": [],
            "has_nonzero_c1": False,
            "status": "REJECTED",
            "reason": "Flat factors can carry torsion/holonomy but not the nonzero Chern charges required by the monad maps.",
        },
        {
            "id": "base_torus_appell_humbert_pullback",
            "description": "pull back Appell-Humbert factors from the abelianized (z1,z2) base torus",
            "supported_axes": [0, 1],
            "has_nonzero_c1": True,
            "status": "PARTIAL_ONLY",
            "reason": "It can see a,b components but cannot realize charges with nonzero c component.",
        },
        {
            "id": "central_fiber_theta_only",
            "description": "theta factor only along the central z3 elliptic fiber",
            "supported_axes": [2],
            "has_nonzero_c1": True,
            "status": "PARTIAL_ONLY",
            "reason": "It can see c components but cannot realize mixed a,b,c charges.",
        },
        {
            "id": "full_nil_theta_automorphy",
            "description": "factor depends on the nonabelian H3(C) group law, including z1*w2 central cocycle",
            "supported_axes": [0, 1, 2],
            "has_nonzero_c1": True,
            "status": "LIVE_REQUIRED",
            "reason": "Only this ansatz class can in principle realize all eleven mixed charges without collapsing to flat or split data.",
        },
        {
            "id": "projective_gerbe_twisted_factor",
            "description": "ordinary factors fail but a twisted cocycle closes after a selected B-field/gerbe correction",
            "supported_axes": [0, 1, 2],
            "has_nonzero_c1": True,
            "status": "LIVE_ALTERNATIVE",
            "reason": "This may be the correct container if ordinary rho_E/line-bundle factors are too small.",
        },
    ]
    coverage = []
    for ansatz in ansatz_classes:
        axes = set(ansatz["supported_axes"])
        covered = [can_cover(charge, axes) for charge in REQUIRED_CHARGES]
        coverage.append(
            {
                "id": ansatz["id"],
                "covered_count": sum(covered),
                "total_required": len(REQUIRED_CHARGES),
                "covers_all_required_charges": all(covered),
                "failed_charges": [charge for charge, ok in zip(REQUIRED_CHARGES, covered) if not ok],
            }
        )
    candidate = {
        "candidate": "SelectedQaSU3AutomorphyFactorConstraintSolver",
        "status": "AUTOMORPHY_FACTOR_CONSTRAINT_SOLVER_BUILT_FULL_NIL_OR_TWIST_REQUIRED",
        "required_charges": REQUIRED_CHARGES,
        "ansatz_classes": ansatz_classes,
        "coverage": coverage,
        "constraint_system_required_next": [
            "choose standard Gamma generators and quotient side",
            "write a_q(gamma,z)=exp(2*pi*i*Phi_q(gamma,z))",
            "impose Phi_q(gamma1 gamma2,z)=Phi_q(gamma1,gamma2.z)+Phi_q(gamma2,z) mod Z",
            "compute the induced integral Chern cocycle",
            "verify c1 equals q=(a,b,c)",
            "solve s(gamma.z)=a_q(gamma,z)s(z)",
        ],
        "target_fitting_used": False,
    }
    full_nil = next(item for item in coverage if item["id"] == "full_nil_theta_automorphy")
    gerbe = next(item for item in coverage if item["id"] == "projective_gerbe_twisted_factor")
    base = next(item for item in coverage if item["id"] == "base_torus_appell_humbert_pullback")
    certificate = {
        "certificate": "SelectedQaSU3AutomorphyFactorConstraintSolver",
        "status": "QA_SU3_AUTOMORPHY_FACTOR_SOLVER_BUILT_FULL_NIL_THETA_OR_GERBE_REQUIRED",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "ansatz_results": {
            "flat_character_rejected": True,
            "base_torus_pullback_partial_count": base["covered_count"],
            "full_nil_theta_covers_all_charge_axes": full_nil["covers_all_required_charges"],
            "projective_gerbe_covers_all_charge_axes": gerbe["covers_all_required_charges"],
        },
        "route_update": {
            "ordinary_primary_route_refined_to": "full_nil_theta_automorphy",
            "secondary_route_refined_to": "projective_gerbe_twisted_factor",
            "base_torus_appell_humbert_is_auxiliary_only": True,
            "next_required_artifact": "Selected_Qa_SU3_Full_Nil_Theta_Cocycle_Equations_v1",
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    text_data = json.dumps(candidate, indent=2, sort_keys=True)
    text_cert = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(text_data + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(text_cert + "\n", encoding="utf-8")
    print(text_cert)


if __name__ == "__main__":
    main()
