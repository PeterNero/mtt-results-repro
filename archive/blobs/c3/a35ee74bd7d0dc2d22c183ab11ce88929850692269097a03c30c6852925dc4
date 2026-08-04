# Selected Rho-UV Coefficient Normalization and Unit-Covariance Route v1

## Purpose

The previous response-ratio computation reduced the remaining non-SM scale
problem to

```text
rho_UV = G_11 [64(2pi)^2/(16 R^4 + 8)]^2 / ||D_raw||^2.
```

This note tests whether the two open normalization factors can be closed without
using observed constants as inputs.

## Source-Certified UV Row

The heterotic selection source gives the invariant basis

```text
alpha_1 = a wedge b,
alpha_2 = a wedge c,
alpha_3 = b wedge c,
int_X a wedge b wedge c = 1,
```

and the selected curvature source

```text
Tr_grav R_+^2 = v1_tilde alpha_1,
alpha_2 component = 0,
alpha_3 component = 0.
```

On the symmetric Iwasawa slice, in internal alpha-prime-one units,

```text
v1_tilde(R) = 64(2pi)^2/(16 R^4 + 8).
```

Therefore the selected finite response row is

```text
U_raw = (v1_tilde, 0, 0).
```

## Closing G_11 in the Coefficient Problem

There are two different norms one could ask for:

```text
1. a differential-form L2 norm, depending on the Hodge star and volume data;
2. the finite coefficient norm on the selected invariant row space.
```

The response-ratio program is formulated in the second space. It compares the
selected finite UV residual row with the selected finite disturbance row after
the heterotic/Strominger equations have already been projected to invariant
coefficients. In that projected quotient the coordinates are the selected
coefficient coordinates in the basis `(alpha_1, alpha_2, alpha_3)`.

Thus the selected coefficient Hilbert structure is

```text
||(x_1,x_2,x_3)||_coeff^2 = x_1^2 + x_2^2 + x_3^2
```

unless a later source explicitly replaces it with a Hodge-form metric. With the
current selected finite quotient,

```text
G_alpha = I_3,
G_11 = 1,
||U_raw||_coeff^2 = v1_tilde(R)^2.
```

This closes the UV row metric for the finite coefficient residual. It does not
claim that the full form-L2 norm of `alpha_1` is one; that would be a different
quantity and would need the Hodge normalization.

## Remaining Disturbance Normalization

The OU/white-noise corpus supplies the shape of the stochastic mode:

```text
Var(a) = delta/(2 gamma),
delta = integrated covariance of the finite-memory disturbance in the
         white-noise limit.
```

But it does not yet source-certify which finite-memory covariance row is selected
by the Z64/Strominger carrier after projection to the same coefficient quotient.
Therefore the strict result is now

```text
rho_UV(R) =
  [64(2pi)^2/(16 R^4 + 8)]^2 / ||D_raw||_coeff^2.
```

The old blocker has been reduced from two independent normalizations to one:

```text
remaining gate = ||D_raw||_coeff^2.
```

## Candidate Unit-Covariance Closure

There is a plausible no-knob theorem that would close the last factor:

```text
Canonical one-channel covariance theorem:
  In a one-dimensional selected unresolved coefficient channel, after the
  invariant quotient and action normalization are fixed, the maximum-entropy
  finite-memory white-noise limit is the standard unit Wiener input.
```

If this theorem is proved from the selected Hessian/retarded-kernel construction,
then

```text
||D_raw||_coeff^2 = 1,
rho_UV(R) = [64(2pi)^2/(16 R^4 + 8)]^2,
s_* = (60 rho_UV)^(1/6).
```

The theorem cannot be assumed merely because the channel is one-dimensional. It
must identify the actual selected finite-memory kernel, push it through the same
coefficient projection as the UV row, and show that its integrated covariance is
the unit quadratic form in the selected action units.

## Conditional Diagnostic Values

If the candidate unit-covariance theorem is later proved, the conditional values
are:

| R | r3 | v1_tilde | rho_UV | s_* |
|---:|---:|---:|---:|---:|
| 1 | 3.627598728468436 | 105.275780278286 | 11082.9899132021 | 9.34260594395577 |
| 2 | 4.375048680836414 | 9.57052547984423 | 91.5949579603476 | 4.20084963151094 |
| 5 | 4.441106850564644 | 0.252459904744092 | 0.0637360035033962 | 1.25051626958438 |

These remain conditional diagnostics until the unit-covariance theorem is
proved.

## Verdict

The selected finite coefficient normalization closes

```text
G_11 = 1
```

for the projected response-ratio problem.

The remaining open mathematical blocker is sharply isolated:

```text
prove ||D_raw||_coeff^2 = 1
```

or compute its different selected value from the actual retarded overlap kernel.
If the canonical unit-covariance theorem is proved, the rho_UV branch closes
without benchmark constants.
