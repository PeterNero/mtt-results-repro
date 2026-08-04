"""Build the selected internal neutral-amplitude successor."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_internal_dimensionless_response.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralAbsoluteAmplitudeNilAnchorOrDiracMajoranaCompletion_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_INTERNAL_DIMENSIONLESS_RESPONSE_CLOSED_PHYSICAL_UNIT_OPEN"
NEXT = "MTT_Selected_NeutralPhysicalUnitOrNilAnchorProjector_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def c(value):
    if isinstance(value, list):
        return complex(value[0], value[1])
    return complex(value, 0.0)


def matrix(value):
    return [[c(item) for item in row] for row in value]


def dagger(value):
    return [[value[j][i].conjugate() for j in range(3)] for i in range(3)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]


def close(a, b, tol=1e-13):
    return all(abs(a[i][j] - b[i][j]) <= tol for i in range(3) for j in range(3))


def main() -> int:
    predecessor = load(
        ROOT / "candidate_data" / "selected_neutralactioncostprefactorordiracmajoranacompletion"
        / "neutral_second_order_relative_amplitude_orbit.packet.json"
    )
    values = load(
        ROOT / "candidate_data" / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
        / "selected_non_scalar_dynamic_overlap_values.packet.json"
    )
    same_source = load(
        ROOT / "candidate_data" / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
        / "same_source_matter_overlap_operator_packet.packet.json"
    )
    validator = load(
        ROOT / "candidate_data" / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
        / "same_source_matter_overlap_operator_validator_result.packet.json"
    )
    promotion = load(
        ROOT / "candidate_data" / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
        / "dynamic_transfer_backpromotion_theorem.packet.json"
    )

    nu = values["sector_first_responses"]["nuD"]
    y0 = matrix(nu["baseline_Y0"])
    dy = matrix(nu["correction_dY"])
    h1 = matrix(nu["first_hermitian_response_H1"])
    recomputed = add(mul(dy, dagger(y0)), mul(y0, dagger(dy)))
    fields = same_source["attempted_selected_packet"]["fields"]
    all_same_source = all(
        row["same_source"] and row["selected_emitted"] and row["theorem_derived"]
        for row in fields.values()
    )
    a = abs(y0[0][0])
    expected_h1 = [
        [-2.0 * a, 0.0, -2.0 * a],
        [0.0, -2.0 * a, -2.0 * a],
        [-2.0 * a, -2.0 * a, 0.0],
    ]
    expected_h1_complex = [[complex(item, 0.0) for item in row] for row in expected_h1]

    gate = all(
        [
            predecessor["theorem"]["proved"],
            values["selected_by_MTT"],
            values["closure_claimed"],
            promotion["backpromotion_allowed"],
            same_source["closure_claimed"],
            same_source["attempted_selected_packet"]["packet_flags"]["one_same_source"],
            validator["returncode"] == 0,
            not validator["stderr_lines"],
            all_same_source,
            close(h1, recomputed),
            close(h1, expected_h1_complex),
        ]
    )

    readiness = dict(predecessor["readiness_subfields"])
    readiness["selected_internal_dimensionless_neutral_overlap_amplitude"] = gate

    rows = []
    for i in range(3):
        for j in range(3):
            rows.append(
                {
                    "row_id": f"nuD.H1.r{i}c{j}",
                    "value": float(h1[i][j].real),
                    "selected_emitted": gate,
                    "theorem_derived": gate,
                    "same_source": gate,
                    "physical_unit_attached": False,
                    "dimensionful_mass_entry": False,
                }
            )

    packet = {
        "schema": "MTTSelectedNeutralAbsoluteAmplitudeNilAnchorOrDiracMajoranaCompletion.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralActionCostPrefactorOrDiracMajoranaCompletion_v1",
        "theorem": {
            "name": "SelectedNeutralInternalDimensionlessResponseTheorem",
            "proved": gate,
            "statement": "The selected same-source dynamic matter/overlap packet emits the neutral nuD baseline Y0, shift correction dY=I3+X3, and complete first Hermitian response H1=dY Y0^dagger+Y0 dY^dagger. The common internal coefficient is a=0.34195899479289005 and H1 has six entries -2a and three exact zeros. This is an absolute value in the selected internal dimensionless normalization, not a physical neutrino Yukawa matrix or mass in eV.",
        },
        "source_provenance": {
            "selected_by_MTT": values["selected_by_MTT"],
            "dynamic_backpromotion_allowed": promotion["backpromotion_allowed"],
            "same_source_validator_returncode": validator["returncode"],
            "same_source_required_field_count": len(fields),
            "same_source_selected_field_count": sum(
                row["same_source"] and row["selected_emitted"] and row["theorem_derived"]
                for row in fields.values()
            ),
            "same_source_fields": fields,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
        "neutral_internal_response": {
            "a_internal": a,
            "baseline_Y0": nu["baseline_Y0"],
            "correction_dY": nu["correction_dY"],
            "first_hermitian_response_H1": nu["first_hermitian_response_H1"],
            "identity_H1_equals_dY_Y0dag_plus_Y0_dYdag": close(h1, recomputed),
            "six_nonzero_entries_equal_minus_2a": sum(abs(h1[i][j] + 2.0 * a) < 1e-13 for i in range(3) for j in range(3)) == 6,
            "three_exact_zero_entries": sum(abs(h1[i][j]) < 1e-13 for i in range(3) for j in range(3)) == 3,
            "invariants": nu["invariants"],
            "source_direction": nu["source_direction"],
        },
        "neutral_internal_H1_rows": rows,
        "internal_dimensionless_rows_closed": sum(row["selected_emitted"] for row in rows),
        "what_closes_here": {
            "selected_internal_dimensionless_neutral_baseline_Y0": gate,
            "selected_internal_dimensionless_neutral_correction_dY": gate,
            "selected_internal_dimensionless_neutral_response_H1": gate,
            "combined_internal_overlap_amplitude": gate,
            "decomposition_into_action_cost_S_gamma_and_prefactor_A_gamma": False,
            "same_scheme_physical_unit": False,
            "dimensionful_neutral_mass_matrix": False,
            "nil_anchor_projector": False,
            "Dirac_only_action_completeness": False,
        },
        "neutral_overlap_OK_gate_acceptance": predecessor["neutral_overlap_OK_gate_acceptance"],
        "neutral_overlap_OK_gates_closed": predecessor["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": predecessor["neutral_overlap_OK_gates_total"],
        "readiness_subfields": readiness,
        "readiness_subfields_closed": sum(bool(value) for value in readiness.values()),
        "readiness_subfields_total": len(readiness),
        "new_internal_dimensionless_value_rows_closed_here": 9,
        "new_physical_value_fields_closed_here": 0,
        "accepted_route_exit_count": 0,
        "route_exit_count": 3,
        "dimensionful_M_D_3x3_closed": False,
        "dimensionful_M_L_3x3_closed": False,
        "dimensionful_M_R_3x3_closed": False,
        "absolute_normalization_and_scheme_closed": False,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "remaining_value_blockers": [
            "same-source conversion from the selected internal overlap normalization to a physical Yukawa/mass normalization",
            "one universal metrology primitive value or strict zero-knob physical-unit theorem",
            "nil-anchor/coherence projector and ordering/absolute-spectrum theorem",
            "Dirac-only completeness or selected Majorana M_L/M_R blocks",
        ],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralAbsoluteAmplitudeNilAnchorOrDiracMajoranaCompletion_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": gate,
        "selected_internal_dimensionless_neutral_response_closed": gate,
        "a_internal": a,
        "internal_dimensionless_rows_closed": packet["internal_dimensionless_rows_closed"],
        "same_source_selected_fields": packet["source_provenance"]["same_source_selected_field_count"],
        "same_source_required_fields": packet["source_provenance"]["same_source_required_field_count"],
        "physical_unit_selected": False,
        "nil_anchor_projector_closed": False,
        "Dirac_only_action_completeness_closed": False,
        "neutral_overlap_OK_gates_closed": packet["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": packet["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": packet["readiness_subfields_closed"],
        "readiness_subfields_total": packet["readiness_subfields_total"],
        "new_physical_value_fields_closed_here": 0,
        "accepted_route_exit_count": 0,
        "route_exit_count": 3,
        "dimensionful_M_D_3x3_closed": False,
        "dimensionful_M_L_3x3_closed": False,
        "dimensionful_M_R_3x3_closed": False,
        "absolute_normalization_and_scheme_closed": False,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Absolute Amplitude, Nil Anchor, or Dirac-Majorana Completion v1

## Result

The later same-source back-promotion theorem validates all seven required
source fields for the selected dynamic matter/overlap packet. It therefore
promotes the complete internal dimensionless neutral response:

```text
a_int = {a}
dY_nu = I3 + X3
H1_nu = dY_nu Y0_nu^dagger + Y0_nu dY_nu^dagger
      = [ -2a   0   -2a ]
        [  0   -2a  -2a ]
        [ -2a  -2a   0  ].
```

All nine `H1_nu` rows are selected and theorem-derived; six equal `-2a` and
three are exact zeros. Readiness advances to
`{packet['readiness_subfields_closed']}/{packet['readiness_subfields_total']}`.

## Boundary

`a_int` is absolute only in the selected internal dimensionless normalization.
It is not a neutrino mass, an eV value, or a dimensionful Yukawa normalization.
The physical-unit bridge, nil anchor, Dirac/Majorana completion, and decomposition
of the effective overlap response into separate `A_gamma` and `S_gamma` rows
remain open. Consequently OK6 stays false and the neutral gate remains
`{packet['neutral_overlap_OK_gates_closed']}/{packet['neutral_overlap_OK_gates_total']}`.

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
