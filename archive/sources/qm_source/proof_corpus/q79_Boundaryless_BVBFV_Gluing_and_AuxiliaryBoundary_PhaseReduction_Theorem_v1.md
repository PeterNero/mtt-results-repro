# q79 Boundaryless BV-BFV Gluing and Auxiliary-Boundary Phase-Reduction Theorem

Date: 2026-07-26

## 1. Claim boundary

The selected continuum q79 Standard-Model construction is a local theory on
the globally hyperbolic spacetime \(Y_4\). Its interaction functional is
compactly supported. It does not introduce a physical boundary.

The smooth bounded boundary used by the local elliptic APS construction is an
auxiliary regulator boundary. Consequently, the current proof obligation is
not to make MTT select that boundary as physical structure. It is to prove
that auxiliary boundary data cancel or become presentation-neutral when the
regulated region is glued to its complement.

This theorem closes that statement at the anomaly-free formal BV-BFV and
determinant-line tier. It does not prove uniform cutoff removal, a
fixed-coupling interacting \(C^*\)-limit, or nonperturbative completion.

## 2. Inputs

The theorem uses the following already certified results.

1. The selected q79 continuum Standard-Model field stack has a classical BV
   master action.
2. The interaction used in perturbative AQFT is local and compactly
   supported.
3. The five-component local gauge-anomaly vector is exactly zero:
   \[
   (0,0,0,0,0).
   \]
4. For the faithful gauge group,
   \[
   G_{\rm SM}=(SU(3)\times SU(2)\times U(1))/\mathbb Z_6,
   \]
   the registered spin-bordism obstruction is
   \[
   \Omega^{\rm Spin}_5(BG_{\rm SM})=0.
   \]
5. The rounded APS boundary is explicitly auxiliary.
6. Gauge and spin-liftable diffeomorphism presentation orbits already have
   canonical determinant transport, zero relative APS flow and zero relative
   BV-BFV flux.
7. Common absolute determinant phase is already proved to be an unpointed
   \(U(1)\)-torsor that cancels from normalized connected-sector
   observables.

## 3. BV-BFV gluing

For a regulated region \(M\subset Y_4\) with boundary
\(\Sigma=\partial M\), the classical BV-BFV identity has the form
\[
\iota_Q\Omega_M
  =\delta S_M+\pi_\Sigma^*\alpha_\Sigma.
\tag{3.1}
\]

The complementary region \(M^c\) induces the opposite boundary orientation.
Therefore
\[
\alpha_{\bar\Sigma}=-\alpha_\Sigma.
\tag{3.2}
\]

The boundary state associated with \(M\) belongs to a boundary line
\(\mathcal L_\Sigma\), while the state associated with \(M^c\) belongs to
the dual line:
\[
Z_M\in\mathcal L_\Sigma,
\qquad
Z_{M^c}\in\mathcal L_\Sigma^\vee.
\tag{3.3}
\]

Gluing evaluates the canonical pairing
\[
Z_{Y_4}
  =\langle Z_{M^c},Z_M\rangle.
\tag{3.4}
\]

Thus the boundary rephasing
\[
Z_M\longmapsto zZ_M,\qquad
Z_{M^c}\longmapsto z^{-1}Z_{M^c},
\qquad z\in U(1),
\tag{3.5}
\]
leaves the glued amplitude invariant.

## 4. Exact finite witness

Use the two-dimensional boundary symplectic model
\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\qquad
L=\operatorname{span}(e_1),
\qquad
L^\vee=\operatorname{span}(e_2).
\tag{4.1}
\]

Both lines are isotropic and
\[
e_1^TJe_2=1.
\tag{4.2}
\]
Orientation reversal sends \(J\) to \(-J=J^T\), giving the complementary
boundary pairing.

For the four exact unit phases
\[
z\in\{1,i,-1,-i\},
\]
the certificate computes
\[
z\bar z=1
\tag{4.3}
\]
using Gaussian-integer arithmetic. This is an exact witness of the dual-line
cancellation, not a numerical approximation to a continuum determinant.

## 5. Anomaly condition

Equation (3.5) removes a common boundary-line phase. Path-independent
coherent transport additionally requires absence of local curvature and
global gauge holonomy obstructions.

At the declared q79 Standard-Model tier these are precisely the already
certified conditions:
\[
\mathcal A_{\rm local}=0,
\qquad
\Omega^{\rm Spin}_5(BG_{\rm SM})=0.
\tag{5.1}
\]

They prove that no local gauge-anomaly curvature or spin global-gauge anomaly
forces an uncancelled phase on the declared category. They do not select an
absolute trivialization; the remaining common choice is the previously
identified \(U(1)\)-torsor.

## 6. Source retyping

The former boundary-source contract mixed auxiliary regulator data with
potentially physical history data. On the present boundaryless domain it
splits as follows.

| Former row | Correct status |
|---|---|
| moving boundary embedding | auxiliary regulator presentation datum |
| collar/adapted-operator convention | auxiliary analytic convention |
| common zero-mode taming/BFV polarization phase | dual boundary datum that cancels on gluing |
| connection history | physical only when an actual background or relative-sector history is supplied |
| endpoint transport | canonical on certified presentation orbits; otherwise part of a genuine relative-sector comparison |

The stationary action determines equations of motion. It does not select one
solution or background history without state, initial, boundary or
preparation data. This theorem therefore does not falsely derive a physical
connection history from the action.

## 7. Theorem

**Theorem.** On the currently selected boundaryless, compact-support,
anomaly-free formal q79 Standard-Model QFT domain:

1. a bounded APS boundary is auxiliary regulator data;
2. the BV-BFV state lines of a regulated region and its complement are dual;
3. their common boundary phase cancels exactly in the glued amplitude;
4. the vanishing local anomaly vector and faithful-\(\mathbb Z_6\) spin
   bordism obstruction remove the corresponding local and global gauge
   obstructions;
5. MTT is not required to select a physical moving regulator boundary,
   collar, or common boundary polarization phase.

Hence
```text
B.QFT.02_selected_physical_noncollar_boundary_family
  = retired_as_false_exit_on_current_boundaryless_QFT_domain
```
and
```text
B.QFT.02_auxiliary_boundary_phase_after_gluing
  = closed_formal_exact_as_dual_line_cancellation.
```

## 8. Remaining physical phase cutset

The following remain open and are not removed by this theorem:

1. relative holonomy between coherently summed disconnected sectors;
2. an actual physical boundary or unpaired edge mode, if the theory contains
   one;
3. inequivalent spin structures or nontransported endpoint data;
4. finite counterterm and renormalization-scheme matching;
5. uniform interacting regulator removal;
6. fixed-nonzero-coupling and nonperturbative completion.

The previously constructed continuum circle family remains a correct
spectral-flow normal form and obstruction witness. It is no longer interpreted
as a history that the boundaryless physical action must select.

## 9. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
false physical source rows retired: 3
```

## 10. Reproduction

Run:

```powershell
python scripts/verify.py
python -m unittest tests.test_qm_source.QmSourceTestCase.test_auxiliary_boundary_phase_cancels_without_a_physical_selector -v
```

The generated certificate is:

```text
certificates/q79_boundaryless_bv_bfv_gluing_phase_reduction.certificate.json
```

## 11. Mathematical context

- Cattaneo, Mnev and Reshetikhin, classical BV theories on manifolds with
  boundary, for the bulk BV to boundary BFV identity.
- Cattaneo, Mnev and Reshetikhin, perturbative quantum gauge theories on
  manifolds with boundary, for BV-BFV pushforward and gluing.
- Dai and Freed, eta invariants and determinant-line holonomy, for anomaly
  lines and their gluing behavior.

