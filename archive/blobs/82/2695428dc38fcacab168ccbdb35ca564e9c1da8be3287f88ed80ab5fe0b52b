# Selected Qa/SU3 Monad Map Construction or Source Augmentation v1

## Purpose

The previous fill attempt showed that the corpus prints the Iwasawa `SU(3)`
monad topology but not the typed maps.  This artifact computes the exact
line-bundle charges that any valid maps must carry.

## Charge Table

For

```text
f_i: K1 -> L_i
g_i: L_i -> K2
```

the required section charges are:

```text
i  ell_i       f_i in H0(L_i K1^-1)   g_i in H0(K2 L_i^-1)
1  (-2,0,1)    (-3,0,1)               (2,1,-1)
2  (-1,1,-1)   (-2,1,-1)              (1,0,1)
3  (1,-1,0)    (0,-1,0)               (-1,2,0)
4  (1,0,-1)    (0,0,-1)               (-1,1,1)
5  (2,1,1)     (1,1,1)                (-2,0,-1)
```

Every product `g_i f_i` has the same composite charge:

```text
K2 - K1 = (-1,1,0)
```

So the monad is charge-compatible at the algebraic level.  That is real
progress: the obstruction is not an immediate charge mismatch.

## Blocker

Charge compatibility is not yet a map construction.  To prove `g*f=0`, we need
a basis of sections and a multiplication table into `H0(K2 K1^-1)`.  The corpus
scan found generic map language and Dolbeault diagnostics, but no selected
Iwasawa section ring, effective cone, line-bundle section basis, or typed
coefficients for the exact `f_i,g_i`.

## Verdict

```text
charge table computed: yes
charge-level compatibility passed: yes
section data found: no
explicit f,g constructed: no
g*f=0 checked: no
monad route retired: no
source augmentation required: yes
Qa/SU3 closed: no
target fitting used: no
```

## Minimal Augmentation

The fastest rigorous route is one of:

```text
A. Source prints the five f_i entries, five g_i entries, and a relation proving sum_i g_i f_i = 0.
B. We build the Iwasawa line-bundle section ring: H0 bases and multiplication table for the ten required charges.
C. Source gives a direct Dolbeault/Cech/rho_E operator exit derived from this same monad.
```

Next artifact:

```text
Selected_Qa_SU3_Iwasawa_Line_Bundle_Section_Ring_Interface_v1
```

