"""Audit the U1/Y Route-C 1_M singlet-neutrino support-promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_singlet_neutrino_rule_support_promotion_or_nogo.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_singlet_neutrino_rule_support_promotion_or_nogo.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_singlet_neutrino_rule_support_promotion_or_nogo_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SingletNeutrinoRule_SupportPromotion_or_NoGo_v1.md"

STATUS = "U1Y_ROUTEC_1M_SINGLET_NEUTRINO_RULE_SUPPORT_PROMOTED_SELECTED_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_SameSource_SelectedEmission_SourceCertificate_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    revised = data["revised_counts_if_support_promoted"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("support witnesses sufficient", cert["support_witness_count"] >= 5 and "finite_cochain_source" in data["support_witnesses"], data["support_witnesses"]),
        check("support count promoted", cert["previous_support_present"] == 6 and cert["revised_support_present"] == 7 and revised["required"] == 7, revised),
        check("singlet support yes selected no", decision["singlet_neutrino_rule_support_promoted"] is True and decision["singlet_neutrino_rule_selected_emitted"] is False, decision),
        check("support gap only", decision["support_gap_closed"] is True and decision["selected_emission_gap_closed"] is False, decision),
        check("selected packet still open", cert["selected_emitted"] == 0 and cert["same_source_packet_closed"] is False and data["closure_claimed"] is False, cert),
        check("contract names selected emission", "same-source selected visible/operator source certificate" in data["selected_emission_contract"]["must_emit_next"], data["selected_emission_contract"]),
        check("guardrails hold", guardrails["claims_selected_emission_closed"] is False and guardrails["claims_lambda12"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records support not selected", "support promotion" in note and "not a same-source selected" in note and "Do not compute `lambda_12`" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C singlet-neutrino support-promotion audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
