"""Audit Route-C R1/R4 fill-attempt import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_r1_r4_fill_attempt_import.candidate.json"
CERT = ROOT / "certificates" / "routec_r1_r4_fill_attempt_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_R1_R4_FillAttempt_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_r1_r4_fill_attempt.py"

STATUS = "ROUTEC_R1_R4_FILL_ATTEMPT_IMPORTED_PRIMITIVE_SEARCH_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1"


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

    upstream = data["upstream_fill_attempt"]
    r1 = upstream["R1_source_certificate_attempt"]
    r4 = upstream["R4_BN_basis_attempt"]
    require(r1["closed"] is False, "R1 overclosed")
    require(r4["closed"] is False, "R4 overclosed")
    require(upstream["R6_honest_replay"]["ready"] is False, "R6 overclosed")
    require(r1["blocking_missing_fields"]["Phi_fin_selected_values"] is True, "R1 blocker missing")
    require(r4["blocking_missing_fields"]["scalar_basis_functions_phi_m"] is True, "R4 blocker missing")

    guard = data["guardrails"]
    for key in [
        "claims_R1_closed",
        "claims_R4_closed",
        "claims_R6_ready",
        "claims_selected_Phi_fin_values",
        "claims_selected_minimizer_identifier",
        "claims_scalar_basis_functions_phi_m",
        "claims_selected_DE_action_on_basis",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("Honest replay remains blocked" in note, "note missing replay blocker")
    require("selected primitive emission" in note, "note missing primitive search")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
