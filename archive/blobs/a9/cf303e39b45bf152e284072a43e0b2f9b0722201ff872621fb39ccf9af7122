# q79 Continuum SM Coupling and Higgs-Extended Classical BV Composition Theorem v1

Date: 2026-07-23

## Status

**Closed at the typed q79-continuum Standard-Model carrier, one-Higgs
Yukawa-covariance and classical BV master-equation tier.**

This theorem composes results that previously lived in three separate places:

1. the selected q79 Lorentzian coframe and framed free Dirac/CAR net;
2. the A45-A51 finite Standard-Model carrier, faithful gauge group, completed
   finite triple and selected one-Higgs operator content;
3. the globally hyperbolic Standard-Model BRST and shifted-cotangent BV
   packets from the Mathematical Language Discovery program.

The result is a single typed continuum field stack on the selected q79
spacetime. It contains the three-family chiral matter bundle, one Higgs
doublet, all four Dirac-Yukawa channels, nonlinear BRST and the minimal
shifted-cotangent BV action. The classical master equation is exact.

It is not a renormalized interacting quantum field theory. No continuum BV
measure, quantum master equation, counterterm scheme, interacting local net or
strict upper-MTT action coefficient source is claimed.

The executable certificate is:

`certificates/q79_continuum_sm_classical_bv_composition.certificate.json`.

It passes 46 of 46 checks.

## 1. Hash-pinned inputs

The theorem consumes the following current authorities.

1. `Q79_LORENTZIAN_COFRAME` selects an oriented, time-oriented, globally
   hyperbolic and globally coframed Lorentzian realization \(Y_4\).
2. The framed q79 free-Dirac theorem supplies the spin bundle, Lorentzian
   Clifford principal symbol, Green-hyperbolic propagation and CAR functor on
   the selected framed category.
3. `SM_A45_CARRIER_SEPARATION` proves that the family carrier and the
   circle-lens-nil rank flag are different factors.
4. `SM_A46_TYPED_CHIRAL_CARRIER` supplies
   \[
   H_{\rm chiral}=\mathbb C^3_{\rm family}\otimes H_{16},
   \qquad \dim_{\mathbb C}H_{\rm chiral}=48,
   \]
   with family-diagonal gauge action and exact anomaly cancellation.
5. `SM_A47_FAITHFUL_GAUGE_GROUP` supplies
   \[
   G=S(U(3)\times U(2))
    \simeq \frac{SU(3)\times SU(2)\times U(1)_Y}{\mathbb Z_6}.
   \]
6. `SM_A50_COMPLETED_FINITE_TRIPLE` supplies the completed finite real-even
   triple and one anomaly-free shared physical circle.
7. `SM_A51_ONE_HIGGS_OPERATOR` supplies the selected one-doublet fluctuation
   and finite Yukawa operator content at its declared profile tier.
8. `MLD_GLOBAL_SM_BRST` supplies the exact nonlinear connection, ghost and
   \(H_{16}\)-matter BRST differential.
9. `MLD_SHIFTED_COTANGENT_BV` supplies the canonical shifted-cotangent
   construction, classical master equation and a finite algebraic QME seed.

Every input is hash-pinned in `source_manifest.json`.

## 2. Mandatory type separation

Let \(F_{q79}\) be the rank-six internal carrier used by the preceding free
q79 Dirac theorem. Let \(H_{\rm chiral}\) be the rank-48 Standard-Model
chiral carrier. There is no established isomorphism

\[
F_{q79}\longrightarrow H_{\rm chiral}.
\]

They must not be silently tensored and the q79 \(P/Q\) ranks must not be
counted as particle multiplicities. The present theorem reuses the common
spacetime spin factor:

\[
S_e^+Y_4,
\]

and attaches the Standard-Model associated bundle to that factor. It does not
identify the two finite carriers.

This is the unique conservative composition allowed by A45:

\[
\text{selected q79 spacetime and spin bundle}
\quad+\quad
\text{separate family-preserving SM representation}.
\]

The still-missing \(F_{q79}\)-to-particle intertwiner remains a separate
source theorem.

## 3. Continuum field bundles

Fix a principal \(G\)-bundle \(P\to Y_4\). The faithful quotient theory is
defined directly on \(P\); no lift to a separate
\(SU(3)\times SU(2)\times U(1)\) bundle is required.

With left-handed Weyl fields throughout, define

\[
E_{\rm chiral}
=P\times_G
 \left(\mathbb C^3_{\rm family}\otimes H_{16}\right),
\qquad
\mathcal E_\psi=S_e^+Y_4\otimes E_{\rm chiral}.
\]

The one-family rows are

\[
\begin{array}{c|c}
Q &(3,2)_{1/6}\\
u^c&(\bar3,1)_{-2/3}\\
d^c&(\bar3,1)_{1/3}\\
L &(1,2)_{-1/2}\\
e^c&(1,1)_1\\
N^c&(1,1)_0 .
\end{array}
\]

Their internal dimensions sum to 16. Three families give 48 internal
left-Weyl states. Since \(S_e^+Y_4\) has complex rank two, the off-shell Weyl
bundle has complex fiber dimension

\[
2\cdot48=96.
\]

This is a component count, not a count of on-shell particles.

The Higgs bundle is

\[
E_H=P\times_G\mathbb C^2_{\,6Y=3}.
\]

It is the single A51 complex doublet. Its conjugate \(H^\dagger\) is not a
second independent doublet.

## 4. Exact quotient and anomaly check

For a row with color triality \(t\), weak-doublet parity \(d\) and integer
charge \(q=6Y\), the generator

\[
(\omega_3,-1,e^{i\pi/3})
\]

of the diagonal \(\mathbb Z_6\) acts with exponent

\[
2t+3d+q\pmod 6.
\]

The certificate evaluates this exponent for

\[
Q,\ u^c,\ d^c,\ L,\ e^c,\ N^c,\ H,\ \bar H
\]

and obtains zero in every case. All continuum bundles therefore descend
through the faithful quotient.

Using \(q=6Y\) and suppressing common positive Dynkin-index factors, the
three-family anomaly coefficients are exactly

\[
\begin{aligned}
SU(3)^3&=0,\\
SU(3)^2U(1)&=0,\\
SU(2)^2U(1)&=0,\\
U(1)^3&=0,\\
\mathrm{grav}^2U(1)&=0.
\end{aligned}
\]

There are 12 weak doublets, so the global \(SU(2)\) Witten anomaly also
vanishes. The scalar Higgs contributes no chiral anomaly.

## 5. Gauge-covariant kinetic operator

For a smooth connection \(A\) on \(P\), define the chiral kinetic operator

\[
D_A^+
=i\sigma^a e_a{}^\mu
\left(
\nabla_\mu^{\rm LC,spin}\otimes1
+1\otimes\rho_{\rm chiral}(A_\mu)
\right).
\tag{5.1}
\]

Its principal symbol is the same Lorentzian Weyl/Dirac symbol already
certified in the free theorem. A smooth gauge connection changes only the
connection part. A smooth Higgs-Yukawa term is zeroth order. Consequently,
after the standard doubled chiral packaging,

\[
D_{A,H}=D_A+Y_H+Y_H^\dagger
\tag{5.2}
\]

is Dirac type and Green hyperbolic on the selected globally hyperbolic base.
For every fixed smooth external background \((A,H)\), it therefore defines a
background-coupled CAR net by the same construction as the free theorem.

This family of background-coupled fermion nets is not the interacting
quantization of the gauge and Higgs fields themselves.

## 6. The four one-Higgs Yukawa channels

In integer \(q=6Y\) units,

\[
q(Q,u^c,d^c,L,e^c,N^c,H)
=(1,-4,2,-3,6,0,3).
\]

The four channels are

\[
\begin{array}{c|c|c}
\text{channel}&\text{invariant}&q\text{-sum}\\ \hline
u&Q\,Y_u\,H\,u^c&1+3-4=0\\
d&Q\,Y_d\,\bar H\,d^c&1-3+2=0\\
e&L\,Y_e\,\bar H\,e^c&-3-3+6=0\\
\nu&L\,Y_\nu\,H\,N^c&-3+3+0=0 .
\end{array}
\]

The color contractions are \(3\otimes\bar3\to1\). The weak contractions are
either \(2\otimes2\to1\) through the invariant epsilon tensor or
\(2\otimes2^\vee\to1\) through evaluation.

The gauge action is

\[
\rho_{\rm phys}=I_{3,\rm family}\otimes\rho_{16}.
\]

Therefore every family matrix

\[
Y_u,\ Y_d,\ Y_e,\ Y_\nu\in
\operatorname{End}(\mathbb C^3_{\rm family})
\]

commutes with the gauge action. Gauge symmetry permits the four family
matrices but does not select their entries. Inserting the accepted A51
profile matrices preserves all identities above; it does not upgrade those
values to strict MTT predictions.

## 7. Gauge-invariant classical action

On compactly supported fields, or with boundary conditions for which the
required integrations by parts vanish, define

\[
\begin{aligned}
S_0=\int_{Y_4}\bigg[
&-\sum_a\frac{1}{4g_a^2}\langle F_a,F_a\rangle
+i\bar\psi D_A\psi
+\langle D_AH,D_AH\rangle
-V(H^\dagger H)\\
&-\left(
QY_uHu^c+QY_d\bar H d^c
+LY_e\bar H e^c+LY_\nu HN^c+\mathrm{h.c.}
\right)
\bigg]\,d\mathrm{vol}_g .
\end{aligned}
\tag{7.1}
\]

Every term is gauge invariant:

- the curvature and kinetic terms use invariant Hermitian forms;
- the Higgs potential depends only on \(H^\dagger H\);
- all four Yukawa monomials are exact gauge singlets;
- family matrices commute with the gauge representation.

Equation (7.1) fixes the invariant action form, not every physical
coefficient. Gauge kinetic normalizations, Higgs potential coefficients and
strict generative Yukawa values remain profile inputs or open upper-source
data.

## 8. Higgs-extended BRST differential

Let \(c\in\Omega^0(Y_4,\operatorname{ad}P)[1]\). Extend the already certified
nonlinear BRST differential by

\[
\begin{aligned}
sA&=d_Ac,&
sc&=-\tfrac12[c,c],\\
s\psi&=-\rho_{\rm chiral}(c)\psi,&
s\bar\psi&=\bar\psi\rho_{\rm chiral}(c),\\
sH&=-\rho_H(c)H.
\end{aligned}
\tag{8.1}
\]

The certificate checks the \(sl_2\) Higgs representation exactly:

\[
[h,e]=2e,\qquad[h,f]=-2f,\qquad[e,f]=h,
\]

and verifies preservation of the weak epsilon tensor. The hypercharge
generator is central. Together with the exact Chevalley-Eilenberg and
\(H_{16}\) checks in `MLD_GLOBAL_SM_BRST`, this gives

\[
s^2A=s^2c=s^2\psi=s^2\bar\psi=s^2H=0.
\tag{8.2}
\]

The gauge invariance of (7.1) gives

\[
sS_0=0.
\tag{8.3}
\]

## 9. Shifted-cotangent BV completion

Introduce antifields with

\[
\operatorname{gh}(\Phi^*)=-1-\operatorname{gh}(\Phi).
\]

Thus \(A^*,\psi^*,\bar\psi^*,H^*\) have ghost number \(-1\), while \(c^*\)
has ghost number \(-2\). The canonical odd symplectic form on the shifted
cotangent field stack has degree \(-1\).

Define

\[
S_{\rm BV}
=S_0
+\langle A^*,sA\rangle
+\langle\psi^*,s\psi\rangle
+\langle\bar\psi^*,s\bar\psi\rangle
+\langle H^*,sH\rangle
+\langle c^*,sc\rangle .
\tag{9.1}
\]

Every term in (9.1) has ghost number zero. The cotangent Hamiltonian identity
gives

\[
\frac12(S_{\rm BV},S_{\rm BV})
=sS_0+\sum_\Phi\langle\Phi^*,s^2\Phi\rangle.
\tag{9.2}
\]

Equations (8.2) and (8.3) imply

\[
(S_{\rm BV},S_{\rm BV})=0.
\tag{9.3}
\]

This is the classical master equation on the composed continuum field stack.
It introduces no new continuous parameter.

The finite shifted-cotangent packet also has an exact flat-Berezinian QME
seed. That seed is not a four-dimensional path-integral measure. It is not
promoted here.

## 10. Exact certificate

The local executable performs 46 checks:

- 9 source and preceding-tier checks;
- 15 carrier, quotient and anomaly checks;
- 10 Higgs and Yukawa checks;
- 9 BRST/BV checks;
- 3 primary-theorem registration checks.

All finite computations use exact rational arithmetic. They include:

- the \(16\), \(48\) and \(96\) dimension ledger;
- three rank-16 family projectors;
- commutation of all nine family matrix units with hypercharge;
- all matter and Higgs \(\mathbb Z_6\) descent exponents;
- the six anomaly conditions;
- exact \(sl_2\) brackets and epsilon preservation;
- all four Yukawa charge and nonabelian singlet conditions;
- ghost-number homogeneity and the classical BV master identity.

The certificate also verifies all 24 upstream global-BRST checks and all 37
upstream shifted-cotangent-BV checks through their pinned packets.

## 11. Theorem

**Theorem.** Let \(Y_4\) be the selected q79 globally hyperbolic framed
Lorentzian realization and let \(P\to Y_4\) be any principal
\(S(U(3)\times U(2))\) bundle. Then:

1. \(P\) defines a global rank-48 three-family left-Weyl Standard-Model
   associated bundle and a single rank-two complex Higgs bundle;
2. all matter and Higgs rows descend through the faithful diagonal
   \(\mathbb Z_6\) quotient;
3. the local, mixed, gravitational and global \(SU(2)\) anomaly tests vanish;
4. the gauge-covariant kinetic operator and all four one-Higgs Yukawa
   channels are globally typed and gauge covariant;
5. for every smooth external \((A,H)\), the fermion operator remains Dirac
   type and gives a background-coupled CAR net;
6. the nonlinear BRST differential extends to the Higgs and Yukawa sector and
   squares to zero;
7. the canonical shifted-cotangent extension satisfies the classical master
   equation exactly.

The theorem is a continuum classical interaction-source composition. It does
not select a global gauge-bundle sector, strict coefficient values, a quantum
measure or a renormalized interacting observable algebra.

## 12. Blocker delta

The following `B.QFT.02` clauses are now closed:

- typed continuum SM gauge, matter and Higgs carrier;
- faithful quotient descent and anomaly compatibility;
- one-Higgs Yukawa gauge covariance;
- Higgs-extended classical BRST;
- canonical continuum classical BV action and master equation;
- background-coupled fermion CAR family for smooth external \(A,H\).

The following remain open:

- dynamical interacting local net;
- continuum regulator and determinant-line orientation;
- renormalized QME and anomalous Ward identities;
- gauge-independent physical BRST/BV cohomology;
- counterterms, RG transport and matching;
- positive interacting states;
- nonperturbative completion.

Thus `B.QFT.02` remains open, but its frontier has moved from carrier and
classical-BRST construction to renormalized quantum interaction.

For `B.ACTION.01`, the downward continuum action form is closed at the A51
profile/covariance tier. The selected upper q79 action and strict coefficient
source remain open.

## 13. Parameter ledger

\[
\begin{array}{l|c}
\text{new continuous parameters from composition}&0\\
\text{new discrete numerical selectors}&0\\
\text{new fits}&0\\
\text{new observed values}&0
\end{array}
\]

The theorem carries symbolic or inherited profile coefficients. It does not
claim that gauge couplings, Higgs coefficients or Yukawa matrices have been
strictly selected by the upper MTT geometry.

## 14. Primary mathematical context

The locally covariant classical and quantum BV distinction follows Rejzner,
*Batalin-Vilkovisky formalism in locally covariant field theory*,
<https://arxiv.org/abs/1111.5130>.

The next quantum step requires the renormalized time-ordered product,
anomalous Master Ward identity and quantum BV operator of Fredenhagen and
Rejzner, *Batalin-Vilkovisky formalism in perturbative algebraic quantum field
theory*, <https://arxiv.org/abs/1110.5232>.

Hollands' construction of renormalized Yang-Mills theory on globally
hyperbolic curved spacetime shows the strength of the remaining exit:
interacting BRST-current conservation, nilpotent quantum charge, Ward
identities and gauge-preserving renormalization,
<https://arxiv.org/abs/0705.3340>.

## 15. Reproduction

From the repository root:

```powershell
python scripts\verify.py
python -m unittest discover -s tests -v
```

