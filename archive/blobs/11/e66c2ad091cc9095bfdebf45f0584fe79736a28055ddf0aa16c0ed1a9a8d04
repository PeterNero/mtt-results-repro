"""Audit the Pic0 invariance or gerbe-twisted D_E source artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_pic0_invariance_or_gerbe_twisted_de_source_certificate.json"
DATA = REPO / "candidate_data" / "selected_pic0_invariance_or_gerbe_twisted_de_source.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Pic0_Invariance_or_Gerbe_Twisted_DE_Source_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_pic0_invariance_or_gerbe_twisted_de_source.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    imported = data["imported_results"]
    contract = data["selected_s3_class_packet_contract"]
    sources_present = all(row["present"] for row in data["source_status"].values())
    checks = [
        check("status", cert["status"] == "MTT_SELECTED_PIC0_INVARIANCE_OR_GERBE_TWISTED_DE_SOURCE_BUILT_CLASS_RESTRICTION_GATE_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("previous frontier matches", imported["previous_frontier"]["next_required_artifact"] == "MTT_Selected_Pic0_Invariance_or_Gerbe_Twisted_DE_Source_v1", imported["previous_frontier"]),
        check("direct Pic0 retired", gates["direct_pic0_invariance_proved"] is False and gates["direct_pic0_invariance_retired_for_now"] is True, data["route_decision"]["direct_pic0_invariance"]),
        check("good cover knob removed", gates["good_cover_knob_removed"] is True and data["cover_knob_reduction"]["good_cover_is_physical_knob"] is False, data["cover_knob_reduction"]),
        check("cover reduction imported", imported["deligne_cover_gauge_reduction"]["what_this_closes"]["good_cover_is_execution_scaffold_not_physical_knob"] is True, imported["deligne_cover_gauge_reduction"]),
        check("q79 gerbe fixed", imported["fixed_gerbe_representative"]["q79_orientation"] == "F" and imported["fixed_gerbe_representative"]["q79_torsion_label_m"] == 1, imported["fixed_gerbe_representative"]),
        check("deck cech imported", gates["deck_cech_f3_squared_imported"] is True and imported["deck_cech_lift"]["deck_quotient_target"] == "F_3^2", imported["deck_cech_lift"]),
        check("flat gerbe imported", gates["flat_gerbe_conditional_promotion_imported"] is True and imported["flat_gerbe_promotion"]["curvature_H_zero_for_flat_representative"] is True, imported["flat_gerbe_promotion"]),
        check("finite S3 CP imported", gates["finite_s3_cp_cancellation_imported"] is True and imported["finite_s3_cp_cancellation"]["finite_S3_CP_cancellation_closed"] is True, imported["finite_s3_cp_cancellation"]),
        check("visible GS imported", gates["visible_gs_curvature_imported"] is True and imported["visible_gs_curvature"]["visible_green_schwarz_curvature_verified"] is True, imported["visible_gs_curvature"]),
        check("smooth source still open", gates["selected_smooth_s3_source_constructed"] is False and imported["smooth_s3_lift_attempt"]["selected_smooth_S3_source_constructed"] is False, imported["smooth_s3_lift_attempt"]),
        check("FW/projector still open", gates["freed_witten_projector_retention_closed"] is False and imported["finite_s3_cp_cancellation"]["selected_projector_retention_verified"] is False, imported["finite_s3_cp_cancellation"]),
        check("operator still open", gates["selected_DE_dotD_Riesz_Green_constructed"] is False and imported["hym_operator_attempt"]["selected_hym_operator_source_verified"] is False, imported["hym_operator_attempt"]),
        check("contract built", contract["schema"] == "SelectedS3ClassRestrictionProjectorRetention.v1" and len(contract["must_supply"]) == 5, contract),
        check("no closure claimed", gates["sm_parity_closure_claimed"] is False and gates["no_knob_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_S3_Class_Restriction_Projector_Retention_v1", data["next_required_artifact"]),
        check("note records route decision", "PRIMARY_EXECUTION_ROUTE" in note and "good cover is not a new physical knob" in note, NOTE),
    ]
    print("\nMTT selected Pic0 invariance or gerbe-twisted D_E source audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
