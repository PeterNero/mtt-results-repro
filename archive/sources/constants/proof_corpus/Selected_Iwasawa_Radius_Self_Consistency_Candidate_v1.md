# Selected Iwasawa Radius Self-Consistency Candidate v1

## Purpose

The final selected-character rho_UV theorem closes the branch function

```text
rho_UV(R) = [64(2pi)^2/(16R^4+8)]^2
```

but leaves the Iwasawa radius `R` unselected.

This note records the strongest currently visible way to close that last gate:
identify the symmetric Iwasawa radius with the same remaining scale variable
selected by the scale-lifting functional.

This is a candidate theorem, not yet a certified theorem, because it requires
one bridge premise.

## Candidate Bridge Premise

On the symmetric Iwasawa branch in internal `alpha'=1` units,

```text
r1 = r2 = R
```

is the remaining positive dilation variable of the selected
Flux/Strominger scale-lifting problem.

Equivalently, after fixing the selected invariant frame and coefficient
normalization, the scale minimizer returned by the reduced functional must
satisfy the self-consistency equation

```text
R = s_*(R).
```

This is not a fit to an observed constant. It is an internal fixed-point
condition identifying two appearances of the same branch scale.

## Self-Consistency Equation

The final rho_UV theorem gives

```text
s_*(R) = (60 rho_UV(R))^(1/6)
```

and therefore

```text
s_*(R)
  = (60)^(1/6) [64(2pi)^2/(16R^4+8)]^(1/3).
```

The selected-radius equation is

```text
R = (60)^(1/6) [64(2pi)^2/(16R^4+8)]^(1/3).
```

Equivalently,

```text
R^6 = 60 [64(2pi)^2/(16R^4+8)]^2.
```

## Uniqueness

Define

```text
g(R) = R - s_*(R),        R > 0.
```

The function `R` is strictly increasing. The function `s_*(R)` is strictly
decreasing because

```text
64(2pi)^2/(16R^4+8)
```

is strictly decreasing on `R > 0`. Therefore `g(R)` is strictly increasing.

Moreover,

```text
lim_{R->0+} g(R) < 0,
lim_{R->infinity} g(R) = +infinity.
```

Hence the self-consistency equation has exactly one positive solution.

## Numerical Candidate

Solving the equation gives

```text
R_* = 2.7576341244749276.
```

At this candidate radius:

```text
r3      = 4.423799651933971,
v1      = 2.7072870676415306,
rho_UV  = 7.329403266619077,
s_*     = 2.7576341244749276.
```

## Relation to Other Routes

This self-consistency route is currently stronger than a direct LensNil import,
because the LensNil corpus fixes `R1/R` for selected flux integers but does not
yet source-certify the selected integers `(f,h)` or a proved bridge identifying
the LensNil `R` with the Iwasawa symmetric radius.

It is also cleaner than using the central-circle radius alone, because the
central circle selects `R1(N)=sqrt(log N/15)`, whereas the rho_UV theorem
requires the Iwasawa horizontal radius `R`.

The likely final closure may still combine all three:

```text
Iwasawa radius self-consistency
+ LensNil ratio compatibility
+ central-circle/shared-circle compatibility.
```

## What Must Be Proved Next

To promote this candidate to a theorem, prove the bridge premise:

```text
The symmetric Iwasawa radius R is the same remaining dilation coordinate s
used in the selected Flux/Strominger scale-lifting functional.
```

The proof should check:

```text
1. no hidden second scale remains in the symmetric Iwasawa slice;
2. alpha'=1 internal units are the same units used by the scale-lifting lemma;
3. the coefficient response rho_UV(R) is evaluated before target constants enter;
4. setting R=s_*(R) is fixed-point consistency, not empirical tuning;
5. Lens, Nil, and shared-circle data do not contradict the resulting R_*.
```

## Verdict

This is the best currently visible route to the missing puzzle piece.

If the bridge premise is certified, the final rho_UV branch becomes a
single no-knob internal number:

```text
R_* = 2.7576341244749276,
rho_UV = 7.329403266619077,
s_* = R_*.
```

Until that bridge premise is certified, this remains a candidate closure rather
than the final selected Iwasawa radius theorem.
