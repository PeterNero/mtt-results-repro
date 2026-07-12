---
abstract: |
  The finite qutrit transport lemma proves that clock and shift polarizations
  are related by the normalized qutrit Fourier matrix.  This note closes the
  next rigor gate: the current corpus does not yet supply selected sector
  bases proving that 10_M is clock-polarized and bar5_M is shift-polarized.
  It also rejects the tempting SU(3) exterior-square shortcut.  The relation
  wedge2(E) ~= E^* is representation-theoretically relevant, but its natural
  Hodge transport is monomial, not the dense Fourier matrix, and therefore
  cannot by itself promote the heavy-link candidate to selected MTT data.
author:
- Peter Nero
date: May 2026
title: |
  SU(5) Qutrit Polarization Selection Gate
---

# Purpose

The previous finite lemma closed:

```text
clock polarization -> shift polarization = qutrit Fourier transport F.
```

The remaining selector would have to prove:

```text
10_M    uses the qutrit clock polarization,
bar5_M  uses the qutrit shift polarization.
```

If that is proved, then:

```text
B_10 = I_3,
B_bar5 = F,
Delta_t = (1/sqrt(3), omega^2/sqrt(3)).
```

# Current Source Check

The current certificates say:

```text
finite qutrit transport lemma: proved,
direct B_10/B_bar5 selector in the corpus: not found,
typed monad/Cech H^1 data: absent,
selected zero-mode sector bases: absent,
selected projective twist source: absent.
```

Thus the selection cannot yet be claimed from current data.

# Exterior-Square Shortcut Test

A natural thought is to use the SU(3) fact:

```text
wedge2(E) ~= E^*.
```

This is real representation evidence, but it is not the missing Fourier
transport.  In the basis:

```text
e01, e02, e12,
```

the exterior-square images of the qutrit clock and shift operators are
monomial matrices.  The Hodge identification:

```text
e01 -> e2^*,
e02 -> -e1^*,
e12 -> e0^*
```

is also monomial.  A monomial `3 x 3` matrix has exactly three nonzero entries.
The qutrit Fourier matrix has nine nonzero entries.

Diagonal rephasings and family permutations preserve the zero pattern, so a
monomial exterior-square/dual transport cannot become `F`.

Therefore:

```text
exterior-square duality supports the SU(5)/SU(3) representation dictionary,
but it does not prove B_10=I_3, B_bar5=F.
```

# Closed Gate

This closes the following:

```text
the finite qutrit transport core is available,
the existing corpus has been checked for a selector,
the current monad/zero-mode data are known absent,
the exterior-square shortcut is rejected,
the minimal remaining finite packet is identified.
```

# Remaining Packet

The remaining finite object is:

```text
certificates/selected_su5_qutrit_polarization_data.template.json
```

It must supply:

```text
U_10,
U_bar5,
selected source certificate,
unitarity in the selected L2 metrics,
U_10^dagger U_bar5 = F or F^* modulo rephasing/permutation,
orientation selection of F for q=79.
```

Only after that packet passes can the SU(5) qutrit heavy-link candidate be
promoted into selected basis-connection data.

# What Is Not Claimed

This gate does not claim:

```text
full polarization selection,
selected CKM angles,
selected Yukawa magnitudes,
full SM closure.
```

It makes the frontier exact: produce `U_10` and `U_bar5` from selected
zero-mode data, or the candidate remains conditional.
