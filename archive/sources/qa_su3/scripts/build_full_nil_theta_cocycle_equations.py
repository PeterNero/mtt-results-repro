"""Build the full nil-theta cocycle equation gate for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
OUTPUT_CERT = CERTS / "full_nil_theta_cocycle_equations_certificate.json"
OUTPUT_DATA = DATA / "full_nil_theta_cocycle_equations.candidate.json"


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


GENERATORS = [
    {"id": "g1", "coords": [1, 0, 0], "meaning": "z1 -> z1+1"},
    {"id": "g2", "coords": ["i", 0, 0], "meaning": "z1 -> z1+i"},
    {"id": "g3", "coords": [0, 1, 0], "meaning": "z2 -> z2+1, z3 -> z3+z1"},
    {"id": "g4", "coords": [0, "i", 0], "meaning": "z2 -> z2+i, z3 -> z3+i*z1"},
    {"id": "g5", "coords": [0, 0, 1], "meaning": "z3 -> z3+1"},
    {"id": "g6", "coords": [0, 0, "i"], "meaning": "z3 -> z3+i"},
]


COMMUTATORS = [
    {"pair": ["g1", "g3"], "central": {"g5": 1, "g6": 0}, "complex_value": "1"},
    {"pair": ["g1", "g4"], "central": {"g5": 0, "g6": 1}, "complex_value": "i"},
    {"pair": ["g2", "g3"], "central": {"g5": 0, "g6": 1}, "complex_value": "i"},
    {"pair": ["g2", "g4"], "central": {"g5": -1, "g6": 0}, "complex_value": "-1"},
]


def charge_to_target_cocycle(charge: list[int]) -> dict[str, int]:
    a, b, c = charge
    return {
        "base_area_g1_g2": a,
        "base_area_g3_g4": b,
        "central_area_g5_g6": c,
    }


def main() -> None:
    charge_targets = [
        {
            "charge": charge,
            "target_cocycle": charge_to_target_cocycle(charge),
            "requires_base_area": charge[0] != 0 or charge[1] != 0,
            "requires_central_area": charge[2] != 0,
            "requires_mixed_nil_response": charge[2] != 0 and (charge[0] != 0 or charge[1] != 0),
        }
        for charge in REQUIRED_CHARGES
    ]
    mixed_count = sum(item["requires_mixed_nil_response"] for item in charge_targets)
    central_count = sum(item["requires_central_area"] for item in charge_targets)
    equations = [
        {
            "id": "group_law",
            "equation": "(z1,z2,z3)*(w1,w2,w3)=(z1+w1,z2+w2,z3+w3+z1*w2)",
        },
        {
            "id": "factor",
            "equation": "a_q(gamma,z)=exp(2*pi*i*Phi_q(gamma,z))",
        },
        {
            "id": "cocycle",
            "equation": "Phi_q(gamma1*gamma2,z)=Phi_q(gamma1,gamma2.z)+Phi_q(gamma2,z) mod Z",
        },
        {
            "id": "section_equivariance",
            "equation": "s_q(gamma.z)=a_q(gamma,z)*s_q(z)",
        },
        {
            "id": "chern_target",
            "equation": "delta Phi_q on generator pairs must represent q_a[g1,g2]+q_b[g3,g4]+q_c[g5,g6]",
        },
    ]
    ansatz_requirements = {
        "ordinary_full_nil_theta": [
            "Phi_q must include coordinate-dependent terms involving z1,z2,z3",
            "central generator equations must be compatible with [g1,g3]=g5, [g1,g4]=g6, [g2,g3]=g6, [g2,g4]=g5^-1",
            "the same Phi_q formula must work functorially for all eleven required charges",
        ],
        "twisted_gerbe_fallback": [
            "if ordinary Phi_q fails integrality or associativity, add a selected B-field 2-cochain beta",
            "replace equality by a twisted cocycle with obstruction delta Phi_q=beta mod Z",
            "the twist must be selected before target comparison and must pass Bianchi/Freed-Witten checks",
        ],
    }
    candidate = {
        "candidate": "SelectedQaSU3FullNilThetaCocycleEquations",
        "status": "FULL_NIL_THETA_COCYCLE_EQUATIONS_BUILT_SOLVER_VALUES_OPEN",
        "generators": GENERATORS,
        "commutators": COMMUTATORS,
        "required_charges": REQUIRED_CHARGES,
        "charge_targets": charge_targets,
        "equations": equations,
        "counts": {
            "required_charges": len(REQUIRED_CHARGES),
            "charges_with_central_component": central_count,
            "charges_requiring_mixed_nil_response": mixed_count,
            "nonabelian_commutator_relations": len(COMMUTATORS),
        },
        "ansatz_requirements": ansatz_requirements,
        "what_this_rules_out": [
            "any factor system that ignores the central commutator relations",
            "base-torus-only Appell-Humbert factors as a complete solution",
            "central-fiber-only factors as a complete solution",
        ],
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3FullNilThetaCocycleEquations",
        "status": "QA_SU3_FULL_NIL_THETA_COCYCLE_EQUATIONS_BUILT_SOLVER_VALUES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "standard_complex_heisenberg_lattice_generators": True,
            "central_commutator_table": True,
            "cocycle_equation_written": True,
            "charge_to_integral_cocycle_target_schema": True,
        },
        "what_remains_open": {
            "explicit_Phi_q_solution": True,
            "integrality_and_c1_proof": True,
            "section_basis_solver": True,
            "multiplication_table": True,
            "operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "route_update": {
            "full_nil_theta_route": "LIVE_REDUCED_TO_PHI_Q_SOLVER",
            "projective_gerbe_route": "LIVE_FALLBACK_IF_ORDINARY_COCYCLE_OBSTRUCTED",
            "next_required_artifact": "Selected_Qa_SU3_PhiQ_Ansatz_Solver_or_Gerbe_Obstruction_v1",
        },
        "counts": candidate["counts"],
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
