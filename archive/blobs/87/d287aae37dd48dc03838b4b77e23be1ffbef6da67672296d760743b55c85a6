"""Audit threshold/mass-scheme/covariance fill gate and Qa/SU3 packet integration status."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BENCH = PACKET_DIR / "internal_rg_convergence_benchmark.packet.json"
POLICY = PACKET_DIR / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
QASU3 = PACKET_DIR / "qasu3_packet_integration_status.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThresholdMassSchemeCovarianceFill_or_QaSU3PacketIntegration_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_THRESHOLDMASSSCHEMECOVARIANCEFILL_OR_QASU3PACKETINTEGRATION_BUILT_INTERNAL_BENCHMARK_CLOSED"
NEXT_ARTIFACT = "MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def finite_run(run: dict) -> bool:
    for key in ["Y_u", "Y_d", "Y_e"]:
        for row in run[key]:
            for pair in row:
                if not (math.isfinite(pair[0]) and math.isfinite(pair[1])):
                    return False
    return math.isfinite(run["lambda_H"])


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    bench = load(BENCH)
    policy = load(POLICY)
    qasu3 = load(QASU3)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")
    require(NEXT_ARTIFACT in note, "note missing next artifact")

    require(bench["status"] == "INTERNAL_RK_CONVERGENCE_BENCHMARK_CLOSED_FOR_DIAGNOSTIC_ENGINE", "benchmark status mismatch")
    require(set(bench["runs"].keys()) == {"128", "256", "512"}, "step runs missing")
    for run in bench["runs"].values():
        require(finite_run(run), "non-finite benchmark run")
    require(bench["max_delta_256_to_512"] < bench["tolerance"], "internal convergence did not pass")
    require(bench["passes_internal_convergence"] is True, "internal convergence flag missing")
    require(bench["accepted_for_SM_parity_values"] is False, "benchmark overpromoted to acceptance")

    require(policy["status"] == "ACCEPTANCE_CONTRACT_BUILT_VALUES_STILL_OPEN", "policy status mismatch")
    for key in ["top", "bottom", "charm", "tau", "W_Z_H"]:
        require(key in policy["threshold_matching_required"], f"threshold missing: {key}")
    require(policy["mass_scheme_conversion_required"]["direct_top_mass"] is True, "top conversion missing")
    require(policy["mass_scheme_conversion_required"]["Higgs_pole_to_running_lambda"] is True, "Higgs conversion missing")
    require(policy["covariance_policy"]["missing_correlations_must_be_reported_not_silently_fitted"] is True, "covariance guardrail missing")
    require(policy["benchmark_policy"]["internal_RK_convergence_closed"] is True, "internal benchmark not closed in policy")
    require(policy["benchmark_policy"]["external_RG_package_comparison"] == "OPEN", "external benchmark overclaimed")
    require(policy["values_promotable_now"] is False, "values overpromoted")

    require(qasu3["status"] == "QASU3_PACKET_INTEGRATION_RECHECKED_STILL_OPEN", "Qa/SU3 status mismatch")
    require(qasu3["can_integrate_selected_packet_now"] is False, "Qa/SU3 overclaimed")
    require(qasu3["final_packet_critical_open_row"]["id"] == "qa_su3_color_operator_packet", "critical Qa/SU3 row missing")
    for needed in ["selected D_E or rho_E operator data", "typed monad or section-ring source maps"]:
        require(needed in qasu3["needed_for_integration"], f"Qa/SU3 needed object missing: {needed}")

    for key in [
        "internal_RK_convergence_benchmark_closed",
        "threshold_mass_scheme_covariance_contract_built",
        "QaSU3_packet_integration_status_rechecked",
        "RG_acceptance_blockers_ranked",
        "source_gate_kept_separate_from_value_transport",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values",
        "accepted_lambda_H_MZ_value",
        "threshold_matching_values",
        "mass_scheme_conversion_values",
        "QaSU3_color_operator_packet",
        "SM_parity_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key in ["patched_SM_parity_closed", "true_SM_equivalence_closed", "no_knob_closed"]:
        require(data["closure_decision"][key] is False, f"closure overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "guardrail violated")
    require("internal benchmark = True" in note, "note missing benchmark result")
    require("Qa/SU3 color/operator packet remains" in note, "note missing Qa/SU3 separation")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
