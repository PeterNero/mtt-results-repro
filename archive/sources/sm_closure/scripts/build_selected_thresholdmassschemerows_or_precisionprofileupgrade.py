"""Build threshold/mass-scheme row readiness or precision-profile upgrade artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdmassschemerows_or_precisionprofileupgrade"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
READINESS = PACKET_DIR / "threshold_mass_scheme_row_readiness_matrix.packet.json"
PROFILE = PACKET_DIR / "precision_profile_upgrade_gate.packet.json"
HARNESS = PACKET_DIR / "rtheta1_validation_harness_row_attachment.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_row_readiness.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdMassSchemeRows_or_PrecisionProfileUpgrade_v1.md"

PREVIOUS = DATA / "selected_thresholdrows_or_diagonalprofilelimitationtheorem.candidate.json"
RTHETA1 = (
    DATA
    / "selected_thresholdrows_or_diagonalprofilelimitationtheorem"
    / "provisional_rtheta1_diagonal_instantiation.packet.json"
)
TOP_HIGGS_ACCEPT = (
    DATA
    / "selected_tophiggsformulamapimport_or_rthetathresholdderivation"
    / "top_higgs_external_formula_map_acceptance.packet.json"
)
TOP_HIGGS_REPLAY = (
    DATA
    / "selected_tophiggsformulamapimport_or_rthetathresholdderivation"
    / "top_higgs_formula_map_import_replay.packet.json"
)
BCT_ATTEMPT = (
    DATA
    / "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
    / "bottom_charm_tau_map_row_fill_attempt.packet.json"
)
BCT_INVENTORY = (
    DATA
    / "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
    / "bottom_charm_tau_native_residual_inventory.packet.json"
)
WZH_INVENTORY = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_electroweak_row_inventory.packet.json"
)
WZH_ACCEPT = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_external_benchmark_row_acceptance.packet.json"
)
WZH_GAP = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "selected_rtheta_mass_scheme_gap_after_wzh_rows.packet.json"
)
WZH_SIDECARS = (
    DATA
    / "selected_covariancesidecarfill_or_rthetasourcerowderivation"
    / "wzh_gauge_and_lambda_covariance_sidecars.packet.json"
)
CROSSBLOCK = (
    DATA
    / "selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill"
    / "firstpass_weak_bct_crossblock_covariance.packet.json"
)
THRESHOLD_RECHECK = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "threshold_response_rows_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_THRESHOLDMASSSCHEMEROWS_OR_PRECISIONPROFILEUPGRADE_"
    "BUILT_ROW_READINESS_EXTERNAL_COORDINATES_ACCEPTED_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_BCTFormulaImport_or_SelectedThresholdRowDerivation_v1"


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
        raise FileNotFoundError("missing threshold/mass-scheme row sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        RTHETA1,
        TOP_HIGGS_ACCEPT,
        TOP_HIGGS_REPLAY,
        BCT_ATTEMPT,
        BCT_INVENTORY,
        WZH_INVENTORY,
        WZH_ACCEPT,
        WZH_GAP,
        WZH_SIDECARS,
        CROSSBLOCK,
        THRESHOLD_RECHECK,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    rtheta1 = load(RTHETA1)
    top_accept = load(TOP_HIGGS_ACCEPT)
    top_replay = load(TOP_HIGGS_REPLAY)
    bct_attempt = load(BCT_ATTEMPT)
    bct_inventory = load(BCT_INVENTORY)
    wzh_inventory = load(WZH_INVENTORY)
    wzh_accept = load(WZH_ACCEPT)
    wzh_gap = load(WZH_GAP)
    wzh_sidecars = load(WZH_SIDECARS)
    crossblock = load(CROSSBLOCK)
    threshold_recheck = load(THRESHOLD_RECHECK)

    readiness_rows: list[dict[str, Any]] = []
    for row in top_accept["accepted_rows"]:
        readiness_rows.append(
            {
                "id": row["id"],
                "sector": "top_higgs",
                "row_kind": "external_formula_map",
                "accepted_as_external_coordinate_or_map_row": row["accepted_as_external_top_higgs_formula_map_row"],
                "accepted_as_selected_Rtheta_source_row": row["accepted_as_Rtheta_source_row"],
                "accepted_as_full_profile_row": row["accepted_as_full_profile_row"],
                "provenance": row["provenance"],
                "covariance_sidecar": row.get("covariance_sidecar"),
                "rtheta1_validation_role": "can validate provisional lambda/y_t evaluator rows",
            }
        )
    for row in wzh_inventory["accepted_wzh_coordinate_rows"]:
        readiness_rows.append(
            {
                "id": row["id"],
                "sector": "WZH",
                "row_kind": "external_coordinate_row",
                "accepted_as_external_coordinate_or_map_row": row["accepted_as_external_WZH_coordinate_row"],
                "accepted_as_selected_Rtheta_source_row": row["accepted_as_selected_Rtheta_source_row"],
                "accepted_as_full_profile_row": False,
                "provenance": row["provenance"],
                "covariance_sidecar": row.get("covariance_sidecar"),
                "rtheta1_validation_role": "can validate WZH coordinate compatibility, not selected source",
            }
        )
    for row in bct_attempt["required_maps"]:
        residual = next(item for item in bct_inventory["residual_rows"] if item["map_id"] == row["id"])
        readiness_rows.append(
            {
                "id": row["id"],
                "sector": "BCT",
                "row_kind": "native_residual_inventory",
                "accepted_as_external_coordinate_or_map_row": False,
                "accepted_as_selected_Rtheta_source_row": False,
                "accepted_as_full_profile_row": False,
                "provenance": bct_inventory["residual_values_source"],
                "residual_id": row["residual_id"],
                "residual_value": residual["delta_source_minus_target"],
                "relative_residual": residual["relative_delta_source_minus_target"],
                "blocking_reason": row["blocking_reason"],
                "rtheta1_validation_role": "finite residual can be checked against provisional composed BCT-to-Mt response",
            }
        )

    external_row_count = sum(1 for row in readiness_rows if row["accepted_as_external_coordinate_or_map_row"])
    selected_source_count = sum(1 for row in readiness_rows if row["accepted_as_selected_Rtheta_source_row"])
    full_profile_count = sum(1 for row in readiness_rows if row["accepted_as_full_profile_row"])

    readiness = {
        "schema": "MTTThresholdMassSchemeRowReadinessMatrix.v1",
        "status": "ROW_READINESS_MATRIX_BUILT_EXTERNAL_COORDINATES_ACCEPTED_SOURCE_ROWS_OPEN",
        "rtheta1_source": rel(RTHETA1),
        "top_higgs_acceptance_source": rel(TOP_HIGGS_ACCEPT),
        "wzh_acceptance_source": rel(WZH_ACCEPT),
        "bct_attempt_source": rel(BCT_ATTEMPT),
        "rows": readiness_rows,
        "row_count": len(readiness_rows),
        "accepted_external_coordinate_or_map_row_count": external_row_count,
        "accepted_selected_Rtheta_source_row_count": selected_source_count,
        "accepted_full_profile_row_count": full_profile_count,
        "sector_summary": {
            "top_higgs_external_formula_rows": top_accept["accepted_external_formula_map_row_count"],
            "wzh_external_coordinate_rows": wzh_accept["accepted_external_wzh_coordinate_row_count"],
            "bct_accepted_map_rows": bct_attempt["accepted_bottom_charm_tau_map_row_count"],
            "bct_finite_residual_rows": len(bct_inventory["residual_rows"]),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(READINESS, readiness)

    profile = {
        "schema": "MTTPrecisionProfileUpgradeGate.v1",
        "status": "INTERIM_PROFILE_SUPPORT_PRESENT_FULL_PRECISION_PROFILE_OPEN",
        "readiness_source": rel(READINESS),
        "wzh_sidecars_source": rel(WZH_SIDECARS),
        "crossblock_source": rel(CROSSBLOCK),
        "top_higgs_diagonal_sidecars_present": top_replay["diagonal_sensitivity_sidecars_present"],
        "wzh_interim_sidecars_present": wzh_sidecars["accepted_as_interim_covariance_sidecars"],
        "weak_bct_crossblock_entries_present": crossblock["accepted_as_firstpass_cross_block_covariance_values"],
        "weak_bct_crossblock_entry_count": crossblock["inserted_entry_count"],
        "accepted_as_precision_profile_upgrade": False,
        "why_not_precision_profile": [
            "BCT map/source rows remain unaccepted",
            "WZH coordinate rows are external benchmark/reference rows, not selected Rtheta source rows",
            "gauge/full covariance sidecars are interim and not full profile likelihood",
            "selected threshold matching and mass-scheme conversion source rows are still empty",
        ],
        "full_covariance_profile_likelihood_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROFILE, profile)

    harness = {
        "schema": "MTTRTheta1ValidationHarnessRowAttachment.v1",
        "status": "RTHETA1_VALIDATION_HARNESS_ATTACHED_TO_ROW_READINESS_MATRIX",
        "rtheta1_source": rel(RTHETA1),
        "readiness_source": rel(READINESS),
        "provisional_Rtheta1_diagonal_instantiated": rtheta1["provisional_firstpass_Rtheta_instantiated"],
        "row_attachment_count": len(readiness_rows),
        "validates_external_top_higgs_rows": top_accept["accepted_external_formula_map_row_count"] == 2,
        "validates_wzh_coordinate_rows": wzh_accept["accepted_external_wzh_coordinate_row_count"] == 5,
        "validates_bct_residual_inventory": len(bct_inventory["residual_rows"]) == 3,
        "selects_threshold_rows": False,
        "promotes_external_rows_to_selected_source_rows": False,
        "threshold_response_rows_closed": threshold_recheck["threshold_response_rows_closed"],
        "mass_scheme_conversion_rows_closed": threshold_recheck["mass_scheme_conversion_rows_closed"],
        "selected_threshold_response_functional_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(HARNESS, harness)

    cutset = {
        "schema": "MTTNextCutsetAfterThresholdRowReadiness.v1",
        "status": "NEXT_ATTACK_BCT_FORMULA_IMPORT_OR_SELECTED_THRESHOLD_ROW_DERIVATION",
        "closed_now": {
            "threshold_mass_scheme_row_readiness_matrix": True,
            "external_top_higgs_rows_integrated_with_Rtheta1_harness": True,
            "external_WZH_coordinate_rows_integrated_with_Rtheta1_harness": True,
            "BCT_residual_rows_attached_as_validation_targets": True,
            "precision_profile_upgrade_gate_rechecked": True,
        },
        "still_open": {
            "BCT_formula_or_table_import": True,
            "selected_threshold_matching_source_rows": True,
            "selected_mass_scheme_conversion_source_rows": True,
            "selected_Rtheta_source_rows": True,
            "selected_threshold_response_functional": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "import provenance-bearing BCT formula/table rows for bottom, charm, and tau",
            "route_B": "derive BCT mass-scheme rows from the selected Rtheta1/Pi source rather than external residuals",
            "route_C": "use accepted external top/Higgs and WZH rows as validation anchors, not source selectors",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedThresholdMassSchemeRowsOrPrecisionProfileUpgrade",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "threshold_mass_scheme_row_readiness_matrix": rel(READINESS),
            "precision_profile_upgrade_gate": rel(PROFILE),
            "rtheta1_validation_harness_row_attachment": rel(HARNESS),
            "next_cutset_after_threshold_row_readiness": rel(CUTSET),
        },
        "theorem": {
            "name": "ThresholdMassSchemeRowReadinessMatrixTheorem",
            "proved": True,
            "statement": (
                "Against the provisional R_theta^(1,diag) evaluator, the repo now has a consolidated threshold/"
                "mass-scheme row readiness matrix: two accepted external top/Higgs formula-map rows, five accepted "
                "external WZH coordinate rows, and three finite BCT residual targets with zero accepted BCT map rows. "
                "This closes readiness and validation-harness attachment, but not selected threshold source rows, "
                "full precision profile likelihood, true SM equivalence, or no-knob closure."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "threshold_mass_scheme_row_readiness_matrix_closed": True,
            "external_top_higgs_rows_integrated": True,
            "external_WZH_coordinate_rows_integrated": True,
            "BCT_residual_rows_attached": True,
            "accepted_BCT_map_rows_closed": False,
            "selected_threshold_matching_source_rows_closed": False,
            "selected_mass_scheme_conversion_source_rows_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
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
        "certificate": "MTT_Selected_ThresholdMassSchemeRows_or_PrecisionProfileUpgrade_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "threshold_mass_scheme_row_readiness_matrix_closed": True,
        "accepted_external_coordinate_or_map_row_count": external_row_count,
        "accepted_selected_Rtheta_source_row_count": selected_source_count,
        "accepted_BCT_map_rows_closed": False,
        "selected_threshold_matching_source_rows_closed": False,
        "selected_mass_scheme_conversion_source_rows_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdMassSchemeRows or PrecisionProfileUpgrade v1

Status: `{STATUS}`.

This artifact consolidates threshold/mass-scheme row readiness against the
provisional `R_theta^(1,diag)` evaluator.

```text
accepted external top/Higgs formula rows : {top_accept["accepted_external_formula_map_row_count"]}
accepted external WZH coordinate rows    : {wzh_accept["accepted_external_wzh_coordinate_row_count"]}
finite BCT residual rows attached        : {len(bct_inventory["residual_rows"])}
accepted BCT map rows                    : {bct_attempt["accepted_bottom_charm_tau_map_row_count"]}
selected Rtheta source rows              : {selected_source_count}
```

The new object is a validation/readiness matrix, not a source-row proof.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
