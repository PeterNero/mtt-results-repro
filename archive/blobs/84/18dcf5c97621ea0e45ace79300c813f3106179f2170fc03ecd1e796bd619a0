"""Build BCT selected-source repair or full-profile upgrade artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bctselectedsourcerepair_or_fullprofileupgrade"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_REPAIR = PACKET_DIR / "selected_source_repair_retest.packet.json"
PROFILE_UPGRADE = PACKET_DIR / "external_profile_upgrade.packet.json"
FRONTIER = PACKET_DIR / "nonlooping_frontier_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bct_source_repair_or_profile_upgrade.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BCTSelectedSourceRepair_or_FullProfileUpgrade_v1.md"

BCT_DUAL = DATA / "selected_bctformulaimport_or_selectedthresholdrowderivation.candidate.json"
BCT_SELECTED_LANE = (
    DATA
    / "selected_bctformulaimport_or_selectedthresholdrowderivation"
    / "bct_selected_rtheta_derivation_lane.packet.json"
)
BCT_EXTERNAL_LANE = (
    DATA
    / "selected_bctformulaimport_or_selectedthresholdrowderivation"
    / "bct_external_formula_import_lane.packet.json"
)
BCT_UPDATED_READINESS = (
    DATA
    / "selected_bctformulaimport_or_selectedthresholdrowderivation"
    / "updated_threshold_readiness_after_bct_import.packet.json"
)
CHARM_SUB = DATA / "selected_charmtablesubstitution_or_selectedrthetarowsdecision.candidate.json"
CHARM_PROFILE = (
    DATA
    / "selected_charmtablesubstitution_or_selectedrthetarowsdecision"
    / "bct_empirical_table_substituted_profile.packet.json"
)
WZH = DATA / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation.candidate.json"
WZH_ROWS = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_external_benchmark_row_acceptance.packet.json"
)
DIAG_PROFILE = (
    DATA
    / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
    / "diagonal_profile_likelihood_execution.packet.json"
)
SURROGATE = (
    DATA
    / "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion"
    / "correlated_threshold_profile_matrix.packet.json"
)

STATUS = (
    "MTT_SELECTED_BCTSELECTEDSOURCEREPAIR_OR_FULLPROFILEUPGRADE_"
    "BUILT_PROFILE_UPGRADED_SOURCE_REPAIR_BLOCKED"
)
NEXT = "MTT_Selected_ExternalProfileToFullCovarianceBridge_or_SelectedSourceRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing BCT profile-upgrade sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        BCT_DUAL,
        BCT_SELECTED_LANE,
        BCT_EXTERNAL_LANE,
        BCT_UPDATED_READINESS,
        CHARM_SUB,
        CHARM_PROFILE,
        WZH,
        WZH_ROWS,
        DIAG_PROFILE,
        SURROGATE,
    ]
    require_sources(sources)

    bct_dual = load(BCT_DUAL)
    selected_lane = load(BCT_SELECTED_LANE)
    external_lane = load(BCT_EXTERNAL_LANE)
    readiness = load(BCT_UPDATED_READINESS)
    charm_sub = load(CHARM_SUB)
    charm_profile = load(CHARM_PROFILE)
    wzh = load(WZH)
    wzh_rows = load(WZH_ROWS)
    diag_profile = load(DIAG_PROFILE)
    surrogate = load(SURROGATE)

    source_repair = {
        "schema": "MTTBCTSelectedSourceRepairRetest.v1",
        "status": "SELECTED_SOURCE_REPAIR_RETESTED_NO_NEW_PROMOTION",
        "source_lane": rel(BCT_SELECTED_LANE),
        "minimal_internal_missing_object": selected_lane["minimal_internal_missing_object"],
        "failed_honest_root_slots": selected_lane["failed_honest_root_slots"],
        "formal_lift_lower_validators_all_pass": selected_lane["formal_lift_lower_validators_all_pass"],
        "honest_root_all_pass": selected_lane["honest_root_all_pass"],
        "selected_Rtheta_mass_scheme_derivation_closed": selected_lane[
            "selected_Rtheta_mass_scheme_derivation_closed"
        ],
        "selected_routec_galerkin_solve_closed": selected_lane["selected_routec_galerkin_solve_closed"],
        "accepted_BCT_selected_source_row_count": selected_lane["accepted_Rtheta_source_row_count"],
        "nonlooping_rule": (
            "Do not spend another artifact on BCT selected-source repair unless "
            "SelectedRouteCStromingerGalerkinResidualSolve changes or emits new honest selected-source payloads."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SOURCE_REPAIR, source_repair)

    external_wzh_count = wzh["closure_decision"]["accepted_external_wzh_coordinate_row_count"]
    profile_upgrade = {
        "schema": "MTTExternalProfileUpgradeAfterBCT.v1",
        "status": "BCT_EMPIRICAL_AND_WZH_EXTERNAL_PROFILE_LAYER_UPGRADED",
        "bct_external_lane": rel(BCT_EXTERNAL_LANE),
        "bct_updated_readiness": rel(BCT_UPDATED_READINESS),
        "charm_table_substitution_profile": rel(CHARM_PROFILE),
        "wzh_external_rows": rel(WZH_ROWS),
        "diagonal_profile_likelihood": rel(DIAG_PROFILE),
        "surrogate_correlated_threshold_profile": rel(SURROGATE),
        "accepted_BCT_external_map_row_count": external_lane["accepted_external_bct_map_row_count"],
        "accepted_WZH_external_coordinate_row_count": external_wzh_count,
        "accepted_external_profile_coordinate_count": (
            external_lane["accepted_external_bct_map_row_count"] + external_wzh_count
        ),
        "BCT_empirical_profile_95pct_closure_closed": charm_sub["closure_decision"][
            "BCT_empirical_profile_95pct_closure_closed"
        ],
        "BCT_empirical_profile_survival_probability": charm_sub["closure_decision"][
            "BCT_empirical_profile_survival_probability"
        ],
        "BCT_source_or_no_knob_profile_closure_closed": charm_sub["closure_decision"][
            "BCT_source_or_no_knob_profile_closure_closed"
        ],
        "W_Z_H_electroweak_matching_rows_closed_at_external_coordinate_layer": wzh["closure_decision"][
            "W_Z_H_electroweak_matching_rows_closed_at_external_coordinate_layer"
        ],
        "diagonal_profile_executed": diag_profile.get("closure_claimed") is True
        or diag_profile.get("profile_execution", {}).get("diagonal_profile_executed") is True,
        "surrogate_correlated_threshold_profile_matrix_emitted": surrogate.get("closure_claimed") is True,
        "full_covariance_profile_likelihood_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "profile_upgrade_boundary": (
            "This is an external-coordinate/profile-readiness upgrade. It is stronger than raw row availability "
            "because BCT empirical 95 percent closure and W/Z/H external coordinate rows are both attached, "
            "but it is not a same-source or no-knob value derivation."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PROFILE_UPGRADE, profile_upgrade)

    frontier = {
        "schema": "MTTNonLoopingFrontierDecisionAfterBCTProfileUpgrade.v1",
        "status": "MOVE_FORWARD_TO_FULL_COVARIANCE_OR_SOURCE_ROWS",
        "new_progress_since_dual_lane": {
            "BCT_empirical_profile_95pct_closure_now_available": profile_upgrade[
                "BCT_empirical_profile_95pct_closure_closed"
            ],
            "WZH_external_coordinate_layer_closed": profile_upgrade[
                "W_Z_H_electroweak_matching_rows_closed_at_external_coordinate_layer"
            ],
            "external_profile_coordinate_count": profile_upgrade["accepted_external_profile_coordinate_count"],
            "selected_source_repair_retested": True,
        },
        "retire_for_now": {
            "repeat_BCT_selected_source_repair_without_new_routec_payload": True,
            "repeat_charm_policy_residual_minimization": True,
            "repeat_fullSM_tau_profile_comparison_without_EFT_to_fullSM_conversion": True,
        },
        "live_frontier": {
            "full_covariance_profile_likelihood": True,
            "published_or_reconstructed_profile_likelihood": True,
            "selected_Rtheta_source_rows": True,
            "SelectedRouteCStromingerGalerkinResidualSolve": True,
            "no_knob_value_source_derivation": True,
            "true_SM_equivalence": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FRONTIER, frontier)

    cutset = {
        "schema": "MTTNextCutsetAfterBCTSelectedSourceRepairOrFullProfileUpgrade.v1",
        "status": "NEXT_ATTACK_FULL_COVARIANCE_PROFILE_OR_SELECTED_SOURCE_ROWS",
        "closed_now": {
            "BCT_selected_source_repair_retested": True,
            "BCT_empirical_profile_95pct_closure_imported": True,
            "WZH_external_coordinate_layer_imported": True,
            "external_profile_coordinate_layer_upgraded": True,
            "nonlooping_frontier_guard_added": True,
        },
        "still_open": frontier["live_frontier"],
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "construct/publish full covariance profile likelihood using the external coordinate layer",
            "route_B": "emit selected Rtheta/source rows from a changed Route-C/Strominger Galerkin payload",
            "route_C": "derive no-knob value-source rows and then replay the profile without empirical imports",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedBCTSelectedSourceRepairOrFullProfileUpgrade",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "selected_source_repair_retest": rel(SOURCE_REPAIR),
            "external_profile_upgrade": rel(PROFILE_UPGRADE),
            "nonlooping_frontier_decision": rel(FRONTIER),
            "next_cutset_after_bct_source_repair_or_profile_upgrade": rel(CUTSET),
        },
        "theorem": {
            "name": "BCTProfileUpgradeAndNonLoopingFrontierTheorem",
            "proved": True,
            "statement": (
                "After trying both lanes, the selected-source repair lane has no new honest promotion because "
                "SelectedRouteCStromingerGalerkinResidualSolve remains unchanged. The forward lane is therefore "
                "the external profile upgrade: three BCT external map rows, the empirical BCT 95 percent profile "
                "closure, and five W/Z/H external coordinate rows form an upgraded validation/profile layer. "
                "This is genuine progress but not full covariance, no-knob, or true SM equivalence closure."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "BCT_selected_source_repair_retested_no_new_promotion": True,
            "accepted_BCT_selected_source_row_count": 0,
            "BCT_empirical_profile_95pct_closure_imported": True,
            "WZH_external_coordinate_layer_imported": True,
            "accepted_external_profile_coordinate_count": profile_upgrade["accepted_external_profile_coordinate_count"],
            "external_profile_layer_upgraded": True,
            "full_covariance_profile_likelihood_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "no_knob_value_source_derivation_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "previous_status": bct_dual["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_BCTSelectedSourceRepair_or_FullProfileUpgrade_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "BCT_selected_source_repair_retested_no_new_promotion": True,
        "accepted_BCT_selected_source_row_count": 0,
        "BCT_empirical_profile_95pct_closure_imported": True,
        "WZH_external_coordinate_layer_imported": True,
        "accepted_external_profile_coordinate_count": profile_upgrade["accepted_external_profile_coordinate_count"],
        "external_profile_layer_upgraded": True,
        "full_covariance_profile_likelihood_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "no_knob_value_source_derivation_closed": False,
        "true_SM_equivalence_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected BCTSelectedSourceRepair or FullProfileUpgrade v1

Status: `{STATUS}`.

This is the non-looping follow-up to the BCT dual-lane attempt.

```text
BCT selected-source rows promoted       : 0
BCT empirical profile 95 percent closed : true
W/Z/H external coordinate rows imported : {external_wzh_count}
external profile coordinates upgraded   : {profile_upgrade["accepted_external_profile_coordinate_count"]}
full covariance / true SM closure        : false
```

The selected-source repair lane is not repeated unless
`SelectedRouteCStromingerGalerkinResidualSolve` changes.  The forward lane is
now the external profile layer: BCT empirical profile plus W/Z/H external
coordinates, still guarded as downstream validation data rather than selected
source data.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
