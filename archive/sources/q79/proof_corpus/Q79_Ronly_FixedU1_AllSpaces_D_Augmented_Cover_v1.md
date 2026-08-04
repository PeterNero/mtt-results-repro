# q79 all-space fixed-u1 D-augmented finite-cover theorem

Date: 2026-07-21

## Dependencies

This theorem combines, without identifying their distinct polynomial cores,
the independently certified space-5 and space-6 results:

```text
Q79_Ronly_FixedU1_Space5_D_Augmented_Cover_v1
Q79_Ronly_FixedU1_Space6_D_Augmented_Cover_v1
```

Both work over `F_101`, fix `u1=1` and hence `u0=1`, retain both inverse-root
scalar representatives, and use the same exact parent involution
`(a,v)->(-a,-v)`.

## Theorem

For each

```text
space in {5,6},  s in {1,2},  a,v in F_101^*,
```

the complete selected `R/y/D` inverse-root fiber ideal is the unit ideal.
Consequently, the simultaneous selected system has no point on the full
40,000-element nonzero endpoint grid at `u1=1`.

The exact canonical accounting is

```text
space       R-only [1]    full R/y/D [1]    canonical total    signed total
5                9,993                   7             10,000          20,000
6                9,996                   4             10,000          20,000
union           19,989                  11             20,000          40,000
```

Every R-only entry is supported by an embedded literal one-element reduced
Groebner basis `[1]` using parent rows 1 through 12. At the eleven exact
nonunit R fibers, a second packet restores the four `y` variables and all
four D-terminal rows and embeds the literal full-parent basis `[1]`. Thus no
timeout, numerical residual, incomplete computation, or nonunit output is
promoted to an emptiness result.

The sign involution maps each canonical `a=1,...,50` line to its omitted
partner while preserving the complete parent scheme. It therefore doubles
the 20,000 explicitly classified canonical fibers to all 40,000 endpoint
fibers without an extra fit or solver assumption.

## Exact tier

This closes exactly four of the 400 finite `(space, scalar class, u1)` slices:

```text
(5,1,1), (5,2,1), (6,1,1), (6,2,1).
```

Each fixed fiber is a unit ideal over `F_101` and remains empty after scalar
extension. The enumeration itself, however, does not range over
extension-valued `u1`, `a`, or `v`; it is not a global symbolic proof for the
two unresolved mirror charts.

## Claim boundary

The remaining finite slices have `u1=2,...,100`. Characteristic-zero lifting,
global scheme closure, and physical HYM/QG source promotion also remain open.
The global chart accounting therefore remains `138/140`.

No continuous fit parameter is introduced.

## Reproduce

```text
python proof_corpus/q79_Ronly_fixed_u1_all_spaces_D_augmented_cover_audit.py
```
