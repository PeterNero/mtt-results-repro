"""Build the two-primitive neutral profile value closure."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraltwoprimitiveprofilevalueclosure"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_two_primitive_profile_values.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralTwoPrimitiveProfileValueClosure_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_TWO_PRIMITIVE_PROFILE_VALUES_CLOSED_STRICT_SOURCE_AND_COVARIANCE_OPEN"
NEXT = "MTT_Selected_NeutralSmoothDeterminantLineHolonomyAndAnchoredScale_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cp(value):
    return complex(value[0], value[1]) if isinstance(value, list) else complex(value)


def pair(value: complex) -> list[float]:
    return [float(value.real), float(value.imag)]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(3)] for i in range(3)]


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def diag(values):
    return [[complex(values[i]) if i == j else 0j for j in range(3)] for i in range(3)]


def max_residual(a, b):
    return max(abs(a[i][j]-b[i][j]) for i in range(3) for j in range(3))


def main() -> int:
    prior = load(
        ROOT / "candidate_data" / "selected_neutralfiniteheisenbergdeterminantnogoandsmoothlifttarget"
        / "neutral_finite_heisenberg_determinant_nogo.packet.json"
    )
    replay = load(ROOT / "candidate_data" / "sm_equivalence_mixing_and_gauge_replay.candidate.json")["PMNS_replay"]
    nil = load(
        ROOT / "candidate_data" / "selected_neutralnilboundarymassfunctional"
        / "neutral_nil_boundary_mass_functional.packet.json"
    )
    common = load(
        ROOT / "candidate_data" / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
        / "yukawa_higgs_common_scale_transport_kernel.packet.json"
    )

    dm21 = float(replay["normal_ordering_minimal_mass_squared_spectrum_eV2"][1])
    dm31 = float(replay["normal_ordering_minimal_mass_squared_spectrum_eV2"][2])
    ratio = dm21/dm31
    phi = math.atan(math.sqrt(3.0)*ratio/(2.0-ratio))
    cosines = [math.cos(phi+2.0*math.pi*k/3.0) for k in range(3)]
    k_min = min(range(3), key=lambda k: cosines[k])
    k_mid = sorted(range(3), key=lambda k: cosines[k])[1]
    k_max = max(range(3), key=lambda k: cosines[k])
    A = dm31/(cosines[k_max]-cosines[k_min])
    m0_sq = -A*cosines[k_min]
    mass_sq_by_k = [m0_sq+A*c for c in cosines]
    physical_k_order = [k_min, k_mid, k_max]
    mass_sq = [mass_sq_by_k[k] for k in physical_k_order]
    masses = [math.sqrt(max(0.0, value)) for value in mass_sq]

    Hnu_diag = [cmath.exp(1j*(phi+2.0*math.pi*k/3.0)) for k in range(3)]
    det_Hnu = Hnu_diag[0]*Hnu_diag[1]*Hnu_diag[2]
    phi_recovered = (cmath.phase(det_Hnu)/3.0) % (2.0*math.pi/3.0)

    U = [[cp(item) for item in row] for row in replay["input_PMNS_matrix"]]
    M_D_eV = matmul(U, diag(masses))
    H_flavor = matmul(M_D_eV, dagger(M_D_eV))
    H_replay = [[cp(item) for item in row] for row in replay["H_nu_mass_squared_flavor_basis_eV2"]]
    v_GeV = float(common["native_values_to_transport"]["higgs_tree"]["v_GeV"])
    yukawa_singular = [math.sqrt(2.0)*mass*1e-9/v_GeV for mass in masses]
    Y_nu = matmul(U, diag(yukawa_singular))
    YYdag = matmul(Y_nu, dagger(Y_nu))
    YYdag_expected = [[2.0e-18*H_flavor[i][j]/(v_GeV**2) for j in range(3)] for i in range(3)]
    m_beta = math.sqrt(sum(abs(U[0][i])**2*mass_sq[i] for i in range(3)))

    checks = {
        "A39_strict_frontier_typed": prior["theorem"]["proved"],
        "minimal_trace_boundary_theorem_proved": nil["theorem"]["proved"],
        "locked_PMNS_replay_available": replay["status"] == "OSCILLATION_MASS_SQUARED_REPLAY_READY_ABSOLUTE_MASS_OPEN",
        "analytic_phi_reproduces_ratio": abs(abs(math.sin(phi))/abs(math.sin(phi+math.pi/3.0))-ratio) < 1e-14,
        "mass_squared_spectrum_reproduced": max(abs(a-b) for a,b in zip(mass_sq,[0.0,dm21,dm31])) < 1e-17,
        "determinant_phase_recovers_phi": abs(phi_recovered-phi) < 1e-14,
        "flavor_mass_squared_reproduces_locked_replay": max_residual(H_flavor,H_replay) < 1e-17,
        "Dirac_Yukawa_Gram_identity": max_residual(YYdag,YYdag_expected) < 1e-40,
        "profile_VEV_positive": v_GeV > 0.0,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    complex_rows = lambda matrix, prefix, unit: [
        {"row_id": f"{prefix}.r{i}c{j}", "value": pair(matrix[i][j]), "unit": unit, "filled": theorem_proved}
        for i in range(3) for j in range(3)
    ]

    packet = {
        "schema": "MTTSelectedNeutralTwoPrimitiveProfileValueClosure.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralFiniteHeisenbergDeterminantNoGoAndSmoothLiftTarget_v1",
        "theorem": {
            "name": "NeutralTwoPrimitiveProfileValueExecutionTheorem",
            "proved": theorem_proved,
            "statement": "At the explicitly declared normal-ordering Dirac profile with nil-boundary m_lightest=0, the two locked oscillation coordinates Delta m21^2 and Delta m31^2 uniquely calibrate the proto-spinor nil holonomy phi_nu and amplitude A_nu. The analytic inversion phi_nu=atan(sqrt(3) r/(2-r)), r=Delta m21^2/Delta m31^2, and A_nu=Delta m31^2/(c_max-c_min) emits the complete mass-squared spectrum. With the locked PMNS replay and right-handed mass basis convention, all Dirac mass, Yukawa and flavor mass-squared matrix rows follow. This is a complete two-primitive measured-profile value closure, not a strict no-knob source theorem or an MTT selection of Dirac ontology, ordering, covariance, or the two primitive values.",
        },
        "source_checks": checks,
        "profile_policy": {
            "ordering": "normal",
            "ontology": "Dirac profile convention",
            "right_handed_basis": "mass eigenbasis U_R=I",
            "charged_lepton_basis": "Y_e diagonal",
            "nil_boundary": "m_lightest=0",
            "continuous_calibration_input_count": 2,
            "calibration_inputs": ["Delta_m21_sq", "Delta_m31_sq"],
            "discrete_policy_choices_not_counted_as_continuous_parameters": ["normal ordering", "Dirac route", "U_R=I convention"],
            "observed_data_used_as_geometry_or_branch_selector": False,
            "observed_data_used_as_profile_calibration": True,
        },
        "calibrated_shape_and_scale": {
            "Delta_m21_sq_eV2": dm21,
            "Delta_m31_sq_eV2": dm31,
            "ratio": ratio,
            "phi_nu_rad": phi,
            "phi_nu_deg": math.degrees(phi),
            "A_nu_eV2": A,
            "m0_sq_offset_eV2": m0_sq,
            "nil_basin_k_order_for_m1_m2_m3": physical_k_order,
            "cosine_orbit_by_k": cosines,
            "Hnu_diagonal_by_k": [pair(value) for value in Hnu_diag],
            "det_Hnu": pair(det_Hnu),
            "phi_recovered_from_determinant_rad": phi_recovered,
        },
        "physical_values": {
            "mass_squared_eV2": mass_sq,
            "masses_eV": masses,
            "sum_masses_eV": sum(masses),
            "m_beta_eV": m_beta,
            "profile_v_GeV": v_GeV,
            "Dirac_Yukawa_singular_values": yukawa_singular,
        },
        "filled_rows": {
            "mass_squared_rows": [{"row_id": f"m{i+1}_sq", "value": mass_sq[i], "unit": "eV^2", "filled": theorem_proved} for i in range(3)],
            "mass_rows": [{"row_id": f"m{i+1}", "value": masses[i], "unit": "eV", "filled": theorem_proved} for i in range(3)],
            "Yukawa_singular_rows": [{"row_id": f"y_nu_{i+1}", "value": yukawa_singular[i], "unit": "dimensionless", "filled": theorem_proved} for i in range(3)],
            "Dirac_mass_matrix_rows": complex_rows(M_D_eV,"M_D","eV"),
            "Dirac_Yukawa_matrix_rows": complex_rows(Y_nu,"Y_nu","dimensionless"),
            "flavor_mass_squared_rows": complex_rows(H_flavor,"H_nu_flavor","eV^2"),
        },
        "matrices": {
            "M_D_eV": [[pair(value) for value in row] for row in M_D_eV],
            "Y_nu": [[pair(value) for value in row] for row in Y_nu],
            "H_nu_flavor_eV2": [[pair(value) for value in row] for row in H_flavor],
        },
        "row_counts": {
            "mass_squared": 3,
            "masses": 3,
            "Yukawa_singular_values": 3,
            "Dirac_mass_matrix_complex": 9,
            "Dirac_Yukawa_matrix_complex": 9,
            "flavor_mass_squared_complex": 9,
            "total_rows_filled": 36 if theorem_proved else 0,
        },
        "closure_boundary": {
            "two_primitive_profile_numerical_closure": theorem_proved,
            "absolute_neutrino_masses_filled_at_profile_tier": theorem_proved,
            "Dirac_Yukawa_rows_filled_at_profile_tier": theorem_proved,
            "strict_MTT_source_for_phi_nu": False,
            "strict_MTT_source_for_A_nu_or_mu_nu": False,
            "Dirac_ontology_selected_by_MTT": False,
            "normal_ordering_selected_by_MTT": False,
            "Majorana_phases_or_0nu2beta": False,
            "uncertainty_covariance_propagated": False,
        },
        "observed_data_used_as_selector": False,
        "observed_data_used_as_profile_calibration": True,
        "target_fitting_used": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralTwoPrimitiveProfileValueClosure_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "continuous_profile_primitives": 2,
        "phi_nu_rad": phi,
        "A_nu_eV2": A,
        "masses_eV": masses,
        "sum_masses_eV": sum(masses),
        "Dirac_Yukawa_singular_values": yukawa_singular,
        "total_rows_filled": 36 if theorem_proved else 0,
        "absolute_neutrino_masses_filled_at_profile_tier": theorem_proved,
        "Dirac_Yukawa_rows_filled_at_profile_tier": theorem_proved,
        "strict_no_knob_source_closed": False,
        "uncertainty_covariance_closed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_as_profile_calibration": True,
        "target_fitting_used": True,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Two-Primitive Profile Value Closure v1

## Declared standard

This is a measured-profile closure, not a no-knob prediction. At normal ordering,
Dirac convention and `m_lightest=0`, the two oscillation inputs uniquely give

```text
phi_nu = {phi} rad = {math.degrees(phi)} deg
A_nu   = {A} eV^2
```

The resulting masses are `{masses}` eV, with sum `{sum(masses)}` eV. The
profile-standard Dirac Yukawa singular values are `{yukawa_singular}`.

All 36 scalar/complex rows for masses, singular values, `M_D`, `Y_nu`, and the
flavor-basis mass-squared matrix are emitted in the packet. They exactly replay
the locked PMNS mass-squared matrix.

## Boundary

The two measured splittings calibrate the two continuous profile primitives;
they do not select the MTT geometry or branch. Strict sources for `phi_nu` and
`A_nu/mu_nu`, ontology/order selection, Majorana observables, and covariance
propagation remain open.

Next strict artifact: `{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
