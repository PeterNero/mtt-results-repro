# MTT Selected SU2 Transport-Closed Finite Gauge Row and SU3 Native-Color Source Reduction v1

## SU2 Row Closure

The missing SU2 bridge was already present in the selected transport theorem, but had not been
applied to the gauge spectrum. The exact object is the transport-closed finite quotient
`Q_sel^U`, not raw multiplication inside the 27 Fourier modes:

```text
Delta_SU2^fin = U (Delta_F3xF3 tensor I_adSU2) U^-1.
```

The selected base spectrum is `0 (x1), g (x4), 2g (x4)` with
`g=4*pi^2/9`. Tensoring the three adjoint lanes and conjugating gives exactly

```text
0 (x3), 4*pi^2/9 (x12), 8*pi^2/9 (x12),
log det' = 43.8024754982987.
```

No scale is fitted or inserted: the gap belongs to the already-selected finite trace. Raw
Fourier multiplication remains non-closed and is not used. The SU2 row is therefore accepted,
moving spectrum readiness from `8/10` to `9/10`.

## SU3 HYM Repair Theorem

The printed heterotic matrix is not integrable. Among signed one-entry repairs of its `B2`
coefficient, the Heisenberg Maurer-Cartan relations uniquely force

```text
B1=sqrt(mu) E13,  B2=-sqrt(mu) E32,  B3=mu E12.
```

But this whole family is one complex-gauge orbit:

```text
G_mu=diag(sqrt(mu),mu^(-1/2),1) in SL3(C),
B_i(mu)=G_mu B_i(1) G_mu^-1.
```

With the Hermitian metric transported, its adjoint spectrum is independent of `mu` and equals
`0,0,1,1,3,3,3,3,4`. Thus `mu` is not a physical selector on this repaired family. The
two-dimensional holomorphic commutant also contradicts simplicity of the claimed stable bundle,
so neither the printed matrix nor this minimal repair is promoted as the color threshold source.

## Final SU3 Reduction

The direct low-energy color group is the automorphism `SU3` of the native rank-three Nil carrier.
The visible heterotic `SU3` bundle instead organizes the UV `E6` matter branch; it is not
automatically the low-energy color gauge Hessian. A background preserving the full native `SU3`
is central, hence zero in `su3`; a possible `Z3` holonomy acts trivially in the adjoint. The final
operator therefore reduces to

```text
1/2 log det'(Delta_1^Nil tensor I8) - log det'(Delta_0^Nil tensor I8).
```

The `p=0` cancellation is already exact. The old numerical `p!=0` value used
`c_nil=1.439 R1`, which belongs to the withdrawn 5 TeV profile; the revised `0.9948493 R1`
value is also calibrated from gauge rows. Neither is a strict selected source value.

Exactly one spectrum row remains. It needs a same-source native Nil metric/lattice/scale and one
full gauge-fixed Hessian calculation deciding whether the `-11/3 C2` heat weight factorizes from
the internal determinant. Only then can a rigorous zeta/heat finite part or exact finite projected
operator be inserted without counting BRST twice.

Next artifact: `MTT_Selected_SU3NativeColorAdjointNilHodgeSourceIdentity_or_NewEndomorphismOperator_v1`.
