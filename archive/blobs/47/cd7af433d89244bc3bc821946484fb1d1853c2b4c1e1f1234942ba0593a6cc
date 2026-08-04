# Iwasawa Finite `D_E` Action Validator

## Purpose

The finite bundle stack now has validators for:

```text
rho_E transition algebra,
finite-mesh rho_E corner consistency,
Hermitian metric compatibility,
sector projection maps.
```

The next finite input is the operator action itself.  The Galerkin protocol
requires sector-specific matrices for the selected operator:

```text
D_E : V_domain -> V_range,
K = D_E^* G_range D_E.
```

This note adds an executable validator for candidate finite `D_E` action data.
It does not construct the selected operator.

## Supported v1 Format

A candidate file supplies:

```text
operator_slots: Q,u,d,L,e,N,H.
```

Each slot has:

```text
kind,
expected_kernel_dimension,
domain_dimension,
range_dimension,
domain_gram,
range_gram,
D_E_matrix,
stiffness_matrix,
ordered_zero_mode_basis,
selected_source_verified,
boundary_conditions_verified.
```

The expected kernel dimensions are:

```text
Q,u,d,L,e,N: 3,
H:           1.
```

The `domain_gram` and `range_gram` matrices define the finite inner products in
the domain and range bases.

## Checks

The script:

```text
scripts/validate_iwasawa_de_action.py
```

checks:

```text
all seven operator slots are present,
sector kind and kernel dimension match the SM slot contract,
domain and range dimensions are positive,
domain_gram and range_gram are positive-definite Hermitian,
D_E_matrix has shape range_dimension x domain_dimension,
stiffness_matrix has shape domain_dimension x domain_dimension,
stiffness_matrix = D_E^* range_gram D_E,
kernel dimension equals the expected value,
ordered_zero_mode_basis has the expected length,
D_E psi_i = 0 for every listed zero mode,
<psi_i,psi_j>_domain_gram = delta_ij,
selected_source_verified and boundary_conditions_verified are true.
```

The script returns:

```text
0: complete finite D_E action candidate passes,
1: complete candidate fails,
2: candidate is incomplete/open.
```

## Smoke Tests

The audit runs four tests.

First, the open Galerkin template is refused with exit code `2`, because it has
no `operator_slots`.

Second, a toy schema candidate passes:

```text
family slots: domain dimension 4, range dimension 1,
D_E = [0 0 0 1],
kernel basis = e1,e2,e3;

H slot: domain dimension 2, range dimension 1,
D_E = [0 1],
kernel basis = e1.
```

This proves the finite algebra contract is executable.  It is not selected
MTT data.

Third, a candidate with a wrong stiffness matrix fails:

```text
K != D_E^* G_range D_E.
```

Fourth, a candidate whose listed zero-mode basis is not annihilated by `D_E`
fails.

A missing slot is treated as incomplete/open rather than as a mathematical
failure.

## What This Closes

This closes:

```text
finite D_E action validator,
stiffness assembly gate,
kernel dimension and zero-mode basis gate,
domain/range Gram consistency gate.
```

It does not close:

```text
actual selected D_E action,
proof D_E comes from typed monad/Cech/HYM or selected spectral source,
actual selected rho_E,
actual selected Hermitian metric,
actual selected sector projection maps,
Riesz projector and complement gap,
dotD_alpha1 and reduced Green operator,
Yukawa overlap matrices.
```

## Guardrail

Do not treat the toy finite operator as selected data.

Do not set `D_E` or its kernel basis from observed masses, CKM angles, or
benchmark matrices.

Do not claim full SM closure from a finite action validator.  This is a
necessary consistency gate before the spectral projector, Green operator, and
overlap-matrix steps.

## Verdict

The finite execution stack can now reject malformed `D_E` matrix data before it
enters the SM closure pipeline.

The next selected-data step is still to supply the real selected `D_E` action
from typed monad/Cech/HYM or a validated non-invariant spectral source.  Once
that exists, the following gates become executable:

```text
Riesz projector,
gap/error certificate,
dotD_alpha1,
reduced Green operator,
overlap matrices.
```
