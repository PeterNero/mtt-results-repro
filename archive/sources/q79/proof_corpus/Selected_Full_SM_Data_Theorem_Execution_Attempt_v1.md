# Selected Full SM Data Theorem: Execution Attempt

## Requested Theorem

The target theorem is:

```text
Selected Full SM Data Theorem
=============================

From the selected q79 / Theta / Iwasawa branch, compute the actual selected
raw and canonical Yukawa matrices, neutral-sector mass data, Higgs boundary
data, and RG/threshold matching, without using benchmark entries or observed
SM masses and mixings as inputs.
```

I attempted to execute this theorem against the current certificate set and the
available MTT corpus.

The result is:

```text
SELECTED_FULL_SM_DATA_THEOREM_NOT_PROVED_SELECTED_DATA_ABSENT.
```

This is not a conceptual dismissal of the program.  It is a precise
underdetermination result for the current artifacts.

## Data That Can Be Used

The following selected data are usable:

```text
q = 79 mod 448,
mu_Theta = 5 TeV,
I2/I1 = 0.560,
I3/I1 = 0.229,
lambda_123 = 1 rank-one Iwasawa tree seed,
E6 -> SM operator dictionary,
single low-energy Higgs projection H_u -> H, H_d -> H^dagger,
finite Gamma_u, Gamma_d, Gamma_e, Gamma_nuD channel sets,
q79/conjugate support only on C6 channels,
C0 tree block A=1, S=0, chi=1, representative E33,
pure C6 character values with S=0,
C1 alpha_1 curvature support,
C1 rank-lift criterion,
CKM leading noncommutation criterion,
Jarlskog closure criterion.
```

These data define the *domain* and the *tests* for the selected SM-data
calculation.  They do not define the missing numerical matrices.

## Data That Must Not Be Used

The Execution II matrices are useful benchmarks, but they are not selected
no-proxy data.  They include local flavor inputs such as benchmark singular
values, local instanton factors, a Majorana scale, a representative `tan beta`,
and mixing rotations.

Those data are rejected as theorem inputs because the no-proxy rule forbids:

```text
benchmark Yukawa entries,
observed masses,
observed CKM or PMNS angles,
entry-local phases,
entry-local distances,
post-hoc threshold choices.
```

They can be used only after a selected overlap-kernel and matching certificate
has frozen the predicted matrices.

## Conditional Computation Map

If the selected data were supplied, the computation would be standard and
mechanical.

For each sector `s in {u,d,e,nuD}`, the raw matrix would be:

```text
Y_s_raw
  = y0_s E33
    + sum_{gamma in Gamma_s minus C0}
        A_{s,gamma} exp(-S_{s,gamma}) chi_{s,gamma}.
```

Here:

```text
A_{s,gamma}
  is the selected overlap prefactor;

S_{s,gamma}
  is the selected action, distance, spectral, flux, or closure-strain cost;

chi_{s,gamma}
  is fixed by the q79 channel rule.
```

The canonical matrices would then be computed from the selected kinetic
metrics:

```text
Y_s_can = K_L_s^{-1/2} Y_s_raw K_R_s^{-1/2},
```

up to the selected Higgs-normalization convention.

For quarks:

```text
H_u = Y_u_can Y_u_can^dagger,
H_d = Y_d_can Y_d_can^dagger,
V_CKM = U_u^dagger U_d,
Delta_CP = Im det([H_u,H_d]).
```

For neutrinos, one must first select whether the neutral sector is Dirac,
Majorana, or seesaw.  Only then can the effective light-neutrino matrix and
PMNS matrix be computed.

For low-energy comparison, all selected high-scale data must be run through a
predeclared RG and threshold scheme.

## Why The Theorem Cannot Be Proved Yet

The current certificates do not supply:

```text
M_C1^(alpha1) entries,
selected V_C1,
Hess_Xi blocks,
dotD operators,
zero-mode contractions,
nontrivial A_gamma values,
nontrivial S_gamma values,
C6 amplitudes and orientations,
family kinetic metrics,
neutral-sector operator,
Higgs quartic/VEV boundary data,
RG threshold spectrum and scheme.
```

Without these, the actual matrices are not determined.

## Underdetermination Witness

The current C1 rank criterion says:

```text
det(E33 + epsilon M)
  = epsilon^2 (M11*M22 - M12*M21)
    + epsilon^3 det(M).
```

So the leading rank-lift test is:

```text
C33(M) = M11*M22 - M12*M21 != 0.
```

But the current certificates do not determine the entries of `M`.  For example,
both light-family blocks:

```text
completion A:
  [[1,0],
   [0,1]]
  C33 = 1

completion B:
  [[2,0],
   [0,1]]
  C33 = 2
```

pass the already-closed nonzero rank-lift criterion, but they yield different
light-family singular values.  The present proof stack does not choose between
them.

Similarly, the leading CKM noncommutation criterion says:

```text
Delta_v = (M_d13 - M_u13, M_d23 - M_u23) != (0,0).
```

Both:

```text
Delta_v = (1,0),
Delta_v = (0,1)
```

pass the noncommutation test, but they correspond to different leading mixing
orientations.  The current proof stack does not choose between them.

Thus the open data are not cosmetic.  They are mathematically necessary.

## The Executable Conclusion

The selected q79 branch currently proves a strong structural route:

```text
finite CP branch,
rank-one seed,
SM operator dictionary,
single-Higgs low-energy projection,
finite channel support,
q79 character restriction,
rank-lift and CP criteria.
```

It does not yet prove the Selected Full SM Data Theorem.

The next object must be:

```text
SelectedOverlapKernelAndMetricDataCertificate
```

supplying:

```text
1. all selected A_gamma and S_gamma values;
2. all selected C1 response matrices or another selected rank-lift source;
3. selected family kinetic metrics;
4. selected neutral-sector operator;
5. selected Higgs boundary data;
6. predeclared RG/threshold matching.
```

Only after that certificate exists can the actual selected matrices be
computed and compared with the Standard Model.
