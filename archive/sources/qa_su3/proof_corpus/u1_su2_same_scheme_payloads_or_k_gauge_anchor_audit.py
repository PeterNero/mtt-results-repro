"""Audit the U1/SU2 same-scheme payload or K_gauge anchor gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "u1_su2_same_scheme_payloads_or_k_gauge_anchor_certificate.json"
DATA = REPO / "candidate_data" / "u1_su2_same_scheme_payloads_or_k_gauge_anchor.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_SU2_Same_Scheme_Internal_Payloads_or_K_Gauge_Anchor_v1.md"
SCRIPT = REPO / "scripts" / "build_u1_su2_same_scheme_payloads_or_k_gauge_anchor.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def by_field(contract: list[dict[str, object]], field: str) -> dict[str, object]:
    return next(item for item in contract if item["field"] == field)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    decision = data["decision"]
    contract = data["acceptance_contract"]
    sources = data["current_sources"]
    scan = sources["repo_scan"]
    checks = [
        check("status", cert["status"] == "U1_SU2_SAME_SCHEME_ACCEPTANCE_CONTRACT_BUILT_PAYLOADS_AND_K_GAUGE_OPEN", cert["status"]),
        check("script agreement", computed["what_remains_open"] == cert["what_remains_open"], computed["what_remains_open"]),
        check("Qa payload carried forward", by_field(contract, "I_Qa")["current_value"] == "log(2008)", by_field(contract, "I_Qa")),
        check("U1 remains open", by_field(contract, "I_1")["current_status"] == "OPEN" and decision["U1_same_scheme_payload"] == "OPEN", decision),
        check("SU2 remains open", by_field(contract, "I_2")["current_status"] == "OPEN" and decision["SU2_same_scheme_payload"] == "OPEN", decision),
        check("K_gauge remains open", by_field(contract, "K_gauge")["current_status"] == "OPEN" and decision["K_gauge_anchor"] == "OPEN", decision),
        check("hypercharge normalization not assumed", by_field(contract, "hypercharge_normalization_policy")["current_status"] == "OPEN", by_field(contract, "hypercharge_normalization_policy")),
        check("no measured closure", decision["measured_electroweak_closure"] is False and decision["full_SM_closure"] is False, decision),
        check("SM structural support present", sources["sm_sector_embedding_interface"]["status"] == "MTT_SM_SECTOR_EMBEDDING_INTERFACE_BUILT_RECOVERY_OPEN", sources["sm_sector_embedding_interface"]),
        check("selected SM packet still open", sources["actual_selected_sm_packet_audit"]["status"] == "MTT_ACTUAL_SELECTED_SM_PACKET_AUDIT_BUILT_PACKET_STILL_OPEN", sources["actual_selected_sm_packet_audit"]),
        check("measured parameter policy imported", sources["core_axioms_measured_parameter_interface"]["status"] == "MTT_CORE_AXIOMS_MEASURED_PARAMETER_INTERFACE_BUILT_SM_PARITY_OPEN", sources["core_axioms_measured_parameter_interface"]),
        check("no exact same-scheme payload found", scan["same_scheme_payloads_present"] is False, scan),
        check(
            "structural support without payloads",
            scan["structural_terms_found"]["anomaly"]
            and sources["sm_sector_embedding_interface"]["structural_support"]["selected_sm_packet_schema"]
            and sources["actual_selected_sm_packet_audit"]["structural_support"]["corpus_support_for_SM_structure_audited"],
            scan,
        ),
        check("fill templates exist", set(data["next_fill_templates"]) == {"Selected_U1_Internal_Overlap_Payload_v1", "Selected_SU2_Internal_Overlap_Payload_v1", "Selected_K_Gauge_Anchor_Packet_v1"}, data["next_fill_templates"]),
        check("note records decision", "U1_same_scheme_payload = OPEN" in note and "K_gauge_anchor = OPEN" in note, NOTE),
    ]
    print("\nSelected U1/SU2 same-scheme payload or K_gauge anchor audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
