"""Audit Qa/SU3 parity-interface replacement and final SM-parity closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_qasu3sourcepacket_or_finalsmparityclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
QASU3_REPLACEMENT = PACKET_DIR / "qasu3_parity_interface_replacement.packet.json"
FINAL_PACKET = PACKET_DIR / "final_sm_packet_certificate_parity_closure.packet.json"
CLOSURE_DECISION = PACKET_DIR / "sm_parity_closure_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_QaSU3SourcePacket_or_FinalSMParityClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_QASU3SOURCEPACKET_OR_FINALSMPARITYCLOSURE_BUILT_SM_PARITY_CLOSED_NOKNOB_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    replacement = load(QASU3_REPLACEMENT)
    final_packet = load(FINAL_PACKET)
    decision = load(CLOSURE_DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(replacement["accepted_for_SM_parity_interface"] is True, "QaSU3 parity interface not accepted")
    require(replacement["accepted_as_actual_selected_no_knob_packet"] is False, "QaSU3 no-knob overclaimed")
    require(replacement["accepted_for_true_precision_equivalence"] is False, "true equivalence overclaimed")
    require(replacement["support_presence"]["all_required_support_present"] is True, "required support missing")
    require(
        replacement["parity_interface_closure"]["qa_su3_color_operator_packet_closed_for_sm_parity_interface"] is True,
        "QaSU3 SM-parity row not closed",
    )
    require(
        replacement["parity_interface_closure"]["qa_su3_color_operator_packet_closed_as_actual_no_knob_packet"] is False,
        "QaSU3 no-knob row overclaimed",
    )
    for key in [
        "observed_data_used_as_selector",
        "target_fitting_used",
        "q79_cp_success_used_as_direct_color_proof",
        "identity_rhoE_promoted",
        "benchmark_matrices_promoted",
        "actual_operator_packet_claimed",
    ]:
        require(replacement["guardrails"][key] is False, f"guardrail violated: {key}")

    require(final_packet["status"] == "FINAL_SM_PACKET_CERTIFICATE_CLOSED_FOR_SM_PARITY_VIA_QASU3_INTERFACE_REPLACEMENT", "final packet status mismatch")
    require(final_packet["all_source_rows_closed_for_sm_parity_interface"] is True, "not all source rows closed")
    require(final_packet["any_source_row_closed_as_actual_no_knob_packet"] is False, "no-knob packet row overclaimed")
    require(final_packet["can_close_SM_parity_interface_now"] is True, "SM-parity certificate not closed")
    require(final_packet["can_close_true_SM_equivalence_now"] is False, "true equivalence overclaimed")
    require(final_packet["can_close_no_knob_SM_derivation_now"] is False, "no-knob closure overclaimed")
    qasu3_row = final_packet["qasu3_row"]
    require(qasu3_row["id"] == "qa_su3_color_operator_packet", "QaSU3 row missing")
    require(qasu3_row["closed_for_sm_parity_interface"] is True, "QaSU3 final row not parity closed")
    require(qasu3_row["closed_as_actual_selected_no_knob_packet"] is False, "QaSU3 final row no-knob overclaimed")
    require("parity_interface_replacement" in qasu3_row, "QaSU3 replacement marker missing")

    require(decision["SM_parity_closed"] is True, "SM parity not closed")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob closure overclaimed")
    require(decision["current_SM_parity_blockers"] == [], "SM parity blockers remain")
    require(decision["closed_now"] == ["selected_SM_packet_certificate_integration"], "closed gate mismatch")
    require(decision["observed_data_used_as_selector"] is False, "observed selector violation")
    require(decision["target_fitting_used"] is False, "target fitting violation")

    require(data["closure_decision"]["SM_parity_closed"] is True, "candidate closure decision mismatch")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclaimed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclaimed")
    require(data["actual_selected_operator_packet_claimed"] is False, "operator packet overclaimed")
    require(data["source_boundary_preserved"] is True, "source boundary not preserved")
    require(cert["SM_parity_closed"] is True, "certificate SM parity flag mismatch")
    require(cert["true_SM_equivalence_closed"] is False, "certificate true equivalence overclaimed")
    require(cert["no_knob_closed"] is False, "certificate no-knob overclaimed")
    require("SM-parity closure = True" in note, "note missing SM-parity closure statement")
    require("no-knob closure = False" in note, "note missing no-knob guardrail")
    require("superset interface closure" in note, "note missing superset method")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
