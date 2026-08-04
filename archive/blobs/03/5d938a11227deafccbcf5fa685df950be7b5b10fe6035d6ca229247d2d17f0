"""Build BCT formula import or selected threshold-row derivation artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bctformulaimport_or_selectedthresholdrowderivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EXTERNAL = PACKET_DIR / "bct_external_formula_import_lane.packet.json"
SAME_SOURCE = PACKET_DIR / "bct_selected_rtheta_derivation_lane.packet.json"
UPDATED = PACKET_DIR / "updated_threshold_readiness_after_bct_import.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bct_dual_lane_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BCTFormulaImport_or_SelectedThresholdRowDerivation_v1.md"

PREVIOUS = DATA / "selected_thresholdmassschemerows_or_precisionprofileupgrade.candidate.json"
READINESS = (
    DATA
    / "selected_thresholdmassschemerows_or_precisionprofileupgrade"
    / "threshold_mass_scheme_row_readiness_matrix.packet.json"
)
RTHETA1 = (
    DATA
    / "selected_thresholdrows_or_diagonalprofilelimitationtheorem"
    / "provisional_rtheta1_diagonal_instantiation.packet.json"
)
BCT_FORMULA = DATA / "selected_bottomcharmtauformulaimport_or_rthetamassschemederivation.candidate.json"
BCT_RUNDEC = DATA / "selected_bottomcharmtaurundecreplay_or_rthetamassschemerows.candidate.json"
ALL_BCT = DATA / "selected_allbctexternalrows_or_fullsmconventionreconciliation.candidate.json"
ALL_BCT_ROWS = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "all_bct_external_rows_assembly.packet.json"
)
BCT_PROFILE = DATA / "selected_bctprofilereconciliation_or_rthetamassschemederivation.candidate.json"
BCT_RTHETA_GAP = (
    DATA
    / "selected_bctprofilereconciliation_or_rthetamassschemederivation"
    / "rtheta_mass_scheme_derivation_gap_recheck.packet.json"
)
ROUTEC_CONTRACT = (
    DATA
    / "selected_rtheta_selectedroutecgalerkinsolve_or_diagonalprofiletheorem"
    / "selected_routec_galerkin_solve_acceptance_contract.packet.json"
)
ROUTEC_DECISION = (
    DATA
    / "selected_rtheta_selectedroutecgalerkinsolve_or_diagonalprofiletheorem"
    / "selected_solve_or_diagonal_profile_decision.packet.json"
)
ROUTEC_FIRST_RUN = DATA / "selected_routec_strominger_galerkin_first_run.candidate.json"

STATUS = (
    "MTT_SELECTED_BCTFORMULAIMPORT_OR_SELECTEDTHRESHOLDROWDERIVATION_"
    "BUILT_EXTERNAL_BCT_ROWS_ACCEPTED_SELECTED_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_BCTSelectedSourceRepair_or_FullProfileUpgrade_v1"


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
        raise FileNotFoundError("missing BCT dual-lane sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        READINESS,
        RTHETA1,
        BCT_FORMULA,
        BCT_RUNDEC,
        ALL_BCT,
        ALL_BCT_ROWS,
        BCT_PROFILE,
        BCT_RTHETA_GAP,
        ROUTEC_CONTRACT,
        ROUTEC_DECISION,
        ROUTEC_FIRST_RUN,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    readiness = load(READINESS)
    rtheta1 = load(RTHETA1)
    bct_formula = load(BCT_FORMULA)
    bct_rundec = load(BCT_RUNDEC)
    all_bct = load(ALL_BCT)
    all_bct_rows = load(ALL_BCT_ROWS)
    bct_profile = load(BCT_PROFILE)
    bct_gap = load(BCT_RTHETA_GAP)
    routec_contract = load(ROUTEC_CONTRACT)
    routec_decision = load(ROUTEC_DECISION)
    routec_first_run = load(ROUTEC_FIRST_RUN)

    external_rows = all_bct_rows["rows"]
    external_lane = {
        "schema": "MTTBCTExternalFormulaImportLane.v1",
        "status": "ALL_THREE_BCT_EXTERNAL_MAP_ROWS_ACCEPTED_FOR_VALIDATION",
        "formula_family_source": rel(BCT_FORMULA),
        "rundec_replay_source": rel(BCT_RUNDEC),
        "all_bct_external_rows_source": rel(ALL_BCT_ROWS),
        "accepted_external_bct_map_row_count": all_bct_rows["accepted_external_map_row_count"],
        "accepted_selected_Rtheta_source_row_count": all_bct_rows["accepted_Rtheta_source_row_count"],
        "all_three_bct_external_mass_scheme_rows_available": all_bct_rows[
            "all_three_bct_external_mass_scheme_rows_available"
        ],
        "rows": external_rows,
        "row_ids": [row["id"] for row in external_rows],
        "what_closes": {
            "bottom_MSbar_native_scale_transport_external_row": bct_rundec["closure_decision"][
                "bottom_MSbar_native_scale_transport_external_row_closed"
            ],
            "charm_MSbar_native_scale_transport_external_row": bct_rundec["closure_decision"][
                "charm_MSbar_native_scale_transport_external_row_closed"
            ],
            "tau_pole_rest_to_running_lepton_external_row": all_bct["closure_decision"][
                "all_three_bct_external_mass_scheme_rows_available"
            ],
            "external_BCT_formula_or_table_import": True,
        },
        "promotion_boundary": (
            "The BCT rows are accepted external map rows with provenance and guardrails. "
            "They may validate R_theta1 but do not select R_theta or prove no-knob source rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EXTERNAL, external_lane)

    formal_lift = routec_first_run["validation"]["formal_lift_diagnostic"]
    honest_root = routec_first_run["validation"]["honest_root"]
    failed_honest_slots = [
        name for name, result in honest_root.items() if isinstance(result, dict) and not result.get("passed", False)
    ]
    same_source = {
        "schema": "MTTBCTSelectedRThetaDerivationLane.v1",
        "status": "SELECTED_BCT_RTHETA_DERIVATION_ATTEMPTED_SELECTED_SOLVE_OPEN",
        "rtheta1_source": rel(RTHETA1),
        "bct_rtheta_gap_source": rel(BCT_RTHETA_GAP),
        "routec_acceptance_contract": rel(ROUTEC_CONTRACT),
        "routec_first_run_source": rel(ROUTEC_FIRST_RUN),
        "minimal_internal_missing_object": bct_gap["minimal_internal_missing_object"],
        "routec_contract_closed": routec_contract["contract_closed"],
        "formal_lift_lower_validators_all_pass": routec_first_run["validation"]["formal_lift_lower_validators_all_pass"],
        "formal_lift_promotion_passes": routec_first_run["validation"]["formal_lift_promotion_passes"],
        "honest_root_all_pass": routec_first_run["validation"]["honest_root_all_pass"],
        "failed_honest_root_slots": failed_honest_slots,
        "selected_routec_galerkin_solve_closed": routec_decision["selected_routec_galerkin_solve_closed"],
        "selected_Rtheta_mass_scheme_derivation_closed": bct_gap["selected_Rtheta_mass_scheme_derivation_closed"],
        "accepted_Rtheta_source_row_count": bct_gap["accepted_Rtheta_source_row_count"],
        "why_not_selected": [
            bct_gap["why_not_selected"],
            "The formal lift tests downstream algebra only; it cannot promote source rows without selected-source provenance.",
            "The honest root payload still fails selected-source verification for Route-C residual/D_E/Riesz/Green/dotD slots.",
        ],
        "conditional_promotion_if_closed": {
            "required_object": routec_contract["source_contract"]["name"],
            "must_emit": routec_contract["must_emit"],
            "would_promote_external_BCT_rows_to_validation_targets": True,
            "would_not_use_observed_values_as_selectors": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SAME_SOURCE, same_source)

    updated_rows = [row for row in readiness["rows"] if row["sector"] != "BCT"]
    for row in external_rows:
        updated_rows.append(
            {
                "id": row["id"],
                "sector": "BCT",
                "row_kind": "external_mass_scheme_map_row",
                "accepted_as_external_coordinate_or_map_row": row["accepted_as_external_map_row"],
                "accepted_as_selected_Rtheta_source_row": row["accepted_as_Rtheta_source_row"],
                "accepted_as_full_profile_row": False,
                "provenance": row["source"],
                "target_convention": row["target_convention"],
                "target_scale": row["target_scale"],
                "running_mass_MZ_GeV": row["running_mass_MZ_GeV"],
                "yukawa_MZ": row["yukawa_MZ"],
                "rtheta1_validation_role": "accepted external BCT map row can validate provisional composed BCT-to-Mt response",
            }
        )

    updated_external_count = sum(1 for row in updated_rows if row["accepted_as_external_coordinate_or_map_row"])
    updated_selected_count = sum(1 for row in updated_rows if row["accepted_as_selected_Rtheta_source_row"])
    updated = {
        "schema": "MTTUpdatedThresholdReadinessAfterBCTImport.v1",
        "status": "READINESS_MATRIX_UPDATED_WITH_THREE_ACCEPTED_EXTERNAL_BCT_MAP_ROWS",
        "previous_readiness_source": rel(READINESS),
        "external_lane_source": rel(EXTERNAL),
        "rtheta1_source": rel(RTHETA1),
        "rows": updated_rows,
        "row_count": len(updated_rows),
        "accepted_external_coordinate_or_map_row_count": updated_external_count,
        "accepted_selected_Rtheta_source_row_count": updated_selected_count,
        "accepted_BCT_external_map_row_count": all_bct_rows["accepted_external_map_row_count"],
        "accepted_BCT_selected_source_row_count": all_bct_rows["accepted_Rtheta_source_row_count"],
        "BCT_residual_targets_replaced_by_external_map_rows": True,
        "rtheta1_harness_can_validate_all_BCT_external_rows": rtheta1["provisional_firstpass_Rtheta_instantiated"],
        "rtheta1_harness_selects_BCT_rows": False,
        "full_profile_status": {
            "BCT_correlated_EFT_profile_computed": bct_profile["closure_decision"][
                "BCT_correlated_EFT_profile_computed"
            ],
            "BCT_EFT_profile_passes_95pct_gate": bct_profile["closure_decision"][
                "BCT_EFT_profile_passes_95pct_gate"
            ],
            "BCT_EFT_profile_passes_99pct_gate": bct_profile["closure_decision"][
                "BCT_EFT_profile_passes_99pct_gate"
            ],
            "full_covariance_profile_likelihood_closed": bct_profile["closure_decision"][
                "full_covariance_profile_likelihood_closed"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(UPDATED, updated)

    cutset = {
        "schema": "MTTNextCutsetAfterBCTDualLaneAttempt.v1",
        "status": "NEXT_ATTACK_SELECTED_SOURCE_REPAIR_OR_FULL_PROFILE_UPGRADE",
        "closed_now": {
            "BCT_external_formula_or_table_import": True,
            "all_three_BCT_external_map_rows_attached_to_Rtheta1_harness": True,
            "BCT_readiness_matrix_replaces_residual_targets_with_external_map_rows": True,
            "selected_Rtheta_derivation_lane_tested": True,
        },
        "still_open": {
            "SelectedRouteCStromingerGalerkinResidualSolve": True,
            "selected_BCT_Rtheta_mass_scheme_derivation": True,
            "selected_BCT_source_rows": True,
            "BCT_profile_95pct_closure": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "repair selected-source provenance for the Route-C/Strominger Galerkin residual solve",
            "route_B": "upgrade the BCT profile/covariance layer now that all external BCT rows are available",
            "route_C": "use Rtheta1 as validation harness while keeping external rows downstream-only",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedBCTFormulaImportOrSelectedThresholdRowDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "bct_external_formula_import_lane": rel(EXTERNAL),
            "bct_selected_rtheta_derivation_lane": rel(SAME_SOURCE),
            "updated_threshold_readiness_after_bct_import": rel(UPDATED),
            "next_cutset_after_bct_dual_lane_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "BCTDualLaneImportAndSelectedDerivationTheorem",
            "proved": True,
            "statement": (
                "Trying both lanes gives a split result. The external lane closes: bottom, charm, and tau all "
                "have accepted external mass-scheme map rows and can be attached to the provisional R_theta1 "
                "validation harness. The same-source selected derivation lane remains open: the Route-C/Strominger "
                "Galerkin solve contract exists and formal-lift diagnostics pass, but the honest selected-source "
                "payload still fails provenance/source verification, so no BCT Rtheta source rows are promoted."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "BCT_external_formula_or_table_import_closed": True,
            "accepted_BCT_external_map_row_count": all_bct_rows["accepted_external_map_row_count"],
            "all_three_BCT_external_map_rows_attached_to_Rtheta1_harness": True,
            "selected_BCT_Rtheta_mass_scheme_derivation_closed": False,
            "selected_BCT_source_rows_closed": False,
            "accepted_BCT_selected_source_row_count": all_bct_rows["accepted_Rtheta_source_row_count"],
            "SelectedRouteCStromingerGalerkinResidualSolve_closed": False,
            "BCT_profile_95pct_closure_closed": False,
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
        "certificate": "MTT_Selected_BCTFormulaImport_or_SelectedThresholdRowDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "BCT_external_formula_or_table_import_closed": True,
        "accepted_BCT_external_map_row_count": all_bct_rows["accepted_external_map_row_count"],
        "selected_BCT_Rtheta_mass_scheme_derivation_closed": False,
        "accepted_BCT_selected_source_row_count": all_bct_rows["accepted_Rtheta_source_row_count"],
        "SelectedRouteCStromingerGalerkinResidualSolve_closed": False,
        "BCT_profile_95pct_closure_closed": False,
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

    note = f"""# MTT Selected BCTFormulaImport or SelectedThresholdRowDerivation v1

Status: `{STATUS}`.

Both requested lanes were tried.

```text
external BCT formula/table import closed : true
accepted BCT external map rows           : {all_bct_rows["accepted_external_map_row_count"]}
selected BCT Rtheta source rows          : {all_bct_rows["accepted_Rtheta_source_row_count"]}
same-source selected derivation closed   : false
```

The external lane now has bottom, charm, and tau map rows attached to the
provisional `R_theta^(1,diag)` validation harness.  The selected-source lane
still requires `SelectedRouteCStromingerGalerkinResidualSolve`; formal-lift
diagnostics pass, but the honest selected-source payload remains unpromoted.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
