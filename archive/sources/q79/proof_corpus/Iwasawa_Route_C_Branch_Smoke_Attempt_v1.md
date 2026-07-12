---
title: |
  Iwasawa Route C Branch-Aware Small-N Smoke Attempt
author: MTT proof reproduction program
---

# Iwasawa Route C Branch-Aware Small-N Smoke Attempt

This note records the first executable small-`N` Route C attempt after the
orientation fork was made explicit.

The goal was not to claim a selected HYM/Strominger solution.  The goal was to
push the branch-aware validator pipeline as far as possible with deterministic
finite data and see exactly where it stops.

## Branches Tested

Both conjugate packets were built:

```text
current_q79_orientation:
  m=1,
  q=79,
  SU(5) orientation F.

conjugate_q369_orientation:
  m=2,
  q=369,
  SU(5) orientation F*.
```

The candidate files are stored under:

```text
candidate_data/iwasawa_route_c_branch_smoke/current_q79_orientation/
candidate_data/iwasawa_route_c_branch_smoke/conjugate_q369_orientation/
```

Each branch has:

```text
route_c_residual.candidate.json,
rhoE_mesh.candidate.json,
rhoE_metric.candidate.json,
sector_maps.candidate.json,
de_action.candidate.json,
riesz_gap.candidate.json,
reduced_green.candidate.json,
dotd_response.candidate.json.
```

## What Was Constructed

The smoke package uses:

```text
mesh_N = 1,
identity rho_E,
identity Hermitian metric,
family projectors Q,u,d,L,e,N = I_3,
H projector = rank-one line,
finite D_E with kernel dimension 3 for family sectors,
finite D_E with kernel dimension 1 for H,
Riesz projectors onto the zero-mode clusters,
reduced Green inverse on the complement,
nonzero branch-phased dotD_alpha1 responses.
```

The dotD response is branch-phased by the finite CP character:

```text
q=79  branch uses chi_79,
q=369 branch uses chi_369 = conjugate(chi_79).
```

This means the two branches are not merely empty labels in the files.  Their
finite response packets are conjugate at the dotD-response level.

## Validator Outcome

For the honest saved candidate files:

```text
rhoE_mesh      PASS,
rhoE_metric    PASS,
sector_maps    PASS,
route_c        FAIL only because selected_source_verified is false,
D_E            FAIL only because selected_source_verified is false,
Riesz/Green    FAIL only because selected_source_verified is false,
dotD           FAIL because selected_dotD_source_verified and alpha1_driver_verified are false.
```

For a temporary algebraic smoke run where only the selected-origin flags are
lifted:

```text
all Route C, rho_E, metric, sector, D_E, Riesz, Green, and dotD validators PASS
for both conjugate branches.
```

This is a useful computational result.  It proves that the branch-aware finite
pipeline is internally coherent and that the two conjugate packets can be
threaded through every validator.

## What It Does Not Prove

It does not prove:

```text
a selected rho_E,
a selected HYM/Strominger residual solve,
a selected D_E,
a selected dotD_alpha1,
primitive C1 contractions,
Yukawa matrices,
full SM closure.
```

The residual values in this attempt are smoke residuals, not a solved
HYM/Strominger source certificate.  Identity `rho_E` is a schema carrier, not a
selected twisted bundle.

## Meaning

The computational frontier moved one layer forward:

```text
before: unknown whether the branch-aware Route C schema can carry the full finite pipeline;
now: yes, it can, for both conjugate branches.
```

The remaining blocker is no longer a schema or finite-linear-algebra blocker.
It is the real source problem:

```text
replace the smoke residuals and identity rho_E
with a genuine finite HYM/Strominger residual solve,
then justify selected_source_verified.
```
