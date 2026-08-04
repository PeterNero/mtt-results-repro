# Selected Matter Payload Import Interface v1

## Result

The next remaining gate has been turned into an executable interface.

The GR repo already has the universal variational stress form:

```text
T_{mu nu} = -2/sqrt(-g) * delta S_matter / delta g^{mu nu}
```

What is missing is not the stress-tensor definition. What is missing is the
same-branch selected matter payload that supplies the scalar, Yang-Mills, Dirac,
Yukawa, neutral/Higgs, and matching coefficients that feed that definition.

## Required Payload

```text
selected source branch
selected sector projectors and zero-mode bases
selected D_E, Riesz/Green, and dotD values
finite C1 Hessian blocks and deltaTheta response
primitive overlap contractions
family kinetic metrics
neutral-sector, Higgs, and matching data
```

The q79 and sm-parity repos provide support shapes and validators for these
objects. They do not yet emit the selected values.

## What This Closes

This closes the interface between the selected matter/source program and the GR
stress-response program. It tells us exactly what must be imported before the
selected full matter stress coefficient gate can close.

## What Remains Open

The template in:

```text
candidate_data/selected_matter_payload_import_interface.template.json
```

must be filled with selected same-branch values. Until then, the universal
stress forms are closed, but the selected matter stress coefficients are open.
