"""Audit PSM-C1-02 SI-1u-B2 local-principle source-packet validation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_psm_c1_02_primitivequadratureexport_or_unpatchedsourcepromotionpacket.py"

SLUG = "selected_psm_c1_02_primitivequadratureexport_or_unpatchedsourcepromotionpacket"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
LOCAL_PSM_PACKET = BASE / "local_principle_psm_source_promotion_packet.packet.json"
LOCAL_PSM_VALIDATION = BASE / "local_principle_psm_source_promotion_validator_result.packet.json"
SOURCE_FIELD_BINDING = BASE / "psm_source_field_binding_from_110row_packet.packet.json"
UNPATCHED_GUARD = BASE / "unpatched_theorem_guardrail_after_b2.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PrimitiveQuadratureExport_or_UnpatchedSourcePromotionPacket_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_B2_LOCAL_PRINCIPLE_SOURCE_PACKET_VALIDATES_UNPATCHED_THEOREM_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_UnpatchedSelectedActionDerivation_or_HonestFiniteC1Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "global closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    packet = load(LOCAL_PSM_PACKET)
    validation = load(LOCAL_PSM_VALIDATION)
    binding = load(SOURCE_FIELD_BINDING)
    guardrail = load(UNPATCHED_GUARD)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1u-B2", "SOURCE-IDENTITY/SI-1u-A"], "routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["theorem"]["proved"] is True and candidate["theorem"]["patched"] is True, "theorem metadata mismatch")

    require(validation["passes"] is True and validation["returncode"] == 0, "PSM validator should pass")
    require(packet["mode"] == "local_principle_patched_replay", "packet mode mismatch")
    require(packet["same_branch"] is True, "packet same_branch missing")
    require(packet["locked_target_values_used_as_source"] is False, "locked target used as source")
    require(packet["strict_110_row_payload_validator_passes"] is True, "strict 110-row flag missing")
    require(packet["emitted_before_residual_replay"] is True, "emitted-before flag missing")
    require(packet["row_counts"]["primitive_kernel_rows"] == 72, "primitive row count mismatch")
    require(packet["row_counts"]["hessian_b_source_rows"] == 2, "hessian row count mismatch")
    require(packet["row_counts"]["sector_assembly_rows"] == 36, "sector row count mismatch")
    for name, field in packet["source_fields"].items():
        require(field["selected_emitted"] is True, f"{name} selected flag missing")
        require(field["theorem_derived"] is True, f"{name} theorem flag missing")
        require(field["source_owner_verified"] is True, f"{name} owner flag missing")
        require(field["same_branch"] is True, f"{name} branch flag missing")

    require(binding["status"] == "PSM_SOURCE_FIELDS_BOUND_TO_LOCAL_PRINCIPLE_110ROW_PACKET", "binding status mismatch")
    require(binding["row_counts"]["primitive_kernel_rows"] == 72, "binding primitive mismatch")
    require(binding["row_counts"]["hessian_b_source_rows"] == 2, "binding hessian mismatch")
    require(binding["row_counts"]["sector_assembly_rows"] == 36, "binding sector mismatch")
    require(binding["row_counts"]["total_source_rows"] == 110, "binding total mismatch")
    require(binding["all_rows_independent_of_residual_replay"] is True, "binding independence missing")
    require(binding["local_principle_inserted"] is True, "binding local principle missing")
    require(binding["derived_unpatched"] is False, "binding overclaims unpatched")

    require(guardrail["status"] == "LOCAL_PRINCIPLE_VALIDATION_SEPARATED_FROM_UNPATCHED_THEOREM", "guardrail status mismatch")
    require(guardrail["current_unpatched_packet_passes"] is False, "current packet overaccepted")
    require(guardrail["local_principle_psm_packet_passes"] is True, "local packet missing")
    require(guardrail["unpatched_SelectedFiniteC1SourceIdentityTheorem"] is False, "unpatched theorem overclosed")
    require(guardrail["derive_principle_from_selected_action"] is False, "action derivation overclosed")
    require(guardrail["honest_new_finite_action_or_galerkin_execution"] is False, "honest execution overclosed")

    require(candidate["what_closes_now"]["SI1u_B2_local_principle_primitive_source_packet_validates"] is True, "B2 local closure missing")
    require(candidate["what_remains_open"]["unpatched_SelectedFiniteC1SourceIdentityTheorem"] is True, "unpatched theorem not open")
    require(candidate["closure_decision"]["local_principle_psm_packet_passes"] is True, "candidate validation missing")
    require(candidate["closure_decision"]["current_unpatched_packet_passes"] is False, "candidate current overaccepted")
    require(candidate["closure_decision"]["patched_local_principle_closure_claimed"] is True, "patched closure missing")
    require(candidate["closure_decision"]["unpatched_theorem_closed"] is False, "unpatched overclosed")
    require(candidate["patched_spine_closure_claimed"] is True, "patched spine flag missing")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A", "next primary mismatch")
    require(next_work["replacement"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2", "replacement label mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["local_principle_psm_packet_passes"] is True, "cert validation missing")
    require(cert["current_unpatched_packet_passes"] is False, "cert current overaccepted")
    require(cert["patched_local_principle_closure_claimed"] is True, "cert patched missing")
    require(cert["unpatched_theorem_closed"] is False, "cert unpatched overclosed")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2`" in note, "note B2 label missing")
    require("This is not the unpatched theorem" in note, "note guardrail missing")
    require("These are not" in note and "knobs" in note, "note superset guard missing")

    for item in [candidate, packet, binding, guardrail, cert]:
        guard(item)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
