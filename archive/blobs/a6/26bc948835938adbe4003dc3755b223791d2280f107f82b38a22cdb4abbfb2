"""Audit selected Route-C provenance-or-basis support import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_provenance_or_basis_support_import.candidate.json"
CERT = ROOT / "certificates" / "routec_provenance_or_basis_support_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_Provenance_or_Basis_Support_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_provenance_or_basis_support.py"

STATUS = "ROUTEC_PROVENANCE_OR_BASIS_SUPPORT_IMPORTED_PRIMITIVE_EMISSION_OPEN"
NEXT = "MTT_Selected_PhiFin_Payload_or_BN_Basis_Emission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    upstream = data["upstream_support"]
    require(upstream["calculation"]["support_closed"]["provenance_support_closed"] is True, "provenance support not closed")
    require(upstream["calculation"]["support_closed"]["basis_support_closed"] is True, "basis support not closed")
    require(upstream["calculation"]["any_gate_closed"] is False, "a gate unexpectedly closed")
    require(upstream["provenance_gate"]["minimal_missing_primitive"] == "Phi_fin_selected_payload", "wrong provenance primitive")
    require(upstream["basis_gate"]["minimal_missing_primitive"] == "quotient_valid_B_N_basis_certificate", "wrong basis primitive")
    require(upstream["what_remains_open"]["honest_manifest_without_lifted_flags"] is True, "honest replay overclosed")

    guard = data["guardrails"]
    for key in [
        "claims_provenance_gate_closed",
        "claims_basis_gate_closed",
        "claims_selected_Phi_fin_payload",
        "claims_quotient_valid_BN_basis_certificate",
        "claims_honest_manifest_without_lifted_flags",
        "claims_selected_source_flags_promoted",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("primitive emission" in note, "note missing primitive-emission frontier")
    require("honest manifest still cannot be replayed" in note, "note missing honest replay guardrail")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
