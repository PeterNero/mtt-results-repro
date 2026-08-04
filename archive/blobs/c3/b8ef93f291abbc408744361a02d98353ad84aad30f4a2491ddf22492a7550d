from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2distinguishedcutsystemandglobalrelation"
FAN = (
    ROOT
    / "candidate_data"
    / SLUG
    / "distinguished_radial_fan.packet.json"
)
TRAJECTORY_BATCH = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedmeridianexecution"
    / "distinguished_trajectory_batch.packet.json"
)
TUBE_BATCH = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedmeridianexecution"
    / "distinguished_root_tube_batch.packet.json"
)
BRAID_RELATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedmeridianexecution"
    / "distinguished_pl_braid_and_global_relation_certificate.packet.json"
)
A115 = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2localmonodromypromotion.candidate.json"
)
HANDLE_PROMOTION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handlemonodromypromotion"
    / "two_promoted_torus_handle_monodromies.packet.json"
)
OUTPUT_DIR = ROOT / "candidate_data" / SLUG
FACTORIZATION = OUTPUT_DIR / "global_integral_gauss_manin_factorization.packet.json"
PERIOD_READY = OUTPUT_DIR / "eight_prym_period_transport.ready.json"
FRONTIER = OUTPUT_DIR / "U6_frontier_after_A116.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79GenusTwoDistinguishedCutSystemAndGlobalSurfaceRelation_v1.md"
)
NEXT = "MTT_Selected_q79GenusTwoEightPrymPeriodRowsAndIntegralBranch_v1"
STATUS = "MTT_U6_Q79_GLOBAL_INTEGRAL_GAUSS_MANIN_FACTORIZATION_CLOSED_PERIOD_EXECUTION_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_rows(value: sp.Matrix) -> list[list[int]]:
    return [
        [int(value[row, column]) for column in range(value.cols)]
        for row in range(value.rows)
    ]


def main() -> int:
    for path in (
        FAN,
        TRAJECTORY_BATCH,
        TUBE_BATCH,
        BRAID_RELATION,
        A115,
        HANDLE_PROMOTION,
        NOTE,
    ):
        if not path.exists():
            raise FileNotFoundError(path)

    fan = load(FAN)
    trajectories = load(TRAJECTORY_BATCH)
    tubes = load(TUBE_BATCH)
    relation = load(BRAID_RELATION)
    a115 = load(A115)
    handles = load(HANDLE_PROMOTION)

    if not fan["topology"]["ordered_distinguished_cut_system_closed"]:
        raise AssertionError("distinguished cut system remains open")
    if trajectories["counts"]["trajectory_packets_complete"] != 90:
        raise AssertionError("distinguished trajectory count")
    if tubes["counts"]["continuous_root_tube_certificates"] != 90:
        raise AssertionError("distinguished tube count")
    if relation["aggregate"]["promoted_distinguished_matrix_count"] != 90:
        raise AssertionError("distinguished promotion count")
    if not all(relation["acceptance"].values()):
        raise AssertionError("distinguished relation acceptance failed")
    if not relation["global_surface_relation"]["exact_integer_matrix_equality"]:
        raise AssertionError("global surface relation is not exact")
    if a115["results"]["local_picard_lefschetz_monodromies_promoted"] != 90:
        raise AssertionError("A115 local promotion missing")
    if a115["results"]["torus_handle_monodromies_promoted"] != 2:
        raise AssertionError("A115 handle promotion missing")

    geometric_margins = {
        key: float(value)
        for key, value in fan["geometric_certificate"].items()
    }
    if not all(value > 0 for value in geometric_margins.values()):
        raise AssertionError("nonpositive fan geometry margin")

    symplectic_form = sp.Matrix(
        load(
            ROOT
            / "candidate_data"
            / "selected_q79genus2picardlefschetzmonodromyexecution"
            / "numerical_monodromy_exploration.packet.json"
        )["homology_convention"]["intersection_matrix"]
    )
    identity = sp.eye(4)
    product = identity
    factors: list[dict] = []
    for expected_index, row in enumerate(relation["rows"], 1):
        if row["distinguished_index"] != expected_index:
            raise AssertionError("distinguished factor order")
        if row["picard_lefschetz_twist_sign"] != 1:
            raise AssertionError("nonpositive distinguished PL factor")
        action = sp.Matrix(
            row["promoted_integral_symplectic_matrix_A114_marking"]
        )
        delta = action - identity
        if (
            action.T * symplectic_form * action != symplectic_form
            or action.det() != 1
            or delta.rank() != 1
            or delta * delta != sp.zeros(4)
        ):
            raise AssertionError("invalid distinguished factor")
        product = action * product
        factors.append(
            {
                "distinguished_index": expected_index,
                "root_id": row["root_id"],
                "positive_vanishing_cycle_up_to_sign": row[
                    "vanishing_cycle_primitive_up_to_sign"
                ],
                "positive_picard_lefschetz_matrix": matrix_rows(action),
                "interval_certified_crossings": row[
                    "interval_certified_crossings"
                ],
                "certified_path_segments": row["certified_path_segments"],
            }
        )

    handle_rows = {row["name"]: row for row in handles["handles"]}
    handle_a = sp.Matrix(handle_rows["A"]["integral_symplectic_matrix"])
    handle_b = sp.Matrix(handle_rows["B"]["integral_symplectic_matrix"])
    boundary = handle_b.inv() * handle_a.inv() * handle_b * handle_a
    if product != boundary:
        raise AssertionError("factor product and handle boundary disagree")
    if matrix_rows(product) != relation["global_surface_relation"][
        "ordered_distinguished_action_product"
    ]:
        raise AssertionError("relation certificate product mismatch")

    factorization = {
        "schema": "MTTQ79GlobalIntegralGaussManinFactorization.v1",
        "status": "GLOBAL_INTEGRAL_H1_GAUSS_MANIN_FACTORIZATION_CLOSED",
        "base": {
            "normalized_torus": "C/(Z+iZ)",
            "base_point": "(1+i)/4",
            "fiber_genus": 2,
            "homology_basis": ["a1", "b1", "a2", "b2"],
            "intersection_matrix": matrix_rows(symplectic_form),
        },
        "distinguished_cut_system": {
            "generator_count": 90,
            "ordering_rule": fan["ordering"]["rule"],
            "ordered_root_ids": fan["ordering"]["root_ids"],
            "minimum_geometric_margin": format(
                min(geometric_margins.values()), ".17g"
            ),
        },
        "factors": factors,
        "handle_actions": {
            "A": matrix_rows(handle_a),
            "B": matrix_rows(handle_b),
        },
        "surface_relation": relation["global_surface_relation"],
        "action_convention": relation["action_convention"],
        "exact_checks": {
            "all_90_factors_positive_rank_one_PL_transvections": True,
            "all_90_factors_integral_symplectic": True,
            "vanishing_cycle_span_rank_four": relation["aggregate"][
                "vanishing_cycle_span_rank"
            ]
            == 4,
            "ordered_product_equals_handle_boundary": product == boundary,
            "global_integral_H1_representation_closed": True,
        },
    }
    dump(FACTORIZATION, factorization)

    period_ready = {
        "schema": "MTTQ79EightPrymPeriodTransportReadiness.v1",
        "status": "GLOBAL_MONODROMY_INPUT_CLOSED_EIGHT_BY_92_PERIOD_EXECUTION_READY",
        "closed_inputs": {
            "critical_values_and_nodes": "90/90",
            "based_path_carriers": "92/92",
            "promoted_local_actions": "90/90",
            "promoted_handle_actions": "2/2",
            "ordered_distinguished_cut_system": True,
            "global_integral_H1_surface_relation": True,
            "residue_numerators": "8/8 from A111",
            "splitting_divisor_normal_function": "explicit from A111",
        },
        "next_execution": {
            "additive_period_table_shape": [8, 92],
            "transport_generators": "90 distinguished positive meridians plus A/B handles",
            "required_output": "eight additive Prym normal-function rows with exact interval/error certificates",
            "integral_test": "membership of the resulting relative period class in the declared integral Z^92 branch",
        },
        "not_yet_emitted": {
            "numerical_period_entries": 0,
            "selected_integral_branch": False,
            "covariant_gerbe_zero_or_no_go": False,
            "selected_marked_K3": False,
        },
    }
    dump(PERIOD_READY, period_ready)

    frontier = {
        "schema": "MTTU6FrontierAfterA116.v1",
        "status": STATUS,
        "critical_values_closed": 90,
        "nodal_points_closed": 90,
        "based_path_carriers_closed": 92,
        "local_picard_lefschetz_monodromies_promoted": 90,
        "torus_handle_monodromies_promoted": 2,
        "distinguished_local_picard_lefschetz_monodromies_promoted": 90,
        "ordered_distinguished_cut_system_closed": True,
        "global_integral_H1_surface_relation_closed": True,
        "local_vanishing_cycle_span_rank": 4,
        "beta_C_period_rows_emitted": 0,
        "integral_period_branch_selected": False,
        "gerbe_zero_or_no_go_executed": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        FAN,
        TRAJECTORY_BATCH,
        TUBE_BATCH,
        BRAID_RELATION,
        A115,
        HANDLE_PROMOTION,
        Path(__file__),
        ROOT / "scripts" / "build_selected_q79genus2distinguishedcutsystem.py",
        ROOT / "scripts" / "q79genus2_root_transport.py",
        ROOT / "scripts" / "explore_q79genus2distinguishedmeridiantrajectory.py",
        ROOT / "scripts" / "run_q79genus2distinguishedtrajectorybatch.py",
        ROOT / "scripts" / "certify_q79genus2singlelocal_root_tubes.py",
        ROOT / "scripts" / "run_q79genus2distinguishedtubebatch.py",
        ROOT
        / "scripts"
        / "certify_q79genus2distinguished_pl_braids_and_global_relation.py",
    ]
    candidate = {
        "schema": "MTTSelectedQ79GenusTwoDistinguishedCutSystemAndGlobalRelation.v1",
        "status": STATUS,
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "authority_hashes": [
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for path in authority_paths
        ],
        "outputs": {
            "global_factorization": str(FACTORIZATION.relative_to(ROOT)).replace("\\", "/"),
            "period_execution_ready": str(PERIOD_READY.relative_to(ROOT)).replace("\\", "/"),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {
            "radial_fan_is_an_ordered_distinguished_cut_system": True,
            "all_229436_path_segments_have_continuous_root_tubes": tubes[
                "counts"
            ]["segments_certified"]
            == 229436,
            "all_3476_crossings_interval_certified": relation["aggregate"][
                "interval_certified_crossing_count"
            ]
            == 3476,
            "all_90_distinguished_PL_factors_promoted": len(factors) == 90,
            "ordered_product_equals_handle_boundary_exactly": product == boundary,
            "global_integral_H1_Gauss_Manin_representation_closed": True,
            "full_mapping_class_faithfulness_not_invented": not relation[
                "strict_scope"
            ]["full_mapping_class_group_faithfulness_claimed"],
            "period_rows_not_invented": period_ready["not_yet_emitted"][
                "numerical_period_entries"
            ]
            == 0,
            "integral_branch_not_invented": not frontier[
                "integral_period_branch_selected"
            ],
            "gerbe_zero_not_invented": not frontier["gerbe_zero_or_no_go_executed"],
            "trial_not_selected": frontier["strict_MTT_source_moduli_removed"] == 0,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": "MTTSelectedQ79GenusTwoDistinguishedCutSystemAndGlobalRelation",
        "status": STATUS,
        "candidate_path": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "candidate_sha256": sha256(CANDIDATE),
        "closure_claimed": False,
        "global_integral_H1_Gauss_Manin_representation_closed": True,
        "full_U6_closed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
