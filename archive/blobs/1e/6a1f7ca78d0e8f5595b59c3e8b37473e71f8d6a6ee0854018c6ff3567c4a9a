"""Audit the same-source symmetry-breaking source artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "same_source_symmetry_breaking_source.candidate.json"
CERT = REPO / "certificates" / "same_source_symmetry_breaking_source_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_SameSource_SymmetryBreaking_Source_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    mode = data["superset_mode"]
    primary = mode["primary_superset_path"]
    repairs = mode["repair_paths"]
    contract = data["selected_template_contract"]

    checks = [
        check("status", data["status"] == "MTT_SAME_SOURCE_SYMMETRY_BREAKING_SOURCE_REDUCED_TO_ORIENTATION_CARRYING_DE_DOTD_PACKET", data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check("superset mode", mode["classification"] == "SUPERSET_CONVERGENCE_WITH_REPAIR_TRIAGE", mode),
        check("straight path blocked", mode["straight_path"]["classification"] == "STRAIGHT_PATH_BLOCKED", mode["straight_path"]),
        check("primary route orientation dedotd", primary["classification"] == "SUPERSET_CONVERGENCE_PRIMARY" and primary["template"].endswith("selected_qa_su3_orientation_carrying_de_dotd_source.template.json"), primary),
        check("primary route closed scaffolds", all(primary["closed"].values()), primary["closed"]),
        check("primary route still open honestly", primary["open"]["selected_orientation_carrying_source"] is True and primary["open"]["actual_selected_D_E_action"] is True, primary["open"]),
        check("gauduchon repair blocked", repairs["gauduchon_wall"]["classification"] == "SUPERSET_REPAIR_LIVE_BUT_BLOCKED" and repairs["gauduchon_wall"]["equal_radius_current_source_rejected"] is True, repairs["gauduchon_wall"]),
        check("two block repair kept", repairs["ordered_integral_cech_or_appell_humbert"]["two_block_shadow_closed"] is True and repairs["ordered_integral_cech_or_appell_humbert"]["selected_s3_deck_limit"]["current_selected_s3_supplies_second_active_block"] is False, repairs["ordered_integral_cech_or_appell_humbert"]),
        check("pic0 insufficient", repairs["pic0_rule_only"]["classification"] == "NECESSARY_BUT_NOT_SUFFICIENT", repairs["pic0_rule_only"]),
        check("no target fitting", data["target_fitting_used"] is False and mode["diagnostic_backfit_only"]["used"] is False, mode["diagnostic_backfit_only"]),
        check("template fields locked", "source_certificate" in contract["source_origin_fields"] and "selected_torsion_label_m" in contract["branch_selection_fields"] and "selected_dotD_alpha1" in contract["operator_data_fields"], contract),
        check("promotion forbids lifted flags", any("lifted" in item for item in contract["forbidden_shortcuts"]), contract["forbidden_shortcuts"]),
        check("next artifact", cert["primary_next_artifact"] == "MTT_Selected_Orientation_Carrying_DE_DotD_Source_v1", cert),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["selected_orientation_carrying_de_dotd_source"] is True, cert),
        check("note records route triage", "Primary Route" in note and "Repair Routes" in note and "Pic0 rule alone" in note, NOTE),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT same-source symmetry-breaking source audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
