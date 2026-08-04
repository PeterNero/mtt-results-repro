# Selected Qa/SU3 Symmetry-Breaking Route Triage

## Result

The remaining `V_alpha/S3` selector problem is now routed.

The finite quotient and integral automorphy work are useful, but they do not
select the branch.  The wall route is also live, but the closed constants
radius imports as an equal-radius Iwasawa branch and therefore cannot be the
visible target wall.

The target wall is:

```text
p1:p2 = 1:2
r1:r2=sqrt(2):1
```

The constants/no-knob selected radius gives:

```text
p1:p2 = 1:1
r1 = r2
```

So the equal-radius import leaves the target and swapped branches degenerate.

## Route Ranking

1. `selected_orientation_carrying_D_E_dotD`

   This is the primary live route.  It can in principle break both the
   `m=1` versus `m=2` conjugate fork and the visible target-vs-swapped branch.
   The finite `D_E/dotD` response validator is already formulated; the missing
   object is selected operator data, not another validator.

2. `non_equal_radius_gauduchon_wall`

   Still live, but current corpus data do not supply the needed
   `r1:r2=sqrt(2):1` source.

3. `ordered_integral_cech_automorphy_source`

   Still live as a source-certificate gap.  The integral model exists; the
   selected source theorem does not.

4. `holonomy_sensitive_pic0_rule_only`

   Necessary, but not sufficient alone.  It must be paired with a branch
   selector or same-source operator packet.

## Next Object

The next packet should be:

```text
SelectedQaSU3OrientationCarryingDEDotDSource.v1
```

It must select one torsion label, bind it to the corresponding global CP label,
provide selected `D_E`, reduced Green, and `dotD_alpha1` data on the same
branch, and pass the finite response validator.  It must not use observed CP
sign, observed masses, or benchmark flavor matrices as inputs.  In particular,
the observed CP sign cannot be used as the branch selector.
