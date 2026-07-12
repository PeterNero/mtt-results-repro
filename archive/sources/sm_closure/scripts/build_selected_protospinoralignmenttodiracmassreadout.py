"""Build the proto-spinor alignment-to-Dirac finite readout theorem."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_protospinoralignmenttodiracmassreadout"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "protospinor_finite_dirac_and_alignment_readout.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ProtoSpinorAlignmentToDiracMassReadout_v1.md"
STATUS = "MTT_SELECTED_PROTOSPINOR_FINITE_DIRAC_READOUT_CLOSED_RADIAL_SECOND_VARIATION_OPEN"
NEXT = "MTT_Selected_NeutralRadialSecondVariationAndVEVCoordinateTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clean(values: np.ndarray, tol: float = 1e-14) -> list[float]:
    return [0.0 if abs(float(value)) < tol else float(value) for value in values]


def main() -> int:
    typed = load(
        ROOT / "candidate_data" / "selected_neutralgammanuactionrowsordiraccompleteness"
        / "neutral_gamma_nu_structural_channel.packet.json"
    )
    finite = load(
        ROOT / "candidate_data" / "selected_neutralfinitegammarowsoractioncostsource"
        / "neutral_finite_gamma_channel_rows.packet.json"
    )
    internal = load(
        ROOT / "candidate_data" / "selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion"
        / "neutral_internal_dimensionless_response.packet.json"
    )
    predecessor = load(
        ROOT / "candidate_data" / "selected_neutralspectralactionslopeorseesawsource"
        / "neutral_spectral_and_seesaw_source_discrimination.packet.json"
    )

    response = internal["neutral_internal_response"]
    a = float(response["a_internal"])
    y0 = np.asarray(response["baseline_Y0"], dtype=float)
    dy = np.asarray(response["correction_dY"], dtype=float)
    h1 = np.asarray(response["first_hermitian_response_H1"], dtype=float)
    h2 = dy @ dy.T
    zero = np.zeros((3, 3), dtype=float)
    d6 = np.block([[zero, dy], [dy.T, zero]])
    chirality = np.diag([-1.0] * 3 + [1.0] * 3)
    coefficient_matched_y = y0 + a * dy
    coefficient_matched_d6 = np.block([[zero, coefficient_matched_y], [coefficient_matched_y.T, zero]])
    gram = coefficient_matched_y @ coefficient_matched_y.T

    h1_eigenvalues = clean(np.linalg.eigvalsh(h1))
    h2_eigenvalues = clean(np.linalg.eigvalsh(h2))
    d6_eigenvalues = clean(np.linalg.eigvalsh(d6))
    matched_singular_values = clean(np.linalg.svd(coefficient_matched_y, compute_uv=False)[::-1])
    matched_gram_eigenvalues = clean(np.linalg.eigvalsh(gram))
    matched_d6_eigenvalues = clean(np.linalg.eigvalsh(coefficient_matched_d6))
    matched_ratio = (matched_gram_eigenvalues[1] - matched_gram_eigenvalues[0]) / (
        matched_gram_eigenvalues[2] - matched_gram_eigenvalues[0]
    )
    postcheck = predecessor["spectral_action_route"]["postcheck_ratio"]

    checks = {
        "selected_left_rank_three": typed["proof_inputs"]["selected_L_projector_rank"] == 3,
        "selected_right_rank_three": typed["proof_inputs"]["selected_Nc_projector_rank"] == 3,
        "selected_typed_dirac_slots": typed["typed_cell_count"] == 9,
        "selected_transfer_full_rank": finite["finite_operator"]["operator_rank"] == 3,
        "selected_transfer_determinant_two": abs(finite["finite_operator"]["determinant"] - 2.0) < 1e-15,
        "finite_dirac_self_adjoint": np.linalg.norm(d6 - d6.T) < 1e-14,
        "finite_dirac_chirally_odd": np.linalg.norm(chirality @ d6 + d6 @ chirality) < 1e-14,
        "H1_is_indefinite": min(h1_eigenvalues) < 0.0 < max(h1_eigenvalues),
        "H2_is_positive_semidefinite": min(h2_eigenvalues) >= 0.0,
        "coefficient_matched_nil_mode": matched_gram_eigenvalues[0] == 0.0,
        "coefficient_matched_ratio_not_postcheck": abs(matched_ratio - postcheck) > 0.2,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedProtoSpinorAlignmentToDiracMassReadout.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralSpectralActionSlopeOrSeesawSource_v1",
        "theorem": {
            "name": "SelectedProtoSpinorFiniteDiracRealizationAndAlignmentReadoutTheorem",
            "proved": theorem_proved,
            "statement": "The selected rank-three L and N^c carriers, nine typed L x N^c x H_u slots, and full-rank I3+X3 transfer define an explicit finite Dirac encoding D_F=[[0,Y],[Y^dagger,0]] that is self-adjoint and odd under chirality. This closes existence of the finite Dirac encoding, not exclusion of a separate Majorana extension. The already selected H1 is indefinite and therefore cannot itself be the positive mass-squared Hessian. The source-coefficient-matched trial Y(a)=Y0+a dY has singular values {0,a,2a}, automatically supplying a nil-anchored zero mode but giving splitting ratio 1/4 rather than the downstream postcheck. The remaining source object is the selected radial second variation and VEV coordinate that converts the carrier response into the anchored Yukawa/mass readout.",
        },
        "source_checks": checks,
        "finite_dirac_encoding": {
            "left_weyl_carrier_rank": 3,
            "right_weyl_carrier_rank": 3,
            "selected_transfer": "I3+X3",
            "selected_transfer_rank": int(np.linalg.matrix_rank(dy)),
            "selected_transfer_determinant": float(np.linalg.det(dy)),
            "operator_formula": "D_F^D(Y)=[[0,Y],[Y^dagger,0]]",
            "operator_dimension": 6,
            "self_adjoint": checks["finite_dirac_self_adjoint"],
            "chirality_formula": "Gamma_F=diag(-I3,+I3)",
            "chirally_odd": checks["finite_dirac_chirally_odd"],
            "eigenvalues_for_Y_equals_dY": d6_eigenvalues,
            "finite_Dirac_encoding_exists": theorem_proved,
            "Dirac_only_action_completeness": False,
            "Majorana_extension_excluded": False,
        },
        "alignment_response_typing": {
            "a_internal": a,
            "Y_of_h_formula": "Y(h)=Y0+h*dY",
            "Gram_formula": "G(h)=Y(h)Y(h)^dagger=Y0Y0^dagger+h H1+h^2 H2",
            "H1_formula": "dY Y0^dagger+Y0 dY^dagger",
            "H1_eigenvalues": h1_eigenvalues,
            "H1_positive_semidefinite": False,
            "H1_can_be_physical_mass_squared_Hessian": False,
            "H2_formula": "dY dY^dagger",
            "H2_eigenvalues": h2_eigenvalues,
            "H2_positive_semidefinite": True,
            "selected_radial_coordinate_h_star_emitted": False,
            "selected_radial_second_variation_emitted": False,
            "selected_Yukawa_readout_emitted": False,
        },
        "coefficient_matched_alignment_trial": {
            "classification": "SOURCE_COEFFICIENT_MATCHED_DIAGNOSTIC_NOT_SELECTED_VEV_COORDINATE",
            "trial_coordinate": "h=a_internal",
            "trial_matrix": coefficient_matched_y.tolist(),
            "singular_values": matched_singular_values,
            "Gram_eigenvalues": matched_gram_eigenvalues,
            "Dirac_operator_eigenvalues": matched_d6_eigenvalues,
            "nil_anchored_zero_mode": matched_gram_eigenvalues[0] == 0.0,
            "splitting_ratio": matched_ratio,
            "postcheck_ratio": postcheck,
            "absolute_residual": abs(matched_ratio - postcheck),
            "accepted_as_physical_prediction": False,
        },
        "mass_readout_contract": {
            "Yukawa_formula": "Y_nu,ij=(partial_h partial_barL_i partial_Nc_j J)|align",
            "Dirac_mass_formula": "M_D=v_align*Y_nu",
            "mass_squared_formula": "spec(M_D M_D^dagger)",
            "required_source_fields": [
                "selected alignment basepoint Xi_align",
                "selected radial coordinate h and physical alignment scale v_align",
                "selected mixed radial third derivative or equivalent second-variation transfer",
                "positive anchored quotient after removal of gauge-flat lens directions",
                "same-source normalization and no-observed-selector certificate",
            ],
            "emitted_source_fields": [
                "selected left/right Weyl carriers",
                "selected finite stabilized transfer",
                "selected Y0, dY, H1 response data",
                "finite Dirac operator and chirality grading",
            ],
        },
        "what_closes_here": {
            "finite_proto_spinor_to_Dirac_encoding": theorem_proved,
            "left_right_Weyl_block_realization": theorem_proved,
            "finite_stabilized_transfer_realization": theorem_proved,
            "H1_not_mass_squared_Hessian_no_go": theorem_proved,
            "coefficient_matched_nil_mode_diagnostic": theorem_proved,
            "Dirac_only_action_completeness": False,
            "selected_radial_second_variation": False,
            "selected_VEV_coordinate": False,
            "dimensionless_Y_nu_physical_readout": False,
            "dimensionful_M_D": False,
        },
        "neutral_overlap_OK_gates_closed": predecessor["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": predecessor["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": predecessor["readiness_subfields_closed"],
        "readiness_subfields_total": predecessor["readiness_subfields_total"],
        "new_physical_value_fields_closed_here": 0,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_ProtoSpinorAlignmentToDiracMassReadout_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "finite_Dirac_encoding_closed": theorem_proved,
        "Dirac_only_action_completeness_closed": False,
        "H1_eigenvalues": h1_eigenvalues,
        "H1_rejected_as_mass_squared_Hessian": theorem_proved,
        "H2_eigenvalues": h2_eigenvalues,
        "coefficient_matched_singular_values": matched_singular_values,
        "coefficient_matched_Gram_eigenvalues": matched_gram_eigenvalues,
        "coefficient_matched_ratio": matched_ratio,
        "coefficient_matched_trial_selected_as_VEV": False,
        "selected_radial_second_variation_closed": False,
        "selected_VEV_coordinate_closed": False,
        "dimensionful_M_D_closed": False,
        "neutral_overlap_OK_gates_closed": packet["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": packet["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": packet["readiness_subfields_closed"],
        "readiness_subfields_total": packet["readiness_subfields_total"],
        "new_physical_value_fields_closed_here": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Proto-Spinor Alignment to Dirac Mass Readout v1

## Finite Dirac encoding

The selected rank-three `L` and `N^c` carriers are the two Weyl blocks. The
selected full-rank transfer `Y=dY=I3+X3` defines

```text
D_F^D(Y) = [[0,Y],[Y^dagger,0]],
Gamma_F  = diag(-I3,+I3).
```

The resulting `6x6` operator is self-adjoint and anticommutes with `Gamma_F`.
This closes a finite proto-spinor-to-Dirac encoding. It does not prove that a
separate Majorana extension is impossible.

## Alignment readout

The selected response obeys

```text
Y(h)=Y0+h*dY,
G(h)=Y(h)Y(h)^dagger=Y0Y0^dagger+h*H1+h^2*H2.
```

`H1` has eigenvalues `{h1_eigenvalues}` and is indefinite. It therefore cannot
be identified with the positive physical mass-squared Hessian. `H2=dY dY^dagger`
has eigenvalues `{h2_eigenvalues}` and is positive semidefinite.

The coefficient-matched trial `h=a_internal` gives singular values
`{matched_singular_values}` and Gram spectrum `{matched_gram_eigenvalues}`. It
automatically contains a nil-anchored zero mode, but its splitting ratio is
`{matched_ratio}`, not the downstream postcheck `{postcheck}`. Since the corpus
has not selected `h=a_internal` as the physical VEV coordinate, this remains a
diagnostic rather than a prediction.

## Exact frontier

The next theorem must emit the radial second variation and the selected VEV
coordinate, then evaluate

```text
Y_nu,ij=(partial_h partial_barL_i partial_Nc_j J)|align,
M_D=v_align*Y_nu.
```

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
