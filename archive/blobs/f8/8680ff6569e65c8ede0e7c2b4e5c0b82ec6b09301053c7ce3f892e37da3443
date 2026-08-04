"""Audit the selected U1/Y Route-C hybrid Galerkin overlap source packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_hybrid_galerkin_overlap_source_packet.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_hybrid_galerkin_overlap_source_packet.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_hybrid_galerkin_overlap_source_packet_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    result = data["hybrid_packet_result"]
    validators = data["validator_inputs"]

    check(
        "status exact",
        data["status"] == "U1Y_ROUTEC_HYBRID_GALERKIN_OVERLAP_PACKET_BUILT_VALUES_OPEN",
        data["status"],
    )
    check(
        "field counts exact",
        result["required_count"] == 7
        and result["support_present_count"] == 6
        and result["selected_emitted_count"] == 0
        and cert["selected_emitted_count"] == 0,
        result,
    )
    check(
        "packet not closed and current source no-go",
        result["packet_closed"] is False
        and data["decision"]["current_source_record_no_go"] is True
        and cert["current_source_record_no_go"] is True,
        data["decision"],
    )
    check(
        "all selected fields open",
        all(value is False for value in data["selected_fields"].values())
        and data["what_remains_open"]["source_identity"] is True
        and data["what_remains_open"]["primitive_contractions"] is True,
        data["selected_fields"],
    )
    check(
        "support broad but singlet support missing",
        data["support_fields"]["source_identity"] is True
        and data["support_fields"]["normalization"] is True
        and data["support_fields"]["singlet_neutrino_rule"] is False,
        data["support_fields"],
    )
    check(
        "fixtures and honest routec remain unselected",
        validators["qutrit_finite_validator_passes"] is True
        and validators["qutrit_promotes_to_selected"] is False
        and validators["selected_source_verified"] is False
        and validators["honest_de_action_pass"] is False
        and validators["honest_dotd_response_pass"] is False,
        validators,
    )
    check(
        "next fill-or-nogo artifact named",
        data["decision"]["best_next_artifact"] == "Selected_U1Y_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1"
        and cert["next_artifact"] == "Selected_U1Y_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1",
        cert,
    )
    check(
        "guardrails hold",
        data["guardrails"]["claims_A_selected"] is False
        and data["guardrails"]["claims_lambda12"] is False
        and data["guardrails"]["promotes_fixture_as_selected"] is False
        and data["target_fitting_used"] is False,
        data["guardrails"],
    )
    check(
        "note records current no-go and next artifact",
        "current_source_record_no_go = true" in note
        and "Selected_U1Y_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1" in note
        and "Do not promote finite SU5/qutrit fixture data as selected" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
