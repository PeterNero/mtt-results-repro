# Selected Qa/SU3 Finite Cochain Packet or D_E Response v1

## Purpose

This gate turns the remaining selected-values problem into a two-lane
acceptance contract.

The finite cochain lane selects the section/cochain bases, product tables, and
therefore the `mu_i`, `a_i`, and `b_i` entries.

The operator-response lane selects the same packet through `D_E`, `dotD`,
projectors, and Green/Riesz response data.

The two lanes must share the same source or be connected by an explicit
change-of-basis bridge.

## Finite Cochain Lane

The selected packet must supply finite bases for:

```text
F1,F2,F3,F4,F5,G1,G2,G3,G4,G5,P
```

and product tables:

```text
m_i: F_i x G_i -> P.
```

The selected multiplication constants are then read from these product tables.
They are not assigned as free parameters.

After the bases, products, and map entries are selected, the monad condition is
checked:

```text
mu_1*a_1*b_1 + mu_2*a_2*b_2 + mu_3*a_3*b_3 + mu_4*a_4*b_4 + mu_5*a_5*b_5 = 0.
```

## Operator Response Lane

The same branch may instead, or independently, supply a finite operator packet.
The contract follows the already useful Iwasawa response validator pattern.

With Gram matrix `G`, stiffness matrix `K`, and

```text
A = G^{-1}K,
```

the selected packet must provide projectors `P,Q`, a reduced Green/Riesz
operator `R`, zero modes `psi_i`, and a selected `dotD` such that:

```text
s_i = Q dotD psi_i,
dotPsi_i = -R Q dotD psi_i,
A dotPsi_i + s_i = 0,
P dotPsi_i = 0.
```

Thus neither source vectors nor horizontal responses can be chosen as texture
knobs.

## Same-Source Bridge

The cochain and operator lanes can promote only if:

```text
source_id(cochain) = source_id(operator),
```

or if an explicit change-of-basis map proves that the product tables and
operator matrices are coordinates for the same selected object.

The bridge must also retain Freed-Witten, Green-Schwarz/Bianchi,
stability/local-freeness, and projector checks.

## Decision

This gate closes the acceptance contract, not the selected data.

The next required artifact is:

```text
Selected_Qa_SU3_Selected_Finite_Source_Solve_v1
```

No selected finite cochain packet, selected `D_E/dotD`, selected `mu_i`, or final
Qa/SU3 closure is claimed here.
