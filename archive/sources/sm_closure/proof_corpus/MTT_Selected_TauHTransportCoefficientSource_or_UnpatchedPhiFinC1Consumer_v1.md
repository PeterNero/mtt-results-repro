# MTT Selected TauH Transport Coefficient Source or UnpatchedPhiFinC1Consumer v1

## Theorem

`TauHSourceRouteAndOneParameterReparamTheorem` is emitted.

## Result

The H radial layer can now be written as:

```text
r_H = pi^4 * tau_H
tau_H = 4.018017196377461
```

This preserves the counted H parameter:

```text
old parameter: UP-RET-OVERLAP.HRG = 391.39140285811936
new parameter: tau_H = 4.018017196377461
parameter count: 1
```

The improvement is that `pi^4` is no longer arbitrary: it is tied to the selected
`D_211/pi^2` normalization clue. Only `tau_H` remains empirical/controlled.

## Rejected Source Routes

```text
tau_H = 4:
  r_H = 389.6363641360097
  relative residual = 0.0044841013606674775

tau_H = -logdet(D_211):
  tau = 4.019441578939575
  r_H = 391.5301506687795
  relative residual = 0.00035449887158216383
```

Both are diagnostics only.

## Remaining Exact Target

The next non-looping target is one of:

1. derive `tau_H` from the unpatched differentiated `Phi_fin^C1` source rule;
2. export `tau_H` from honest selected Galerkin C1 tables;
3. emit a typed HRG consumer map from selected dynamic payload;
4. emit direct `K_threshold.Omega_H.lambda`.

## Next Artifact

`MTT_Selected_UnpatchedPhiFinC1SourceRule_or_HonestGalerkinTauHExport_v1`
