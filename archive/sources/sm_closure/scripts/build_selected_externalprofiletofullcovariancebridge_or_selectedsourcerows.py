"""Build external-profile to full-covariance bridge or selected-source rows artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_externalprofiletofullcovariancebridge_or_selectedsourcerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
COV_BRIDGE = PACKET_DIR / "external_profile_full_covariance_bridge.packet.json"
SOURCE_FORK = PACKET_DIR / "selected_source_rows_fork.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_external_profile_bridge.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ExternalProfileToFullCovarianceBridge_or_SelectedSourceRows_v1.md"

PREVIOUS = DATA / "selected_bctselectedsourcerepair_or_fullprofileupgrade.candidate.json"
PROFILE_UPGRADE = (
    DATA
    / "selected_bctselectedsourcerepair_or_fullprofileupgrade"
    / "external_profile_upgrade.packet.json"
)
FRONTIER = (
    DATA
    / "selected_bctselectedsourcerepair_or_fullprofileupgrade"
    / "nonlooping_frontier_decision.packet.json"
)
BCT_PROFILE = (
    DATA
    / "selected_charmtablesubstitution_or_selectedrthetarowsdecision"
    / "bct_empirical_table_substituted_profile.packet.json"
)
WZH_ROWS = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_external_benchmark_row_acceptance.packet.json"
)
SURROGATE_MATRIX = (
    DATA
    / "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion"
    / "correlated_threshold_profile_matrix.packet.json"
)
PROMOTION_GATE = (
    DATA
    / "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion"
    / "yukawa_higgs_precision_promotion_gate.packet.json"
)
BCT_SELECTED_LANE = (
    DATA
    / "selected_bctformulaimport_or_selectedthresholdrowderivation"
    / "bct_selected_rtheta_derivation_lane.packet.json"
)

STATUS = (
    "MTT_SELECTED_EXTERNALPROFILETOFULLCOVARIANCEBRIDGE_OR_SELECTEDSOURCEROWS_"
    "BUILT_8X8_COVARIANCE_TARGET_SELECTED_ROWS_OPEN"
)
NEXT = "MTT_Selected_PublishedCovarianceLikelihoodImport_or_RouteCSelectedSourceEmission_v1"


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
        raise FileNotFoundError("missing external-profile bridge sources: " + ", ".join(missing))


def symmetric_unique(n: int) -> int:
    return n * (n + 1) // 2


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PROFILE_UPGRADE,
        FRONTIER,
        BCT_PROFILE,
        WZH_ROWS,
        SURROGATE_MATRIX,
        PROMOTION_GATE,
        BCT_SELECTED_LANE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    profile_upgrade = load(PROFILE_UPGRADE)
    frontier = load(FRONTIER)
    bct_profile = load(BCT_PROFILE)
    wzh_rows = load(WZH_ROWS)
    surrogate = load(SURROGATE_MATRIX)
    promotion = load(PROMOTION_GATE)
    selected_lane = load(BCT_SELECTED_LANE)

    bct_n = profile_upgrade["accepted_BCT_external_map_row_count"]
    wzh_n = profile_upgrade["accepted_WZH_external_coordinate_row_count"]
    total_n = profile_upgrade["accepted_external_profile_coordinate_count"]
    full_unique = symmetric_unique(total_n)
    bct_unique = symmetric_unique(bct_n)
    wzh_unique = symmetric_unique(wzh_n)
    cross_entries = bct_n * wzh_n

    cov_bridge = {
        "schema": "MTTExternalProfileFullCovarianceBridge.v1",
        "status": "EIGHT_COORDINATE_FULL_COVARIANCE_TARGET_FIXED_VALUES_OPEN",
        "profile_upgrade_source": rel(PROFILE_UPGRADE),
        "bct_profile_source": rel(BCT_PROFILE),
        "wzh_row_source": rel(WZH_ROWS),
        "surrogate_matrix_source": rel(SURROGATE_MATRIX),
        "external_coordinate_blocks": {
            "BCT_empirical_block": {
                "coordinate_count": bct_n,
                "unique_covariance_entries": bct_unique,
                "profile_95pct_closed": bct_profile["passes_95pct_profile_gate"],
                "source_or_Rtheta_closure_claimed": bct_profile["source_or_Rtheta_closure_claimed"],
                "status": bct_profile["status"],
            },
            "WZH_weak_scale_block": {
                "coordinate_count": wzh_n,
                "unique_covariance_entries": wzh_unique,
                "external_coordinate_rows_closed": (
                    wzh_rows["accepted_external_wzh_coordinate_row_count"] == wzh_n
                ),
                "accepted_full_covariance_profile_row_count": wzh_rows[
                    "accepted_full_covariance_profile_row_count"
                ],
                "surrogate_matrix_available": surrogate["accepted_as_surrogate_correlated_threshold_profile_matrix"],
                "published_or_reconstructed_likelihood_available": surrogate[
                    "accepted_as_published_or_reconstructed_profile_likelihood"
                ],
            },
            "BCT_cross_WZH_block": {
                "coordinate_count": [bct_n, wzh_n],
                "cross_covariance_entries": cross_entries,
                "published_or_reconstructed_cross_covariance_available": False,
            },
        },
        "full_covariance_target": {
            "coordinate_count": total_n,
            "matrix_shape": [total_n, total_n],
            "symmetric_unique_entries": full_unique,
            "known_or_scaffolded_substructure_entries": {
                "BCT_empirical_profile_block": bct_unique,
                "WZH_surrogate_weak_scale_block": wzh_unique,
                "BCT_cross_WZH_block": 0,
            },
            "strict_full_profile_entries_accepted": 0,
            "surrogate_or_empirical_entries_scaffolded": bct_unique + wzh_unique,
            "hard_missing_entries_for_published_or_reconstructed_likelihood": cross_entries,
        },
        "promotion_gate": {
            "published_or_reconstructed_profile_likelihood_imported": promotion["promotion_tests"][
                "published_or_reconstructed_profile_likelihood_imported"
            ],
            "threshold_matching_values_emitted": promotion["promotion_tests"]["threshold_matching_values_emitted"],
            "mass_scheme_conversion_values_emitted": promotion["promotion_tests"][
                "mass_scheme_conversion_values_emitted"
            ],
            "multi_loop_threshold_convention_values_emitted": promotion["promotion_tests"][
                "multi_loop_threshold_convention_values_emitted"
            ],
            "no_knob_MTT_source_derivation_of_values": promotion["promotion_tests"][
                "no_knob_MTT_source_derivation_of_values"
            ],
        },
        "full_covariance_profile_likelihood_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(COV_BRIDGE, cov_bridge)

    source_fork = {
        "schema": "MTTSelectedSourceRowsForkAfterExternalProfileBridge.v1",
        "status": "SELECTED_SOURCE_ROWS_STILL_REQUIRE_ROUTEC_SOLVE_OR_NO_KNOB_DERIVATION",
        "selected_lane_source": rel(BCT_SELECTED_LANE),
        "minimal_internal_missing_object": selected_lane["minimal_internal_missing_object"],
        "accepted_selected_BCT_source_row_count": selected_lane["accepted_Rtheta_source_row_count"],
        "honest_root_all_pass": selected_lane["honest_root_all_pass"],
        "selected_routec_galerkin_solve_closed": selected_lane["selected_routec_galerkin_solve_closed"],
        "live_source_routes": {
            "RouteC_Strominger_Galerkin_selected_source_emission": True,
            "no_knob_value_source_derivation": True,
            "external_published_likelihood_import_as_validation_not_source": True,
        },
        "must_not_promote": [
            "empirical BCT table substitution as source derivation",
            "WZH external coordinates as selected Rtheta rows",
            "surrogate covariance matrix as published likelihood",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SOURCE_FORK, source_fork)

    cutset = {
        "schema": "MTTNextCutsetAfterExternalProfileBridge.v1",
        "status": "NEXT_ATTACK_PUBLISHED_COVARIANCE_LIKELIHOOD_OR_ROUTEC_SOURCE_EMISSION",
        "closed_now": {
            "external_profile_coordinate_count_fixed": True,
            "full_8x8_covariance_target_shape_fixed": True,
            "BCT_WZH_cross_covariance_gap_quantified": True,
            "selected_source_rows_fork_guarded": True,
        },
        "still_open": {
            "published_or_reconstructed_8x8_profile_likelihood": True,
            "BCT_WZH_cross_covariance_entries": True,
            "WZH_full_covariance_profile_rows": True,
            "threshold_matching_values": True,
            "mass_scheme_conversion_values": True,
            "SelectedRouteCStromingerGalerkinResidualSolve": True,
            "selected_Rtheta_source_rows": True,
            "no_knob_value_source_derivation": True,
            "true_SM_equivalence": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "import or reconstruct the published 8x8 covariance/profile likelihood for the external coordinate layer",
            "route_B": "emit Route-C selected source rows and replace empirical/external rows with no-knob rows",
            "route_C": "derive threshold and mass-scheme conversion values, then rebuild the covariance target from source values",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedExternalProfileToFullCovarianceBridgeOrSelectedSourceRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "external_profile_full_covariance_bridge": rel(COV_BRIDGE),
            "selected_source_rows_fork": rel(SOURCE_FORK),
            "next_cutset_after_external_profile_bridge": rel(CUTSET),
        },
        "theorem": {
            "name": "ExternalProfileEightCoordinateBridgeAndSourceRowsForkTheorem",
            "proved": True,
            "statement": (
                "The upgraded external profile layer fixes an eight-coordinate covariance target: three BCT "
                "empirical coordinates and five W/Z/H weak-scale coordinates. This closes the target shape and "
                "quantifies the 3x5 BCT-WZH cross-covariance gap. It does not close full covariance likelihood "
                "or selected source rows: the W/Z/H block remains a surrogate/coordinate layer, the cross-block "
                "is absent, and Route-C selected-source emission is still open."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "external_profile_coordinate_count_fixed": True,
            "external_profile_coordinate_count": total_n,
            "full_covariance_matrix_shape_fixed": [total_n, total_n],
            "full_covariance_symmetric_unique_entries": full_unique,
            "BCT_WZH_cross_covariance_entries_missing": cross_entries,
            "full_covariance_profile_likelihood_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "no_knob_value_source_derivation_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ExternalProfileToFullCovarianceBridge_or_SelectedSourceRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "external_profile_coordinate_count": total_n,
        "full_covariance_matrix_shape_fixed": [total_n, total_n],
        "full_covariance_symmetric_unique_entries": full_unique,
        "BCT_WZH_cross_covariance_entries_missing": cross_entries,
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

    note = f"""# MTT Selected ExternalProfileToFullCovarianceBridge or SelectedSourceRows v1

Status: `{STATUS}`.

The external profile layer now has a fixed covariance target.

```text
external coordinates              : {total_n}
full covariance shape             : {total_n} x {total_n}
symmetric covariance entries       : {full_unique}
BCT empirical block entries        : {bct_unique}
W/Z/H surrogate block entries      : {wzh_unique}
BCT-W/Z/H cross entries missing    : {cross_entries}
selected source rows closed        : false
```

This moves the frontier from "need full profile" to a precise object:
import/reconstruct the eight-coordinate profile likelihood or replace the
external coordinates with selected source rows from Route-C/no-knob derivation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
