"""Audit heterotic/Route-C same-source identity or selected connection witness gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_heterotic_routec_sourceidentity_or_selectedconnectionwitness.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_heterotic_routec_sourceidentity_or_selectedconnectionwitness.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_heterotic_routec_sourceidentity_or_selectedconnectionwitness_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_HeteroticRouteC_SourceIdentity_or_SelectedConnectionWitness_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_HETEROTIC_ROUTEC_SOURCEIDENTITY_OPEN_CONNECTION_WITNESS_REQUEST_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_SelectedConnectionWitness_Export_Fill_v1"


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
    routes = data["route_status"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("same source open", routes["same_source_identity"]["closed"] is False and decision["same_source_identity_closed"] is False, routes["same_source_identity"])
    check("typed witness open", routes["typed_monad_cech_witness"]["closed"] is False and routes["typed_monad_cech_witness"]["missing_count"] > 0, routes["typed_monad_cech_witness"])
    check("direct HYM open", routes["direct_hym_witness"]["closed"] is False and routes["direct_hym_witness"]["missing_count"] > 0, routes["direct_hym_witness"])
    check("finite routec open", routes["finite_routec_solve_witness"]["closed"] is False and routes["finite_routec_solve_witness"]["missing_count"] > 0, routes["finite_routec_solve_witness"])
    check("smooth EQA open", routes["smooth_bundle_EQa_witness"]["closed"] is False, routes["smooth_bundle_EQa_witness"])
    check("request built", decision["connection_witness_export_request_built"] is True and request["status"] == "SELECTED_CONNECTION_WITNESS_EXPORT_REQUIRED", request)
    check("acceptable families", set(request["acceptable_witness_families"]) == {"typed_monad_cech", "direct_hym", "finite_routec_solve", "smooth_EQa_quotient"}, request["acceptable_witness_families"])
    check("export fields", set(request["must_export_to_oriented_phifin"]) == {"source_identity", "BN27_deck_action", "operators", "kernel_policy", "trace_policy", "audit_replay"}, request["must_export_to_oriented_phifin"])
    check("no bridge closure", decision["BN27_orbitclosure_source_bridge_closed"] is False and cert["BN27_orbitclosure_source_bridge_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records request", str(REQUEST.relative_to(ROOT)) in note and NEXT in note and "selected_connection_witness_export_closed = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin heterotic/Route-C source identity audit passed")


if __name__ == "__main__":
    main()
