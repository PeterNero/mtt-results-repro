"""Audit CKM, gauge-running, and PMNS convention fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_ckm_gauge_pmns_convention_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_CKM_Gauge_PMNS_Convention_Fill_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_ckm_gauge_pmns_convention_fill.py"

STATUS = "MTT_SM_EQUIVALENCE_CKM_GAUGE_PMNS_CONVENTION_FILL_BUILT_REPLAY_READY"
NEXT = "MTT_SM_Equivalence_Mixing_and_Gauge_Replay_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["source_boundary_preserved"] is True, "source boundary not preserved")

    ckm = data["CKM_packet"]
    require(ckm["status"] == "FILLED_REPLAY_READY_WITHOUT_COVARIANCE", "CKM status mismatch")
    require(ckm["unitarity_max_residual"] < 1e-12, "CKM not unitary")
    require(abs(ckm["jarlskog"]) > 1e-6, "CKM CP invariant missing")
    require(ckm["used_as_source_selector"] is False, "CKM used as selector")
    require(ckm["derived_parameters"]["delta_deg"] > 0, "CKM delta missing")

    pmns = data["PMNS_packet"]
    require(pmns["status"] == "FILLED_REPLAY_READY_WITHOUT_COVARIANCE", "PMNS status mismatch")
    require(pmns["ordering"] == "normal", "PMNS ordering mismatch")
    require(pmns["unitarity_max_residual"] < 1e-12, "PMNS not unitary")
    require(abs(pmns["jarlskog"]) > 1e-3, "PMNS CP invariant missing")
    require(pmns["used_as_source_selector"] is False, "PMNS used as selector")
    require(pmns["absolute_mass_policy"].startswith("not filled"), "absolute mass overfilled")

    gauge = data["gauge_packet"]
    require(gauge["status"] == "CONVENTION_FILLED_VALUES_PARTIAL_ALPHA_EM_MZ_OPEN", "gauge status mismatch")
    require(gauge["filled_reference_values"]["sin2_thetaW_MSbar_MZ"]["central_value"] == 0.23122, "sin2 mismatch")
    require(gauge["filled_reference_values"]["alpha_s_MZ"]["central_value"] == 0.1180, "alpha_s mismatch")
    require("alpha_em_MSbar_MZ" in gauge["open_reference_values"], "alpha_em(MZ) not left open")
    require("alpha_1_GUT" in gauge["conversion_formulas"], "U1 conversion missing")

    ready = data["replay_readiness"]
    require(ready["CKM_matrix_ready_for_replay"] is True, "CKM not replay-ready")
    require(ready["PMNS_matrix_ready_for_replay"] is True, "PMNS not replay-ready")
    require(ready["gauge_conventions_ready"] is True, "gauge conventions not ready")
    require(ready["gauge_alpha1_alpha2_alpha3_values_ready"] is False, "gauge triplet overclaimed")
    require(ready["full_covariance_ready"] is False, "covariance overclaimed")
    require(ready["RG_common_scale_ready"] is False, "RG overclaimed")

    closes = data["what_closes_now"]
    for key in [
        "CKM_convention_and_matrix_seed",
        "PMNS_convention_and_matrix_seed",
        "gauge_running_convention_packet",
        "mixing_unitarity_checks",
        "source_selection_guardrails_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "CKM_covariance_or_profile_policy",
        "PMNS_covariance_or_profile_policy",
        "alpha_em_MSbar_MZ_value",
        "alpha1_alpha2_alpha3_numeric_triplet",
        "common_RG_scale_transport",
        "mixing_and_gauge_replay",
        "full_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["sm_equivalence_claimed"] is False, "SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("measured replay inputs" in note, "note guardrail missing")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
