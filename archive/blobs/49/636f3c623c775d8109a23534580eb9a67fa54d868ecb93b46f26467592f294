"""Audit the source-leaf direct-carrier or bundle-A gate for oriented Phi_fin."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundleA.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_source_theorem_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceLeaf_DirectCarrier_or_BundleA_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCELEAF_DIRECT_CARRIER_OR_BUNDLE_A_CURRENT_SOURCE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceLeaf_SourceAmendment_or_CorpusDiscovery_v1"


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
    direct = data["direct_leaf_attempt"]
    smooth = data["smooth_leaf_attempt"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("direct carrier remains open", direct["source_emits_oriented_BN_carrier"]["closed"] is False, direct["source_emits_oriented_BN_carrier"])
    check("orientation support retained", direct["source_emits_oriented_BN_carrier"]["support_present"] is True and data["parent_statuses"]["orientation_functor"].endswith("MAGNITUDE_OPEN"), data["parent_statuses"])
    check("positive functor remains open", direct["source_emits_positive_operator_domain_and_functor"]["closed"] is False, direct["source_emits_positive_operator_domain_and_functor"])
    check("logdet not promoted", direct["finitepart_trace_identity_for_log92160000"]["support_present"] is True and direct["finitepart_trace_identity_for_log92160000"]["closed"] is False, direct["finitepart_trace_identity_for_log92160000"])
    check("bundle A remains open", smooth["selected_bundle_connection_A"]["closed"] is False and smooth["selected_bundle_connection_A"]["support_present"] is True, smooth["selected_bundle_connection_A"])
    check("R plus not promoted", smooth["bundle_curvature_F_A"]["closed"] is False and smooth["bundle_curvature_F_A"]["support_present"] is True, smooth["bundle_curvature_F_A"])
    check("standard embedding kept retired", smooth["standard_embedding_reopen"]["closed"] is False and data["parent_statuses"]["standard_embedding_gate"].endswith("PHIFIN_DIRECT_OPERATOR_PRIMARY"), data["parent_statuses"])
    check("request built", request["status"] == "SOURCE_THEOREM_REQUIRED" and cert["source_theorem_request_built"] is True, request["status"])
    check("request has both lanes", set(request) >= {"lane_A_direct_carrier_required", "lane_B_bundle_A_required", "must_not_use"}, request.keys())
    check("direct request asks for carrier", "same_branch_source_emits_oriented_BN_carrier" in request["lane_A_direct_carrier_required"], request["lane_A_direct_carrier_required"])
    check("smooth request asks for bundle A", "selected_bundle_connection_A_or_projective_connection" in request["lane_B_bundle_A_required"], request["lane_B_bundle_A_required"])
    check("forbidden shortcuts", "R+ curvature as bundle F_A" in request["must_not_use"] and "27x11 rho-shadow embedding as a threshold functor" in request["must_not_use"], request["must_not_use"])
    check("no closure", decision["direct_carrier_leaf_closed"] is False and decision["bundle_A_leaf_closed"] is False and data["closure_claimed"] is False and cert["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records request", NEXT in note and str(REQUEST.relative_to(ROOT)) in note and "Source Theorem Request" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-leaf direct-carrier or bundle-A audit passed")


if __name__ == "__main__":
    main()
