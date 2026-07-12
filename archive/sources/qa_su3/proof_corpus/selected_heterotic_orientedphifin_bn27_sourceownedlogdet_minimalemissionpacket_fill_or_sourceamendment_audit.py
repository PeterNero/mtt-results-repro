"""Audit BN27 source-owned logdet minimal-emission packet fill/source-amendment gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimalemissionpacket_fill_or_sourceamendment.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimalemissionpacket_fill_or_sourceamendment.candidate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_source_amendment_template.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimalemissionpacket_fill_or_sourceamendment_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnedLogdet_MinimalEmissionPacket_Fill_or_SourceAmendment_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOWNED_LOGDET_FILL_ATTEMPT_SOURCE_AMENDMENT_REQUIRED"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_SQaSU3BN27_Declaration_or_ConnectionValueExport_v1"


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
    template = load(TEMPLATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("template built", decision["source_amendment_template_built"] is True and TEMPLATE.exists(), decision)
    check("conditional implication closed", decision["conditional_implication_theorem_closed"] is True and cert["conditional_implication_theorem_closed"] is True, data["conditional_implication_theorem"])
    check("direct lane still open", decision["direct_source_theorem_closed"] is False and data["lane_evaluation"]["direct_source_theorem_fill"]["closed_now"] is False, data["lane_evaluation"]["direct_source_theorem_fill"])
    check("kernel trace lane still open", decision["kernel_trace_ownership_closed"] is False and data["lane_evaluation"]["kernel_trace_ownership_fill"]["closed_now"] is False, data["lane_evaluation"]["kernel_trace_ownership_fill"])
    check("connection lane still open", decision["connection_or_smooth_source_closed"] is False and data["lane_evaluation"]["connection_or_smooth_source_fill"]["closed_now"] is False, data["lane_evaluation"]["connection_or_smooth_source_fill"])
    check("template direct source fields null", all(value is None for value in template["smallest_direct_source_amendment"].values()), template["smallest_direct_source_amendment"])
    check("template connection fields null", all(value is None for value in template["equivalent_connection_export"].values()), template["equivalent_connection_export"])
    check("known values retained", template["known_values_to_consume"]["oriented_abs_sector_product"] == 92160000 and template["known_values_to_consume"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", template["known_values_to_consume"])
    check("no closure", decision["source_owned_logdet_closed"] is False and decision["BN27_source_identity_closed"] is False and data["closure_claimed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records template", NEXT in note and str(TEMPLATE.relative_to(ROOT)) in note and "conditional_implication_theorem_closed = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 source-owned logdet minimal-emission fill/source-amendment audit passed")


if __name__ == "__main__":
    main()
