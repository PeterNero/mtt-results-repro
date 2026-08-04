# MTT Selected q79 Hidden E8 Confinement and NS5 Quality Amplitude Certificate v1

Status: `MTT_U6_SECOND_E8_TYPING_AND_TWO_FUYAU_CURVATURE_HIDDEN_EXIT_NO_GO_CLOSED_SELECTED_HIDDEN_BUNDLE_AND_AMPLITUDES_OPEN`

## What A101 closes

A100 fixed the full source-free axion charge rows and the primitive wrapped-NS5
action, but it deliberately left the second `E8` bundle and all numerical
non-QCD amplitudes open. A101 audits the actual MTT source, repairs its type,
proves the exact hidden-sector decision procedure, eliminates one entire
candidate construction, and reduces both NS5 and hidden-condensate quality to
executable A98 inequalities.

## Two-E8 source typing repair

The cited MTT Strominger paper writes one configuration `(g,Phi,B;A)`, one
fixed holomorphic bundle `E`, one Yang-Mills term and one `Tr F_A^2` Bianchi
term. That is a one-bundle Hull-Strominger functional. It does not select the
hidden bundle of an `E8 x E8` compactification.

The correctly typed configuration has `(A1,A2)` and

```text
Hhat = dB-alpha'/4*(omega3(A1)+omega3(A2)-omega3(omega+)),
dHhat = alpha'/4*(Tr F1^2+Tr F2^2-Tr R+^2).
```

The Yang-Mills term is the sum of the two gauge terms. The gauge-fixed Hessian
contains `Delta_A1 direct_sum Delta_A2`; therefore the existing local
convexity argument extends blockwise when both blocks satisfy its gap
hypothesis. This repairs the theorem's type. It does not manufacture `P2`.

## Exact confinement decision theorem

For a selected hidden bundle `(P2,rho2)`, first compute

```text
G_hid = C_E8(rho2(H2))
```

and branch the adjoint `248` under `H2 x G_hid`. Bundle-valued cohomology and
the selected threshold matrix determine the light charged representations.
For each simple factor,

```text
b0 = 3 C2(G)-sum_j N_j T(R_j).
```

Pure `N=1` SYM is certified only after every charged chiral field is absent or
selected massive. In that case the standard condensate theorem applies.
`b0>0` with light matter is not, by itself, a confinement theorem. The q79
certificate supplies none of `P2`, `rho2`, branching, cohomology or thresholds,
so it cannot yet decide the hidden phase.

## Two-Fu-Yau-curvature no-go

Let `q1,q2` be `E8` cocharacters. Removing every nonabelian root requires that
no one of the 240 `E8` roots be orthogonal to both. Define

```text
F(q1,q2)=q1^2+q2^2-|q1.q2|.
```

Move `q1` to the dominant chamber, let `m_i=(q1,alpha_i)` and let `Z` be its
zero-label Dynkin subdiagram. The residual Weyl group makes `q2` regular on
`Z`. Completing the square gives

```text
F = (3/4) q1^2 + |q2-q1/2|^2
  >= (3/4) m^T A_E8^-1 m + 1^T A_Z^-1 1.
```

When `q1^2>=40` this is at least 30. The generated exact table exhausts all 40
dominant labels with `q1^2<40`; its minimum is also 30. Equality is attained by

```text
q1=(0,0,0,1,1,1,1,4),
q2=(0,1,2,-3,-2,-1,0,-1),
Gram(q1,q2)=[[20,-10],[-10,20]].
```

Direct enumeration finds zero common orthogonal roots among all 240 roots.

For two independent integral ASD K3 classes, put
`I_ab=-integral omega_a wedge omega_b`. In a Minkowski-reduced integral basis,
`I=[[a,b],[b,c]]` with `2|b|<=a<=c` and even `a>=2`. Hence

```text
k2=(1/2) sum_ab (q_a,q_b) I_ab
  >= (a/2) [q1^2+q2^2-|q1.q2|]
  >= 30.
```

The smooth source-free K3/Fu-Yau budget is 24. Thus no construction using
only the two Fu-Yau circle curvatures can abelianize the hidden `E8`. This does
not exclude a nonabelian hidden bundle, additional bundle curvatures, or an
NS5-sourced branch.

## NS5 quality envelope

The supplementary formula in [Benabou et al. (2026)](https://arxiv.org/abs/2605.04142)
refines the A100 placeholder to

```text
Lambda_NS5,W^4 = [kappa/(16 pi alpha_GUT)] m3/2 M_GUT^3
                 exp(-2 pi/alpha_GUT).
```

Thus `A_NS5=kappa/(16*pi*alpha_GUT)`. With
`Ctheta=chi_QCD sin(epsilon)`, the exact A98 derivative condition is

```text
kappa*m3/2 < 16*pi*alpha_GUT*Ctheta
             *exp(2*pi/alpha_GUT)/M_GUT^3.
```

The Kahler contribution obeys

```text
A_K*m3/2^2 < Ctheta*exp(2*pi/alpha_GUT)/M_s^2.
```

The generated profiles use external benchmark values only. They are envelope
checks, not selected MTT predictions.

## Full-holonomy candidate and remaining frontier

If a stable selected `P2` has full `E8` holonomy, its continuous commutant is
trivial and hidden gaugino condensation disappears. The K3 index
`30*k2-248` first becomes nonnegative at `k2=9` (value 22), but an index is not
an existence, full-holonomy, Fu-Yau-lift or Bianchi-allocation theorem.

The next artifact must construct one actual `P2`, prove its characteristic
class fits the same 24-unit source-free Bianchi allocation, solve/establish its
HYM connection and commutant, execute its cohomology and thresholds, and then
insert the selected scales and prefactors into the now-closed A98 envelopes.

Next artifact: `MTT_Selected_q79HiddenBundleExistenceBianchiAllocationAndSpectrumExecution_v1`.

## Primary references

- [Supersymmetric Hidden Sectors for Heterotic Standard Models](https://arxiv.org/abs/1301.6767)
- [Non-Perturbative Properties of Heterotic String Vacua Compactified on K3 x T2](https://arxiv.org/abs/hep-th/9606049)
- [Heterotic String Theory Suggests a QCD Axion Near 0.5 neV](https://arxiv.org/abs/2605.04142)
- [Gaugino Condensation and Nonperturbative Superpotentials](https://arxiv.org/abs/hep-th/9501065)
