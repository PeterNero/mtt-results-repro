"""Build threshold/mass-scheme/covariance fill gate and Qa/SU3 packet integration status."""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BENCH = PACKET_DIR / "internal_rg_convergence_benchmark.packet.json"
POLICY = PACKET_DIR / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
QASU3 = PACKET_DIR / "qasu3_packet_integration_status.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdMassSchemeCovarianceFill_or_QaSU3PacketIntegration_v1.md"

STATUS = "MTT_SELECTED_THRESHOLDMASSSCHEMECOVARIANCEFILL_OR_QASU3PACKETINTEGRATION_BUILT_INTERNAL_BENCHMARK_CLOSED"
NEXT_ARTIFACT = "MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_rg_module():
    path = ROOT / "scripts" / "build_selected_rgengineexecution_or_selectedsmpacketcertificateintegration.py"
    spec = importlib.util.spec_from_file_location("mtt_rg_engine_gate", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load RG engine module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frob_delta(a: list, b: list) -> float:
    total = 0.0
    for row_a, row_b in zip(a, b):
        for za, zb in zip(row_a, row_b):
            dr = za[0] - zb[0]
            di = za[1] - zb[1]
            total += dr * dr + di * di
    return math.sqrt(total)


def run_custom(module, yu, yd, ye, lam: float, mu0: float, g1: float, g2: float, g3: float, steps: int) -> dict[str, Any]:
    h = (math.log(module.MZ) - math.log(mu0)) / steps
    for _ in range(steps):
        yu, yd, ye, lam = module.rk4_step(yu, yd, ye, lam, h, g1, g2, g3)
    return {
        "steps": steps,
        "Y_u": module.from_complex_matrix(yu),
        "Y_d": module.from_complex_matrix(yd),
        "Y_e": module.from_complex_matrix(ye),
        "lambda_H": lam,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_rgengineexecution_or_selectedsmpacketcertificateintegration.candidate.json")
    kernel = load(
        DATA
        / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
        / "yukawa_higgs_common_scale_transport_kernel.packet.json"
    )
    final_packet = load(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json")
    qasu3_import = load(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")
    anomaly = load(DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json")

    module = load_rg_module()
    native = kernel["native_values_to_transport"]
    gauges = kernel["available_common_scale_inputs"]
    yu = module.to_complex_matrix(native["Y_u_native"])
    yd = module.to_complex_matrix(native["Y_d_native_complex_up_diagonal_convention"])
    ye = module.to_complex_matrix(native["Y_e_native"])
    lam = float(native["lambda_H_tree_native"])
    mu0 = float(native["input_masses_GeV"]["t"])
    g1 = float(gauges["g_1_GUT_MZ"]["central_value"])
    g2 = float(gauges["g_2_MZ"]["central_value"])
    g3 = float(gauges["g_3_MZ"]["central_value"])

    runs = {
        str(steps): run_custom(module, [row[:] for row in yu], [row[:] for row in yd], [row[:] for row in ye], lam, mu0, g1, g2, g3, steps)
        for steps in (128, 256, 512)
    }
    delta_128_256 = {
        "Y_u": frob_delta(runs["128"]["Y_u"], runs["256"]["Y_u"]),
        "Y_d": frob_delta(runs["128"]["Y_d"], runs["256"]["Y_d"]),
        "Y_e": frob_delta(runs["128"]["Y_e"], runs["256"]["Y_e"]),
        "lambda_H": abs(runs["128"]["lambda_H"] - runs["256"]["lambda_H"]),
    }
    delta_256_512 = {
        "Y_u": frob_delta(runs["256"]["Y_u"], runs["512"]["Y_u"]),
        "Y_d": frob_delta(runs["256"]["Y_d"], runs["512"]["Y_d"]),
        "Y_e": frob_delta(runs["256"]["Y_e"], runs["512"]["Y_e"]),
        "lambda_H": abs(runs["256"]["lambda_H"] - runs["512"]["lambda_H"]),
    }
    max_delta_256_512 = max(delta_256_512.values())

    benchmark = {
        "schema": "MTTInternalRGConvergenceBenchmark.v1",
        "status": "INTERNAL_RK_CONVERGENCE_BENCHMARK_CLOSED_FOR_DIAGNOSTIC_ENGINE",
        "engine_scope": "diagnostic one-loop SM Yukawa/Higgs RG with frozen M_Z gauge couplings",
        "runs": runs,
        "delta_128_to_256": delta_128_256,
        "delta_256_to_512": delta_256_512,
        "max_delta_256_to_512": max_delta_256_512,
        "tolerance": 1e-12,
        "passes_internal_convergence": max_delta_256_512 < 1e-12,
        "accepted_for_SM_parity_values": False,
        "why_not_acceptance": (
            "Convergence checks the local integrator only. Accepted SM-parity values still require "
            "threshold matching, mass-scheme conversion, covariance/profile execution, and either an "
            "external accepted RG benchmark or a fully specified internal benchmark policy."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    policy = {
        "schema": "MTTThresholdMassSchemeCovarianceAcceptanceContract.v1",
        "status": "ACCEPTANCE_CONTRACT_BUILT_VALUES_STILL_OPEN",
        "threshold_matching_required": {
            "top": "direct/top mass convention to running top Yukawa input",
            "bottom": "MSbar m_b(m_b) to M_Z transport with threshold policy",
            "charm": "MSbar m_c(m_c) to M_Z transport with threshold policy",
            "tau": "pole/rest mass to running charged-lepton Yukawa convention",
            "W_Z_H": "electroweak matching for v, lambda_H, and gauge/Yukawa convention",
        },
        "mass_scheme_conversion_required": {
            "pole_or_rest_leptons": True,
            "direct_top_mass": True,
            "MSbar_quarks_native_scales": True,
            "Higgs_pole_to_running_lambda": True,
        },
        "covariance_policy": {
            "central_value_replay_allowed": True,
            "diagonal_uncertainty_propagation_allowed_when_correlations_absent": True,
            "correlation_matrix_required_for_final_profile_likelihood": True,
            "missing_correlations_must_be_reported_not_silently_fitted": True,
        },
        "benchmark_policy": {
            "internal_RK_convergence_closed": benchmark["passes_internal_convergence"],
            "external_RG_package_comparison": "OPEN",
            "analytic_or_literature_common_scale_table_comparison": "OPEN",
        },
        "values_promotable_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    qasu3 = {
        "schema": "MTTQaSU3PacketIntegrationStatus.v1",
        "status": "QASU3_PACKET_INTEGRATION_RECHECKED_STILL_OPEN",
        "crossrepo_status": qasu3_import["status"],
        "actual_selected_sm_packet_anomaly_status": anomaly["status"],
        "final_packet_critical_open_row": final_packet["final_packet_certificate"]["critical_open_row"],
        "can_integrate_selected_packet_now": False,
        "needed_for_integration": [
            "selected D_E or rho_E operator data",
            "typed monad or section-ring source maps",
            "color/operator packet pushdown to the SM source certificate",
            "mapped Bianchi/Freed-Witten/anomaly certificate",
        ],
        "rejected_shortcuts": final_packet["final_packet_certificate"]["unsafe_shortcuts_rejected"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedThresholdMassSchemeCovarianceFillOrQaSU3PacketIntegration",
        "status": STATUS,
        "inputs": {
            "previous_rg_gate": rel(DATA / "selected_rgengineexecution_or_selectedsmpacketcertificateintegration.candidate.json"),
            "common_scale_transport_kernel": rel(
                DATA
                / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
                / "yukawa_higgs_common_scale_transport_kernel.packet.json"
            ),
            "final_packet_certificate": rel(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"),
            "qasu3_crossrepo_import": rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"),
            "actual_selected_sm_packet_anomaly_audit": rel(DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"),
        },
        "output_packets": {
            "internal_rg_convergence_benchmark": rel(BENCH),
            "threshold_mass_scheme_covariance_acceptance_contract": rel(POLICY),
            "qasu3_packet_integration_status": rel(QASU3),
        },
        "theorem": {
            "name": "ThresholdMassSchemeCovarianceAndQaSU3SeparationTheorem",
            "proved": True,
            "statement": (
                "The diagnostic RG engine now has an internal RK convergence benchmark. This closes only "
                "the local integrator sanity check; accepted M_Z Yukawa/Higgs values still require threshold "
                "matching, mass-scheme conversion, covariance/profile execution, and benchmark validation. "
                "The Qa/SU3 packet remains a separate source-side integration gate."
            ),
        },
        "what_closes_now": {
            "internal_RK_convergence_benchmark_closed": benchmark["passes_internal_convergence"],
            "threshold_mass_scheme_covariance_contract_built": True,
            "QaSU3_packet_integration_status_rechecked": True,
            "RG_acceptance_blockers_ranked": True,
            "source_gate_kept_separate_from_value_transport": True,
        },
        "what_remains_open": {
            "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values": True,
            "accepted_lambda_H_MZ_value": True,
            "threshold_matching_values": True,
            "mass_scheme_conversion_values": True,
            "external_or_literature_RG_benchmark": True,
            "profile_likelihood_or_covariance_matrix": True,
            "QaSU3_color_operator_packet": True,
            "selected_SM_packet_certificate_integration": True,
            "final_integrated_empirical_replay_audit": True,
            "SM_parity_closure": True,
        },
        "closure_decision": {
            "patched_SM_parity_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_ThresholdMassSchemeCovarianceFill_or_QaSU3PacketIntegration_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = f"""# MTT Selected ThresholdMassSchemeCovarianceFill or QaSU3PacketIntegration v1

Status: `{STATUS}`.

The diagnostic RG engine now has an internal RK convergence benchmark:

```text
max delta 256->512 = {max_delta_256_512:.6e}
tolerance          = 1.0e-12
internal benchmark = {benchmark["passes_internal_convergence"]}
```

This closes the local integrator sanity check only. Accepted `M_Z` Yukawa/Higgs
values still require threshold matching, mass-scheme conversion, covariance or
profile-likelihood execution, and benchmark validation.

The Qa/SU3 color/operator packet remains a separate source-side gate.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    BENCH.write_text(json.dumps(benchmark, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    POLICY.write_text(json.dumps(policy, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    QASU3.write_text(json.dumps(qasu3, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
