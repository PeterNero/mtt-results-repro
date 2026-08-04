---
abstract: |
  We prove the finite algebraic core of the SU(5) qutrit Sector Transport
  Selection Lemma.  In the irreducible qutrit Heisenberg carrier with clock Z
  and shift X satisfying ZX=omega XZ, the normalized qutrit Fourier matrix F
  is the unique dephased transport from clock polarization to shift
  polarization, up to the conjugate orientation.  Thus if selected zero-mode
  data place 10_M in the clock polarization and bar5_M in the shift
  polarization, then B_10=I_3 and B_bar5=F, giving the candidate heavy-link
  direction (1/sqrt(3), omega^2/sqrt(3)).  The finite theorem is closed; the
  remaining selection hypothesis is the geometric proof that MTT chooses those
  polarizations for the SU(5) matter slots.
author:
- Peter Nero
date: May 2026
title: |
  Qutrit Polarization Transport Lemma
---

# Statement

Let the qutrit clock and shift operators be:

```text
Z e_j = omega^j e_j,
X e_j = e_(j+1 mod 3),
omega = exp(2*pi*i/3).
```

They satisfy:

```text
Z X = omega X Z.
```

Let:

```text
F_jk = omega^(j k)/sqrt(3).
```

Then:

```text
F^dagger Z F = X,
F^dagger X F = Z^-1.
```

Therefore `F` is exactly the transport from the clock polarization to the
shift polarization, with the chosen orientation convention.

# Uniqueness

Fix the usual dephasing:

```text
first row positive,
first column positive.
```

A brute-force root-of-unity classification over third roots finds exactly two
dephased `3 x 3` complex Hadamard matrices:

```text
F,
F^*.
```

The orientation condition:

```text
F^dagger Z F = X
```

selects `F`.  The opposite shift orientation selects `F^*`.

Thus the finite ambiguity is only:

```text
orientation conjugation,
external row/column rephasings,
family relabeling conventions.
```

Those are exactly the expected finite gauge choices.

# SU(5) Consequence

If the selected zero-mode construction proves:

```text
10_M    uses the clock polarization,
bar5_M  uses the shift polarization,
```

then after dephasing:

```text
B_10 = I_3,
B_bar5 = F.
```

For the pure diagonal support `I_3`, the transported support is:

```text
M(left,right) = B_left^dagger I_3 B_right.
```

The up channel is:

```text
M_u = B_10^dagger B_10 = I_3.
```

The down channel is:

```text
M_d = B_10^dagger B_bar5 = F.
```

So the heavy-link vector is:

```text
Delta_t = (F_13, F_23)
        = (1/sqrt(3), omega^2/sqrt(3)).
```

Numerically:

```text
Delta_t = (0.5773502691896258,
           -0.28867513459481287 - 0.5 i).
```

# What Is Proved

This proves:

```text
clock/shift qutrit polarization transport = Fourier,
the SU(5) heavy-link candidate follows from the polarization hypothesis,
the only finite orientation alternative is the conjugate Fourier convention.
```

# What Is Not Proved Here

This does not by itself prove:

```text
MTT selects 10_M as clock-polarized,
MTT selects bar5_M as shift-polarized,
the selected overlap-kernel prefactor,
canonical kinetic normalization,
CKM angles or Jarlskog,
full SM closure.
```

# Remaining Lemma

The hard selection lemma is now smaller:

```text
Polarization Selection Lemma.
Selected zero-mode/monad/Galerkin data place 10_M in the qutrit clock
polarization and bar5_M in the qutrit shift polarization.
```

Once this is proved, the previous SU(5) qutrit heavy-link candidate is promoted
from conditional fixture to selected heavy-link input.
