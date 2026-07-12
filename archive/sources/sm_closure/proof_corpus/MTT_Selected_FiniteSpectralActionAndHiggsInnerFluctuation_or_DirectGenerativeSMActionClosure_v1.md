# MTT Selected Finite Spectral Action and Higgs Inner Fluctuation or Direct Generative SM Action Closure v1

## Executed One-Form Space

The finite one-forms were computed directly from the A50 triple:

```text
Omega_D^1(A_F) = span rho(a)[D_F,rho(b)],
A = A*,
A_real = A + J_F A J_F^-1.
```

All `26x26=676` real-algebra basis pairs were executed. The unrestricted real fluctuation space has
rank `12`, not `4`. It splits into three rank-four scalar modules:

```text
H_up,   H_down/charged-lepton,   H_neutrino.
```

Thus the unrestricted four-summand A50 triple is a three-Higgs-doublet extension. Calling its raw
inner fluctuation the one-Higgs Standard Model would be incorrect.

## Selected Single-Higgs Projection

The earlier q79/ProtoSpinor alignment certificate selects

```text
H_up = H_neutrino = H,
H_down = H_charged-lepton = -epsilon conjugate(H).
```

This rule has now been executed on the actual A50 one-form space. Its image has real rank `4`, lies
inside the rank-12 fluctuation space with residual `6.152e-15`, and its canonical
`12x12` projector is exactly self-adjoint and idempotent. The kernel has dimension `8`; precisely the
two unwanted doublets are removed. The surviving field is one complex `SU(2)` doublet with
`Y=+1/2`, with pseudoreality supplying its conjugate channels.

## Finite Spectral Traces

The three-family fermion representation gives

```text
k_Y:k_2:k_3 = 10:6:6.
```

After the standard `5/3` hypercharge normalization this is `(6,6,6)`, equivalently
`g3^2=g2^2=(5/3)gY^2` at the spectral normalization scale.

The accepted profile `D_F` gives

```text
a = Tr(Ydagger Y)                    = 3.15667873398489,
b = Tr((Ydagger Y)^2)                = 3.31696406124945,
b/a^2                                = 0.332874093710992.
```

Color multiplicity is included. These are finite profile traces at `M_Z`, not high-scale predictions.

## What Is Closed

Using the standard Chamseddine--Connes product-triple heat-kernel theorem, the selected finite data
generate the operator content of the bosonic SM action: Yang--Mills terms, one Higgs covariant kinetic
term and potential, plus the standard gravitational and nonminimal terms. The finite representation,
single-Higgs module, gauge trace ratios and Yukawa trace invariants are executable rather than assumed.

Absolute spectral-action normalization is not closed here. It still requires the selected four-dimensional
base Dirac geometry, cutoff scale/function or moments `f0,f2,f4`, canonical field normalization and RG
transport from the spectral scale. The corpus paper claiming those moments are fixed by the MTT gap is
therefore still conditional, not yet an executed theorem.

Next artifact: `MTT_Selected_SpectralCutoffMomentsAndSpacetimeProductTriple_or_BosonicActionNormalization_v1`.
