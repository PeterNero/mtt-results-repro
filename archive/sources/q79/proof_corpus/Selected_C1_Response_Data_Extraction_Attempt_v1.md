# Selected C1 Response Data Extraction Attempt

## Purpose

This note attempts the next concrete step toward the selected full SM-data
theorem: compute the selected C1 response matrix induced by the Iwasawa
`alpha_1` curvature driver.

The desired object is:

```text
SelectedC1ResponseDataCertificate
```

It should supply the matrices:

```text
M_u,C1^(alpha1),
M_d,C1^(alpha1),
M_e,C1^(alpha1),
M_nuD,C1^(alpha1),
```

then evaluate:

```text
C33(M_s) = M_s11*M_s22 - M_s12*M_s21
Delta_v = (M_d13-M_u13, M_d23-M_u23).
```

## What We Can Compute Now

The selected Iwasawa `R_+` curvature support is already closed:

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
v1_tilde = 8 r3^2/(r1^2 r2^2),
alpha_2 component = 0,
alpha_3 component = 0.
```

Thus C1 has only one invariant curvature driver row on this branch.  This is a
real computation.  It prevents C1 from being treated as three independent
curvature knobs.

## Response Chain Needed

To turn the closed driver row into actual matrix entries, the following chain
must be evaluated:

```text
alpha_1
-> grad V_C1
-> Hess_Xi^{-1}
-> deltaTheta_C1
-> dotD_Q, dotD_u, dotD_d, dotD_L, dotD_e, dotD_N, dotD_H
-> dotP_a by the Riesz/resolvent formula
-> corrected zero-mode representatives
-> raw overlap derivatives
-> M_s,C1^(alpha1).
```

The already formulated equations are:

```text
Hess_Xi(Theta0) deltaTheta_C1
  = - Pi_coh grad V_C1(Theta0),
```

and:

```text
dotP_a
  = -(1/(2*pi*i)) Integral_Gamma_a
      (D_a-z)^(-1) dotD_a (D_a-z)^(-1) dz.
```

The matrix entries are:

```text
M_s,ij
  = d/depsilon Y_s_raw(
        Psi_L,i(epsilon),
        Psi_R,j(epsilon),
        H_s(epsilon),
        Theta(epsilon))
    at epsilon=0.
```

## Attempt Result

The current corpus does not supply:

```text
selected V_C1 functional,
explicit Hess_Xi blocks,
selected deltaTheta_C1 solution,
dotD operators for the matter and Higgs zero-mode operators,
selected family zero-mode bases,
selected L2 Gram-Schmidt rule,
evaluated zero-mode response integrals,
sector response matrices.
```

Therefore the C1 response matrix cannot yet be computed.

The exact status is:

```text
C1_RESPONSE_EXTRACTION_BLOCKED_MISSING_SELECTED_OPERATOR_DATA.
```

## Partial Fill Achieved

The corpus does provide the operator-level `Xi` data behind the C1 source.
The selected Strominger/heterotic flux paper defines:

```text
Xi =
  int e^{-2Phi}(R + 4|grad Phi|^2 - 1/2|Hhat|^2)
  + (1/(2g10^2)) int e^{-2Phi} Tr(F_A wedge *F_A)
  + int K wedge (dHhat - alpha'/4(Tr F_A wedge F_A - Tr R+ wedge R+))
  + int Lambda wedge (Hhat - dB + alpha'/4(omega3(A)-omega3(omega+)))
  + OU.
```

Therefore the C1 curvature part of the selected functional includes:

```text
+ alpha'/4 int K wedge Tr(R+ wedge R+)
- alpha'/4 int Lambda wedge omega3(omega+).
```

Combined with the closed Iwasawa support:

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
```

this identifies the operator-level C1 source.  The same paper also gives the
Hessian principal blocks:

```text
metric/dilaton:  Delta^(Hhat) on symmetric 2-tensors and scalars,
B-field:         Delta^(Hhat) on 2-forms,
bundle:          Yang-Mills Laplacian Delta_A on u(E)-valued 1-forms,
residual moduli: positive OU weights gamma_{n,k}^{-1}.
```

This is progress: `V_C1` is no longer a nameless symbol at operator level.
However, it is not enough to compute `M_C1`.  We still need the selected source
vector `grad V_C1`, the lower-order Hessian terms and inverse on the selected
slice, the induced `dotD` operators, and the sector-resolved zero-mode bases.

## Underdetermination Witness

The closed `alpha_1` driver row alone does not determine whether C1 succeeds.
For example, both of the following response maps share the same closed driver
support:

```text
zero response:
  light block [[0,0],[0,0]]
  C33 = 0
  rank-lift fails

nonzero response:
  light block [[1,0],[0,1]]
  C33 = 1
  rank-lift passes
```

The current certificates do not select between these possibilities because the
response operator chain is not yet supplied.  Thus it would be invalid to infer
nonzero light-family masses directly from `alpha_1` support.

## First Pass/Fail Tests Once Data Exist

When the selected response matrices are supplied, the first tests are:

```text
up rank:
  C33(M_u) != 0

down rank:
  C33(M_d) != 0

charged-lepton rank:
  C33(M_e) != 0

CKM leading noncommutation:
  Delta_v = (M_d13-M_u13, M_d23-M_u23) != (0,0).
```

If these pass, C1 becomes the first actual no-proxy rank-lift and CKM-source
candidate.  If they fail, C1 alone does not close the light-family or CKM
problem, and the program must use C2/C4/C7 or a repaired C3 source.

## Forbidden Shortcuts

The following moves are not allowed:

```text
choosing M_C1 entries from Execution II benchmark matrices,
choosing M_C1 entries to fit observed light-family masses,
choosing heavy-link entries to fit CKM angles,
treating alpha_1-only support as a proof of nonzero matrix entries,
promoting pure kinetic metric changes to raw C1 Yukawa entries.
```

## Next Artifact

The next file to fill is:

```text
certificates/selected_c1_response_data_certificate.template.json
```

That certificate is the exact door into actual no-proxy matrix computation.
