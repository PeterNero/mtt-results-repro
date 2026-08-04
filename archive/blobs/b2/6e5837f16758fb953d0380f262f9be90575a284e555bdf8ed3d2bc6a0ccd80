# Selected Qa/SU3 Minimal Hsel/Gret Finite Galerkin Candidate v1

## Construction

This artifact constructs the missing finite candidate rather than searching for
another prose source.  The only numerical input is the already-used typed monad
charge table.  No observed residual, mass, coupling, q79 table, or fitted target
enters the calculation.

Finite basis:

```text
['F1', 'F2', 'F3', 'F4', 'F5', 'G1', 'G2', 'G3', 'G4', 'G5', 'P']
```

Charge-coordinate basis:

```text
[K1, K2, c]
```

The selected finite Galerkin Hessian is the canonical charge Gram block:

```text
H_sel = sum_L q(L) q(L)^T = [[26, -3, 0], [-3, 10, 0], [0, 0, 8]]
det(H_sel) = 2008
```

Its exact retarded Green kernel is:

```text
G_ret = H_sel^-1 = [['10/251', '3/251', 0], ['3/251', '26/251', 0], [0, 0, '1/8']]
H_sel G_ret = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

## Twist Selector

The admissible product target `P=(-1,1,0)` forces an integral covector
annihilating `P` to have the form:

```text
ell = (a, a, c)
```

The twisted sector requires `c != 0`.  The exact retarded norm is:

```text
||ell||^2_G = 42*a^2/251 + c^2/8
```

So the primitive twisted minimizers are `+/-e3`.  The positive primitive
orientation selects:

```text
Pi_tw = +e3 = [0,0,1]
```

Then:

```text
tau(L)=<e3,q(L)>
tau = {'F1': 1, 'F2': -1, 'F3': 0, 'F4': -1, 'F5': 1, 'G1': -1, 'G2': 1, 'G3': 0, 'G4': 1, 'G5': -1, 'P': 0}
```

and the five products obey:

```text
tau(F_i)+tau(G_i)=tau(P)=0
```

## Machine Result

The filled packet is:

```text
candidate_data\hessian_kernel_central_cocycle_finite_galerkin_candidate.packet.json
```

Validator result:

```text
exit code: 0
output: packet passes implemented Hessian/kernel central-cocycle checks
```

## What This Closes

- actual finite `H_sel`;
- exact rational `G_ret`;
- exact inverse identity;
- finite selection of `Pi_tw=+e3`;
- Hessian/Green-derived `tau`;
- implemented central-cocycle validator pass.

## What It Does Not Yet Close

This is still not the full smooth Qa/SU3 threshold proof.  The next promotion
must prove that this finite charge-coordinate Galerkin block is the actual
MTT-selected smooth/operator Hessian block, or else reject it.  It must also
provide the same-source `D_E/rho_E`, full admissibility checks, and determinant
finite part.

Next artifact:

```text
Selected_Qa_SU3_Finite_Galerkin_to_Smooth_Operator_Promotion_or_NoGo_v1
```
