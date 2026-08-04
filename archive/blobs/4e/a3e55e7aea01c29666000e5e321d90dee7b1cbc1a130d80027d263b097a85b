from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "cross_repo_remaining_gates_source_triage_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    triage = cert["gate_triage"]
    imports = cert["useful_imports"]
    verdict = cert["verdict"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "CROSS_REPO_REMAINING_GATES_TRIAGED_BEST_NEXT_GATE_SELECTED_MATTER_PAYLOAD",
        "unexpected cross-repo triage status",
    )
    require(verdict["all_relevant_sibling_repos_checked"] is True, "sibling repos must be checked")
    require(verdict["missed_closed_remaining_gate_found"] is False, "must not find a missed closed gate")
    require(verdict["safe_to_claim_full_GR_or_full_SM_closure"] is False, "must not claim full closure")
    require(verdict["safe_to_import_numeric_matter_coefficients"] is False, "must not import absent coefficients")
    require(cert["no_missed_closed_proof"] is True, "no closed proof should be missed")

    expected_gates = {
        "absolute_SI_metrology",
        "selected_full_matter_stress_coefficients",
        "unconditional_GR_TT_operator_identity",
        "literal_GR_TT_noise_channel_identity",
    }
    require(set(triage) == expected_gates, "remaining gate set changed")
    require(all(row["promote_to_closed"] is False for row in triage.values()), "no gate may promote")

    require(
        triage["absolute_SI_metrology"]["evidence_status"] == "OBSTRUCTION_CERTIFIED",
        "dimensionful obstruction must be imported",
    )
    require(
        triage["selected_full_matter_stress_coefficients"]["q79_status"]
        == "SELECTED_FULL_SM_DATA_THEOREM_NOT_PROVED_SELECTED_DATA_ABSENT",
        "q79 full SM blocker changed",
    )
    require(
        triage["selected_full_matter_stress_coefficients"]["sm_payload_status"]
        == "MTT_SELECTED_PHIFIN_ALPHA1_PAYLOAD_ATTEMPT_BUILT_SELECTED_SPECTRAL_VALUES_OPEN",
        "sm payload blocker changed",
    )
    require(
        imports["full_sm_data_blocker"]["recommended_strategy"] == "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES",
        "recommended matter-source strategy changed",
    )
    require(
        imports["finite_retarded_kernel_patterns"]["what_cannot_be_used"]
        == "direct substitution as GR matter-stress or full smooth GR operator coefficients",
        "Qa/SU3 guardrail changed",
    )
    require(packet["best_next_gate"] == "selected_full_matter_stress_coefficients", "best next gate changed")
    require(packet["next_executable_artifact"] == "Selected_Matter_Payload_Import_Interface_v1", "next artifact changed")

    require("No missed closed theorem was found" in note, "note must report no missed theorem")
    require("cannot be substituted" in note and "matter coefficients" in note, "note must include Qa/SU3 guardrail")

    require(all(guards.values()), "all guardrails must be true")

    print("AUDIT_PASS: cross-repo remaining gates triaged; selected matter payload is the next best gate")


if __name__ == "__main__":
    main()
