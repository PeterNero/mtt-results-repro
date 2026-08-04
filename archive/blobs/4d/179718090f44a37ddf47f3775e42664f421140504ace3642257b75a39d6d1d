"""Audit the equal-radius Gauduchon HYM bridge repair."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_routec_equalradius_gauduchon_hym_bridge.candidate.json"
CERT = ROOT / "certificates" / "selected_routec_equalradius_gauduchon_hym_bridge_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_RouteC_EqualRadius_Gauduchon_HYM_Bridge_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_ROUTEC_EQUALRADIUS_GAUDUCHON_HYM_EXISTENCE_BRIDGE_CLOSED_OPERATOR_VALUES_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    require(data["key_repair"]["equal_radius_does_not_select_branch"] is True, "must preserve radius no-go")
    require(data["key_repair"]["branch_selected_elsewhere"] is True, "branch must be selected elsewhere")
    require(data["selected_equal_radius_gauduchon_metric"]["selected"] is True, "equal-radius metric not selected")
    require(data["selected_equal_radius_gauduchon_metric"]["p"] == [1, 1, 1], "wrong equal-radius p")
    require(
        data["selected_equal_radius_gauduchon_metric"]["matches_target_wall"] is False,
        "equal radius must not be target wall",
    )
    require(data["equal_radius_stability_enumeration"]["mu_L_at_equal_radius"] < 0, "L must have negative slope")
    require(data["equal_radius_stability_enumeration"]["hom_to_L_nonnegative_candidates"] == [], "Hom-to-L not empty")
    require(
        data["equal_radius_stability_enumeration"]["hom_to_Q_nonnegative_candidates"]
        == [[-2, 2, 0], [-1, 1, 0], [-1, 2, 0]],
        "unexpected equal-radius Hom-to-Q candidates",
    )
    require(
        data["equal_radius_stability_enumeration"]["all_equal_radius_candidates_obstructed_by_prior_Yoneda"] is True,
        "equal-radius candidates not obstructed",
    )
    require(
        data["HYM_existence_bridge"]["abstract_HYM_existence_for_selected_bundle_metric"] is True,
        "abstract HYM bridge should close",
    )
    require(data["HYM_existence_bridge"]["operator_values_emitted"] is False, "operator values must remain open")
    require(data["what_remains_open"]["same_source_D_E_Riesz_Green_dotD"] is True, "operator pipeline must remain open")
    require(
        data["next_required_artifact"] == "MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1",
        "wrong next artifact",
    )
    require(cert["abstract_HYM_existence_bridge_closed"] is True, "certificate HYM close missing")
    require(cert["operator_values_open"] is True, "certificate operator-open flag missing")
    require("Equal radius is not used as a branch selector" in proof, "proof must state equal-radius guardrail")
    require("does not emit HYM operator values" in proof, "proof must state operator guardrail")

    print("PASS selected Route-C equal-radius Gauduchon HYM bridge audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
