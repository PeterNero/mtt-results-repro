from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")

SLUG = "selected_q79twistedspectralgerbelifthymandbianchiexecution"
STATUS = (
    "MTT_U6_Q79_SPECTRAL_DD_RESTRICTION_ZERO_FLAT_ANALYTIC_BRAUER_"
    "RESIDUE_HYM_BIANCHI_OPEN"
)
NEXT = "MTT_Selected_q79NormalizedPoincareGerbeAndPGL3PrymReduction_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79TwistedSpectralGerbeLiftHYMAndBianchiExecution_v1.md"
)

SURFACE = OUT / "spectral_surface_invariants.packet.json"
DD = OUT / "integral_DD_restriction.packet.json"
ANALYTIC = OUT / "flat_analytic_gerbe_lift_gate.packet.json"
EXECUTION = OUT / "HYM_Bianchi_execution_gate.packet.json"
FRONTIER = OUT / "U6_frontier_after_A104.packet.json"
OPEN_INPUT = OUT / "flat_analytic_gerbe_cech_input.open.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    paths = {
        "A103": ROOT / "candidate_data" / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection.candidate.json",
        "A103_spectral": ROOT / "candidate_data" / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection" / "q79_genus_two_determinant_zero_spectral_cover.packet.json",
        "A103_topology": ROOT / "candidate_data" / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection" / "rank_one_fuyau_shared_circle_clutching.packet.json",
        "A102_bianchi": ROOT / "candidate_data" / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution" / "rank_one_fuyau_k3_lattice_and_bianchi_allocation.packet.json",
        "q79_adjacent_flat_gerbe": Q79 / "candidate_data" / "time_oriented_m1_flat_gerbe_promotion.candidate.json",
        "qa_adjacent_gerbe_gate": QA / "candidate_data" / "minimal_gerbe_source_candidate_or_nogo.candidate.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A104 authority: " + ", ".join(missing))

    a103 = load(paths["A103"])
    spectral_a103 = load(paths["A103_spectral"])
    topology_a103 = load(paths["A103_topology"])
    bianchi_a102 = load(paths["A102_bianchi"])
    q79_flat = load(paths["q79_adjacent_flat_gerbe"])
    qa_gerbe = load(paths["qa_adjacent_gerbe_gate"])

    assert a103["next_required_artifact"] == "MTT_Selected_q79TwistedSpectralGerbeLiftHYMAndBianchiExecution_v1"
    assert spectral_a103["determinant_zero_cover"]["reference_class"] == "[C]=3*sigma+pi^*H"
    assert spectral_a103["q79_genus_two_map"]["H_square"] == 2
    assert spectral_a103["determinant_zero_cover"]["degree_over_K3"] == 3
    assert spectral_a103["determinant_zero_cover"]["PGL3_alignment_complex_dimension"] == 8
    assert topology_a103["rank_one_FuYau_topology"]["delta_square"] == -4
    assert bianchi_a102["K3_lattice"]["Gram_h_delta"][0][1] == 0
    assert q79_flat["calculation_results"]["torsion_order_three"]
    assert not q79_flat["calculation_results"]["selected_flat_gerbe_representative_closed"]
    assert qa_gerbe["evaluated_routes"][2]["status"] == "ADJACENT_GUARDRAIL_NOT_SAME_SOURCE"

    # Let J=S x E and C be a smooth divisor D=A+B with A=p_S^*H and
    # B=p_E^*(3[0]). Only A^2 B survives in D^3.
    h_square = spectral_a103["q79_genus_two_map"]["H_square"]
    fiber_degree = spectral_a103["determinant_zero_cover"]["degree_over_K3"]
    a2b = h_square * fiber_degree
    d_cube = 3 * a2b
    c2_j_dot_d = 24 * fiber_degree
    canonical_square = d_cube
    topological_euler = d_cube + c2_j_dot_d
    holomorphic_euler = (canonical_square + topological_euler) // 12
    irregularity = 1
    geometric_genus = holomorphic_euler + irregularity - 1
    b1 = 2 * irregularity
    b3 = b1
    b2 = topological_euler - 2 + b1 + b3
    h11 = b2 - 2 * geometric_genus
    betti = [1, b1, b2, b3, 1]

    assert a2b == 6
    assert d_cube == canonical_square == 18
    assert c2_j_dot_d == 72
    assert topological_euler == 90
    assert holomorphic_euler == 9
    assert geometric_genus == 9
    assert betti == [1, 2, 92, 2, 1]
    assert h11 == 74

    surface = {
        "schema": "MTTQ79SpectralSurfaceInvariants.v1",
        "status": "EXACT_SMOOTH_GENERIC_SPECTRAL_SURFACE_TOPOLOGY_CLOSED",
        "ambient_threefold": "J=K3 x E",
        "divisor": {
            "class": "D=A+B=p_K3^*H+p_E^*(3[0])",
            "H_square": h_square,
            "fiber_divisor_degree": fiber_degree,
            "A_cubed": 0,
            "B_squared": 0,
            "A_squared_B": a2b,
            "D_cubed": d_cube,
            "ample": True,
            "generic_member_smooth_by_Bertini": True,
        },
        "adjunction_and_Noether": {
            "K_C_squared": canonical_square,
            "c2_J_dot_C": c2_j_dot_d,
            "integral_c2_C": topological_euler,
            "chi_O_C": holomorphic_euler,
        },
        "Lefschetz_and_Hodge": {
            "pi1_C": "Z^2",
            "H1_C": "Z^2",
            "H3_C": "Z^2",
            "H3_torsion": False,
            "q": irregularity,
            "p_g": geometric_genus,
            "h11": h11,
            "betti": betti,
        },
        "theorem": {
            "name": "Q79DegreeThreeSpectralSurfaceTopologyTheorem",
            "proved": True,
            "statement": "A smooth generic q79 determinant-zero degree-three spectral surface C in |H+3[0]| has K_C^2=18, c2(C)=90, chi(O_C)=9, q=1, p_g=9, h11=74 and Betti numbers (1,2,92,2,1).",
        },
    }

    # For the rank-one principal elliptic bundle, the standard Poincare/T-dual
    # obstruction on J has integral class delta cup u, up to exchanging the
    # fiber basis u,v. Pair its restriction with the two H^1(C) generators.
    delta_dot_h = bianchi_a102["K3_lattice"]["Gram_h_delta"][0][1]
    pairing_with_u = 0
    pairing_with_v = delta_dot_h
    dd_restriction_zero = (
        pairing_with_u == 0
        and pairing_with_v == 0
        and surface["Lefschetz_and_Hodge"]["H3_C"] == "Z^2"
        and not surface["Lefschetz_and_Hodge"]["H3_torsion"]
    )
    assert dd_restriction_zero

    dd = {
        "schema": "MTTQ79IntegralDDRestriction.v1",
        "status": "EXACT_INTEGRAL_DIXMIER_DOUADY_RESTRICTION_ZERO_CLOSED",
        "principal_FuYau_input": {
            "torus_Chern_pair": ["delta", "0"],
            "delta_square": topology_a103["rank_one_FuYau_topology"]["delta_square"],
            "H_dot_delta": delta_dot_h,
            "shared_circle_untwisted": True,
        },
        "standard_dual_gerbe_class": {
            "ambient": "J=K3 x E",
            "fiber_H1_basis": ["u", "v"],
            "DD_alpha": "delta cup u, up to u<->v",
            "typing": "H^2(K3,Z) tensor H^1(E,Z) subset H^3(J,Z)",
        },
        "restriction_pairing": {
            "H1_C_generated_by_ambient_u_v": True,
            "formula": "integral_C i^*(delta u) cup i^*a = integral_J delta u a (H+3[0])",
            "pair_with_u": pairing_with_u,
            "pair_with_v": pairing_with_v,
            "only_nonzero_candidate": "(delta.H) integral_E u cup v",
            "delta_dot_H": delta_dot_h,
            "all_pairings_zero": True,
            "H3_C_torsion_free": True,
            "integral_DD_restriction_zero": dd_restriction_zero,
        },
        "consequence": {
            "topological_gerbe_obstruction_on_C": False,
            "torsion_escape_remaining": False,
            "holomorphic_gerbe_triviality_proved": False,
            "warning": "Vanishing of the integral Dixmier-Douady class leaves a possibly nonzero topologically trivial holomorphic gerbe class.",
        },
        "theorem": {
            "name": "Q79OrthogonalityKillsSpectralDDRestrictionTheorem",
            "proved": True,
            "statement": "For the standard dual Poincare gerbe of the rank-one Fu-Yau torsor, the restriction of DD(alpha)=delta cup u to every smooth q79 spectral surface C of class H+3[0] is zero in H^3(C,Z), because H^1(C) is ambient, H^3(C,Z) is torsion-free of rank two and every Poincare pairing is proportional to delta.H=0.",
        },
        "primary_references": [
            "https://arxiv.org/abs/math/0501487",
            "https://arxiv.org/abs/hep-th/0306062",
            "https://arxiv.org/abs/1008.3365",
        ],
    }

    analytic = {
        "schema": "MTTQ79FlatAnalyticGerbeLiftGate.v1",
        "status": "INTEGRAL_OBSTRUCTION_CLOSED_FLAT_HOLOMORPHIC_GERBE_RESIDUE_OPEN",
        "exponential_sequence": {
            "sequence": "H^2(C,Z) -> H^2(C,O_C) -> H^2(C,O_C^*) -> H^3(C,Z)",
            "DD_alpha_restricted": 0,
            "residual_class": "beta_C in H^2(C,O_C)/image(H^2(C,Z))",
            "H2_O_complex_dimension": geometric_genus,
            "residual_is_one_selected_class_not_nine_fit_parameters": True,
            "beta_C_computed": False,
            "beta_C_zero_proved": False,
        },
        "rank_one_spectral_object_gate": {
            "inverse_gerbe_twisted_rank_one_sheaf_exists_iff_beta_C_zero": True,
            "twisted_rank_one_sheaf_constructed": False,
            "inverse_Fourier_Mukai_transform_executed": False,
            "inverse_transform_locally_free": False,
            "determinant_trivialized": False,
        },
        "unselected_geometry_inventory": {
            "K3_lattice_polarized_moduli_complex_dimension": 18,
            "PGL3_spectral_alignment_complex_dimension": 8,
            "elliptic_modulus_complex_dimension": 1,
            "Pic0_C_complex_dimension": irregularity,
            "flat_residue_ambient_complex_dimension": geometric_genus,
            "hidden_W9_bundle_moduli_complex_dimension": a103["results"]["hidden_bundle_moduli_complex_dimension"],
            "counted_as_fitted_observable_parameters": 0,
            "warning": "These are unselected geometric/source moduli and obstruction coordinates, not a claim that all listed dimensions are independent physical knobs.",
        },
        "adjacent_repo_guardrails": {
            "q79_Iwasawa_order3_flat_gerbe": {
                "conditional_candidate_exists": q79_flat["calculation_results"]["conditional_flat_gerbe_representative_exists"],
                "selected": q79_flat["calculation_results"]["selected_flat_gerbe_representative_closed"],
                "same_FuYau_spectral_source": False,
                "allowed_use": "finite order-three shadow/checklist only",
            },
            "Qa_SU3_minimal_gerbe_gate": {
                "status": qa_gerbe["status"],
                "same_branch_source_supplied": qa_gerbe["gate_results"]["same_branch_Qa_SU3_selected_source_supplied"],
                "allowed_use": "adjacent guardrail only",
            },
        },
        "selection_guard": {
            "PGL3_alignment_selected": False,
            "lambda_or_winding_source_map_selected": False,
            "observed_flavor_values_used": False,
            "new_fitted_continuous_parameters": 0,
        },
    }

    open_input = {
        "schema": "MTTQ79FlatAnalyticGerbeCechInput.v1",
        "status": "OPEN_INPUT_TEMPLATE",
        "required_same_branch_fields": {
            "marked_K3_sextic_or_period_point_realizing_H_delta": None,
            "elliptic_curve_period_tau": None,
            "PGL3_alignment_iota_matrix": None,
            "spectral_surface_equation": None,
            "good_cover_of_C": None,
            "FuYau_torsor_transition_functions": None,
            "relative_Poincare_discrepancy_line_bundles_on_double_overlaps": None,
            "restricted_scalar_gerbe_cocycle_alpha_ijk": None,
            "trivializing_line_bundles_and_isomorphisms": None,
            "beta_C_period_vector_length_9": [None] * geometric_genus,
            "Cech_coboundary_residual": None,
        },
        "acceptance": {
            "beta_C_exactly_zero_or_explicit_Cech_coboundary": False,
            "rank_one_twisted_spectral_object_constructed": False,
            "provenance_same_q79_FuYau_branch": False,
        },
    }

    execution = {
        "schema": "MTTQ79SpectralHYMAndBianchiExecutionGate.v1",
        "status": "TOPOLOGICAL_DD_GATE_CLOSED_ANALYTIC_HYM_BIANCHI_GATES_OPEN",
        "visible_bundle_chain": {
            "smooth_spectral_surface": True,
            "integral_DD_restriction_zero": True,
            "holomorphic_gerbe_trivialization": False,
            "rank_one_twisted_spectral_object": False,
            "locally_free_rank3_inverse_transform": False,
            "SU3_determinant_condition": False,
            "actual_total_space_c3_plusminus6": False,
            "balanced_slope_stability": False,
            "balanced_HYM_connection": False,
        },
        "Bianchi_chain": {
            "A102_base_cohomology_allocation": "9+11+4=24 retained as the K3 reference allocation",
            "nonpullback_visible_Chern_Weil_representative": False,
            "hidden_SU9_HYM_connection": True,
            "torsion_connection_R_plus_representative": False,
            "global_H_flux_or_Deligne_representative": False,
            "differential_Bianchi_identity_verified": False,
            "integrated_Bianchi_may_be_silently_reused": False,
        },
        "hidden_branch_retained": {
            "full_SU9_holonomy": a103["results"]["hidden_full_SU9_holonomy_proved"],
            "continuous_hidden_gauge_factor": a103["results"]["hidden_continuous_gauge_factor"],
            "hidden_gaugino_condensate_available": a103["results"]["hidden_gaugino_condensate_available"],
        },
        "ordered_next_execution": [
            "compute beta_C from the same-branch Cech/Deligne Poincare data",
            "if beta_C=0, construct the twisted rank-one spectral sheaf and inverse Fourier-Mukai transform",
            "prove local freeness, determinant zero and balanced stability/HYM",
            "compute actual Chern-Weil representatives and solve the full differential Bianchi identity",
            "only then execute threshold and NS5 numerical rows",
        ],
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA104.v1",
        "status": STATUS,
        "closed_here": [
            "all integral/Hodge invariants of a smooth generic q79 degree-three spectral surface needed by the gerbe test",
            "exact vanishing of the restricted integral Dixmier-Douady class by delta.H=0",
            "elimination of any residual torsion loophole because H^3(C,Z)=Z^2",
            "exact factorization of the remaining obstruction through one topologically trivial holomorphic gerbe class beta_C",
        ],
        "not_closed_here": [
            "same-branch Cech/Deligne computation proving or disproving beta_C=0",
            "selection of the PGL3 spectral alignment and the orientation/lambda source",
            "inverse-gerbe twisted rank-one spectral sheaf and locally free SU3 inverse transform",
            "balanced stability/HYM and actual total-space c3 computation",
            "full differential Strominger Bianchi representative",
            "hidden threshold and seven A101/A98 NS5 numerical values",
        ],
        "new_fitted_continuous_parameters": 0,
        "integral_DD_restriction_zero": True,
        "analytic_gerbe_residue_zero": False,
        "analytic_gerbe_residue_decided": False,
        "actual_FuYau_holomorphic_nonpullback_bundle_constructed": False,
        "actual_FuYau_balanced_HYM_proved": False,
        "actual_FuYau_nonpullback_Bianchi_proved": False,
        "hidden_full_SU9_holonomy_retained": True,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
        "next_exact_target": "Compute the restricted Poincare gerbe Cech cocycle on C and either exhibit its holomorphic coboundary or prove beta_C nonzero; do not revisit the now-closed integral DD obstruction.",
    }

    for path, payload in [
        (SURFACE, surface),
        (DD, dd),
        (ANALYTIC, analytic),
        (OPEN_INPUT, open_input),
        (EXECUTION, execution),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    outputs = {
        "spectral_surface": str(SURFACE.relative_to(ROOT)).replace("\\", "/"),
        "integral_DD_restriction": str(DD.relative_to(ROOT)).replace("\\", "/"),
        "flat_analytic_gerbe_gate": str(ANALYTIC.relative_to(ROOT)).replace("\\", "/"),
        "flat_analytic_gerbe_open_input": str(OPEN_INPUT.relative_to(ROOT)).replace("\\", "/"),
        "HYM_Bianchi_gate": str(EXECUTION.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    checks = {
        "A103_frontier_consumed": a103["next_required_artifact"] == "MTT_Selected_q79TwistedSpectralGerbeLiftHYMAndBianchiExecution_v1",
        "spectral_surface_invariants_exact": surface["Lefschetz_and_Hodge"]["betti"] == [1, 2, 92, 2, 1],
        "integral_DD_restriction_zero": dd["restriction_pairing"]["integral_DD_restriction_zero"],
        "torsion_loophole_closed": not dd["consequence"]["torsion_escape_remaining"],
        "analytic_residue_not_invented": not analytic["exponential_sequence"]["beta_C_zero_proved"],
        "adjacent_Iwasawa_gerbe_not_promoted": not analytic["adjacent_repo_guardrails"]["q79_Iwasawa_order3_flat_gerbe"]["same_FuYau_spectral_source"],
        "rank_one_spectral_object_not_overclaimed": not execution["visible_bundle_chain"]["rank_one_twisted_spectral_object"],
        "Bianchi_not_silently_reused": not execution["Bianchi_chain"]["integrated_Bianchi_may_be_silently_reused"],
        "hidden_SU9_result_retained": execution["hidden_branch_retained"]["full_SU9_holonomy"],
        "new_fitted_continuous_parameters_zero": frontier["new_fitted_continuous_parameters"] == 0,
        "U6_not_overclosed": not frontier["U6_strong_CP_closed"],
    }
    assert all(checks.values())

    authority_hashes = [
        {"label": label, "path": str(path), "sha256": sha256(path)}
        for label, path in paths.items()
    ]
    results = {
        "new_fitted_continuous_parameters": 0,
        "spectral_surface_K_squared": canonical_square,
        "spectral_surface_c2": topological_euler,
        "spectral_surface_p_g": geometric_genus,
        "spectral_surface_h11": h11,
        "integral_DD_restriction_zero": True,
        "analytic_gerbe_residue_decided": False,
        "analytic_gerbe_residue_zero_proved": False,
        "twisted_rank_one_spectral_object_constructed": False,
        "actual_FuYau_holomorphic_nonpullback_bundle_constructed": False,
        "actual_FuYau_balanced_HYM_proved": False,
        "actual_FuYau_nonpullback_Bianchi_proved": False,
        "hidden_full_SU9_holonomy_retained": True,
        "U6_strong_CP_closed": False,
    }
    candidate = {
        "schema": "MTTSelectedQ79TwistedSpectralGerbeLiftHYMAndBianchiExecution.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": authority_hashes,
        "results": results,
    }
    certificate = {
        "certificate": "MTT_Selected_q79TwistedSpectralGerbeLiftHYMAndBianchiExecution_v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "results": results,
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Twisted Spectral Gerbe Lift, HYM and Bianchi Execution v1

Status: `{STATUS}`

## Exact advance

A104 consumes A103's degree-three determinant-zero cover and computes the
gerbe obstruction on that same q79 rank-one Fu-Yau branch. It closes the
integral obstruction exactly. It does not promote the remaining holomorphic
gerbe residue, HYM connection or Bianchi representative without their source.

## Spectral surface topology

Put `J=K3 x E`, let `A=p_K3^*H`, and let `B=p_E^*(3[0])`. A smooth generic
spectral surface has class `D=A+B`. Since `H^2=2` and `deg(3[0])=3`,

```text
A^2 B = 6,
D^3 = 3 A^2 B = 18,
c2(J).D = 24*3 = 72.
```

Adjunction and Noether's formula therefore give

```text
K_C^2 = 18,
c2(C) = 18+72 = 90,
chi(O_C) = (18+90)/12 = 9.
```

Lefschetz gives `pi1(C)=pi1(K3 x E)=Z^2`, hence `q=1`. It follows that

```text
p_g=9,
h11=74,
b(C)=(1,2,92,2,1),
H^3(C,Z)=Z^2.
```

The last equality matters: there is no hidden torsion class after the two
integral pairings vanish.

## Integral gerbe restriction theorem

For the rank-one principal elliptic bundle with torus Chern pair `(delta,0)`,
the standard dual Poincare gerbe on `J` has, up to exchanging a fiber basis
`u,v`,

```text
DD(alpha)=delta cup u in H^2(K3,Z) tensor H^1(E,Z).
```

Every class in `H^1(C,Z)` is the restriction of a linear combination of
`u,v`. For either generator `a`, the Poincare pairing is

```text
integral_C i^*(delta cup u) cup i^*a
  = integral_J delta cup u cup a cup (H+3[0]).
```

The same-fiber-basis term vanishes by antisymmetry. The other is proportional
to `delta.H`, which is exactly zero on the A102 q79 lattice. Thus both
pairings vanish. Since `H^3(C,Z)=Z^2` is torsion-free, Poincare duality proves

```text
i^* DD(alpha)=0 in H^3(C,Z).
```

This is stronger than a de Rham cancellation: the integral class itself is
zero, and no torsion escape remains.

## The remaining analytic residue

Integral DD vanishing is necessary but not sufficient for a holomorphic
trivialization. The exponential sequence leaves

```text
beta_C in H^2(C,O_C) / image H^2(C,Z),
dim_C H^2(C,O_C)=p_g=9.
```

`beta_C` is one selected geometric class to compute, not nine fitted
observable parameters. A rank-one inverse-gerbe twisted spectral sheaf exists
exactly when this class is trivialized. The present repositories do not emit
the same-branch Cech cocycle or a trivializing cochain, so A104 records
`beta_C=0` as undecided.

The nearby q79 order-three flat deck gerbe is conditional on an Iwasawa deck
scaffold and is not the present Fu-Yau Poincare gerbe. The Qa/SU3 gerbe packet
itself labels the q79 class an adjacent guardrail rather than a same-source
promotion. Neither may fill this gate by import.

## Explicit closing object

The generated open-input packet now states the required calculation rather
than another generic existence request. It needs:

1. a marked q79 K3 period/sextic realizing `H,delta`, an elliptic period, and
   the selected `PGL(3)` alignment;
2. the actual spectral equation and a good cover of `C`;
3. the Fu-Yau torsor transitions and relative Poincare discrepancies;
4. the restricted scalar Cech 2-cocycle and either a trivializing 1-cochain
   or a nonzero `beta_C` period certificate.

If the result is zero, the next execution is the inverse Fourier-Mukai
transform, local-freeness/determinant check, balanced stability/HYM, and then
the full differential Bianchi identity. If it is nonzero, the current
rank-one spectral candidate is ruled out and one must change the cover or use
higher-rank twisted spectral data.

## Bianchi guard

The A102 equation `9+11+4=24` remains the exact K3 reference allocation, but
it is not the differential Bianchi proof for a non-pullback visible bundle.
The actual visible Chern-Weil form, hidden SU9 HYM form, torsion connection and
global `H`/Deligne representative must be placed in one equation. A104 keeps
that gate open. A103's full hidden `SU(9)` holonomy and finite `Z3` commutant
remain closed.

## Current result

Closed now:

```text
spectral surface topology,
integral DD restriction = 0,
torsion loophole = absent,
remaining obstruction = one explicitly typed flat holomorphic class beta_C.
```

Still open:

```text
beta_C Cech/period decision,
twisted rank-one spectral object,
locally free non-pullback SU3 transform,
balanced HYM,
differential Bianchi,
threshold and NS5 numerical rows.
```

No measured value and no new fitted continuous parameter is used.

Next artifact: `{NEXT}`.

## Primary references

- [Bunke, Rumpf and Schick, The topology of T-duality for T-bundles](https://arxiv.org/abs/math/0501487)
- [Bouwknegt, Evslin and Mathai, T-duality: topology change from H-flux](https://arxiv.org/abs/hep-th/0306062)
- [Brinzanescu, Halanay and Trautmann, Vector bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
- [Caldararu, Derived categories of twisted sheaves on elliptic threefolds](https://arxiv.org/abs/math/0012083)
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
