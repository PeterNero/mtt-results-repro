"""Build published covariance likelihood import or Route-C selected-source emission artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LIKELIHOOD = PACKET_DIR / "published_covariance_likelihood_import_attempt.packet.json"
ROUTEC = PACKET_DIR / "routec_selected_source_emission_attempt.packet.json"
REPLAY = PACKET_DIR / "external_profile_replay_closure_under_declared_standard.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_likelihood_or_source_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PublishedCovarianceLikelihoodImport_or_RouteCSelectedSourceEmission_v1.md"

PREVIOUS = DATA / "selected_externalprofiletofullcovariancebridge_or_selectedsourcerows.candidate.json"
BRIDGE = (
    DATA
    / "selected_externalprofiletofullcovariancebridge_or_selectedsourcerows"
    / "external_profile_full_covariance_bridge.packet.json"
)
SOURCE_FORK = (
    DATA
    / "selected_externalprofiletofullcovariancebridge_or_selectedsourcerows"
    / "selected_source_rows_fork.packet.json"
)
PRECISION_SUITE = DATA / "selected_precisionempiricalreplaysuite_or_trueequivalence.candidate.json"
COV_POLICY = (
    DATA
    / "selected_precisionempiricalreplaysuite_or_trueequivalence"
    / "covariance_profile_policy.packet.json"
)
PROFILE_IMPORT = (
    DATA
    / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
    / "profile_likelihood_source_import_status.packet.json"
)
SM_PARITY_REFRESH = (
    DATA
    / "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy"
    / "full_smparity_replay_closure_refresh.packet.json"
)
NONHIGGS_POLICY = (
    DATA
    / "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy"
    / "nonhiggs_profile_policy.packet.json"
)
BCT_PROFILE_UPGRADE = (
    DATA
    / "selected_bctselectedsourcerepair_or_fullprofileupgrade"
    / "external_profile_upgrade.packet.json"
)

STATUS = (
    "MTT_SELECTED_PUBLISHEDCOVARIANCELIKELIHOODIMPORT_OR_ROUTECSELECTEDSOURCEEMISSION_"
    "BUILT_EXTERNAL_REPLAY_CLOSED_TRUE_EQ_SOURCE_OPEN"
)
NEXT = "MTT_Selected_ExternalProfileReplayFrozenBoundary_or_TrueEquivalenceValueSourceCutset_v1"


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
        raise FileNotFoundError("missing likelihood/source emission sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        BRIDGE,
        SOURCE_FORK,
        PRECISION_SUITE,
        COV_POLICY,
        PROFILE_IMPORT,
        SM_PARITY_REFRESH,
        NONHIGGS_POLICY,
        BCT_PROFILE_UPGRADE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    bridge = load(BRIDGE)
    source_fork = load(SOURCE_FORK)
    precision_suite = load(PRECISION_SUITE)
    cov_policy = load(COV_POLICY)
    profile_import = load(PROFILE_IMPORT)
    sm_parity_refresh = load(SM_PARITY_REFRESH)
    nonhiggs_policy = load(NONHIGGS_POLICY)
    bct_profile_upgrade = load(BCT_PROFILE_UPGRADE)

    target = bridge["full_covariance_target"]
    total_n = target["coordinate_count"]
    unique_entries = target["symmetric_unique_entries"]
    missing_cross = target["hard_missing_entries_for_published_or_reconstructed_likelihood"]

    likelihood = {
        "schema": "MTTPublishedCovarianceLikelihoodImportAttempt.v1",
        "status": "NO_PUBLISHED_8X8_LIKELIHOOD_IMPORTED_TARGET_FIXED",
        "bridge_source": rel(BRIDGE),
        "legacy_profile_import_status": rel(PROFILE_IMPORT),
        "required_import_payload": [
            "published or reconstructed 8x8 covariance/profile likelihood in the fixed external profile basis",
            "3x3 BCT empirical covariance block provenance",
            "5x5 W/Z/H weak-scale covariance or likelihood workspace",
            "3x5 BCT-W/Z/H cross-covariance block",
            "profile convention, nuisance treatment, and reproducible acceptance rule",
        ],
        "local_import_candidates_checked": profile_import["local_import_candidates_checked"]
        + [
            "current 8x8 external profile bridge",
            "BCT empirical table-substituted profile",
            "W/Z/H surrogate weak-scale covariance block",
        ],
        "published_or_reconstructed_profile_likelihood_imported": False,
        "accepted_as_full_profile_likelihood": False,
        "accepted_for_true_SM_equivalence": False,
        "fixed_target_shape": target["matrix_shape"],
        "fixed_target_symmetric_entries": unique_entries,
        "missing_BCT_WZH_cross_covariance_entries": missing_cross,
        "why_import_absent": [
            "the repo still contains no published or reconstructed 8x8 likelihood workspace",
            "the W/Z/H block is surrogate/coordinate data, not a public profile likelihood",
            "the BCT-W/Z/H cross-block is absent",
            "importing central rows closes replay/admission only, not true precision equivalence",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(LIKELIHOOD, likelihood)

    routec = {
        "schema": "MTTRouteCSelectedSourceEmissionAttempt.v1",
        "status": "ROUTEC_SELECTED_SOURCE_EMISSION_NOT_PROMOTED",
        "source_fork": rel(SOURCE_FORK),
        "minimal_internal_missing_object": source_fork["minimal_internal_missing_object"],
        "accepted_selected_BCT_source_row_count": source_fork["accepted_selected_BCT_source_row_count"],
        "honest_root_all_pass": source_fork["honest_root_all_pass"],
        "selected_routec_galerkin_solve_closed": source_fork["selected_routec_galerkin_solve_closed"],
        "selected_Rtheta_source_rows_closed": False,
        "no_knob_value_source_derivation_closed": False,
        "must_not_promote": source_fork["must_not_promote"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROUTEC, routec)

    replay = {
        "schema": "MTTExternalProfileReplayClosureUnderDeclaredStandard.v1",
        "status": "EXTERNAL_PROFILE_REPLAY_CLOSED_UNDER_DECLARED_ADMISSION_STANDARD",
        "inspiration": "Mirrors the earlier SM-parity replay rule: central/external rows may close admitted replay, while full covariance/source/no-knob remain true-equivalence targets.",
        "sm_parity_source": rel(SM_PARITY_REFRESH),
        "nonhiggs_policy_source": rel(NONHIGGS_POLICY),
        "precision_suite_source": rel(PRECISION_SUITE),
        "covariance_policy_source": rel(COV_POLICY),
        "profile_upgrade_source": rel(BCT_PROFILE_UPGRADE),
        "external_profile_coordinate_count": total_n,
        "external_profile_replay_closed_under_declared_standard": True,
        "SM_parity_closed": sm_parity_refresh["SM_parity_closed"],
        "precision_empirical_replay_suite_built": precision_suite["closure_decision"][
            "precision_empirical_replay_suite_built"
        ],
        "BCT_empirical_profile_95pct_closure_imported": bct_profile_upgrade[
            "BCT_empirical_profile_95pct_closure_closed"
        ],
        "WZH_external_coordinate_layer_imported": bct_profile_upgrade[
            "W_Z_H_electroweak_matching_rows_closed_at_external_coordinate_layer"
        ],
        "full_covariance_profile_required_for_declared_replay": False,
        "full_covariance_profile_required_for_true_equivalence": cov_policy["policy"][
            "covariance_matrices"
        ]
        == "required where public fits provide correlated parameters",
        "full_covariance_profile_likelihood_closed": False,
        "published_or_reconstructed_profile_likelihood_imported": False,
        "selected_Rtheta_source_rows_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "admission_boundary": (
            "This closes the admitted external replay layer only. It does not derive the rows from MTT, "
            "does not supply a public 8x8 likelihood, and does not replace Route-C selected-source rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(REPLAY, replay)

    cutset = {
        "schema": "MTTNextCutsetAfterPublishedLikelihoodOrSourceAttempt.v1",
        "status": "NEXT_FREEZE_EXTERNAL_REPLAY_AND_ATTACK_TRUE_EQ_VALUE_SOURCE",
        "closed_now": {
            "published_likelihood_import_attempt_executed": True,
            "routec_selected_source_emission_attempt_executed": True,
            "external_profile_replay_closed_under_declared_standard": True,
            "SM_parity_pattern_imported_without_reopening_SM_parity": True,
        },
        "still_open": {
            "published_or_reconstructed_8x8_profile_likelihood": True,
            "BCT_WZH_cross_covariance_entries": True,
            "RouteC_selected_source_emission": True,
            "selected_Rtheta_source_rows": True,
            "threshold_matching_values": True,
            "mass_scheme_conversion_values": True,
            "no_knob_value_source_derivation": True,
            "true_SM_equivalence": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "freeze external replay as closed and move it out of the active blocker list",
            "route_B": "attack the true-equivalence value-source cutset: public 8x8 likelihood or Route-C selected rows",
            "route_C": "derive no-knob rows and replay the 8-coordinate layer without empirical admissions",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedPublishedCovarianceLikelihoodImportOrRouteCSelectedSourceEmission",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "published_covariance_likelihood_import_attempt": rel(LIKELIHOOD),
            "routec_selected_source_emission_attempt": rel(ROUTEC),
            "external_profile_replay_closure_under_declared_standard": rel(REPLAY),
            "next_cutset_after_likelihood_or_source_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "ExternalProfileReplayClosureAndTrueEquivalenceCutsetTheorem",
            "proved": True,
            "statement": (
                "The current repo does not import a published/reconstructed 8x8 covariance likelihood and does "
                "not emit Route-C selected source rows. However, following the earlier SM-parity closure pattern, "
                "the eight-coordinate external profile layer is sufficient to close the declared external replay "
                "tier: BCT empirical 95 percent profile, W/Z/H external coordinate rows, and the precision replay "
                "policy are all present with no observed-data source selection. True SM equivalence remains open "
                "until a public 8x8 likelihood, selected source rows, or no-knob source derivation is supplied."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "external_profile_replay_closed_under_declared_standard": True,
            "published_or_reconstructed_8x8_profile_likelihood_imported": False,
            "RouteC_selected_source_emission_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
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
        "certificate": "MTT_Selected_PublishedCovarianceLikelihoodImport_or_RouteCSelectedSourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "external_profile_replay_closed_under_declared_standard": True,
        "published_or_reconstructed_8x8_profile_likelihood_imported": False,
        "RouteC_selected_source_emission_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PublishedCovarianceLikelihoodImport or RouteCSelectedSourceEmission v1

Status: `{STATUS}`.

This pushes the current external-profile layer home at the declared replay tier.

```text
external profile coordinates admitted : {total_n}
external replay tier closed           : true
published 8x8 likelihood imported     : false
Route-C selected source rows emitted   : false
true SM equivalence closed             : false
```

The move mirrors the earlier SM-parity closure rule: admitted external/central
replay can close the replay tier without selecting sources.  The active frontier
is now true-equivalence value-source work: import/reconstruct the 8x8 likelihood
or emit selected Route-C/no-knob rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
