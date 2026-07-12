"""Audit the U1/Y selected AH/good-cover promotion and HYM bridge gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_selected_ah_or_goodcover_promotion_hym_certificate.py"
DATA = REPO / "candidate_data" / "selected_u1y_selected_ah_or_goodcover_promotion_hym_certificate.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_selected_ah_or_goodcover_promotion_hym_certificate_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    bridge = data["bridge"]
    source = data["source_selection"]
    chamber = data["gauduchon_status"]
    decision = data["decision"]

    check(
        "status exact",
        data["status"] == "U1Y_SELECTED_AH_GOODCOVER_REFLEXIVE_HULL_AND_CONDITIONAL_HYM_BRIDGE_PROVED_SOURCE_SELECTION_OPEN",
        data["status"],
    )
    check(
        "bridge closed conditionally",
        bridge["rank_one_torsion_free_reflexive_hull_theorem_proved"] is True
        and bridge["conditional_AH_to_full_stability_bridge_proved"] is True
        and bridge["conditional_HYM_bridge_proved"] is True,
        bridge,
    )
    check(
        "selected AH source still open",
        source["AH_representative_constructed"] is True
        and source["AH_selected_by_mtt"] is False
        and source["literal_goodcover_table_selected"] is False,
        source,
    )
    check(
        "Gauduchon and HYM not overpromoted",
        chamber["target_wall_source_certified"] is False
        and chamber["selected_Gauduchon_chamber_source_proved"] is False
        and decision["full_HYM_proved"] is False,
        {"chamber": chamber, "decision": decision},
    )
    check(
        "operator source and lambda still open",
        decision["selected_HYM_operator_source_verified"] is False
        and decision["selected_RouteC_residual_values_emitted"] is False
        and decision["lambda_12_closed"] is False,
        decision,
    )
    check(
        "certificate agrees",
        cert["what_closes"]["rank_one_torsion_free_destabilizer_reduces_to_reflexive_line_hull"] is True
        and cert["full_HYM_proved"] is False
        and cert["lambda_12_closed"] is False,
        cert,
    )
    check(
        "note records next frontier",
        "Selected_U1Y_Selected_AH_GoodCover_Source_or_RouteC_SelectedResidual_v1" in note
        and "lambda_12_closed = false" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
