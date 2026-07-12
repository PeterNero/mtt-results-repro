# MTT Selected H Phase-Sign Selector: Lens-Circle or HRG Value Map v1

## Result

The binary H phase sign is now selected in the current finite-Weyl convention.

- Previous work reduced the Higgs off-diagonal phase to the imaginary axis, `phi_Omega in {+pi/2,-pi/2}`.
- The ordered Huv source basis is `(H_u,H_d^dagger)` on the same `q79/F,m=1` diagonal HYM lane.
- The q79 repo selects the time-oriented `F`, `m=1` finite lens-circle representative, with commutator matrix `[[0,1],[2,0]]`.
- The antiunitary conjugate `q369/F*`, `m=2` representative is retained and carries the conjugate commutator `[[0,2],[1,0]]`.

Therefore the selected time-oriented branch maps the binary imaginary axis to

```text
phi_Omega = +pi/2,
Hud = +i * |Omega|,
Hdu = -i * |Omega|.
```

The conjugate `-i` branch remains real as the antiunitary branch, but it is not the selected time-oriented branch.

## Guardrail

This uses lens/circle data only as an orientation/sign selector. It does not reuse the retired Lens-Nil numerical weight block.

## Remaining Frontier

`r_H` is still not promoted. Final strict Herm(2) value rows require a typed same-source HRG value map, an independent H radial action scale, or a selected finite-H Hessian radial norm.

New frontier:

```text
MTT_Selected_HRGValueSourceMap_or_HRadialActionScale_v1
```

