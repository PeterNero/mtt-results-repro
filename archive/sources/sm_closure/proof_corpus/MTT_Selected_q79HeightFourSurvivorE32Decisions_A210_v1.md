# MTT Selected q79 Height-Four Survivor E32 Decisions A210 v1

## Result

A210 applies the A207 E32 interval logic to every height-four row retained by
A208. It combines canonically oriented raw-thimble intervals, the A209 primitive
handle combinations, and the same refined beta interval.

| A132 rank | candidate | residual center | radius | decision |
|---:|---|---|---:|---|
| 1 | `b2d40611a5b6ee69` | {'real': '-0.0028546742907991705', 'imaginary': '-0.0047070008760710996'} | 0.00565465183 | REJECTED_BY_A207_SHARPER_DIRECT_HANDLE_INTERVAL |
| 2 | `9ac6f799790741e6` | {'real': '-0.0037815392451720242', 'imaginary': '-0.0032926676360795024'} | 0.0103785209 | NOT_SEPARATED_BY_CURRENT_E32_INTERVAL |
| 3 | `5224d7bf54fb9115` | {'real': '-4.4071604249039997e-06', 'imaginary': '0.00015846606390946101'} | 0.0166078413 | NOT_SEPARATED_BY_CURRENT_E32_INTERVAL |
| 4 | `54ed4988d883b0cc` | {'real': '0.00044165884836532899', 'imaginary': '0.0025938544294498047'} | 0.0117816253 | NOT_SEPARATED_BY_CURRENT_E32_INTERVAL |
| 5 | `df1934b78f6111ac` | {'real': '0.00033444635587092248', 'imaginary': '0.0028849369459561791'} | 0.00494806849 | NOT_SEPARATED_BY_CURRENT_E32_INTERVAL |

The ledger now has one preserved A207 rejection, 0 new
survivor rejection(s), and 4 E32-nonseparated
survivor(s). Nonseparation means only that the current E32 interval contains
zero; it is not promoted to equality or to a covariant solution.

The result is complete for the five rows emitted by the finite A132 grid, not
for all of `Z^90`. No observed Standard Model value is used.
