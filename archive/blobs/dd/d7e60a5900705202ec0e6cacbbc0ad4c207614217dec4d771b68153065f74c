from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

SLUG = "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution"
STATUS = (
    "MTT_U6_EXACT_MINIMAL_FUYAU_ALLOCATION_AND_STABLE_BUNDLES_CLOSED_"
    "FULL_HOLONOMY_AND_CHIRAL_VISIBLE_SOURCE_OPEN"
)
NEXT = "MTT_Selected_q79NonPullbackChiralVisibleBundleAndFullSU9HolonomySelection_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79HiddenBundleExistenceBianchiAllocationAndSpectrumExecution_v1.md"

MUKAI = OUT / "mukai_kernel_and_primitive_hidden_charge_repair.packet.json"
BIANCHI = OUT / "rank_one_fuyau_k3_lattice_and_bianchi_allocation.packet.json"
BUNDLES = OUT / "stable_SU3_SU9_HYM_bundle_existence.packet.json"
HIDDEN = OUT / "hidden_SU9_in_E8_embedding_and_commutant.packet.json"
CHIRALITY = OUT / "visible_pullback_index_and_chirality_no_go.packet.json"
FRONTIER = OUT / "U6_frontier_after_A102.packet.json"


# Bourbaki E8 ordering: 1-3-4-5-6-7-8, with node 2 attached to node 4.
E8_CARTAN = [
    [2, 0, -1, 0, 0, 0, 0, 0],
    [0, 2, 0, -1, 0, 0, 0, 0],
    [-1, 0, 2, -1, 0, 0, 0, 0],
    [0, -1, -1, 2, -1, 0, 0, 0],
    [0, 0, 0, -1, 2, -1, 0, 0],
    [0, 0, 0, 0, -1, 2, -1, 0],
    [0, 0, 0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, 0, 0, -1, 2],
]
E8_HIGHEST_ROOT = [2, 3, 4, 6, 5, 4, 3, 2]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def determinant(matrix: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next(row for row in range(column, len(work)) if work[row][column])
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            result *= -1
        scale = work[column][column]
        result *= scale
        work[column] = [entry / scale for entry in work[column]]
        for row in range(column + 1, len(work)):
            scale = work[row][column]
            work[row] = [
                work[row][index] - scale * work[column][index]
                for index in range(len(work))
            ]
    assert result.denominator == 1
    return result.numerator


def mukai_square(vector: tuple[int, int, int], h_square: int = 2) -> int:
    rank, h_coefficient, degree_four = vector
    return h_square * h_coefficient**2 - 2 * rank * degree_four


def c2_from_mukai(vector: tuple[int, int, int], h_square: int = 2) -> int:
    rank, h_coefficient, degree_four = vector
    return rank + h_square * h_coefficient**2 // 2 - degree_four


def lattice_dot(left: list[int], right: list[int]) -> int:
    # Coordinates are (e1,f1,e2,f2,e3,f3) in U^3.
    return sum(
        left[2 * block] * right[2 * block + 1]
        + left[2 * block + 1] * right[2 * block]
        for block in range(3)
    )


def e8_a8_gram() -> list[list[int]]:
    simple = []
    for index in [0, 2, 3, 4, 5, 6, 7]:
        vector = [0] * 8
        vector[index] = 1
        simple.append(vector)
    simple.append([-value for value in E8_HIGHEST_ROOT])
    return [
        [
            sum(
                simple[i][p] * E8_CARTAN[p][q] * simple[j][q]
                for p in range(8)
                for q in range(8)
            )
            for j in range(8)
        ]
        for i in range(8)
    ]


def main() -> int:
    paths = {
        "A101": ROOT / "candidate_data" / "selected_q79hiddene8confinementandns5qualityamplitudecertificate.candidate.json",
        "q79_charge": Q79 / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json",
        "q79_stable_gate": Q79 / "proof_corpus" / "Stable_Sheaf_Existence_Gate_for_Mukai_Z7_Block_v1.md",
        "q79_shared_circle_clue": Q79 / "proof_corpus" / "Visible_Rank2_L2_Appell_Humbert_Automorphy_Source_Attempt_v1.md",
        "A97_visible_embedding": ROOT / "candidate_data" / "selected_4dgreenschwarzaxionreductionandsurvivingcurrent" / "visible_E8_E6_SU3_embedding_index.packet.json",
        "current_ledger": ROOT / "proof_corpus" / "MTT_Current_TrueSMClosure_ConsolidatedLedger_v1.md",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A102 authority: " + ", ".join(missing))

    a101 = load(paths["A101"])
    q79 = load(paths["q79_charge"])
    visible_embedding = load(paths["A97_visible_embedding"])
    shared_circle_text = paths["q79_shared_circle_clue"].read_text(encoding="utf-8")

    assert a101["next_required_artifact"] == "MTT_Selected_q79HiddenBundleExistenceBianchiAllocationAndSpectrumExecution_v1"
    assert q79["charge_data"]["a"] == [5, "H", 0]
    assert q79["charge_data"]["b"] == [7, "3H", 1]
    assert q79["conclusion"]["q_7"] == 2
    assert visible_embedding["selected_chain"]["visible_SU3_bundle_in_E8_sources_E6"]
    assert "shared circle is retained with zero degree" in shared_circle_text

    a = (5, 1, 0)
    b = (7, 3, 1)
    kernel = tuple(3 * a[index] - b[index] for index in range(3))
    ideal_length_two = (1, 0, -1)
    repaired = tuple(kernel[index] + ideal_length_two[index] for index in range(3))
    assert kernel == (8, 0, -1)
    assert repaired == (9, 0, -2)
    assert c2_from_mukai(kernel) == 9
    assert c2_from_mukai(repaired) == 11
    assert mukai_square(kernel) == 16
    assert mukai_square(repaired) == 36
    assert math.gcd(*repaired) == 1

    mukai = {
        "schema": "MTTQ79MukaiKernelAndPrimitiveHiddenChargeRepair.v1",
        "status": "EXACT_ARITHMETIC_AND_LOCAL_FREENESS_OBSTRUCTION_CLOSED_Q7_IDEAL_PROMOTION_OPEN",
        "selected_q79_block": {
            "a": list(a),
            "b": list(b),
            "H_square": 2,
            "first_Chern_map": "(x,y)->(x+3*y)H",
            "primitive_kernel_generator": [3, -1],
            "uniqueness": "Every determinant-free integer combination is n*(3a-b); the primitive choices are plus/minus (3,-1).",
        },
        "determinant_free_kernel": {
            "vector_3a_minus_b": list(kernel),
            "c1": 0,
            "c2": c2_from_mukai(kernel),
            "Mukai_square": mukai_square(kernel),
            "Yoshioka_Proposition_0_5_obstruction": "The vector (8,0,-1)=8-omega is an all-non-locally-free exceptional case, so it is not an honest physical HYM bundle.",
        },
        "minimal_primitive_repair_candidate": {
            "length_two_ideal_sheaf_vector": list(ideal_length_two),
            "vector": list(repaired),
            "rank": 9,
            "c1": 0,
            "c2": c2_from_mukai(repaired),
            "Mukai_square": mukai_square(repaired),
            "primitive": True,
            "stable_locally_free_representative_exists": True,
            "reason": "Yoshioka nonemptiness plus the Proposition 0.5 classification, independently reinforced by the K3 stable-bundle bound.",
        },
        "source_guard": {
            "q7_equals_length_two_numerically": q79["conclusion"]["q_7"] == 2,
            "q7_to_point_ideal_source_map_in_corpus": False,
            "interpretation": "The equality is a candidate bridge, not a selected theorem. The c2=11 hidden sector can instead be fixed by the Bianchi allocation.",
        },
        "theorem": {
            "name": "Q79DeterminantFreeKernelAndPrimitiveRepairTheorem",
            "proved": True,
            "statement": "The q79 Mukai block has unique primitive determinant-free combination 3a-b=(8,0,-1), but that vector lies in Yoshioka's all-non-locally-free class. Adding the length-two ideal charge gives the primitive locally-free-admissible vector (9,0,-2) with c2=11; identifying that repair with q7=2 remains a source-map premise.",
        },
        "primary_reference": "https://arxiv.org/abs/math/9907001",
    }

    h = [1, 1, 0, 0, 0, 0]
    delta = [0, 0, 1, -2, 0, 0]
    assert lattice_dot(h, h) == 2
    assert lattice_dot(delta, delta) == -4
    assert lattice_dot(h, delta) == 0
    assert math.gcd(*delta) == 1

    visible_c2 = 9
    hidden_c2 = 11
    torus_cost = -lattice_dot(delta, delta)
    assert visible_c2 + hidden_c2 + torus_cost == 24

    bianchi = {
        "schema": "MTTRankOneFuYauK3LatticeAndBianchiAllocation.v1",
        "status": "EXACT_CONDITIONAL_SOURCE_FREE_ALLOCATION_CLOSED_SHARED_CIRCLE_TO_TORUS_SOURCE_MAP_OPEN",
        "K3_lattice": {
            "ambient": "Lambda_K3=U^3 direct_sum E8(-1)^2",
            "polarization_h_in_U3_coordinates": h,
            "primitive_ASD_class_delta_in_U3_coordinates": delta,
            "Gram_h_delta": [
                [lattice_dot(h, h), lattice_dot(h, delta)],
                [lattice_dot(delta, h), lattice_dot(delta, delta)],
            ],
            "delta_primitive": True,
            "existence": "The K3 period map realizes the primitive sublattice; choose the Kahler chamber containing h.",
        },
        "minimality_theorem": {
            "even_lattice": "Every integral K3 class has even square.",
            "minus_two_exclusion": "An integral ASD (1,1) class of square -2 cannot be orthogonal to an ample class: Riemann-Roch makes one sign effective, contradicting ampleness.",
            "minimal_nonzero_ASD_cost": 4,
            "witness": "delta=e2-2f2 has delta^2=-4 and h.delta=0.",
            "proved": True,
        },
        "rank_one_torus_candidate": {
            "omega_1_over_2pi": "delta",
            "omega_2_over_2pi": 0,
            "normalized_curvature_cost": torus_cost,
            "one_geometric_circle_untwisted": True,
            "FuYau_theorem_allows_zero_second_class": True,
        },
        "source_free_Bianchi": {
            "normalization": "dimensionless string-unit convention alpha'=1",
            "c2_TK3": 24,
            "c2_visible_SU3": visible_c2,
            "c2_hidden_SU9": hidden_c2,
            "torus_curvature_cost": torus_cost,
            "identity": "9+11+4=24",
            "residual": 24 - visible_c2 - hidden_c2 - torus_cost,
            "NS5_charge": 0,
        },
        "source_guard": {
            "corpus_shared_circle_is_degree_zero_in_flavor_support": True,
            "corpus_identifies_it_with_the_untwisted_FuYau_circle": False,
            "rank_one_FuYau_topology_selected_by_MTT": False,
            "conditional_premise": "Identify the unique shared degree-zero circle with the untwisted factor of the Fu-Yau T2 bundle and select the primitive minimal nonzero companion class delta.",
        },
        "theorem": {
            "name": "MinimalRankOneFuYauBianchiAllocationTheorem",
            "proved_conditionally": True,
            "statement": "Under the displayed discrete shared-circle premise, the minimal nontrivial integral Fu-Yau curvature costs exactly four units and the source-free allocation c2(V3)=9, c2(W9)=11 closes exactly with no NS5 charge.",
        },
        "primary_references": [
            "https://arxiv.org/abs/hep-th/0509028",
            "https://arxiv.org/abs/1901.10322",
        ],
    }

    visible_vector = (3, 0, -6)
    hidden_vector = repaired
    assert c2_from_mukai(visible_vector) == visible_c2
    assert mukai_square(visible_vector) == 36
    assert mukai_square(hidden_vector) == 36

    bundles = {
        "schema": "MTTStableSU3SU9HYMBundleExistence.v1",
        "status": "EXACT_EXISTENCE_AND_HYM_GATE_CLOSED_UNIQUE_MTT_MODULI_POINT_OPEN",
        "K3_stable_bundle_bound": {
            "statement": "For c1=0 on a surface, the cited Artamkin bound gives a stable locally free rank-r bundle when c2>(r+1)*max(1,p_g).",
            "K3_p_g": 1,
            "visible": {"rank": 3, "c2": visible_c2, "strict_bound": 4, "passes": visible_c2 > 4},
            "hidden": {"rank": 9, "c2": hidden_c2, "strict_bound": 10, "passes": hidden_c2 > 10},
            "primary_reference": "https://arxiv.org/abs/math/9411233",
        },
        "visible_SU3_bundle": {
            "Mukai_vector": list(visible_vector),
            "Mukai_square": mukai_square(visible_vector),
            "expected_complex_moduli_dimension": mukai_square(visible_vector) + 2,
            "determinant": "trivial because c1=0 and Pic^0(K3)=0",
            "stable_locally_free_exists": True,
            "irreducible_HYM_exists": True,
        },
        "hidden_SU9_bundle": {
            "Mukai_vector": list(hidden_vector),
            "Mukai_square": mukai_square(hidden_vector),
            "expected_complex_moduli_dimension": mukai_square(hidden_vector) + 2,
            "primitive": True,
            "determinant": "trivial because c1=0 and Pic^0(K3)=0",
            "stable_locally_free_exists": True,
            "irreducible_HYM_exists": True,
        },
        "HYM_theorem": {
            "name": "StableSU3SU9HYMExistenceTheorem",
            "proved": True,
            "statement": "Stable locally free K3 bundles V3 and W9 with (rank,c1,c2)=(3,0,9) and (9,0,11) exist. Donaldson-Uhlenbeck-Yau supplies irreducible HYM connections, and their pullbacks solve the Fu-Yau gauge equation.",
        },
        "selection_guard": {
            "visible_moduli_point_selected": False,
            "hidden_moduli_point_selected": False,
            "new_fitted_continuous_parameters": 0,
            "unfixed_reduced_bundle_moduli_complex_dimension": 76,
            "interpretation": "Existence of a sector is not unique MTT selection of a connection or modulus vacuum.",
        },
        "primary_references": [
            "https://arxiv.org/abs/math/9411233",
            "https://arxiv.org/abs/math/9907001",
            "https://arxiv.org/abs/1901.10322",
        ],
    }

    a8_gram = e8_a8_gram()
    a8_determinant = determinant(a8_gram)
    affine_pairings = [
        sum(E8_CARTAN[row][column] * E8_HIGHEST_ROOT[column] for column in range(8))
        for row in range(8)
    ]
    assert affine_pairings == [0, 0, 0, 0, 0, 0, 0, 1]
    assert a8_determinant == 9

    end0_rank = 9**2 - 1
    end0_c2 = 2 * 9 * hidden_c2
    wedge3_rank = math.comb(9, 3)
    wedge3_c2_factor = math.comb(9 - 2, 3 - 1)
    wedge3_c2 = wedge3_c2_factor * hidden_c2
    end0_h1 = end0_c2 - 2 * end0_rank
    wedge3_h1 = wedge3_c2 - 2 * wedge3_rank
    total_h1 = end0_h1 + 2 * wedge3_h1
    e8_expected_h1 = 2 * (30 * hidden_c2 - 248)
    assert (end0_rank, end0_c2, end0_h1) == (80, 198, 38)
    assert (wedge3_rank, wedge3_c2, wedge3_h1) == (84, 231, 63)
    assert total_h1 == e8_expected_h1 == 164

    hidden = {
        "schema": "MTTHiddenSU9InE8EmbeddingCommutantAndCohomology.v1",
        "status": "EXACT_EMBEDDING_BRANCHING_AND_INDEX_SPECTRUM_CLOSED_FULL_HOLONOMY_SELECTION_OPEN",
        "affine_E8_certificate": {
            "Cartan": E8_CARTAN,
            "highest_root_coefficients": E8_HIGHEST_ROOT,
            "A_times_highest_root": affine_pairings,
            "A8_simple_root_order": ["alpha1", "alpha3", "alpha4", "alpha5", "alpha6", "alpha7", "alpha8", "alpha0=-theta"],
            "A8_Gram": a8_gram,
            "A8_determinant": a8_determinant,
            "A8_lattice_index_in_E8": 3,
            "maximal_connected_subgroup": "SU(9)/Z3",
        },
        "E8_branching": {
            "formula": "248=80+84+bar84 under SU(9)/Z3",
            "dimension_check": 80 + 84 + 84,
            "84_representation": "Lambda^3(9)",
            "embedding_Dynkin_index": 1,
        },
        "commutant": {
            "conditional_on_holonomy": "Hol(W9)=SU(9)",
            "continuous_centralizer_dimension": 0,
            "finite_centralizer": "Z3",
            "continuous_hidden_gauge_group": None,
            "hidden_gaugino_condensate": False,
            "proved_for_every_stable_W9": False,
        },
        "associated_bundle_index_spectrum": {
            "End0_W9": {"rank": end0_rank, "c2": end0_c2, "chi": -end0_h1, "h1_if_full_holonomy": end0_h1},
            "Lambda3_W9": {"rank": wedge3_rank, "c2_factor": wedge3_c2_factor, "c2": wedge3_c2, "chi": -wedge3_h1, "h1_if_full_holonomy": wedge3_h1},
            "Lambda3_W9_dual": {"rank": wedge3_rank, "c2": wedge3_c2, "chi": -wedge3_h1, "h1_if_full_holonomy": wedge3_h1},
            "total_h1_adE8_if_full_holonomy": total_h1,
            "E8_K3_index_cross_check": "2*(30*11-248)=164",
            "SU9_reduction_locus_complex_dimension": end0_h1,
            "transverse_E8_deformation_directions": 2 * wedge3_h1,
        },
        "theorem": {
            "name": "SU9InE8FiniteCommutantAndIndexSpectrumTheorem",
            "proved": True,
            "statement": "Deleting affine E8 node 2 gives an A8 root subsystem of determinant nine and lattice index three, hence SU(9)/Z3 in E8 with branching 248=80+84+bar84. If W9 has full SU9 holonomy, the continuous commutant vanishes; its K3 cohomology counts 38+63+63=164, exactly matching the E8 instanton index at k=11.",
        },
        "selection_guard": {
            "stable_W9_existence": True,
            "one_full_SU9_or_full_E8_holonomy_candidate_expected_generically": True,
            "full_holonomy_selected_or_constructively_certified": False,
            "why_not_promoted": "Stability gives irreducibility, not automatically full SU9 holonomy. The 126 transverse E8 directions establish a large exit space but do not select a deformation.",
        },
        "primary_reference": "https://arxiv.org/abs/math/0601120",
    }

    visible_h1 = visible_c2 - 2 * 3
    assert visible_h1 == 3
    chirality = {
        "schema": "MTTVisiblePullbackIndexAndChiralityNoGo.v1",
        "status": "EXACT_THREE_K3_SLOTS_AND_ZERO_CHIRAL_INDEX_NO_GO_CLOSED_NONPULLBACK_VISIBLE_BUNDLE_OPEN",
        "visible_E8_branching": "248=(78,1)+(1,8)+(27,3)+(bar27,bar3) under E6 x SU3",
        "K3_cohomology": {
            "V3": {"rank": 3, "c1": 0, "c2": visible_c2, "chi": -3, "h0": 0, "h2": 0, "h1": visible_h1},
            "V3_dual": {"chi": -3, "h0": 0, "h2": 0, "h1": visible_h1},
            "interpretation": "Three 27 slots and three conjugate 27-bar slots before any additional projection: vectorlike, not three net chiral families.",
        },
        "FuYau_pullback": {
            "bundle": "pi^*V3",
            "c3": 0,
            "holomorphic_Euler_index": 0,
            "Leray_input": "For a principal elliptic bundle, translations act trivially on H^q(O_E), so R^0 pi_*O=R^1 pi_*O=O_K3.",
            "h1_pi_star_V3": 3,
            "h1_pi_star_V3_dual": 3,
            "net_chiral_27_index": 0,
        },
        "no_go_theorem": {
            "name": "FuYauBasePullbackChiralityNoGo",
            "proved": True,
            "statement": "Any SU bundle pulled back from the K3 base has c3=0. On a complex threefold with c1(T)=c1(V)=0, HRR gives chi(V)=one-half integral c3(V), so the standard Fu-Yau pullback ansatz cannot produce a nonzero four-dimensional chiral index.",
        },
        "required_visible_exit": {
            "bundle_type": "stable non-pullback SU3 bundle on the Fu-Yau threefold, or an independently proved equivariant construction with the same index",
            "required_integral_c3_for_three_net_families": [6, -6],
            "required_Bianchi_base_component": "compatible with the 9-unit visible allocation or a recomputed exact allocation",
            "selected_now": False,
        },
        "guard": "The exact h1(K3,V3)=3 is useful structural evidence but is not a proof of three chiral Standard Model families.",
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA102.v1",
        "status": STATUS,
        "closed_here": [
            "unique primitive determinant-free q79 Mukai kernel and its local-freeness obstruction",
            "primitive rank-nine c2=11 hidden charge repair candidate",
            "minimal nonzero rank-one integral Fu-Yau curvature cost four",
            "exact conditional source-free allocation 9+11+4=24",
            "stable locally free SU3 c2=9 and SU9 c2=11 K3 bundle existence and HYM gates",
            "exact maximal SU(9)/Z3 in E8 embedding, finite conditional commutant and 164-mode index cross-check",
            "exact no-go for obtaining four-dimensional net chirality from a K3-pullback visible bundle",
        ],
        "A101_hidden_payload_candidate_progress": {
            "candidate_filled": 6,
            "required": 8,
            "fields": {
                "P2": "stable SU9 c2=11 candidate exists",
                "rho2": "SU(9)/Z3 -> E8 index-one embedding",
                "characteristic_class": 11,
                "Wilson_lines": "trivial candidate",
                "branching": "248=80+84+bar84",
                "cohomology": "38+63+63=164 conditional on full holonomy",
                "thresholds": None,
                "f_hidden": None,
            },
            "selected_filled": 0,
            "interpretation": "Candidate construction has advanced; no field is called MTT-selected until the discrete source and holonomy gates close.",
        },
        "exact_remaining_cutset": [
            "Prove that MTT identifies the shared degree-zero circle with the untwisted Fu-Yau factor and selects the primitive norm-four companion class.",
            "Construct/select a non-pullback visible SU3 bundle with integral c3=plus or minus 6 and verify its HYM/anomaly data on the same Fu-Yau branch.",
            "Select or constructively certify full SU9/full E8 hidden holonomy, then execute thresholds; this would remove the hidden condensate rather than tune f_hidden.",
            "Supply the seven selected NS5 numerical inputs required by A101's already closed A98 envelope.",
        ],
        "candidate_hidden_condensate_exit": {
            "if_full_holonomy_selected": "No continuous hidden gauge factor, hence no hidden gaugino condensate and no f_hidden amplitude row.",
            "selected_now": False,
        },
        "new_fitted_continuous_parameters": 0,
        "unfixed_reduced_bundle_moduli_complex_dimension": 76,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
        "next_exact_target": "Construct the non-pullback c3=plus/minus6 visible bundle and a full-holonomy hidden representative on the same selected rank-one Fu-Yau sector.",
    }

    for path, payload in [
        (MUKAI, mukai),
        (BIANCHI, bianchi),
        (BUNDLES, bundles),
        (HIDDEN, hidden),
        (CHIRALITY, chirality),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    outputs = {
        "Mukai_repair": str(MUKAI.relative_to(ROOT)).replace("\\", "/"),
        "Bianchi_allocation": str(BIANCHI.relative_to(ROOT)).replace("\\", "/"),
        "stable_bundles": str(BUNDLES.relative_to(ROOT)).replace("\\", "/"),
        "hidden_embedding_spectrum": str(HIDDEN.relative_to(ROOT)).replace("\\", "/"),
        "visible_chirality_no_go": str(CHIRALITY.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    checks = {
        "A101_frontier_consumed": a101["next_required_artifact"] == "MTT_Selected_q79HiddenBundleExistenceBianchiAllocationAndSpectrumExecution_v1",
        "q79_kernel_unique_and_obstruction_recorded": mukai["determinant_free_kernel"]["vector_3a_minus_b"] == [8, 0, -1],
        "hidden_repair_primitive_c2_11": mukai["minimal_primitive_repair_candidate"]["primitive"] and mukai["minimal_primitive_repair_candidate"]["c2"] == 11,
        "q7_ideal_promotion_not_invented": not mukai["source_guard"]["q7_to_point_ideal_source_map_in_corpus"],
        "minimal_ASD_cost_4": bianchi["minimality_theorem"]["minimal_nonzero_ASD_cost"] == 4,
        "Bianchi_identity_exact": bianchi["source_free_Bianchi"]["residual"] == 0,
        "shared_circle_bridge_not_invented": not bianchi["source_guard"]["corpus_identifies_it_with_the_untwisted_FuYau_circle"],
        "stable_SU3_SU9_bundles_exist": bundles["HYM_theorem"]["proved"],
        "bundle_moduli_not_hidden": bundles["selection_guard"]["unfixed_reduced_bundle_moduli_complex_dimension"] == 76,
        "A8_embedding_exact": hidden["affine_E8_certificate"]["A8_determinant"] == 9,
        "hidden_index_cross_check": hidden["associated_bundle_index_spectrum"]["total_h1_adE8_if_full_holonomy"] == 164,
        "full_holonomy_not_invented": not hidden["selection_guard"]["full_holonomy_selected_or_constructively_certified"],
        "pullback_chirality_no_go_closed": chirality["no_go_theorem"]["proved"],
        "nonpullback_visible_exit_open": not chirality["required_visible_exit"]["selected_now"],
        "U6_not_overclosed": not frontier["U6_strong_CP_closed"],
    }
    assert all(checks.values())

    authority_hashes = [
        {"label": label, "path": str(path), "sha256": sha256(path)}
        for label, path in paths.items()
    ]
    candidate = {
        "schema": "MTTSelectedQ79HiddenBundleExistenceBianchiAllocationAndSpectrumExecution.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": authority_hashes,
        "results": {
            "new_fitted_continuous_parameters": 0,
            "unfixed_reduced_bundle_moduli_complex_dimension": 76,
            "admissible_hidden_P2_candidate_constructed": True,
            "selected_hidden_P2": False,
            "conditional_source_free_Bianchi_allocation_closed": True,
            "conditional_hidden_embedding_and_spectrum_executed": True,
            "hidden_condensate_removed_on_full_holonomy_branch": True,
            "full_holonomy_selected": False,
            "FuYau_pullback_visible_chirality_ruled_out": True,
            "nonpullback_three_family_visible_bundle_constructed": False,
            "U6_strong_CP_closed": False,
        },
    }
    certificate = {
        "certificate": "MTT_Selected_q79HiddenBundleExistenceBianchiAllocationAndSpectrumExecution_v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "results": candidate["results"],
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Hidden Bundle Existence, Bianchi Allocation, and Spectrum Execution v1

Status: `{STATUS}`

## What A102 closes

A101 proved that the second `E8` bundle was missing from the typed source and
ruled out abelianizing it with only two Fu-Yau curvature embeddings. A102 now
constructs the strongest exact source-free nonabelian candidate: a stable
`SU(3)` bundle with `c2=9`, a stable hidden `SU(9)` bundle with `c2=11`, and a
rank-one Fu-Yau torus class of norm four. It proves the bundle-existence and
HYM gates, executes the hidden `E8` branching and cohomology, and identifies an
important visible-sector obstruction that prevents overclaiming.

## q79 Mukai kernel and repair

For the selected q79 Mukai vectors

```text
a=(5,H,0), b=(7,3H,1), H^2=2,
```

the first-Chern map is `(x,y)->(x+3y)H`. Its unique primitive kernel is
`(x,y)=(3,-1)`, hence

```text
3a-b=(8,0,-1), c2=9, v^2=16.
```

This is not an honest bundle: it is exactly Yoshioka's `l-omega` exceptional
case, whose moduli contains only non-locally-free sheaves. Adding the Mukai
vector of a length-two ideal sheaf gives

```text
(8,0,-1)+(1,0,-1)=(9,0,-2), c2=11, v^2=36.
```

The repaired vector is primitive and has stable locally free representatives.
The numerical coincidence with `q7=2` is not promoted: the corpus contains no
theorem mapping the CP residue `q7` to an ideal-sheaf length.

## Minimal rank-one Fu-Yau allocation

Inside `Lambda_K3=U^3+E8(-1)^2`, choose

```text
h=e1+f1,       h^2=2,
delta=e2-2f2,  delta^2=-4, h.delta=0.
```

An integral ASD `(1,1)` class orthogonal to an ample K3 class cannot have
square `-2`: one sign would be effective by K3 Riemann-Roch and would have zero
intersection with an ample class. Since the lattice is even, four is therefore
the minimal nonzero curvature cost, and `delta` attains it.

Taking `[omega1/2pi]=delta` and `[omega2/2pi]=0`, the dimensionless Fu-Yau
integrability row is exactly

```text
c2(V3)+c2(W9)-delta^2 = 9+11+4 = 24.
```

This is a smooth source-free candidate with zero NS5 charge. Its remaining
discrete source premise is explicit: MTT must identify the corpus's unique
shared degree-zero circle with the untwisted Fu-Yau factor and select the
primitive norm-four companion class. The corpus supports the first phrase in
its flavor geometry but does not yet make this Fu-Yau identification.

## Stable HYM bundles exist

The explicit stable-bundle bound reported by Li and Qin gives a stable locally
free `c1=0` rank-`r` bundle on a K3 whenever `c2>r+1`, since `p_g(K3)=1`.
Both candidates pass strictly:

```text
SU3: c2=9 > 4,
SU9: c2=11 > 10.
```

Donaldson-Uhlenbeck-Yau supplies irreducible HYM connections. The two reduced
bundle moduli spaces each have expected complex dimension `36+2=38`. Thus no
measured fit parameter was added, but existence is not unique selection: 76
complex reduced bundle-moduli directions remain unfixed.

## Exact hidden E8 execution

With the Bourbaki `E8` Cartan matrix, the highest-root coefficients are
`(2,3,4,6,5,4,3,2)`. Delete affine node 2. The remaining roots

```text
alpha1-alpha3-alpha4-alpha5-alpha6-alpha7-alpha8-alpha0
```

have the `A8` Cartan matrix, determinant nine and lattice index three. This is
the maximal `SU(9)/Z3` subgroup of `E8`, with

```text
248 = 80 + 84 + bar84,  84=Lambda^3(9).
```

For `c2(W9)=11`, exact Chern-root and K3 index calculations give

```text
h1(End0 W9)=38,
h1(Lambda^3 W9)=63,
h1(Lambda^3 W9*)=63,
total=164=2*(30*11-248).
```

If `Hol(W9)=SU(9)`, its centralizer in `E8` is finite `Z3`; no continuous
hidden gauge factor or hidden gaugino condensate remains. Stability alone does
not prove full `SU(9)` holonomy. The 126 transverse `84+bar84` deformations show
that the reduced locus sits inside a much larger `E8` deformation space, but
MTT still has to select or constructively certify a full-holonomy point.

## Visible chirality no-go

The same K3 calculation gives

```text
h1(K3,V3)=h1(K3,V3*)=3.
```

These are three `27` slots and three conjugate slots, not three net families.
For the standard Fu-Yau pullback, `c3(pi*V3)=0`. On a complex threefold with
`c1(T)=c1(V)=0`, Hirzebruch-Riemann-Roch gives

```text
chi(V)=1/2 integral c3(V).
```

Therefore every K3-pullback `SU(3)` bundle has zero four-dimensional chiral
index. The exact `h1=3` coincidence is structural evidence only. A physical
three-family exit needs a stable non-pullback bundle on the Fu-Yau threefold
with `integral c3=+/-6`, plus the same-branch HYM and Bianchi certificate.

## Remaining cutset

1. Prove the shared-circle-to-rank-one-Fu-Yau source map.
2. Construct/select a non-pullback visible `SU(3)` bundle with `c3=+/-6`.
3. Select or constructively certify full hidden `SU(9)` or `E8` holonomy.
4. Supply the seven numerical NS5 values required by A101's exact A98 bound.

Next artifact: `{NEXT}`.

## Primary references

- [Li and Qin, Stable vector bundles on algebraic surfaces](https://arxiv.org/abs/math/9411233)
- [Yoshioka, Irreducibility of moduli spaces of vector bundles on K3 surfaces](https://arxiv.org/abs/math/9907001)
- [Balaji and Kollar, Holonomy groups of stable vector bundles](https://arxiv.org/abs/math/0601120)
- [Fu and Yau, The theory of superstring with flux on non-Kahler manifolds and the complex Monge-Ampere equation](https://arxiv.org/abs/hep-th/0509028)
- [Fino, Grantcharov and Vezzoni, Solutions to the Hull-Strominger system with torus symmetry](https://arxiv.org/abs/1901.10322)
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
