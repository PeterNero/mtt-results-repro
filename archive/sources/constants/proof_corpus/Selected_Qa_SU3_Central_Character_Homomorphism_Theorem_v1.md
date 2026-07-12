# Selected Qa/SU3 Central Character Homomorphism Theorem v1

## Purpose

This tests whether the selected `q64=15` phase can be used as an ordinary
Qa/SU3 compact-Nil local-system character.

## Theorem

For the ordinary compact Heisenberg/Nil lattice presentation

```text
Gamma_Nil = <x,y,z | z central, [x,y] = z>,
```

no rank-one `U(1)` local-system character can send the central generator to

```text
exp(2*pi*i*15/64).
```

Reason:

```text
rho([x,y]) = 1
```

for every abelian `U(1)` character `rho`.  Since `z=[x,y]`, every rank-one
character has `rho(z)=1`.  The selected `q64=15` phase has exact order `64`,
so it is nontrivial on `z`.

The same phase also cannot be used as a scalar `SU3` center element, because a
scalar `lambda I_3` lies in `SU3` only when `lambda^3=1`.

## Meaning

This closes the ordinary local-system bridge negatively:

```text
q64=15 -> rank-one U(1) local system on compact Nil: no
q64=15 -> scalar SU3 center element: no
```

It does not kill the broader idea.  It redirects it:

```text
q64=15 can only survive here through a nonabelian/projective clock-shift
representation or through a separately source-certified endomorphism_E /
threshold operator.
```

The clock-shift route is mathematically natural because finite Heisenberg
representations can realize central commutator phases.  But that route is not
yet Qa/SU3 closure: it needs an operator-domain bridge and a torsion/determinant
finite part.

## Verdict

```text
rank-one U1 local-system bridge: closed negative
SU3 scalar-center bridge: closed negative
Qa/SU3 closed: no
full SM closure achieved: no
target fitting used: no
projective q64 route remains open: yes
```
