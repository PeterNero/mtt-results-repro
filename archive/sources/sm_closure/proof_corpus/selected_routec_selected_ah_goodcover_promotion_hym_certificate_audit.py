"""Audit the selected AH/good-cover promotion and HYM certificate attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_routec_selected_ah_goodcover_promotion_hym_certificate.py"
DATA = REPO / "candidate_data" / "selected_routec_selected_ah_goodcover_promotion_hym_certificate.candidate.json"
CERT = REPO / "certificates" / "selected_routec_selected_ah_goodcover_promotion_hym_certificate_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_REFLEXIVE_HULL_AND_CONDITIONAL_HYM_BRIDGE_PROVED_AH_SELECTION_OPEN"
NEXT = "MTT_Selected_RouteC_AH_Source_Selection_or_RouteC_SelectedResidual_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> bool:
    print(f"{'PASS' if condition else 'FAIL'}: {label} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    hull = data["rank_one_torsion_free_reflexive_hull_theorem"]
    implication = data["reduced_AH_to_full_stability_implication"]
    hym = data["HYM_bridge"]
    source = data["selected_AH_goodcover_status"]
    closes = data["what_closes_now"]
    remaining = data["what_remains_open"]

    checks = [
        check("script exits 0", proc.returncode == 0, proc.stdout[:500]),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("no full closure claimed", data["closure_claimed"] is False and cert["full_HYM_proved"] is False, cert),
        check("no target fitting", data["target_fitting_used"] is False, data["superset_strategy"]),
        check(
            "reflexive hull theorem proved",
            hull["proved"] is True
            and "same selected slope" in hull["statement"]
            and "line bundle" in hull["statement"],
            hull,
        ),
        check(
            "stability implication conditional",
            implication["proved_conditionally"] is True
            and implication["imports_reduced_AH_stability"] is True
            and implication["imports_reflexive_hull_reduction"] is True
            and "selected AH representative" in implication["condition"],
            implication,
        ),
        check(
            "HYM bridge conditional only",
            hym["li_yau_gauduchon_support_in_corpus"] is True
            and hym["proved_conditionally"] is True
            and hym["operator_source_not_emitted"] is True,
            hym,
        ),
        check(
            "source selection still open",
            source["AH_degree_product_law_verified"] is True
            and source["AH_selected_by_mtt"] is False
            and source["pullback_cech_validator_passes"] is True
            and source["pullback_cech_role"] == "UNSELECTED_FIXTURE",
            source,
        ),
        check(
            "closes only legal pieces",
            closes["rank_one_torsion_free_destabilizer_reduces_to_reflexive_line_hull"] is True
            and closes["remaining_blocker_identified_as_source_selection_not_destabilizer_enumeration"] is True,
            closes,
        ),
        check(
            "remaining source gates explicit",
            remaining["selected_AH_representative_or_literal_goodcover_Cech_source"] is True
            and remaining["selected_HYM_connection_values"] is True
            and remaining["same_source_D_E_Riesz_Green_dotD"] is True,
            remaining,
        ),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records theorem and nonclosure",
            "rank-one torsion-free destabilizer reduction is now closed" in note
            and "Full HYM is still not claimed" in note
            and NEXT in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C selected AH/good-cover HYM certificate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
