"""Audit Higgs accepted-profile import or row-value replacement controller."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsacceptedprofileimport_or_rowvaluereplacement"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ACCEPTANCE = PACKET_DIR / "accepted_profile_import_acceptance_result.packet.json"
REPLACEMENT = PACKET_DIR / "row_value_replacement_controller.packet.json"
PROMOTION = PACKET_DIR / "precision_promotion_after_replacement_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsAcceptedProfileImport_or_RowValueReplacement_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSACCEPTEDPROFILEIMPORT_OR_ROWVALUEREPLACEMENT_BUILT_CONTROLLER_NO_ACCEPTED_VALUES"
NEXT = "MTT_Selected_HiggsExternalProfilePacketFill_or_RowFormulaValues_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    acceptance = load(ACCEPTANCE)
    replacement = load(REPLACEMENT)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(acceptance["structural_schema_tests_pass"] is True, "structural schema tests should pass")
    require(acceptance["precision_acceptance_tests_pass"] is False, "precision acceptance overpassed")
    require(acceptance["accepted_as_profile_convention_import"] is False, "profile import overaccepted")
    require(acceptance["accepted_as_precision_total_width_source"] is False, "precision total source overaccepted")
    require(acceptance["accepted_precision_row_count"] == 0, "precision row count overaccepted")
    require(len(acceptance["rejection_reasons"]) == 3, "rejection reasons mismatch")
    require("necessary but not sufficient" in acceptance["promotion_rule"], "promotion rule missing")

    require(replacement["summary"]["row_count"] == 10, "replacement row count mismatch")
    require(replacement["summary"]["replacement_values_filled"] == 0, "replacement values overfilled")
    require(replacement["summary"]["profile_import_still_preferred_for_bulk_precision"] is True, "profile preference missing")
    require(replacement["summary"]["route_A_formula_fallback_available_for_all_rows"] is True, "route A fallback missing")
    require(replacement["summary"]["route_C_no_knob_source_upgrade_retained_for_all_rows"] is True, "route C guard missing")
    require(all(row["accepted_replacement_value_filled"] is False for row in replacement["rows"]), "row replacement overaccepted")
    require(any(row["channel"] == "H_to_gg" and "QCD" in row["replacement_lane"] for row in replacement["rows"]), "gg replacement lane missing")
    require(any(row["channel"] == "H_to_WW_star" and "profile_import_preferred" in row["replacement_lane"] for row in replacement["rows"]), "WW replacement lane missing")

    require(promotion["accepted_profile_import"] is False, "promotion profile overaccepted")
    require(promotion["accepted_row_replacements"] == 0, "promotion replacements overaccepted")
    require(promotion["structural_rehearsal_valid"] is True, "promotion structural validity missing")
    require(promotion["precision_total_width_closed"] is False, "precision total width overclosed")
    require(promotion["precision_branching_ratios_closed"] is False, "precision branching overclosed")

    require(data["closure_decision"]["profile_acceptance_controller_built"] is True, "candidate controller missing")
    require(data["closure_decision"]["rehearsal_profile_structurally_valid"] is True, "candidate structural validity missing")
    require(data["closure_decision"]["accepted_profile_import"] is False, "candidate profile overaccepted")
    require(data["closure_decision"]["accepted_row_replacements"] == 0, "candidate replacements overaccepted")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("No precision profile import or row replacement is accepted here" in note, "note missing guard")

    for packet in [acceptance, replacement, promotion, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
