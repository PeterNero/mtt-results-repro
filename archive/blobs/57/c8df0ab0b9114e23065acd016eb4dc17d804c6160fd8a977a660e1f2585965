"""Build the minimal source-emission subpacket attack plan."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
CONTRACT = DATA / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"
VISIBLE = DATA / "selected_visible_chern_weil_operator_source.candidate.json"
PHIFIN = DATA / "selected_phifin_alpha1_payload.candidate.json"

OUTPUT = DATA / "selected_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json"
CERT = CERTS / "selected_routec_sourceemission_minimal_subpacket_attack_plan_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_SOURCEEMISSION_MINIMAL_SUBPACKET_ATTACK_PLAN_BUILT"
NEXT = "MTT_Selected_RouteC_OperatorSourceIdentity_Subpacket_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    contract = load(CONTRACT)
    visible = load(VISIBLE)
    phifin = load(PHIFIN)

    dependency_order = [
        {
            "id": "S1_operator_source_identity",
            "priority": 1,
            "reason": "Without visible/Route-C operator-source identity, no downstream D_E, dotD, overlap, or normalization field can be same-source selected.",
            "must_emit": [
                "selected visible bundle/sheaf or Route-C source on q79/F,m=1",
                "operator-level projective/twisted rho_E promotion or explicit replacement",
                "HYM/Strominger or Route-C residual with selected_source_verified true",
            ],
            "current_blockers": visible["open_gates"]["same_source_cut_set"],
            "next_artifact": NEXT,
        },
        {
            "id": "S2_operator_values",
            "priority": 2,
            "reason": "Once source identity exists, D_E/dotD/Riesz/Green values are the validator backbone for all C1 emissions.",
            "must_emit": [
                "selected D_E action",
                "selected reduced Green/Riesz projectors",
                "selected dotD alpha1 with alpha1_driver_verified",
            ],
            "current_blockers": {
                key: not value
                for key, value in phifin["payload_summary"]["selected_payload_flags"].items()
                if key in {"D_E_action", "Riesz_Green", "dotD_alpha1"}
            },
            "next_artifact": "MTT_Selected_RouteC_DE_DotD_Green_SourceEmission_Subpacket_v1",
        },
        {
            "id": "S3_matter_slot_charge",
            "priority": 3,
            "reason": "Matter-slot charge and the 1_M neutrino rule can only promote after S1/S2 give selected sector bases/operators.",
            "must_emit": [
                "10_M -> u/e",
                "non-10 plus 1_M -> d/nuD",
                "selected sector routing independent of locked C1 target",
            ],
            "current_blockers": {
                "selected_charge_table": True,
                "selected_1M_neutrino_rule": True,
            },
            "next_artifact": "MTT_Selected_RouteC_MatterSlotCharge_Subpacket_v1",
        },
        {
            "id": "S4_overlap_and_normalization",
            "priority": 4,
            "reason": "Overlap functor and normalization require selected source, selected operators, and selected sector routing.",
            "must_emit": [
                "selected T_selected source-to-C1 functor",
                "selected trace/inner-product/Hessian normalization",
                "selected primitive C1/Yukawa contractions",
                "selected b_selected",
            ],
            "current_blockers": {
                "overlap_transfer_functor": True,
                "normalization": True,
                "primitive_contractions": True,
                "b_selected": True,
            },
            "next_artifact": "MTT_Selected_RouteC_OverlapNormalization_Subpacket_v1",
        },
    ]

    candidate = {
        "candidate": "MTTSelectedRouteCSourceEmissionMinimalSubpacketAttackPlan",
        "status": STATUS,
        "inputs": {
            "previous_fill_or_nogo": rel(PREVIOUS),
            "same_source_contract": rel(CONTRACT),
            "visible_cw_operator_source": rel(VISIBLE),
            "selected_phifin_alpha1_payload": rel(PHIFIN),
        },
        "strategy": {
            "why_not_fill_all_at_once": "The fill/no-go validator rejected all seven fields; attempting all fields together hides the first dependency.",
            "minimal_first_subpacket": NEXT,
            "dependency_order": dependency_order,
            "promotion_condition": "Only after S1-S4 pass may conditional A_weylpair be promoted to A_selected.",
        },
        "what_closes_now": {
            "minimal_dependency_order_built": True,
            "first_subpacket_selected": True,
            "fill_nogo_converted_to_attack_plan": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": previous["what_remains_open"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C SourceEmission Minimal Subpacket Attack Plan

Status: `MTT_SELECTED_ROUTEC_SOURCEEMISSION_MINIMAL_SUBPACKET_ATTACK_PLAN_BUILT`

The seven-field packet cannot be filled at once from current scaffolds.  The
minimal first target is operator-source identity.

## Dependency Order

1. Operator-source identity.
2. Selected D_E/dotD/Riesz/Green values.
3. Selected matter-slot charge and `1_M` neutrino routing.
4. Selected overlap functor, normalization, primitive contractions, and
   `b_selected`.

Only after these pass may the conditional Weyl-pair operator be promoted to
`A_selected`.

Next artifact: `MTT_Selected_RouteC_OperatorSourceIdentity_Subpacket_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
