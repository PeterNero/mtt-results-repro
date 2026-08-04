# Selected C1 Operator Source Rebuild Attempt v1

## Result

The selected C1 operator-source/Galerkin rebuild was attempted.

The attempt does not emit `A_selected` or `b_selected`.

It does close a useful audit:

```text
all candidate block sources classified: yes
diagnostic sources rejected as A_selected: yes
minimal rebuild payload specified: yes
target fitting used: no
```

## Slot Audit

The rebuild requires all of the following as selected finite data:

```text
selected source certificate,
selected non-identity rho_E or connection,
selected D_E/Riesz/Green/dotD,
selected alpha1 driver,
selected finite Hess_Xi blocks,
selected source vector b_selected,
selected zero-mode bases and Gram-Schmidt rule,
selected primitive C1 contractions,
selected sector response matrices.
```

Current artifacts provide support schemas, principal symbols, diagnostic finite
matrices, and model active operators. They do not provide the complete selected
finite block set.

## Rejected Shortcuts

The following cannot be promoted as proof sources:

```text
diagnostic non-invariant C1 candidates,
model-active B_N/D_E/dotD prefix,
q79 principal-symbol-only Hess_Xi template,
identity or unselected rho_E payload.
```

## Next Payload

The next artifact should fill:

```text
certificates/selected_routec_c1_operator_source_rebuild.payload.template.json
```

with selected finite blocks and theorem-derived source flags. Only then should
we run rank, consistency, DeltaTheta, mass-splitting, CKM/PMNS, and CP tests.
