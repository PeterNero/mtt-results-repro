"""Audit oriented Phi_fin magnitude finite-part source-theorem attempt."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_MagnitudeFinitepart_SourceTheorem_or_SmoothEQa_TraceIdentity_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_MAGNITUDE_FINITEPART_EXACTLY_COMPUTED_SOURCE_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_PositiveMagnitude_SourceOwnership_or_SmoothEQa_Emission_v1"


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
    packet = load(PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    values = packet["finitepart_values"]
    source_gate = packet["source_gate"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("sector products", values["plus_sector_product"] == 9600 and values["minus_sector_product"] == 9600 and values["oriented_abs_sector_product"] == 92160000, values)
    check("full product", values["full_positive_product"] == 884736000000 and values["full_positive_logdet_exact"] == "log(884736000000)", values)
    check("numeric logdet matches exact", abs(values["oriented_abs_sector_logdet_numeric"] - math.log(92160000)) < 1e-12, values)
    check("table finitepart computed", decision["oriented_table_magnitude_finitepart_computed"] is True and decision["oriented_abs_sector_logdet_exact"] == "log(92160000)", decision)
    check("source gate remains open", source_gate["orientation_functor_closed"] is True and source_gate["closed"] is False, source_gate)
    check("no source promotion", decision["source_owned_positive_PhiFin_magnitude"] is False and source_gate["source_owned_positive_PhiFin_magnitude"] is False, (decision, source_gate))
    check("no trace identity", decision["finitepart_trace_identity_closed"] is False and source_gate["finitepart_trace_identity_closed"] is False, (decision, source_gate))
    check("smooth lane open", decision["smooth_E_Qa_trace_identity_closed"] is False and source_gate["smooth_E_Qa_emitted"] is False, source_gate)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records exact value", "log(92160000)" in note and str(PACKET.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin magnitude finitepart audit passed")


if __name__ == "__main__":
    main()
