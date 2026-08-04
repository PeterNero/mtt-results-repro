# MTT Selected q79 Genus-Two Handle Monodromy Promotion v1

Status: `MTT_U6_Q79_TWO_TORUS_HANDLE_MONODROMIES_PROMOTED_90_LOCAL_AND_GLOBAL_RELATION_OPEN`

## The promoted result

A114 promotes the two nonlocal torus-handle actions for the selected q79
genus-two family. The normalized base loops are

```text
A: w(s)=(1+i)/4+s,
B: w(s)=(1+i)/4+i*s,
```

and elliptic periodicity returns both endpoints to the same regular fiber.
FLINT/Arb Rouche tests certify six pairwise-disjoint continuous root tubes on
all 6,928 A segments and all 5,004 B segments, 11,932 segments in total. The few broad interval boxes are
bisected while retaining one fixed root disk; the maximum subdivision depth is
one for A and three for B. The minimum relative Rouche margins remain positive:
`2.9057104471154688e-05` and
`1.5917270505657217e-06`.

An independent 80-digit interval projection at `exp(-i*pi/7)` certifies every
endpoint order, all 74 crossing signs and heights, and the order of the two
segments containing multiple crossing events. Convexity of each disjoint tube
gives an isotopy from the true root strands to these certified piecewise-linear
braids.

Birman-Hilden hyperelliptic lifting supplies the standard topological bridge:
each adjacent branch-point half-twist lifts to the corresponding chain Dehn
twist. In the frozen basis `[a1,b1,a2,b2]`, exact word replay gives

```text
M_A = [[0, 0, 1, 2], [2, 1, -1, -1], [-1, 0, 1, 2], [0, -1, -2, -4]],
M_B = [[-1, -1, 0, 1], [1, 0, 0, 0], [-1, 0, -1, -1], [1, 0, 1, 0]].
```

Both matrices have determinant one and preserve the integral intersection
form. They do not commute. Their promoted commutator is

```text
[M_A,M_B] = [[3, 9, 6, -1], [-3, -4, -8, -1], [4, 11, 9, -1], [-6, -20, -12, 3]].
```

This is a real advance over A113: the handle matrices are no longer numerical candidates.
The expensive root-tube computation is frozen with hashes, while
the active verifier independently checks every word and matrix exactly.

## Exact remaining frontier

A114 does **not** promote the 90 local Picard-Lefschetz candidates. Their frozen
exploration lacks the continuous trajectories needed for the same Rouche-tube
argument. It also does not multiply independently based meridians in root-id
order. A distinguished ordered cut system on the 90-punctured torus must first
fix all conjugations and the action convention; only then can the punctured-base
surface relation be checked against the promoted handle commutator.

Therefore the rank-four Gauss-Manin local system, Leray basis, beta periods,
gerbe zero, and strong-CP conclusion remain open. No MTT source modulus is
removed at this step.

## Reproduction

```powershell
python scripts/certify_q79genus2handle_root_tubes.py
python scripts/certify_q79genus2handle_pl_braids.py
python proof_corpus/selected_q79genus2handlemonodromypromotion_audit.py
```

The half-twist/Dehn-twist bridge is classical Birman-Hilden theory; A114's new
content is the explicit certified q79 path execution in the frozen marking.
