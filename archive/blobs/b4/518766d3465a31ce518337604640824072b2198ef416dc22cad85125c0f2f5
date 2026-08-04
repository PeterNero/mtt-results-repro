# Selected PhiFin S2 A_sel,N Form Bound Interface v1

## Result

Status: `A_SEL_N_FORM_BOUND_INTERFACE_BUILT_VALUES_OPEN`

The comparison interface is now explicit. The current model operator is:

```text
basis_id: F3xF3_gerbe_twisted_fourier_N1_rank3
shape: [27, 27]
zero cluster indices: [12, 13, 14]
complement gap: 4.386490844928603
eta threshold: 2.1932454224643014
```

## Accepted Payload

An accepted fill must provide either:

1. a selected `27 x 27` operator `A_sel,N` on the same `B_N` basis, with
   certified `||A_sel,N - A_model,N||_op`; or
2. a selected quadratic form bound proving
   `|<v,(A_sel,N-A_model,N)v>| <= eta_N` for all normalized `v` in `B_N`.

It passes only if:

```text
0 <= eta_N < eta_N_threshold
eta_N_threshold = 2.1932454224643014
```

## Existing Payload Classification

The small Strominger Galerkin solve is rejected because its sector dimensions
are 2 or 4, not the required 27-mode basis.

The 27-mode smooth `B_N` matrices are rejected as `A_sel,N` because their
selected-source flags remain false; they are model-active scaffold data, not
selected full-operator data.

## Next Artifact

```text
Selected_PhiFin_S2_A_sel_N_Form_Bound_Fill_Attempt_v1
```
