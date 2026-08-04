# q79 eta9 characteristic-zero detecting-meridian transport

## Scope

This packet advances blocker `B.ETA9.01` from a promoted finite good fibre to
an exact characteristic-zero execution problem.  It does not yet claim the
detecting meridian, its integral transport, a period value, the physical
Deligne row, or `U_eta9`.

Gate 1 remains frozen at 30/30 groups and 225/225 support columns.  None of
its campaign calculations is rerun.  Gate 2 is consumed through the promoted
hash-bound packet containing:

- 248 H02 stage-one rows of rank 248 over `GF(11)`;
- the `1509 x 248` source block of rank 248 over `GF(11)`;
- the `1509 x 1509` operator of rank 1509 and determinant 1 over `GF(11)`.

These data certify the selected good reduction.  They are not interpreted as
a characteristic-zero connection.

## Exact H02 decomposition

The characteristic-zero chart oracle supplies the selected H02 matrix over
`Z[gamma]`.  Removing the 248 quotient-unit columns and rows leaves a
`42458 x 42458` complement with 2,325,539 exact nonzero positions.  Its
structural matching is perfect.  Strong-component decomposition in the
matched directed graph gives an exact block upper-triangular order with no
backward edge and the following diagonal blocks:

- one core of dimension 24,767;
- 17,691 scalar blocks.

The full exact matrix has 1,800,425 entries with a nonconstant `gamma`
coefficient.  Within the unique diagonal core, 17,676 columns and 15,158 rows
carry the nonconstant part.  Concatenating powers `gamma^1` through
`gamma^5` gives a `24767 x 88380` update pattern with 7,901,469 nonzero
integer coefficients.  Of the scalar diagonal blocks, 1,614 depend on
`gamma`; they remain one-dimensional exact divisions.  Off-diagonal entries
are propagated in the certified condensation-DAG order and are not additional
large solves.

The packet records canonical SHA-256 identities for the exact pattern,
matching, component assignments, component sizes, topological order, and
active core rows and columns.  The dedicated verifier reconstructs all of
them independently from the selected Macaulay columns.

## Integer-anchor theorem

Let `A(gamma)` denote the unique 24,767-dimensional diagonal H02 core.  The
coefficient field has six certified embeddings.  Choose, for each embedding,
the nearest displayed integer in the selected residue class:

| Embedding | Kind | Anchor |
| --- | --- | ---: |
| 0 | real | -19 |
| 1 | real | -8 |
| 2 | complex, negative imaginary | 3 |
| 3 | complex, positive imaginary | 3 |
| 4 | complex, negative imaginary | 3 |
| 5 | complex, positive imaginary | 3 |

Every anchor is congruent to 3 modulo 11.  Consequently `A(a)` reduces to the
selected H02 matrix at `(11, gamma - 3)`, whose determinant is 2 modulo 11.
Thus every integral anchor matrix has nonzero determinant over `Q`.

For an embedding `e`, let `U` include the 15,158 active core coordinate rows
and let `V_e` contain the corresponding exact rows of
`A(gamma_e) - A(a_e)`.  Then

```text
A(gamma_e) = A(a_e) + U V_e.
```

The determinant lemma and Woodbury identity therefore reduce the core to

```text
W_e = I_15158 + V_e A(a_e)^(-1) U.
```

This is an exact identity.  The good-fibre calculation is used only to prove
the integer anchors invertible; it is never substituted for the
characteristic-zero matrix.

## Combined execution boundary

The three Hodge blocks now have the following exact execution form:

| Block | Current exact reduction |
| --- | --- |
| H20 | exact inverse action already emitted |
| H11 | two large cores reduced to kernels of dimensions 934 and 398 |
| H02 | unique large core reduced to a kernel of dimension 15,158 |

This removes the need for one monolithic 42,458-dimensional
characteristic-zero solve.  It does not evaluate the reduced kernels at the
six embeddings, and it does not provide path-ordered transport.

## What remains

The next proof object must combine two independent ingredients:

1. The D6 relation campaign must supply the selected detecting-meridian word
   and its labeled path transport.
2. The exact reduced kernels must be executed along that path with certified
   complex interval balls.

The resulting transport must then be normalized to an integral rank-1509
representative and applied to the selected 248-dimensional period source.
Only a certified 248-coordinate period image can decide the physical Deligne
row and either emit `U_eta9` or prove a nonzero obstruction.

The fourteen binary filling/framing choices are not candidate period knobs:
the existing twisted-surgery invariance theorem shows that they do not change
the relevant twisted homology or period pairing.  No unified-action claim is
made in this packet.
