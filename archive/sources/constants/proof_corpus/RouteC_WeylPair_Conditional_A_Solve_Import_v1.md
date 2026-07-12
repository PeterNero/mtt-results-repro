# RouteC WeylPair Conditional A Solve Import v1

Status: `ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_IMPORTED_SOURCE_PROVENANCE_OPEN`.

Primitive-only basis transport is now a counterexample branch: its span does
not contain the locked 72-real qutrit/Weyl splitter target.  The enriched
Weyl-pair packet fixes that algebraic obstruction.

Conditioned on source provenance, the imported operator has:

```text
shape                 = [72, 2]
rank                  = 2
condition_number      = 1.0000000000000002
deltaTheta_conditional = [1.0, 1.0000000000000002]
relative_residual     = 1.5700924586837752e-16
```

This operator is not promoted to `A_selected`: the source-provenance lemma still
has to prove that the selected q79/Route-C branch emits the phase-like and
shift-like Weyl-pair columns, and then emit `b_selected`.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `Q79_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1`.
