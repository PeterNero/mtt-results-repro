"""Audit Step45 alpha1-to-Rtheta row execution attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step45_alpha1rthetarow_execution_attempt_or_coefficientmapfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ANCHOR_IMPORT = PACKET_DIR / "step45_alpha1_anchor_import_into_rtheta_gate.packet.json"
ROW_ATTEMPT = PACKET_DIR / "step45_alpha1_to_rtheta_row_execution_attempt.packet.json"
FRONTIER = PACKET_DIR / "step45_selected_coefficient_map_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step45_Alpha1RThetaRowExecutionAttempt_or_CoefficientMapFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP45_ALPHA1_RTHETA_ROW_EXECUTION_ATTEMPT_BUILT_ANCHOR_BLOCKER_RETIRED_COEFFICIENT_MAP_OPEN"
NEXT = "MTT_Selected_Alpha1ToRThetaCoefficientMap_or_InternalScalarRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    anchor_import = load(ANCHOR_IMPORT)
    row_attempt = load(ROW_ATTEMPT)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "gate contraction theorem not proved")

    for packet in [data, anchor_import, row_attempt, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    require(
        anchor_import["source_anchor_imported_into_rtheta_gate"] is True,
        "alpha1 anchor not imported",
    )
    require(
        anchor_import["stale_no_universal_anchor_blocker_retired"] is True,
        "stale no-anchor blocker not retired",
    )
    require(anchor_import["selected_source_anchor_count_after_import"] == 1, "anchor count mismatch")
    require(anchor_import["selected_value_anchor_count"] == 0, "value anchor overselected")
    require(anchor_import["effective_fitted_parameter_count"] == 0, "fitted parameter count mismatch")

    require(row_attempt["rtheta_domain_ready"] is True, "Rtheta domain not ready")
    require(row_attempt["alpha1_source_anchor_available"] is True, "alpha1 unavailable")
    require(row_attempt["coefficient_functional_skeleton_closed"] is True, "functional skeleton open")
    require(row_attempt["charged_functional_row_count"] == 9, "charged row count mismatch")
    require(row_attempt["coefficient_map_closed"] is False, "coefficient map overclosed")
    require(row_attempt["accepted_internal_Rtheta_row_count"] == 0, "internal rows overaccepted")
    require(row_attempt["lambda_H_accepted_as_internal_Rtheta_row"] is False, "lambda_H overaccepted")
    require(len(row_attempt["admitted_replay_rows_checked_as_postchecks"]) == 9, "postcheck row count mismatch")
    for row in row_attempt["admitted_replay_rows_checked_as_postchecks"]:
        require(row["accepted_as_internal_Rtheta_value"] is False, f"postcheck promoted: {row['row_id']}")

    closed_now = frontier["closed_now"]
    require(closed_now["alpha1_source_anchor_imported_into_Rtheta_gate"] is True, "frontier anchor missing")
    require(closed_now["stale_no_anchor_blocker_retired"] is True, "frontier stale blocker missing")
    require(closed_now["Rtheta_domain_and_coefficient_functional_available"] is True, "frontier domain missing")
    require(closed_now["admitted_replay_rows_demoted_to_postchecks"] is True, "postcheck boundary missing")
    require(frontier["still_open"]["selected_alpha1_to_Rtheta_coefficient_map"] is True, "coefficient map not open")
    require(frontier["next_required_artifact"] == NEXT, "frontier next mismatch")

    decision = data["closure_decision"]
    require(decision["alpha1_source_anchor_imported_into_Rtheta_gate"] is True, "decision anchor missing")
    require(decision["stale_no_universal_anchor_blocker_retired"] is True, "decision stale blocker missing")
    require(decision["Rtheta_domain_and_coefficient_functional_ready"] is True, "decision domain missing")
    for key in [
        "selected_alpha1_to_Rtheta_coefficient_map_closed",
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "coefficient rows overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "stale no-anchor blocker retired",
        "accepted internal Rtheta coefficient rows       : 0",
        NEXT,
        "postchecks only",
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
