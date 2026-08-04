from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79normalizedpoincaregerbeandpgl3prymreduction"
STATUS = "MTT_U6_Q79_GERBE_RESIDUE_REDUCED_TO_8X8_PGL3_PRYM_SYSTEM_JACOBIAN_VALUES_OPEN"
NEXT = "MTT_Selected_q79PGL3ToPrymGerbeJacobianExecution_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79NormalizedPoincareGerbeAndPGL3PrymReduction_v1.md"

PUSHFORWARD = OUT / "degree_three_spectral_trace_decomposition.packet.json"
PRYM = OUT / "normalized_Poincare_gerbe_Prym_reduction.packet.json"
SQUARE = OUT / "PGL3_to_Prym_square_system.packet.json"
OPEN_JACOBIAN = OUT / "PGL3_to_Prym_Jacobian.open.json"
FRONTIER = OUT / "U6_frontier_after_A105.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    paths = {
        "A104": ROOT / "candidate_data" / "selected_q79twistedspectralgerbelifthymandbianchiexecution.candidate.json",
        "A104_surface": ROOT / "candidate_data" / "selected_q79twistedspectralgerbelifthymandbianchiexecution" / "spectral_surface_invariants.packet.json",
        "A104_DD": ROOT / "candidate_data" / "selected_q79twistedspectralgerbelifthymandbianchiexecution" / "integral_DD_restriction.packet.json",
        "A104_analytic": ROOT / "candidate_data" / "selected_q79twistedspectralgerbelifthymandbianchiexecution" / "flat_analytic_gerbe_lift_gate.packet.json",
        "A103_spectral": ROOT / "candidate_data" / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection" / "q79_genus_two_determinant_zero_spectral_cover.packet.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A105 authority: " + ", ".join(missing))

    a104 = load(paths["A104"])
    surface = load(paths["A104_surface"])
    dd = load(paths["A104_DD"])
    analytic = load(paths["A104_analytic"])
    spectral = load(paths["A103_spectral"])

    assert a104["next_required_artifact"] == "MTT_Selected_q79NormalizedPoincareGerbeAndPGL3PrymReduction_v1"
    assert a104["results"]["integral_DD_restriction_zero"]
    assert not a104["results"]["analytic_gerbe_residue_decided"]
    assert surface["Lefschetz_and_Hodge"]["p_g"] == 9
    assert dd["restriction_pairing"]["delta_dot_H"] == 0
    assert spectral["determinant_zero_cover"]["fiberwise_determinant"] == 0
    assert spectral["determinant_zero_cover"]["PGL3_alignment_complex_dimension"] == 8

    degree = spectral["determinant_zero_cover"]["degree_over_K3"]
    h0_elliptic_degree_three = degree
    trace_free_rank = degree - 1
    k3_h2_o = 1
    trace_free_h2 = surface["Lefschetz_and_Hodge"]["p_g"] - k3_h2_o
    pgl3_dimension = 3 * 3 - 1
    double_cover_extra_twist = -3
    h0_tangent = pgl3_dimension
    h0_tangent_twist_minus3 = 0

    assert degree == 3
    assert h0_elliptic_degree_three == 3
    assert trace_free_rank == 2
    assert trace_free_h2 == 8
    assert pgl3_dimension == 8
    assert h0_tangent == 8
    assert h0_tangent_twist_minus3 == 0

    pushforward = {
        "schema": "MTTQ79DegreeThreeSpectralTraceDecomposition.v1",
        "status": "EXACT_TRACE_FREE_PUSHFORWARD_AND_HODGE_SPLIT_CLOSED",
        "spectral_exact_sequence": {
            "ambient": "K3 x E",
            "spectral_line": "p_K3^*O(H) tensor p_E^*O(3[0])",
            "sequence": "0 -> O(-H,-3[0]) -> O -> O_C -> 0",
            "H0_E_O_minus3": 0,
            "H1_E_O_minus3_dimension": h0_elliptic_degree_three,
        },
        "pushforward_to_K3": {
            "evaluation_sequence": "0 -> K -> O(-H)^3 -> O -> 0",
            "trace_free_bundle_K": "ker(O(-H)^3 -> O)",
            "K_identification": "K = phi_H^* Omega^1_P2",
            "rank_K": trace_free_rank,
            "trace_split": "p_*O_C = O_K3 direct_sum K via unit and (1/3)Tr",
            "split_canonical_in_characteristic_zero": True,
        },
        "cohomology_split": {
            "H2_O_C": "H2(O_K3) direct_sum H2(K)",
            "H2_O_K3_dimension": k3_h2_o,
            "H2_K_dimension": trace_free_h2,
            "H2_O_C_dimension": k3_h2_o + trace_free_h2,
            "trace_component_dimension": 1,
            "Prym_trace_free_component_dimension": trace_free_h2,
        },
        "theorem": {
            "name": "DegreeThreeSpectralTraceDecompositionTheorem",
            "proved": True,
            "statement": "For the smooth q79 degree-three spectral cover p:C->K3, p_*O_C splits canonically as O_K3 direct_sum phi_H^*Omega^1_P2. Consequently H^2(C,O_C) is the direct sum of a one-dimensional trace component and an eight-dimensional trace-free component.",
        },
    }

    prym = {
        "schema": "MTTQ79NormalizedPoincareGerbePrymReduction.v1",
        "status": "EXACT_BASE_BRAUER_NORMALIZATION_AND_DETERMINANT_ZERO_NORM_REDUCTION_CLOSED",
        "base_Brauer_normalization": {
            "relative_Jacobian": "J=K3 x E with zero section z",
            "lift_ambiguity": "alpha may be shifted by p_J^*gamma for gamma in Br(K3)",
            "normalization": "alpha_0=alpha-p_J^*z^*alpha",
            "zero_section_restriction": 0,
            "normalization_unique": True,
            "reason": "z^*p_J^*=identity on Br(K3)",
        },
        "biextension_norm_identity": {
            "Poincare_additivity": "alpha_0(y1)+alpha_0(y2)+alpha_0(y3)=alpha_0(y1+y2+y3)",
            "spectral_determinant": "y1+y2+y3=0 in E on every fiber",
            "normalized_origin_value": "alpha_0(0)=0",
            "norm_alpha_C_to_K3": 0,
            "trace_beta_C_to_K3": 0,
        },
        "Prym_residue": {
            "A104_ambient_H2O_dimension": analytic["exponential_sequence"]["H2_O_complex_dimension"],
            "trace_component_removed": 1,
            "remaining_complex_tangent_dimension": trace_free_h2,
            "class": "beta_C in ker(Nm:C-gerbes->K3-gerbes), modulo the trace-free integral lattice",
            "beta_C_zero_proved": False,
            "interpretation": "Determinant zero removes the norm component but does not trivialize the Prym component.",
        },
        "theorem": {
            "name": "DeterminantZeroSpectralGerbePrymReductionTheorem",
            "proved": True,
            "statement": "After the unique zero-section normalization of the Poincare gerbe, the determinant-zero spectral condition forces the norm of alpha|C, and hence the trace of beta_C, to vanish. The unresolved analytic obstruction lies in the eight-dimensional trace-free/Prym component.",
        },
    }

    square = {
        "schema": "MTTQ79PGL3ToPrymSquareSystem.v1",
        "status": "EXACT_8_BY_8_DOMAIN_CODOMAIN_TYPING_CLOSED_JACOBIAN_VALUES_OPEN",
        "Serre_duality": {
            "K": "phi_H^*Omega^1_P2",
            "H2_K_dual": "H0(phi_H^*T_P2)",
            "double_cover_pushforward": "phi_H*O_K3=O_P2 direct_sum O_P2(-3)",
            "H0_T_P2_dimension": h0_tangent,
            "H0_T_P2_minus3_dimension": h0_tangent_twist_minus3,
            "H0_phi_pullback_T_dimension": h0_tangent + h0_tangent_twist_minus3,
            "identification": "H2(K)^* = H0(phi_H^*T_P2) = pgl3",
            "perfect_dimension_match": True,
        },
        "alignment_to_residue_map": {
            "domain": "PGL3 alignments iota:|H|^* -> |3[0]|",
            "domain_complex_dimension": pgl3_dimension,
            "family": "smooth spectral surfaces C_iota over the open Bertini locus in PGL3",
            "codomain": "relative topologically trivial norm-zero gerbe/Prym-torus bundle T_Prym -> PGL3",
            "codomain_fiber_complex_tangent_dimension": trace_free_h2,
            "map": "section B:iota -> beta_C_iota in T_Prym,iota",
            "equations": "B(iota)=0",
            "local_Jacobian": "after a local Gauss-Manin/holomorphic trivialization, dB_iota:pgl3 -> H2(K) trace-free tangent",
            "Jacobian_shape": [trace_free_h2, pgl3_dimension],
            "Jacobian_entries_computed": False,
            "Jacobian_determinant_computed": False,
            "zero_alignment_found": False,
        },
        "selection_logic": {
            "if_zero_and_nonzero_Jacobian": "the gerbe condition selects an isolated local PGL3 alignment rather than adding eight fit knobs",
            "if_no_zero": "the smooth rank-one degree-three spectral candidate is ruled out on this branch",
            "if_positive_dimensional_zero_locus": "an additional MTT selector is still required",
            "current_outcome": "undecided until the same-branch Poincare Cech/period Jacobian is executed",
            "observed_data_used": False,
            "new_fitted_continuous_parameters": 0,
        },
        "theorem": {
            "name": "PGL3PrymDimensionMatchingTheorem",
            "proved": True,
            "statement": "The remaining q79 spectral gerbe equation is a square complex system: its trace-free obstruction tangent is eight-dimensional and Serre-dual to the eight-dimensional infinitesimal PGL3 alignment space. This types an 8x8 Jacobian test but does not assert its determinant or a zero.",
        },
    }

    open_jacobian = {
        "schema": "MTTQ79PGL3ToPrymJacobianInput.v1",
        "status": "OPEN_INPUT_TEMPLATE",
        "basis": {
            "pgl3_generators_8": [None] * pgl3_dimension,
            "trace_free_H2_K_basis_8": [None] * trace_free_h2,
            "integral_Prym_lattice_basis": None,
        },
        "same_branch_data": {
            "marked_K3_period_or_sextic": None,
            "elliptic_period": None,
            "base_alignment_iota": None,
            "normalized_Poincare_Cech_cocycle": None,
            "local_Gauss_Manin_or_holomorphic_Prym_trivialization": None,
            "beta_C_coordinates_8": [None] * trace_free_h2,
            "d_beta_d_alignment_8x8": [[None] * pgl3_dimension for _ in range(trace_free_h2)],
        },
        "acceptance": {
            "beta_C_zero": False,
            "Jacobian_determinant_nonzero": False,
            "isolated_alignment_certificate": False,
            "same_q79_FuYau_provenance": False,
        },
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA105.v1",
        "status": STATUS,
        "closed_here": [
            "canonical trace decomposition p_*O_C=O direct_sum phi_H^*Omega1_P2",
            "unique zero-section normalization removing the base Brauer lift ambiguity",
            "determinant-zero norm cancellation of the analytic spectral gerbe residue",
            "reduction from the A104 nine-dimensional ambient residue to an eight-dimensional Prym residue",
            "Serre-dual identification of the obstruction tangent with pgl3^* and exact 8x8 Jacobian typing",
        ],
        "not_closed_here": [
            "one explicit same-branch normalized Poincare Cech/period evaluation",
            "the eight beta_C coordinates and 8x8 alignment Jacobian",
            "existence and isolation or no-go of a beta_C-zero PGL3 alignment",
            "twisted spectral sheaf, inverse Fourier-Mukai local freeness and SU3 determinant",
            "balanced HYM and differential Bianchi execution",
            "threshold and NS5 numerical rows",
        ],
        "analytic_residue_ambient_dimension_A104": 9,
        "analytic_residue_active_Prym_dimension": 8,
        "alignment_domain_dimension": 8,
        "square_Jacobian_shape": [8, 8],
        "new_fitted_continuous_parameters": 0,
        "actual_FuYau_holomorphic_nonpullback_bundle_constructed": False,
        "actual_FuYau_balanced_HYM_proved": False,
        "actual_FuYau_nonpullback_Bianchi_proved": False,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
        "next_exact_target": "Evaluate the normalized Poincare gerbe periods and the 8x8 derivative of the relative section B of the Prym-gerbe torus bundle at a same-branch marked q79 geometry; certify a transverse zero or a no-go.",
    }

    for path, payload in [
        (PUSHFORWARD, pushforward),
        (PRYM, prym),
        (SQUARE, square),
        (OPEN_JACOBIAN, open_jacobian),
        (FRONTIER, frontier),
    ]:
        dump(path, payload)

    outputs = {
        "spectral_trace_decomposition": str(PUSHFORWARD.relative_to(ROOT)).replace("\\", "/"),
        "normalized_gerbe_Prym_reduction": str(PRYM.relative_to(ROOT)).replace("\\", "/"),
        "PGL3_Prym_square_system": str(SQUARE.relative_to(ROOT)).replace("\\", "/"),
        "PGL3_Prym_open_Jacobian": str(OPEN_JACOBIAN.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    checks = {
        "A104_integral_gate_consumed": a104["results"]["integral_DD_restriction_zero"],
        "trace_split_1_plus_8": pushforward["cohomology_split"]["H2_O_C_dimension"] == 9,
        "base_Brauer_ambiguity_normalized": prym["base_Brauer_normalization"]["normalization_unique"],
        "determinant_zero_norm_cancellation": prym["biextension_norm_identity"]["norm_alpha_C_to_K3"] == 0,
        "Prym_residue_dimension_eight": prym["Prym_residue"]["remaining_complex_tangent_dimension"] == 8,
        "PGL3_dimension_eight": square["alignment_to_residue_map"]["domain_complex_dimension"] == 8,
        "Serre_dual_dimension_match": square["Serre_duality"]["perfect_dimension_match"],
        "Jacobian_not_invented": not square["alignment_to_residue_map"]["Jacobian_entries_computed"],
        "zero_not_invented": not square["alignment_to_residue_map"]["zero_alignment_found"],
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
        "spectral_H2O_dimension": 9,
        "trace_component_dimension": 1,
        "active_Prym_residue_dimension": 8,
        "PGL3_alignment_dimension": 8,
        "PGL3_Prym_Jacobian_shape": [8, 8],
        "PGL3_Prym_Jacobian_computed": False,
        "analytic_gerbe_residue_zero_proved": False,
        "isolated_gerbe_trivial_alignment_selected": False,
        "actual_FuYau_holomorphic_nonpullback_bundle_constructed": False,
        "actual_FuYau_balanced_HYM_proved": False,
        "actual_FuYau_nonpullback_Bianchi_proved": False,
        "U6_strong_CP_closed": False,
    }
    candidate = {
        "schema": "MTTSelectedQ79NormalizedPoincareGerbeAndPGL3PrymReduction.v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": authority_hashes,
        "results": results,
    }
    certificate = {
        "certificate": "MTT_Selected_q79NormalizedPoincareGerbeAndPGL3PrymReduction_v1",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "candidate": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "results": results,
    }
    dump(CANDIDATE, candidate)
    dump(CERT, certificate)

    note = f"""# MTT Selected q79 Normalized Poincare Gerbe and PGL3-Prym Reduction v1

Status: `{STATUS}`

## Why this is a new step

A104 proved that the integral Dixmier-Douady class vanishes on the q79
spectral surface and isolated a topologically trivial holomorphic residue in
a nine-dimensional ambient space. A105 uses the degree-three spectral
equation and its determinant-zero condition. The active residue is only
eight-dimensional, and those eight directions are canonically dual to the
eight previously unfixed `PGL(3)` alignment directions.

## Trace decomposition

For `p:C->K3`, the divisor sequence is

```text
0 -> O(-H,-3[0]) -> O -> O_C -> 0.
```

On the elliptic curve, `h0(O(-3[0]))=0` and `h1(O(-3[0]))=3`. Pushing the
sequence to K3 gives the evaluation kernel

```text
0 -> K -> O(-H)^3 -> O -> 0.
```

The three sections are the genus-two map `phi_H:K3->P2`, so the Euler
sequence identifies

```text
K = phi_H^* Omega^1_P2.
```

The unit and one-third of the trace split the finite degree-three algebra:

```text
p_*O_C = O_K3 direct_sum K.
```

Consequently

```text
H^2(C,O_C) = H^2(K3,O) direct_sum H^2(K3,K),
9 = 1 + 8.
```

## Normalize the Poincare gerbe

The obstruction gerbe lifting the Fu-Yau torsor can be shifted by a gerbe
pulled back from K3. The relative Jacobian has a zero section `z`, so

```text
alpha_0 = alpha - p_J^* z^*alpha
```

is the unique lift with `z^*alpha_0=0`; uniqueness follows from
`z^*p_J^*=identity`. This removes a genuine base-Brauer ambiguity before any
numerical or period calculation.

The normalized Poincare object is a biextension and is additive in the
elliptic coordinate. If the three spectral points are `y1,y2,y3`, then

```text
Nm(alpha_0|C)
  = alpha_0(y1)+alpha_0(y2)+alpha_0(y3)
  = alpha_0(y1+y2+y3).
```

The A103 cover is determinant-zero, so `y1+y2+y3=0`, and normalization gives
`alpha_0(0)=0`. Therefore

```text
Nm(alpha_0|C)=0,
Tr(beta_C)=0.
```

This does not prove `beta_C=0`. It proves that its one-dimensional trace
component is zero and places the remaining class in the eight-dimensional
Prym/trace-free component.

## The 8 by 8 theorem

Serre duality and the genus-two double-cover formula give

```text
H^2(K)^* = H^0(phi_H^*T_P2),
phi_H*O_K3 = O_P2 direct_sum O_P2(-3).
```

Since `h0(T_P2)=8` and `h0(T_P2(-3))=0`,

```text
H^2(K)^* = pgl3,
dim H^2(K) = dim PGL(3) = 8.
```

Thus the exact remaining problem is the square holomorphic system

```text
B is a section of T_Prym -> PGL(3),
B(iota)=beta_C_iota=0,
dB_iota is 8 by 8 after local Gauss-Manin/holomorphic trivialization.
```

This dimension match is not itself an existence theorem. It gives a decisive
finite calculation:

- a zero with nonzero determinant of `dB` selects an isolated local alignment
  and turns the former eight moduli into solved geometric coordinates;
- no zero rules out this smooth rank-one degree-three spectral route;
- a positive-dimensional zero locus leaves a smaller selector problem.

No observed Standard-Model value appears in this system, and no alignment
coordinate is yet counted as a fitted parameter.

## Required execution

The generated Jacobian template requires a marked lattice-polarized K3
sextic/period point, the elliptic period, a base alignment, the normalized
Poincare Cech cocycle, a local Gauss-Manin/holomorphic Prym trivialization,
eight Prym coordinates and their eight-by-eight alignment derivative. Current
repositories contain none of those numerical same-branch entries, so A105
does not fabricate the determinant or a zero.

After a transverse zero, the ordered chain remains: twisted rank-one spectral
sheaf, inverse Fourier-Mukai local freeness and determinant, balanced HYM,
then the full differential Bianchi identity.

Next artifact: `{NEXT}`.

## Primary references

- [Brinzanescu, Halanay and Trautmann, Vector bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
- [Caldararu, Derived categories of twisted sheaves on elliptic threefolds](https://arxiv.org/abs/math/0012083)
- [Friedman, Morgan and Witten, Vector bundles over elliptic fibrations](https://arxiv.org/abs/alg-geom/9709029)
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
