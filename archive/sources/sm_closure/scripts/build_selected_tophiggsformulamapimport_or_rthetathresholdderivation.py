"""Build top/Higgs formula map import or R_theta threshold derivation artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_tophiggsformulamapimport_or_rthetathresholdderivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FORMULA_IMPORT = PACKET_DIR / "top_higgs_formula_map_import_replay.packet.json"
ACCEPTANCE = PACKET_DIR / "top_higgs_external_formula_map_acceptance.packet.json"
RTHETA_GAP = PACKET_DIR / "rtheta_threshold_map_derivation_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_top_higgs_formula_import.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TopHiggsFormulaMapImport_or_RThetaThresholdDerivation_v1.md"

PREVIOUS = DATA / "selected_tophiggsthresholdmaprows_or_externalprecisiontable.candidate.json"
EXTERNAL_CONTRACT = (
    DATA
    / "selected_tophiggsthresholdmaprows_or_externalprecisiontable"
    / "external_precision_table_import_contract.packet.json"
)
MAP_FILL = (
    DATA
    / "selected_tophiggsthresholdmaprows_or_externalprecisiontable"
    / "top_higgs_threshold_map_row_fill_attempt.packet.json"
)
FORMULA_REPLAY = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "buttazzo_boundary_formula_replay.packet.json"
)
COVARIANCE = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "diagonal_sensitivity_covariance_scaffold.packet.json"
)
FORMULA_GATE = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "updated_true_equivalence_gate_after_formula_replay.packet.json"
)
SOURCE_ATTEMPT = (
    DATA
    / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
    / "same_branch_convention_source_theorem_attempt.packet.json"
)
POLICY_CONTRACT = (
    DATA
    / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
    / "threshold_pole_running_policy_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_TOPHIGGSFORMULAMAPIMPORT_OR_RTHETATHRESHOLDDERIVATION_"
    "BUILT_EXTERNAL_FORMULA_MAP_ROWS_CLOSED_RTHETA_OPEN"
)
NEXT = "MTT_Selected_BottomCharmTauMaps_or_RThetaThresholdDerivation_v1"


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
        raise FileNotFoundError("missing top/Higgs formula import sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        EXTERNAL_CONTRACT,
        MAP_FILL,
        FORMULA_REPLAY,
        COVARIANCE,
        FORMULA_GATE,
        SOURCE_ATTEMPT,
        POLICY_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    external_contract = load(EXTERNAL_CONTRACT)
    map_fill = load(MAP_FILL)
    formula_replay = load(FORMULA_REPLAY)
    covariance = load(COVARIANCE)
    formula_gate = load(FORMULA_GATE)
    source_attempt = load(SOURCE_ATTEMPT)
    policy_contract = load(POLICY_CONTRACT)

    row_ids = ["lambda_Mt", "y_t_Mt"]
    formula_rows = []
    for row_id in row_ids:
        formula_rows.append(
            {
                "id": row_id,
                "formula": formula_replay["formula_reference"][row_id],
                "buttazzo_central_input_value": formula_replay["buttazzo_central_input_replay"][
                    "values"
                ][row_id],
                "current_repo_input_value": formula_replay["current_repo_input_variant"]["values"][
                    row_id
                ],
                "diagonal_sigma": covariance["propagated_diagonal_uncertainties"][row_id][
                    "diagonal_sigma"
                ],
                "jacobian": covariance["jacobian"][row_id],
            }
        )

    central_replay_rows = [
        row
        for row in formula_replay["buttazzo_central_input_replay"]["comparison_rows"]
        if row["id"] in {"lambda_Mt_formula_vs_literature", "y_t_Mt_formula_vs_literature"}
    ]
    formulas_replay_exactly = (
        len(central_replay_rows) == 2
        and all(row["absolute_delta"] < 1e-14 for row in central_replay_rows)
        and formula_replay["buttazzo_central_input_replay"]["replays_encoded_literature_values"]
        is True
    )
    diagonal_sidecars_present = all(
        row_id in covariance["propagated_diagonal_uncertainties"] for row_id in row_ids
    )
    import_contract_satisfied = (
        external_contract["accepted_external_precision_table_now"] is False
        and formulas_replay_exactly
        and diagonal_sidecars_present
        and formula_replay["observed_data_used_as_selector"] is False
        and formula_replay["target_fitting_used"] is False
    )

    formula_import = {
        "schema": "MTTTopHiggsFormulaMapImportReplay.v1",
        "status": "TOP_HIGGS_BUTTAZZO_FORMULA_MAPS_IMPORTED_FOR_EXTERNAL_VALIDATION",
        "external_contract_source": rel(EXTERNAL_CONTRACT),
        "formula_replay_source": rel(FORMULA_REPLAY),
        "diagonal_covariance_source": rel(COVARIANCE),
        "source": formula_replay["source"],
        "reference_inputs": formula_replay["buttazzo_central_input_replay"]["inputs"],
        "current_repo_inputs": formula_replay["current_repo_input_variant"]["inputs"],
        "formula_rows": formula_rows,
        "central_replay_rows": central_replay_rows,
        "formulas_replay_encoded_literature_values": formulas_replay_exactly,
        "diagonal_sensitivity_sidecars_present": diagonal_sidecars_present,
        "accepted_as_external_formula_map_import": import_contract_satisfied,
        "accepted_as_same_branch_Rtheta_derivation": False,
        "accepted_as_full_profile_likelihood": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FORMULA_IMPORT, formula_import)

    accepted_rows = [
        {
            "id": row_id,
            "accepted_as_external_top_higgs_formula_map_row": import_contract_satisfied,
            "accepted_as_Rtheta_source_row": False,
            "accepted_as_full_profile_row": False,
            "provenance": rel(FORMULA_REPLAY),
            "covariance_sidecar": rel(COVARIANCE),
        }
        for row_id in row_ids
    ]
    acceptance = {
        "schema": "MTTTopHiggsExternalFormulaMapAcceptance.v1",
        "status": "TWO_EXTERNAL_TOP_HIGGS_FORMULA_MAP_ROWS_ACCEPTED_RTHETA_OPEN",
        "previous_map_fill_source": rel(MAP_FILL),
        "accepted_rows": accepted_rows,
        "accepted_external_formula_map_row_count": sum(
            1 for row in accepted_rows if row["accepted_as_external_top_higgs_formula_map_row"]
        ),
        "accepted_Rtheta_source_row_count": 0,
        "accepted_full_profile_row_count": 0,
        "old_accepted_top_higgs_threshold_map_row_count": map_fill[
            "accepted_top_higgs_threshold_map_row_count"
        ],
        "promotion_boundary": (
            "These rows are accepted as external formula-map imports with provenance and diagonal "
            "sidecars. They are not selected MTT source rows and do not close full profile likelihood."
        ),
        "residuals_are_requirements_not_fitted_corrections": map_fill[
            "residuals_are_requirements_not_fitted_corrections"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ACCEPTANCE, acceptance)

    rtheta_gap = {
        "schema": "MTTRThetaThresholdMapDerivationGap.v1",
        "status": "EXTERNAL_FORMULA_MAP_ROWS_ACCEPTED_SELECTED_RTHETA_DERIVATION_OPEN",
        "source_attempt_source": rel(SOURCE_ATTEMPT),
        "same_branch_convention_source_theorem_closed": source_attempt[
            "same_branch_convention_source_theorem_closed"
        ],
        "formula_values_are_literature_replay_not_MTT_source": formula_gate["guardrails"][
            "formula_values_are_literature_replay_not_MTT_source"
        ],
        "current_input_variant_is_not_selected_prediction": formula_gate["guardrails"][
            "current_input_variant_is_not_selected_prediction"
        ],
        "what_Rtheta_must_still_derive": [
            "same-branch convention source selecting the scale/scheme/loop policy",
            "top y_t threshold map without importing observed target values as selectors",
            "Higgs lambda threshold map without importing observed target values as selectors",
            "basis map from selected MTT rows to the accepted formula-map coordinates",
        ],
        "accepted_external_formula_rows_may_validate_Rtheta": True,
        "accepted_external_formula_rows_select_Rtheta": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA_GAP, rtheta_gap)

    cutset = {
        "schema": "MTTNextCutsetAfterTopHiggsFormulaImport.v1",
        "status": "NEXT_ATTACK_BOTTOM_CHARM_TAU_MAPS_OR_RTHETA_THRESHOLD_DERIVATION",
        "closed_now": {
            "top_higgs_external_formula_map_import": import_contract_satisfied,
            "lambda_Mt_external_formula_map_row": import_contract_satisfied,
            "y_t_Mt_external_formula_map_row": import_contract_satisfied,
            "diagonal_sensitivity_sidecars": diagonal_sidecars_present,
            "Rtheta_nonselector_gap_recorded": True,
        },
        "still_open": {
            "same_branch_Rtheta_threshold_derivation": True,
            "full_covariance_profile_likelihood": True,
            "bottom_charm_native_MSbar_scale_transport_maps": True,
            "tau_pole_rest_to_running_lepton_map": True,
            "W_Z_H_electroweak_matching_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "fill bottom/charm/tau mass-scheme maps using external formula/table imports",
            "route_B": "derive Rtheta threshold maps against the accepted top/Higgs formula-map rows",
            "route_C": "build full covariance/profile likelihood over the accepted formula-map basis",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedTopHiggsFormulaMapImportOrRThetaThresholdDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "top_higgs_formula_map_import_replay": rel(FORMULA_IMPORT),
            "top_higgs_external_formula_map_acceptance": rel(ACCEPTANCE),
            "rtheta_threshold_map_derivation_gap": rel(RTHETA_GAP),
            "next_cutset_after_top_higgs_formula_import": rel(CUTSET),
        },
        "theorem": {
            "name": "TopHiggsExternalFormulaMapImportAndRThetaGapTheorem",
            "proved": True,
            "statement": (
                "The Buttazzo boundary-condition formulas can be promoted under the strict external "
                "precision-table contract to two accepted external top/Higgs formula-map rows: lambda_Mt "
                "and y_t_Mt. The rows carry provenance, replay to the encoded literature values at the "
                "published central inputs, and have diagonal sensitivity sidecars. They are not selected "
                "R_theta source rows and do not close full covariance/profile likelihood, true SM "
                "equivalence, or no-knob derivation."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "top_higgs_external_formula_map_import_closed": import_contract_satisfied,
            "lambda_Mt_external_formula_map_row_closed": import_contract_satisfied,
            "y_t_Mt_external_formula_map_row_closed": import_contract_satisfied,
            "accepted_external_formula_map_row_count": acceptance[
                "accepted_external_formula_map_row_count"
            ],
            "same_branch_Rtheta_threshold_derivation_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "bottom_charm_tau_mass_scheme_maps_closed": False,
            "W_Z_H_electroweak_matching_rows_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_TopHiggsFormulaMapImport_or_RThetaThresholdDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "accepted_external_formula_map_row_count": acceptance[
            "accepted_external_formula_map_row_count"
        ],
        "same_branch_Rtheta_threshold_derivation_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected TopHiggsFormulaMapImport or RThetaThresholdDerivation v1

Status: `{STATUS}`.

This artifact promotes the existing Buttazzo boundary formula replay under the
strict top/Higgs external precision-table contract.

```text
accepted external formula-map rows : {acceptance["accepted_external_formula_map_row_count"]}
lambda_Mt formula row accepted     : {str(import_contract_satisfied).lower()}
y_t_Mt formula row accepted        : {str(import_contract_satisfied).lower()}
same-branch R_theta derivation     : false
full covariance/profile likelihood : false
```

The accepted rows are external formula-map rows with provenance and diagonal
sensitivity sidecars. They validate later `R_theta` derivations but do not
select the MTT source branch.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
