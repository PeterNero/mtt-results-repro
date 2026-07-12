---
title: |
  Iwasawa Route C Smoke to C1 Dependency Reduction
author: MTT proof reproduction program
---

# Iwasawa Route C Smoke to C1 Dependency Reduction

This note records the next computation after the branch-aware Route C smoke
package.

The branch smoke data now supplies, for both conjugate branches:

```text
D_E,
Riesz projectors,
reduced Green operators,
dotD_alpha1,
horizontal zero-mode responses.
```

The natural next question is whether those values already determine the C1
Yukawa response matrices.

They do not.  They determine the response side of the contraction, but not the
sector-resolved trilinear overlap tensors that convert a horizontal response
into a Yukawa entry.

## Executed Calculation

The executable calculation is:

```text
scripts/analyze_iwasawa_route_c_smoke_c1_dependency.py
```

It reads:

```text
candidate_data/iwasawa_route_c_branch_smoke/
```

and writes:

```text
candidate_data/iwasawa_route_c_smoke_c1_dependency.candidate.json
certificates/iwasawa_route_c_smoke_c1_dependency_certificate.json
```

For each sector:

```text
u   : Q x u x H,
d   : Q x d x Hdagger,
e   : L x e x Hdagger,
nuD : L x N x H.
```

the script records the exact symbolic dependency:

```text
B_s,L[i,j] = dotPsi_left[i]  * T_s[left_complement, j, H0],
B_s,R[i,j] = dotPsi_right[j] * T_s[i, right_complement, H0],
B_s,H[i,j] = dotPsi_H       * T_s[i, j, H_complement].
```

The known numerical coefficients are the branch-smoke horizontal responses.
The unknowns are the selected trilinear tensor slots `T_s`.

## Count Reduction

If the direct `theta`, explicit-vertex, and basis-connection terms are absent
or separately proved zero, the dotD response reduces the C1 primitive matrix
problem to:

```text
15 complex overlap slots per sector for the full 3 x 3 matrix,
5 complex overlap slots per sector for the heavy-link entries (13,23).
```

So the computation did not close the C1 matrices, but it did shrink and locate
the missing object.

## Universal Tensor Test

The script also tests the bare universal E6 tensor case:

```text
T_u = T_d,
theta/vertex/basis terms agree between u and d,
no selected SU(5) sector splitting,
no selected basis transport.
```

In the branch-smoke data, the family response coefficients are identical across
`Q,u,d,L,e,N` inside each branch.  Therefore, under the universal tensor
assumption:

```text
M_u = M_d,
Delta_t = (M_d13 - M_u13, M_d23 - M_u23) = (0,0).
```

Thus the Route C smoke `dotD` response alone cannot supply the character-trivial
CKM heavy link.  A nonzero leading CKM heavy link needs selected data that
distinguishes the up and down sector contractions.

## Branch Pair

The q79 and q369 branch response coefficients are exact conjugates within
floating tolerance.  This preserves the global-conjugate-pair picture:

```text
q=79 branch  -> chi_79 response,
q=369 branch -> conjugate chi_369 response.
```

The calculation does not split the conjugate pair.  It shows that both branches
hit the same next obstacle.

## Meaning

The hard frontier moved from:

```text
compute dotD response
```

to:

```text
derive the selected sector-resolved overlap tensor T_s,
or derive the selected SU(5) representation-projection tensor,
or derive selected theta/vertex/basis primitive terms.
```

This aligns with the existing SU(5) family-orientation candidate: that
candidate is not selected yet, but it is now exactly the kind of missing
structure that would make `u` and `d` differ.

## Guardrail

This is not a selected C1 response computation.  It does not claim:

```text
selected overlap tensors,
selected C1 matrices,
CKM angle magnitudes,
Yukawa magnitudes,
full SM closure.
```

It is a dependency reduction and a no-go for the universal-tensor-only route.
