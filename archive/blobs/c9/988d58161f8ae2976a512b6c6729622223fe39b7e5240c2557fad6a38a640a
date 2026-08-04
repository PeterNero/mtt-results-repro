# q79 Trial Branch Irreducibility and Strict-Spin Decision v1

Date: 2026-07-15

## Exact identity-alignment calculation

The corpus contains an exact smooth q79 spectral surface at the square elliptic
curve and identity `PGL3` alignment. That alignment is explicitly a trial, not
an MTT-selected source. It nevertheless permits the missing branch-complement
test to be executed exactly.

For

```text
E: b^2=a^3-a,
```

the Gauss map to the dual cubic is

```text
[l0:l1:l2]=[1-3a^2:2b:a^3+a].
```

The discriminant of a line section gives the dual sextic

```text
4*l0^5*l2 + l0^4*l1^2 - 4*l0^3*l2^3
+ 30*l0^2*l1^2*l2^2 + 24*l0*l1^4*l2
+ 4*l1^6 - 27*l1^2*l2^4 = 0.
```

Pull the exact K3 branch sextic through this Gauss map and reduce by
`b^2=a^3-a`. The result is `A(a)+bB(a)`, with degrees `18` and `14`. Its norm
to `Q(a)` is

```text
N(a)=A(a)^2-(a^3-a)B(a)^2.
```

The executable factorization proves that `N` is irreducible over `Q`, has
degree `36`, occurs with multiplicity one, and is square-free. If `A+bB` were a
square in `Q(E)`, its norm would be a square in `Q(a)`. It is not. Therefore
the pulled-back dual sextic is reduced and irreducible in this exact carrier.

## Spin decision for the witness

The preceding `w2` theorem then applies without a remaining complement premise:

```text
[branch]=6H,
H1(branch complement;Z)=Z6,
sign:Z6->Z2 has no Z4 lift,
w2=a^2 != 0.
```

Hence the identity-alignment signed-sheet carrier has no strict Spin lift on
its branch complement. A SpinC determinant-line construction remains a
separate open theorem.

## Selected-source boundary

This is not yet the selected q79 decision. The source packet marks the identity
alignment as unselected. What has been proved is stronger than a numerical
example: the irreducible alignment locus is nonempty, and the selected decision
is now one exact membership test.

Run the same norm calculation after substituting the selected `PGL3` matrix, or
certify that a path from identity to the selected matrix avoids the
reducibility discriminant. No new metric, fit, or physical constant is needed.

Current status:

```text
TRIAL_IDENTITY_STRICT_SPIN_NOGO_CLOSED_SELECTED_ALIGNMENT_MEMBERSHIP_OPEN
```
