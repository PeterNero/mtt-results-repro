# Selected Qa/SU3 Selected Multiplication Constants or D_E Source Gate v1

## Purpose

The previous scaffold reduced the monad condition to the finite equation

```text
mu_1*a_1*b_1 + mu_2*a_2*b_2 + mu_3*a_3*b_3 + mu_4*a_4*b_4 + mu_5*a_5*b_5 = 0.
```

This note records the next gate: the equation alone is not a proof source for
selected Qa/SU3 data. It is only an acceptance equation after the basis,
product constants, and map entries have been selected by the same MTT branch.

## Formal Underdetermination

The scaffold contains:

- five `f` entries: `a_1,...,a_5`;
- five `g` entries: `b_1,...,b_5`;
- five multiplication constants: `mu_1,...,mu_5`;
- one scalar equation: `g*f=0`.

So the formal problem has 15 symbols and one equation. On any nondegenerate
stratum this leaves a 14-dimensional formal solution family. Therefore an
arbitrary solve of `g*f=0` is underdetermined and cannot be treated as selected
MTT data.

## Route Verdicts

`pure_convenience_solve_gf_zero` is rejected. It can satisfy the equation, but
it does not select bases, `mu_i`, `f,g`, or an operator source.

`appell_humbert_or_base_pullback_cech_formula` remains useful as a guardrail. It
can supply algebraic Cech/product formulas, but a formula family is not yet the
selected finite Qa/SU3 packet.

`finite_cech_dolbeault_cochain_packet` is the primary matrix construction
target. It would provide selected bases and product tables, hence the actual
`mu_i`.

`same_source_DE_dotD_response` is the primary operator promotion route. It would
provide the same-source `D_E`, `dotD`, `rho_E`, Riesz, Green, heat, zeta, or
torsion finite-part exit required by the A01/D_E gate.

`fixed_gerbe_Bfield_representative` remains an alternate period-selector route,
but only with same-branch Deligne/B-field data and Freed-Witten/Green-Schwarz
Bianchi checks.

## Decision

The selected-values problem is now reduced to either:

```text
selected finite Cech/Dolbeault cochain packet
```

or:

```text
same-source D_E/dotD response
```

The next required artifact is
`Selected_Qa_SU3_Finite_Cochain_Packet_or_DE_Response_v1`.

No selected `mu_i`, selected `f,g` entries, or selected operator matrix is
claimed in this note.
