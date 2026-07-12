# MTT Selected Neutral CRT Phase Typing and Proto-Spinor Nil-Drift Reduction v1

## CRT correction

The selected exact branch has `q64=15`, `q7=2`, and `q=79 mod 448`.
The isolated `Z7` residue is a phase fraction `2/7`. Its canonical CRT lift is
`128 mod 448`, hence `128/448=2/7`. It is not `2/448`.

The previously attractive calculation

```text
phi = 2*pi*(2/448)
r_NO(phi) = 0.03188132963123951
```

therefore mixed a `Z7` residue numerator with the full `Z448` denominator. It
is neither the local `Z7` character, its CRT lift, nor the selected global
`79/448` character. The numerical near-hit is retired as a source clue.

## Correct proto-spinor frontier

The proto-spinor corpus supplies the structurally appropriate neutrino family

```text
m_k^2 = m_0^2 + A cos(phi_nu + 2*pi*k/3),
r_NO = |sin(phi_nu)|/|sin(phi_nu+pi/3)|.
```

It explicitly treats the numerical realization as execution-level. The
remaining physical coordinates are therefore the genuine neutral nil-holonomy
`phi_nu` and one absolute scale `mu_nu`. A31 remains a valid no-go for promoting
the A29 `[1,4,7]` orbit by common scaling, but it does not exclude this distinct
proto-spinor nil-drift family.

Next artifact: `MTT_Selected_NeutralNilHolonomySourceAndAbsoluteScale_v1`.
