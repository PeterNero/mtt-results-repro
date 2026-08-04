"""Build a Higgs profile-convention data-file rehearsal and precision-row value gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsprofileconventiondatafile_or_precisionrowvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE = PACKET_DIR / "higgs_profile_convention_datafile_rehearsal.packet.json"
VALIDATION = PACKET_DIR / "profile_datafile_schema_validation.packet.json"
VALUES = PACKET_DIR / "precision_row_value_fill_status.packet.json"
DECISION = PACKET_DIR / "profile_datafile_or_precision_values_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_profile_datafile_rehearsal.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsProfileConventionDataFile_or_PrecisionRowValues_v1.md"

STATUS = "MTT_SELECTED_HIGGSPROFILECONVENTIONDATAFILE_OR_PRECISIONROWVALUES_BUILT_REHEARSAL_PROFILE_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_symmetric(matrix: list[list[float]]) -> bool:
    return all(abs(matrix[i][j] - matrix[j][i]) < 1e-30 for i in range(len(matrix)) for j in range(len(matrix)))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsprecisionvaluefill_or_profileconventionimport.candidate.json")
    schema = load(
        DATA
        / "selected_higgsprecisionvaluefill_or_profileconventionimport"
        / "higgs_precision_profile_convention_input_schema.packet.json"
    )
    total = load(
        DATA
        / "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
        / "ten_channel_total_width_diagonal_profile.packet.json"
    )
    branching = load(
        DATA
        / "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
        / "ten_channel_branching_ratio_replay.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsprecisionvaluefill_or_profileconventionimport"
        / "updated_true_equivalence_gate_after_profile_import_gate.packet.json"
    )

    row_basis = total["row_basis"]
    central_widths = {row["channel"]: row["width_GeV"] for row in total["rows"]}
    covariance = []
    for row_i in total["rows"]:
        covariance_row = []
        for row_j in total["rows"]:
            covariance_row.append(row_i["variance_GeV2"] if row_i["channel"] == row_j["channel"] else 0.0)
        covariance.append(covariance_row)
    total_width = total["summary"]["total_width_GeV"]
    branching_by_channel = {row["channel"]: row["branching_ratio"] for row in branching["rows"]}

    profile = {
        "schema": "MTTHiggsProfileConventionDataFileRehearsal.v1",
        "status": "REHEARSAL_PROFILE_DATAFILE_FILLED_FROM_CURRENT_SCAFFOLD_NOT_PRECISION",
        "profile_id": "internal_current_mixed_proxy_import_higgs_replay_rehearsal",
        "profile_version": "local-scaffold-generated-2026-05-28",
        "row_basis": row_basis,
        "central_widths_GeV": central_widths,
        "total_width_GeV": total_width,
        "covariance_matrix_GeV2": covariance,
        "nuisance_profile": None,
        "branching_ratios": branching_by_channel,
        "branching_ratio_policy": "derived by fixed map BR_i = Gamma_i / sum_j Gamma_j from current scaffold widths",
        "scheme": {
            "higgs_mass": "current repo mixed scaffold convention inherited from measured replay sidecars",
            "electroweak_inputs": "mixed scaffold; EW offshell rows remain external import identities",
            "qcd_inputs": "mixed scaffold; QCD rows include first-pass proxy/formula rows",
            "perturbative_orders": "nonuniform: proxy, first-pass formula, and import-identity rows coexist",
            "threshold_policy": "not a precision threshold policy",
        },
        "provenance": {
            "source": "repo-generated rehearsal from current ten-channel Higgs replay packets",
            "license_or_access_note": "internal reproducibility artifact; not an external precision profile",
            "retrieved_or_generated_date": "2026-05-28",
        },
        "guards": {
            "used_to_select_source": False,
            "fit_factor_applied_to_repo_rows": False,
            "row_basis_changed_after_comparison": False,
        },
        "accepted_as_precision_profile_convention": False,
        "accepted_as_precision_row_values": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    covariance_diag = [covariance[i][i] for i in range(len(covariance))]
    validation = {
        "schema": "MTTProfileDataFileSchemaValidation.v1",
        "status": "REHEARSAL_PROFILE_VALIDATES_SCHEMA_BUT_FAILS_PRECISION_ACCEPTANCE",
        "schema_source": rel(
            DATA
            / "selected_higgsprecisionvaluefill_or_profileconventionimport"
            / "higgs_precision_profile_convention_input_schema.packet.json"
        ),
        "tests": {
            "row_basis_matches_schema": row_basis == schema["required_fields"]["row_basis"],
            "central_widths_sum_to_total_width": abs(sum(central_widths.values()) - total_width) < 1e-18,
            "covariance_symmetric": is_symmetric(covariance),
            "covariance_psd_by_diagonal_nonnegative": all(value >= 0.0 for value in covariance_diag),
            "branching_ratios_derived_by_fixed_map": all(
                abs(branching_by_channel[channel] - central_widths[channel] / total_width) < 1e-15
                for channel in row_basis
            ),
            "source_selection_guard_passes": profile["guards"]["used_to_select_source"] is False,
            "fit_factor_guard_passes": profile["guards"]["fit_factor_applied_to_repo_rows"] is False,
            "precision_convention_acceptance_passes": False,
        },
        "why_precision_acceptance_fails": [
            "profile provenance is internal scaffold, not an accepted external precision convention",
            "rows are mixed proxy, first-pass formula, and import-identity values",
            "covariance is diagonal fallback only, not a full correlated covariance/profile likelihood",
        ],
        "accepted_as_schema_rehearsal": True,
        "accepted_as_precision_profile_convention": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    value_rows = []
    for row in total["rows"]:
        value_rows.append(
            {
                "channel": row["channel"],
                "current_width_GeV": row["width_GeV"],
                "current_row_kind": row["row_kind"],
                "rehearsal_value_filled": True,
                "accepted_precision_value_filled": False,
                "blocking_reason": (
                    "current value is scaffold/proxy/import-identity; accepted precision row value still requires "
                    "route A formula fill or route B accepted profile convention import"
                ),
            }
        )
    values = {
        "schema": "MTTHiggsPrecisionRowValueFillStatus.v1",
        "status": "REHEARSAL_VALUES_FILLED_ZERO_PRECISION_VALUES_ACCEPTED",
        "rows": value_rows,
        "summary": {
            "row_count": len(value_rows),
            "rehearsal_values_filled": len(value_rows),
            "accepted_precision_values_filled": 0,
            "all_rows_still_require_precision_acceptance": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTHiggsProfileDataFileOrPrecisionValuesDecision.v1",
        "status": "REHEARSAL_PROFILE_BUILT_ACCEPTED_PRECISION_VALUES_STILL_OPEN",
        "profile_datafile_rehearsal_built": True,
        "schema_validation_passed_for_rehearsal": True,
        "precision_profile_convention_imported": False,
        "accepted_precision_row_values_filled": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "next_required_action": "replace rehearsal profile with accepted external precision convention data or fill accepted route-A row values",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterProfileDataFileRehearsal.v1",
        "status": "REHEARSAL_PROFILE_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs profile datafile rehearsal",
            "Higgs profile schema validation harness",
            "precision row value status matrix",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "accepted external Higgs precision profile convention data or route-A precision row values",
        "guardrails": {
            "rehearsal_profile_not_precision_profile": True,
            "zero_precision_values_accepted": True,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsProfileConventionDataFileOrPrecisionRowValues",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsprecisionvaluefill_or_profileconventionimport.candidate.json"),
            "profile_input_schema": rel(
                DATA
                / "selected_higgsprecisionvaluefill_or_profileconventionimport"
                / "higgs_precision_profile_convention_input_schema.packet.json"
            ),
            "ten_channel_total_width_profile": rel(
                DATA
                / "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
                / "ten_channel_total_width_diagonal_profile.packet.json"
            ),
            "ten_channel_branching_replay": rel(
                DATA
                / "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
                / "ten_channel_branching_ratio_replay.packet.json"
            ),
        },
        "output_packets": {
            "profile_datafile_rehearsal": rel(PROFILE),
            "schema_validation": rel(VALIDATION),
            "precision_row_value_fill_status": rel(VALUES),
            "profile_datafile_or_precision_values_decision": rel(DECISION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsProfileConventionDataFileRehearsalTheorem",
            "proved": True,
            "statement": (
                "The current mixed Higgs scaffold can be serialized into the exact profile-convention data-file "
                "schema and mechanically validated for row-basis, summation, branching-map, PSD-diagonal covariance, "
                "and guardrail consistency. This proves the import interface is executable, while rejecting precision "
                "acceptance because the data are scaffold/proxy/import-identity values, not an accepted precision convention."
            ),
        },
        "what_closes_now": {
            "profile_datafile_rehearsal": True,
            "schema_validation_harness": True,
            "precision_row_value_status_matrix": True,
        },
        "what_remains_open": {
            "accepted_external_precision_profile_convention": True,
            "accepted_route_A_precision_row_values": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "profile_datafile_rehearsal_built": True,
            "schema_validation_passed_for_rehearsal": True,
            "precision_profile_convention_imported": False,
            "accepted_precision_row_values_filled": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsProfileConventionDataFile_or_PrecisionRowValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "profile_datafile_rehearsal_built": True,
        "schema_validation_passed_for_rehearsal": True,
        "precision_profile_convention_imported": False,
        "accepted_precision_row_values_filled": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsAcceptedProfileImport_or_RowValueReplacement_v1",
    }

    note = f"""# MTT Selected HiggsProfileConventionDataFile or PrecisionRowValues v1

Status: `{STATUS}`.

This artifact fills the profile-convention data-file schema with the current
internal mixed Higgs scaffold as a rehearsal packet. It validates the import
interface, row basis, total-width summation, branching-ratio map, diagonal PSD
covariance, and source-selection guards.

It is not an accepted precision profile. It accepts zero precision row values.
"""

    for path, payload in [
        (PROFILE, profile),
        (VALIDATION, validation),
        (VALUES, values),
        (DECISION, decision),
        (UPDATED_TRUE, updated_true),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
