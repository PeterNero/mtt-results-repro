# MTT Selected Typed Family-Gauge Carrier and Diagonal SM Representation Theorem v1

## Cross-Repository Finding

This was partly done before, but never assembled as the object now required. The repositories
already contained the selected six-arrow SM-slot functor, the standard
`E6 -> SO(10) -> SU(5) -> SM` dictionary, the `Z3` family carrier, and structural
hypercharge/anomaly formulas. Older audits correctly refused closure because no single artifact
listed the selected chiral rows and evaluated every anomaly on those same rows.

## Typed Carrier

Using left-handed Weyl fields throughout,

```text
H_16 = Q + u^c + d^c + L + e^c + N^c,
H_chiral = C3_family tensor H_16,
rho_phys(g) = I3_family tensor rho_16(g).
```

The dimensions are `16` per family and `48` in total. All three family projectors commute
with every constructed gauge generator with residual `0.0`. This preserves the family factor
and fixes the type error identified in A45.

## Emitted Chiral Rows

```text
Q   : (3,2)_( 1/6) from 10_M
u^c : (bar3,1)_(-2/3) from 10_M
d^c : (bar3,1)_( 1/3) from bar5_M
L   : (1,2)_(-1/2) from bar5_M
e^c : (1,1)_( 1) from 10_M
N^c : (1,1)_( 0) from 1_M
```

The Higgs is the scalar row `(1,2)_(1/2)` and contributes no chiral anomaly.

## Exact Anomaly Execution

On three identical families the machine-evaluated coefficients are

```text
SU(3)^3            = 0
SU(3)^2 U(1)_Y     = 0
SU(2)^2 U(1)_Y     = 0
U(1)_Y^3           = 0
gravity^2 U(1)_Y   = 0
SU(2) doublets     = 12 = 0 mod 2
```

Thus the local gauge, mixed, gravitational, and global Witten anomaly tests all close on
the same family-preserving representation packet.

## Exact Scope

This closes the previously missing consolidated chiral representation and anomaly table. The
upstream source is genuinely bundle-derived: the selected rank-three `SU(3)` bundle in visible
`E8` leaves `E6` as commutant, its index gives three chiral `27`s, and the selected terminal
section-ring packet emits `10_M`, `bar5_M`, and `1_M`. The displayed E6/SO10/SU5/SM
decomposition is then exact representation theory.

What remains is narrower: a selected physical vacuum-breaking operator, Wilson line, holonomy,
or equivalent theorem proving that the selected E6 compactification realizes this low-energy
subgroup route rather than another admissible E6 route. This is one discrete physical selector,
not a fitted numerical knob. The full Connes finite bimodule including antiparticles, order-one,
orientation, and native unimodularity also remains open.

Next artifact: `MTT_Selected_NativeFlagToE6SMChiralModuleCompatibilityAndUnimodularityTheorem_v1`.
