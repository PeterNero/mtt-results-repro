# Certified Representation Diagram Theorem v1

Date: 2026-07-17

Status: proved finite-dimensional theorem; MTT interpretation and nonlinear
extensions are a research program, not an authority promotion.

## 1. Motivation

MTT repeatedly represents one proposed source in several forms:

```text
finite character
integral bundle or cocycle
connection
operator
gauge orbit
retarded response
physical observable
```

Agreement at the last numeric node does not prove that the earlier nodes came
from one source. The following construction makes compatibility itself an
operator.

## 2. Linear representation diagram

Let `Gamma=(V,E)` be a finite directed graph. Assign:

```text
a finite-dimensional Hilbert space H_v to every vertex v;
a linear transport T_e : H_s(e) -> H_t(e) to every edge e;
a positive-definite weight W_e on every edge residual space.
```

Set

```text
H_0 = direct_sum_v H_v,
H_1 = direct_sum_e H_t(e).
```

For `x=(x_v)` define the compatibility coboundary

```text
(delta_D x)_e = T_e x_s(e) - x_t(e).
```

Let `W=direct_sum_e W_e`, `A=W^(1/2) delta_D`, and define the compatibility
Laplacian

```text
L_D = A^* A = delta_D^* W delta_D.
```

## 3. Compatibility theorem

### Theorem 1: kernel, projection and obstruction

For the finite linear diagram above:

1. `L_D` is self-adjoint and positive semidefinite.
2. `ker L_D = ker delta_D`.
3. `ker L_D` is exactly the vector space of compatible sections of the diagram.
4. The orthogonal projector onto compatible sections is

   ```text
   Pi_D = I - A^+ A
        = I - A^* (A A^*)^+ A,
   ```

   where `+` is the Moore-Penrose inverse.
5. For an affine compatibility equation `A x=b`, the minimum squared defect is

   ```text
   epsilon_min^2 = ||(I-A A^+)b||^2.
   ```

   A compatible source exists if and only if `epsilon_min=0`.
6. If a linear gauge subspace `G` is contained in `ker L_D`, then the local
   physical source freedom is

   ```text
   nullity_phys = dim ker L_D - dim G.
   ```

### Proof

For every `x`,

```text
<x,L_D x> = <x,A^* A x> = ||A x||^2 >= 0.
```

Hence `L_D` is positive semidefinite. Also,

```text
L_D x=0
  => <x,L_D x>=0
  => ||A x||=0
  => A x=0
  => delta_D x=0,
```

because `W` is positive definite. The converse is immediate. Thus items 1-3
hold.

The Moore-Penrose identities imply that `A^+A` is the orthogonal projector onto
`im A^*=ker(A)^perp`. Therefore `I-A^+A` is the orthogonal projector onto
`ker A=ker delta_D`, proving item 4.

The vector `A A^+b` is the orthogonal projection of `b` onto `im A`. The affine
equation is solvable exactly when the orthogonal remainder `(I-A A^+)b`
vanishes, proving item 5. Item 6 is the dimension of the quotient by a free
linear gauge action. QED.

## 4. Spectral meaning

Let the eigenvalues of `L_D` be

```text
0 = lambda_1 = ... = lambda_k < lambda_(k+1) <= ... .
```

Then:

```text
k                         = compatible-section dimension;
k - dim G                 = unresolved physical source directions;
lambda_(k+1)              = linear stability gap;
1/lambda_(k+1)            = worst compatibility sensitivity on ker(L_D)^perp.
```

A small positive gap means source promotion is ill-conditioned even when it is
formally unique.

## 5. Lifting interpretation

Suppose the diagram splits into known nodes `K` and a stronger source node `S`.
The restriction map

```text
pi_K : lim D -> lim D|_K
```

has the following interpretations:

```text
empty fiber             incompatible packets or a no-go;
one gauge orbit         selected same-source promotion;
several discrete orbits unresolved branch selection;
positive-dimensional fiber hidden or explicit continuous choices;
```

This is the precise distinction between validating a finite shadow and selecting
its integral lift.

## 6. Nonlinear and gauge version

Let the node spaces be manifolds, groupoids, or stacks and let the edge mismatch
map be

```text
Phi : X -> Y.
```

A compatible source is a point of `Phi^-1(0)`. At a candidate `x_0`, use the
linearized compatibility operator

```text
A_x0 = D Phi|_x0,
L_x0 = A_x0^* W A_x0.
```

If `A_x0` is surjective and its kernel consists exactly of gauge directions, the
implicit-function theorem gives local uniqueness modulo gauge. If the action has
stabilizers or the equations have derived intersections, the correct reference
object is the homotopy fiber or derived zero locus, not an ordinary quotient
set.

For a contraction `T` with `||DT|| <= Z < 1`, the fixed-point equation

```text
Phi(u)=u-T(u)=0
```

has invertible linearization, with

```text
||(I-DT)^-1|| <= 1/(1-Z).
```

This is the analytic form used by the current HYM benchmark.

## 7. Same-source certificate

A same-source certificate must contain:

1. one source point or source orbit;
2. its realization at every claimed node;
3. every edge transport or correspondence;
4. a zero compatibility residual, or a rigorous interval containing zero with a
   uniqueness bound;
5. gauge and branch stabilizers;
6. the dimension and spectral gap of the remaining kernel;
7. provenance hashes for the executable realizations.

Matching terminal numbers without items 1-4 is not a same-source certificate.

## 8. Finite-group version

For finite abelian groups, use group algebras and character transforms instead
of embedding residue constraints into real vector spaces. The compatible-section
projector is a product of character averages. For a congruence `q=r mod n`,

```text
P_(n,r)(q) = (1/n) sum_(k=0)^(n-1) exp(2*pi*i*k*(q-r)/n).
```

This is exactly `1` on the selected residue class and `0` otherwise. Products
of commuting residue projectors implement arithmetic descent. In the q79
benchmark,

```text
P_(64,15) P_(7,2)
```

has one-point support `{79}` in `Z448`.

## 9. Cohomological version

When the diagram is a cover or group-cochain complex, `delta_D` is the Cech or
group-cohomology differential. Then:

```text
ker delta_D              cocycles;
im delta_previous        gauge/coboundary changes;
H = ker/im               inequivalent global classes.
```

The current `F3^2` witness has, in the normalized `F3` complex,

```text
dim C1 = 8,
dim C2 = 64,
dim C3 = 512,
rank d1 = 6,
rank d2 = 55,
dim Z2 = 9,
dim B2 = 6,
dim H2 = 3.
```

The emitted bilinear witness lies in `Z2` but not `B2`. Thus it defines a
nontrivial class, while compatibility alone does not uniquely select that class.

## 10. Exact benchmark consequences

The executable prototype currently proves:

```text
B1 CRT lift:                         unique global section q=79
B2 normalized F3^2 group/Cech model: nontrivial H2 class, dim H2=3
B3 qutrit representation square:     injective image rank 27
B3 qutrit commutant:                 exact dimension 27
B3 direct SM-algebra identification: rejected
B4 selected Cech-to-HYM branch:       compatible and locally invertible
B5 target/swapped finite shadow:      two-element finite fiber
B5 ordered integral lift edge:        one-element target fiber
B5 integral source selection:         still open, not promoted
B6 GR internal/physical scale map:     Jacobian rank 1, scale nullity 1
B7 SMDR measured-profile map:          Jacobian rank 8, source nullity 7
B7 covariance transport:               relative reconstruction residual 4.003e-16
```

The literal adapter from the normalized B2 model to the corpus's emitted
81-entry/729-triple witness remains a separate implementation task. The current
B2 result proves that the reference language distinguishes cocycle,
coboundary, and cohomology class; it does not claim that adapter has already
been written.

## 11. What is new and what is not

Not new:

```text
graph/sheaf Laplacians;
Moore-Penrose compatibility projection;
homotopy limits and derived zero loci;
group cohomology;
double-centralizer arguments;
moment-map and gauge-reduction ideas.
```

Potentially new if completed:

```text
one typed MTT representation diagram that composes arithmetic descent,
differential-cohomology lifts, HYM reduction, spectral correspondences, causal
response, metrology, and observable transport while retaining executable
same-source certificates.
```

The novelty test is whether that combined diagram yields a theorem or value that
the separate formalisms did not make accessible.
