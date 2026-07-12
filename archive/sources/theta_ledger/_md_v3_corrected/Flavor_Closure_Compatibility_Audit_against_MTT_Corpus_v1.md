# Flavor Closure Compatibility Audit against the MTT Corpus

## Purpose

This note checks the current no-proxy flavor-closure program against the broader Modal Triplet Theory corpus. The goal is to identify whether the present flavor papers assume anything that violates the established MTT setup, and to specify the correct next step.

## Corpus Constraints That Must Be Respected

The corpus imposes four relevant constraints.

First, flavor data are a known open execution-level problem. The core roadmap states that continuous parameters such as Yukawa couplings and mixing angles still require numerical evaluation of overlap integrals and renormalization-group flow inside admissible regions. Therefore no flavor paper may claim that CKM, PMNS, CP phases, or absolute masses have been derived unless the internal overlap problem has actually been solved.

Second, proxy knobs are forbidden. The superset paper explicitly identifies Wilson-line phases and localization/separation data as the flavor bottleneck, and forbids entry-local Yukawa rescalings and entry-local phase adjustments as fundamental degrees of freedom. These quantities may appear only as diagnostics or benchmarks until they are selected by global geometry, spectral extremality, or inter-sector rigidity.

Third, topology-only admissibility applies before dynamics. Hypercharge, anomaly cancellation, determinant-line triviality, overlap-bundle global sections, and the Majorana real-structure condition are prior filters. In particular, a Majorana mass or seesaw sector is admissible only if the relevant overlap bundle admits a global real or pseudo-real structure compatible with the coherent projector.

Fourth, the proto-spinor and closure-strain papers already give a qualitative flavor theorem: PMNS is generically larger than CKM because the sector-induced closure metric is soft for neutrino-like co-aligned loops and stiff for quark composites. Numerical values, however, are explicitly deferred to realization-level curvature and overlap data.

## Compatibility Verdict

The current flavor-closure work is compatible with the corpus if interpreted as a constrained execution program, not as a completed derivation.

The no-proxy paper is compatible. Its main theorem is exactly the corpus rule: if Yukawa entries, phases, or localization separations can be changed while the underlying bottleneck data are unchanged, predictive closure fails.

The complex-holonomy and finite-character benchmarks are compatible only as target models. They obey the phase-sum idea and show that a finite character can reproduce the observed size of CP violation, but the order `N = 448` is not yet derived from a torsion subgroup, line-bundle quotient, orbifold group, or selected flat-connection moduli space. It must not be presented as forced.

The localization-distance papers are compatible only as local overlap diagnostics. Gaussian distances are acceptable as a heat-kernel or local wavefunction approximation, but not as a global assumption. The correct global object is an overlap integral of selected zero modes, generally of the form

```text
Y_abc = sum_gamma A_gamma exp(-S_gamma) chi_gamma
```

where the allowed channels `gamma`, actions `S_gamma`, amplitudes `A_gamma`, and characters `chi_gamma` are determined by the selected internal geometry and bundle data.

The PMNS triangle obstruction is not a contradiction. It is evidence that the simplest one-width, one-channel Euclidean pairwise localization model is too rigid for the lepton sector. This agrees with the proto-spinor claim that the neutrino sector uses a softer induced metric and residual nil-phase drift. The next model should not force PMNS to be a direct triangle of pairwise separations.

The seesaw benchmark is admissible only conditionally. A diagonal or degenerate `M_R` may be useful for reproducibility, but it becomes an MTT claim only after the global real-structure condition and the right-handed neutral overlap bundle are exhibited.

## What Must Be Reframed

The phrase "prediction" should be reserved for quantities computed from selected bottleneck data. At the current stage:

- CKM and PMNS matrices are benchmark targets, not derived matrices.
- `Z_448` is a candidate finite holonomy quotient, not a selected quotient.
- Gaussian localization distances are inverse targets for the overlap problem, not fundamental separations.
- The real Yukawa matrices in the reproducibility benchmark are witnesses that the numerical target is reachable, not MTT-derived textures.
- CP phases are finite-character targets until the character group is derived from topology or the selected flat-connection moduli problem.
- Majorana/seesaw claims must be stated as conditional on the topology-only real-structure admissibility test.

## Correct Way Forward

The next step should be a minimal no-proxy flavor closure model with three layers.

### Layer 1: Topological Admissibility

Construct the flavor overlap bundles and determine:

- the allowed pairwise line bundles or difference bundles;
- the flat holonomy character group;
- the determinant/phase-sum constraint;
- whether the neutral sector admits the real or pseudo-real structure needed for Majorana masses;
- whether the right-handed neutrino sector is a legitimate neutral overlap sector rather than an imported field.

This layer decides which flavor operators are allowed at all.

### Layer 2: Selected Overlap Kernel

Replace direct entry-wise Yukawa matrices by a selected overlap formula:

```text
Y_abc(Theta) = sum_{gamma in Gamma_abc(Theta)}
    A_gamma(Theta) exp(-S_gamma(Theta)) chi_gamma(Theta).
```

The formula should reduce to the Gaussian-distance targets only in a controlled local limit. This keeps the useful numerical diagnostics while removing the hidden proxy assumption.

### Layer 3: Sector Stiffness and Seesaw Geometry

Use different induced metrics for quark, charged-lepton, and neutrino sectors:

```text
D_q >> D_l >> D_nu.
```

The quark sector may be modeled first by direct localization, because the CKM triangle already passes the simplest consistency test. The lepton sector should be modeled through charged-lepton stiffness plus a neutrino Majorana/seesaw overlap kernel. PMNS should then emerge from diagonalizing the charged-lepton and neutrino effective matrices, not from forcing all PMNS angles to be direct pairwise distances.

## Immediate Technical Program

The next concrete paper should be:

```text
Holonomy_Quotient_and_Majorana_Admissibility_for_No_Proxy_Flavor_Closure_in_MTT_v1.md
```

It should prove or fail the following items:

1. Identify the candidate finite holonomy group from the internal geometry, not from CKM fitting.
2. Determine whether `Z_448`, a divisor/multiple of it, or a different finite quotient is actually selected.
3. Check the phase-sum condition inside that quotient.
4. Check the topology-only Majorana admissibility condition for the neutral sector.
5. Define the allowed overlap channels for quark, charged-lepton, and neutrino sectors.
6. State the exact pass/fail criterion: if the selected quotient and overlap channels cannot produce the observed hierarchy without entry-local adjustments, no-proxy flavor closure fails at this corner.

## Bottom Line

No fatal contradiction was found. The current work is pointing in the right direction, but it must stay honest about its status. The correct path is not to tune a better Yukawa matrix; it is to derive the finite character group, admissible neutral-sector real structure, and overlap kernel from the same selected internal data that already constrain gauge and gravity.

