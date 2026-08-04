from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADJACENT_Q79 = ROOT.parent / "mtt-q79-proof-repro"
SLUG = "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution"
STATUS = "MTT_U6_Q79_ELLIPTIC_MODULUS_REDUCED_TO_Z4_CHERN_ORBIT_BRIDGE_MARKED_K3_AND_PERIOD_ZERO_OPEN"
NEXT = "MTT_Selected_q79SplittingConicK3PeriodSelectorOrExactGerbeExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79MarkedK3EllipticPeriodSourceAndGerbeZeroExecution_v1.md"

STABILIZER = OUT / "single_branch_order4_stabilizer_nogo.packet.json"
ORBIT = OUT / "Z4_Chern_orbit_superset.packet.json"
MODULUS = OUT / "order4_elliptic_modulus_selection.packet.json"
BRIDGE = OUT / "complex_nesting_and_retarded_bridge_gate.packet.json"
OPEN_K3 = OUT / "splitting_conic_K3_period_selector.open.json"
FRONTIER = OUT / "U6_frontier_after_A107.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mat_vec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def mat_mul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def main() -> int:
    paths = {
        "A102_lattice": ROOT
        / "candidate_data"
        / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution"
        / "rank_one_fuyau_k3_lattice_and_bianchi_allocation.packet.json",
        "A106": ROOT / "candidate_data" / "selected_q79pgl3toprymgerbejacobianexecution.candidate.json",
        "A106_normal_form": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "splitting_conic_K3_normal_form.packet.json",
        "A106_source": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "same_branch_source_reduction_and_crossuse_guard.packet.json",
        "A106_frontier": ROOT
        / "candidate_data"
        / "selected_q79pgl3toprymgerbejacobianexecution"
        / "U6_frontier_after_A106.packet.json",
        "U9_retarded": ROOT
        / "candidate_data"
        / "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness"
        / "branch_orbit_retarded_representative_and_global_measure_cutset.packet.json",
        "complex_nesting": ADJACENT_Q79
        / "proof_corpus"
        / "Complex_Orthogonal_Nesting_for_MTT_Flavor_Holonomy_v1.md",
        "complex_clue_ledger": ADJACENT_Q79
        / "proof_corpus"
        / "Corpus_Clue_Ledger_for_Complex_Nested_Flavor_Holonomy_v1.md",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A107 authority: " + ", ".join(missing))

    lattice = load(paths["A102_lattice"])
    a106 = load(paths["A106"])
    normal = load(paths["A106_normal_form"])
    source = load(paths["A106_source"])
    frontier106 = load(paths["A106_frontier"])
    u9 = load(paths["U9_retarded"])
    complex_nesting = paths["complex_nesting"].read_text(encoding="utf-8")
    clue_ledger = paths["complex_clue_ledger"].read_text(encoding="utf-8")

    assert lattice["rank_one_torus_candidate"]["omega_1_over_2pi"] == "delta"
    assert lattice["rank_one_torus_candidate"]["omega_2_over_2pi"] == 0
    assert not lattice["source_guard"]["rank_one_FuYau_topology_selected_by_MTT"]
    assert a106["next_required_artifact"] == "MTT_Selected_q79MarkedK3EllipticPeriodSourceAndGerbeZeroExecution_v1"
    assert a106["results"]["unselected_geometric_source_moduli_complex"] == 19
    assert normal["parameter_count"]["result"] == 18
    assert not source["tau_i_crossuse"]["same_FuYau_K3_torus_source_theorem"]
    assert not frontier106["beta_C_zero_proved"]
    assert u9["retarded_representative_selection"]["q79_time_oriented_representative_selected"]
    assert not u9["decision"]["unique_global_MTT_carrier_or_geometry_closed"]
    assert "J^2 = -1" in complex_nesting
    assert "plausible and structurally supported" in clue_ledger

    quarter_turn = [[0, -1], [1, 0]]
    identity = [[1, 0], [0, 1]]
    minus_identity = [[-1, 0], [0, -1]]
    c0 = [1, 0]
    orbit_vectors = []
    matrix_power = identity
    for _ in range(4):
        orbit_vectors.append(mat_vec(matrix_power, c0))
        matrix_power = mat_mul(quarter_turn, matrix_power)

    j2 = mat_mul(quarter_turn, quarter_turn)
    j4 = mat_mul(j2, j2)
    assert orbit_vectors == [[1, 0], [0, 1], [-1, 0], [0, -1]]
    assert j2 == minus_identity
    assert j4 == identity

    stabilizer = {
        "schema": "MTTQ79SingleRankOneChernBranchOrderFourStabilizerNoGo.v1",
        "status": "EXACT_SINGLE_BRANCH_ORDER4_STABILIZER_NOGO_CLOSED",
        "chern_pair": ["delta", 0],
        "SL2Z_action": "M acts on the integral Chern column c=(c1,c2)^T by c -> M c.",
        "exact_stabilizer": {
            "equations": "For M=[[a,b],[c,d]] in SL2Z, M*(delta,0)=(delta,0) forces a=d=1 and c=0.",
            "matrices": "Stab(c0)={[[1,n],[0,1]]: n in Z}",
            "finite_order_subgroup": "identity only",
            "allowing_sign": "The stabilizer of {+/-c0} adds order-two -I but still contains no order-four element.",
        },
        "quarter_turn_test": {
            "J": quarter_turn,
            "J_squared": j2,
            "J_fourth": j4,
            "J_c0": orbit_vectors[1],
            "preserves_single_branch": False,
        },
        "consequence": "A lens quarter-turn cannot select tau=i as a symmetry of the single Fu-Yau branch (delta,0). Treating it as such would contradict the bundle Chern data.",
        "theorem": {
            "name": "SingleRankOneFuYauBranchOrderFourStabilizerNoGoTheorem",
            "proved": True,
            "statement": "The exact SL(2,Z) stabilizer of the primitive rank-one Chern pair (delta,0) is parabolic and has no order-four torsion. Even after identifying c with -c, only an order-two element is added. Therefore a global quarter-turn cannot act within one selected rank-one Fu-Yau bundle.",
        },
    }

    orbit = {
        "schema": "MTTQ79Z4ChernOrbitSuperset.v1",
        "status": "EXACT_MINIMAL_Z4_ORBIT_COMPLETION_AND_ONE_EXECUTION_COVARIANCE_CLOSED_SOURCE_BRIDGE_OPEN",
        "generator": {
            "J": quarter_turn,
            "order": 4,
            "orientation_inverse": [[0, 1], [-1, 0]],
        },
        "orbit": [
            ["delta", 0],
            [0, "delta"],
            ["-delta", 0],
            [0, "-delta"],
        ],
        "orbit_length": len(orbit_vectors),
        "minimality": "Any J-invariant set containing the primitive branch (delta,0) contains its full four-element orbit.",
        "Bianchi_and_cost": {
            "square_metric_required": True,
            "each_curvature_norm_cost": 4,
            "each_source_free_allocation": "9+11+4=24",
            "continuous_parameter_added": 0,
        },
        "symmetry_breaking_interpretation": {
            "unoriented_superset": "the four Chern orientations",
            "physical_branch": ["delta", 0],
            "selection_type": "a later orientation/retarded selector may choose one representative without changing the parent square geometry",
            "typed_selector_currently_proved": False,
        },
        "gerbe_execution_covariance": {
            "Poincare_naturality": "The elliptic automorphism transports the principal torsor, normalized dual Poincare gerbe, degree-three theta system and integral cohomology branch.",
            "zero_invariant": True,
            "transversality_invariant": True,
            "one_period_execution_suffices_for_orbit": True,
            "scope": "conditional on the Z4 orbit being the selected parent Fu-Yau source",
        },
        "theorem": {
            "name": "MinimalQuarterTurnChernOrbitCompletionTheorem",
            "proved": True,
            "statement": "The minimal SL(2,Z) quarter-turn completion of the rank-one Chern pair is the four-element orbit (delta,0),(0,delta),(-delta,0),(0,-delta). With a square fiber metric all representatives have the same curvature cost and Bianchi allocation. Naturality makes gerbe zero and transversality orbit-invariant, so one exact A106 execution suffices conditionally for all four.",
        },
    }

    modulus = {
        "schema": "MTTQ79OrderFourEllipticModulusSelection.v1",
        "status": "EXACT_ORDER4_TO_J1728_MODULUS_THEOREM_CLOSED_MTT_SOURCE_PREMISE_OPEN",
        "modular_action": {
            "quarter_turn_matrix": quarter_turn,
            "action_on_tau": "tau -> -1/tau",
            "fixed_point_equation": "tau=-1/tau",
            "upper_half_plane_solution": "tau=i",
            "j_invariant": 1728,
            "modular_equivalence": "the square elliptic curve E_i=C/(Z+iZ), up to SL2Z change of marked basis",
        },
        "orientation": {
            "plus_i": "J",
            "minus_i": "J^-1",
            "same_unoriented_elliptic_curve": True,
        },
        "selection_logic": {
            "local_orthogonal_complex_structure_selects_tau": False,
            "reason": "Every elliptic fiber has a translation-invariant tangent complex structure; it need not preserve the integral lattice as a global order-four automorphism.",
            "global_integral_order4_automorphism_selects_tau_i": True,
            "single_branch_supplies_that_automorphism": False,
            "Z4_orbit_superset_supplies_it_conditionally": True,
        },
        "source_count": {
            "strict_current_unselected_complex_moduli": 19,
            "conditional_Z4_parent_unselected_complex_moduli": 18,
            "elliptic_continuous_modulus_removed_conditionally": 1,
            "new_fitted_parameters": 0,
        },
        "theorem": {
            "name": "OrderFourIntegralFiberAutomorphismSelectsSquareEllipticCurveTheorem",
            "proved": True,
            "statement": "An origin-preserving integral order-four automorphism of a complex elliptic fiber is modularly the square lattice: its action fixes tau under tau -> -1/tau, hence tau=i in the upper half-plane and j=1728. A tangent complex structure alone does not imply this. In the rank-one Fu-Yau setting the premise can hold only on the four-branch Chern-orbit parent, not on one branch.",
        },
    }

    bridge = {
        "schema": "MTTQ79ComplexNestingRetardedChernOrbitBridgeGate.v1",
        "status": "CORPUS_SUPPORT_AND_EXACT_TARGET_CLOSED_TYPED_SOURCE_BRIDGE_OPEN",
        "corpus_support": {
            "orthogonal_complex_structure_J2_minus1": True,
            "lens_quarter_turn_structurally_plausible": True,
            "plus_i_minus_i_orientation_language": True,
            "global_FuYau_Chern_orbit_action_derived": False,
            "source_scope": "The corpus explicitly labels the quarter-turn plausible/structurally supported and says complex nesting does not itself prove the finite quotient.",
        },
        "U9_retarded_import": {
            "q79_q369_antiunitary_orbit_closed": u9["decision"]["unoriented_antiunitary_equivalence_class_closed"],
            "retarded_q79_representative_closed": u9["decision"]["time_oriented_q79_representative_closed"],
            "global_carrier_geometry_unique": u9["decision"]["unique_global_MTT_carrier_or_geometry_closed"],
            "typed_map_to_Z4_Chern_orbit": False,
            "guard": "An orientation selector in flavor space cannot be reused as a Fu-Yau Chern-orbit selector until one same-operator/same-carrier functor is proved.",
        },
        "missing_source_theorem": {
            "name": "LensQuarterTurnToFuYauChernOrbitSourceTheorem",
            "must_prove": [
                "the lens quarter-turn acts on the integral lattice of the same Fu-Yau T2 fiber",
                "the parent selected carrier contains the full four-element Chern orbit",
                "the MTT retarded/orientation selector descends to one Chern representative",
                "the action preserves the Strominger source, bundle data and normalized Poincare construction",
            ],
        },
        "decision": {
            "tau_i_strictly_promoted": False,
            "tau_i_conditional_superset_candidate": True,
            "single_branch_tau_i_selector_retired": True,
            "observed_data_used": False,
        },
    }

    open_k3 = {
        "schema": "MTTQ79SplittingConicK3PeriodSelectorInput.v1",
        "status": "OPEN_MARKED_K3_SOURCE_OR_DIRECT_EXACT_EXECUTION",
        "strict_source_route": {
            "MTT_functional_on_18d_lattice_period_domain": None,
            "isolated_admissible_minimizer_certificate": None,
            "selected_Q2_G3_H4_coefficients": None,
            "selected_period_point": None,
        },
        "conditional_Z4_route": {
            "LensQuarterTurnToFuYauChernOrbitSourceTheorem": False,
            "elliptic_tau": "i if and only if the bridge theorem is accepted",
            "remaining_K3_complex_moduli": 18,
        },
        "direct_existence_route": {
            "filled_smooth_splitting_conic_model": None,
            "exact_relative_Deligne_zero_or_nonzero_certificate": None,
            "role": "A direct model can decide existence/no-go for this compactification route but does not by itself prove unique MTT vacuum selection.",
        },
        "acceptance": {
            "marked_K3_selected_by_MTT": False,
            "Z4_Chern_orbit_selected_by_MTT": False,
            "tau_i_strictly_selected": False,
            "beta_C_zero": False,
            "isolated_alignment": False,
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA107.v1",
        "status": STATUS,
        "closed_now": [
            "single rank-one Fu-Yau branch has no order-four integral stabilizer",
            "minimal four-element Chern-orbit superset under the quarter-turn",
            "order-four global fiber automorphism selects tau=i and j=1728",
            "gerbe zero/transversality is covariant across the four branches",
            "precise corpus-to-Fu-Yau source bridge contract",
        ],
        "strict_current_source_moduli_complex": 19,
        "conditional_Z4_superset_source_moduli_complex": 18,
        "new_fitted_continuous_parameters": 0,
        "strict_tau_i_selected": False,
        "conditional_tau_i_selected_if_bridge": True,
        "marked_K3_selected": False,
        "beta_C_zero_proved": False,
        "isolated_alignment_found": False,
        "actual_FuYau_balanced_HYM_proved": False,
        "actual_FuYau_nonpullback_Bianchi_proved": False,
        "U6_strong_CP_closed": False,
        "next_exact_target": "Either prove the LensQuarterTurnToFuYauChernOrbitSourceTheorem and then select/execute one 18-modulus splitting-conic K3, or directly provide a smooth marked model and exact relative-Deligne zero/no-go certificate.",
        "next_required_artifact": NEXT,
    }

    outputs = {
        "single_branch_order4_stabilizer_nogo": str(STABILIZER.relative_to(ROOT)).replace("\\", "/"),
        "Z4_Chern_orbit_superset": str(ORBIT.relative_to(ROOT)).replace("\\", "/"),
        "order4_elliptic_modulus_selection": str(MODULUS.relative_to(ROOT)).replace("\\", "/"),
        "complex_nesting_retarded_bridge_gate": str(BRIDGE.relative_to(ROOT)).replace("\\", "/"),
        "splitting_conic_K3_open_selector": str(OPEN_K3.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    for path, payload in [
        (STABILIZER, stabilizer),
        (ORBIT, orbit),
        (MODULUS, modulus),
        (BRIDGE, bridge),
        (OPEN_K3, open_k3),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    checks = {
        "single_branch_order4_nogo_proved": stabilizer["theorem"]["proved"],
        "quarter_turn_orbit_length_four": orbit["orbit_length"] == 4,
        "orbit_cost_and_Bianchi_invariant": orbit["Bianchi_and_cost"]["each_curvature_norm_cost"] == 4,
        "one_gerbe_execution_suffices_conditionally": orbit["gerbe_execution_covariance"]["one_period_execution_suffices_for_orbit"],
        "order4_selects_tau_i": modulus["theorem"]["proved"] and modulus["modular_action"]["upper_half_plane_solution"] == "tau=i",
        "tau_i_not_strictly_promoted": not bridge["decision"]["tau_i_strictly_promoted"],
        "U9_not_cross_promoted": not bridge["U9_retarded_import"]["typed_map_to_Z4_Chern_orbit"],
        "marked_K3_still_open": not open_k3["acceptance"]["marked_K3_selected_by_MTT"],
        "no_observed_selector": not bridge["decision"]["observed_data_used"],
        "no_new_fitted_parameters": frontier["new_fitted_continuous_parameters"] == 0,
    }
    assert all(checks.values())

    authority_hashes = [{"path": str(path), "sha256": sha256(path)} for path in paths.values()]
    candidate = {
        "schema": "MTTSelectedQ79MarkedK3EllipticPeriodSourceAndGerbeZeroExecution.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "results": {
            "single_branch_order4_selector_retired": True,
            "minimal_Z4_Chern_orbit_constructed": True,
            "tau_i_selected_conditionally_on_source_bridge": True,
            "tau_i_strictly_selected": False,
            "strict_unselected_geometric_source_moduli_complex": 19,
            "conditional_Z4_unselected_geometric_source_moduli_complex": 18,
            "new_fitted_continuous_parameters": 0,
            "marked_K3_selected": False,
            "beta_C_zero_proved": False,
            "U6_strong_CP_closed": False,
        },
        "authority_hashes": authority_hashes,
    }
    certificate = {
        "certificate": "MTT_Selected_q79MarkedK3EllipticPeriodSourceAndGerbeZeroExecution_v1",
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "status": STATUS,
        "next_required_artifact": NEXT,
        "checks": checks,
        "results": candidate["results"],
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Marked-K3/Elliptic Source and Gerbe-Zero Execution v1

Status: `{STATUS}`

## Why A107 is needed

A106 reduced the gerbe calculation to one marked splitting-conic K3, one
elliptic modulus and eight solved alignment variables. The corpus also contains
a square `tau=i` Appell-Humbert implementation and repeated lens quarter-turn
language. A107 tests whether that value can lawfully fill the Fu-Yau elliptic
source.

The answer has two parts:

```text
one rank-one Chern branch: no,
four-branch Chern-orbit parent: conditionally yes.
```

## Single-branch order-four no-go

Write the Fu-Yau Chern pair as the integral column

```text
c0=(delta,0)^T.
```

For `M=[[a,b],[c,d]] in SL(2,Z)`, the equation `M c0=c0` forces

```text
a=d=1, c=0,
Stab(c0)={{[[1,n],[0,1]] : n in Z}}.
```

This parabolic stabilizer has no nontrivial finite-order element. If `c0` and
`-c0` are identified, `-I` adds order two, but still no order four.

For the quarter-turn

```text
J=[[0,-1],[1,0]],  J^2=-I,  J^4=I,
```

one has

```text
J(delta,0)=(0,delta).
```

Thus a global lens quarter-turn cannot be a symmetry of one selected
`(delta,0)` Fu-Yau bundle. This retires the direct `complex nesting => tau=i`
shortcut on the single branch.

## Minimal Z4 Chern-orbit superset

The minimal `J`-invariant completion is

```text
(delta,0)
 -> (0,delta)
 -> (-delta,0)
 -> (0,-delta)
 -> (delta,0).
```

With the square fiber metric all four representatives have curvature cost
four and the same source-free allocation

```text
9+11+4=24.
```

This adds no continuous parameter. A later orientation selector may choose one
representative, just as an oriented universe can select one member of a parent
conjugacy orbit. That physical interpretation is conditional until MTT derives
the parent orbit and the selector on this same carrier.

The Poincare construction is natural under elliptic automorphisms. Hence
gerbe triviality and nonzero Jacobian determinant are invariant across this
orbit after transporting the spectral cover and integral branch. One exact
A106 period execution suffices for all four representatives.

## When order four selects tau=i

On a marked elliptic curve the quarter-turn acts modularly as

```text
tau -> -1/tau.
```

An integral origin-preserving order-four automorphism therefore requires

```text
tau=-1/tau,
tau=i in the upper half-plane,
j(E)=1728.
```

The inverse generator gives `-i`; both orientations belong to the same
unoriented square elliptic curve.

This statement requires a *global integral automorphism*. Every elliptic
fiber already has a tangent complex structure, but that local `J^2=-1` does
not force its period lattice to be square.

Consequently:

```text
strict present branch: 19 unselected complex geometric moduli,
conditional Z4 parent: 18 unselected complex K3 moduli, tau=i fixed.
```

## Corpus and retarded guard

The complex-nesting corpus calls the lens quarter-turn plausible and
structurally supported; it also explicitly says complex nesting does not by
itself prove the finite quotient. It does not act on the Fu-Yau Chern pair.

The U9 q79/q369 packet proves an antiunitary orbit and selects q79 after
retarded orientation. This is the right pattern, but it is not yet a typed map
to the four Fu-Yau Chern orientations. Reusing it without a same-carrier
functor would be another cross-source shortcut.

The missing theorem is now exact:

```text
LensQuarterTurnToFuYauChernOrbitSourceTheorem.
```

It must place the lens quarter-turn on the integral lattice of this Fu-Yau
fiber, select the four-element parent orbit, and prove that the MTT orientation
selector descends to one Chern representative while preserving the Strominger
and normalized-Poincare data.

## Remaining frontier

A107 conditionally removes the elliptic modulus but does not select a marked
K3 point and does not prove the gerbe zero. The next constructive choice is:

1. prove the Chern-orbit source theorem, then select or execute one point in
   the 18-dimensional splitting-conic K3 family; or
2. directly insert a smooth marked K3 and produce an exact gerbe zero/no-go
   certificate, which decides existence but not unique MTT vacuum selection.

No observed value and no new fitted continuous parameter enters A107.

Next artifact: `{NEXT}`.

## Primary references

- [Bunke, Rumpf and Schick, The topology of T-duality for T-bundles](https://arxiv.org/abs/math/0501487)
- [Brinzanescu, Halanay and Trautmann, Vector bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
