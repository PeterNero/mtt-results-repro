# q79 SM Determinant-Phase Torsor No-Go and Normalized-Observable Quotient Theorem v1

## Status

This theorem removes the common absolute determinant phase from the list of
physical `B.QFT.02` exits on one connected normalized q79 Standard-Model
sector.

It does not calculate a numerical determinant phase. It proves that current
anomaly-free QME, Ward and normalized-observable data cannot select one, and
that no such selection is physically required at the declared tier.

Relative phases between coherently summed disconnected sectors, determinant
holonomy on paths not covered by the certified transports, noncollar
boundary/BFV phases, finite counterterm matching and the interacting limit
remain open.

## 1. Certified inputs

The result composes four prior packages.

1. The q79 renormalized local-QME certificate has exactly zero local anomaly
   vector,
   \[
   (0,0,0,0,0),
   \]
   and records
   \[
   \Omega_5^{\mathrm{Spin}}
   \bigl(B((SU(3)\times SU(2)\times U(1))/\mathbb Z_6)\bigr)=0.
   \]
2. The Mathematical Language anomaly-line packet concludes that the local
   curvature and global gauge-holonomy obstructions to determinant-line
   trivialization vanish. It explicitly does not select an absolute phase,
   basepoint, finite counterterm or numerical determinant normalization.
3. The based gauge/frame and spin-liftable diffeomorphism certificates
   provide canonical unitary determinant-line transport on their declared
   connected presentation paths.
4. The finite-shell and temporal-companion certificates prove equality of
   normalized free physical observables while retaining an unnormalized
   determinant-line scalar.

The second input is hash pinned as

```text
4defdb471fbabbd761780928bba49d5707dec2719c3cb63399498eef525d48c3
```

in `source_manifest.json`.

## 2. Unit trivializations form a torsor

Let \(B_0\) be one connected component of the certified anomaly-free
background/gauge sector. Let

\[
\mathcal L_{\det}\longrightarrow B_0
\]

be its Hermitian determinant line with the anomaly connection. At this tier,
the certified vanishing curvature and holonomy obstruction ensure that a
unit parallel trivializing section exists.

Let \(\mathcal T\) denote the set of unit parallel trivializing sections.
For \(s\in\mathcal T\) and \(u\in U(1)\), define

\[
u\cdot s:=us.
\tag{2.1}
\]

This action is free. It is also transitive: if \(s_1,s_2\in\mathcal T\), then

\[
s_2=f\,s_1
\tag{2.2}
\]

for a unit function \(f:B_0\to U(1)\). Parallelness gives \(df=0\), and
connectedness makes \(f\) one constant \(u\in U(1)\). Hence

\[
\mathcal T\ \text{is a }U(1)\text{-torsor}.
\tag{2.3}
\]

A torsor has relative differences but no distinguished origin. Anomaly
cancellation proves nonemptiness of \(\mathcal T\); it does not point
\(\mathcal T\).

## 3. Homogeneous QME and Ward equations do not point the torsor

In semidensity form the quantum master equation is linear:

\[
\Delta_{\mathrm{BV}}\Psi=0.
\tag{3.1}
\]

For a constant \(u\in U(1)\),

\[
\Delta_{\mathrm{BV}}(u\Psi)
=u\,\Delta_{\mathrm{BV}}\Psi
=0.
\tag{3.2}
\]

The same argument applies to every homogeneous linear Ward operator that
commutes with scalar multiplication.

In action form, write

\[
\Psi=\exp(iS/\hbar),\qquad u=\exp(i\alpha).
\]

Then \(u\Psi\) corresponds to

\[
S\longmapsto S+\hbar\alpha.
\tag{3.3}
\]

The BV bracket, BV Laplacian and source derivatives annihilate the constant
shift. Thus the action-form QME also cannot select \(\alpha\).

The executable certificate realizes (3.1)-(3.2) with a rational
four-dimensional real representation of a complex Ward complex. The four
phases \(1,i,-1,-i\) produce four distinct closed states. This finite witness
does not replace the general linear argument; it checks the implementation
and prevents accidental phase fixing in the certificate logic.

## 4. Normalized observables quotient the common phase

Let \(Z[J]\) be nonzero at the reference source and let

\[
Z_u[J]=uZ[J],\qquad u\in U(1).
\tag{4.1}
\]

For an insertion \(\mathcal O\),

\[
\frac{Z_u[\mathcal O]}{Z_u[1]}
=\frac{uZ[\mathcal O]}{uZ[1]}
=\frac{Z[\mathcal O]}{Z[1]}.
\tag{4.2}
\]

Locally in source space,

\[
\log Z_u[J]=\log Z[J]+\log u,
\tag{4.3}
\]

so every positive-order source derivative of the connected generating
functional is unchanged. Only the source-independent zeroth-order
normalization remembers the chosen point of the torsor.

The exact Gaussian-integer witness uses

\[
Z[1]=3+4i,\qquad Z[\mathcal O]=7-i,
\]

and obtains

\[
\frac{7-i}{3+4i}
=\frac{17}{25}-\frac{31}{25}i.
\tag{4.4}
\]

Multiplication of numerator and denominator by each of
\(1,i,-1,-i\) leaves (4.4) exactly unchanged. The certificate performs the
same check for first- and second-order normalized source coefficients.

Choosing \(Z[0]=1\), a positive reference determinant, or another basepoint
is therefore a normalization convention. It is not a newly derived physical
constant.

## 5. Why relative phase remains

The quotient in Section 4 removes only one common phase. It does not permit
independent rephasing of sectors that enter one coherent sum.

For two unit sector amplitudes,

\[
|1+1|^2=4,\qquad |1+i|^2=2.
\tag{5.1}
\]

Thus a relative phase can change an observable interference term. Such a
phase requires actual determinant transport, eta/APS data, a boundary
polarization comparison or another source theorem relating the sectors.

The prior q79 certificates already provide that transport on:

1. the connected based gauge/residual-frame presentation orbit;
2. spin-liftable identity-component diffeomorphisms;
3. ambient-isotopic pushforwards of the complete rounded-region package;
4. collar-relative temporal-companion paths with only positive contractible
   cutoff crossings.

Equation (5.1) applies outside those certified relations, including
disconnected topological sectors and nontransported boundary polarizations.

## 6. Theorem

On one connected q79 SM sector satisfying the certified local/global anomaly
conditions, the unit parallel determinant-line trivializations form a
\(U(1)\)-torsor. Homogeneous QME and Ward equations are equivariant under its
action. Normalized expectation values and positive-order connected source
responses are invariant under that same common action.

Consequently,

```text
B.QFT.02_absolute_common_determinant_phase
  = excluded_as_unidentifiable_U1_convention_torsor
```

and

```text
B.QFT.02_absolute_unnormalized_determinant_line
  = retyped_not_a_physical_exit_on_one_connected_normalized_sector.
```

This is a no-go and quotient theorem, not an absolute phase prediction.

## 7. Remaining phase cutset

Still open:

1. relative determinant holonomy around a nontransported or noncontractible
   loop;
2. relative phases between coherently summed disconnected sectors;
3. eta, Maslov and BFV phases when the boundary polarization changes;
4. finite local counterterm and numerical scheme matching;
5. zero-mode crossings not covered by positive-shell contraction;
6. uniform interacting cutoff removal;
7. the interacting fixed-coupling gauge-BRST C*-limit.

These are not reformulations of the retired common phase. Each requires data
that can affect comparisons or observables.

## 8. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed inputs:                0
```

One normalization convention may be chosen per connected noninterfering
sector. It is not counted as a physical parameter. A relative phase is not
counted until a source-selected interfering pair or nontrivial loop is
supplied.

## 9. Reproduction

Run:

```powershell
python scripts/verify.py
python -m unittest discover -s tests -v
```

The generated certificate is:

```text
certificates/q79_sm_determinant_phase_torsor_quotient.certificate.json
```

## 10. References

- X. Dai and D. S. Freed, eta invariants and determinant-line holonomy,
  arXiv:hep-th/9405012.
- Global anomaly/bordism inputs consumed by the Mathematical Language packet,
  arXiv:1808.00009 and arXiv:1910.11277.
- A. Schwarz, *Geometry of Batalin-Vilkovisky quantization*,
  arXiv:hep-th/9205088.
- A. S. Cattaneo, P. Mnev and N. Reshetikhin, quantum BV-BFV pushforward,
  arXiv:1507.01221.
