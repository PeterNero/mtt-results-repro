# MTT CONST EW 02 Weak Mixing Angle Source Frontier v1

Status: `MTT_CONST_EW_02_WEAK_MIXING_SOURCE_FRONTIER_BUILT_VALUE_OPEN`

Label: `CONST-EW-02 / WEAK-MIXING / B1-B3-SOURCE-FRONTIER`

## Result

The weak mixing angle is now opened as the second individual-constant branch.
The alpha1 handoff, electroweak formula map, and internal weak-split packet are
accepted as source support.

Imported internal values:

- `p_Y_internal = 1.4217420994950278`,
- `p_SU2_weaksplit = -1.1961941178318218`,
- `lambda_12_internal = 2.6179362173268497`,
- `Delta_G12_internal = 0.08450302790361214`.

This closes the target setup and internal split import.  It does not derive a
physical weak mixing angle.

## Formula Boundary

The target formula is

`sin^2(theta_W)(mu) = alpha_Y(mu)/(alpha_Y(mu)+alpha_2(mu))`.

Equivalently, with inverse couplings `AY=1/alpha_Y` and `A2=1/alpha_2`,

`sin^2(theta_W)(mu) = A2(mu)/(AY(mu)+A2(mu))`.

Therefore an internal weak split is not enough.  We still need the same-branch
physical `AY(mu)` and `A2(mu)` packet, including common anchor, scale, scheme,
and thresholds.

## Superset Use

We combine several encodings under a locked target:

- gauge-row path: U1/Y and SU2 source rows,
- mass-shell path: W/Z replay only as downstream parity check,
- RG path: scale/profile transport,
- one-universal-primitive path: only if the alpha1 primitive is selected
  target-independently and shared across sectors.

Forbidden shortcuts:

- backsolve from measured `sin^2(theta_W)`,
- identify `lambda_12_internal` directly with the physical angle,
- use W/Z masses as source selectors,
- claim `sin^2(theta_eff^l)` without the effective-profile `kappa` factor.

## Next

Next label: `CONST-EW-02 / WEAK-MIXING / B4-SU2-PHYSICAL-PACKET`.
