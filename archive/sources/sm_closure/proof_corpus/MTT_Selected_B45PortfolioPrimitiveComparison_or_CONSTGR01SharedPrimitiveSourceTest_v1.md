# MTT Selected B45 Portfolio Primitive Comparison or CONST-GR-01 Shared Primitive Source Test v1

Status: `MTT_SELECTED_B45PORTFOLIOPRIMITIVECOMPARISON_OR_CONSTGR01SHAREDPRIMITIVESOURCETEST_G4_IMPORTED_HRG_SEPARATED_METROLOGY_OPEN`

## Result

This packet imports the actual next result after B45: CONST-GR-01 has already
advanced through G4.

```text
B45 = MTT_CONST_EW_02_B45_UNIVERSAL_PRIMITIVE_PORTFOLIO_HANDOFF_BUILT
G4  = MTT_CONST_GR_01_G4_OMEGA0_OR_ONE_METROLOGY_PRIMITIVE_BUILT
```

G4 closes the relative physical-scale solution and defines a
one-universal-metrology-primitive tier, but it does **not** select the physical
value:

```text
relative physical scale closed = True
one metrology primitive tier   = True
selected metrology values now  = 0
Newton/Planck prediction now   = false
```

The key G4 formulae now imported are:

```text
tau_int = 0.40698621549433234
Omega0/sqrt(alpha_phys) = 1.5675093859261626
G_eff(L0) = 0.29759362932431804 * L0^2
G_eff(E0) = 0.29759362932431804 / E0^2
```

## Separation

`UP-ABS-SCALE` and `UP-RET-OVERLAP.HRG` are not the same object in the current
typed ledger.

```text
UP-ABS-SCALE       = dimensionful metrology conversion: E0/L0/Omega0/T0
UP-RET-OVERLAP.HRG = dimensionless threshold/RG multiplier
HRG value           = 391.39140285811936
log(HRG)            = 5.969708089616292
```

No selected typed identity theorem currently maps the HRG value to
`E0/L0/Omega0`.  A deeper identity theorem is not ruled out, but until it is
supplied the ledger must not count HRG as already paid for by the metrology
primitive.

## Portfolio After This Cut

If HRG is retained, the current legal portfolio is:

```text
1. UP-ABS-SCALE: G4 metrology primitive tier, value open.
2. UP-RET-OVERLAP.HRG: H-threshold retarded-overlap candidate, strict source open.
```

That is not an ordinary fitted H knob: the controlled empirical HRG layer is
recorded, but it gives no no-knob or prediction credit for `lambda_H`.  It also
does not close true SM equivalence.

## What Actually Moved

- B45/G4 is no longer an unexamined pointer; it is imported into this repo.
- The silent one-primitive-does-everything route is rejected for the current
  formal ledger.
- The next non-looping target is sharpened to either a Higgs shared-metrology
  handoff or a strict HRG source/admission theorem.

## Next

`MTT_Selected_HiggsSharedMetrologyPrimitiveHandoff_or_HRGSourceTheoremReentry_v1`
