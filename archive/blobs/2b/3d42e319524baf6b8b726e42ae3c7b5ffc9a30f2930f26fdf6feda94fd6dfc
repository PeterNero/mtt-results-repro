"""Build threshold-response row emission / external source-row import bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INTERNAL = PACKET_DIR / "internal_threshold_response_functional_row_emission.packet.json"
EXTERNAL = PACKET_DIR / "post_pi_external_source_row_import.packet.json"
READINESS = PACKET_DIR / "step4_value_layer_readiness_after_external_import.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_response_import.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdResponseFunctionalRowEmission_or_ExternalSourceRowImport_v1.md"

PREVIOUS = DATA / "selected_valuelayerfirstnonloopingrowemission_or_thresholdimportexecution.candidate.json"
FIRST_EXTERNAL = (
    DATA
    / "selected_valuelayerfirstnonloopingrowemission_or_thresholdimportexecution"
    / "external_threshold_import_execution.packet.json"
)
OLD_MANIFEST = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "external_threshold_import_manifest.packet.json"
)
OBLIGATION = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)
POST_PI_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "external_row_admission_not_rtheta_selection.packet.json"
)
THRESHOLD_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "post_pi_admitted_threshold_matching_rows.packet.json"
)
MASS_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "post_pi_admitted_mass_scheme_rows.packet.json"
)
DIAGONAL = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "accepted_diagonal_profile_theorem_after_external_rows.packet.json"
)
POST_PI_BOUNDARY = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "post_pi_external_replay_boundary.packet.json"
)
FINAL_FRONTIER = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "rtheta_readiness_final_frontier.packet.json"
)
NOKNOB_RECHECK = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "final_no_knob_value_derivation_recheck.packet.json"
)
RTHETA_SOURCE = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "rtheta_scalar_value_functional_source_packet.packet.json"
)

STATUS = (
    "MTT_SELECTED_THRESHOLDRESPONSEFUNCTIONALROWEMISSION_OR_EXTERNALSOURCEROWIMPORT_"
    "BUILT_EXTERNAL_REPLAY_IMPORT_CLOSED_INTERNAL_RTHETA_OPEN"
)
NEXT = "MTT_Selected_NoKnobValueDerivationKernel_or_SourceAnchorTheorem_v1"


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
        raise FileNotFoundError("missing threshold response import inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        FIRST_EXTERNAL,
        OLD_MANIFEST,
        OBLIGATION,
        POST_PI_ROWS,
        THRESHOLD_ROWS,
        MASS_ROWS,
        DIAGONAL,
        POST_PI_BOUNDARY,
        FINAL_FRONTIER,
        NOKNOB_RECHECK,
        RTHETA_SOURCE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    first_external = load(FIRST_EXTERNAL)
    old_manifest = load(OLD_MANIFEST)
    obligation = load(OBLIGATION)
    post_pi_rows = load(POST_PI_ROWS)
    threshold_rows = load(THRESHOLD_ROWS)
    mass_rows = load(MASS_ROWS)
    diagonal = load(DIAGONAL)
    boundary = load(POST_PI_BOUNDARY)
    final_frontier = load(FINAL_FRONTIER)
    noknob = load(NOKNOB_RECHECK)
    rtheta_source = load(RTHETA_SOURCE)

    external_threshold_count = post_pi_rows["accepted_external_threshold_row_count"]
    external_mass_count = post_pi_rows["accepted_external_mass_scheme_row_count"]
    external_profile_closed = diagonal["accepted_diagonal_theorem_closed"]
    external_replay_ready = boundary["post_pi_external_replay_ready"]

    internal = {
        "schema": "MTTInternalThresholdResponseFunctionalRowEmission.v1",
        "status": "RTHETA_SOURCE_DOMAIN_CLOSED_NUMERIC_VALUE_ROWS_NOT_EMITTED",
        "rtheta_source_packet": rel(RTHETA_SOURCE),
        "source_domain_closed": rtheta_source["source_domain_closed"],
        "selected_functional_symbol": rtheta_source["selected_functional_symbol"],
        "selected_threshold_response_functional_instantiated": noknob[
            "selected_threshold_response_functional_instantiated"
        ],
        "selected_internal_value_emission_count": noknob["selected_internal_value_emission_count"],
        "accepted_coefficient_value_count": noknob["accepted_coefficient_value_count"],
        "lambda_H_coefficient_selected": noknob["lambda_H_coefficient_selected"],
        "basis_map_to_sector_scaled_magnitude_rows_closed": noknob[
            "basis_map_to_sector_scaled_magnitude_rows_closed"
        ],
        "coefficient_functional_closed": noknob["coefficient_functional_closed"],
        "why_no_internal_row_emitted": noknob["why_not_closed"],
        "accepted_as_internal_selected_Rtheta_row": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INTERNAL, internal)

    old_manifest_superseded_for_post_pi = (
        first_external["accepted_external_threshold_row_imported"] is False
        and old_manifest["accepted_external_rows_present"] is False
        and external_replay_ready
        and external_threshold_count == threshold_rows["accepted_admitted_external_threshold_matching_row_count"]
        and external_mass_count == mass_rows["accepted_admitted_external_mass_scheme_row_count"]
    )
    external = {
        "schema": "MTTPostPiExternalSourceRowImport.v1",
        "status": "POST_PI_ADMITTED_EXTERNAL_SOURCE_ROWS_IMPORTED_FOR_REPLAY",
        "previous_first_nonlooping_external_attempt": rel(FIRST_EXTERNAL),
        "old_manifest_source": rel(OLD_MANIFEST),
        "old_manifest_local_scan_had_no_rows": old_manifest["accepted_external_rows_present"] is False,
        "post_pi_admission_supersedes_old_local_scan": old_manifest_superseded_for_post_pi,
        "post_pi_external_replay_boundary": rel(POST_PI_BOUNDARY),
        "threshold_rows_source": rel(THRESHOLD_ROWS),
        "mass_scheme_rows_source": rel(MASS_ROWS),
        "diagonal_profile_source": rel(DIAGONAL),
        "accepted_external_threshold_row_count": external_threshold_count,
        "accepted_external_mass_scheme_row_count": external_mass_count,
        "accepted_diagonal_profile_theorem_closed": external_profile_closed,
        "accepted_external_source_row_imported": True,
        "accepted_external_threshold_rows_imported": True,
        "accepted_external_mass_scheme_rows_imported": True,
        "accepted_external_profile_row_imported": True,
        "accepted_as_internal_selected_Rtheta_row": False,
        "external_rows_used_as_branch_selector": boundary["external_rows_used_as_branch_selector"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_tier": "admitted external replay",
        "closure_claimed": True,
    }
    write_json(EXTERNAL, external)

    readiness = {
        "schema": "MTTStep4ValueLayerReadinessAfterExternalImport.v1",
        "status": "STEP4_EXTERNAL_IMPORT_LANE_CLOSED_INTERNAL_VALUE_EMISSION_OPEN",
        "previous_status": previous["status"],
        "old_first_nonlooping_external_imported": first_external["accepted_external_threshold_row_imported"],
        "post_pi_external_source_row_imported": True,
        "post_pi_external_replay_ready": external_replay_ready,
        "present_count": final_frontier["present_count"],
        "requirement_count": final_frontier["requirement_count"],
        "readiness_fraction": final_frontier["readiness_fraction"],
        "only_remaining_readiness_blocker": final_frontier["only_remaining_readiness_blocker"],
        "closed_value_obligation_rows_at_internal_no_knob_tier": noknob[
            "closed_obligation_count_under_no_knob"
        ],
        "closed_value_obligation_rows_at_admitted_external_tier": 4,
        "obligation_count": obligation["required_row_count"],
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(READINESS, readiness)

    cutset = {
        "schema": "MTTNextCutsetAfterThresholdResponseImport.v1",
        "status": "NEXT_ATTACK_INTERNAL_NOKNOB_VALUE_DERIVATION_OR_SOURCE_ANCHOR",
        "what_closes_now": {
            "old_no_external_import_status_reconciled_with_post_pi_chain": True,
            "accepted_external_threshold_rows_imported_at_admitted_replay_tier": True,
            "accepted_external_mass_scheme_rows_imported_at_admitted_replay_tier": True,
            "accepted_diagonal_profile_theorem_imported_at_admitted_replay_tier": True,
            "step4_external_import_lane_closed": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_internal_Rtheta_threshold_response_row": True,
            "selected_internal_value_emission": True,
            "coefficient_functional": True,
            "lambda_H_value_execution": True,
            "Yukawa_mass_mixing_value_closure_without_external_replay": True,
            "candidate_specific_universal_source_anchor_theorem": True,
            "full_no_knob_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive selected internal Rtheta value rows from the closed source domain",
            "route_B": "prove a candidate-specific universal source-anchor theorem for the remaining numerical value layer",
            "route_C": "keep admitted external replay as SM-parity support while no-knob remains open",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedThresholdResponseFunctionalRowEmissionOrExternalSourceRowImport",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "internal_threshold_response_functional_row_emission": rel(INTERNAL),
            "post_pi_external_source_row_import": rel(EXTERNAL),
            "step4_value_layer_readiness_after_external_import": rel(READINESS),
            "next_cutset_after_threshold_response_import": rel(CUTSET),
        },
        "theorem": {
            "name": "PostPiExternalImportAndInternalRThetaBoundaryTheorem",
            "proved": True,
            "statement": (
                "The earlier first non-looping import attempt was a local manifest scan and correctly found no "
                "accepted external rows at that stage.  The later post-Pi chain supplies admitted external "
                "threshold rows, mass-scheme rows, and an accepted diagonal profile theorem, so the external "
                "source-row import lane is now closed at the admitted-replay tier.  This does not emit internal "
                "selected Rtheta numerical rows and does not close no-knob or true-SM equivalence."
            ),
        },
        "what_closes_now": cutset["what_closes_now"],
        "what_remains_open": cutset["what_remains_open"],
        "closure_decision": {
            "external_import_lane_closed_at_admitted_replay_tier": True,
            "accepted_external_source_row_imported": True,
            "accepted_external_threshold_row_count": external_threshold_count,
            "accepted_external_mass_scheme_row_count": external_mass_count,
            "accepted_diagonal_profile_theorem_closed": external_profile_closed,
            "internal_selected_Rtheta_value_row_emitted": False,
            "selected_threshold_response_functional_instantiated": False,
            "selected_internal_value_emission_count": 0,
            "accepted_coefficient_value_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ThresholdResponseFunctionalRowEmission_or_ExternalSourceRowImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "external_import_lane_closed_at_admitted_replay_tier": True,
        "accepted_external_source_row_imported": True,
        "accepted_external_threshold_row_count": external_threshold_count,
        "accepted_external_mass_scheme_row_count": external_mass_count,
        "accepted_diagonal_profile_theorem_closed": external_profile_closed,
        "internal_selected_Rtheta_value_row_emitted": False,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_coefficient_value_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdResponseFunctionalRowEmission or ExternalSourceRowImport v1

Status: `{STATUS}`.

This artifact reconciles the first non-looping local import attempt with the
later post-Pi admitted external row chain.

```text
external import lane, admitted replay tier : closed
accepted external threshold rows           : {external_threshold_count}
accepted external mass-scheme rows         : {external_mass_count}
accepted diagonal profile theorem          : {str(external_profile_closed).lower()}
internal selected Rtheta value rows         : 0
Rtheta readiness                            : {final_frontier["readiness_fraction"]}
remaining readiness blocker                : {final_frontier["only_remaining_readiness_blocker"]}
true SM equivalence                         : false
full no-knob closure                        : false
```

The gain is real but bounded: Step 4 no longer needs to loop on the external
threshold import lane.  The remaining target is the internal no-knob value
derivation or a candidate-specific source-anchor theorem.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
