"""Audit the selected AH/Cech source-layer promotion and residual gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json"
CERT = ROOT / "certificates" / "selected_routec_ah_source_selection_or_routec_selected_residual_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_RouteC_AH_Source_Selection_or_RouteC_SelectedResidual_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_ROUTEC_ORDERED_AH_SOURCE_LAYER_PROMOTED_GAUDUCHON_OR_RESIDUAL_SOURCE_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    require(data["selected_AH_goodcover_stability_layer"]["proved"] is True, "selected AH/Cech stability layer must promote")
    require(
        data["selected_AH_goodcover_stability_layer"]["scope"]
        == "ordered Chern/H1/ordinary-curvature/stability layer only",
        "scope must stay layer-limited",
    )
    require(data["selected_AH_goodcover_stability_layer"]["selected_ordered_source"] is True, "ordered source not selected")
    require(data["selected_AH_goodcover_stability_layer"]["selected_cohomology_h1_ext"] is True, "cohomology not selected")
    require(data["selected_AH_goodcover_stability_layer"]["ordered_L_vector"] == [1, -2, 0], "wrong L vector")
    require(data["selected_AH_goodcover_stability_layer"]["h1_L2"] == 8, "wrong h1")
    require(
        data["selected_AH_goodcover_stability_layer"]["operator_layer_pic0_reopens"] is True,
        "operator-layer Pic0 must reopen",
    )
    require(data["stability_consequence"]["stable_in_selected_ordered_AH_layer"] is True, "stability layer not closed")
    require(
        data["stability_consequence"]["stable_as_full_selected_Gauduchon_bundle"] is False,
        "must not promote full Gauduchon stability",
    )
    require(
        data["gauduchon_or_routec_gate"]["selected_gauduchon_target_wall"] is False,
        "Gauduchon wall should remain open",
    )
    require(
        data["gauduchon_or_routec_gate"]["selected_routec_residual_values"] is False,
        "Route-C residual values should remain unselected",
    )
    require(data["gauduchon_or_routec_gate"]["routec_residual_zero_smoke_support"] is True, "expected zero smoke support")
    require(data["HYM_status"]["HYM_existence_selected_now"] is False, "must not claim selected HYM")
    require(
        data["what_closes_now"]["selected_ordered_AH_goodcover_source_for_stability_layer"] is True,
        "main close flag missing",
    )
    require(data["what_remains_open"]["selected_Gauduchon_chamber_source"] is True, "Gauduchon open flag missing")
    require(data["what_remains_open"]["selected_RouteC_residual_values"] is True, "Route-C open flag missing")
    require(
        data["next_required_artifact"] == "MTT_Selected_RouteC_Gauduchon_Chamber_or_SelectedResidual_Source_v1",
        "wrong next artifact",
    )

    require(cert["selected_AH_goodcover_stability_layer_proved"] is True, "certificate layer close missing")
    require(cert["selected_gauduchon_or_routec_residual_source_open"] is True, "certificate open gate missing")
    require("support-only residual smoke is" in proof.lower(), "proof must state smoke guardrail")
    require("r1:r2=sqrt(2):1" in proof, "proof must name wall radius ratio")
    require("ordered AH/Cech stability layer is promoted" in proof, "proof must name promoted layer")

    print("PASS selected Route-C AH source selection / residual gate audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
