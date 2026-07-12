# Monad Difference Pic0 Source Switch Reduction

## Question

After the selected `V_alpha` source sufficiency check, the ordered `L3-K2`
subgate still names both source selection and `Pic0`.  Are these one hidden
problem, or two independent source switches?

## Two-Switch Reduction

The local q79 ordered-source validator and the constants-repo switch table agree:

```text
no source, no Pic0  -> OPEN
Pic0-only           -> OPEN
source-only         -> OPEN
both switches pass  -> PASS
```

The `Pic0-only` case removes the `Pic0` open item but still fails source
selection.  The `source-only` case removes the source open items but still fails
`Pic0`.  Therefore `Pic0` is not secretly solved by the terminal monad lane
selector, and the lane selector is not secretly solved by quotienting `Pic0`.

## Meaning

This is a two-switch reduction.  The ordered matrix is already the accepted
matrix:

```text
E(g1,g2)=2, E(g3,g4)=-4, E(g5,g6)=0.
```

The next packet must prove:

```text
Selected_Monad_Difference_L2_Source_and_Pic0_Quotient.v1
```

It must supply source selection of the terminal monad lane `L3-K2`, a selected
or physically quotiented `Pic0` rule, binding to Appell-Humbert/Cech transition
data, and promotion of the `h1=8` Ext packet as selected data.

## Guardrail

This is not a proof of either switch.  It proves only that the two switches are
independent and jointly sufficient for the ordered-source validator.  Stability,
HYM or Route-C, same-source `D_E/Riesz/Green/dotD`, primitive `C1`, and full SM
closure remain open.
