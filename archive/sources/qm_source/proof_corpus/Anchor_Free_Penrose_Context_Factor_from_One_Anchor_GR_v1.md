# Anchor-Free Penrose Context Factor from One-Anchor GR

## Theorem

Work in natural units and write the one-anchor GR result as

```text
G_eff=g0/E0^2,
g0=0.29759362932431804.
```

For a physical branch context `C`, introduce dimensionless coordinates,
density and smearing data

```text
xi=E0*x,
delta_mu(x)=E0^4 f_C(xi),
ell_hat=E0*ell.
```

Define the dimensionless regulated Newton functional

```text
J_C=integral f_C,ell(xi) f_C,ell(eta)
            /|xi-eta| d^3xi d^3eta.
```

Then the Penrose energy and its ratio to the q79 reference clock are

```text
E_C^(G,ell)=(g0/2)E0 J_C,
gamma0=log(448)E0/hbar,
gamma_C=E_C^(G,ell)/hbar,
r_C=gamma_C/gamma0=g0 J_C/(2 log(448)).
```

Thus both the absolute anchor `E0` and `hbar` cancel from `r_C`.

## Proof

The two density factors contribute `E0^8`, the two volume elements contribute
`E0^-6`, and the Newton kernel contributes `E0`. Their product scales as
`E0^3`. Multiplication by `G_eff=g0/E0^2` therefore gives an energy proportional
to `E0`. Dividing by the reference energy `log(448)E0` gives the displayed
anchor-independent ratio.

## Meaning

The one metrological primitive is required to express absolute rates in
seconds, but not to compute their ratio to the selected q79 coherence clock.
Once MTT selects the smearing rule and branch-to-profile map, each prepared
context supplies a dimensionless `J_C` and therefore an unambiguous `r_C`.

This is not a universal numerical collapse prediction. Masses, shapes and
separations are preparation data, and different contexts correctly produce
different rates.
