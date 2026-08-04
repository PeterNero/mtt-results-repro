"""Audit selected Route-C D_E action on smooth B_N import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_de_action_on_smooth_bn_import.candidate.json"
CERT = ROOT / "certificates" / "routec_de_action_on_smooth_bn_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_DE_Action_on_Smooth_BN_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_de_action_on_smooth_bn.py"

STATUS = "ROUTEC_DE_ACTION_ON_SMOOTH_BN_IMPORTED_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1"


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

    summary = data["de_action_summary"]
    require(summary["domain_dimension"] == 27, "wrong domain dimension")
    require(summary["family_kernel_dimension"] == 3, "wrong family kernel dimension")
    require(summary["higgs_kernel_dimension"] == 1, "wrong Higgs kernel dimension")
    require(summary["honest_selected_source_verified"] is False, "honest source overpromoted")
    require(summary["honest_validator_exit_code"] == 1, "honest validator did not reject")
    require(summary["diagnostic_selected_source_verified"] is True, "diagnostic source lift absent")
    require(
        summary["diagnostic_claims_physical_selected_source"] is False,
        "diagnostic lift claims physical source",
    )
    require(summary["diagnostic_validator_exit_code"] == 0, "diagnostic validator failed")
    require(summary["model_active_DE_only"] is True, "model-active qualifier missing")

    upstream = data["upstream_de_action_on_smooth_bn"]
    require(upstream["what_closes_now"]["D_E_matrix_on_27_mode_BN_emitted"] is True, "D_E not emitted")
    require(upstream["what_closes_now"]["stiffness_equals_DstarD"] is True, "D*D not emitted")
    require(
        upstream["what_remains_open"]["selected_D_E_source_promotion"] is True,
        "source-promotion gap not preserved",
    )
    require(
        upstream["what_remains_open"]["full_iwasawa_strominger_DE_action_not_only_model_active"]
        is True,
        "full D_E gap not preserved",
    )
    require(upstream["what_remains_open"]["sector_projectors"] is True, "sector gap not preserved")
    require(upstream["what_remains_open"]["dotD_alpha1_in_same_basis"] is True, "dotD gap not preserved")

    guard = data["guardrails"]
    for key in [
        "claims_selected_DE_source_promotion",
        "claims_full_iwasawa_strominger_DE_action",
        "claims_sector_projectors_constructed",
        "claims_dotD_alpha1_in_same_basis",
        "claims_C1_response",
        "claims_honest_replay_ready",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("finite model-active `D_E` action" in note, "note missing D_E statement")
    require("This is not selected-source closure" in note, "note missing source caveat")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
