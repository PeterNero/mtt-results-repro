# MTT Selected Neutral Physical Unit or Nil Anchor Projector v1

## Result

The selected A29 orbit has Hermitian spectrum `[1,4,7]`. A common physical
unit or prefactor cannot change eigenvalue ratios. Nil subtraction gives
`[0,3,6]`, hence

```text
r_direct = 3/6 = 0.5.
```

The normal-ordering oscillation postcheck already stored in the neutral packet
gives `r_post = 0.029805013927576625`. It is used only as a downstream falsification
check. Therefore attaching `v_u`, `Omega0`, or any other common scale, even
together with nil subtraction, cannot make the selected internal orbit the
physical neutrino mass spectrum.

## Minimal surviving repair

One economical non-affine family is

```text
m_k^2 = C * (exp(beta*(lambda_k-lambda_min)) - 1),
r = 1/(exp(3 beta)+1).
```

For orientation only, replaying the postcheck gives `beta=1.1609401453013648` and
`C=2.3739040284360217e-06 eV^2`. These are diagnostic values, not selected source rows. The
important theorem is the parameter count: one dimensionless action slope and
one universal physical scale are algebraically sufficient, whereas one common
scale alone is impossible.

Next artifact: `MTT_Selected_NeutralSpectralActionSlopeOrSeesawSource_v1`.
