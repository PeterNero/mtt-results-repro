"""Audit full-quotient spectrum or OU/Hessian scale source packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_sourcepacket.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_sourcepacket.candidate.json"
SOURCE_PACKET = ROOT / "candidate_data" / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_required_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_sourcepacket_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_HYM_FullQuotientSpectrum_or_OUHessianScale_SourcePacket_v1.md"

STATUS = "HETEROTIC_HYM_FULLQUOTIENT_OR_OUHESSIAN_SOURCEPACKET_BUILT_PAYLOAD_OPEN"
NEXT = "Selected_Heterotic_HYM_FullQuotientSpectrum_or_OUHessianScale_FillAttempt_v1"


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
    source_packet = load(SOURCE_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and source_packet["status"] == "OPEN_VALUES_REQUIRED", (data["status"], cert["status"], source_packet["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("source packet built", decision["source_packet_built"] is True and data["closed_now"]["combined_source_packet"] is True, decision)
    check("lane A prioritized", decision["best_next_lane"] == "lane_A_full_quotient_DeltaA" and data["lane_scores"]["lane_A_full_quotient_DeltaA"]["current_best"] is True, data["lane_scores"])
    check("source backed invariant block", source_packet["already_source_backed"]["invariant_EndC3_block"]["positive_logdet_prime"] == "log(12*mu^9*(1+mu)*(2+mu)*(1+2*mu))", source_packet["already_source_backed"]["invariant_EndC3_block"])
    check("source backed Rplus", source_packet["already_source_backed"]["geometry_tensor_payload"]["R_plus_curvature"] is True and source_packet["already_source_backed"]["geometry_tensor_payload"]["R_plus_summary"]["nonzero_components"] == 68, source_packet["already_source_backed"]["geometry_tensor_payload"])
    check("required lane leaves open", all(value is None for value in source_packet["lane_A_full_quotient_DeltaA_required"].values()) and len(source_packet["lane_A_full_quotient_DeltaA_required"]) == 9, source_packet["lane_A_full_quotient_DeltaA_required"])
    check("no value closure", decision["full_quotient_spectrum_closed"] is False and decision["OU_Hessian_scale_closed"] is False and decision["mu_selected"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("forbidden promotions", "promote R_plus curvature to bundle curvature F_A" in source_packet["forbidden_promotions"] and "select mu=1 from internal determinant units for the physical heterotic threshold" in source_packet["forbidden_promotions"], source_packet["forbidden_promotions"])
    check("no closure overclaim", data["closure_claimed"] is False and source_packet["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("note records packet", str(SOURCE_PACKET.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic HYM full-quotient / OU-Hessian source-packet audit")


if __name__ == "__main__":
    main()
