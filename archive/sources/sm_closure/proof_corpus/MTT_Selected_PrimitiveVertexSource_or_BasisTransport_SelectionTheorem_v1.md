# MTT Selected PrimitiveVertexSource or BasisTransport SelectionTheorem v1

Status: `MTT_SELECTED_PRIMITIVEVERTEX_SOURCE_OR_BASISTRANSPORT_SELECTIONTHEOREM_BUILT_SOURCE_SELECTOR_CLOSED_VALUES_OPEN`.

This artifact promotes the source selector for the differentiated `Phi_fin^C1`
primitive-overlap template.

Selected selector:

```text
Z / clock / phase  -> u,e
X / shift          -> d,nuD
active deck shift  -> (1,1)
fixed fiber class  -> 0,1,2 quotient class
1_M=N^c            -> shift / Dirac-neutrino side
```

It uses the selected S3/GS qutrit Weyl carrier, the selected SM-slot functor
source arrows, the selected static trace normalization, and the theorem-derived
alpha1/dotD replay.

This does not emit primitive overlap values.  The next artifact must fill the
template by evaluating the selected primitive vertex/basis-transport
contractions, or by running an honest selected Galerkin C1 solve.

Selector packet: `candidate_data/selected_primitivevertex_source_or_basistransport_selectiontheorem/primitive_vertex_source_selector.packet.json`.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `MTT_Selected_PrimitiveOverlapContractions_ValueEmission_or_HonestGalerkinRun_v1`.
