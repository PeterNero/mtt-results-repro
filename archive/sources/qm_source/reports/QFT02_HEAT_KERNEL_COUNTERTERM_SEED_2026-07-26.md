# QFT02 Heat-Kernel Counterterm Seed

Date: 2026-07-26

## Result

The spectral-to-Epstein-Glaser bridge is no longer an undifferentiated
six-row request.

Closed exactly:

- a six-dimensional rational Hodge-complex heat-semigroup seed;
- regulated-propagator scale additivity;
- the finite BV homotopy identity;
- a normalized quadratic local-counterterm cocycle;
- the zero-anomaly all-orders QME induction cutset.

The exact certificate has 35 checks.

## Frontier delta

The six requirements reduce to three independent q79 tasks:

1. `HK`: verify the selected mixed gauge-Higgs-chiral boundary heat operator,
   polyhomogeneous expansion and microlocal remainder estimates;
2. `CT`: calculate the actual local coefficients and BRST primitives;
3. `GLUE`: prove compatibility of bulk and boundary coefficients with BV-BFV
   gluing.

Epstein-Glaser target identification then follows up to one finite local
Stueckelberg-Petermann map; it is not a fourth coefficient computation.

## Important boundary

The exact dyadic model is an algebraic regulator witness, not the q79
short-time heat expansion. The quadratic counterterm is a normalization and
cocycle witness, not the Standard-Model counterterm table. No fixed-coupling
or nonperturbative convergence is claimed.

## Reproduction

```powershell
python -m unittest tests.test_qm_source.QmSourceTestCase.test_heat_kernel_counterterm_seed_reduces_bridge_to_three_jobs -v
python scripts/verify.py
```
