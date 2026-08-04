# MTT Selected FiniteEmissionMorphismPhiFinRestrictionProof or RouteBProvenanceExecution v1

Status: `MTT_SELECTED_FINITEEMISSIONMORPHISMPHIFINRESTRICTIONPROOF_OR_ROUTEBPROVENANCEEXECUTION_BUILT_FUNCTIONAL_RESTRICTION_PROVED_FINITE_REPLAY_OPEN`.

## Result

The target was attacked directly. The selected gauge-transported `Phi_fin`
trace proves the functional/minimizer side:

```text
K_s^sel = U K_s^model
P_s^sel = U P_s^model U^-1
U = exp(-u ad(T3))
```

This matches the constructed restriction map:

```text
res_C1_to_selected_finite_Weyl_quotient(delta S_phys) = Tr_Frob(Phi_fin(delta S_phys)|Q_sel)
```

So the selected Strominger/HYM branch now emits the correct restriction map at
the function-space level.

## Why this is not full unpatched closure

The finite emission morphism is still not premise-free. The gauge-frame replay
is exact, but the raw 27-mode `B_N` truncation is not transport-closed:

```text
direct truncated relative residual = 0.23373530261576297
gauge-frame residual              = 8.863447760090952e-16
```

The conditional Route A certificate still passes, but the unpatched Route A
attempt still rejects. That is the correct behavior: the functional theorem is
proved; the finite replay/promotion theorem remains open.

## Next object

`MTT_Selected_TransportClosedPhiFinFiniteReplay_or_SymbolicConjugationValidator_v1`.

It must either emit a transport-closed finite `Phi_fin` replay, add an exact
symbolic transport-conjugation validator, or complete Route B independent
provenance with exactness/error certificates.
