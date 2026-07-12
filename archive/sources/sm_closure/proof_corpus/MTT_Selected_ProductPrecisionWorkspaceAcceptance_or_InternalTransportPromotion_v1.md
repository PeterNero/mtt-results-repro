# MTT Selected Product Precision Workspace Acceptance or Internal Transport Promotion v1

## Result

The provisional direct-product independence rule is retired. It is incompatible
with the repo's already executed common-source RG Jacobian, which gives six
nonzero BCT-to-`lambda_Mt`/`y_t_Mt` covariance entries.

On the locked eight-coordinate basis, use the first-order transport identity

```text
C_out = J C_source J^T.
```

The admitted BCT covariance block, selected WZH sensitivity block, and executed
one-loop `M_Z -> M_t` response determine all `3 x 5 = 15` cross entries:

```text
executed nonzero common-source entries : 6
structural one-loop zero entries        : 9
missing entries                         : 0
```

The nine zeros are scoped statements, not independence assumptions. At one loop,
the SM gauge beta rows do not depend on the Yukawa/mass coordinates, so the BCT
response into `g_2_Mt`, `g_Y_Mt`, and `g_3_Mt` vanishes in this transport basis.
The six nonzero entries are inherited exactly from the existing finite-difference
RG Jacobian execution.

The assembled `8x8` matrix is symmetric and positive definite. It is therefore
accepted as the internal common-source first-pass precision workspace.

## Scope Boundary

This proves a reproducible first-order covariance transport object. It does not
promote the one-loop replay to multi-loop precision, turn the WZH surrogate into
a published likelihood, derive the empirical source covariance from MTT, or
close final true-SM precision equivalence. Accepted final true-equivalence
precision rows remain `0`.

The next artifact is
`MTT_Selected_MultiLoopCommonSourcePrecisionTransport_or_OfficialJointLikelihood_v1`.
