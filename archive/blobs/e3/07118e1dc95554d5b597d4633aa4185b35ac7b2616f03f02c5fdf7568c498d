# Global TT Hessian and Action Uniqueness Reduction v1

Date: 2026-07-15

## 1. Global Hessian form

The new helicity bundle removes the old patching ambiguity.  A symmetric
fiber Hessian on the real weight-two representation has coordinates

```text
H = [[a,b],[b,c]].
```

Invariance under a spatial `pi/4` rotation, which acts on helicity two by the
quarter-turn matrix `J`, gives

```text
a=c,
b=0.
```

The exact constraint matrix has rank two, so the symmetric equivariant
commutant is one-dimensional.  Consequently the local plus/cross result
patches globally as

```text
H_e = kappa_e Id_E
```

on `E_TT`.  If the selected fixed point is nondegenerate and stable in this
sector, `kappa_e>0`.  This proves the global form, not the MTT source of that
stability hypothesis or a numerical value.

## 2. Exact coordinate correction

The displayed metric source is

```text
e = (1/2) log G,
G = exp(2e),
h = delta G = 2e
```

at the identity background.  Hessians transform contragrediently, hence

```text
H_h = (1/2 I)^T H_e (1/2 I)
    = (kappa_e/4) Id_E.
```

Define `kappa_h=kappa_e/4`.  In the repository's Einstein-Hilbert metric
normalization,

```text
kappa_h = (32 pi G_eff)^(-1),
kappa_e = (8 pi G_eff)^(-1).
```

The older `kappa_STF` notation was overloaded: it denoted both the closure
strain coefficient and the metric-coordinate Einstein-Hilbert coefficient.
The new notation resolves that factor-of-four ambiguity.  Existing numerical
rows remain metric-coordinate rows if they use the `1/(32 pi G_eff)` formula.

## 3. The action is no longer an arbitrary matrix problem

For a symmetric metric perturbation, write the most general local,
parity-even, Lorentz-covariant, formally self-adjoint two-derivative operator
with coefficients `(A,B,C,D,E)`.  The off-shell linearized Bianchi identity and
self-adjointness give a rank-four exact system.  Its nullspace is one
dimensional and is spanned by

```text
(A,B,C,D,E) = (1,-1,1,1,-1).
```

This is the Fierz-Pauli/linearized-Einstein operator.  On TT fields it reduces
to `Box` in flat space and to the corresponding Lichnerowicz block on an
Einstein background.  The same gauge identity excludes every algebraic mass
term.  On a selected globally hyperbolic, time-oriented Lorentzian background,
the resulting normally hyperbolic operator has unique retarded and advanced
Green operators.

These are conditional uniqueness statements.  They reduce the remaining
source theorem to four explicit action hypotheses: locality, the two-derivative
infrared order, self-adjointness, and linearized diffeomorphism invariance.
They do not derive those hypotheses from MTT.

## 4. Honest frontier

The old claim that the projection into TT is missing is superseded: the global
`DG` and TT projector now provide it.  The remaining hard object is also not an
unknown `2 x 2` Hessian.  It is the same-source action theorem proving that MTT
selects:

1. the displayed `G=Q^TQ` observable;
2. the four action hypotheses above;
3. the coefficient `kappa_h` and the matter stress normalization; and
4. the Lorentzian time orientation/background domain used by the retarded
   solution.

The revised proto-spinor action cannot close that gate by itself: it correctly
states that it is an ansatz and that it imports the Einstein-Hilbert term.
