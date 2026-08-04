"""Audit BN27 source-ownership transport/connection-witness value gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_witness.template.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnership_Transport_or_ConnectionWitness_Values_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOWNERSHIP_TRANSPORT_VALUES_BRANCHCERT_CLOSED_TRANSPORT_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectBN27_SourceIdentityTransport_Fill_or_TypedConnectionWitnessValues_v1"


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
    ranking = data["route_ranking"]
    fields = data["BN27_source_ownership_fields"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("branch certificate closed only", decision["branch_certificate_closed"] is True and decision["S_QaSU3_BN27_declared_as_selected_source"] is False, decision)
    check("BN27 ownership fields still open", all(value is False for value in fields.values()), fields)
    check("export still support-only", ranking["rank_2_selected_connection_witness_values"]["support_ready_count"] == 6 and ranking["rank_2_selected_connection_witness_values"]["export_filled_count"] == 1, ranking["rank_2_selected_connection_witness_values"])
    check("projective lift stays retired", decision["projective_rhoE_lift_reopened"] is False and ranking["rank_3_projective_rhoE_BN27_lift"]["retired_as_threshold_proof_source"] is True, ranking["rank_3_projective_rhoE_BN27_lift"])
    check("no transport closure", decision["transport_witness_values_found"] is False and decision["BN27_source_ownership_transport_closed"] is False and decision["selected_connection_witness_values_closed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("template required payload present", set(template["required_closed_payload"].keys()) == {
        "source_identity_transport_theorem",
        "S_QaSU3_BN27_declaration",
        "EndE_or_rhoE_to_BN27_carrier_functor",
        "BN27_deck_action_export",
        "operator_coemission_export",
        "kernel_policy_export",
        "trace_policy_export",
        "finitepart_identity_export",
        "not_routec_import_proof",
    }, template["required_closed_payload"])
    check("template lanes open", all(lane["status"] == "open" for lane in template["connection_values_family"].values()), template["connection_values_family"])
    check("support values retained", data["support_now_locked"]["basis_dimension"] == 27 and data["support_now_locked"]["oriented_abs_sector_product"] == 92160000, data["support_now_locked"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records template", NEXT in note and str(TEMPLATE.relative_to(ROOT)) in note and "projective_rhoE_lift_reopened = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 source-ownership transport/connection-witness audit passed")


if __name__ == "__main__":
    main()
