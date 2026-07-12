# VAlpha Appell-Humbert Yoneda Promotion v1

## Purpose

The reduced Kunneth proof gives explicit Yoneda boundary maps for the six
central-neutral destabilizer candidates.  This note checks whether those maps
are the actual multiplication law for the already-constructed Appell-Humbert
automorphy representative.

## Multiplication Law

For the neutral standard Gaussian Appell-Humbert representative,

```text
a_d(gamma,z)=prod_j exp(-pi*i*d_j*n_j^2*i - 2*pi*i*d_j*n_j*z_j).
```

The exponent is linear in the degree vector `d`.  Therefore:

```text
a_d(gamma,z) * a_e(gamma,z) = a_{d+e}(gamma,z).
```

For the V_alpha extension class, `e=L^2=(2,-4,0)`.  For each candidate line
`M`, the Hom section has degree `D=Q-M`, and the boundary target has degree
`L-M`.  The identity to check is:

```text
(Q-M) + L^2 = L-M.
```

## Candidate Table

| M | Q-M | product | L-M | identity | reduced boundary status |
|---|---|---|---|---:|---|
| `(-4, 2, 0)` | `(3, 0, 0)` | `(5, -4, 0)` | `(5, -4, 0)` | `True` | `EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY` |
| `(-3, 2, 0)` | `(2, 0, 0)` | `(4, -4, 0)` | `(4, -4, 0)` | `True` | `EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY` |
| `(-2, 1, 0)` | `(1, 1, 0)` | `(3, -3, 0)` | `(3, -3, 0)` | `True` | `EXCLUDED_BY_PROVED_REDUCED_KUNNETH_YONEDA_SCALAR` |
| `(-2, 2, 0)` | `(1, 0, 0)` | `(3, -4, 0)` | `(3, -4, 0)` | `True` | `EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY` |
| `(-1, 1, 0)` | `(0, 1, 0)` | `(2, -3, 0)` | `(2, -3, 0)` | `True` | `EXCLUDED_BY_INJECTIVE_REDUCED_KUNNETH_BOUNDARY` |
| `(-1, 2, 0)` | `(0, 0, 0)` | `(2, -4, 0)` | `(2, -4, 0)` | `True` | `EXCLUDED_BY_NON_SPLIT_EXTENSION_BOUNDARY` |

Every row satisfies the degree identity, keeps the shared/central circle at
degree zero, and inherits an injective reduced boundary matrix.  Thus the
reduced Kunneth boundary maps are exactly the Appell-Humbert theta
multiplication maps for this neutral representative.

## What This Does Not Prove

This is a promotion to Appell-Humbert automorphy multiplication, not a final selection theorem.
The current Appell-Humbert representative remains
selection-open: MTT still has to select the ordered base, the target branch
over the swapped branch, and the neutral Pic0 character or a Pic0 quotient
rule.  If the final paper insists on literal finite good-cover transition
tables, that cover refinement is also still unsupplied.

No full V_alpha stability, HYM existence, or full SM closure is claimed here.
