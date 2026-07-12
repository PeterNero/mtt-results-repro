# MTT SM Equivalence Mixing and Gauge Replay v1

Status: `MTT_SM_EQUIVALENCE_MIXING_AND_GAUGE_REPLAY_BUILT_PARTIAL_EMPIRICAL_REPLAY`.

This is a straight SM-standard measured replay after the source/interface
boundary is fixed.  The superset strategy is not used to tune the values.

What is emitted:

```text
CKM replay:  Y_u diagonal, Y_d = V_CKM diag(y_d)
PMNS replay: H_nu = U_PMNS diag(0, Delta_m21^2, Delta_m3l^2) U_PMNS^dagger
Gauge replay: alpha_1=(5/3) alpha_em/(1-sin^2 theta_W), alpha_2=alpha_em/sin^2 theta_W, alpha_3=alpha_s
```

Central gauge triplet at `M_Z`:

```text
alpha_1^GUT = 0.01694349460179486
alpha_2     = 0.03380110659969169
alpha_3     = 0.118
g_1^GUT     = 0.46143063689849223
g_2         = 0.6517340199093397
g_3         = 1.2177157847767197
```

Replay residuals:

```text
CKM unitarity residual         = 2.220446049250313e-16
CKM H_d reconstruction residual = 3.388131789115809e-21
PMNS unitarity residual        = 1.1102230246251565e-16
PMNS diagonalization residual  = 1.8472310776187047e-19
```

Still open:

```text
full CKM/PMNS covariance or profile policy
absolute neutrino mass and Dirac neutrino Yukawa magnitudes
common RG scale transport, loop order, and threshold policy
empirical equivalence audit
full SM-equivalence closure
full no-knob closure
```

Next artifact: `MTT_SM_Equivalence_Common_RG_and_Empirical_Audit_v1`.
