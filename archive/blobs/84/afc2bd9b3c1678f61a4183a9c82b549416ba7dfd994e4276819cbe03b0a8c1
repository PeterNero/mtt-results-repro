# Cross-Repo Primitive Row Adapter for Right-Channel Labels v1

## Question

Can the sibling SM-parity primitive C1 row packets provide the missing
right-channel label source for the finite mass-action operator?

## Imported packets

We test the support-level rows from:

`C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\candidate_data\selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution\inputs\primitive_contraction_terms.packet.json`

and the corresponding qutrit zero-mode basis from:

`C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\candidate_data\selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution\inputs\zero_mode_basis.packet.json`

The packets are not treated as a proof source.  Their own fields say
`selected_emitted=false` and `source_owner_verified=false`.  They are tested
only as an adapter clue for the next source-emission theorem.

## Adapter Test

For each of the `u` and `d` sectors, reconstruct the support-level phase and
shift matrices in the canonical qutrit basis.  Hermitianize them, project them
against the already selected weighted right-channel projectors, and ask whether
an affine source normalization can reproduce the required trace labels:

```text
up spin label:       (-1,+1)
down dyad label:     (+1,0)
down nil label:      (0,+1)
```

The affine test is deliberately weaker than proof.  Passing it would mean:
the row shape is compatible with the required labels after a finite source
normalization.  It would not mean the labels are selected by MTT geometry.

## Result

The imported primitive rows are useful but not closing.

They reconstruct nontrivial `u`/`d` row operators, so they are a real design
clue.  However, because their provenance is explicitly support-level residual
replay, they cannot be imported as `MTTFlavorRightChannelLabelRowEmission.v1`.

The proof frontier therefore stays:

```text
emit a same-source right-channel label row packet
or
promote the primitive-row source theorem so these rows become selected
```

## Correct Use

Allowed:

- use these rows to design the shape of the right-channel row-emission packet;
- use their qutrit pattern to guide the finite source basis;
- test whether their traces match the required label rows after a source
  normalization.

Not allowed:

- call them selected mass labels;
- use their residual replay values as an independent source;
- treat affine trace matching as no-proxy mass closure.

## Next Target

Create the adapter payload schema:

```text
MTTPrimitiveC1ToRightLabelAdapter.v1
```

It must name:

- source packet id and branch id;
- primitive row matrices used;
- right-channel projector basis;
- trace labels emitted;
- finite normalization rule;
- source-owner proof or independent quadrature/trace certificate;
- explicit flags excluding observed masses, CKM entries, and target fitting.

Until that source-owner field is closed, this is a strong construction clue,
not a theorem.
