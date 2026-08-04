# QFT02 Gauge-Fixed Laplace and Interior Heat Kernel

Date: 2026-07-26

## Frontier result

`HK` is closed at the current boundaryless compact-support formal tier.

The proof makes one necessary correction: the compact-resolvent adjoint
Hodge sum built from the order-\((1,2,1)\) Maxwell detour complex is not
Laplace type. Its transverse symbol scales by `16` when the covector doubles,
not by `4`.

The corrected heat operator is the blockwise Euclideanized
background-Feynman-gauge Hessian. Exact rational checks prove a common
`|xi|^2 id` principal symbol for gauge, Higgs and squared-Weyl BV blocks.

## Boundary result

For compact interaction support a positive distance from the auxiliary
boundary, the boundary correction is `O(t^infinity)`. Therefore:

- local UV coefficients are independent of the auxiliary boundary;
- counterterms remain supported away from that boundary;
- local UV `GLUE` is derived from support preservation after counterterm
  construction.

The unsmeared APS trace is separately and honestly classified as a
power/power-log expansion with potentially nonlocal boundary coefficients.

## Corrected remaining bridge

Two independent packages remain:

1. `CT`: graphwise heat counterterms, BRST primitives and equicausal Cauchy
   induction;
2. `EL`: Euclidean-to-Lorentzian comparison with the existing
   Epstein-Glaser prescription.

The second package was previously hidden by an invalid use of
Stueckelberg-Petermann comparison as though it were a Wick-rotation theorem.
The auxiliary coframe flip has never been promoted to physical Wick
rotation.

## Verification

The generated certificate contains 46 checks before canonical composition.

```powershell
python -m unittest tests.test_qm_source.QmSourceTestCase.test_gaugefixed_laplace_operator_closes_local_HK -v
python scripts/verify.py
```
