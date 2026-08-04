# Selected Gauge-Factor Spectral Table Candidate v1

## Purpose

This note implements the first concrete spectral-table pipeline for the
remaining electroweak local determinant gate.

The target object is:

```text
Selected_Gauge_Factor_Spectral_Table_v1
```

with entries:

```text
{lambda_{a,j}, m_{a,j}, w_{a,j}} for a in {U1, SU2, SU3}.
```

## Selected Scaffold

The generator uses the selected q79/Theta scaffold:

```text
N = 79,
R1 = 0.5397189300902845,
(f2 R_lens)^2 = 0.280 R1,
c_nil = 1.439 R1.
```

## Operator Profile

The diagnostic operator profile is:

```text
U1:
  circle scalar Laplacian,
  lambda_n = n^2/R1^2,
  multiplicity = 2 for n >= 1.

SU2:
  effective round S2/lens scalar Laplacian,
  lambda_ell = ell(ell+1)/(0.280 R1),
  multiplicity = 2 ell + 1.

SU3:
  compact Nil scalar Laplacian diagnostic,
  exact p=0 torus sector plus p != 0 Landau lower-proxy.
```

All index weights are currently set to unit diagnostic weights.  This is not a
final threshold representation weight profile.

## Executable Pipeline

The generator is:

```text
scripts/generate_selected_gauge_factor_spectral_table.py
```

The cutoff scan is:

```text
scripts/scan_selected_spectral_table_cutoffs.py
```

The generated table plugs into:

```text
scripts/compute_selected_local_determinant_response.py
```

so the computation is now reproducible end to end.

## Why It Is Not Yet Final

The pipeline is useful because it exercises the whole determinant handoff.  It
is not a no-knob electroweak prediction because:

```text
1. the SU3 Nil p != 0 spectrum is not the exact compact spectrum;
2. the scalar Laplacian is a proxy for the true gauge threshold operator;
3. unit weights are placeholders for topology-certified gauge weights;
4. finite cutoff sums are not zeta/heat-kernel determinant finite parts.
```

The cutoff scan is expected to vary with cutoff.  That variation is not a bug;
it is the audit signal that regularization and exact spectral data are still
needed.

## Verdict

The spectral-table pipeline is now built.  The next required artifact is:

```text
Selected_Gauge_Factor_Zeta_Determinant_v1
```

which must replace the finite cutoff diagnostic with a selected zeta or
heat-kernel finite part and replace unit weights with topology-certified
weights.
