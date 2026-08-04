# QM Context-Source Functor Frontier Report

Date: 2026-07-23

Kernel handoff: `5bcd0810-9e4a-40fd-95bb-63d5301f6dfe`

Controlling blocker: `B.QM.01`

## Authoritative Starting Point

The Research Kernel records `B.QM.01` as open. Already accepted are:

- canonical finite q79 `P_Haar/Q` kinematics;
- exact pointer dilation and one-rate dephasing shape;
- the one-anchor reference rate;
- the universal Penrose-rate no-go;
- the anchor-free context factor
  \[
  r_C=\frac{g_0\mathcal J_C}{2\log448}.
  \]

The open source is the preparation-to-profile/smearing/context map plus the
selected instrument and realized-outcome law.

## New Theorem

`Selected MTT Context-to-Profile, Smearing and Instrument Source Theorem v1`
proves that one selected variational-spectral apparatus action canonically
emits

\[
C\longmapsto
\left(
Z_C,\,
f_C,\,
\widehat\ell_C,\,
\mathcal J_C,\,
\mathrm{instrument}_C
\right)
\]

provided it supplies four typed source blocks:

1. a joint action-generated system-apparatus evolution;
2. its atomic stable record algebra;
3. branch stress tensors obtained by metric variation of the same action;
4. an external spatial finite Hodge/spectral projector and reduced Green
   operator obtained from the same action Hessian.

The construction is:

```text
G_C = D_C^* D_C
U_C = D_C G_C^(-1/2)
Z_C = U_C^*(Pi_C,+ - Pi_C,-)U_C

delta_mu_C = n^mu n^nu(T_C,+ - T_C,-)
f_C = P_C^sp[E0^-4 delta_mu_C]
ell_hat_C = Lambda_C^(-1/2)
J_C = 4*pi <f_C, Green_C f_C>

M_C,a = Pi_C,a U_C
I_C,a(rho) = M_C,a rho M_C,a^*
```

## Exactness and Parameter Result

The finite spectral expression

\[
\mathcal J_C
=4\pi
\sum_{0<\lambda_j\leq\Lambda_C}
\frac{|f_{C,j}|^2}{\lambda_j}
\]

is exact inside the selected finite external spatial object. It is not a
claim that an unprojected continuum integral has zero truncation error.

The map adds:

```text
universal continuous parameters: 0
fitted parameters:               0
observed inputs:                 0
unselected theory payloads:      1
```

Physical preparation, apparatus geometry and boundary conditions remain
context data rather than theory fits.

## Exact Witness

The executable certificate verifies:

```text
Z_C                         = diag(1,-1)
ell_hat_C                   = 1/2
J_C/(4*pi)                  = 13/25
instrument record weights  = (1/3,2/3)
```

These are rational theorem witnesses, not promoted physical profile values.

## Type Guard

`P_Haar/Q` acts on the internal finite q79 sheet carrier. It cannot be reused
as the external spatial mass-density cutoff.

The finite-projected HYM result supplies a valid exactness pattern, and the
Hodge/BV mathematical-language program supplies the right same-action
architecture. Neither currently promotes an external collapse regulator.

## Frontier Delta

Before:

```text
five separately listed choices:
Z_C, f_C, ell_hat_C, J_C, instrument_C
```

After:

```text
one closed conditional functor;
one selected physical variational-spectral apparatus-action payload remains.
```

`B.QM.01` is not closed. The remaining physical clauses are:

1. emit the selected q79 joint system-apparatus action;
2. derive its stable external record center;
3. derive its external spatial density Hessian/projector/Green operator;
4. prove the direct Penrose rate identity or a controlled correlation-kernel
   limit;
5. derive the realized-outcome law.

## Verification

```powershell
python scripts\verify.py
python -m unittest discover -s tests -v
```

Results:

```text
all exact checks: 233/233
new context-source checks: 20/20
unit tests: 21/21
source hashes: 16/16 current
```
