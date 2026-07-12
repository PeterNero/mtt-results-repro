"""Audit selected Route-C/Strominger Galerkin first-run import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_strominger_galerkin_first_run_import.candidate.json"
CERT = ROOT / "certificates" / "routec_strominger_galerkin_first_run_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_Strominger_Galerkin_FirstRun_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_strominger_galerkin_first_run.py"

STATUS = "ROUTEC_STROMINGER_GALERKIN_FIRST_RUN_IMPORTED_SELECTOR_OPEN"
NEXT = "MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1"


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

    upstream = data["upstream_first_run"]
    require(all(upstream["manifest_filled"].values()), "manifest not filled")
    require(upstream["validation"]["honest_root_all_pass"] is False, "honest root overpromoted")
    require(upstream["validation"]["formal_lift_lower_validators_all_pass"] is True, "formal lift lower validators failed")
    require(upstream["validation"]["formal_lift_promotion_passes"] is True, "formal lift promotion diagnostic failed")
    require(upstream["interpretation"]["proof_promotion_allowed"] is False, "proof promotion accidentally allowed")
    require(upstream["root_payload"]["selected_source_verified"] is False, "root source overpromoted")
    require(upstream["formal_lift_payload"]["selected_source_verified"] is True, "formal lift diagnostic missing")
    require(upstream["target_fitting_used"] is False, "target fitting used")

    guard = data["guardrails"]
    for key in [
        "claims_selected_source_theorem",
        "claims_quotient_valid_selected_basis_BN",
        "claims_honest_root_manifest_passes",
        "promotes_formal_lift_to_proof",
        "claims_primitive_C1_contractions",
        "claims_spectral_projector_error_bounds",
        "claims_proof_usable_de_response_packet",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_masses_mixings_or_benchmark_matrices",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("formal-lift diagnostic passes" in note, "note missing diagnostic pass")
    require("It is not proof promotion" in note, "note missing proof-promotion guardrail")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
