"""Audit BN27 source-domain bridge or smooth E_Qa quotient gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_orbitclosure_source_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceDomainBridge_or_SmoothEQa_Quotient_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_BRIDGE_CURRENT_SOURCE_OPEN_ORBITCLOSURE_REQUEST_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_OrbitClosure_SourceFill_v1"


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
    test = data["orbit_completion_test"]
    direct = data["routes"]["BN27_orbitclosure_source_bridge"]
    smooth = data["routes"]["smooth_EQa_quotient_to_BN27"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("embedding insufficient", decision["embedding_support_insufficient"] is True and test["verdict"] == "EMBEDDING_SUPPORT_INSUFFICIENT_FOR_SOURCE_BRIDGE", test)
    check("domain sizes", test["full_BN27_domain"]["basis_dimension"] == 27 and test["embedded_11_shadow"]["domain_label_count"] == 11, test)
    check("missing rows exact", test["completion_gap"]["missing_rows_count"] == 16 and test["completion_gap"]["missing_positive_oriented_row_count"] == 10, test["completion_gap"])
    check("product gap exact", test["completion_gap"]["embedded_abs_product"] == 16 and test["completion_gap"]["full_abs_sector_product"] == 92160000 and test["completion_gap"]["missing_multiplier_to_full_abs_sector"] == 5760000, test["completion_gap"])
    check("direct route support but open", direct["closed"] is False and all(value is True for value in direct["support"].values()), direct)
    check("smooth route open", smooth["closed"] is False and smooth["support"]["smooth_selected_bundle_A_packet_found"] is False, smooth)
    check("request built", decision["orbitclosure_source_request_built"] is True and request["status"] == "SOURCE_ORBIT_CLOSURE_REQUIRED", request)
    check("request must emit seven", set(request["must_emit"]) == {"selected_deck_action", "rank_slot_completion", "orbit_closure_rule", "kernel_policy", "trace_weight_policy", "compatibility", "audit_replay"}, request["must_emit"])
    check("forbidden shortcuts", "promote sparse 27x11 embedding as the source-domain bridge" in request["forbidden_shortcuts"], request["forbidden_shortcuts"])
    check("bridge remains open", decision["BN27_orbitclosure_source_bridge_closed"] is False and cert["BN27_orbitclosure_source_bridge_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records request", str(REQUEST.relative_to(ROOT)) in note and NEXT in note and "missing_multiplier_to_full_abs_sector = 5760000" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 source-domain bridge audit passed")


if __name__ == "__main__":
    main()
