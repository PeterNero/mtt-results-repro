"""Audit selected Route-C primitive emission search import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_selected_primitive_emission_search_import.candidate.json"
CERT = ROOT / "certificates" / "routec_selected_primitive_emission_search_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_SelectedPrimitiveEmissionSearch_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_selected_primitive_emission_search.py"

STATUS = "ROUTEC_SELECTED_PRIMITIVE_SEARCH_IMPORTED_NONIDENTITY_RHOE_BN_OPEN"
NEXT = "MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1"


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

    upstream = data["upstream_primitive_search"]
    results = upstream["search_results"]
    require(results["Phi_fin_payload"]["selected_values_emitted"] is False, "Phi_fin overclosed")
    require(results["Phi_fin_payload"]["identity_smoke_rejected"] is True, "identity rhoE not rejected")
    require(results["B_N_basis"]["required_success_gates_pass"] is False, "BN overclosed")
    require(results["formal_lift_diagnostic"]["promotion_allowed"] is False, "formal lift promoted")

    guard = data["guardrails"]
    for key in [
        "claims_legal_primitive_found",
        "claims_selected_Phi_fin_payload",
        "claims_quotient_valid_BN_payload",
        "claims_identity_rhoE_selected",
        "claims_formal_lift_is_proof",
        "claims_R1_R4_R6_closed",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("found no legal selected primitive" in note, "note missing strict search result")
    require("identity `rho_E` smoke: rejected" in note, "note missing identity rhoE rejection")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
