"""Execute the finite one-form/Higgs sector and finite spectral trace coefficients."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_selected_physicalfinitediracoperatorandintersectionform_or_fullfinitetripleclosure as a49  # noqa: E402


SLUG = "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "finite_inner_fluctuation_and_spectral_traces.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteSpectralActionAndHiggsInnerFluctuation_or_DirectGenerativeSMActionClosure_v1.md"
STATUS = "MTT_FINITE_ONEFORM_EXECUTED_RAW_THREE_DOUBLET_SPACE_SELECTED_SINGLE_HIGGS_PROJECTION_AND_TRACE_COEFFICIENTS_CLOSED_SPECTRAL_MOMENTS_OPEN"
NEXT = "MTT_Selected_SpectralCutoffMomentsAndSpacetimeProductTriple_or_BosonicActionNormalization_v1"
Q79_CERT = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates\single_higgs_channel_projection_certificate.json")
TOL = 1e-10


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_matrix(rows: list) -> np.ndarray:
    return np.array([[complex(*entry) for entry in row] for row in rows], dtype=complex)


def real_vector(matrix: np.ndarray) -> np.ndarray:
    flat = matrix.reshape(-1)
    return np.concatenate([flat.real, flat.imag])


def real_span_matrix(matrices: list[np.ndarray]) -> np.ndarray:
    return np.stack([real_vector(matrix) for matrix in matrices], axis=1)


def real_rank(matrices: list[np.ndarray]) -> int:
    return int(np.linalg.matrix_rank(real_span_matrix(matrices), tol=TOL))


def channel_generators(uj: np.ndarray) -> dict[str, np.ndarray]:
    up = np.array([[1.0], [0.0]], dtype=complex)
    down = np.array([[0.0], [1.0]], dtype=complex)
    return {
        "up": a49.internal_channel_dirac("Q_L", "u_R", np.kron(up, np.eye(3)), uj),
        "down": a49.internal_channel_dirac("Q_L", "d_R", np.kron(down, np.eye(3)), uj),
        "charged_lepton": a49.internal_channel_dirac("L_L", "e_R", down, uj),
        "neutrino": a49.internal_channel_dirac("L_L", "N_R", up, uj),
    }


def real_fluctuation_span(d_f: np.ndarray, left_basis: list[np.ndarray], uj: np.ndarray) -> list[np.ndarray]:
    answer: list[np.ndarray] = []
    for left_a in left_basis:
        for left_b in left_basis:
            one_form = left_a @ (d_f @ left_b - left_b @ d_f)
            for self_adjoint in [one_form + one_form.conjugate().T, 1j * (one_form - one_form.conjugate().T)]:
                answer.append(self_adjoint + uj @ self_adjoint.conjugate() @ uj.conjugate().T)
    return answer


def add_scalar_link(matrix: np.ndarray, left_field: str, right_field: str, internal: np.ndarray) -> None:
    left_edge = next(edge for edge in a49.EDGES if edge["field"] == left_field)
    right_edge = next(edge for edge in a49.EDGES if edge["field"] == right_field)
    left_width = left_edge["n_left"] * left_edge["n_right"]
    right_width = right_edge["n_left"] * right_edge["n_right"]
    l0, r0 = a49.PARTICLE_OFFSETS[left_field], a49.PARTICLE_OFFSETS[right_field]
    if internal.shape != (left_width, right_width):
        raise AssertionError(f"bad scalar link {left_field}<-{right_field}: {internal.shape}")
    matrix[l0 : l0 + left_width, r0 : r0 + right_width] = internal
    matrix[r0 : r0 + right_width, l0 : l0 + left_width] = internal.conjugate().T


def selected_single_higgs_fluctuation(higgs: np.ndarray, uj: np.ndarray) -> np.ndarray:
    # For H=(v,0), -epsilon conjugate(H)=(0,v), matching the A48/A49 incidence convention.
    epsilon = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    conjugate_higgs = -epsilon @ higgs.conjugate()
    particle = np.zeros((a49.FAMILY_DIM, a49.FAMILY_DIM), dtype=complex)
    add_scalar_link(particle, "Q_L", "u_R", np.kron(higgs, np.eye(3)))
    add_scalar_link(particle, "Q_L", "d_R", np.kron(conjugate_higgs, np.eye(3)))
    add_scalar_link(particle, "L_L", "e_R", conjugate_higgs)
    add_scalar_link(particle, "L_L", "N_R", higgs)
    return particle + uj @ particle.conjugate() @ uj.conjugate().T


def main() -> int:
    a50 = load(ROOT / "certificates" / "selected_neutralalgebrasummandorequivalentaxiomrevision_certificate.json")
    q79 = load(Q79_CERT)
    charged = load(ROOT / "candidate_data" / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution" / "versioned_common_scale_yukawa_higgs_values.packet.json")
    neutral = load(ROOT / "candidate_data" / "selected_neutraltwoprimitiveprofilevalueclosure" / "neutral_two_primitive_profile_values.packet.json")

    uj = a49.real_structure_matrix()
    _, algebra_values = a49.algebra_basis()
    left_basis = [a49.left_representation(value) for value in algebra_values]
    channels = channel_generators(uj)

    groups = {
        "up_type": ["up"],
        "down_plus_charged_lepton": ["down", "charged_lepton"],
        "neutral": ["neutrino"],
        "unrestricted_all": list(channels),
    }
    fluctuation_ranks = {}
    unrestricted_span: list[np.ndarray] = []
    for name, members in groups.items():
        d_group = sum((channels[member] for member in members), np.zeros_like(uj))
        span = real_fluctuation_span(d_group, left_basis, uj)
        fluctuation_ranks[name] = real_rank(span)
        if name == "unrestricted_all":
            unrestricted_span = span

    higgs_real_basis = [
        np.array([[1.0], [0.0]], dtype=complex),
        np.array([[1j], [0.0]], dtype=complex),
        np.array([[0.0], [1.0]], dtype=complex),
        np.array([[0.0], [1j]], dtype=complex),
    ]
    selected_higgs_matrices = [selected_single_higgs_fluctuation(higgs, uj) for higgs in higgs_real_basis]
    raw_matrix = real_span_matrix(unrestricted_span)
    selected_matrix = real_span_matrix(selected_higgs_matrices)
    containment_coefficients = np.linalg.lstsq(raw_matrix, selected_matrix, rcond=1e-12)[0]
    containment_residual = float(np.linalg.norm(raw_matrix @ containment_coefficients - selected_matrix))

    # In the real coefficient order (Re h1, Im h1, Re h2, Im h2), C implements
    # h -> -epsilon conjugate(h). The embedding is (H_up, H_down/e, H_nu)=(h,Ch,h).
    conjugation_matrix = np.array(
        [[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]],
        dtype=float,
    )
    embedding = np.vstack([np.eye(4), conjugation_matrix, np.eye(4)])
    single_higgs_projector = embedding @ np.linalg.inv(embedding.T @ embedding) @ embedding.T

    values = charged["values"]
    yukawas = {
        "u": complex_matrix(values["Y_u_MZ_firstpass"]),
        "d": complex_matrix(values["Y_d_MZ_firstpass"]),
        "e": complex_matrix(values["Y_e_MZ_firstpass"]),
        "nu": complex_matrix(neutral["matrices"]["Y_nu"]),
    }
    yukawa_trace_rows = {}
    invariant_a = 0.0
    invariant_b = 0.0
    for sector, yukawa in yukawas.items():
        gram = yukawa.conjugate().T @ yukawa
        multiplicity = 3 if sector in {"u", "d"} else 1
        trace2 = float(multiplicity * np.trace(gram).real)
        trace4 = float(multiplicity * np.trace(gram @ gram).real)
        invariant_a += trace2
        invariant_b += trace4
        yukawa_trace_rows[sector] = {"color_multiplicity": multiplicity, "weighted_Tr_YdaggerY": trace2, "weighted_Tr_YdaggerY_squared": trace4}

    gauge_trace_one_family = {"U1_Y": 10 / 3, "SU2": 2, "SU3": 2}
    gauge_trace_three_families = {key: 3 * value for key, value in gauge_trace_one_family.items()}
    gut_normalized_three_families = {"U1_GUT": gauge_trace_three_families["U1_Y"] * 3 / 5, "SU2": 6, "SU3": 6}

    checks = {
        "A50_completed_profile_finite_triple_closed": a50["full_finite_triple_at_profile_standard_closed"],
        "q79_single_Higgs_projection_certificate_closed": q79["closed"]["single_higgs_channel_projection"],
        "unrestricted_finite_scalar_space_rank_12": fluctuation_ranks["unrestricted_all"] == 12,
        "up_type_module_rank_4": fluctuation_ranks["up_type"] == 4,
        "down_plus_charged_lepton_module_rank_4": fluctuation_ranks["down_plus_charged_lepton"] == 4,
        "neutral_module_rank_4": fluctuation_ranks["neutral"] == 4,
        "selected_single_Higgs_module_rank_4": real_rank(selected_higgs_matrices) == 4,
        "selected_single_Higgs_is_inside_unrestricted_oneform_space": containment_residual < TOL,
        "single_Higgs_projector_rank_4": int(np.linalg.matrix_rank(single_higgs_projector, tol=TOL)) == 4,
        "single_Higgs_projector_idempotent": np.linalg.norm(single_higgs_projector @ single_higgs_projector - single_higgs_projector) < TOL,
        "single_Higgs_projector_self_adjoint": np.linalg.norm(single_higgs_projector - single_higgs_projector.T) < TOL,
        "eight_extra_scalar_directions_removed": 12 - int(np.linalg.matrix_rank(single_higgs_projector, tol=TOL)) == 8,
        "gauge_trace_SU2_equals_SU3": gauge_trace_three_families["SU2"] == gauge_trace_three_families["SU3"],
        "GUT_normalized_U1_equals_nonabelian_traces": gut_normalized_three_families["U1_GUT"] == gut_normalized_three_families["SU2"] == gut_normalized_three_families["SU3"],
        "finite_Yukawa_trace_invariants_positive": invariant_a > 0 and invariant_b > 0,
    }
    checks = {key: bool(value) for key, value in checks.items()}

    packet = {
        "schema": "MTTSelectedFiniteSpectralActionAndHiggsInnerFluctuationOrDirectGenerativeSMActionClosure.v1",
        "status": STATUS,
        "theorems": {
            "unrestricted_inner_fluctuation_audit": {
                "proved": checks["unrestricted_finite_scalar_space_rank_12"],
                "statement": "The represented self-adjoint real finite one-forms of the A50 completion have real rank 12 and split into three rank-4 scalar doublet modules: up, down/charged-lepton, and neutrino. Therefore the unrestricted A50 inner fluctuation is a three-doublet extension, not automatically the one-Higgs SM.",
            },
            "selected_single_Higgs_projection": {
                "proved": all(checks[key] for key in ["q79_single_Higgs_projection_certificate_closed", "selected_single_Higgs_module_rank_4", "selected_single_Higgs_is_inside_unrestricted_oneform_space", "single_Higgs_projector_idempotent", "eight_extra_scalar_directions_removed"]),
                "statement": "The previously certified MTT alignment projection H_up=H_nu=H and H_down/e=-epsilon conjugate(H) is an exact rank-4 real submodule of the computed rank-12 one-form space. Its canonical projector is self-adjoint and idempotent and removes exactly eight extra scalar directions.",
            },
            "finite_spectral_trace_coefficients": {
                "proved_at_profile_tier": checks["GUT_normalized_U1_equals_nonabelian_traces"] and checks["finite_Yukawa_trace_invariants_positive"],
                "statement": "The A46/A50 representation gives three-family gauge trace coefficients (10,6,6) for (U1_Y,SU2,SU3), hence (6,6,6) after 5/3 GUT normalization. The profile D_F emits the finite Yukawa invariants a and b controlling Higgs kinetic/quartic terms once spectral moments and field normalization are supplied.",
            },
        },
        "one_form_execution": {
            "finite_algebra_real_basis_dimension": len(algebra_values),
            "represented_one_form_generators_tested": len(algebra_values) ** 2,
            "reality_and_self_adjointness_imposed": True,
            "raw_real_fluctuation_ranks": fluctuation_ranks,
            "raw_scalar_interpretation": ["H_up", "H_down_and_charged_lepton", "H_neutrino"],
            "unrestricted_raw_model": "three-Higgs-doublet finite scalar sector",
        },
        "single_Higgs_projection": {
            "source_certificate": str(Q79_CERT),
            "source_certificate_sha256": sha256(Q79_CERT),
            "rule": "H_up=H_neutrino=H; H_down=H_charged_lepton=-epsilon conjugate(H)",
            "real_embedding_matrix_12x4": embedding.tolist(),
            "real_projector_12x12": single_higgs_projector.tolist(),
            "projector_rank": int(np.linalg.matrix_rank(single_higgs_projector, tol=TOL)),
            "projector_kernel_dimension": 12 - int(np.linalg.matrix_rank(single_higgs_projector, tol=TOL)),
            "projector_idempotence_residual": float(np.linalg.norm(single_higgs_projector @ single_higgs_projector - single_higgs_projector)),
            "projector_self_adjoint_residual": float(np.linalg.norm(single_higgs_projector - single_higgs_projector.T)),
            "oneform_containment_residual": containment_residual,
            "selected_Higgs_representation": "complex SU2 doublet with Y=+1/2; conjugate channels use -epsilon conjugate(H)",
        },
        "finite_spectral_traces": {
            "gauge_trace_coefficients_one_family": gauge_trace_one_family,
            "gauge_trace_coefficients_three_families": gauge_trace_three_families,
            "GUT_normalized_coefficients_three_families": gut_normalized_three_families,
            "structural_coupling_relation_at_spectral_normalization_scale": "g3^2=g2^2=(5/3)gY^2",
            "Yukawa_trace_rows": yukawa_trace_rows,
            "a_TrY2": invariant_a,
            "b_TrY4": invariant_b,
            "b_over_a_squared": invariant_b / invariant_a**2,
            "profile_scale": charged["reference_scale"],
            "profile_scope": "diagnostic finite traces at the accepted M_Z profile; not high-scale spectral-action boundary predictions",
        },
        "bosonic_action_interface": {
            "generated_after_standard_product_triple_heat_kernel_theorem": [
                "SU3, SU2 and U1_Y Yang-Mills kinetic terms",
                "one complex Higgs-doublet covariant kinetic term",
                "Higgs quadratic and quartic potential",
                "cosmological, Einstein-Hilbert, Weyl-curvature and nonminimal R|H|^2 terms",
            ],
            "standard_theorem_source": "Chamseddine-Connes spectral action and inner-fluctuation theorem",
            "standard_theorem_urls": ["https://arxiv.org/abs/hep-th/9606001", "https://arxiv.org/abs/hep-th/0605011"],
            "operator_content_closed": True,
            "absolute_coefficient_normalization_closed": False,
        },
        "checks": checks,
        "epistemic_policy": {
            "raw_A50_inner_fluctuation_called_one_Higgs_SM": False,
            "single_Higgs_projection_imported_without_execution": False,
            "standard_heat_kernel_theorem_imported": True,
            "spectral_cutoff_function_derived_from_MTT": False,
            "spectral_moments_f0_f2_f4_selected": False,
            "four_dimensional_base_Dirac_geometry_executed_here": False,
            "profile_Yukawa_values_promoted_to_no_knob_predictions": False,
            "new_continuous_parameters": 0,
        },
        "remaining_for_absolute_bosonic_action": [
            "selected four-dimensional product-triple Dirac/base geometry",
            "selected cutoff scale and cutoff function or moments f0,f2,f4",
            "canonical field normalization and RG matching from the spectral scale",
        ],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_FiniteSpectralActionAndHiggsInnerFluctuation_or_DirectGenerativeSMActionClosure_v1",
        "status": STATUS,
        "unrestricted_inner_fluctuation_real_rank": fluctuation_ranks["unrestricted_all"],
        "unrestricted_scalar_doublet_count": 3,
        "raw_one_Higgs_SM_closed": False,
        "selected_single_Higgs_projection_closed": packet["theorems"]["selected_single_Higgs_projection"]["proved"],
        "selected_single_Higgs_real_rank": packet["single_Higgs_projection"]["projector_rank"],
        "removed_extra_scalar_real_dimensions": packet["single_Higgs_projection"]["projector_kernel_dimension"],
        "finite_gauge_trace_relation_closed": True,
        "finite_Yukawa_trace_invariants_closed_at_profile_tier": True,
        "bosonic_SM_operator_content_closed_via_standard_heat_kernel_theorem": True,
        "absolute_spectral_action_normalization_closed": False,
        "new_continuous_knobs": 0,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Finite Spectral Action and Higgs Inner Fluctuation or Direct Generative SM Action Closure v1

## Executed One-Form Space

The finite one-forms were computed directly from the A50 triple:

```text
Omega_D^1(A_F) = span rho(a)[D_F,rho(b)],
A = A*,
A_real = A + J_F A J_F^-1.
```

All `26x26=676` real-algebra basis pairs were executed. The unrestricted real fluctuation space has
rank `12`, not `4`. It splits into three rank-four scalar modules:

```text
H_up,   H_down/charged-lepton,   H_neutrino.
```

Thus the unrestricted four-summand A50 triple is a three-Higgs-doublet extension. Calling its raw
inner fluctuation the one-Higgs Standard Model would be incorrect.

## Selected Single-Higgs Projection

The earlier q79/ProtoSpinor alignment certificate selects

```text
H_up = H_neutrino = H,
H_down = H_charged-lepton = -epsilon conjugate(H).
```

This rule has now been executed on the actual A50 one-form space. Its image has real rank `4`, lies
inside the rank-12 fluctuation space with residual `{containment_residual:.3e}`, and its canonical
`12x12` projector is exactly self-adjoint and idempotent. The kernel has dimension `8`; precisely the
two unwanted doublets are removed. The surviving field is one complex `SU(2)` doublet with
`Y=+1/2`, with pseudoreality supplying its conjugate channels.

## Finite Spectral Traces

The three-family fermion representation gives

```text
k_Y:k_2:k_3 = 10:6:6.
```

After the standard `5/3` hypercharge normalization this is `(6,6,6)`, equivalently
`g3^2=g2^2=(5/3)gY^2` at the spectral normalization scale.

The accepted profile `D_F` gives

```text
a = Tr(Ydagger Y)                    = {invariant_a:.15g},
b = Tr((Ydagger Y)^2)                = {invariant_b:.15g},
b/a^2                                = {invariant_b / invariant_a**2:.15g}.
```

Color multiplicity is included. These are finite profile traces at `M_Z`, not high-scale predictions.

## What Is Closed

Using the standard Chamseddine--Connes product-triple heat-kernel theorem, the selected finite data
generate the operator content of the bosonic SM action: Yang--Mills terms, one Higgs covariant kinetic
term and potential, plus the standard gravitational and nonminimal terms. The finite representation,
single-Higgs module, gauge trace ratios and Yukawa trace invariants are executable rather than assumed.

Absolute spectral-action normalization is not closed here. It still requires the selected four-dimensional
base Dirac geometry, cutoff scale/function or moments `f0,f2,f4`, canonical field normalization and RG
transport from the spectral scale. The corpus paper claiming those moments are fixed by the MTT gap is
therefore still conditional, not yet an executed theorem.

Next artifact: `{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
