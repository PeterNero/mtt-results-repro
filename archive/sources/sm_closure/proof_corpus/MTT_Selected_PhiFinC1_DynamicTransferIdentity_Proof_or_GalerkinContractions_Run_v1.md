# MTT Selected PhiFinC1 DynamicTransferIdentity Proof or GalerkinContractions Run v1

Status: `MTT_SELECTED_PHIFINC1_DYNAMICTRANSFERIDENTITY_PROOF_OR_GALERKINCONTRACTIONS_RUN_BUILT_STATIONARY_TRACE_CLOSED_C1_OPEN`.

This artifact imports the symbolic transport-conjugation theorem into the
`Phi_fin^C1` proof target.

Closed now:

```text
P_s^sel = U P_s^model U^-1
G_s^sel = U G_s^model U^-1
rho_s selected-source validator ready
stationary projector/Riesz/Green/source layer closed
```

But this is a stationary trace theorem.  It does not emit the differentiated
`Phi_fin^C1` overlap/Hessian data:

```text
Phi_C1_selected(Z) = phase_packet
Phi_C1_selected(X) = shift_packet
b_selected         = phase_packet + shift_packet
G_selected         = 12 I_2
```

So the previous normal-form values remain conditional:

```text
A^T A         = [[12.0, 0.0], [0.0, 12.0]]
A^T b         = [12.0, 12.0]
deltaTheta_C1 = [1.0, 1.0]
```

The live target is now precise: emit a differentiated `Phi_fin^C1` packet with
the primitive overlap contractions, or run the honest selected Galerkin C1
contract and solve whatever selected equation it emits.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `MTT_Selected_DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_v1`.
