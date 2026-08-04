# Selected PhiFin S2 Full Operator Error Bound or Source Theorem v1

## Result

Status: `CONDITIONAL_OPERATOR_BRIDGE_PROVED_NUMERIC_ETA_SOURCE_OPEN`

This theorem gate closes the abstract perturbation step, but not the selected
full-operator theorem itself.

The current 27-mode model has a positive complement gap. Therefore a selected
full operator compressed to the same `B_N` basis may be promoted if the missing
operator error bound is small enough.

```text
gamma_model = 4.386490844928603
epsilon_model = 0.0
strict half-gap budget = 2.1932454224643014
strict eta budget after epsilon = 2.1932454224643014
```

## Conditional Theorem

If

```text
eta_N + epsilon_N < gamma_model / 2
```

where `eta_N = ||A_sel,N - A_model,N||_op`, then the selected Riesz contour is
stable, the selected complement gap is bounded below by

```text
gamma_selected >= gamma_model - 2*(eta_N + epsilon_N)
```

and the selected reduced Green operator exists.

## What This Changes

The remaining obstruction is now one of two sharply typed payloads:

1. source theorem route: derive I3/I4/I5 and emit theorem-derived selected
   source flags;
2. operator-bound route: emit an `eta_N` bound satisfying
   `eta_N + epsilon_N < gamma_model / 2`.

The current strict budget is:

```text
eta_N < 2.1932454224643014
```

No such `eta_N` has been emitted yet, so selected value emission and honest
replay remain open.

## Next Artifact

```text
Selected_PhiFin_S2_Eta_N_Bound_or_Source_Flag_Emission_v1
```
