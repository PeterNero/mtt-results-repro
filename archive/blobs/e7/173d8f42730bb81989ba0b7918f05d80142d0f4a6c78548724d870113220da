# Selected Qa/SU3 Hessian Kernel Central Cocycle Derivation Interface v1

## Purpose

This is the executable interface for the derivation lane. It prevents a
Hessian/kernel argument from passing unless it supplies actual selected data.

## Required Objects

```text
H_sel    selected Hessian block on the Qa/SU3 c-twist/source sector
G_ret    retarded overlap or Green kernel on the admissible complement
Pi_tw    projection from Hessian/kernel data to twisted module labels
tau      central 2-cocycle/action extracted from H_sel and G_ret
response projective rho_E or D_E/dotD/Riesz/Green/heat/zeta/torsion payload
```

## Validator

```text
template: certificates\hessian_kernel_central_cocycle_derivation.template.json
validator: scripts\validate_hessian_kernel_central_cocycle_derivation.py
open-template exit code: 2
open-template output: open or incomplete fields: source_identity, hessian_block, retarded_kernel, twist_projection, tau_extraction, admissibility, response_payload, guardrails
```

The validator checks that a filled packet supplies all top-level data, refuses
target fitting and direct q79 import, and verifies the basic twist law:

```text
tau(F_i)+tau(G_i)=0 for i=1..5,
tau(P)=0.
```

It also requires the filled packet to carry the projective cocycle or response
payload from the same selected source.

## Verdict

```text
interface built: yes
validator built: yes
open template refuses to compute: yes
Qa/SU3 closed: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Hessian_Kernel_Central_Cocycle_Fill_Attempt_v1
```
