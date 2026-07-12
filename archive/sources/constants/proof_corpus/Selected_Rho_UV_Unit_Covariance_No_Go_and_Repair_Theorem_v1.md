# Selected Rho-UV Unit-Covariance No-Go and Repair Theorem v1

## Purpose

The coefficient-normalization route closed the UV response metric:

```text
G_11 = 1.
```

The remaining candidate shortcut was:

```text
||D_raw||_coeff^2 = 1.
```

This note tests whether that equality can be proved from the current corpus.

## Theorem

The current corpus does not prove

```text
||D_raw||_coeff^2 = 1.
```

Moreover, setting it to one by calling the Wiener process "standard" is only a
coordinate convention unless the selected finite-memory disturbance kernel is
also fixed.

## Proof

The white-noise/Markov-limit source writes a finite-memory covariance kernel
with integrated covariance

```text
int C_tau(t) dt = 2D
```

and obtains the white-noise limit

```text
E[xi(t) xi(t')] = 2D delta(t-t').
```

The same source explicitly separates this structural limit from the missing
carrier-specific computation. It states that the finite-memory model matters
before the white-noise limit is taken.

For the OU reduction one may write

```text
da = -gamma a dt + sqrt(delta) dW_t,
Var(a) = delta/(2 gamma).
```

Here `W_t` is standard Brownian motion, but the disturbance power is the
coefficient multiplying it. Replacing `sqrt(delta) dW_t` by `dW'_t` simply
defines a new Brownian scale. It does not determine the physical covariance in
the already selected coefficient coordinate `a`.

The coefficient coordinate cannot be freely rescaled at this stage, because the
UV response row has already been source-certified in the same coefficient basis:

```text
U_raw = (v1_tilde, 0, 0).
```

If one rescales the coefficient coordinate to absorb `delta`, the UV row
coefficient rescales too. Thus the invariant ratio

```text
rho_UV = ||U_raw||_coeff^2 / ||D_raw||_coeff^2
```

is not closed by Brownian standardization.

The fixed-point damping and physical-action-normalization gates close:

```text
lambda_* = 15,
kappa = 1,
alpha_int = 1,
G10_int = 1.
```

These fix the drift/Hessian/action units of the selected exact branch. They do
not supply the missing bath temperature, fluctuation-dissipation relation,
carrier covariance, or finite-memory kernel amplitude for the unresolved
coefficient channel.

Therefore the equality

```text
||D_raw||_coeff^2 = 1
```

is not a theorem of the current corpus.

## Minimal Repair Theorem

The exact object needed for closure is:

```text
Selected finite-memory covariance theorem:
  Let K_tau be the selected unresolved finite-memory disturbance kernel induced
  by the Z64/Strominger carrier after projection to the invariant coefficient
  quotient. Let pi_alpha1 be the selected alpha_1 coefficient functional. Then

    ||D_raw||_coeff^2 =
      int_R (pi_alpha1 K_tau pi_alpha1^*)(t) dt

  has a source-computable value.
```

If that integral evaluates to one in the already certified internal action
normalization, then the rho_UV branch closes as

```text
rho_UV(R) = [64(2pi)^2/(16 R^4 + 8)]^2.
```

If it evaluates to another positive number `d`, then the correct closure is

```text
rho_UV(R) = [64(2pi)^2/(16 R^4 + 8)]^2 / d.
```

Either outcome is acceptable. What is not acceptable is selecting `d=1` by
renaming the noise.

## Best Way Forward

The next executable calculation is not another normalization argument. It is to
construct `K_tau` from the selected Hessian/retarded kernel:

```text
H = selected positive Hessian block,
K_ret = selected retarded kernel,
P = selected unresolved-to-alpha_1 projection,
Q_tau = selected finite-memory bath covariance,
D_raw^2 = int_R P K_ret Q_tau K_ret^* P^* dt.
```

In the exact Z64 central-circle block the retarded kernel is already certified:

```text
K_ret,64 = S^-1 = S^63.
```

What remains absent is `Q_tau`, the actual unresolved bath covariance. Once that
is supplied by the MTT/Strominger carrier rather than chosen by convention, the
final ratio is computable.

## Verdict

The attempted unit-covariance shortcut fails as a no-knob proof.

The remaining blocker is now fully closed in a rigorous negative sense:

```text
No numeric rho_UV closure follows from the present corpus.
```

The positive repair is also exact:

```text
compute the projected finite-memory covariance integral from K_ret, H, and the
selected unresolved carrier covariance Q_tau.
```

This is the first place where genuinely new branch data, not algebraic
normalization, is required.
