"""Audit BN27 orbit-closure source fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill.candidate.json"
REPORT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill_report.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_orbitclosure_sourcefill_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_OrbitClosure_SourceFill_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_ORBITCLOSURE_FILL_ATTEMPT_SUPPORT_ONLY_SOURCE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_HeteroticRouteC_SourceIdentity_or_SelectedConnectionWitness_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    report = load(REPORT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    fill = report["fill_status"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("fill count", report["filled_count"] == 2 and report["required_count"] == 7 and decision["filled_count"] == 2, report)
    check("compatibility and audit only", fill["compatibility"]["filled"] is True and fill["audit_replay"]["filled"] is True, fill)
    check("deck action support only", fill["selected_deck_action"]["filled"] is False and fill["selected_deck_action"]["support"]["present"] is True, fill["selected_deck_action"])
    check("rank slot support only", fill["rank_slot_completion"]["filled"] is False and fill["rank_slot_completion"]["support"]["rank_slot_count"] == 3, fill["rank_slot_completion"])
    check("orbit closure open", fill["orbit_closure_rule"]["filled"] is False and decision["orbit_closure_rule_closed_for_heterotic_source"] is False, fill["orbit_closure_rule"])
    check("kernel trace source open", fill["kernel_policy"]["filled"] is False and fill["trace_weight_policy"]["filled"] is False and decision["kernel_trace_policy_source_owned"] is False, fill)
    check("audit replay values", fill["audit_replay"]["support"]["oriented_nonzero_positive_rows"] == 16 and fill["audit_replay"]["support"]["oriented_abs_sector_product"] == 92160000, fill["audit_replay"])
    check("routec state not closed", report["routec_source_state"]["selected_basis_B_N_emitted_in_old_subpacket"] is False and report["routec_source_state"]["selected_routec_source_certificate_closed"] is False, report["routec_source_state"])
    check("cutset named", report["source_identity_cutset"]["status"] == "SELECTED_CONNECTION_WITNESS_REQUIRED" and "same_source_identity" in report["source_identity_cutset"]["minimal_closing_payload"], report["source_identity_cutset"])
    check("bridge remains open", decision["BN27_orbitclosure_source_bridge_closed"] is False and cert["BN27_orbitclosure_source_bridge_closed"] is False, cert)
    check("branch remains open", decision["branch_identity_closed"] is False and cert["branch_identity_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records report", str(REPORT.relative_to(ROOT)) in note and NEXT in note and "BN27_orbitclosure_source_bridge_closed = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 orbit-closure sourcefill audit passed")


if __name__ == "__main__":
    main()
