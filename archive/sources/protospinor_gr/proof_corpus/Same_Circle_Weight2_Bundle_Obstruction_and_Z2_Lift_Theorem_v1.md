# Same-Circle Weight-2 Bundle Obstruction and Z2 Lift Theorem v1

Date: 2026-07-15

## Result

The phrase "the same circle" has to be typed before it can be proved. Let `Z`
be a correspondence base with maps to the internal q79 base and to the physical
transverse-frame base. Pull both lines to `Z`:

```text
L_sh   = p_sh^* L_shared,
L_perp = p_perp^* H_(+1).
```

The positive-helicity TT line is the weight-two line `L_perp^2`. Therefore the
TT sector can identify the two circle actions precisely when

```text
L_sh^2 ~= L_perp^2
```

as unitary line bundles with connection. With

```text
D = L_sh tensor L_perp^(-1),
```

this is equivalent to `D^2` being connection-trivial. Thus `D` is an
order-two flat line system:

```text
[D] in H^1(Z;Z2),
Hol_D(gamma) in {+1,-1}.
```

It follows that

```text
2(c1(L_sh)-c1(L_perp))=0,
F_sh=F_perp.
```

The Chern equation alone is not enough: connection-preserving equality also
requires the flat holonomies to agree. A unique weight-one root follows if
`H^1(Z;Z2)=0` or if an independent odd-weight/spinorial observable trivializes
`D`.

## Exact finite calculation

For `Z64`, the TT representation is

```text
chi_2(j)=exp(2*pi*i*2*j/64).
```

Its exact kernel and order are

```text
ker(chi_2)={0,32},
ord(chi_2)=32.
```

Hence the spin-2 action factors through `Z32`. It cannot distinguish `j` from
`j+32`. The two and only two character square roots are

```text
chi_1^2=chi_2,
chi_33^2=chi_2,
chi_33/chi_1=chi_32,
ord(chi_32)=2.
```

Weight one changes sign under `j -> j+32`; weight two does not. No calculation
using only the TT representation can choose between `chi_1` and `chi_33`.

## Corpus comparison

The terminal spinorial-return paper supplies an order-two parity type, and the
ambient `Z1344` Majorana check identifies its nontrivial self-conjugate label
`672`, whose CRT residues are `(32,0,0)` in `Z64 x Z7 x Z3`. These are exact
matches to the representation type `chi_32`.

They do not yet prove that this parity is the gravity mismatch line `D`, and
they do not choose `chi_1` rather than `chi_33`. The terminal paper still leaves
its concrete MTT operator extraction open; the q79 packet still leaves every
global Spin/SpinC contract field false.

## Local and global scope

The existing plus/cross map is valid at a fixed propagation direction. It must
not be silently promoted to a global polarization frame. Over the sphere of
momentum directions, a helicity-`h` line has first Chern number `C=-2h` in the
convention of Palmerduca and Qin; helicity `+2` therefore has `C=-4`. See the
primary result [Helicity is a topological invariant of massless particles](https://arxiv.org/abs/2407.03494).

## What advanced

The first clause of the QG compatibility theorem is no longer the unstructured
request "prove the circles are the same." It is now the following finite
cutset:

1. construct the correspondence base `Z` and both pullbacks;
2. compute the differential line class and prove `D^2` is trivial;
3. use an odd-weight/spinorial source to decide whether `D` itself is trivial;
4. extend that decision through the q79 branch locus with the selected HYM
   connection.

Current status:

```text
WEIGHT2_SAME_CIRCLE_REDUCED_TO_Z2_BUNDLE_OBSTRUCTION_ODD_LIFT_SELECTOR_OPEN
```
