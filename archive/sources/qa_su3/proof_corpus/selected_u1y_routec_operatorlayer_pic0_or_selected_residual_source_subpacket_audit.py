"""Audit the U1/Y Route-C operator-layer Pic0 or selected-residual split gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_operatorlayer_pic0_or_selected_residual_source_subpacket.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_operatorlayer_pic0_or_selected_residual_source_subpacket.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_operatorlayer_pic0_or_selected_residual_source_subpacket_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_OperatorLayerPic0_or_SelectedResidual_Source_Subpacket_v1.md"

STATUS = "U1Y_ROUTEC_OPERATORLAYER_PIC0_OR_SELECTED_RESIDUAL_SPLIT_BUILT_PRIMARY_PHIFIN"
NEXT = "Selected_U1Y_RouteC_FiniteEmissionMorphism_PhiFin_Subpacket_v1"


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
    pic0 = data["pic0_lane"]
    residual = data["residual_lane"]

    check("status exact", data["status"] == STATUS and cert["status"] == STATUS, data["status"])
    check(
        "pic0 demoted to side condition",
        pic0["can_close_bridge_alone"] is False
        and pic0["status"] == "NECESSARY_BUT_NOT_SUFFICIENT_CURRENT_SOURCE_NOGO"
        and pic0["support"]["flat_pic0_preserves_c1"] is True
        and pic0["support"]["pic0_invariance_proved"]["curvature_and_bianchi_terms_can_select_neutral_character"]
        is False,
        pic0,
    )
    check(
        "residual lane primary phifin",
        residual["status"] == "PRIMARY_LIVE_REDUCED_TO_FINITE_EMISSION_MORPHISM"
        and residual["can_close_bridge_with_pic0_side_condition"] is True
        and residual["support"]["fixed_topological_sector_named"] is True
        and residual["support"]["mtt_strominger_selection_available"] is True
        and residual["blockers"]["finite_emission_morphism"] is True,
        residual,
    )
    check(
        "route decision exact",
        data["route_decision"]["primary_next_lane"] == "selected_residual_hym_strominger_source"
        and data["route_decision"]["primary_next_artifact"] == NEXT
        and data["next_required_artifact"] == NEXT
        and cert["primary_next_artifact"] == NEXT,
        data["route_decision"],
    )
    check(
        "split does not close bridge",
        data["source_split_result"]["pic0_closed"] is False
        and data["source_split_result"]["selected_residual_closed"] is False
        and data["source_split_result"]["bridge_closed"] is False
        and cert["current_source_nogo"] is True,
        data["source_split_result"],
    )
    check(
        "phifin contract has validator acceptance",
        "selected_source_verified becomes a theorem-derived field, not a lifted flag"
        in residual["accepts_if"]
        and "D_E, dotD, Riesz/Green, and residual validators pass honestly" in residual["accepts_if"],
        residual["accepts_if"],
    )
    check(
        "what closes records hidden selector rejection",
        data["what_closes_now"]["pic0_only_route_demoted_to_side_condition"] is True
        and data["what_closes_now"]["finite_emission_morphism_named_as_next_object"] is True
        and data["what_closes_now"]["hidden_pic0_selector_rejected"] is True,
        data["what_closes_now"],
    )
    check(
        "guardrails hold",
        data["guardrails"]["claims_pic0_closed"] is False
        and data["guardrails"]["claims_selected_residual_closed"] is False
        and data["guardrails"]["claims_lambda12"] is False
        and cert["lambda_12_closed"] is False
        and cert["target_fitting_used"] is False,
        data["guardrails"],
    )
    check(
        "note records phifin next",
        "Phi_fin" in note and NEXT in note and "necessary side condition" in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
