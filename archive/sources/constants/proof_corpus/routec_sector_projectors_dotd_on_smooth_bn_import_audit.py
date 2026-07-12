"""Audit selected Route-C sector projectors/dotD on smooth B_N import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_sector_projectors_dotd_on_smooth_bn_import.candidate.json"
CERT = ROOT / "certificates" / "routec_sector_projectors_dotd_on_smooth_bn_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_SectorProjectors_DotD_on_Smooth_BN_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_sector_projectors_dotd_on_smooth_bn.py"

STATUS = "ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_IMPORTED_C1_SOURCE_OPEN"
NEXT = "MTT_Selected_RouteC_C1_Primitive_Response_or_Selected_Source_Proof_v1"


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

    summary = data["sector_dotd_summary"]
    require(summary["family_sector_rank"] == 3, "wrong family sector rank")
    require(summary["higgs_sector_rank"] == 1, "wrong Higgs sector rank")
    require(summary["projectors_idempotent_and_hermitian"] is True, "projectors not exact")
    require(summary["honest_selected_dotD_source_verified"] is False, "dotD source overpromoted")
    require(summary["honest_alpha1_driver_verified"] is False, "alpha1 driver overpromoted")
    require(summary["honest_validator_exit_code"] == 1, "honest validator did not reject")
    require(summary["diagnostic_selected_dotD_source_verified"] is True, "diagnostic dotD absent")
    require(summary["diagnostic_alpha1_driver_verified"] is True, "diagnostic alpha1 absent")
    require(
        summary["diagnostic_claims_physical_selected_source"] is False,
        "diagnostic claims physical source",
    )
    require(summary["diagnostic_validator_exit_code"] == 0, "diagnostic validator failed")
    require(summary["finite_horizontal_response_algebra_only"] is True, "finite-only qualifier missing")

    upstream = data["upstream_sector_projectors_dotd_on_smooth_bn"]
    require(upstream["what_closes_now"]["sector_projectors_on_27_mode_BN_emitted"] is True, "projectors not emitted")
    require(upstream["what_closes_now"]["dotD_alpha1_matrix_in_same_basis_emitted"] is True, "dotD not emitted")
    require(upstream["what_closes_now"]["horizontal_response_equation_passes_diagnostic_validator"] is True, "horizontal equation not validated")
    require(upstream["what_remains_open"]["selected_dotD_source_verified"] is True, "dotD source gap not preserved")
    require(upstream["what_remains_open"]["alpha1_driver_verified"] is True, "alpha1 gap not preserved")
    require(upstream["what_remains_open"]["primitive_C1_overlap_contractions"] is True, "C1 gap not preserved")
    require(upstream["what_remains_open"]["honest_replay_without_lifted_flags"] is True, "honest replay gap not preserved")

    guard = data["guardrails"]
    for key in [
        "claims_selected_dotD_source_verified",
        "claims_alpha1_driver_verified",
        "claims_primitive_C1_overlap_contractions",
        "claims_honest_replay_ready",
        "claims_full_iwasawa_strominger_DE",
        "claims_full_iwasawa_truncation_error",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("sector projectors and `dotD_alpha1` response" in note, "note missing dotD statement")
    require("This is finite response algebra only" in note, "note missing finite-only caveat")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
