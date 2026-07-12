"""Audit q79 selected AH/good-cover HYM or Route-C residual promotion import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_q79_selected_ah_goodcover_hym_or_routec_residual_promotion.py"
PACKET = ROOT / "candidate_data" / "q79_selected_ah_goodcover_hym_or_routec_residual_promotion_import.candidate.json"
CERT = ROOT / "certificates" / "q79_selected_ah_goodcover_hym_or_routec_residual_promotion_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Selected_AH_GoodCover_HYM_or_RouteC_Residual_Promotion_Import_v1.md"

STATUS = "Q79_SELECTED_AH_GOODCOVER_HYM_PROMOTION_BRIDGE_IMPORTED_SOURCE_VALUES_OPEN"
NEXT = "Q79_Selected_AH_Source_Selection_or_RouteC_SelectedResidual_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_packet = json.loads(proc.stdout)

    check("packet and cert match", packet == cert, {"packet": PACKET, "cert": CERT})
    check("script agrees", script_packet["status"] == packet["status"], script_packet["status"])
    check("status", packet["status"] == STATUS, packet["status"])
    check("all import checks pass", all(packet["import_checks"].values()), packet["import_checks"])
    check("theorem proved as bridge import", packet["theorem"]["proved"] is True, packet["theorem"])
    check("closure not overclaimed", packet["theorem"]["closure_claimed"] is False, packet["theorem"])

    bridge = packet["promotion_bridge"]
    check(
        "reflexive hull reduction proved",
        bridge["rank_one_torsion_free_reflexive_hull_theorem"]["proved"] is True
        and bridge["rank_one_torsion_free_reflexive_hull_theorem"]["uses_selected_source_data"]
        is False,
        bridge["rank_one_torsion_free_reflexive_hull_theorem"],
    )
    check(
        "stability bridge conditional",
        bridge["reduced_AH_to_full_stability_implication"]["proved_conditionally"] is True
        and bridge["promotion_summary"]["conditional_reduced_AH_to_full_stability_bridge_proved"]
        is True
        and bridge["promotion_summary"]["selected_AH_or_goodcover_source_supplied"] is False,
        bridge["promotion_summary"],
    )
    check(
        "HYM bridge conditional no values",
        bridge["HYM_bridge"]["proved_conditionally"] is True
        and bridge["HYM_bridge"]["operator_source_not_emitted"] is True
        and bridge["promotion_summary"]["selected_HYM_connection_values_supplied"] is False,
        bridge["HYM_bridge"],
    )
    check(
        "AH Yoneda law verified not selected",
        packet["AH_yoneda_status"]["closed_by_this_attempt"][
            "AH_factor_product_law_matches_yoneda_degree_addition"
        ]
        is True
        and packet["AH_yoneda_status"]["appell_humbert_selection_state"]["selected_by_mtt"]
        is False,
        packet["AH_yoneda_status"]["appell_humbert_selection_state"],
    )
    check(
        "Route-C operator still blocked",
        packet["routec_or_operator_status"]["hym_operator_attempt"][
            "selected_hym_operator_source_verified"
        ]
        is False
        and packet["routec_or_operator_status"]["hym_operator_attempt"][
            "route_c_honest_operator_pipeline_pass"
        ]
        is False,
        packet["routec_or_operator_status"]["hym_operator_attempt"],
    )
    check(
        "remaining open retains source and values",
        packet["what_remains_open"]["selected_AH_representative_or_literal_goodcover_Cech_source"]
        is True
        and packet["what_remains_open"]["selected_RouteC_residual_values"] is True
        and packet["what_remains_open"]["same_source_DE_Riesz_Green_dotD"] is True,
        packet["what_remains_open"],
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])
    check(
        "next artifact named",
        packet["verdict"]["promotion_bridge_imported"] is True
        and packet["verdict"]["selected_source_or_values_closed"] is False
        and packet["verdict"]["best_next_artifact"] == NEXT,
        packet["verdict"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "promotion bridge",
        "conditional Li-Yau/Gauduchon HYM bridge",
        "does **not** emit selected HYM connection coefficients",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 selected AH/good-cover HYM or Route-C residual promotion import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
