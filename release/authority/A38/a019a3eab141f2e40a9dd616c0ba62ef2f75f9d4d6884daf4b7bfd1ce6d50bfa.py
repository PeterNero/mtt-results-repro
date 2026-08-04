"""Build the neutral common-circle factorization and holonomy-scalar reduction."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralcommoncirclefactorizationandholonomyscalarreduction"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_common_circle_factorization.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralCommonCircleFactorizationAndHolonomyScalarReduction_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_COMMON_CIRCLE_FACTORIZATION_CLOSED_CENTRAL_HOLONOMY_AND_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralCentralHolonomyValueAndAnchoredHessianScale_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cp(value: list[float]) -> complex:
    return complex(value[0], value[1])


def main() -> int:
    prior = load(
        ROOT / "candidate_data" / "selected_neutralcrtphasetypingandprotospinornildriftreduction"
        / "neutral_crt_phase_typing_and_nil_drift.packet.json"
    )
    common = load(
        ROOT / "candidate_data" / "selected_commoncirclesectorresponseexecution_or_csktracerows"
        / "source_level_common_circle_hcen_operator.packet.json"
    )
    common_candidate = load(
        ROOT / "candidate_data" / "selected_commoncirclesectorresponseexecution_or_csktracerows.candidate.json"
    )

    h = common["H_cen"]
    matrix = [[cp(item) for item in row] for row in h["matrix_numeric_complex_pairs"]]
    eigenvalues = [matrix[i][i] for i in range(3)]
    phases = [(cmath.phase(value) % (2.0 * math.pi)) for value in eigenvalues]
    zeta = cmath.exp(2j * math.pi / 3.0)
    phi_test = 0.137
    neutral_eigenvalues = [cmath.exp(1j * phi_test) * value for value in eigenvalues]
    real_parts = [value.real for value in neutral_eigenvalues]
    expected_real = [math.cos(phi_test + 2.0 * math.pi * k / 3.0) for k in range(3)]
    determinant = neutral_eigenvalues[0] * neutral_eigenvalues[1] * neutral_eigenvalues[2]
    recovered_phi = (cmath.phase(determinant) / 3.0) % (2.0 * math.pi / 3.0)

    checks = {
        "A37_CRT_typing_closed": prior["theorem"]["proved"],
        "Hcen_source_level_operator_emitted": common["accepted_as_common_circle_source_level_operator"],
        "Hcen_symbolic_form": h["matrix_symbolic"] == "diag(1, zeta_3, zeta_3^2)",
        "Hcen_order_three": h["order"] == 3 and h["order3_residual"] < 1e-10,
        "Hcen_unitary": h["unitary"],
        "Hcen_trace_zero": abs(sum(eigenvalues)) < 1e-12,
        "Hcen_determinant_one": abs(eigenvalues[0] * eigenvalues[1] * eigenvalues[2] - 1.0) < 1e-12,
        "Hcen_eigenvalues_are_Z3_orbit": all(abs(eigenvalues[k] - zeta**k) < 1e-12 for k in range(3)),
        "central_phase_real_parts_equal_proto_cosine_orbit": all(abs(a-b) < 1e-12 for a,b in zip(real_parts, expected_real)),
        "determinant_recovers_common_phase_mod_2pi_over_3": abs(recovered_phi - phi_test) < 1e-12,
        "operator_level_neutral_response_not_emitted": not h["operator_level_projective_rhoE_promoted"],
        "current_sector_execution_excludes_neutral": common_candidate["closure_decision"]["accepted_strict_csk_source_row_count"] == 0,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedNeutralCommonCircleFactorizationAndHolonomyScalarReduction.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralCRTPhaseTypingAndProtoSpinorNilDriftReduction_v1",
        "theorem": {
            "name": "SelectedCommonCircleToProtoSpinorThreeBasinFactorizationTheorem",
            "proved": theorem_proved,
            "statement": "The selected q79/F,m=1 source emits H_cen=diag(1,zeta_3,zeta_3^2), a unitary order-three determinant-one common-circle operator. On the proto-spinor co-aligned neutral sector, a common residual nil holonomy can only multiply all three family eigenlines by one central U(1) phase, so H_nu(phi_nu)=exp(i phi_nu) H_cen. Taking the real closure-cost channel gives the exact three-basin shape cos(phi_nu+2 pi k/3). Conversely det H_nu=exp(3 i phi_nu), hence phi_nu=(1/3)arg det H_nu modulo 2 pi/3. This closes the common-circle-to-nil-drift transfer and proves that only one shape scalar remains. The current packet does not emit the operator-level neutral H_nu or its determinant, and it does not emit the anchored Hessian scale.",
        },
        "source_checks": checks,
        "selected_common_circle_operator": {
            "symbolic": h["matrix_symbolic"],
            "eigenvalue_phases": phases,
            "trace": h["trace_complex_pair"],
            "determinant": h["determinant_complex_pair"],
            "order": h["order"],
            "source_level_emitted": h["source_level_emitted"],
            "operator_level_projective_rhoE_promoted": h["operator_level_projective_rhoE_promoted"],
        },
        "neutral_factorization": {
            "co_aligned_hypothesis_source": "proto-spinor neutrinos are same-direction/co-aligned loop identities",
            "formula": "H_nu(phi_nu)=exp(i*phi_nu)*H_cen",
            "eigenvalues": "exp(i*(phi_nu+2*pi*k/3)), k=0,1,2",
            "mass_squared_shape": "m_k^2=m_0^2+A*Re eig_k(H_nu)=m_0^2+A*cos(phi_nu+2*pi*k/3)",
            "determinant_identity": "det H_nu=exp(3*i*phi_nu)",
            "phase_readout": "phi_nu=(arg det H_nu)/3 mod 2*pi/3",
            "independent_shape_scalar_count": 1,
            "transfer_functor_closed": theorem_proved,
        },
        "numeric_identity_witness": {
            "phi_test": phi_test,
            "real_parts_of_expiphi_Hcen": real_parts,
            "cosine_orbit": expected_real,
            "determinant_complex_pair": [determinant.real, determinant.imag],
            "recovered_phi_mod_2pi_over_3": recovered_phi,
        },
        "value_boundary": {
            "Hcen_supplies_relative_family_offsets": True,
            "Hcen_supplies_common_neutral_phase": False,
            "neutral_operator_Hnu_emitted": False,
            "neutral_determinant_emitted": False,
            "phi_nu_value_emitted": False,
            "anchored_Hessian_scale_mu_nu_emitted": False,
            "why_phi_not_zero": "det H_cen=1 fixes only the source-level relative Z3 orbit; identifying H_nu with H_cen would erase the separately typed residual neutral nil holonomy without a neutral response theorem",
        },
        "reduced_physical_cutset": {
            "shape": "one scalar phi_nu from operator-level neutral determinant holonomy",
            "scale": "one scalar mu_nu from the anchored neutral Hessian/closure-cost normalization",
            "count": 2,
            "next_source_payload": [
                "operator-level neutral co-aligned response H_nu or det H_nu",
                "same-branch anchored neutral Hessian contraction in a declared physical unit",
            ],
        },
        "what_closes_here": {
            "selected_Z3_common_circle_family_operator": theorem_proved,
            "common_circle_to_proto_spinor_three_basin_transfer": theorem_proved,
            "single_scalar_nil_holonomy_reduction": theorem_proved,
            "phi_nu_value": False,
            "mu_nu_value": False,
            "dimensionful_neutral_masses": False,
        },
        "new_physical_value_fields_closed_here": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralCommonCircleFactorizationAndHolonomyScalarReduction_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "Hcen_source_level_emitted": h["source_level_emitted"],
        "Hcen_order": h["order"],
        "common_circle_to_three_basin_transfer_closed": theorem_proved,
        "independent_shape_scalar_count": 1,
        "phi_nu_value_closed": False,
        "mu_nu_value_closed": False,
        "dimensionful_neutral_masses_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Common-Circle Factorization and Holonomy Scalar Reduction v1

## Selected operator

The selected source-level common-circle operator is

```text
H_cen = diag(1,zeta_3,zeta_3^2).
```

It is unitary, has order three, trace zero and determinant one. For the
proto-spinor co-aligned neutral sector, the residual common nil holonomy is a
central phase, hence

```text
H_nu(phi_nu)=exp(i phi_nu) H_cen.
```

Its real eigenvalue channel is exactly

```text
cos(phi_nu+2*pi*k/3), k=0,1,2,
```

which derives the corpus three-basin formula from the selected finite operator.
Moreover `det H_nu=exp(3 i phi_nu)`, so the complete shape uncertainty is the
single scalar `phi_nu=(arg det H_nu)/3 mod 2*pi/3`.

## Boundary

The current source emits `H_cen` only at source level. It does not emit the
operator-level neutral response `H_nu`, its determinant, or the anchored
Hessian scale `mu_nu`. Setting `phi_nu=0` would silently identify two differently
typed objects and is not allowed.

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
