"""Audit post-policy CKM heavy-link vector execution contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_heavylinkvectors_after_policybridge_or_ckmlaw.py"

SLUG = "selected_heavylinkvectors_after_policybridge_or_ckmlaw"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HeavyLinkVectorValuesAfterPolicyBridge_or_CKMHigherBreakdownLaw_v1.md"
SLOT_CONTRACT = PACKET_DIR / "heavy_link_vector_slot_contract.packet.json"
SUPPORT_LEDGER = PACKET_DIR / "heavy_link_support_and_forbidden_proxy_ledger.packet.json"
EXECUTION_GATE = PACKET_DIR / "heavy_link_selected_value_execution_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_heavy_link_value_source_search.packet.json"

STATUS = "MTT_SELECTED_HEAVYLINKVECTORS_AFTER_POLICYBRIDGE_CONTRACT_READY_VALUES_OPEN"
NEXT = "MTT_Selected_HeavyLinkValueSourceSearch_or_SelectedCKMAngleLaw_v1"
REQUIRED = ["t_u13", "t_u23", "t_d13", "t_d23", "c_u13", "c_u23", "c_d13", "c_d23"]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    slots = load(SLOT_CONTRACT)
    support = load(SUPPORT_LEDGER)
    gate = load(EXECUTION_GATE)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, slots, support, gate, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["heavy_link_slot_contract_ready"] is True, "slot contract not ready")
    require(decision["required_heavy_link_entry_count"] == 8, "required count")
    require(decision["selected_heavy_link_entry_count"] == 0, "selected entry count overaccepted")
    require(decision["selected_heavy_link_values_emitted"] is False, "heavy values overemitted")
    require(decision["q79_phase_contact_closed"] is True, "q79 not closed")
    require(decision["leading_noncommutation_closed"] is True, "noncommutation not closed")
    require(decision["static_same_orientation_filter_closed"] is True, "static filter not closed")
    require(decision["mixed_branches_rejected_at_static_tier"] is True, "mixed branches not rejected")
    require(decision["CKM_angle_magnitudes_derived"] is False, "CKM angles overderived")
    require(decision["selected_CKM_orientation_source_closed"] is False, "orientation overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(slots["required_packet_entries"] == REQUIRED, "slot list mismatch")
    require(slots["required_entry_count"] == 8, "slot required count")
    require(slots["emitted_entry_count"] == 0, "slot emitted count")
    require(slots["missing_entries"] == REQUIRED, "missing slot list")
    require(slots["vector_formula"] == "Delta_v = Delta_t + chi_q Delta_c", "vector formula")

    require(support["q79_phase_contact"] is True, "support q79")
    require(support["leading_noncommutation_closed"] is True, "support noncommutation")
    require(support["static_same_orientation_filter_closed"] is True, "support filter")
    require(support["mixed_branches_rejected_at_static_tier"] is True, "support mixed")
    for proxy in ["observed_masses_and_mixings", "execution_ii_ckm_pmns_matrices", "execution_ii_yukawa_matrices"]:
        require(proxy in support["rejected_proxy_inputs_found"], f"proxy rejection missing: {proxy}")

    require(gate["selected_heavy_link_values_emitted"] is False, "gate heavy values")
    require(gate["selected_Delta_v_value_emitted"] is False, "gate delta v")
    require(gate["CKM_angle_magnitudes_derived"] is False, "gate CKM")
    require(gate["Jarlskog_value_derived"] is False, "gate J")
    for source in ["M_C1_alpha1 entries", "selected V_C1 functional", "explicit Hess_Xi blocks"]:
        require(source in gate["first_required_source_objects"], f"source object missing: {source}")

    for item in [
        "q79 CKM CP phase contact",
        "CKM/PMNS policy-tier bridge",
        "static same-orientation branch filter",
        "leading noncommutation criterion",
    ]:
        require(item in next_packet["do_not_reopen"], f"non-reopen missing: {item}")
    require(next_packet["search_targets"] == REQUIRED, "next search targets")
    for route in [
        "selected alpha1/C1 primitive contractions",
        "selected Hess_Xi and dotD operator blocks",
        "selected zero-mode contraction table",
        "source-owned up/down response orientation map",
    ]:
        require(route in next_packet["allowed_source_routes"], f"allowed route missing: {route}")
    for route in ["observed CKM angle backsolve", "benchmark Yukawa or CKM matrices", "per-entry empirical fitting"]:
        require(route in next_packet["forbidden_routes"], f"forbidden route missing: {route}")

    require(cert["heavy_link_slot_contract_ready"] is True, "cert slot")
    require(cert["required_heavy_link_entry_count"] == 8, "cert required count")
    require(cert["selected_heavy_link_entry_count"] == 0, "cert selected count")
    require(cert["selected_heavy_link_values_emitted"] is False, "cert heavy")
    require(cert["CKM_angle_magnitudes_derived"] is False, "cert CKM")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("eight-slot heavy-link vector" in note, "note heavy")
    require("No selected heavy-link values are emitted yet" in note, "note boundary")
    require(NEXT in note, "note next")

    print("Heavy-link vector contract audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
