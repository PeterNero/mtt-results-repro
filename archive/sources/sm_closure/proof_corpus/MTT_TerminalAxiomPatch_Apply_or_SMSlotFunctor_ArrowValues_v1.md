# MTT TerminalAxiomPatch Apply or SMSlotFunctor ArrowValues v1

Status: `MTT_TERMINAL_AXIOM_PATCH_APPLIED_CORPUS_AND_SPINE_TERMINAL_SOURCE_CLOSED_SMSLOT_ARROWS_OPEN`.

## Result

Route A is now applied inside the local proof spine and verified in the target
Obsidian corpus papers: the `TerminalAdmissibleSectionSelectionAxiom` is an
explicit patched-spine axiom with matching corpus insertions. Under that patched
spine and patched corpus, the terminal replay is unconditional:

```text
selected source = g3 / L3-K2
L               = (1,-2,0)
L^2             = (2,-4,0)
c2              = (4,0,0)
h1 Ext packet   = 8, nonzero
```

The ordered-source and cohomology validators are therefore no longer merely
conditional on an external principle inside this proof spine.

## Boundary

This does not emit selected SM-slot functor values.  Route B remains open at the
same six arrows:

1. terminal Ext source -> `10_M` clock row;
2. terminal Ext source -> `bar5_M` shift row;
3. terminal Ext source -> `1_M=N^c` Dirac row;
4. selected `U_10=I_3`, `U_bar5=F` source outputs;
5. selected overlap/transfer normalization;
6. same-source consistency map.

No observed constants, benchmark targets, or locked C1 columns are used.

Next artifact: `MTT_SelectedSMSlotFunctor_SixArrow_SourceEmission_v1`.
