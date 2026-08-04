"""Build top/Higgs threshold map rows or external precision table artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_tophiggsthresholdmaprows_or_externalprecisiontable"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRECISION_RECHECK = PACKET_DIR / "top_higgs_partial_precision_rows_recheck.packet.json"
MAP_FILL = PACKET_DIR / "top_higgs_threshold_map_row_fill_attempt.packet.json"
EXTERNAL_CONTRACT = PACKET_DIR / "external_precision_table_import_contract.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_top_higgs_threshold_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TopHiggsThresholdMapRows_or_ExternalPrecisionTable_v1.md"

PREVIOUS = DATA / "selected_thresholdpolerunningmaps_or_rthetaconventionsource.candidate.json"
TOP_HIGGS_TARGET = (
    DATA
    / "selected_thresholdpolerunningmaps_or_rthetaconventionsource"
    / "top_higgs_threshold_map_target.packet.json"
)
MAP_DECOMP = (
    DATA
    / "selected_thresholdpolerunningmaps_or_rthetaconventionsource"
    / "threshold_pole_running_map_decomposition.packet.json"
)
PARTIAL_PRECISION = (
    DATA
    / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill"
    / "partial_precision_value_emission.packet.json"
)
PROMOTION_DECISION = (
    DATA
    / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill"
    / "true_equivalence_promotion_decision_after_value_attempt.packet.json"
)
EXTERNAL_BENCH = (
    DATA
    / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
    / "external_literature_rg_benchmark_values.packet.json"
)
RESIDUAL_REQS = (
    DATA
    / "selected_thresholdpolerunningmaps_or_covarianceprofile"
    / "pole_threshold_residual_map_requirements.packet.json"
)
POLICY_CONTRACT = (
    DATA
    / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
    / "threshold_pole_running_policy_contract.packet.json"
)
SOURCE_ATTEMPT = (
    DATA
    / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
    / "same_branch_convention_source_theorem_attempt.packet.json"
)

STATUS = (
    "MTT_SELECTED_TOPHIGGSTHRESHOLDMAPROWS_OR_EXTERNALPRECISIONTABLE_"
    "BUILT_PARTIAL_PRECISION_ROWS_MAPS_OPEN"
)
NEXT = "MTT_Selected_TopHiggsFormulaMapImport_or_RThetaThresholdDerivation_v1"


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
        raise FileNotFoundError("missing top/Higgs threshold sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        TOP_HIGGS_TARGET,
        MAP_DECOMP,
        PARTIAL_PRECISION,
        PROMOTION_DECISION,
        EXTERNAL_BENCH,
        RESIDUAL_REQS,
        POLICY_CONTRACT,
        SOURCE_ATTEMPT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    top_higgs_target = load(TOP_HIGGS_TARGET)
    map_decomp = load(MAP_DECOMP)
    partial_precision = load(PARTIAL_PRECISION)
    promotion = load(PROMOTION_DECISION)
    external_bench = load(EXTERNAL_BENCH)
    residual_reqs = load(RESIDUAL_REQS)
    policy_contract = load(POLICY_CONTRACT)
    source_attempt = load(SOURCE_ATTEMPT)

    top_higgs_ids = {"lambda_Mt", "y_t_Mt"}
    partial_top_higgs_rows = [
        row for row in partial_precision["value_rows"] if row["id"] in top_higgs_ids
    ]
    partial_rows_closed = (
        len(partial_top_higgs_rows) == 2
        and all(row["accepted_as_partial_precision_value"] for row in partial_top_higgs_rows)
        and partial_precision["accepted_as_value_emission_attempt"] is True
        and partial_precision["accepted_as_full_true_equivalence_profile"] is False
    )

    precision_recheck = {
        "schema": "MTTTopHiggsPartialPrecisionRowsRecheck.v1",
        "status": "TOP_HIGGS_PARTIAL_PRECISION_ROWS_PRESENT_FULL_PROFILE_OPEN",
        "partial_precision_source": rel(PARTIAL_PRECISION),
        "promotion_decision_source": rel(PROMOTION_DECISION),
        "rows": partial_top_higgs_rows,
        "partial_top_higgs_precision_rows_closed": partial_rows_closed,
        "accepted_as_external_precision_target_rows": partial_rows_closed,
        "accepted_as_threshold_map_source_rows": False,
        "accepted_as_full_true_equivalence_profile": False,
        "why_not_full_profile": partial_precision["why_not_full_true_equivalence"],
        "true_SM_equivalence_closed": promotion["true_SM_equivalence_closed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PRECISION_RECHECK, precision_recheck)

    map_requirements = [
        {
            "id": "top_direct_or_pole_to_MSbar_running_y_t",
            "target_row": "y_t_Mt",
            "required_formula_or_table": "top pole/direct mass to MSbar running top Yukawa matching",
            "residual_slots": top_higgs_target["top_targets"]["residual_slots"],
            "accepted_as_map_now": False,
            "blocking_reason": "current rows are partial precision values and residual requirements, not a provenance-bearing map formula/table",
        },
        {
            "id": "Higgs_pole_to_running_lambda_H",
            "target_row": "lambda_Mt",
            "required_formula_or_table": "Higgs pole mass and vev convention to MSbar lambda(Mt) matching",
            "residual_slots": top_higgs_target["higgs_targets"]["residual_slots"],
            "accepted_as_map_now": False,
            "blocking_reason": "current rows are partial precision values and residual requirements, not a provenance-bearing map formula/table",
        },
    ]
    map_fill = {
        "schema": "MTTTopHiggsThresholdMapRowFillAttempt.v1",
        "status": "TOP_HIGGS_MAP_ROW_FILL_ATTEMPTED_NO_MAP_ROWS_ACCEPTED",
        "map_decomposition_source": rel(MAP_DECOMP),
        "target_source": rel(TOP_HIGGS_TARGET),
        "same_branch_Rtheta_convention_source_theorem_closed": source_attempt[
            "same_branch_convention_source_theorem_closed"
        ],
        "accepted_precision_threshold_row_count_before": map_decomp[
            "accepted_precision_threshold_row_count"
        ],
        "map_requirements": map_requirements,
        "accepted_top_higgs_threshold_map_rows": [],
        "accepted_top_higgs_threshold_map_row_count": 0,
        "partial_precision_rows_may_validate_maps": partial_rows_closed,
        "residuals_are_requirements_not_fitted_corrections": residual_reqs[
            "interpretation"
        ].endswith("cannot be used as selected MTT source data."),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(MAP_FILL, map_fill)

    external_contract = {
        "schema": "MTTExternalPrecisionTableImportContract.v1",
        "status": "EXTERNAL_PRECISION_TABLE_IMPORT_CONTRACT_BUILT_ROWS_OPEN",
        "external_benchmark_source": rel(EXTERNAL_BENCH),
        "current_benchmark_reference": external_bench["source"],
        "current_benchmark_reference_point": external_bench["reference_point"],
        "current_benchmark_values_available": [
            "lambda_Mt",
            "y_t_Mt",
            "g_1_GUT_Mt",
            "g_2_Mt",
            "g_3_Mt",
            "g_Y_Mt",
        ],
        "current_benchmark_accepted_as_reference": external_bench[
            "accepted_as_external_literature_benchmark_reference"
        ],
        "current_benchmark_accepted_as_full_precision_match": external_bench[
            "accepted_as_full_precision_match"
        ],
        "required_for_acceptance_as_map_source": [
            "explicit top pole/direct to MSbar y_t matching formula or table with provenance",
            "explicit Higgs pole/vev to MSbar lambda matching formula or table with provenance",
            "declared loop order and scheme tied to the M_t reference point",
            "input uncertainty and covariance/diagonal sidecar semantics",
            "replay command or machine-readable table sufficient to regenerate rows",
            "proof rows validate but do not select the MTT source branch",
        ],
        "policy_contract_source": rel(POLICY_CONTRACT),
        "current_policy_map_outputs_required": policy_contract["map_outputs_required_next"],
        "accepted_external_precision_table_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EXTERNAL_CONTRACT, external_contract)

    cutset = {
        "schema": "MTTNextCutsetAfterTopHiggsThresholdAttempt.v1",
        "status": "NEXT_ATTACK_FORMULA_MAP_IMPORT_OR_RTHETA_THRESHOLD_DERIVATION",
        "closed_now": {
            "top_higgs_partial_precision_rows_rechecked": partial_rows_closed,
            "external_precision_table_import_contract": True,
            "top_higgs_map_fill_attempt": True,
            "residuals_kept_as_requirements_not_fits": True,
        },
        "still_open": {
            "accepted_top_higgs_threshold_map_rows": True,
            "accepted_external_precision_table_as_map_source": True,
            "same_branch_Rtheta_convention_source_theorem": True,
            "full_profile_covariance": True,
            "bottom_charm_tau_mass_scheme_maps": True,
            "W_Z_H_electroweak_matching_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "import explicit Buttazzo-style top/Higgs matching formula/table rows with replay provenance",
            "route_B": "derive the top/Higgs maps from selected R_theta convention/source geometry",
            "route_C": "extend partial precision rows with covariance/profile sidecars while keeping source-map status open",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedTopHiggsThresholdMapRowsOrExternalPrecisionTable",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "top_higgs_partial_precision_rows_recheck": rel(PRECISION_RECHECK),
            "top_higgs_threshold_map_row_fill_attempt": rel(MAP_FILL),
            "external_precision_table_import_contract": rel(EXTERNAL_CONTRACT),
            "next_cutset_after_top_higgs_threshold_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "TopHiggsPartialPrecisionRowsAndMapSourceSeparationTheorem",
            "proved": True,
            "statement": (
                "The repo already emits lambda_Mt and y_t_Mt as partial diagonal precision value rows, "
                "and these rows may validate top/Higgs threshold maps. They cannot be promoted to "
                "threshold-map source rows: residual slots are requirements, external benchmark values "
                "are references, and no same-branch R_theta convention source or provenance-bearing "
                "top/Higgs matching formula/table is accepted yet."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "top_higgs_partial_precision_rows_closed": partial_rows_closed,
            "external_precision_table_import_contract_closed": True,
            "top_higgs_threshold_map_fill_attempt_closed": True,
            "accepted_top_higgs_threshold_map_rows_closed": False,
            "accepted_external_precision_table_as_map_source_closed": False,
            "same_branch_Rtheta_convention_source_theorem_closed": False,
            "full_profile_covariance_closed": False,
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
        "certificate": "MTT_Selected_TopHiggsThresholdMapRows_or_ExternalPrecisionTable_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "top_higgs_partial_precision_rows_closed": partial_rows_closed,
        "accepted_top_higgs_threshold_map_row_count": 0,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected TopHiggsThresholdMapRows or ExternalPrecisionTable v1

Status: `{STATUS}`.

This artifact attacks the top/Higgs map rows.

```text
lambda_Mt and y_t_Mt partial precision rows closed : {str(partial_rows_closed).lower()}
accepted top/Higgs threshold map rows              : 0
external precision table import contract closed    : true
same-branch R_theta convention source closed       : false
full profile covariance closed                     : false
```

The gain is the separation: `lambda_Mt` and `y_t_Mt` exist as partial diagonal
precision rows, but not as threshold-map source rows.  To promote them, we need
either provenance-bearing top/Higgs matching formulas/tables or a selected
`R_theta` derivation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
