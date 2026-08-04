"""Build the neutral effective-weight identifiability reduction theorem."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraleffectiveweightidentifiabilityreduction"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_effective_weight_identifiability.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralEffectiveWeightIdentifiabilityReduction_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_EFFECTIVE_WEIGHT_CLOSED_SEPARATE_AS_ROWS_RETIRED_PHYSICAL_SHAPE_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralPhysicalShapeOperatorAndAbsoluteScale_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cmatrix(value: list) -> np.ndarray:
    return np.asarray([[complex(*x) if isinstance(x, list) else complex(x) for x in row] for row in value])


def main() -> int:
    insertion = load(
        ROOT / "candidate_data" / "selected_neutralhiggsinsertionfunctorandradialcoordinatenormalization"
        / "neutral_higgs_insertion_and_radial_normalization.packet.json"
    )
    internal = load(
        ROOT / "candidate_data" / "selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion"
        / "neutral_internal_dimensionless_response.packet.json"
    )
    orbit = load(
        ROOT / "candidate_data" / "selected_neutralactioncostprefactorordiracmajoranacompletion"
        / "neutral_second_order_relative_amplitude_orbit.packet.json"
    )
    obstruction = load(
        ROOT / "candidate_data" / "selected_neutralphysicalunitornilanchorprojector"
        / "neutral_scale_invariant_obstruction_and_spectral_repair.packet.json"
    )

    response = internal["neutral_internal_response"]
    dy = np.asarray(response["correction_dY"], dtype=float)
    gamma = np.asarray(insertion["insertion_functor"]["Gamma_nu_channel_matrix"], dtype=float)
    a_int = float(response["a_internal"])

    t = 0.731
    A0 = a_int
    S0 = 0.0
    W0 = A0 * math.exp(-S0)
    A1 = math.exp(t) * A0
    S1 = S0 + t
    W1 = A1 * math.exp(-S1)

    representatives = [cmatrix(row["Gamma_nu_relative_matrix"]) for row in orbit["selected_relative_amplitude_orbit"]]
    gram_spectra = [np.linalg.eigvalsh(matrix @ matrix.conj().T).tolist() for matrix in representatives]
    conjugate_equal = bool(np.allclose(representatives[1], representatives[0].conj(), atol=1e-13))
    spectra_equal = bool(np.allclose(gram_spectra[0], gram_spectra[1], atol=1e-13))

    checks = {
        "A35_insertion_closed": insertion["theorem"]["proved"],
        "combined_internal_overlap_closed": internal["what_closes_here"]["combined_internal_overlap_amplitude"],
        "same_source_internal_fields_complete": internal["source_provenance"]["same_source_selected_field_count"] == internal["source_provenance"]["same_source_required_field_count"] == 7,
        "effective_derivative_equals_normalized_Gamma": bool(np.array_equal(dy, gamma)),
        "factorization_gauge_identity_exact_numerically": abs(W0 - W1) < 1e-15,
        "conjugate_orbit_closed": orbit["theorem"]["proved"] and len(representatives) == 2,
        "orbit_representatives_are_conjugate": conjugate_equal,
        "mass_Gram_spectra_equal": spectra_equal,
        "scale_only_route_rejected": obstruction["theorem"]["proved"],
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedNeutralEffectiveWeightIdentifiabilityReduction.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralHiggsInsertionFunctorAndRadialCoordinateNormalization_v1",
        "theorem": {
            "name": "NeutralEffectiveWeightFactorizationGaugeAndPhysicalCutsetTheorem",
            "proved": theorem_proved,
            "statement": "In the already-declared neutral amplitude law W_gamma=A_gamma exp(-S_gamma) sign_gamma, separate positive A_gamma and real S_gamma are non-identifiable: for every real t, (A_gamma,S_gamma)->(exp(t)A_gamma,S_gamma+t) leaves W_gamma invariant. The selected same-source packet already emits the combined internal dimensionless response W_gamma Gamma_nu, and A35 identifies its normalized Higgs derivative with I3+X3. Therefore separate A_gamma and S_gamma rows are retired as independent physical closure obligations; only their effective product can be selected. The conjugate relative representatives have identical mass-Gram spectra, so representative selection is unnecessary for masses but remains relevant to CP-sensitive observables. Physical completion still requires a selected non-affine neutral shape operator and one absolute scale; the earlier scale-only no-go remains in force.",
        },
        "source_checks": checks,
        "factorization_gauge": {
            "amplitude_law": "W_gamma=A_gamma*exp(-S_gamma)*sign_gamma",
            "redundancy": "A_gamma -> exp(t) A_gamma; S_gamma -> S_gamma+t",
            "invariant": "A_gamma*exp(-S_gamma)",
            "numeric_witness_t": t,
            "before": {"A_gamma": A0, "S_gamma": S0, "effective_weight": W0},
            "after": {"A_gamma": A1, "S_gamma": S1, "effective_weight": W1},
            "separate_A_gamma_and_S_gamma_identifiable": False,
            "separate_rows_required_for_physical_closure": False,
        },
        "selected_effective_internal_response": {
            "a_internal": a_int,
            "combined_internal_overlap_amplitude_closed": True,
            "normalized_Higgs_derivative": dy.tolist(),
            "equals_Gamma_nu_I3_plus_X3": checks["effective_derivative_equals_normalized_Gamma"],
            "same_source_provenance_fields": "7/7",
            "physical_Y_nu": False,
            "dimensionful_mass": False,
        },
        "conjugate_orbit_mass_equivalence": {
            "representative_count": len(representatives),
            "representatives_are_complex_conjugates": conjugate_equal,
            "Gram_spectra": gram_spectra,
            "mass_spectra_equal": spectra_equal,
            "representative_selection_needed_for_mass_eigenvalues": False,
            "representative_selection_needed_for_CP_sensitive_observables": True,
        },
        "reduced_physical_cutset": {
            "retired_artificial_requirements": [
                "separate A_gamma row after effective W_gamma is selected",
                "separate S_gamma row after effective W_gamma is selected",
                "unique conjugate representative for mass eigenvalues",
            ],
            "still_required": [
                "source-selected non-affine neutral shape operator or Majorana/seesaw real-structure block",
                "one same-scheme absolute physical scale",
                "branch/retarded representative only for CP-sensitive neutral observables",
                "Dirac-only completeness or selected M_L/M_R ontology",
            ],
            "minimum_new_continuous_physical_coordinates_for_Dirac_shape_and_scale": 2,
            "coordinates": ["non-affine shape coordinate beta_nu", "absolute scale mu_nu"],
            "reason_two_not_one": "A31 proves any common scale leaves the wrong hierarchy ratio invariant; one scale cannot repair shape",
            "one_to_three_knob_policy_compatible": True,
        },
        "what_closes_here": {
            "effective_internal_action_weight_product": theorem_proved,
            "A_gamma_S_gamma_factorization_nonidentifiability": theorem_proved,
            "separate_A_gamma_S_gamma_obligations_retired": theorem_proved,
            "conjugate_representative_mass_equivalence": theorem_proved,
            "physical_non_affine_shape_operator": False,
            "absolute_physical_scale": False,
            "dimensionful_M_D": False,
            "absolute_neutrino_mass_ontology": False,
        },
        "new_physical_value_fields_closed_here": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralEffectiveWeightIdentifiabilityReduction_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "combined_internal_effective_weight_closed": theorem_proved,
        "separate_A_gamma_S_gamma_identifiable": False,
        "separate_A_gamma_S_gamma_obligations_retired": theorem_proved,
        "conjugate_representative_mass_equivalence_closed": theorem_proved,
        "minimum_new_continuous_physical_coordinates": 2,
        "physical_shape_operator_closed": False,
        "absolute_physical_scale_closed": False,
        "dimensionful_M_D_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Effective Weight Identifiability Reduction v1

## Factorization theorem

The neutral amplitude was written schematically as

```text
W_gamma = A_gamma exp(-S_gamma) sign_gamma.
```

But `A_gamma` and `S_gamma` are not separately identifiable. For any real `t`,

```text
A_gamma -> exp(t) A_gamma,
S_gamma -> S_gamma+t
```

leaves `W_gamma` unchanged. Requiring two separately selected rows after their
combined effective response has already been emitted is therefore redundant.
The A30 same-source packet closes that internal product, and A35 proves its
normalized Higgs derivative is exactly `I3+X3`.

The two conjugate relative representatives have identical mass-Gram spectra
`{gram_spectra[0]}`. Selecting one is unnecessary for mass eigenvalues, though
it remains necessary for CP-sensitive observables.

## Reduced frontier

Physical closure still needs two identifiable ingredients: a source-selected
non-affine neutral shape coordinate/operator and one same-scheme absolute
scale. A scale alone cannot work because A31 proves it preserves the wrong
hierarchy ratio. This two-coordinate frontier is compatible with the adopted
one-to-three-knob research policy, but neither coordinate is selected here.

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
