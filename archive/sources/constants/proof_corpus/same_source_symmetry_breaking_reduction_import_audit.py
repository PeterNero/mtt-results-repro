"""Audit same-source symmetry-breaking reduction import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "same_source_symmetry_breaking_reduction_import.candidate.json"
CERT = ROOT / "certificates" / "same_source_symmetry_breaking_reduction_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "SameSourceSymmetryBreaking_Reduction_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_same_source_symmetry_breaking_reduction.py"

STATUS = "SAME_SOURCE_SYMMETRY_BREAKING_IMPORTED_ORIENTATION_DE_DOTD_OPEN"
NEXT = "MTT_Selected_Orientation_Carrying_DE_DotD_Source_v1"


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

    upstream = data["upstream_same_source_symmetry_breaking"]
    primary = upstream["superset_mode"]["primary_superset_path"]
    require(primary["status"] == "PRIMARY_LIVE_ROUTE_SOURCE_OPEN", "primary route not open")
    require(primary["template"] == "certificates\\selected_qa_su3_orientation_carrying_de_dotd_source.template.json", "wrong template")
    for key in [
        "conjugate_pair_reduced_to_q79_q369",
        "finite_branch_data_reaches_validator_layer",
        "finite_dotD_response_validator_ready",
        "dotd_response_validator_formulated",
    ]:
        require(primary["closed"][key] is True, f"primary closed flag missing: {key}")
    for key in [
        "selected_orientation_carrying_source",
        "unique_m1_vs_m2_selection",
        "actual_selected_D_E_action",
        "actual_selected_dotD_alpha1_operator",
        "same_branch_derivative_verified",
        "pic0_selected_or_quotiented",
    ]:
        require(primary["open"][key] is True, f"primary open flag missing: {key}")

    repairs = upstream["superset_mode"]["repair_paths"]
    require(repairs["gauduchon_wall"]["equal_radius_current_source_rejected"] is True, "Gauduchon current source not rejected")
    require(repairs["pic0_rule_only"]["classification"] == "NECESSARY_BUT_NOT_SUFFICIENT", "Pic0-only misclassified")
    require(
        repairs["ordered_integral_cech_or_appell_humbert"]["selected_s3_deck_limit"]["selected_s3_active_image_rank_over_F3"] == 2,
        "S3 deck rank mismatch",
    )
    require(upstream["superset_mode"]["straight_path"]["classification"] == "STRAIGHT_PATH_BLOCKED", "straight path not blocked")

    closes = data["what_closes_now"]
    for key in [
        "symmetry_breaking_shortcuts_triaged",
        "straight_topology_h1_qutrit_curvature_path_blocked",
        "orientation_carrying_DE_dotD_route_selected_as_primary",
        "q79_q369_conjugate_pair_formulated",
        "finite_DE_dotD_validator_layer_reachable",
        "gauduchon_wall_repair_kept_but_current_equal_radius_source_rejected",
        "ordered_integral_two_block_repair_kept_as_source_certificate_gap",
        "pic0_only_marked_necessary_but_insufficient",
        "operator_payload_template_contract_locked",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_selected_orientation_source",
        "claims_unique_m1_vs_m2_selection",
        "claims_selected_pic0_resolution",
        "claims_selected_DE_dotD_Riesz_Green",
        "claims_primitive_C1_contractions",
        "claims_A_selected_or_b_selected",
        "claims_Yukawa_or_full_SM_closure",
        "uses_observed_cp_sign",
        "uses_benchmark_flavor_matrices",
        "uses_lifted_selected_flags_as_proof",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("orientation-carrying" in note, "note missing orientation route")
    require("Pic0-only is necessary but not sufficient" in note, "note missing Pic0 guardrail")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
