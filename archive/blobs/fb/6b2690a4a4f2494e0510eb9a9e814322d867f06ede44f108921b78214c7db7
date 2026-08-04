"""Audit the U1/Y selected AH/good-cover source or Route-C residual gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_ah_goodcover_source_or_routec_selected_residual.py"
DATA = REPO / "candidate_data" / "selected_u1y_ah_goodcover_source_or_routec_selected_residual.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_ah_goodcover_source_or_routec_selected_residual_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_Selected_AH_GoodCover_Source_or_RouteC_SelectedResidual_v1.md"


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
    source = data["source_layer"]
    stability = data["ah_goodcover_stability_layer"]
    residual = data["residual_or_chamber"]
    decision = data["decision"]

    check(
        "status exact",
        data["status"] == "U1Y_ORDERED_AH_GOODCOVER_SOURCE_LAYER_PROMOTED_GAUDUCHON_OR_RESIDUAL_SOURCE_OPEN",
        data["status"],
    )
    check(
        "terminal source selected under principle",
        source["selected_source_label"] == "g3 / L3-K2"
        and source["selected_L"] == [1, -2, 0]
        and source["selected_L2"] == [2, -4, 0]
        and source["terminal_lane_unique_visible_c2"] is True
        and source["terminal_lane_unique_zero_central"] is True,
        source,
    )
    check(
        "ordered layer and Ext close",
        source["ordered_layer_pic0_quotiented"] is True
        and source["h1"] == 8
        and source["nonzero_ext_class"] is True
        and stability["stable_in_selected_ordered_AH_layer"] is True,
        {"source": source, "stability": stability},
    )
    check(
        "not overpromoted to full HYM",
        stability["stable_as_full_selected_Gauduchon_bundle"] is False
        and decision["selected_HYM_or_Strominger_existence_proved"] is False
        and decision["lambda_12_closed"] is False,
        decision,
    )
    check(
        "residual and chamber remain open",
        residual["selected_gauduchon_target_wall"] is False
        and residual["routec_selected_source_verified"] is False
        and residual["selected_routec_residual_values"] is False,
        residual,
    )
    check(
        "certificate agrees",
        cert["selected_AH_goodcover_stability_layer_proved"] is True
        and cert["full_selected_Gauduchon_stability_proved"] is False
        and cert["selected_RouteC_residual_values_emitted"] is False,
        cert,
    )
    check(
        "note records next frontier",
        "Selected_U1Y_Gauduchon_Chamber_or_SelectedResidual_Source_v1" in note
        and "lambda_12_closed = false" in note
        and "principle_unconditional_in_mtt_axioms = false" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
