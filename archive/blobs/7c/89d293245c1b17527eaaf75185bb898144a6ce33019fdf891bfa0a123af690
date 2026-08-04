"""Audit source-origin/alpha1-driver reduction import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "source_origin_alpha1_driver_reduction_import.candidate.json"
CERT = ROOT / "certificates" / "source_origin_alpha1_driver_reduction_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "SourceOrigin_Alpha1Driver_Reduction_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_source_origin_alpha1_driver_reduction.py"

STATUS = "SOURCE_ORIGIN_ALPHA1_DRIVER_IMPORTED_PHIFIN_PAYLOAD_OPEN"
NEXT = "MTT_Selected_PhiFin_Alpha1_Payload_v1"


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

    upstream = data["upstream_source_origin_alpha1_driver"]
    source = upstream["source_origin_audit"]
    alpha = upstream["alpha1_driver_audit"]
    contract = upstream["unified_payload_contract"]

    for key in [
        "fixed_topological_sector_named",
        "mtt_strominger_selection_available",
        "s3_projective_gerbe_support_promoted",
        "same_source_support_converges",
        "visible_chern_weil_contract_reduced",
    ]:
        require(source["support_closed"][key] is True, f"support flag missing: {key}")
    require(source["ordinary_nonidentity_rhoe_retired"] is True, "ordinary rhoE not retired")
    require(source["projective_gerbe_rhoe_live"] is True, "projective gerbe rhoE not live")
    require(all(flag is False for flag in source["selected_flags"].values()), "source flags overfilled")
    require(all(flag is False for flag in source["phifin_selected_payload_flags"].values()), "payload flags overfilled")
    require(all(flag is False for flag in alpha["selected_values"].values()), "alpha selected values overfilled")

    require(alpha["operator_level_support"]["selected_driver_alpha1_row"] is True, "alpha1 row support missing")
    require(alpha["operator_level_support"]["single_driver_not_algebraically_fatal"] is True, "single driver criterion missing")
    require(contract["name"] == "SelectedPhiFinAlpha1Payload", "wrong payload contract")
    require("selected dotD_alpha1 as the same-branch derivative of selected D_E" in contract["must_emit"], "missing same-branch derivative emission")

    guard = data["guardrails"]
    for key in [
        "claims_selected_PhiFin_alpha1_payload",
        "claims_selected_nonidentity_rhoE_values",
        "claims_source_origin_flags",
        "claims_same_branch_dotD_derivative",
        "claims_finite_C1_source_vector_or_Hessian_blocks",
        "claims_deltaTheta_C1_or_sector_dotD",
        "claims_zero_mode_bases_or_primitive_contractions",
        "claims_A_selected_or_b_selected",
        "claims_Yukawa_or_full_SM_closure",
        "uses_observed_masses_or_CKM_phase",
        "uses_benchmark_entries",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("SelectedPhiFinAlpha1Payload" in note, "note missing payload")
    require("support side is not the active" in note, "note missing support reduction")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
