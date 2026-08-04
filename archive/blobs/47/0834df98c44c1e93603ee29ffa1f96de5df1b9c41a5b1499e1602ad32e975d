"""Build external-profile replay frozen boundary or true-equivalence value-source cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_externalprofilereplayfrozenboundary_or_trueequivalencevaluesourcecutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BOUNDARY = PACKET_DIR / "external_profile_replay_frozen_boundary.packet.json"
THREE_LANE = PACKET_DIR / "three_lane_true_equivalence_value_source_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_three_lane_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ExternalProfileReplayFrozenBoundary_or_TrueEquivalenceValueSourceCutset_v1.md"

PREVIOUS = DATA / "selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission.candidate.json"
REPLAY = (
    DATA
    / "selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission"
    / "external_profile_replay_closure_under_declared_standard.packet.json"
)
LIKELIHOOD = (
    DATA
    / "selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission"
    / "published_covariance_likelihood_import_attempt.packet.json"
)
ROUTEC_ATTEMPT = (
    DATA
    / "selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission"
    / "routec_selected_source_emission_attempt.packet.json"
)
BRIDGE = (
    DATA
    / "selected_externalprofiletofullcovariancebridge_or_selectedsourcerows"
    / "external_profile_full_covariance_bridge.packet.json"
)
ROUTEC_SELECTOR = DATA / "selected_routec_source_selector_and_basis_theorem.candidate.json"
RTHETA_PROVENANCE = DATA / "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure.candidate.json"
VALUE_KERNEL = DATA / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest.candidate.json"
NO_KNOB_AUDIT = DATA / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation.candidate.json"

STATUS = (
    "MTT_SELECTED_EXTERNALPROFILEREPLAYFROZENBOUNDARY_OR_TRUEEQUIVALENCEVALUESOURCECUTSET_"
    "BUILT_THREE_LANES_ATTEMPTED_EXTERNAL_REPLAY_FROZEN"
)
NEXT = "MTT_Selected_Public8x8LikelihoodSearch_or_RouteCSourceEmissionExecution_v1"


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
        raise FileNotFoundError("missing three-lane cutset sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        REPLAY,
        LIKELIHOOD,
        ROUTEC_ATTEMPT,
        BRIDGE,
        ROUTEC_SELECTOR,
        RTHETA_PROVENANCE,
        VALUE_KERNEL,
        NO_KNOB_AUDIT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    replay = load(REPLAY)
    likelihood = load(LIKELIHOOD)
    routec_attempt = load(ROUTEC_ATTEMPT)
    bridge = load(BRIDGE)
    routec_selector = load(ROUTEC_SELECTOR)
    rtheta_provenance = load(RTHETA_PROVENANCE)
    value_kernel = load(VALUE_KERNEL)
    no_knob = load(NO_KNOB_AUDIT)

    target = bridge["full_covariance_target"]
    external_refs = [
        {
            "id": "Huang-Zhou-2020-running-masses",
            "url": "https://arxiv.org/abs/2009.04851",
            "use": "BCT running-mass/table/correlation provenance; does not supply the combined 8x8 BCT-WZH likelihood.",
        },
        {
            "id": "Buttazzo-et-al-2013-near-criticality",
            "url": "https://arxiv.org/abs/1307.3536",
            "use": "Weak-scale lambda/yt/gauge formula inspiration; does not supply the combined BCT-WZH cross-covariance block.",
        },
    ]

    boundary = {
        "schema": "MTTExternalProfileReplayFrozenBoundary.v1",
        "status": "EXTERNAL_PROFILE_REPLAY_CLOSED_DO_NOT_REOPEN_AS_ACTIVE_BLOCKER",
        "replay_source": rel(REPLAY),
        "boundary_locks": True,
        "closed_tiers": {
            "SM_parity_replay_under_declared_standard": replay["SM_parity_closed"],
            "external_profile_replay_under_declared_standard": replay[
                "external_profile_replay_closed_under_declared_standard"
            ],
        },
        "external_profile_coordinate_count": replay["external_profile_coordinate_count"],
        "guardrails": {
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "full_covariance_profile_likelihood_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "reopen_policy": {
            "may_reopen_external_profile_replay_only_if": [
                "a verifier regression makes the replay audit fail",
                "a replay row is shown to have selected a source or branch using observed values",
                "the declared replay/admission standard itself is changed",
            ],
            "must_not_reopen_external_profile_replay_because": [
                "true SM equivalence is still open",
                "public 8x8 likelihood import is still open",
                "Route-C selected source emission is still open",
                "no-knob value-source derivation is still open",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(BOUNDARY, boundary)

    routec_calc = routec_selector["calculation"]
    three_lane = {
        "schema": "MTTThreeLaneTrueEquivalenceValueSourceAttempt.v1",
        "status": "ALL_THREE_LANES_ATTEMPTED_NONE_CLOSE_TRUE_EQUIVALENCE",
        "lane_A_public_8x8_likelihood": {
            "attempted": True,
            "external_refs_checked": external_refs,
            "fixed_target_shape": likelihood["fixed_target_shape"],
            "fixed_target_symmetric_entries": likelihood["fixed_target_symmetric_entries"],
            "missing_BCT_WZH_cross_covariance_entries": likelihood[
                "missing_BCT_WZH_cross_covariance_entries"
            ],
            "published_or_reconstructed_profile_likelihood_imported": likelihood[
                "published_or_reconstructed_profile_likelihood_imported"
            ],
            "accepted_as_full_profile_likelihood": likelihood["accepted_as_full_profile_likelihood"],
            "result": "No combined public/reconstructed 8x8 BCT-WZH likelihood is present locally or identified by the checked literature route.",
        },
        "lane_B_routec_selected_source_rows": {
            "attempted": True,
            "minimal_internal_missing_object": routec_attempt["minimal_internal_missing_object"],
            "selected_routec_galerkin_solve_closed": routec_attempt["selected_routec_galerkin_solve_closed"],
            "honest_root_all_pass": routec_attempt["honest_root_all_pass"],
            "accepted_selected_BCT_source_row_count": routec_attempt["accepted_selected_BCT_source_row_count"],
            "formal_lift_lower_validators_all_pass": routec_calc["formal_lift_lower_validators_all_pass"],
            "formal_lift_de_response_promotion_passes": routec_calc[
                "formal_lift_de_response_promotion_passes"
            ],
            "basis_skeleton_closed": routec_calc["basis_skeleton_verdict"]["closes_basis_skeleton"],
            "basis_protocol_values_open": routec_calc["basis_protocol_values_open"],
            "rtheta_value_evaluator_readiness_present_count": rtheta_provenance["closure_decision"][
                "value_evaluator_readiness_present_count"
            ],
            "rtheta_value_evaluator_readiness_required_count": rtheta_provenance["closure_decision"][
                "value_evaluator_readiness_required_count"
            ],
            "result": "Route-C is algebraically close under formal lift and has a basis skeleton, but honest selected-source and basis/operator values are still absent.",
        },
        "lane_C_no_knob_value_source_rows": {
            "attempted": True,
            "obligation_kernel_closed": value_kernel["closure_decision"]["obligation_kernel_closed"],
            "import_manifest_closed": value_kernel["closure_decision"]["import_manifest_closed"],
            "selected_dynamic_value_source_rows_emitted": value_kernel["closure_decision"][
                "selected_dynamic_value_source_rows_emitted"
            ],
            "accepted_external_threshold_rows_imported": value_kernel["closure_decision"][
                "accepted_external_threshold_rows_imported"
            ],
            "no_knob_value_derivation_closed": no_knob["closure_decision"][
                "no_knob_value_derivation_closed"
            ],
            "accepted_threshold_mass_scheme_source_layer_closed": no_knob["closure_decision"][
                "accepted_threshold_mass_scheme_source_layer_closed"
            ],
            "result": "The typed obligations and import manifest are closed, but no selected/no-knob value-source rows are emitted.",
        },
        "combined_decision": {
            "external_profile_replay_frozen": True,
            "true_SM_equivalence_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "no_knob_value_source_derivation_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(THREE_LANE, three_lane)

    cutset = {
        "schema": "MTTNextCutsetAfterThreeLaneAttempt.v1",
        "status": "NEXT_ATTACK_PUBLIC_8X8_SEARCH_OR_ROUTEC_EMISSION_EXECUTION",
        "closed_now": {
            "external_profile_replay_frozen_boundary": True,
            "lane_A_public_8x8_likelihood_attempted": True,
            "lane_B_routec_selected_source_rows_attempted": True,
            "lane_C_no_knob_value_source_rows_attempted": True,
            "three_lane_true_equivalence_cutset_sharpened": True,
        },
        "still_open": {
            "public_or_reconstructed_8x8_likelihood": True,
            "BCT_WZH_cross_covariance_entries": True,
            "selected_routec_basis_operator_values": True,
            "selected_Rtheta_source_rows": True,
            "selected_dynamic_value_source_rows": True,
            "threshold_matching_values": True,
            "mass_scheme_conversion_values": True,
            "no_knob_value_source_derivation": True,
            "true_SM_equivalence": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "perform a dedicated public-data search/reconstruction for the 8x8 covariance likelihood",
            "route_B": "execute Route-C selected basis/operator value emission until honest flags are theorem-derived",
            "route_C": "fill the first typed no-knob value-source row from the obligation kernel",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedExternalProfileReplayFrozenBoundaryOrTrueEquivalenceValueSourceCutset",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "external_profile_replay_frozen_boundary": rel(BOUNDARY),
            "three_lane_true_equivalence_value_source_attempt": rel(THREE_LANE),
            "next_cutset_after_three_lane_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "ExternalProfileReplayFrozenBoundaryAndThreeLaneCutsetTheorem",
            "proved": True,
            "statement": (
                "All three requested true-equivalence lanes can be attempted from the current frontier. "
                "The public 8x8 likelihood lane fixes the exact target but imports no combined likelihood; "
                "the Route-C lane has formal-lift algebra and a basis skeleton but no honest selected-source "
                "basis/operator values; the no-knob lane has a typed obligation kernel and import manifest "
                "but emits no selected value-source row. Therefore external profile replay is frozen as closed "
                "under the declared admission standard, while true SM equivalence is reduced to the three-lane "
                "value-source cutset."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "external_profile_replay_frozen_boundary_closed": True,
            "all_three_lanes_attempted": True,
            "public_or_reconstructed_8x8_likelihood_imported": False,
            "RouteC_selected_source_emission_closed": False,
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
        "certificate": "MTT_Selected_ExternalProfileReplayFrozenBoundary_or_TrueEquivalenceValueSourceCutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "external_profile_replay_frozen_boundary_closed": True,
        "all_three_lanes_attempted": True,
        "public_or_reconstructed_8x8_likelihood_imported": False,
        "RouteC_selected_source_emission_closed": False,
        "no_knob_value_source_derivation_closed": False,
        "true_SM_equivalence_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ExternalProfileReplayFrozenBoundary or TrueEquivalenceValueSourceCutset v1

Status: `{STATUS}`.

All three requested lanes were tried.

```text
external replay frozen boundary closed : true
public/reconstructed 8x8 likelihood     : false
Route-C selected source rows            : false
no-knob value-source rows               : false
true SM equivalence                     : false
```

The external replay tier is now frozen closed under the declared admission
standard.  The active problem is the three-lane true-equivalence value-source
cutset: public 8x8 likelihood, Route-C selected source emission, or no-knob
value-source row derivation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
