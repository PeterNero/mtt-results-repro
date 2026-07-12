---
title: |
  Time-Oriented Fixed Gerbe Representative
author: MTT proof reproduction program
---

# Question

Can the remaining finite torsion-label ambiguity:

```text
m in {1,2}
```

be fixed on the time-oriented q79 branch?

Yes, at the finite representative level.

# Result

The executable theorem is:

```text
q79/F  -> m = 1,
q369/F* -> m = 2.
```

This uses the already closed retarded exact/charge branch.  Without time
orientation, the selected object is still the conjugate pair.  With the
retarded q79 branch, the representative is fixed.

# Inputs

The proof uses:

```text
selected nontrivial gerbe-Fourier type,
finite Z3 gerbe holonomy map,
four-route torsion selector,
time-oriented q79/F branch theorem,
visible rho_E ordinary-source search.
```

The four-route torsion selector already proved:

```text
m = 0 is rejected,
m in {1,2} is the common nontrivial candidate pair.
```

The time-oriented branch theorem supplies the branch packet:

```text
q79/F:   torsion_label_m = 1,
q369/F*: torsion_label_m = 2.
```

# What This Closes

This removes one ambiguity:

```text
m=1 versus m=2 is no longer a time-oriented fitting knob.
```

The antiunitary conjugate is retained.  It is not a second unrelated universe
and not an extra adjustable parameter.

# What This Does Not Close

This does not claim:

```text
full Deligne/Cech gerbe period table,
full heterotic Green-Schwarz embedding for the new twist,
Freed-Witten verification on selected cycles,
twisted projector retention,
selected D_E,
dotD_alpha1,
primitive C1 contractions,
ordered SU(5) matter-slot packet,
Yukawa magnitudes,
full SM closure.
```

# Why This Matters

The previous blocker had two neighboring missing pieces:

```text
fixed selected torsion representative,
selected D_E/dotD response.
```

This closes the finite representative piece for the retarded branch.  The next
object is now more focused:

```text
selected de_response packet on q79/F with m=1.
```

# Artifact

The proof script is:

```text
scripts/prove_time_oriented_fixed_gerbe_representative.py
```

It writes:

```text
candidate_data/time_oriented_fixed_gerbe_representative.candidate.json
certificates/time_oriented_fixed_gerbe_representative_certificate.json
```

# Verdict

Closed:

```text
finite time-oriented torsion representative m=1 on q79/F.
```

Open:

```text
selected D_E/dotD response and full visible operator-source packet.
```
