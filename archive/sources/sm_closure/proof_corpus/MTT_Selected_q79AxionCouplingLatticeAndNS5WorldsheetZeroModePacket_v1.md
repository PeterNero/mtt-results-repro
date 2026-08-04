# MTT Selected q79 Axion Coupling Lattice and NS5/Worldsheet Zero-Mode Packet v1

## Exact `E8 x E8` reduction

Let

```text
v_i = integral_X beta_i wedge tr(F1_bar^2),
h_i = integral_X beta_i wedge tr(F2_bar^2),
r_i = integral_X beta_i wedge tr(R_bar^2).
```

The smooth source-free Fu--Yau Bianchi identity is `r_i=v_i+h_i`. Reducing
the heterotic `B2 wedge X8` polynomial therefore gives

```text
E8_1: -r_i+4v_i-2h_i = +3(v_i-h_i),
E8_2: -r_i+4h_i-2v_i = -3(v_i-h_i).
```

This removes A99's unnecessary flat-hidden-bundle hypothesis. It closes the
full structural row formula, but not the selected integral numbers: the q79
packet still does not emit an integral `beta_i` basis or the two characteristic
vectors `v_i,h_i`.

## NS5 span obstruction

In the axion basis `Theta=(theta_MI,b_i)`, write `d_i=v_i-h_i`. The primitive
rows are

```text
k_vis  = (1,+3d_i),
k_hid  = (1,-3d_i),
k_NS5  = (1,0,...,0).
```

Hence

```text
k_vis+k_hid=2 k_NS5.
```

This proves a sharp no-go: a direction annihilated by both the hidden gauge
row and the wrapped-NS5 row is also annihilated by the visible/QCD row. The
A99 hidden-only cancellation remains correct, but it solves quality only if
the NS5 contribution is absent or passes the A98 suppression bound. More
model-dependent axions alone do not evade this identity.

## Fu--Yau worldsheet gate

A rational worldsheet curve cannot lie vertically in a complex torus fiber.
If a rational curve in the Fu--Yau total space projects to `C` in K3, its lift
is a section of the restricted principal `T2` bundle. Therefore the necessary
integral conditions are

```text
integral_C omega_1 = integral_C omega_2 = 0.
```

Topological triviality is not by itself sufficient. A superpotential term also
requires a smooth isolated rational lift and a nonzero Pfaffian. For the bundle
restriction the exact individual zero-mode test is

```text
H0(C,V|C tensor O_C(-1)) = 0  <=>  the Pfaffian is not forced to vanish.
```

The selected torus classes, effective rational curves, lifts, bundle
restrictions and Pfaffians are not present in the q79 corpus, so no worldsheet
amplitude is promoted.

There is nevertheless an exact quality simplification. For an arbitrary
worldsheet potential `W_ws(b_i)`, the full worldsheet-plus-QCD potential is

```text
V = W_ws(b_i)
    + chi_QCD [1-cos(theta_MI+3 d_i b_i+theta_bar)].
```

For every fixed `b_i`, the primitive surviving `theta_MI` sets the QCD angle to
zero. Thus worldsheet instantons alone have perfect direct strong-CP quality,
independently of their actions or Pfaffians. Their detailed rows remain needed
for the mass spectrum and for a hidden-sector cancellation route, but they are
not an independent direct quality blocker.

There is also a clean conditional vanishing branch. If the selected K3 lies in
the minimal Picard stratum generated over `Q` by the ample class and the torus
Chern span, the common algebraic orthogonal is positive and contains no `-2`
rational-curve class. That generic stratum has no rational worldsheet lift, but
the current q79 certificate does not yet select its Picard rank.

## NS5 quality kernel

The primitive Euclidean NS5 wraps the full selected `X6`, has charge row
`(1,0,...,0)`, and has action

```text
S_NS5 = 2 pi / alpha_GUT.
```

This fills the wrapped cycle and action formula structurally (`2/9` A98 source
fields), but selected numerical amplitudes remain `0/9`. The recent heterotic
EFT forms are proportional to

```text
A_NS5 m_3/2 M_GUT^3 exp(-S_NS5)
```

for a superpotential contribution and approximately

```text
m_3/2^2 M_s^2 exp(-S_NS5)
```

for a Kahler-potential contribution. A superpotential Pfaffian zero alone is
therefore insufficient; both contributions must vanish or their combined
`M0,M1,M2` norms must pass A98.

## Honest frontier

This packet closes new theorems without adding a parameter, but it does not
close strong CP. Strict same-source readiness remains `0/6` because the six
fields require selected integral values and amplitudes, not only their exact
formulas. The direct frontier is now narrower than that six-field construction:
select whether the hidden `E8` confines and bound the unavoidable wrapped-NS5
amplitude. The next source object is `MTT_Selected_q79HiddenE8ConfinementAndNS5QualityAmplitudeCertificate_v1`.
