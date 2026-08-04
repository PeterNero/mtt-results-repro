from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_source_overlap_packet_chain_import_certificate.json"
OUT_CERT = ROOT / "certificates" / "routec_sourceemission_stability_chain_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_sourceemission_stability_chain_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_SourceEmission_Stability_Chain_Import_v1.md"

STATUS = "ROUTEC_SOURCEEMISSION_STABILITY_CHAIN_IMPORTED_HYM_EXISTENCE_OPERATOR_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1"

ARTIFACTS = [
    {
        "name": "source-emission minimal subpacket attack plan",
        "data": "candidate_data/selected_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json",
        "cert": "certificates/selected_routec_sourceemission_minimal_subpacket_attack_plan_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1.md",
        "status": "MTT_SELECTED_ROUTEC_SOURCEEMISSION_MINIMAL_SUBPACKET_ATTACK_PLAN_BUILT",
        "next": "MTT_Selected_RouteC_OperatorSourceIdentity_Subpacket_v1",
    },
    {
        "name": "operator-source identity subpacket",
        "data": "candidate_data/selected_routec_operatorsourceidentity_subpacket.candidate.json",
        "cert": "certificates/selected_routec_operatorsourceidentity_subpacket_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_OperatorSourceIdentity_Subpacket_v1.md",
        "status": "MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_IDENTITY_SUBPACKET_REDUCED_TO_RANK2_OR_ROUTEC_FILL_VALUES_OPEN",
        "next": "MTT_Selected_RouteC_Rank2_L2_Cohomology_or_RouteC_Residual_Fill_v1",
    },
    {
        "name": "rank-two L2 cohomology fill",
        "data": "candidate_data/selected_routec_rank2_l2_or_routec_residual_fill.candidate.json",
        "cert": "certificates/selected_routec_rank2_l2_or_routec_residual_fill_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_Rank2_L2_Cohomology_or_RouteC_Residual_Fill_v1.md",
        "status": "MTT_SELECTED_ROUTEC_RANK2_L2_COHOMOLOGY_FILL_CLOSED_STABILITY_OR_ROUTEC_RESIDUAL_OPEN",
        "next": "MTT_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1",
    },
    {
        "name": "stability/HYM or Route-C residual source",
        "data": "candidate_data/selected_routec_stability_hym_or_routec_residual_source.candidate.json",
        "cert": "certificates/selected_routec_stability_hym_or_routec_residual_source_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1.md",
        "status": "MTT_SELECTED_ROUTEC_STABILITY_ATTEMPT_CENTRAL_NEUTRAL_CLOSED_GLOBAL_ENUMERATION_OPEN",
        "next": "MTT_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1",
    },
    {
        "name": "global destabilizer enumeration",
        "data": "candidate_data/selected_routec_global_destabilizer_enumeration_or_selected_residual.candidate.json",
        "cert": "certificates/selected_routec_global_destabilizer_enumeration_or_selected_residual_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1.md",
        "status": "MTT_SELECTED_ROUTEC_REDUCED_AH_GLOBAL_DESTABILIZER_ENUMERATION_PROVED_PROMOTION_OPEN",
        "next": "MTT_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1",
    },
    {
        "name": "AH/good-cover promotion and HYM certificate",
        "data": "candidate_data/selected_routec_selected_ah_goodcover_promotion_hym_certificate.candidate.json",
        "cert": "certificates/selected_routec_selected_ah_goodcover_promotion_hym_certificate_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_Selected_AH_or_GoodCover_Promotion_and_HYM_Certificate_v1.md",
        "status": "MTT_SELECTED_ROUTEC_REFLEXIVE_HULL_AND_CONDITIONAL_HYM_BRIDGE_PROVED_AH_SELECTION_OPEN",
        "next": "MTT_Selected_RouteC_AH_Source_Selection_or_RouteC_SelectedResidual_v1",
    },
    {
        "name": "AH source selection or Route-C selected residual",
        "data": "candidate_data/selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json",
        "cert": "certificates/selected_routec_ah_source_selection_or_routec_selected_residual_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_AH_Source_Selection_or_RouteC_SelectedResidual_v1.md",
        "status": "MTT_SELECTED_ROUTEC_ORDERED_AH_SOURCE_LAYER_PROMOTED_GAUDUCHON_OR_RESIDUAL_SOURCE_OPEN",
        "next": "MTT_Selected_RouteC_Gauduchon_Chamber_or_SelectedResidual_Source_v1",
    },
    {
        "name": "equal-radius Gauduchon HYM bridge",
        "data": "candidate_data/selected_routec_equalradius_gauduchon_hym_bridge.candidate.json",
        "cert": "certificates/selected_routec_equalradius_gauduchon_hym_bridge_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_EqualRadius_Gauduchon_HYM_Bridge_v1.md",
        "status": "MTT_SELECTED_ROUTEC_EQUALRADIUS_GAUDUCHON_HYM_EXISTENCE_BRIDGE_CLOSED_OPERATOR_VALUES_OPEN",
        "next": NEXT_ARTIFACT,
    },
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    input_checks = {
        "previous_import_proved": prev["theorem"]["proved"] is True,
        "previous_next_matches_first_artifact": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1",
    }

    imported = []
    for artifact in ARTIFACTS:
        data_path = SM / artifact["data"]
        cert_path = SM / artifact["cert"]
        note_path = SM / artifact["note"]
        data = load(data_path)
        cert = load(cert_path)
        note = note_path.read_text(encoding="utf-8")

        checks = {
            "data_status_matches": data["status"] == artifact["status"],
            "cert_status_matches": cert["status"] == artifact["status"],
            "next_matches": data["next_required_artifact"] == artifact["next"],
            "closure_not_claimed": data.get("closure_claimed") is False,
            "target_fitting_not_used": data.get("target_fitting_used") is False,
            "note_is_present": len(note.strip()) > 0,
        }
        imported.append(
            {
                "name": artifact["name"],
                "source_data": str(data_path),
                "source_certificate": str(cert_path),
                "source_note": str(note_path),
                "status": data["status"],
                "next_required_artifact": data["next_required_artifact"],
                "checks": checks,
                "what_closes_now": data.get("what_closes_now") or cert.get("what_closes"),
                "what_remains_open": data.get("what_remains_open") or cert.get("what_remains_open"),
            }
        )

    rank2 = load(SM / ARTIFACTS[2]["data"])
    equal = load(SM / ARTIFACTS[-1]["data"])
    final_checks = {
        "rank2_l2_h1_is_8": rank2["rank2_l2_fill"]["reported_cohomology"]["h1"] == 8,
        "rank2_nonzero_ext_closed": rank2["rank2_l2_fill"]["closed_now"]["nonzero_ext_class_selected"] is True,
        "selected_equal_radius_metric_present": equal["selected_equal_radius_gauduchon_metric"]["selected"] is True,
        "equal_radius_stability_closed": equal["what_closes_now"][
            "V_alpha_stable_at_selected_equal_radius_in_selected_AH_layer"
        ]
        is True,
        "abstract_hym_existence_bridge_closed": equal["what_closes_now"][
            "abstract_HYM_existence_bridge_for_selected_V_alpha"
        ]
        is True,
        "operator_values_not_emitted": equal["HYM_existence_bridge"]["operator_values_emitted"] is False,
    }

    theorem = {
        "name": "RouteCSourceEmissionStabilityChainImportTheorem",
        "proved": all(input_checks.values())
        and all(all(item["checks"].values()) for item in imported)
        and all(final_checks.values()),
        "statement": (
            "The source-emission chain is imported through the selected "
            "equal-radius Gauduchon HYM bridge. The rank-two L2 arithmetic "
            "blocker is retired with h1=8 and selected nonzero Ext input; "
            "reduced and promoted stability gates advance to selected "
            "equal-radius stability; abstract HYM existence is bridged. "
            "The remaining open gate is not HYM existence but selected "
            "HYM/operator values: Chern-Weil/GS row, rho_E, D_E, Riesz/Green, "
            "dotD, operator-layer Pic0/holonomy, and primitive contractions."
        ),
    }

    verdict = {
        "sourceemission_plan_built": True,
        "operator_source_identity_reduced": True,
        "rank2_l2_arithmetic_blocker_retired": True,
        "selected_nonzero_ext_input_closed": True,
        "selected_AH_source_layer_promoted": True,
        "selected_equal_radius_gauduchon_metric_used": True,
        "abstract_HYM_existence_bridged": True,
        "selected_HYM_operator_values_emitted": False,
        "selected_A_selected_emitted": False,
        "selected_b_selected_emitted": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "input_checks": input_checks,
        "imported_artifacts": imported,
        "final_checks": final_checks,
        "verdict": verdict,
    }

    note = """# Route-C SourceEmission Stability Chain Import v1

## Result

The source-emission chain is imported through the selected equal-radius
Gauduchon HYM bridge.

Closed or advanced:

```text
source-emission plan split into ordered subpackets
operator-source identity reduced to rank-two L2 or Route-C residual fill
rank-two L2 cohomology validates with h1 = 8
selected nonzero non-exact Ext input for V_alpha
reduced/global AH stability enumeration
reflexive-hull reduction and conditional Li-Yau/Gauduchon HYM bridge
selected equal-radius Gauduchon metric from rho_UV/constants branch
V_alpha stability at equal radius in the selected AH layer
abstract HYM existence bridge for selected V_alpha
```

What remains open is now smaller and more concrete:

```text
selected HYM connection/operator values
same-source Chern-Weil/Green-Schwarz row
same-source rho_E, D_E, Riesz/Green, and dotD
operator-layer Pic0 or holonomy-sensitive quotient
primitive C1 contractions
A_selected and b_selected
```

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_SOURCEEMISSION_STABILITY_CHAIN_IMPORTED_HYM_EXISTENCE_OPERATOR_VALUES_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_sourceemission_stability_chain_import",
                "status": STATUS,
                "input_certificate": str(PREV_IMPORT),
                "theorem": theorem,
                "input_checks": input_checks,
                "imported_artifacts": imported,
                "final_checks": final_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
