"""Construct the C1 positive density and prove its Q/L-symmetric gauge no-go."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_positivesectordensitysourcetheorem_or_commongaugeflavorweightemission"
OUT = ROOT / "candidate_data" / SLUG
DENSITY_PACKET = OUT / "conditional_c1_positive_sector_density.packet.json"
NOGO_PACKET = OUT / "quark_lepton_doublet_symmetry_gauge_nogo.packet.json"
CONTRACT_PACKET = OUT / "next_ql_resolved_density_source_contract.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PositiveSectorDensitySourceTheorem_or_CommonGaugeFlavorWeightEmission_v1.md"
STATUS = "MTT_SELECTED_CONDITIONAL_C1_POSITIVE_DENSITY_CONSTRUCTED_QL_SYMMETRIC_GAUGE_NOGO_PROVED_QL_RESOLVED_SOURCE_OPEN"
NEXT = "MTT_Selected_QuarkLeptonDoubletResolvedPositiveDensitySource_or_KineticWeightEmission_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encode_matrix(matrix: np.ndarray) -> list[list[list[float]]]:
    return [
        [[float(value.real), float(value.imag)] for value in row]
        for row in matrix
    ]


def main() -> int:
    paths = {
        "A52_profile": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A66_superset": ROOT / "candidate_data" / "selected_finitekineticweightoperatorsource_or_circlelensnilzeromodegramexecution" / "common_positive_sector_density_superset_contract.packet.json",
        "conditional_payload": ROOT / "candidate_data" / "selected_step20_conditionalatompayload_or_sourcetheorem" / "step20_conditional_phase_shift_payload.packet.json",
        "conditional_validation": ROOT / "candidate_data" / "selected_step20_conditionalatompayload_or_sourcetheorem" / "step20_conditional_normal_form_validation.packet.json",
        "patched_closure": ROOT / "candidate_data" / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "patched_dynamic_c1_closure_theorem.packet.json",
        "strict_phi_gate": ROOT / "candidate_data" / "selected_phisectornsourcevalues_or_noknobcskrows.candidate.json",
        "A46_carrier": ROOT / "candidate_data" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem" / "typed_family_gauge_carrier_and_anomaly_table.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    omega = np.exp(2j * math.pi / 3.0)
    Z = np.diag([1.0 + 0j, omega, omega**2])
    X = np.asarray([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    I = np.eye(3, dtype=complex)
    M_phase = I + Z
    M_shift = I + X
    Phi_phase = M_phase @ M_phase.conj().T
    Phi_shift = M_shift @ M_shift.conj().T
    Phi_left = Phi_phase + Phi_shift

    eig_phase = np.sort(np.linalg.eigvalsh(Phi_phase))[::-1]
    eig_shift = np.sort(np.linalg.eigvalsh(Phi_shift))[::-1]
    eig_left = np.sort(np.linalg.eigvalsh(Phi_left))[::-1]
    trace_phase = float(np.trace(Phi_phase).real)
    trace_shift = float(np.trace(Phi_shift).real)
    trace_left = float(np.trace(Phi_left).real)

    sector_blocks = {
        "Q": Phi_left,
        "u": Phi_phase,
        "d": Phi_shift,
        "L": Phi_left,
        "e": Phi_phase,
        "N": Phi_shift,
    }
    sector_traces = np.asarray([float(np.trace(sector_blocks[sector]).real) for sector in SECTORS])
    trace_map = np.asarray(
        [
            [3 / 10, 12 / 5, 3 / 5, 9 / 10, 9 / 5, 0],
            [9 / 2, 0, 0, 3 / 2, 0, 0],
            [3, 3 / 2, 3 / 2, 0, 0, 0],
        ],
        dtype=float,
    )
    gauge_rows = trace_map @ sector_traces
    gauge_normalized = gauge_rows / gauge_rows[1]
    profile = np.asarray(data["A52_profile"]["minimal_profile_normalization"]["K_gauge_diagonal"], dtype=float)
    profile_log_residual = float(np.linalg.norm(np.log(gauge_normalized) - np.log(profile)))

    # For any positive Q/L-symmetric two-class density, write a for Q,L and b
    # for u,d,e,N. The exact representation-index map then gives these ratios.
    # K3/K2 = (3a+3b)/(6a) = 1/2 + b/(2a) > 1/2.
    profile_k3_over_k2 = float(profile[2])
    required_l_over_q_plus_colored_at_half = "l > q + 2(u+d)"
    required_l_for_profile_if_q_u_d_fixed = (
        (3.0 - 4.5 * profile_k3_over_k2) * trace_left
        + 1.5 * (trace_phase + trace_shift)
    ) / (1.5 * profile_k3_over_k2)

    validation = data["conditional_validation"]
    patched = data["patched_closure"]
    strict_phi = data["strict_phi_gate"]
    checks = {
        "A66_common_density_interface_imported": data["A66_superset"]["status"] == "ONE_COMMON_GAUGE_FLAVOR_DENSITY_OPERATOR_IDENTIFIED_VALUES_OPEN",
        "phase_matrix_matches_I_plus_Z": abs(trace_phase - 6.0) < 1e-13,
        "shift_matrix_matches_I_plus_X": abs(trace_shift - 6.0) < 1e-13,
        "right_density_spectra_are_4_1_1": bool(np.allclose(eig_phase, [4, 1, 1], atol=1e-12, rtol=0.0)) and bool(np.allclose(eig_shift, [4, 1, 1], atol=1e-12, rtol=0.0)),
        "left_blocks_Q_L_are_equal": bool(np.allclose(sector_blocks["Q"], sector_blocks["L"], atol=1e-13, rtol=0.0)),
        "all_right_block_traces_are_six": all(abs(sector_traces[index] - 6.0) < 1e-13 for index in [1, 2, 4, 5]),
        "left_block_traces_are_twelve": abs(sector_traces[0] - 12.0) < 1e-13 and abs(sector_traces[3] - 12.0) < 1e-13,
        "conditional_Gram_is_12I2": validation["checks"]["gram_is_12I2"],
        "patched_source_is_axiom_conditional": patched["scientific_status"] == "axiom-conditional closure",
        "strict_Phi_sector_values_remain_zero": strict_phi["closure_decision"]["accepted_Phi_sector_N_source_value_count"] == 0,
        "conditional_density_K3_over_K2_above_half": gauge_normalized[2] > 0.5,
        "accepted_profile_K3_over_K2_below_half": profile_k3_over_k2 < 0.5,
        "conditional_density_not_exact_profile": profile_log_residual > 1e-10,
    }

    density = {
        "schema": "MTTConditionalC1PositiveSectorDensity.v1",
        "status": "EXACT_PSD_DENSITY_CONSTRUCTED_AT_AXIOM_CONDITIONAL_C1_TIER",
        "source_status": {
            "dynamic_C1_packet": patched["status"],
            "scientific_status": patched["scientific_status"],
            "strict_unpatched_no_knob_source": False,
            "observed_data_used_as_selector": False,
        },
        "generators": {
            "Z": encode_matrix(Z),
            "X": encode_matrix(X),
            "M_phase": "I+Z on u,e",
            "M_shift": "I+X on d,N",
        },
        "positive_blocks": {
            "Phi_phase": encode_matrix(Phi_phase),
            "Phi_shift": encode_matrix(Phi_shift),
            "Phi_left_incidence_pullback": encode_matrix(Phi_left),
            "right_block_eigenvalues_phase": eig_phase.tolist(),
            "right_block_eigenvalues_shift": eig_shift.tolist(),
            "left_block_eigenvalues": eig_left.tolist(),
        },
        "sector_order": SECTORS,
        "sector_trace_weights": sector_traces.tolist(),
        "sector_block_rule": {
            "Q": "Phi_phase+Phi_shift from Q-u and Q-d incidences",
            "u": "Phi_phase",
            "d": "Phi_shift",
            "L": "Phi_phase+Phi_shift from L-e and L-N incidences",
            "e": "Phi_phase",
            "N": "Phi_shift",
        },
        "positivity": {
            "all_blocks_positive_semidefinite": all(np.min(np.linalg.eigvalsh(block)) > -1e-12 for block in sector_blocks.values()),
            "construction": "each right block is M M^*, each left block is the sum of incident M M^* blocks",
        },
        "theorem": {
            "proved_conditionally": True,
            "statement": "Under the accepted differentiated-C1 source axiom, the exact phase/shift matrices define a positive sector density. Its right blocks have spectrum [4,1,1] and trace 6; incidence pullback gives identical Q and L blocks with trace 12.",
        },
    }

    nogo = {
        "schema": "MTTQuarkLeptonDoubletSymmetryGaugeNoGo.v1",
        "status": "QL_SYMMETRIC_POSITIVE_DENSITY_CANNOT_MATCH_K3_OVER_K2_BELOW_HALF",
        "conditional_C1_execution": {
            "sector_trace_weights_Q_u_d_L_e_N": sector_traces.tolist(),
            "gauge_rows_U1_SU2_SU3": gauge_rows.tolist(),
            "K_over_K2": gauge_normalized.tolist(),
            "profile_K_over_K2_downstream_only": profile.tolist(),
            "profile_log_residual": profile_log_residual,
            "accepted": False,
        },
        "general_two_class_theorem": {
            "premises": ["w_Q=w_L=a>0", "w_u=w_d=w_e=w_N=b>0"],
            "K1_over_K2": "1/5 + (4/5)(b/a)",
            "K3_over_K2": "1/2 + (1/2)(b/a)",
            "consequence": "K3/K2 > 1/2 for every positive a,b",
            "profile_fact": profile_k3_over_k2,
            "proved": True,
        },
        "minimum_required_symmetry_breaking": {
            "inequality_to_cross_below_half": required_l_over_q_plus_colored_at_half,
            "derivation": "3q+(3/2)(u+d) < (1/2)[(9/2)q+(3/2)l] iff l>q+2(u+d)",
            "meaning": "The positive kinetic density must weight the lepton doublet L more strongly than the quark doublet Q plus the colored singlet contribution. A Q=L source can never work.",
            "required_l_trace_for_exact_profile_if_C1_q_u_d_retained": required_l_for_profile_if_q_u_d_fixed,
            "current_C1_l_trace": trace_left,
            "profile_used_only_for_last_numeric_diagnostic": True,
        },
        "relation_to_quark_second_order_hypothesis": "The theorem gives a precise place where an additional quark-versus-lepton order can enter: it must alter the Q/L positive density or suppress colored right-sector weight before the gauge trace, not merely split generations.",
    }

    contract = {
        "schema": "MTTNextQLResolvedDensitySourceContract.v1",
        "status": "QL_RESOLVED_POSITIVE_SOURCE_REQUIRED",
        "required_operator": "Phi_sector^+ with independently selected Q and L blocks and positive u,d,e,N blocks",
        "required_fields": [
            "same-branch source owner stronger than the parity-only residual-projector axiom, or explicit declaration that the axiom is fundamental",
            "positive Q,u,d,L,e,N family blocks",
            "proof of gauge commutation and common-circle compatibility",
            "source-derived Q-versus-L asymmetry",
            "same-action N_kin map into W_kin",
            "gauge K rows and flavor traces emitted without refitting",
            "exactness/error certificate",
        ],
        "guardrails": [
            "do not choose Q/L weights from the gauge residual",
            "do not use generation splitting as a substitute for Q/L sector splitting",
            "do not call the axiom-conditional C1 density strict no-knob data",
            "do not alter the A62 spectrum contract",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "schema": "MTTSelectedPositiveSectorDensitySourceTheoremOrCommonGaugeFlavorWeightEmission.v1",
        "status": STATUS,
        "theorems": {
            "conditional_positive_density": density["theorem"],
            "QL_symmetric_density_no_go": nogo["general_two_class_theorem"],
            "minimum_QL_breaking": {
                "proved": True,
                "statement": "For a positive six-sector kinetic weight to produce K3/K2 below one half, it is necessary that l>q+2(u+d). Therefore the source must distinguish Q from L; family splitting and the symmetric C1 incidence density are insufficient.",
            },
        },
        "closure_decision": {
            "conditional_C1_positive_density_constructed": True,
            "conditional_density_positive": True,
            "conditional_density_source_tier": "axiom-conditional parity",
            "conditional_density_promoted_as_strict_no_knob": False,
            "QL_symmetric_positive_density_class_retired": True,
            "Q_vs_L_source_asymmetry_required": True,
            "nonuniversal_gauge_rows_accepted": 0,
            "strict_flavor_rows_accepted_from_this_density": 0,
            "no_knob_gauge_coupling_prediction_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "density": str(DENSITY_PACKET.relative_to(ROOT)).replace("\\", "/"),
            "nogo": str(NOGO_PACKET.relative_to(ROOT)).replace("\\", "/"),
            "contract": str(CONTRACT_PACKET.relative_to(ROOT)).replace("\\", "/"),
        },
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "checks": {key: bool(value) for key, value in checks.items()},
        "epistemic_policy": {
            "target_fitting_used": False,
            "profile_used_only_as_downstream_rejection": True,
            "conditional_axiom_tier_disclosed": True,
            "strict_source_claimed": False,
            "prediction_claimed": False,
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_PositiveSectorDensitySourceTheorem_or_CommonGaugeFlavorWeightEmission_v1",
        "status": STATUS,
        "conditional_C1_positive_density_constructed": True,
        "right_block_spectrum": [4.0, 1.0, 1.0],
        "sector_trace_weights_Q_u_d_L_e_N": sector_traces.tolist(),
        "conditional_K_over_K2": gauge_normalized.tolist(),
        "QL_symmetric_positive_density_no_go_proved": True,
        "Q_vs_L_source_asymmetry_required": True,
        "strict_density_source_closed": False,
        "nonuniversal_gauge_rows_accepted": 0,
        "new_continuous_parameters": 0,
        "no_knob_gauge_coupling_prediction_closed": False,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Positive Sector Density Source Theorem or Common Gauge/Flavor Weight Emission v1

## Conditional density constructed

The accepted parity-tier differentiated-C1 axiom supplies

```text
M_phase = I+Z on u,e,
M_shift = I+X on d,N.
```

Their positive blocks `M M^*` both have exact spectrum `[4,1,1]` and trace `6`.
Pulling the density back through the fixed Yukawa incidence graph gives

```text
Phi_Q = Phi_phase + Phi_shift,
Phi_L = Phi_phase + Phi_shift,
Tr(Phi_Q,Phi_u,Phi_d,Phi_L,Phi_e,Phi_N) = {sector_traces.tolist()}.
```

This is an exact positive operator at the axiom-conditional parity tier. It is not promoted as an
unpatched strict no-knob source.

## Exact gauge test

Inserted into the A46 kinetic trace, the density gives

```text
K/K2 = {gauge_normalized.tolist()}.
```

More generally, every positive two-class density with `w_Q=w_L=a` and
`w_u=w_d=w_e=w_N=b` obeys

```text
K1/K2 = 1/5 + (4/5)(b/a),
K3/K2 = 1/2 + (1/2)(b/a) > 1/2.
```

The accepted downstream profile has `K3/K2={profile_k3_over_k2:.15g}<1/2`, so the entire positive
Q/L-symmetric class is ruled out, independently of generation details.

## New sharp requirement

For a general positive sector weight, crossing below one half requires

```text
l > q + 2(u+d).
```

Thus the next source must distinguish the quark doublet `Q` from the lepton doublet `L`. This gives
a precise mathematical location for the proposed extra order of quark breakdown: it must alter the
Q/L kinetic density or colored-sector suppression, not merely produce another family split.

No parameter was added and no gauge value selected the source.

Next artifact: `{NEXT}`.
"""

    dump(DENSITY_PACKET, density)
    dump(NOGO_PACKET, nogo)
    dump(CONTRACT_PACKET, contract)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
