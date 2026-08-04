"""Audit strict physical prefactor source or full-SM minimal-parameter packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_RECHECK_PACKET = PACKET_DIR / "strict_physical_prefactor_source_recheck.packet.json"
PARAMETER_POLICY_PACKET = PACKET_DIR / "p_ew_minimal_parameter_policy.packet.json"
FULLSM_AUDIT_SEED_PACKET = PACKET_DIR / "fullsm_minimal_parameter_audit_seed.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_pew_or_fullsm_parameter_ledger_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictPhysicalPrefactorSource_or_FullSMMinimalParameterAudit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_STRICTPHYSICALPREFACTORSOURCE_OR_FULLSMMINIMALPARAMETERAUDIT_"
    "STRICT_SOURCE_OPEN_MINIMAL_ONE_PRIMITIVE_POLICY_CLOSED"
)
NEXT = "MTT_Selected_FullSMMinimalParameterLedger_or_StrictPEWSourceTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    strict = load(STRICT_RECHECK_PACKET)
    policy = load(PARAMETER_POLICY_PACKET)
    seed = load(FULLSM_AUDIT_SEED_PACKET)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("strict", strict),
        ("policy", policy),
        ("seed", seed),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "next artifact")
    require(next_packet["next_required_artifact"] == NEXT, "next packet artifact")
    require(data["theorem"]["proved"] is True, "theorem")

    require(data["strict_prefactor_source_theorem_closed"] is False, "strict source overclaim")
    require(data["minimal_one_primitive_policy_closed"] is True, "minimal policy")
    require(data["H_lambda_lane_closed_at_one_primitive"] is True, "H/lambda lane")
    require(data["full_SM_minimal_parameter_audit_closed"] is False, "full ledger overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    decision = data["closure_decision"]
    require(decision["accepted_strict_prefactor_source_row_total"] == 0, "strict rows")
    require(decision["strict_P_EW_source_promoted"] is False, "strict P_EW promotion")
    require(decision["direct_K_threshold_Omega_H_lambda_emitted"] is False, "direct K overclaim")
    require(decision["P_EW_counted_as_shared_physical_primitive"] is True, "P_EW counted")
    require(decision["P_EW_parameter_count"] == 1, "P_EW count")
    require(decision["H_specific_parameter_count"] == 0, "H count")
    require(decision["lambda_H_used_as_selector"] is False, "lambda selector")
    require(decision["minimal_H_lambda_lane_ready_for_full_SM_ledger"] is True, "ledger readiness")
    require(decision["full_SM_minimal_parameter_ledger_closed"] is False, "ledger overclaim")

    require(strict["strict_prefactor_source_closed"] is False, "strict packet overclaim")
    require(strict["accepted_strict_row_total"] == 0, "strict packet rows")
    require(all(value is False for value in strict["required_strict_source_fields"].values()), "strict fields")

    primitive = policy["primitive"]
    require(primitive["parameter_count"] == 1, "policy primitive count")
    require(primitive["selected_source_data"] is False, "policy source overclaim")
    require(primitive["admitted_minimal_parameter"] is True, "policy admission")
    require(primitive["lambda_H_used_to_choose_value"] is False, "policy lambda selector")
    require(primitive["per_observable_retuning_allowed"] is False, "retuning")

    lane = policy["H_lambda_lane"]
    require(lane["H_specific_free_parameters"] == 0, "lane H count")
    require(lane["shared_physical_primitives"] == 1, "lane primitive count")
    require(lane["lambda_H_is_downstream_postcheck"] is True, "downstream lambda")
    require(lane["strict_no_knob_closed"] is False, "lane no-knob overclaim")

    seed_status = seed["global_full_SM_status"]
    require(seed["H_lambda_seed"]["lane_status"] == "closed_at_one_shared_physical_primitive", "seed lane")
    require(seed_status["full_minimal_parameter_ledger_closed"] is False, "seed ledger overclaim")
    require(seed_status["full_no_knob_closed"] is False, "seed no-knob overclaim")
    require(seed_status["true_SM_equivalence_claimed"] is False, "seed true SM overclaim")

    for phrase in [
        "StrictPhysicalPrefactorSourceOrFullSMMinimalParameterAuditTheorem",
        "total accepted strict rows = 0",
        "H-specific free parameters = 0",
        "shared physical primitives = 1",
        "lambda_H used as selector = false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: historical physical-prefactor diagnostic preserved: at this older "
        "diagnostic layer strict P_EW rows were 0, but this is superseded by the active "
        "strict P_EW denominator-selection/direct-K lock. Minimal one-primitive "
        "H/lambda policy is closed and exported to the full-SM ledger."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
