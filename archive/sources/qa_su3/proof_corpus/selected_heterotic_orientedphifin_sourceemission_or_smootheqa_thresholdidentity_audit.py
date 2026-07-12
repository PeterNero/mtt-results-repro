"""Audit oriented Phi_fin source-emission / smooth E_Qa threshold identity gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_thresholdidentity_source_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceEmission_or_SmoothEQa_ThresholdIdentity_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEEMISSION_CURRENT_SOURCE_NOGO_REQUEST_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_ThresholdIdentity_SourceFill_or_SmoothEQa_Construction_v1"


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
    request = load(REQUEST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    support = data["closed_support"]
    open_fields = data["open_source_fields"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("algebraic support closed", support["same_BN_domain"] is True and support["commutation"] is True and support["oriented_table_built"] is True, support)
    check("source fields open", decision["open_source_field_count"] == 4 and all(item["closed"] is False for item in open_fields.values()), open_fields)
    check("current source nogo", decision["current_source_nogo"] is True and decision["mathematical_impossibility_claimed"] is False, decision)
    check("no threshold promotion", decision["source_emission_closed"] is False and decision["heterotic_threshold_magnitude_promoted"] is False, decision)
    check("support values retained", isinstance(decision["full_positive_logdet_support_value"], float) and isinstance(decision["oriented_abs_logdet_support_value"], float), decision)
    check("request must emit identity", "operator_identity" in request["must_emit"] and "finitepart_payload" in request["must_emit"], request["must_emit"])
    check("request forbids shortcuts", "use the oriented table logdet values before source emission" in request["forbidden_shortcuts"], request["forbidden_shortcuts"])
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records source request", str(REQUEST.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-emission / smooth E_Qa threshold-identity audit")


if __name__ == "__main__":
    main()
