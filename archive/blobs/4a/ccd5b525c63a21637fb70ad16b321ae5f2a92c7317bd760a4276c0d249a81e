from __future__ import annotations

import hashlib
import json
import os
from itertools import permutations
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
RESEARCH_DATE = "2026-07-30"
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
PROTO_ROOT = Path(
    os.environ.get(
        "MTT_PROTOSPINOR_GR_ROOT",
        TEXPAPERS / "mtt-protospinor-gr-response-proof",
    )
)
QM_ROOT = Path(
    os.environ.get(
        "MTT_QM_SOURCE_ROOT",
        TEXPAPERS / "mtt-qm-source-proof",
    )
)
SM_ROOT = Path(
    os.environ.get(
        "MTT_SM_CLOSURE_ROOT",
        TEXPAPERS / "mtt-sm-parity-closure",
    )
)

HESSIAN_SOURCE = (
    PROTO_ROOT
    / "certificates"
    / "q79_finite_rootstack_reynolds_tt_hessian_certificate.json"
)
JDE_SOURCE = (
    PROTO_ROOT
    / "certificates"
    / "q79_shared_rootplane_twisted_exterior_jde_functor_certificate.json"
)
QM_KINEMATICS_SOURCE = (
    QM_ROOT / "certificates" / "finite_q79_quantum_kinematics.certificate.json"
)
QM_ACTION_SOURCE = (
    QM_ROOT / "certificates" / "canonical_q79_hessian_recorder_source.certificate.json"
)
PREPARATION_NOGO_SOURCE = (
    QM_ROOT / "certificates" / "preparation_selection_nogo.certificate.json"
)
PQ_CONTEXT_SOURCE = (
    QM_ROOT / "certificates" / "canonical_pq_hazard_rigidity.certificate.json"
)
UNIVERSAL_LINE_SOURCE = ROOT / "q79_universal_shared_line_intertwiner.packet.json"
GAUGE_STACK_SOURCE = ROOT / "shared_circle_sm_gauge_stack_reference.packet.json"
A50_SOURCE = ROOT / "a50_determinant_fiber_unimodularity_bridge.packet.json"
UPPER_COMPLEX_SOURCE = ROOT / "q79_upstairs_derived_complex_contract.packet.json"
FOUNDATION_SOURCE = (
    SM_ROOT
    / "proof_corpus"
    / "mtt_selected_closureshadowgaugeactionaxiomderivation_or_explicitadoptionandheldoutvalidation_v1.md"
)

OUT_PACKET = ROOT / "q79_shared_circle_closure_dynamics_source.packet.json"
OUT_NOTE = ROOT / "Q79_SHARED_CIRCLE_CLOSURE_DYNAMICS_SOURCE_THEOREM_v1.md"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix(values: list[list[object]]) -> sp.Matrix:
    return sp.Matrix(
        [[sp.sympify(value, locals={"I": sp.I}) for value in row] for row in values]
    )


def matrix_json(value: sp.MatrixBase) -> list[list[str]]:
    return [[str(sp.simplify(entry)) for entry in row] for row in value.tolist()]


def is_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def permutation_matrix(permutation: tuple[int, ...]) -> sp.Matrix:
    result = sp.zeros(len(permutation))
    for column, row in enumerate(permutation):
        result[row, column] = 1
    return result


def source_record(
    repository: str,
    repository_root: Path,
    path: Path,
    payload: dict | None = None,
) -> dict[str, object]:
    record: dict[str, object] = {
        "repository": repository,
        "relative_path": path.relative_to(repository_root).as_posix(),
        "sha256": sha256(path),
    }
    if payload is not None:
        if payload.get("schema"):
            record["schema"] = payload["schema"]
        if payload.get("status"):
            record["status"] = payload["status"]
    return record


def coefficient_nullspace(
    identity: sp.Matrix,
    complex_structure: sp.Matrix,
    normal_projector: sp.Matrix,
) -> list[list[int]]:
    c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3", real=True)
    candidate = (
        c0 * identity
        + c1 * complex_structure
        + c2 * normal_projector
        + c3 * complex_structure * normal_projector
    )
    equations = list(candidate + candidate.T)
    coefficient_matrix, _ = sp.linear_eq_to_matrix(
        equations,
        [c0, c1, c2, c3],
    )
    return [
        [int(entry) for entry in vector]
        for vector in coefficient_matrix.nullspace()
    ]


def build_note(packet: dict) -> str:
    finite = packet["finite_source_theorem"]
    classification = packet["phase_generator_classification"]
    blockers = packet["blocker_assessment"]
    return f"""# q79 Shared-Circle Closure-Dynamics Source Theorem v1

**Date:** {packet["date"]}

**Executable packet:** `q79_shared_circle_closure_dynamics_source.packet.json`

**Builder:** `build_q79_shared_circle_closure_dynamics_source.py`

**Independent verifier:** `verify_q79_shared_circle_closure_dynamics_source.py`

## 1. Result

The review-level proposal

```text
closure repair
  -> linearization
  -> dissipative operator
  -> semigroup and kernel
```

is already part of the MTT fixed-point architecture. The new question is
whether the selected q79 shared-circle data derive the stabilization operator
from an actual repair action, and whether that same source supplies the
coherent operator used in the duality paper.

At the finite root-stack-symbol tier, the answer can now be stated exactly.
The accepted carrier contains

```text
P = P_Haar,
Q = I-P,
H_fin/kappa_fin = Q,
J = J_DE,
```

with

```text
P^2=P, Q^2=Q, PQ=0,
J^2=-I, J*= -J,
[J,P]=[J,Q]=0.
```

The ranks are

```text
rank(P)=2,
rank(Q)=4.
```

No observed value or fitted coefficient enters these identities.

## 2. Closure repair is now derived

The finite action is not being invented here. The accepted q79 certificate
already supplies the exact sum of squares

```text
S_fin(w)
 = kappa_fin/(4|S3|)
   sum_(g in S3) ||(I-rho(g))w||^2.
```

Direct differentiation gives

```text
D2 S_fin=kappa_fin Q.
```

The executable theorem independently re-sums all six group elements and
recovers `Q` exactly.

Define the normalized finite closure functional

```text
C_fin(w)=1/2 <w,Qw>.
```

Its critical manifold is `Ran(P)`, its Hessian is exactly `Q`, and its
negative-gradient repair equation is

```text
d_tau w = -Qw.
```

The solution is

```text
R_tau=P+exp(-tau)Q.
```

Hence the invariant/Haar sector is fixed and the transverse sector contracts
exactly at rate `exp(-tau)`. This is a finite Morse-Bott realization of
"closure repair -> Hessian -> semigroup", not merely a verbal analogy.

With an overall source normalization `kappa`, replace `tau` by `kappa tau`.
The already accepted finite Hessian leaves precisely that one action scale.

## 3. The same action also emits the finite unitary

Because `Q` is an orthogonal projector, the accepted action has the entire
operator-valued continuation

```text
T(z)=exp(-zQ)=P+exp(-z)Q.
```

Its positive real ray is the repair semigroup:

```text
T(tau)=P+exp(-tau)Q.
```

Its imaginary boundary is unitary:

```text
T(it)=P+exp(-it)Q.
```

This is exactly the dimensionless finite q79 quantum flow already certified
in the QM repository. On the real `J_DE` carrier it is

```text
U_Q(t)=P+cos(t)Q-sin(t)J_DE Q.
```

Thus one accepted finite action supplies both:

```text
gradient/repair generator  = -Q,
Hamiltonian phase generator = -J_DE Q.
```

No second operator has been inserted. In finite dimension the continuation is
unique: each matrix entry is entire, and two entire extensions agreeing on a
real interval agree everywhere. At a quarter turn,

```text
T(i*pi/2)=P-iQ,
T(-i*pi/2)=P+iQ.
```

The two signs are the two orientations of the same analytic boundary, not two
new theories.

This closes the same-action repair/unitary bridge at the finite-symbol tier.
It does not identify the dimensionless parameter with physical time. That
still requires the selected `kappa_fin/hbar` scale and a physical comparison
map. In a continuum or interacting theory, an analogous Euclidean-to-
Lorentzian promotion additionally needs the relevant domain, reflection-
positivity or equivalent reconstruction hypotheses.

## 4. Exact phase-allocation classification

The real star-algebra generated by `J` and `Q` has basis

```text
I, J, Q, JQ.
```

Its skew-adjoint part is exactly two-dimensional:

```text
K_(a,b)=a JP+b JQ.
```

The two canonical endpoint choices are

```text
K_coh=-JP  phase on the invariant/Haar kernel,
K_exc=-JQ  phase on the positive-Hessian complement.
```

Both are exact, skew, symmetry-compatible, and commute with the repair
operator. They are distinct. The previously certified finite q79 quantum
kinematics,

```text
U(s)=P+exp(-is)Q,
```

is the `K_exc` choice in the positive-`i` polarization of `J_DE`. The
duality-paper interpretation, where the retained coherent sector carries the
unitary phase, corresponds instead to `K_coh`.

Therefore the current operator/projector data do not uniquely select the
phase allocation. Modulo the diagonal common rotation `J=JP+JQ`, one relative
phase coefficient remains.

The new same-action rule removes this ambiguity:

```text
same-action phase is the imaginary boundary of the repair semigroup
```

selects `K_exc=-JQ` uniquely, because the real repair generator is `-Q`.
By contrast, imposing

```text
phase acts only on the coherent zero-mode sector
```

selects the different generator `K_coh=-JP`. That is a lawful extension of the
finite data, but it is not generated by the same closure action.

This agrees with, and sharpens, the existing preparation-state no-go. The
zero-Hessian coherent sector already contains two exact rank-one polarization
lines

```text
K_plus =(P-iJP)/2,
K_minus=(P+iJP)/2.
```

The retarded q79 branch cannot be used to choose a physical analytic boundary
orientation, or between the two coherent polarization lines, until a typed
intertwiner from branch orientation to the corresponding finite polarization
is proved.

## 5. General tangent-normal theorem

Let a selected configuration space carry a compatible metric `g`, complex or
Poisson structure `J`, and closure functional `C`. Suppose its critical set is
a smooth symmetry orbit or manifold `O`, and `C` is Morse-Bott with positive
normal Hessian `A`.

After gauge reduction,

```text
T_X M = T_X O direct-sum N_X O,
D2C|_(T O)=0,
D2C|_(N O)=A>0.
```

Then the linearized negative-gradient repair is zero tangentially and `-A`
normally. It generates

```text
I_(T O) direct-sum exp(-tau A).
```

If `A` is nonnegative and self-adjoint, the spectral theorem defines

```text
T(z)=integral exp(-z lambda) dE_A(lambda), Re(z)>=0.
```

For positive real `z=tau`, this is a contraction semigroup. On the imaginary
boundary `z=it`, it is the strongly continuous unitary group `exp(-itA)`.
This uniquely phases the positive normal modes under the same-action analytic-
boundary rule. It does not by itself prove that this boundary parameter is
physical Lorentzian time.

The spectral theorem alone gives this operator family, not a spatial heat
kernel with locality or smoothing. Calling its integral kernel a heat kernel
additionally requires the appropriate elliptic or sectorial differential
operator, domain, and regularity hypotheses.

A unitary phase on the zero-mode tangent sector `T O` is different: it still
requires an additional skew generator there. It is not determined by `A`
alone.

The finite q79 calculation above is the exact specialization with
`T O=Ran(P)` and `N O=Ran(Q)`.

Nor can the nonlinear action be recovered from the Hessian. Even in one real
coordinate,

```text
C1(x)=x^2/2,
C2(x)=x^2/2+lambda x^4
```

have the same Hessian at zero and different nonlinear repair fields. The
selected upper action must therefore be constructed upstream; it cannot be
reverse-engineered uniquely from the finite operator.

## 6. Exact relation to the duality-paper operator

The duality paper uses

```text
B_adm=P chi(A) exp(-tau A) chi(A) P,
```

where `P` is the Riesz projector onto an isolated coherent spectral cluster.
If a selected nonlinear closure functional `C` and compatible metric first
produce

```text
A=g^(-1) D2C
```

as a nonnegative self-adjoint elliptic fixed-point linearization, then
`B_adm` is exactly the spectrally filtered compression of the linearized
repair semigroup. Under those hypotheses, the paper's operator is downstream
of closure repair rather than an independent axiom.

There is, however, an exact finite-tier boundary. For the present q79 source,

```text
A_fin=Q,
chi(Q)=chi_0 P+chi_1 Q.
```

Functional calculus and `PQ=0` give

```text
P chi(Q) exp(-tau Q) chi(Q) P=chi_0^2 P.
```

For the sharp normalized window `chi_0=1`, this is simply `P`, independent of
`tau`, and

```text
P T(it) P=P.
```

Thus the finite q79 action proves the source mechanism, but its zero/one
Hessian spectrum does not yet emit nontrivial dynamics inside the retained
coherent sector. A projector kernel can still have a nontrivial local versus
spectral representation; what is absent here is a derived internal coherent
frequency spectrum.

This does not contradict the duality paper, whose assumptions allow an
isolated cluster of positive or split low eigenvalues. It shows exactly what
the selected continuum execution must add.

The finite obstruction leaves two distinct continuum routes.

First, a selected continuum operator can have an isolated low spectral cluster
containing several positive eigenvalues. Its Riesz projector commutes with
`A`, yet `P exp(-tau A) P` has nontrivial internal spectral weights. This is
the direct route used by the duality paper and requires no Feshbach correction.

Second, if the desired geometric or Galerkin projector `Pi` is not an invariant
spectral projector, form its Feshbach-Schur reduction

```text
F_Pi(A-z)
 = Pi(A-z)Pi
   - Pi A Pi_perp [Pi_perp(A-z)Pi_perp]^(-1) Pi_perp A Pi.
```

where the complementary block is invertible. That reduction can emit the
effective operator on a non-invariant retained subspace. A Riesz projector
cannot generate such off-diagonal couplings because it already commutes with
`A`.

Every element of the current minimal finite algebra

```text
span{{I,J_DE,Q,J_DE Q}}
```

commutes with `Q`; consequently that finite algebra supplies neither a richer
continuum spectrum nor a non-invariant reduction. It does not choose between
the two continuum routes.

## 7. What this closes

Closed exactly:

- a finite q79 Morse-Bott closure functional whose Hessian is the accepted
  Reynolds Hessian;
- its repair semigroup and exponential transverse decay;
- the unique entire continuation of that same semigroup;
- the existing finite q79 unitary as its imaginary boundary;
- the complete minimal-algebra classification of compatible phase generators;
- the exact relation of the existing complement-phase flow to `-JQ`;
- a coherent-kernel phase candidate `-JP`;
- exact quarter-boundary operators `P-iQ` and `P+iQ`;
- the conditional derivation of `B_adm` from a selected repair action;
- the exact finite compression `B_adm_fin=chi_0^2 P`;
- the no-go showing that the current two-eigenvalue commuting algebra emits
  neither a richer coherent cluster nor a non-invariant Feshbach coupling;
- zero new dimensionless parameters.

This changes the frontier because the finite phase-source problem is no longer
an unspecified search. The same-action analytic boundary selects the already
certified complement flow exactly. What remains is the physical justification
of that analytic boundary and its scale/time comparison.

## 8. What remains open

`B.ACTION.01` remains open. The finite source does not provide:

1. the selected physical visible-hidden q79 holomorphic/HYM carrier;
2. the physical nonlinear Hull-Strominger/heterotic action on that carrier;
3. the symbol functor carrying its Hessian to `Q`;
4. the theorem that physical Lorentzian evolution is the appropriate analytic
   boundary of its repair semigroup;
5. the physical coefficient `kappa_fin/hbar`;
6. particles as localized nonlinear relative equilibria;
7. a detector instrument or Born outcome law.
8. either a selected continuum Hessian with a nontrivial isolated low spectral
   cluster, or a selected non-invariant finite projector and its
   Feshbach-Schur effective operator.

`B.OP.01` also remains open because the physical rank-102 continuum Hessian
blocks and reduced Green operator have not been executed.

## 9. Circle-separation guard

This theorem uses the q79 finite differential-character quarter-turn
`J_DE`. It does not identify:

```text
the q79 Z64/C4 root line,
the continuous A50 hypercharge circle,
global quantum phase,
Lorentzian time.
```

Those objects can intertwine only through separately proved differential maps.
In particular, the exact A50 representation theorem is retained but not
silently promoted to a q79 connection-level identification.

## 10. Frontier statement

The strongest justified chain is now

```text
selected finite shared-line geometry
  -> (P,Q,J_DE)
  -> accepted exact sum-of-squares closure action
  -> exact repair semigroup
  -> unique entire continuation and existing finite unitary
  -> exact filtered coherent compression B_adm_fin=P.
```

The physical next theorem is:

> Construct the selected q79 upper action and its gauge-reduced Hodge Hessian.
> Test first whether an isolated positive low spectral cluster directly gives
> the coherent operator. If the selected finite carrier is not invariant,
> compute its Feshbach-Schur effective operator instead. In either case, prove
> the unitary parallel symbol map to the finite `P,Q,J_DE` source and justify
> the Lorentzian propagator as the controlled analytic boundary of that same
> source.

Current blocker assessment:

```text
B.ACTION.01: {blockers["B.ACTION.01"]}
B.OP.01:     {blockers["B.OP.01"]}
```

## 11. Reproduction

```powershell
python .\\build_q79_shared_circle_closure_dynamics_source.py
python .\\verify_q79_shared_circle_closure_dynamics_source.py
```

Expected output:

```text
Q79_SHARED_CIRCLE_CLOSURE_DYNAMICS_SOURCE_BUILD_PASS
Q79_SHARED_CIRCLE_CLOSURE_DYNAMICS_SOURCE_VERIFY_PASS
```
"""


def main() -> None:
    hessian_packet = load(HESSIAN_SOURCE)
    jde_packet = load(JDE_SOURCE)
    qm_packet = load(QM_KINEMATICS_SOURCE)
    qm_action_packet = load(QM_ACTION_SOURCE)
    preparation_packet = load(PREPARATION_NOGO_SOURCE)
    pq_context_packet = load(PQ_CONTEXT_SOURCE)
    universal_packet = load(UNIVERSAL_LINE_SOURCE)
    gauge_stack_packet = load(GAUGE_STACK_SOURCE)
    a50_packet = load(A50_SOURCE)
    upper_complex_packet = load(UPPER_COMPLEX_SOURCE)

    require(
        hessian_packet["status"].startswith(
            "Q79_FINITE_ROOTSTACK_REYNOLDS_TT_HESSIAN_CLOSED_EXACT"
        ),
        "finite Hessian source tier",
    )
    require(
        jde_packet["status"].startswith(
            "Q79_SHARED_ROOTPLANE_TWISTED_EXTERIOR_JDE_FUNCTOR_CLOSED"
        ),
        "J_DE source tier",
    )
    require(qm_packet["all_exact_checks_pass"] is True, "finite QM source checks")
    require(
        qm_action_packet["status"]
        == "Q79_HESSIAN_RESIDUAL_AND_SPECTRAL_RECORDER_SOURCE_EXACT_CONTEXT_AND_ACTUALIZATION_OPEN",
        "finite action source tier",
    )
    require(
        preparation_packet["status"]
        == "FINITE_SYMMETRY_AND_HESSIAN_DO_NOT_SELECT_A_UNIQUE_PREPARATION_STATE",
        "preparation no-go tier",
    )
    require(
        pq_context_packet["status"]
        == "CANONICAL_BINARY_RESPONSE_SELECTED_CLOCK_OPEN",
        "P/Q context tier",
    )
    require(
        universal_packet["theorem"]["tier"]
        == "CLOSED_EXACT_FLAT_DIFFERENTIAL_CHARACTER_AND_FINITE_ROOTSTACK_SYMBOL",
        "universal line theorem tier",
    )
    require(
        gauge_stack_packet["guardrails"][
            "claims_nonabelian_nonlinear_BRST_or_BV_closure"
        ]
        is False,
        "gauge stack nonlinear boundary",
    )
    require(
        a50_packet["guardrails"]["claims_differential_bundle_trivializations_are_identified"]
        is False,
        "A50 differential boundary",
    )
    require(
        upper_complex_packet["guardrails"]["claims_HYM_or_selected_metric"] is False,
        "upper complex physical boundary",
    )

    finite = hessian_packet["finite_data"]
    identity = sp.eye(6)
    tangent_projector = matrix(finite["reynolds_projector"])
    normal_projector = matrix(finite["normalized_hessian_shape"])
    complex_structure = matrix(finite["J_DE"])
    jde_independent = matrix(jde_packet["finite_data"]["induced_JDE"])
    qm_hessian = matrix(qm_packet["operators"]["normalized_hessian_shape"])

    tangent_complex = complex_structure * tangent_projector
    normal_complex = complex_structure * normal_projector
    coherent_generator = -tangent_complex
    complement_generator = -normal_complex
    global_generator = -complex_structure
    complex_source = tangent_projector + sp.I * normal_projector
    complex_source_conjugate = tangent_projector - sp.I * normal_projector
    complex_source_swapped = normal_projector + sp.I * tangent_projector

    r, s = sp.symbols("r s", real=True)
    repair_r = tangent_projector + r * normal_projector
    repair_s = tangent_projector + s * normal_projector
    coherent_quarter_turn = normal_projector - tangent_complex
    complement_quarter_turn = tangent_projector - normal_complex
    positive_i_projector = (identity - sp.I * complex_structure) / 2
    positive_i_existing = (
        tangent_projector - sp.I * normal_projector
    ) * positive_i_projector

    skew_nullspace = coefficient_nullspace(
        identity,
        complex_structure,
        normal_projector,
    )
    representations = [
        sp.diag(
            permutation_matrix(permutation),
            permutation_matrix(permutation),
        )
        for permutation in permutations(range(3))
    ]
    reconstructed_reynolds = sum(representations, sp.zeros(6)) / len(
        representations
    )
    reconstructed_defect_gram = sum(
        (
            (identity - representation).T
            * (identity - representation)
            for representation in representations
        ),
        sp.zeros(6),
    ) / (2 * len(representations))
    k_plus = (
        tangent_projector
        - sp.I * complex_structure * tangent_projector
    ) / 2
    k_minus = (
        tangent_projector
        + sp.I * complex_structure * tangent_projector
    ) / 2
    scalar_x = sp.symbols("x", real=True)
    nonlinear_lambda = sp.symbols("lambda", real=True, nonzero=True)
    quadratic_action = scalar_x**2 / 2
    nonlinear_action = quadratic_action + nonlinear_lambda * scalar_x**4
    chi_zero, chi_one = sp.symbols("chi_0 chi_1", real=True)
    finite_filter = chi_zero * tangent_projector + chi_one * normal_projector
    finite_filtered_operator = sp.simplify(
        tangent_projector
        * finite_filter
        * repair_r
        * finite_filter
        * tangent_projector
    )
    minimal_source_basis = (
        identity,
        complex_structure,
        normal_projector,
        complex_structure * normal_projector,
    )

    checks = {
        "source_projector_is_exact": tangent_projector**2 == tangent_projector,
        "normal_projector_is_exact": normal_projector**2 == normal_projector,
        "projectors_are_complementary": tangent_projector + normal_projector
        == identity,
        "projectors_are_orthogonal": is_zero(
            tangent_projector * normal_projector
        )
        and is_zero(normal_projector * tangent_projector),
        "tangent_rank_is_two": tangent_projector.rank() == 2,
        "normal_rank_is_four": normal_projector.rank() == 4,
        "accepted_hessian_is_normal_projector": qm_hessian == normal_projector,
        "accepted_sum_of_squares_action_reconstructs_P": reconstructed_reynolds
        == tangent_projector,
        "accepted_sum_of_squares_action_reconstructs_Q": reconstructed_defect_gram
        == normal_projector,
        "accepted_action_declares_Hessian_kappa_Q": qm_action_packet[
            "finite_action_source"
        ]["hessian"]
        == "H_fin=kappa_fin Q",
        "P_is_typed_as_coherent_symmetric_response": pq_context_packet[
            "q79_selected_context"
        ]["interpretation"][0]
        == "coherent/symmetric response",
        "Q_is_typed_as_closure_strain_response": pq_context_packet[
            "q79_selected_context"
        ]["interpretation"][1]
        == "closure-strain response",
        "J_sources_agree": jde_independent == complex_structure,
        "J_square_is_minus_identity": complex_structure**2 == -identity,
        "J_is_skew_adjoint": complex_structure.T == -complex_structure,
        "J_is_orthogonal": complex_structure.T * complex_structure == identity,
        "J_commutes_with_tangent_projector": is_zero(
            complex_structure * tangent_projector
            - tangent_projector * complex_structure
        ),
        "J_commutes_with_normal_projector": is_zero(
            complex_structure * normal_projector
            - normal_projector * complex_structure
        ),
        "repair_semigroup_multiplication_is_exact": sp.simplify(
            repair_r * repair_s
            - (tangent_projector + r * s * normal_projector)
        )
        == sp.zeros(6),
        "repair_energy_contracts_by_r_squared": sp.simplify(
            repair_r.T * normal_projector * repair_r
            - r**2 * normal_projector
        )
        == sp.zeros(6),
        "coherent_generator_is_skew": coherent_generator.T
        == -coherent_generator,
        "complement_generator_is_skew": complement_generator.T
        == -complement_generator,
        "coherent_and_complement_generators_are_distinct": coherent_generator
        != complement_generator,
        "coherent_generator_rank_is_two": coherent_generator.rank() == 2,
        "complement_generator_rank_is_four": complement_generator.rank() == 4,
        "phase_generators_sum_to_global_shared_rotation": coherent_generator
        + complement_generator
        == global_generator,
        "coherent_quarter_turn_is_orthogonal": coherent_quarter_turn.T
        * coherent_quarter_turn
        == identity,
        "complement_quarter_turn_is_orthogonal": complement_quarter_turn.T
        * complement_quarter_turn
        == identity,
        "coherent_phase_commutes_with_repair": is_zero(
            coherent_generator * normal_projector
            - normal_projector * coherent_generator
        ),
        "complement_phase_commutes_with_repair": is_zero(
            complement_generator * normal_projector
            - normal_projector * complement_generator
        ),
        "existing_complex_flow_is_minus_JQ_in_positive_i_polarization": is_zero(
            complement_quarter_turn * positive_i_projector
            - positive_i_existing
        ),
        "minimal_source_algebra_skew_dimension_is_two": len(skew_nullspace) == 2,
        "minimal_source_algebra_skew_basis_is_J_and_JQ": skew_nullspace
        == [[0, 1, 0, 0], [0, 0, 0, 1]],
        "JP_and_JQ_are_linearly_independent": sp.Matrix.hstack(
            sp.Matrix(tangent_complex).reshape(36, 1),
            sp.Matrix(normal_complex).reshape(36, 1),
        ).rank()
        == 2,
        "K_plus_is_rank_one_Hermitian_projector": k_plus.rank() == 1
        and is_zero(sp.conjugate(k_plus).T - k_plus)
        and is_zero(k_plus**2 - k_plus),
        "K_minus_is_rank_one_Hermitian_projector": k_minus.rank() == 1
        and is_zero(sp.conjugate(k_minus).T - k_minus)
        and is_zero(k_minus**2 - k_minus),
        "K_plus_and_K_minus_are_distinct": k_plus != k_minus,
        "preparation_no_go_independently_retains_both_polarizations": preparation_packet[
            "checks"
        ]["two_ground_states_are_distinct"]
        is True,
        "same_Hessian_different_nonlinear_actions": sp.diff(
            quadratic_action,
            scalar_x,
            2,
        ).subs(scalar_x, 0)
        == sp.diff(nonlinear_action, scalar_x, 2).subs(scalar_x, 0)
        == 1,
        "same_Hessian_does_not_fix_nonlinear_repair_field": sp.simplify(
            sp.diff(nonlinear_action, scalar_x)
            - sp.diff(quadratic_action, scalar_x)
        )
        == 4 * nonlinear_lambda * scalar_x**3,
        "finite_filtered_coherent_operator_is_chi0_squared_P": is_zero(
            finite_filtered_operator - chi_zero**2 * tangent_projector
        ),
        "sharp_finite_filtered_coherent_operator_is_P": is_zero(
            finite_filtered_operator.subs(chi_zero, 1) - tangent_projector
        ),
        "finite_filtered_coherent_operator_is_tau_independent": not finite_filtered_operator.has(
            r
        ),
        "same_action_unitary_compresses_trivially_to_P": is_zero(
            tangent_projector
            * complex_source_conjugate
            * tangent_projector
            - tangent_projector
        ),
        "same_action_phase_generator_vanishes_on_coherent_sector": is_zero(
            tangent_projector
            * complement_generator
            * tangent_projector
        ),
        "current_minimal_source_algebra_commutes_with_Q": all(
            is_zero(element * normal_projector - normal_projector * element)
            for element in minimal_source_basis
        ),
        "complex_source_is_unitary": is_zero(
            sp.conjugate(complex_source).T * complex_source - identity
        ),
        "complex_source_has_order_four": complex_source**4 == identity,
        "opposite_quarter_boundary_is_unitary": is_zero(
            sp.conjugate(complex_source_conjugate).T
            * complex_source_conjugate
            - identity
        ),
        "same_action_quarter_boundaries_are_conjugate": is_zero(
            sp.conjugate(complex_source) - complex_source_conjugate
        ),
        "swapped_complex_source_is_also_unitary": is_zero(
            sp.conjugate(complex_source_swapped).T
            * complex_source_swapped
            - identity
        ),
        "complex_source_and_swap_are_distinct": complex_source
        != complex_source_swapped,
        "q79_universal_line_does_not_claim_A50_identification": universal_packet[
            "guardrails"
        ]["claims_q79_Z64_is_the_SM_hypercharge_circle"]
        is False,
        "finite_qm_physical_time_and_energy_remain_open": qm_packet[
            "blocker_readiness"
        ]["B.QM.02_physical_time_and_energy"]
        == "open",
        "physical_upper_complex_HYM_remains_open": upper_complex_packet[
            "strict_physical_upper_state_readiness"
        ]["gates"]["balanced_HYM_superconnection"]
        is False,
    }
    require(all(checks.values()), f"failed checks: {[k for k, v in checks.items() if not v]}")

    packet = {
        "schema": "MTTQ79SharedCircleClosureDynamicsSource.v1",
        "date": RESEARCH_DATE,
        "status": (
            "Q79_FINITE_SUM_OF_SQUARES_CLOSURE_REPAIR_HOLOMORPHIC_SEMIGROUP_"
            "AND_UNITARY_BOUNDARY_PLUS_MINIMAL_GENERATOR_CLASSIFICATION_"
            "CLOSED_EXACT_PHYSICAL_CONTINUUM_ACTION_ANALYTIC_RECONSTRUCTION_"
            "AND_TIME_SCALE_OPEN"
        ),
        "inputs": {
            "finite_Reynolds_Hessian": source_record(
                "mtt-protospinor-gr-response-proof",
                PROTO_ROOT,
                HESSIAN_SOURCE,
                hessian_packet,
            ),
            "shared_rootplane_JDE": source_record(
                "mtt-protospinor-gr-response-proof",
                PROTO_ROOT,
                JDE_SOURCE,
                jde_packet,
            ),
            "finite_q79_quantum_kinematics": source_record(
                "mtt-qm-source-proof",
                QM_ROOT,
                QM_KINEMATICS_SOURCE,
                qm_packet,
            ),
            "accepted_finite_q79_action": source_record(
                "mtt-qm-source-proof",
                QM_ROOT,
                QM_ACTION_SOURCE,
                qm_action_packet,
            ),
            "finite_preparation_polarization_no_go": source_record(
                "mtt-qm-source-proof",
                QM_ROOT,
                PREPARATION_NOGO_SOURCE,
                preparation_packet,
            ),
            "canonical_PQ_response_typing": source_record(
                "mtt-qm-source-proof",
                QM_ROOT,
                PQ_CONTEXT_SOURCE,
                pq_context_packet,
            ),
            "universal_shared_line": source_record(
                "20 Mathematical Language Discovery Program",
                ROOT,
                UNIVERSAL_LINE_SOURCE,
                universal_packet,
            ),
            "shared_circle_gauge_stack": source_record(
                "20 Mathematical Language Discovery Program",
                ROOT,
                GAUGE_STACK_SOURCE,
                gauge_stack_packet,
            ),
            "A50_determinant_fiber_bridge": source_record(
                "20 Mathematical Language Discovery Program",
                ROOT,
                A50_SOURCE,
                a50_packet,
            ),
            "q79_upstairs_derived_complex": source_record(
                "20 Mathematical Language Discovery Program",
                ROOT,
                UPPER_COMPLEX_SOURCE,
                upper_complex_packet,
            ),
            "closure_shadow_action_audit": source_record(
                "mtt-sm-parity-closure",
                SM_ROOT,
                FOUNDATION_SOURCE,
            ),
        },
        "finite_source_data": {
            "carrier": "W_fin=R3_D direct_sum R3_E",
            "dimension": 6,
            "tangent_or_invariant_projector_P": matrix_json(tangent_projector),
            "normal_or_positive_Hessian_projector_Q": matrix_json(normal_projector),
            "shared_quarter_turn_JDE": matrix_json(complex_structure),
            "tangent_complex_generator_JP": matrix_json(tangent_complex),
            "normal_complex_generator_JQ": matrix_json(normal_complex),
            "ranks": {
                "P": tangent_projector.rank(),
                "Q": normal_projector.rank(),
                "JP": tangent_complex.rank(),
                "JQ": normal_complex.rank(),
            },
            "spectrum_Q": {"0": 2, "1": 4},
            "polarization_lines_in_Ran_P": {
                "K_plus": matrix_json(k_plus),
                "K_minus": matrix_json(k_minus),
                "rank_each": 1,
                "orientation_selected": False,
            },
            "dimensionless_fitted_parameters": 0,
            "accepted_overall_action_normalizations": 1,
        },
        "finite_source_theorem": {
            "accepted_sum_of_squares_action": (
                "S_fin(w)=kappa_fin/(4|S3|) "
                "sum_g ||(I-rho(g))w||^2"
            ),
            "independent_action_Hessian_reconstruction": (
                "(1/(2|S3|)) sum_g "
                "(I-rho(g))^*(I-rho(g))=Q"
            ),
            "closure_functional": "C_fin(w)=1/2 <w,Qw>",
            "critical_manifold": "Crit(C_fin)=Ran(P)",
            "Hessian": "D2 C_fin=Q",
            "negative_gradient_repair": "d_tau w=-Qw",
            "repair_semigroup": "R_tau=P+exp(-tau)Q",
            "repair_energy_identity": (
                "C_fin(R_tau w)=exp(-2tau) C_fin(w)"
            ),
            "same_action_entire_semigroup": "T(z)=P+exp(-z)Q",
            "same_action_unitary_boundary": "T(it)=P+exp(-it)Q",
            "same_action_real_JDE_generator": "-JDE Q",
            "coherent_zero_mode_alternative_generator": "-JDE P",
            "coherent_zero_mode_alternative_flow": (
                "U_coh(t)=Q+cos(t)P-sin(t)JDE P"
            ),
            "same_action_complex_time_flow": (
                "T(tau+it)=P+exp(-tau-it)Q"
            ),
            "analytic_uniqueness": (
                "Every matrix entry is entire; agreement with the real repair "
                "semigroup on an interval fixes the entire continuation and "
                "its imaginary boundary uniquely."
            ),
            "general_scope": (
                "This is the exact finite Morse-Bott tangent-normal theorem. "
                "Its continuum analogue requires a selected gauge-reduced "
                "closure functional with positive normal Hessian."
            ),
        },
        "same_action_holomorphic_semigroup": {
            "operator_family": "T(z)=exp(-zQ)=P+exp(-z)Q",
            "repair_ray": "T(tau)=P+exp(-tau)Q",
            "unitary_boundary": "T(it)=P+exp(-it)Q",
            "real_JDE_form": "P+cos(t)Q-sin(t)JDE Q",
            "positive_imaginary_quarter_boundary": {
                "operator": "P-iQ",
                "matrix": matrix_json(complex_source_conjugate),
            },
            "negative_imaginary_quarter_boundary": {
                "operator": "P+iQ",
                "matrix": matrix_json(complex_source),
            },
            "uniqueness": (
                "The finite matrix-valued entire continuation is unique by the "
                "identity theorem once its repair values are fixed on a real interval."
            ),
            "dimensionless_same_action_bridge_closed": True,
            "physical_time_and_scale_selected": False,
        },
        "abstract_same_action_linearization_theorem": {
            "hypotheses": [
                "a gauge-reduced Hilbert or Kahler tangent space",
                "a Morse-Bott closure functional at the selected critical manifold",
                "a nonnegative self-adjoint normal Hessian A",
            ],
            "repair": "R_tau=exp(-tau A), tau>=0",
            "holomorphic_family": (
                "T(z)=integral exp(-z lambda) dE_A(lambda), Re(z)>=0"
            ),
            "unitary_boundary": "U_t=exp(-itA)",
            "boundary_norm": "||T(z)||<=1 for Re(z)>=0; U_t is unitary",
            "scope": (
                "This is an operator-theoretic theorem. Interpreting t as "
                "physical Lorentzian time requires a separate reconstruction "
                "and comparison theorem."
            ),
            "spatial_heat_kernel_status": (
                "NOT_CLAIMED: locality, smoothing and a spatial integral kernel "
                "require elliptic or sectorial differential-operator, domain "
                "and regularity hypotheses."
            ),
        },
        "duality_filtered_operator_source_assessment": {
            "paper_operator": "B_adm=P chi(A) exp(-tau A) chi(A) P",
            "conditional_source_theorem": (
                "If a selected nonlinear closure functional C and compatible "
                "metric have a fixed point with nonnegative self-adjoint "
                "elliptic linearization A=g^{-1}D2C, then B_adm is exactly the "
                "spectrally filtered compression of the linearized closure-repair "
                "semigroup. Under those hypotheses the operator is downstream "
                "of repair rather than an independent axiom."
            ),
            "finite_q79_specialization": {
                "linearization": "A_fin=Q",
                "spectral_filter": "chi(Q)=chi_0 P+chi_1 Q",
                "exact_compression": "B_adm_fin=chi_0^2 P",
                "sharp_normalized_window": "chi_0=1 implies B_adm_fin=P",
                "tau_dependence": False,
                "compressed_same_action_unitary": "P T(it) P=P",
                "nontrivial_coherent_spectral_dynamics_emitted": False,
            },
            "interpretation": (
                "The finite q79 action proves the source mechanism but has only "
                "the zero/one Hessian spectrum. It therefore does not yet realize "
                "the duality paper's potentially nontrivial isolated coherent "
                "spectral cluster. Local/spectral dual representation can remain "
                "nontrivial for a projector kernel, but dynamical coherent phases "
                "do not follow from this finite A_fin."
            ),
            "commuting_spectral_cluster_route": (
                "A selected continuum A can have an isolated low cluster with "
                "several positive eigenvalues. Its Riesz projector commutes with "
                "A while P exp(-tau A) P still has nontrivial internal spectral "
                "weights. This route needs no Feshbach correction."
            ),
            "noninvariant_preprojection_route": (
                "If a selected geometric or Galerkin projector Pi is not invariant "
                "under A, its Feshbach-Schur reduction emits the effective retained "
                "operator. A Riesz projector itself cannot create this coupling "
                "because it already commutes with A."
            ),
            "feshbach_schur_candidate": (
                "F_Pi(A-z)=Pi(A-z)Pi-Pi A Pi_perp "
                "[Pi_perp(A-z)Pi_perp]^{-1} Pi_perp A Pi"
            ),
            "current_finite_algebra_boundary": (
                "Every element of span{I,JDE,Q,JDE Q} commutes with Q, so the "
                "current two-eigenvalue algebra supplies neither a richer coherent "
                "cluster nor a non-invariant Feshbach coupling."
            ),
            "status": (
                "CONDITIONAL_GENERAL_SOURCE_CLOSED_EXACT_AND_FINITE_Q79_"
                "ZERO_MODE_COMPRESSION_OBSTRUCTION_CLOSED_EXACT_"
                "CONTINUUM_SPECTRUM_OR_NONINVARIANT_REDUCTION_OPEN"
            ),
        },
        "nonlinear_source_nonuniqueness": {
            "action_1": "C1(x)=x^2/2",
            "action_2": "C2(x)=x^2/2+lambda x^4",
            "common_Hessian_at_zero": 1,
            "repair_field_difference": "4 lambda x^3",
            "conclusion": (
                "The Hessian and its holomorphic linear flow do not determine "
                "the nonlinear upper action. B.ACTION.01 must be solved upstream."
            ),
        },
        "phase_generator_classification": {
            "minimal_star_algebra": "R[I,JDE,Q,JDE Q]",
            "minimal_star_algebra_dimension": 4,
            "skew_subspace_dimension": 2,
            "skew_subspace": "K_(a,b)=a JDE P+b JDE Q",
            "coherent_endpoint": {
                "generator": "-JDE P",
                "rank": coherent_generator.rank(),
                "quarter_turn": matrix_json(coherent_quarter_turn),
            },
            "complement_endpoint": {
                "generator": "-JDE Q",
                "rank": complement_generator.rank(),
                "quarter_turn": matrix_json(complement_quarter_turn),
            },
            "global_rotation": "-JDE=-JDE P-JDE Q",
            "relative_parameter_space": (
                "R2 / diagonal common rotation is one-dimensional"
            ),
            "existing_q79_finite_kinematics": {
                "flow": qm_packet["operators"]["dimensionless_flow"],
                "positive_i_polarization_generator": "-JDE Q",
                "allocation": "positive-Hessian complement",
            },
            "coherent_only_exit": (
                "Demanding zero phase transport on Ran(Q) forces b=0. "
                "Unit angular normalization leaves a=+/-1; physical orientation "
                "and scale still require source selection."
            ),
            "same_action_analytic_boundary_exit": (
                "Requiring phase transport to be the imaginary boundary of the "
                "accepted repair semigroup uniquely selects -JDE Q, matching "
                "the existing finite q79 unitary."
            ),
            "orientation_exit": (
                "The existing K_plus/K_minus coherent polarization no-go is "
                "retained. A retarded-branch-to-JDE-P intertwiner is required "
                "before either sign may be promoted."
            ),
            "uniqueness_from_current_operator_projector_data": False,
            "uniqueness_after_same_action_analytic_boundary_rule": True,
            "no_go_reason": (
                "-JDE P and -JDE Q are two distinct exact skew generators built "
                "from the same accepted data and satisfying all untyped "
                "commutation/symmetry requirements."
            ),
        },
        "theorem": {
            "name": (
                "q79SharedCircleMorseBottClosureRepairPhaseAndFiltered"
                "CoherentSourceTheorem"
            ),
            "statement": (
                "On the accepted six-real-dimensional q79 finite root-stack "
                "carrier, the accepted S3 sum-of-squares action has Hessian "
                "kappa_fin Q. The Reynolds projector P, normalized Hessian Q=I-P "
                "and shared-root quarter-turn JDE define an exact Morse-Bott "
                "closure functional C_fin=1/2<w,Qw>. Its negative-gradient "
                "flow is P+exp(-tau)Q, and its unique entire continuation has "
                "unitary imaginary boundary P+exp(-it)Q, exactly the existing "
                "finite q79 dimensionless unitary. The minimal star-algebra generated by "
                "JDE and Q has exactly the two-dimensional skew part "
                "a JDE P+b JDE Q. Hence a coherent-kernel phase and the already "
                "certified complement phase are both exact symmetry-compatible "
                "flows on the same finite data, "
                "so symmetry alone does not select their allocation. The "
                "same-action analytic-boundary rule does select the complement "
                "generator -JDE Q uniquely. Physical promotion still requires "
                "the continuum action, analytic reconstruction and time-scale map. "
                "For the duality-paper compression, A_fin=Q gives exactly "
                "B_adm_fin=chi_0^2 P and no internal coherent frequency spectrum. "
                "A nontrivial coherent operator may instead come directly from a "
                "richer selected continuum spectral cluster, or from a Feshbach "
                "reduction when the selected finite carrier is not invariant."
            ),
            "tier": (
                "CLOSED_EXACT_FINITE_ROOTSTACK_SAME_ACTION_HOLOMORPHIC_"
                "REPAIR_UNITARY_BRIDGE_WITH_EXPLICIT_PHYSICAL_PROMOTION_BOUNDARY"
            ),
        },
        "blocker_assessment": {
            "B.ACTION.01": (
                "OPEN: the exact finite same-action bridge does not supply the selected "
                "physical q79 nonlinear upper action, automorphism transfer or "
                "continuum symbol/analytic-reconstruction intertwiner."
            ),
            "B.OP.01": (
                "OPEN: the selected physical rank-102 Hessian blocks, harmonic "
                "projection, reduced Green operator and contraction data are "
                "not computed."
            ),
            "finite_phase_source_frontier": (
                "ADVANCED: the accepted finite action now derives both repair "
                "and the existing unitary as one holomorphic semigroup. The "
                "broader symmetry-only generator space is classified exactly."
            ),
        },
        "checks": checks,
        "guardrails": {
            "claims_physical_q79_upper_action_selected": False,
            "claims_B_ACTION_01_closed": False,
            "claims_B_OP_01_closed": False,
            "claims_existing_complement_phase_is_wrong": False,
            "claims_phase_allocation_is_unique_without_new_source_rule": False,
            "claims_retarded_branch_selects_K_plus_or_K_minus_without_intertwiner": False,
            "claims_q79_Z64_circle_equals_A50_hypercharge_circle": False,
            "claims_shared_circle_is_Lorentzian_time": False,
            "claims_finite_phase_orbit_is_a_physical_particle": False,
            "claims_spatial_heat_kernel_without_elliptic_regularity_data": False,
            "claims_finite_Q_model_has_nontrivial_coherent_spectral_dynamics": False,
            "claims_full_duality_operator_comes_from_selected_physical_q79_action": False,
            "claims_measurement_or_Born_rule": False,
            "uses_observed_values": False,
            "adds_dimensionless_fitted_parameters": False,
        },
        "frontier_delta": (
            "The accepted finite q79 S3 sum-of-squares action now emits an "
            "exact Morse-Bott repair semigroup and a unique entire continuation "
            "whose imaginary boundary is exactly the existing finite unitary. "
            "The same-action finite repair/unitary source bridge is closed with "
            "zero new parameters. The complete two-dimensional symmetry-only "
            "phase-generator space is also classified, showing why analytic "
            "same-source typing is essential. The remaining physical exit is "
            "the selected continuum q79 action and Hodge spectrum, or a "
            "non-invariant finite reduction with its operator/symbol intertwiner, "
            "plus the analytic reconstruction theorem and physical time/scale "
            "map. The duality-paper filtered operator is conditionally derived "
            "from repair, while its nontrivial coherent spectrum is not emitted "
            "by the present A_fin=Q model."
        ),
        "next_required_object": (
            "q79SelectedHodgeActionSpectrumOrFeshbachIntertwiner.v1: "
            "construct the selected visible-hidden Hull-Strominger/heterotic "
            "action and gauge-reduced Hodge Hessian. Test its isolated low "
            "spectral cluster first; if the selected finite carrier is not "
            "invariant, compute its Feshbach-Schur operator. Prove the resulting "
            "unitary parallel symbol map to the finite P,Q,JDE package and "
            "justify physical Lorentzian evolution as the controlled analytic "
            "boundary of the same source."
        ),
    }

    OUT_PACKET.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_NOTE.write_text(build_note(packet), encoding="utf-8")
    print("Q79_SHARED_CIRCLE_CLOSURE_DYNAMICS_SOURCE_BUILD_PASS")
    print("finite same-action repair/unitary bridge: CLOSED_EXACT")
    print("physical q79 continuum action, analytic reconstruction and time scale: OPEN")


if __name__ == "__main__":
    main()
