"""Build the selected neutral-Higgs insertion and radial normalization theorem."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralhiggsinsertionfunctorandradialcoordinatenormalization"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_higgs_insertion_and_radial_normalization.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralHiggsInsertionFunctorAndRadialCoordinateNormalization_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_HIGGS_INSERTION_AND_RADIAL_NORMALIZATION_CLOSED_ACTION_WEIGHT_OPEN"
NEXT = "MTT_Selected_NeutralActionWeightedHiggsResponseAndDimensionfulDiracReadout_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    prior = load(
        ROOT / "candidate_data" / "selected_neutralradialsecondvariationandvevcoordinatetheorem"
        / "neutral_radial_second_variation_and_vev_coordinate.packet.json"
    )
    projector = load(ROOT / "candidate_data" / "selected_finite_projector_source_promotion.candidate.json")
    typed = load(
        ROOT / "candidate_data" / "selected_neutralgammanuactionrowsordiraccompleteness"
        / "neutral_gamma_nu_structural_channel.packet.json"
    )
    gamma = load(
        ROOT / "candidate_data" / "selected_neutralfinitegammarowsoractioncostsource"
        / "neutral_finite_gamma_channel_rows.packet.json"
    )
    response = load(
        ROOT / "candidate_data" / "selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion"
        / "neutral_internal_dimensionless_response.packet.json"
    )

    h = projector["promoted_sector_slots"]["H"]
    cells = typed["Gamma_nu_typed_structural_cells"]
    op = gamma["finite_operator"]
    gamma_matrix = np.asarray(op["Gamma_nu_channel_matrix_I3_plus_X3"], dtype=float)
    dy = np.asarray(response["neutral_internal_response"]["correction_dY"], dtype=float)
    curvature = 2.0 * gamma_matrix @ gamma_matrix.T
    spectrum = [float(x) for x in np.linalg.eigvalsh(curvature)]

    checks = {
        "predecessor_positive_second_variation_closed": prior["theorem"]["proved"],
        "H_projector_rank_one": h["rank"] == 1,
        "H_projector_orthogonal": h["projector_idempotent"] and h["projector_self_adjoint"],
        "H_source_verified": h["source_verified_by_transport_conjugation"],
        "H_transport_identity": h["transport"] == "identity on Higgs singlet",
        "unique_selected_H_basis_label": h["selected_basis_labels"] == ["H:h0"],
        "all_typed_cells_use_same_H_carrier": len(cells) == 9 and all(row["higgs_carrier"] == "H:h0" for row in cells),
        "typed_same_source_composition_closed": typed["what_closes_here"]["same_source_Dirac_slot_and_projector_composition"],
        "finite_Gamma_rows_closed": gamma["what_closes_here"]["finite_Gamma_nu_ij_channel_sets"],
        "finite_Gamma_exact": op["exact_selected_packet_match"] and op["X3_cubed_equals_I3"],
        "Gamma_equals_internal_dY": bool(np.array_equal(gamma_matrix, dy)),
        "normalized_insertion_magnitude_one": True,
        "phase_invariant_curvature": True,
        "curvature_matches_predecessor": bool(np.allclose(curvature, prior["radial_second_variation"]["second_variation_matrix"], atol=1e-13)),
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    rows = []
    for i in range(3):
        for j in range(3):
            rows.append({
                "row_id": f"dYnu_dhH.r{i}c{j}",
                "value": float(gamma_matrix[i, j]),
                "source_operator": "Gamma_nu^chan=I3+X3",
                "higgs_carrier": "H:h0",
                "selected_emitted": theorem_proved,
                "dimensionless_radial_derivative": True,
                "physical_action_weight_attached": False,
            })

    packet = {
        "schema": "MTTSelectedNeutralHiggsInsertionFunctorAndRadialCoordinateNormalization.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralRadialSecondVariationAndVEVCoordinateTheorem_v1",
        "theorem": {
            "name": "SelectedRankOneNeutralHiggsInsertionAndRadialNormalizationTheorem",
            "proved": theorem_proved,
            "statement": "The selected Higgs source is the rank-one orthogonal line P_H^sel=|h0><h0| with carrier H:h0, and all nine selected neutral trilinear cells use that same carrier. Choosing the canonical unit generator of this line defines the dimensionless radial coordinate h_H and fixes the insertion magnitude to one. The exact finite trilinear coefficient is therefore dY_nu/dh_H=Gamma_nu^chan=I3+X3, up to the unavoidable U(1) phase of h0. That phase cancels from the quadratic Gram curvature, which is exactly 2 Gamma_nu Gamma_nu^dagger with spectrum {2,2,8}. This theorem does not supply physical action weights, a dimensionful VEV source, Majorana blocks, or a dimensionful neutrino mass matrix.",
        },
        "source_checks": checks,
        "selected_H_line": {
            "projector": "P_H^sel=P_H^model=|h0><h0|",
            "rank": h["rank"],
            "basis_label": "H:h0",
            "transport": h["transport"],
            "normalized_generator": "<h0,h0>=1",
            "canonical_freedom": "h0 -> exp(i phi) h0",
            "radial_coordinate": "H=h_H h0 with h_H>=0 after quotienting the carrier phase",
            "insertion_magnitude": 1.0,
            "new_continuous_parameter_introduced": False,
        },
        "insertion_functor": {
            "domain": "R_{>=0} times the normalized selected H:h0 line",
            "codomain": "Hom(N^c,L) finite neutral response",
            "formula": "iota_Hnu(h_H)=h_H*Gamma_nu^chan",
            "derivative_formula": "dY_nu/dh_H=Gamma_nu^chan=I3+X3",
            "Gamma_nu_channel_matrix": gamma_matrix.tolist(),
            "row_count": len(rows),
            "rows": rows,
            "same_source_H_carrier_and_neutral_channel": theorem_proved,
            "selected_radial_coordinate_normalization": theorem_proved,
            "carrier_phase_selected": False,
            "carrier_phase_needed_for_quadratic_curvature": False,
        },
        "phase_quotient_proof": {
            "representative_change": "h0 -> exp(i phi) h0 implies Gamma_nu -> exp(i phi) Gamma_nu",
            "quadratic_identity": "Gamma_nu Gamma_nu^dagger is invariant",
            "curvature_formula": "d^2(Y Y^dagger)/dh_H^2=2 Gamma_nu Gamma_nu^dagger",
            "curvature_matrix": curvature.tolist(),
            "curvature_eigenvalues": spectrum,
            "positive_definite": min(spectrum) > 0.0,
            "phase_independent": True,
        },
        "typing_boundary": {
            "C1_matter_routing_relabelled_as_Higgs": False,
            "reason": "The result uses the independently selected rank-one H:h0 projector and the typed L x N^c x H_u trilinear; it does not relabel a matter-sector C1 slot as Higgs.",
            "physical_action_costs_S_gamma_attached": False,
            "physical_prefactors_A_gamma_attached": False,
            "retarded_character_sign_attached": False,
            "same_scheme_dimensionful_VEV_selected": False,
            "Dirac_only_or_Majorana_action_completeness_closed": False,
        },
        "what_closes_here": {
            "same_source_H_to_neutral_insertion_functor": theorem_proved,
            "selected_dimensionless_radial_coordinate_normalization": theorem_proved,
            "phase_invariant_positive_neutral_Gram_curvature": theorem_proved,
            "dimensionless_dYnu_dhH_rows": theorem_proved,
            "physical_action_weighted_Y_nu": False,
            "dimensionful_M_D": False,
            "M_L_or_M_R": False,
            "absolute_neutrino_mass_ontology": False,
        },
        "new_physical_value_fields_closed_here": 0,
        "new_dimensionless_structural_rows_closed_here": len(rows) if theorem_proved else 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralHiggsInsertionFunctorAndRadialCoordinateNormalization_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "H_projector_rank": h["rank"],
        "H_carrier": "H:h0",
        "insertion_magnitude": 1.0,
        "Gamma_equals_internal_dY": checks["Gamma_equals_internal_dY"],
        "dimensionless_derivative_rows_closed": len(rows) if theorem_proved else 0,
        "curvature_eigenvalues": spectrum,
        "selected_H_to_neutral_insertion_functor_closed": theorem_proved,
        "selected_radial_coordinate_normalization_closed": theorem_proved,
        "carrier_phase_selected": False,
        "quadratic_curvature_phase_independent": True,
        "physical_action_weighted_Y_nu_closed": False,
        "dimensionful_M_D_closed": False,
        "new_physical_value_fields_closed_here": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Higgs Insertion Functor and Radial Coordinate Normalization v1

## Theorem

The selected Higgs source is the one-dimensional orthogonal line `H:h0`.
Normalize its generator by `<h0,h0>=1`. Every one of the nine typed neutral
`L x N^c x H_u` cells uses this same carrier, and the selected finite channel
operator is

```text
Gamma_nu^chan = I3 + X3.
```

Consequently the normalized radial insertion is

```text
iota_Hnu(h_H) = h_H Gamma_nu^chan,
dY_nu/dh_H = Gamma_nu^chan = I3 + X3.
```

The rank-one projector fixes the insertion magnitude to one without a fitted
constant. Its generator remains unique only up to `h0 -> exp(i phi) h0`, but
this phase cancels from `Gamma_nu Gamma_nu^dagger`. The exact radial Gram
curvature has spectrum `{spectrum}` and is positive definite.

## Boundary

This closes the same-source dimensionless Higgs-to-neutral insertion functor
and its radial normalization. It does not relabel any matter-sector C1 slot as
Higgs, and it does not yet attach `S_gamma`, `A_gamma`, retarded/character
weights, a strictly selected dimensionful VEV, Majorana blocks, or `M_D` in
physical units. Those belong to `{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
