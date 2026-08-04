# MTT Selected TransportClosedPhiFinFiniteReplay or SymbolicConjugationValidator v1

Status: `MTT_SELECTED_TRANSPORTCLOSEDPHIFINFINITE_REPLAY_OR_SYMBOLICCONJUGATIONVALIDATOR_BUILT_SYMBOLIC_FINITE_MORPHISM_VALIDATES_UNPATCHED_SOURCE`.

## What Closed

The raw `B_N` Fourier truncation is not closed under multiplication by
`U=exp(-u ad(T3))`, so this artifact takes the other accepted route: exact
symbolic transport conjugation.

It emits the finite-rank symbolic quotient `Q_sel^U`, with relations

```text
U^-1 U = I
P_s^sel = U P_s^model U^-1
G_s^sel = U G_s^model U^-1
Tr_Frob^U(U A U^-1) = Tr_Frob(A)
```

The new symbolic validator passes, and the strict physical-source validator
passes for a premise-free Route A certificate.

## Guardrail

Raw 27-mode closure is still not claimed:

```text
direct truncated relative residual = 0.23373530261576297
gauge-frame residual              = 8.863447760090952e-16
```

So the closure is exact in the symbolic finite quotient `Q_sel^U`, not in the
old raw Fourier basis.

## Next

`MTT_Selected_UnpatchedSourcePromotionReplay_or_FullSMClosureGate_v1`.

The finite source gate now validates. Next we should replay the upstream
promotion chain and see whether `A_selected`, `b_selected`, and
`deltaTheta_C1` promote through all prior gates.
