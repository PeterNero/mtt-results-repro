"""Audit selected Route-C non-identity rho_E/B_N construction import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_nonidentity_rhoe_bn_construction_import.candidate.json"
CERT = ROOT / "certificates" / "routec_nonidentity_rhoe_bn_construction_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_NonIdentity_RhoE_BN_Construction_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_nonidentity_rhoe_bn_construction.py"

STATUS = "ROUTEC_NONIDENTITY_RHOE_PACKET_IMPORTED_SMOOTH_BN_OPEN"
NEXT = "MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1"


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

    upstream = data["upstream_nonidentity_rhoe_bn"]
    gates = upstream["rho_E_candidate"]["numeric_gates"]
    basis = upstream["B_N_scaffold"]
    require(gates["passes_numeric_packet_gate"] is True, "rho_E numerical packet failed")
    require(gates["nonidentity_norm"] > 0.1, "rho_E is identity-like")
    require(upstream["rho_E_candidate"]["selected_by_mtt"] is False, "rho_E source promotion overclaimed")
    require(basis["passes_B_N_payload_gate"] is False, "B_N payload overclosed")
    require(basis["selected_D_E_action_emitted"] is False, "D_E action overclosed")

    guard = data["guardrails"]
    for key in [
        "claims_rhoE_source_promoted",
        "claims_BN_payload_built",
        "claims_smooth_scalar_basis_phi_m",
        "claims_selected_DE_action_on_basis",
        "claims_gap_error_certificate",
        "claims_honest_replay_ready",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("identity `rho_E` smoke branch has been replaced" in note, "note missing rho_E replacement")
    require("This is not full promotion" in note, "note missing promotion guardrail")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
