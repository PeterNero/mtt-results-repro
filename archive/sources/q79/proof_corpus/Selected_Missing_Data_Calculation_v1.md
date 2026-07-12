# Selected Missing Data Calculation

## Purpose

The current proof-repro stack has validators through:

```text
D_E action,
Riesz projector and gap,
reduced Green operator,
dotD_alpha1 horizontal response.
```

The user request is now to calculate what is missing. The calculation is not a
new physics assumption. It is a repository scan that asks:

```text
which selected finite data are actually present,
which values are still null,
and which missing atom blocks the computation first?
```

The executable calculator is:

```text
scripts/calculate_missing_selected_data.py
```

## Result

The first blocking layer is:

```text
selected_operator_source.
```

The current corpus has not supplied a computable selected `D_E`.

The three admissible routes remain:

```text
R1 corrected selected non-invariant Dolbeault operator: BLOCKED,
R2 typed monad/Cech sections: BLOCKED,
R3 direct selected HYM/Strominger solve: ABSTRACT EXISTENCE ONLY.
```

Therefore no honest selected finite spectral matrix can yet be diagonalized.

## Slot Data Scan

The calculator searches the certificates for filled selected data keys:

```text
operator_slots,
spectral_slots,
green_slots,
dotd_response_slots.
```

Only validator certificates define those names as schemas. No non-validator certificate currently contains filled selected slot data.

So the missing validator layers are:

```text
operator_slots for Q,u,d,L,e,N,H,
spectral_slots for Q,u,d,L,e,N,H,
green_slots for Q,u,d,L,e,N,H,
dotd_response_slots for Q,u,d,L,e,N,H.
```

## Primitive C1 Missing Count

The selected C1 primitive template has four sectors:

```text
u, d, e, nuD.
```

Each sector needs six primitive 3x3 matrices:

```text
theta_overlap_variation,
left_zero_mode_response,
right_zero_mode_response,
higgs_zero_mode_response,
explicit_vertex,
basis_connection.
```

Thus the current missing primitive matrix count is:

```text
4 sectors x 6 terms = 24 selected 3x3 matrices.
```

The existing C1 calculator refuses the template until those 24 matrices are
filled from selected data.

## Minimal New Data To Compute C1

To compute the selected C1 matrices, the next data must be supplied in this
order:

```text
1. one selected D_E source;
2. finite basis B_N and Gram/stiffness matrices for Q,u,d,L,e,N,H;
3. validated Riesz projectors and complement gaps;
4. validated reduced Green operators;
5. selected dotD_alpha1 matrices and horizontal responses;
6. the 24 selected primitive 3x3 C1 contraction matrices.
```

After that, `scripts/compute_c1_response_matrices.py` can compute:

```text
M_u,C1,
M_d,C1,
M_e,C1,
M_nuD,C1,
C33(M_s),
Delta_v_ud.
```

## Guardrail

The diagnostic h1=3 candidate, rank-one E33 seed, Execution II matrices, and
observed masses/mixings are not allowed to fill these missing slots. They are
respectively a pipeline test, a tree seed, benchmark/comparison data, and
experimental targets.

## Verdict

What is missing has now been calculated. The selected numerical values
themselves are not calculable from the current corpus because the first
required object, a computable selected `D_E`, is absent.
