"""Audit minimal-new-source-packet fill / proof-closure gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_or_proofclosure.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_or_proofclosure.candidate.json"
REPORT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_report.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_or_proofclosure_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_MinimalNewSourcePacket_Fill_or_ProofClosure_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_MINIMAL_NEW_SOURCE_PACKET_FILL_ATTEMPT_IRREDUCIBLE_SOURCE_LEAF_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceLeaf_SourceEmitsOrientedBNCarrier_or_SelectedBundleConnectionA_v1"


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
    route_a = report["route_A_direct_fill"]
    route_b = report["route_B_smooth_fill"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("known exact value retained", report["known_values"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", report["known_values"])
    check("support prefilter/interface retained", report["source_prefilter_closed"] is True and report["smooth_interface_built"] is True, report)
    check("direct first leaf open", route_a["source_emits_oriented_BN_carrier"]["filled"] is False, route_a["source_emits_oriented_BN_carrier"])
    check("direct downstream open", route_a["source_emits_positive_PhiFin_D_E_magnitude_on_oriented_BN"]["filled"] is False and route_a["source_proves_finitepart_trace_identity_for_log92160000"]["filled"] is False, route_a)
    check("smooth first leaf open", route_b["selected_bundle_connection_A"]["filled"] is False, route_b["selected_bundle_connection_A"])
    check("smooth downstream open", route_b["E_Qa_matrix_or_equivalent_zero_order_block"]["filled"] is False and route_b["trace_lift_or_complement_quotient_proof"]["filled"] is False, route_b)
    check("irreducible leaf named", decision["irreducible_source_leaf_identified"] is True and decision["first_direct_leaf"] == "source_emits_oriented_BN_carrier" and decision["first_smooth_leaf"] == "selected_bundle_connection_A", decision)
    check("routes remain open", report["route_A_closed"] is False and report["route_B_closed"] is False and cert["route_A_direct_source_owned_operator_closed"] is False and cert["route_B_smooth_EQa_payload_closed"] is False, cert)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("note records report", str(REPORT.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin minimal-new-source-packet audit passed")


if __name__ == "__main__":
    main()
