---
title: |
  Time-Oriented Conjugate Branch Selection
author: MTT proof reproduction program
---

# Target

The branch question has two levels.

```text
Unoriented level: MTT selects a conjugate pair {q=79/F, q=369/F*}.
Time-oriented level: a selected retarded branch chooses one representative.
```

This note proves the second statement from the existing exact/charge branch
certificates.  It does not prove the ordered SU(5) matter-slot packet
`U_10=I_3, U_bar5=F`.

# Existing Inputs

The selected gerbe-Fourier type theorem proves:

```text
MTT selects the nontrivial Z3 gerbe/qutrit Fourier type up to global
conjugation.
```

The orientation bridge identifies the two remaining packets:

```text
m=1  <->  q=79   <->  F,
m=2  <->  q=369  <->  F*.
```

The C6 common-holonomy and global-phase certificates show that these are a
single global conjugate pair, not two unrelated phase knobs.

# Retarded Representative

The exact Z64 central-circle branch supplies the selected retarded kernel:

```text
K_ret,64 = S^-1,
selected lag = 16 -> 15,
q_64 = 15.
```

The Fu-Yau/Mukai charge sector supplies:

```text
q_7 = 2.
```

The executable CRT check gives:

```text
q = 15 mod 64,
q = 2  mod 7,
therefore q = 79 mod 448.
```

The conjugate label is:

```text
-79 = 369 mod 448,
369 = 49 mod 64,
369 = 5  mod 7.
```

Thus, once the retarded branch is part of the selected data, the selected
time-oriented representative is the `q=79` branch.  The `q=369` branch remains
as the global antiunitary/conjugate branch.

# Interpretation

This matches the user's hunch:

```text
MTT may contain both branches at the unoriented structural level.
A retarded initial/boundary choice selects the branch we see.
```

The analogy with an arrow of time is appropriate in this limited sense.  The
unoriented structure retains both conjugate possibilities; the time-oriented
realization selects the retarded representative.  This is a branch-selection
statement, not a claim that two independently tunable universes are being fit.

# What Remains Open

The theorem still does not select the ordered SU(5) packet:

```text
10_M = clock,
bar5_M = shift,
U_10 = I_3,
U_bar5 = F.
```

That requires selected matter-slot data from the same retarded branch, such as
a selected `D_E/dotD` operator package, typed monad/Cech zero-mode theorem, or
equivalent fixed differential-cohomology representative.

# Verdict

Closed now:

```text
Without time orientation: MTT selects the conjugate pair {q79/F, q369/F*}.
With the closed retarded exact/charge branch: MTT selects q79/F as the
time-oriented representative.
```

Still open:

```text
Exact ordered SU(5) matter-slot selection and full SM closure.
```
