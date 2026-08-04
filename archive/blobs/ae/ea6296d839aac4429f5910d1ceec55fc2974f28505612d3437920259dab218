"""Search the next visible rho_E source ansatz frontier.

This script is deliberately conservative.  It does not promote an ansatz by
flipping selected-source flags.  Instead it tests the ordinary-source escape
hatches that remained after the visible operator-source cut-set:

1. can the qutrit/projective central phase be absorbed into an ordinary
   constant rank-three rho_E carrier?
2. does moving scalar phase tables from mesh N=1 to N=2 expose a non-coboundary
   source-level rho_E class?
3. does a constant perfect/non-solvable carrier evade the N=1 solvable-carrier
   obstruction?

The answer produced here is negative for these routes.  The next live source is
therefore not another constant ordinary rho_E table; it is a selected
twisted/gerbe representative or selected D_E/dotD response data.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path
from typing import Any

from analyze_iwasawa_n1_phase_coboundary_obstruction import analyze_modulus


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "candidate_data" / "visible_rhoE_source_ansatz_search.candidate.json"
CERT = ROOT / "certificates" / "visible_rhoE_source_ansatz_search_certificate.json"

GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")

# These two N=2 entries are intentionally recorded in the certificate because
# each rank computation is heavyweight in the current pure-Python linear algebra
# implementation.  Re-run with --recompute-n2 to regenerate them.
N2_SCALAR_PHASE_CERTIFIED = {
    2: {
        "field": "F2",
        "modulus": 2,
        "mesh_N": 2,
        "closed_nodes": 729,
        "unknown_face_values": 1176,
        "corner_equations": 2783,
        "target_mismatches": 0,
        "corner_equation_rank": 748,
        "flat_solution_dimension": 428,
        "source_key_gauge_components": 504,
        "source_key_component_size_histogram": {"1": 369, "2": 90, "4": 45},
        "source_key_coboundary_rank": 428,
        "gauge_kernel_dimension": 76,
        "coboundary_image_equation_residual_count": 0,
        "coboundary_image_inside_flat_solution_space": True,
        "flat_solution_space_equals_source_key_coboundaries": True,
        "rhoE_source_promotion_possible_in_scalar_phase_ansatz": False,
    },
    3: {
        "field": "F3",
        "modulus": 3,
        "mesh_N": 2,
        "closed_nodes": 729,
        "unknown_face_values": 1176,
        "corner_equations": 2783,
        "target_mismatches": 0,
        "corner_equation_rank": 748,
        "flat_solution_dimension": 428,
        "source_key_gauge_components": 504,
        "source_key_component_size_histogram": {"1": 369, "2": 90, "4": 45},
        "source_key_coboundary_rank": 428,
        "gauge_kernel_dimension": 76,
        "coboundary_image_equation_residual_count": 0,
        "coboundary_image_inside_flat_solution_space": True,
        "flat_solution_space_equals_source_key_coboundaries": True,
        "rhoE_source_promotion_possible_in_scalar_phase_ansatz": False,
    },
}


Node = tuple[int, int, int, int, int, int]
Word = tuple[str, ...]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def cert(name: str) -> dict[str, Any]:
    return load_json(ROOT / "certificates" / name)


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def boundary_generators(node: Node, mesh_n: int) -> list[str]:
    return [GENERATORS[index] for index, value in enumerate(node) if value == mesh_n]


def reduce_target(node: Node, generator: str, mesh_n: int) -> Node:
    x1, x2, y1, y2, t1, t2 = node
    if generator == "g1" and x1 == mesh_n:
        return (0, x2, y1, y2, (t1 - y1) % mesh_n, (t2 - y2) % mesh_n)
    if generator == "g2" and x2 == mesh_n:
        return (x1, 0, y1, y2, (t1 + y2) % mesh_n, (t2 - y1) % mesh_n)
    if generator == "g3" and y1 == mesh_n:
        return (x1, x2, 0, y2, t1, t2)
    if generator == "g4" and y2 == mesh_n:
        return (x1, x2, y1, 0, t1, t2)
    if generator == "g5" and t1 == mesh_n:
        return (x1, x2, y1, y2, 0, t2)
    if generator == "g6" and t2 == mesh_n:
        return (x1, x2, y1, y2, t1, 0)
    raise ValueError(f"generator {generator} does not reduce node {node}")


def reductions(node: Node, mesh_n: int, word: Word = ()) -> list[tuple[Node, Word]]:
    generators = boundary_generators(node, mesh_n)
    if not generators:
        return [(node, word)]
    out: list[tuple[Node, Word]] = []
    for generator in generators:
        out.extend(reductions(reduce_target(node, generator, mesh_n), mesh_n, word + (generator,)))
    return out


def constant_word_equations(mesh_n: int) -> set[tuple[Word, Word]]:
    equations: set[tuple[Word, Word]] = set()
    for node in product(range(mesh_n + 1), repeat=6):
        node_tuple = node  # type: ignore[assignment]
        paths = reductions(node_tuple, mesh_n)
        reference_target, reference_word = paths[0]
        for target, word in paths[1:]:
            if target == reference_target and word != reference_word:
                equations.add((reference_word, word))
    return equations


def relation_present(equations: set[tuple[Word, Word]], left: Word, right: Word) -> bool:
    return (left, right) in equations or (right, left) in equations


def analyze_constant_carrier(mesh_n: int) -> dict[str, Any]:
    equations = constant_word_equations(mesh_n)
    forced_identity = {
        "g5_from_g1": relation_present(equations, ("g1",), ("g5", "g1")),
        "g6_from_g1": relation_present(equations, ("g1",), ("g6", "g1")),
        "g5_from_g2": relation_present(equations, ("g2",), ("g5", "g2")),
        "g6_from_g2": relation_present(equations, ("g2",), ("g6", "g2")),
    }
    noncentral = ("g1", "g2", "g3", "g4")
    commuting_pairs = {
        f"{left}_{right}": relation_present(equations, (left, right), (right, left))
        for index, left in enumerate(noncentral)
        for right in noncentral[index + 1 :]
    }
    central_generators_forced_identity = all(forced_identity.values())
    all_noncentral_commute = all(commuting_pairs.values())
    return {
        "mesh_N": mesh_n,
        "constant_word_equation_count": len(equations),
        "forced_identity_relations": forced_identity,
        "commuting_noncentral_pairs": commuting_pairs,
        "central_generators_forced_identity": central_generators_forced_identity,
        "all_noncentral_generators_commute": all_noncentral_commute,
        "constant_carrier_image_forced_abelian": central_generators_forced_identity
        and all_noncentral_commute,
        "qutrit_central_absorption_possible": False
        if central_generators_forced_identity and all_noncentral_commute
        else None,
        "reason": (
            "Invertibility turns g1=g5*g1 and g1=g6*g1 into g5=g6=I; "
            "the same face equations force g1,g2,g3,g4 to commute. A constant "
            "ordinary carrier therefore cannot absorb XZ=omega ZX as an "
            "ordinary rho_E central-generator relation."
            if central_generators_forced_identity and all_noncentral_commute
            else "The constant-carrier word constraints need a deeper search."
        ),
    }


def scalar_phase_analysis(recompute_n2: bool) -> dict[str, Any]:
    n1 = {prime: analyze_modulus(1, prime) for prime in (2, 3, 5, 7)}
    if recompute_n2:
        n2 = {prime: analyze_modulus(2, prime) for prime in (2, 3)}
        n2_source = "recomputed"
    else:
        n2 = N2_SCALAR_PHASE_CERTIFIED
        n2_source = "stored_from_recompute_n2_run"
    return {
        "mesh_N1_prime_fields": n1,
        "mesh_N2_prime_fields": n2,
        "mesh_N2_source": n2_source,
        "N1_all_scalar_phase_tables_coboundary": all(
            entry["flat_solution_space_equals_source_key_coboundaries"]
            for entry in n1.values()
        ),
        "N2_F2_F3_scalar_phase_tables_coboundary": all(
            entry["flat_solution_space_equals_source_key_coboundaries"]
            for entry in n2.values()
        ),
        "N2_qutrit_phase_source_level_blocked": n2[3][
            "flat_solution_space_equals_source_key_coboundaries"
        ],
    }


def analyze_dependencies() -> dict[str, Any]:
    gerbe_fourier = cert("selected_gerbe_fourier_type_theorem_certificate.json")
    block_twist = cert("iwasawa_block_factorized_twisted_packet_candidate_certificate.json")
    block_sector = cert("iwasawa_block_factorized_sector_maps_certificate.json")
    visible_cut = cert("visible_operator_source_blocker_resolution_certificate.json")
    return {
        "selected_gerbe_fourier_type_closed": get(
            gerbe_fourier,
            "calculation_results",
            "selected_gerbe_fourier_type_closed",
        )
        is True,
        "exact_su5_packet_selected": get(
            gerbe_fourier,
            "calculation_results",
            "exact_su5_packet_selected",
        )
        is True,
        "block_factorized_candidate_valid": get(
            block_twist,
            "calculation_results",
            "block_factorized_candidate_valid",
        )
        is True,
        "finite_block_factorized_sector_maps_validated": get(
            block_sector,
            "verdict",
            "finite_block_factorized_sector_maps_validated",
        )
        is True,
        "visible_cut_set_requires_new_source": get(
            visible_cut,
            "verdict",
            "current_status",
        )
        == "IRREDUCIBLE_NEW_SELECTED_OPERATOR_SOURCE_REQUIRED",
    }


def analyze(recompute_n2: bool = False) -> dict[str, Any]:
    constant_n1 = analyze_constant_carrier(1)
    constant_n2 = analyze_constant_carrier(2)
    scalar = scalar_phase_analysis(recompute_n2)
    deps = analyze_dependencies()

    ordinary_constant_blocked = (
        constant_n1["constant_carrier_image_forced_abelian"]
        and constant_n2["constant_carrier_image_forced_abelian"]
    )
    scalar_blocked = (
        scalar["N1_all_scalar_phase_tables_coboundary"]
        and scalar["N2_F2_F3_scalar_phase_tables_coboundary"]
    )
    qutrit_projective_needs_twist = (
        constant_n1["qutrit_central_absorption_possible"] is False
        and scalar["N2_qutrit_phase_source_level_blocked"] is True
    )
    selected_response_or_twist_is_next = (
        deps["selected_gerbe_fourier_type_closed"]
        and deps["block_factorized_candidate_valid"]
        and deps["finite_block_factorized_sector_maps_validated"]
        and deps["visible_cut_set_requires_new_source"]
        and qutrit_projective_needs_twist
    )

    status = (
        "VISIBLE_RHOE_SOURCE_ANSATZ_SEARCH_NARROWS_TO_SELECTED_RESPONSE_OR_TWISTED_SOURCE"
        if ordinary_constant_blocked and scalar_blocked and selected_response_or_twist_is_next
        else "VISIBLE_RHOE_SOURCE_ANSATZ_SEARCH_INCOMPLETE"
    )
    return {
        "calculation": "VisibleRhoESourceAnsatzSearch",
        "status": status,
        "generated_by": "scripts/search_visible_rhoE_source_ansatz.py",
        "ordinary_constant_carrier_analysis": {
            "mesh_N1": constant_n1,
            "mesh_N2": constant_n2,
            "ordinary_constant_carriers_blocked": ordinary_constant_blocked,
            "perfect_or_non_solvable_constant_carriers_do_not_help": ordinary_constant_blocked,
        },
        "scalar_phase_analysis": scalar,
        "dependency_state": deps,
        "calculation_results": {
            "ordinary_constant_carriers_blocked": ordinary_constant_blocked,
            "scalar_phase_N1_and_N2_F2_F3_source_level_blocked": scalar_blocked,
            "qutrit_projective_central_absorption_as_ordinary_rhoE_blocked": qutrit_projective_needs_twist,
            "perfect_non_solvable_constant_carrier_route_blocked": ordinary_constant_blocked,
            "selected_gerbe_fourier_type_available": deps["selected_gerbe_fourier_type_closed"],
            "selected_block_factorized_finite_scaffold_available": deps[
                "block_factorized_candidate_valid"
            ]
            and deps["finite_block_factorized_sector_maps_validated"],
            "selected_visible_operator_source_still_unconstructed": True,
            "next_object_identified": "selected_D_E_dotD_response_or_fixed_gerbe_period_representative",
        },
        "surviving_routes": {
            "primary": "selected D_E/dotD de_response promotion on the q79/F branch",
            "parallel": "fixed differential-cohomology gerbe/B-field period representative for the already selected nontrivial qutrit Fourier type",
            "fallback": "nonconstant N>1 genuinely matrix-valued finite table; constant ordinary carriers are now retired",
        },
        "minimal_next_packet": [
            "selected fixed gerbe/B-field representative or selected finite HYM/Strominger response source",
            "same-branch D_E and dotD_alpha1 matrices for Q,u,d,L,e,N,H",
            "Riesz projectors, complement gaps, and reduced Green operators",
            "projector retention for ordered SU(5) matter slots",
            "no observed flavor or benchmark entries",
        ],
        "guardrails": {
            "claims_selected_visible_operator_source": False,
            "claims_selected_D_E_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "promotes_projective_fixture_as_selected": False,
        },
        "verdict": {
            "honest_answer": (
                "The ordinary rho_E source search did not produce the missing "
                "operator source. It rules out central absorption, scalar "
                "N=2 qutrit phases, and constant perfect/non-solvable carriers. "
                "The live resolution path is selected response/twist data."
            ),
            "recommended_next_action": (
                "Construct the selected de_response packet directly, using the "
                "already selected gerbe-Fourier type and block-factorized finite "
                "scaffold as source constraints."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "VisibleRhoESourceAnsatzSearchCertificate",
        "status": report["status"],
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "analysis_script": "scripts/search_visible_rhoE_source_ansatz.py",
        "calculation_results": report["calculation_results"],
        "surviving_routes": report["surviving_routes"],
        "minimal_next_packet": report["minimal_next_packet"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--recompute-n2",
        action="store_true",
        help="recompute the heavyweight N=2 scalar phase F2/F3 rank checks",
    )
    args = parser.parse_args()
    report = analyze(recompute_n2=args.recompute_n2)
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
