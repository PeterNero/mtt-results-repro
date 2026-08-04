# Iwasawa rho_E Source Recovery Attempt

## Purpose

The bundle finite-element contract reduced the next missing input to:

```text
rho_E(g_j,z), j=1..6,
```

the rank-three transition matrices for the candidate Iwasawa deck generators.

This note asks whether the current corpus already supplies those matrices or
an equivalent selected source.

The result is:

```text
IWASAWA_RHOE_SOURCE_RECOVERY_BLOCKED_SELECTED_TRANSITIONS_MISSING.
```

## What Is Recovered

The corpus and current certificates recover:

```text
rank-three bundle target,
topological monad sequence,
line-bundle Chern labels,
c1(E)=0,
ch2(E)=0,
integral c3(E)=6,
abstract stable-bundle/HYM existence route,
bundle finite-element rho_E input contract.
```

These are real structural inputs.  They are not yet transition matrices.

## What Is Not Recovered

The current corpus does not supply:

```text
rho_E(g1,z),
rho_E(g2,z),
rho_E(g3,z),
rho_E(g4,z),
rho_E(g5,z),
rho_E(g6,z),

transition functions for L_i,K1,K2,
Cech cover and cocycle data,
typed f_i and g_i section representatives,
rho_E cocycle/path-independence certificate,
rho_E Hermitian metric compatibility certificate,
sector projection maps Q,u,d,L,e,N,H,
selected D_E action on the rho_E-glued basis.
```

So the template:

```text
certificates/iwasawa_bundle_rhoE_data.template.json
```

correctly remains open.

## Route Evaluation

### R1: Corrected A01 Or Connection

This route would produce a selected connection, hence parallel transport or
transition functions in a chosen frame.

Current status:

```text
blocked.
```

The selected `D_E` construction attempt already showed:

```text
literal printed A01 is not integrable,
invariant repairs are retired,
no corrected non-invariant connection coefficients are supplied.
```

### R2: Typed Monad/Cech Transitions

This is still mathematically the cleanest route. It would provide:

```text
line-bundle transition functions,
typed f_i and g_i sections,
Cech cocycles,
E = ker(g)/im(f),
rho_E induced on the quotient bundle.
```

Current status:

```text
blocked from current corpus.
```

The typed monad recovery attempt found the monad sequence and Chern labels, but
not the typed sections, transition functions, Cech cover, or `g o f = 0`
certificate.

### R3: Direct HYM/Strominger Solve

This route could produce `rho_E` and `D_E` by solving for the selected HYM
connection in a fixed topological sector.

Current status:

```text
abstract existence only.
```

The corpus supports stable-bundle/HYM existence as a theorem package. It does
not supply a computable connection, frame, holonomy, residual bound, or
transition-function evaluation rule.

## Invalid Shortcuts

The following are not allowed:

```text
rho_E = I_3
```

unless the selected bundle is proved globally trivial in the chosen frame.
The identity case is only a schema smoke test.

Also invalid:

```text
c1(E)=0 implies rho_E is trivial.
```

It does not. It is a determinant/topological condition, not a trivialization of
the rank-three bundle.

Also invalid:

```text
generic constant matrices in the left-invariant frame
```

as global maps without typed section and transition-function data.

Also invalid:

```text
q79 character = rho_E.
```

The q79 character restricts finite CP/channel support. It is not the full
rank-three bundle transition system.

## Minimal New Data

One of the following would close the `rho_E` blocker:

```text
1. explicit selected rho_E(g_j,z) for j=1..6 on the FE boundary targets,
   with cocycle and metric compatibility;

2. typed line-bundle transition functions plus typed monad sections f_i,g_i
   inducing rho_E on E=ker(g)/im(f);

3. a selected HYM/Strominger connection in a global or patched frame from
   which rho_E and D_E can be evaluated.
```

Then the computation becomes:

```text
bundle-glued FE basis,
Hermitian metric and quadrature,
selected D_E action,
Gram matrix G_N,
stiffness/operator matrix K_N or L_N,
Riesz projector and gap/error certificate.
```

## Verdict

The `rho_E` input contract is now closed, but the selected transition data are
not recovered from the current corpus.

This is a useful hard edge. The next successful proof step must provide
selected bundle transition data, not another abstract statement that a bundle
exists.

