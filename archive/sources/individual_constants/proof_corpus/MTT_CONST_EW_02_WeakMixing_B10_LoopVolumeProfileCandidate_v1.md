# MTT CONST EW 02 Weak Mixing B10 Loop Volume Profile Candidate v1

Status: `MTT_CONST_EW_02_B10_LOOP_VOLUME_PROFILE_CANDIDATE_FOUND_BRIDGE_OPEN`

Label: `CONST-EW-02 / WEAK-MIXING / B10-LOOP-VOLUME-PROFILE-CANDIDATE`

## Candidate Found

B9 reduced the no-threshold one-loop profile to:

```text
y = x*log(mu_Theta/MZ)/(8*pi^2)
```

The alpha1/metrology branch already emits:

```text
inv_sqrt_tau_int = sqrt(15/log(448)) = 1.5675093859261626
```

The clean source-side candidate is therefore:

```text
y_loop = sqrt(15/log(448))/(8*pi^2) = 0.019852738294064105
```

Inserted into the B9 no-threshold one-loop formula, this would give:

```text
sin2_if_bridge_holds = 0.2315309482915084
```

This is not promoted as a prediction.  The bridge is still missing.

## Required Bridge

`SelectedEWLoopVolumeProfileBridge`:

```text
x*log(mu_Theta/MZ) = sqrt(15/log(448))
```

or equivalently:

```text
K_EW[B]_profile = sqrt(15/log(448))/(8*pi^2)
```

## Guardrail

The candidate was selected from existing source-side alpha1/metrology data and
the universal one-loop volume.  It was not selected from the observed weak
angle.  Its numerical behavior is a reason to attack the bridge lemma, not a
proof of closure.

## Next

`CONST-EW-02 / WEAK-MIXING / B11-PROVE-xL-EQUALS-inv_sqrt_tau`
