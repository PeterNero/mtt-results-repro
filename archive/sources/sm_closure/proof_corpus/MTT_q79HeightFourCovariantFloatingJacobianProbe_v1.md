# MTT q79 Height-Four Covariant Floating Jacobian Probe v1

This artifact computes the same-source central finite difference of

`F(A,m)=beta(A)-Pi(A)m`

using a moving selected beta branch, moving critical values, 86 moving thimble
columns, the moving marked fiber basis, and moving A/B handles. It currently
contains 8 of 8 real PGL3 directions.

| A132 rank | center replay max | real rank | center L2 | linearized L2 |
|---:|---:|---:|---:|---:|
| 2 | 2.311e-08 | 8 | 0.0116149 | 0.00864623 |
| 3 | 2.335e-08 | 8 | 0.0141755 | 0.00589842 |
| 4 | 2.459e-08 | 8 | 0.01239 | 0.00501941 |
| 5 | 4.193e-08 | 8 | 0.0132709 | 0.0116318 |

This is a floating derivative probe, not an interval Jacobian certificate or a
covariant zero proof. The fixed handle representatives are required to remain
in the same Picard-Lefschetz chamber for every signed sample.
