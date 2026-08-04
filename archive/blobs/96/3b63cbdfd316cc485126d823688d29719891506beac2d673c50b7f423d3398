"""Audit selected alpha1 tangent promotion / sector-routing theorem slot."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json"
CERT = ROOT / "certificates" / "selected_alpha1_tangent_promotion_or_sector_routing_theorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Alpha1_Tangent_Promotion_or_SectorRouting_Normalization_Theorem_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_TANGENT_PROMOTION_THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    theorem = data["theorem_slot"]
    routes = theorem["conditional_promotion_routes"]
    boundary = data["operator_payload_boundary"]
    paper = data["paper_update_record"]
    draft_texts = {
        key: (ROOT / path).read_text(encoding="utf-8")
        for key, path in paper["draft_paths"].items()
    }

    unconditional = theorem["proved_unconditionally_now"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "theorem slot named",
            theorem["id"] == "I5a_alpha1_tangent_promotion_or_sector_routing_normalization"
            and theorem["name"] == "SelectedAlpha1TangentPromotionOrSectorRoutingNormalizationTheorem"
            and "physical dotD_alpha1 iff" in theorem["formal_statement"],
            theorem,
        ),
        check(
            "selected tangent packaged",
            unconditional["selected_Ext_density_tangent_closed"] is True
            and unconditional["residual_below_1e_12"] is True
            and unconditional["zero_mean_tangent"] is True
            and unconditional["nontrivial_tangent"] is True
            and unconditional["dotD_frechet_replay_closed"] is True,
            unconditional,
        ),
        check(
            "operator support retained",
            unconditional["offdiagonal_T1T2_leakage_controlled"] is True
            and unconditional["End0_connection_formula_available"] is True
            and unconditional["T1T2_covariant_green_closed"] is True,
            unconditional,
        ),
        check(
            "promotion routes are conditional",
            routes["route_A_source_normalization"]["proved_now"] is False
            and routes["route_B_sector_routing_normalization"]["proved_now"] is False
            and "discrete alpha1" in routes["route_A_source_normalization"]["hypothesis"]
            and "End0-to-sector routing functor" in routes["route_B_sector_routing_normalization"]["hypothesis"],
            routes,
        ),
        check(
            "no-promotion lemma applies",
            theorem["no_promotion_lemma"]["applies_now"] is True
            and "support-only" in theorem["no_promotion_lemma"]["statement"],
            theorem["no_promotion_lemma"],
        ),
        check(
            "payload boundary honest",
            boundary["selected_Ext_density_scale_dotD_tangent_extracted"] is True
            and boundary["physical_dotD_alpha1_payload_extracted"] is False
            and boundary["selected_End0_to_sector_routing_values_extracted"] is False
            and boundary["validator_ready"] is False,
            boundary,
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            {
                "closure_claimed": data["closure_claimed"],
                "target_fitting_used": data["target_fitting_used"],
            },
        ),
        check(
            "paper drafts guarded",
            set(paper["target_papers"]) == {"theta_execution_flavor", "theta_nonabelian_overlaps", "strominger_system"}
            and len(paper["draft_paths"]) == 3
            and all("does not promote physical `alpha1`" in text for text in draft_texts.values())
            and all("No observed masses, mixings, CP phases" in text for text in draft_texts.values()),
            paper,
        ),
        check(
            "remaining gates explicit",
            data["what_remains_open"]["selected_source_normalization_identifies_alpha1_tangent"] is True
            and data["what_remains_open"]["selected_End0_to_sector_routing_values"] is True
            and data["what_remains_open"]["physical_dotD_alpha1_same_branch_driver"] is True,
            data["what_remains_open"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records theorem and guardrail",
            "This tangent may be promoted to physical `dotD_alpha1` if and only if" in note
            and "Without one of these two normalizations" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected alpha1 tangent promotion / sector-routing theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
