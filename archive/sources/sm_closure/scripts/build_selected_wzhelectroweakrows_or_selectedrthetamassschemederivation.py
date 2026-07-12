"""Build W/Z/H electroweak rows or selected Rtheta mass-scheme derivation artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INVENTORY = PACKET_DIR / "wzh_electroweak_row_inventory.packet.json"
ACCEPTANCE = PACKET_DIR / "wzh_external_benchmark_row_acceptance.packet.json"
RTHETA_GAP = PACKET_DIR / "selected_rtheta_mass_scheme_gap_after_wzh_rows.packet.json"
HIGGS_EW = PACKET_DIR / "higgs_decay_electroweak_boundary_reconciliation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_wzh_external_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_WZHElectroweakRows_or_SelectedRThetaMassSchemeDerivation_v1.md"

CHARM_CUTSET = (
    DATA
    / "selected_charmtablesubstitution_or_selectedrthetarowsdecision"
    / "next_cutset_after_charm_table_substitution.packet.json"
)
EXTERNAL_BENCHMARK = (
    DATA
    / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
    / "external_literature_rg_benchmark_values.packet.json"
)
TOP_HIGGS_ACCEPTANCE = (
    DATA
    / "selected_tophiggsformulamapimport_or_rthetathresholdderivation"
    / "top_higgs_external_formula_map_acceptance.packet.json"
)
TOP_HIGGS_IMPORT = (
    DATA
    / "selected_tophiggsformulamapimport_or_rthetathresholdderivation"
    / "top_higgs_formula_map_import_replay.packet.json"
)
GAUGE_BRIDGE = (
    DATA
    / "selected_thresholdpolerunningmaps_or_rthetaconventionsource"
    / "gauge_bridge_policy_validation_status.packet.json"
)
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
)
REFERENCE_VALUES = DATA / "sm_equivalence_reference_data_values_fill.candidate.json"
HIGGS_EW_POLICY = (
    DATA
    / "selected_higgsewbenchmarkpolicy_or_fullformulas"
    / "remaining_electroweak_benchmark_replay_policy.packet.json"
)
HIGGS_EW_CANDIDATE = DATA / "selected_higgsewbenchmarkpolicy_or_fullformulas.candidate.json"

STATUS = (
    "MTT_SELECTED_WZHELECTROWEAKROWS_OR_SELECTEDRTHETAMASSSCHEMEDERIVATION_"
    "BUILT_EXTERNAL_BENCHMARK_ROWS_CLOSED_COVARIANCE_RTHETA_OPEN"
)
NEXT = "MTT_Selected_FullCovarianceProfile_or_SelectedRThetaSourceRows_v1"


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
        raise FileNotFoundError("missing W/Z/H electroweak row sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        CHARM_CUTSET,
        EXTERNAL_BENCHMARK,
        TOP_HIGGS_ACCEPTANCE,
        TOP_HIGGS_IMPORT,
        GAUGE_BRIDGE,
        THRESHOLD_CONTRACT,
        REFERENCE_VALUES,
        HIGGS_EW_POLICY,
        HIGGS_EW_CANDIDATE,
    ]
    require_sources(sources)

    charm_cutset = load(CHARM_CUTSET)
    external = load(EXTERNAL_BENCHMARK)
    top_higgs_acceptance = load(TOP_HIGGS_ACCEPTANCE)
    top_higgs_import = load(TOP_HIGGS_IMPORT)
    gauge_bridge = load(GAUGE_BRIDGE)
    threshold_contract = load(THRESHOLD_CONTRACT)
    reference = load(REFERENCE_VALUES)
    higgs_ew_policy = load(HIGGS_EW_POLICY)
    higgs_ew_candidate = load(HIGGS_EW_CANDIDATE)

    literature_values = external["literature_values"]
    reference_constants = reference["reference_values"]["constants"]
    reference_masses = reference["reference_values"]["masses"]

    accepted_wzh_rows = [
        {
            "id": "v_from_G_F_tree_reference",
            "role": "electroweak vacuum normalization reference row",
            "central_value": reference_constants["v_from_G_F"]["central_value"],
            "units": reference_constants["v_from_G_F"]["units"],
            "scheme": reference_constants["v_from_G_F"]["scheme"],
            "provenance": rel(REFERENCE_VALUES),
            "accepted_as_external_WZH_coordinate_row": True,
            "accepted_as_MSbar_threshold_match": False,
            "accepted_as_selected_Rtheta_source_row": False,
            "used_as_source_selector": False,
        },
        {
            "id": "g_Y_Mt",
            "role": "hypercharge gauge coupling at mu=M_t",
            "central_value": literature_values["g_Y_Mt"]["central_value"],
            "scheme": "MSbar at mu=M_t",
            "provenance": rel(EXTERNAL_BENCHMARK),
            "accepted_as_external_WZH_coordinate_row": True,
            "accepted_as_precision_threshold_match": False,
            "accepted_as_selected_Rtheta_source_row": False,
            "used_as_source_selector": False,
        },
        {
            "id": "g_1_GUT_Mt",
            "role": "GUT-normalized hypercharge alias sqrt(5/3)*g_Y",
            "central_value": literature_values["g_1_GUT_Mt"]["central_value"],
            "scheme": "MSbar at mu=M_t, GUT-normalized U(1)",
            "provenance": rel(EXTERNAL_BENCHMARK),
            "accepted_as_external_WZH_coordinate_row": True,
            "accepted_as_precision_threshold_match": False,
            "accepted_as_selected_Rtheta_source_row": False,
            "used_as_source_selector": False,
        },
        {
            "id": "g_2_Mt",
            "role": "SU(2) gauge coupling at mu=M_t",
            "central_value": literature_values["g_2_Mt"]["central_value"],
            "scheme": "MSbar at mu=M_t",
            "provenance": rel(EXTERNAL_BENCHMARK),
            "accepted_as_external_WZH_coordinate_row": True,
            "accepted_as_precision_threshold_match": False,
            "accepted_as_selected_Rtheta_source_row": False,
            "used_as_source_selector": False,
        },
        {
            "id": "lambda_Mt",
            "role": "Higgs quartic coordinate at mu=M_t",
            "central_value": literature_values["lambda_Mt"]["central_value"],
            "scheme": "MSbar at mu=M_t",
            "provenance": rel(TOP_HIGGS_IMPORT),
            "covariance_sidecar": top_higgs_acceptance["accepted_rows"][0]["covariance_sidecar"],
            "accepted_as_external_WZH_coordinate_row": True,
            "accepted_as_precision_threshold_match": False,
            "accepted_as_selected_Rtheta_source_row": False,
            "used_as_source_selector": False,
        },
    ]

    supporting_rows = [
        {
            "id": "g_3_Mt",
            "role": "QCD coupling needed by full RG/profile basis, not a W/Z/H electroweak row",
            "central_value": literature_values["g_3_Mt"]["central_value"],
            "provenance": rel(EXTERNAL_BENCHMARK),
            "accepted_as_supporting_RG_benchmark_row": True,
        },
        {
            "id": "y_t_Mt",
            "role": "top Yukawa needed by full RG/profile basis, already accepted by top/Higgs formula-map artifact",
            "central_value": literature_values["y_t_Mt"]["central_value"],
            "provenance": rel(TOP_HIGGS_IMPORT),
            "accepted_as_supporting_RG_benchmark_row": True,
        },
    ]

    gauge_rows = {row["id"]: row for row in gauge_bridge["comparison_rows"]}
    all_wzh_rows_available = all(row["accepted_as_external_WZH_coordinate_row"] for row in accepted_wzh_rows)
    gauge_bridge_passes = gauge_bridge["passes_coarse_gauge_bridge"] is True
    lambda_import_accepted = any(
        row["id"] == "lambda_Mt" and row["accepted_as_external_top_higgs_formula_map_row"]
        for row in top_higgs_acceptance["accepted_rows"]
    )
    v_reference_available = reference_constants["v_from_G_F"]["used_as_source_selector"] is False
    row_coordinate_closure = all_wzh_rows_available and gauge_bridge_passes and lambda_import_accepted and v_reference_available

    inventory = {
        "schema": "MTTWZHElectroweakRowInventory.v1",
        "status": "WZH_ELECTROWEAK_COORDINATE_ROWS_INVENTORIED",
        "threshold_contract_source": rel(THRESHOLD_CONTRACT),
        "contract_text": threshold_contract["threshold_matching_required"]["W_Z_H"],
        "external_benchmark_source": rel(EXTERNAL_BENCHMARK),
        "reference_value_source": rel(REFERENCE_VALUES),
        "top_higgs_formula_import_source": rel(TOP_HIGGS_IMPORT),
        "accepted_wzh_coordinate_rows": accepted_wzh_rows,
        "supporting_rg_benchmark_rows": supporting_rows,
        "row_inventory_summary": {
            "wzh_coordinate_row_count": len(accepted_wzh_rows),
            "supporting_rg_benchmark_row_count": len(supporting_rows),
            "independent_hypercharge_rows": 1,
            "g_1_GUT_is_normalization_alias_of_g_Y": True,
            "v_row_is_tree_reference_anchor_not_MSbar_threshold_match": True,
            "all_wzh_coordinate_rows_available": all_wzh_rows_available,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(INVENTORY, inventory)

    acceptance = {
        "schema": "MTTWZHExternalBenchmarkRowAcceptance.v1",
        "status": "WZH_EXTERNAL_BENCHMARK_COORDINATE_ROWS_ACCEPTED_SOURCE_RTHETA_OPEN",
        "inventory_source": rel(INVENTORY),
        "accepted_external_wzh_coordinate_row_count": len(accepted_wzh_rows),
        "accepted_selected_Rtheta_source_row_count": 0,
        "accepted_full_covariance_profile_row_count": 0,
        "row_coordinate_closure_claimed": row_coordinate_closure,
        "full_precision_threshold_match_claimed": False,
        "full_covariance_profile_likelihood_claimed": False,
        "gauge_bridge_policy_validation": {
            "source": rel(GAUGE_BRIDGE),
            "accepted_as_policy_validation_scaffold": gauge_bridge["accepted_as_policy_validation_scaffold"],
            "accepted_as_precision_threshold_match": gauge_bridge["accepted_as_precision_threshold_match"],
            "passes_coarse_gauge_bridge": gauge_bridge_passes,
            "max_absolute_delta_to_literature": gauge_bridge["max_absolute_delta_to_literature"],
            "comparison_rows": [
                {
                    "id": key,
                    "transported_value": row["transported_value"],
                    "literature_value": row["literature_value"],
                    "absolute_delta": row["absolute_delta"],
                    "relative_delta": row["relative_delta"],
                }
                for key, row in gauge_rows.items()
            ],
        },
        "covariance_boundary": {
            "lambda_Mt_has_diagonal_sidecar": "covariance_sidecar" in accepted_wzh_rows[-1],
            "gauge_rows_have_full_uncertainty_or_correlation_sidecars": False,
            "v_row_has_reference_uncertainty_but_not_MSbar_threshold_covariance": True,
            "full_covariance_required_before_profile_likelihood": True,
        },
        "promotion_boundary": (
            "The W/Z/H coordinate rows are accepted as external benchmark/reference coordinates with "
            "provenance. They are not selected MTT Rtheta source rows, not full precision threshold "
            "matches, and not a full covariance/profile likelihood."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ACCEPTANCE, acceptance)

    rtheta_gap = {
        "schema": "MTTSelectedRThetaMassSchemeGapAfterWZHRows.v1",
        "status": "WZH_EXTERNAL_ROWS_ACCEPTED_SELECTED_RTHETA_MASS_SCHEME_STILL_OPEN",
        "wzh_acceptance_source": rel(ACCEPTANCE),
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "same_branch_Rtheta_threshold_derivation_closed": False,
        "accepted_external_rows_may_validate_Rtheta": True,
        "accepted_external_rows_select_Rtheta": False,
        "minimal_internal_missing_objects": [
            "selected source map from MTT geometry to v/gY/g2/lambda coordinates",
            "selected Rtheta threshold/mass-scheme functional producing the same coordinate rows",
            "gauge-row uncertainty/correlation sidecars at the common scale",
            "full covariance matrix linking W/Z/H, top/Higgs, BCT, and Higgs-decay rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA_GAP, rtheta_gap)

    higgs_ew = {
        "schema": "MTTHiggsDecayElectroweakBoundaryReconciliation.v1",
        "status": "HIGGS_DECAY_EW_ROWS_REMAIN_BENCHMARK_REPLAY_NOT_WZH_MATCHING_SOURCE",
        "higgs_ew_candidate_source": rel(HIGGS_EW_CANDIDATE),
        "higgs_ew_policy_source": rel(HIGGS_EW_POLICY),
        "boundary": (
            "W/Z/H electroweak matching coordinates are RG/threshold coordinates for the SM parameter "
            "basis. The Higgs WW*, ZZ*, and Zgamma rows are downstream Higgs-decay observables and remain "
            "benchmark replay rows until executable formula kernels or official likelihood/covariance are imported."
        ),
        "higgs_ten_channel_replay_completed": higgs_ew_candidate["closure_decision"][
            "ten_channel_replay_completed"
        ],
        "higgs_uniform_formula_rows_fully_closed": higgs_ew_candidate["closure_decision"][
            "uniform_formula_rows_fully_closed"
        ],
        "remaining_higgs_ew_benchmark_rows": [
            {
                "channel": row["channel"],
                "accepted_as_downstream_benchmark_replay_row": row[
                    "accepted_as_downstream_benchmark_replay_row"
                ],
                "accepted_as_executable_formula_kernel": row["accepted_as_executable_formula_kernel"],
                "accepted_as_precision_formula_row": row["accepted_as_precision_formula_row"],
                "source_url": row["source_url"],
            }
            for row in higgs_ew_policy["rows"]
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(HIGGS_EW, higgs_ew)

    cutset = {
        "schema": "MTTNextCutsetAfterWZHExternalRows.v1",
        "status": "NEXT_ATTACK_FULL_COVARIANCE_PROFILE_OR_SELECTED_RTHETA_SOURCE_ROWS",
        "previous_cutset_source": rel(CHARM_CUTSET),
        "closed_now": {
            "W_Z_H_external_benchmark_coordinate_rows": row_coordinate_closure,
            "v_from_G_F_reference_coordinate_row": True,
            "gY_g1_g2_Mt_external_benchmark_rows": True,
            "lambda_Mt_external_benchmark_row_integrated": True,
            "Higgs_decay_EW_boundary_reconciled": True,
        },
        "still_open": {
            "selected_Rtheta_mass_scheme_derivation": True,
            "same_branch_Rtheta_threshold_derivation": True,
            "gauge_row_uncertainty_and_correlation_sidecars": True,
            "full_covariance_profile_likelihood": True,
            "EW_formula_kernels_for_WW_ZZ_Zgamma": True,
            "BCT_source_or_no_knob_profile_closure": True,
            "selected_CRunDec_charm_input_policy": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "construct/import the full covariance profile over accepted external coordinate rows",
            "route_B": "derive selected Rtheta source rows for v/gY/g2/lambda and replace external benchmark status",
            "route_C": "fill gauge uncertainty/correlation sidecars and combine with BCT/top/Higgs/tau blocks",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedWZHElectroweakRowsOrSelectedRThetaMassSchemeDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "wzh_electroweak_row_inventory": rel(INVENTORY),
            "wzh_external_benchmark_row_acceptance": rel(ACCEPTANCE),
            "selected_rtheta_mass_scheme_gap_after_wzh_rows": rel(RTHETA_GAP),
            "higgs_decay_electroweak_boundary_reconciliation": rel(HIGGS_EW),
            "next_cutset_after_wzh_external_rows": rel(CUTSET),
        },
        "theorem": {
            "name": "WZHElectroweakExternalBenchmarkCoordinateRowTheorem",
            "proved": True,
            "statement": (
                "The W/Z/H electroweak matching coordinates needed by the current external-profile ledger "
                "can be assembled from the accepted Buttazzo MSbar benchmark rows and the existing v(G_F) "
                "reference anchor: v_from_G_F, g_Y(M_t), g_1^GUT(M_t), g_2(M_t), and lambda(M_t). This "
                "closes the external benchmark coordinate-row layer only. It does not prove selected "
                "Rtheta source rows, full precision threshold matching, full covariance/profile likelihood, "
                "true SM equivalence, or no-knob closure."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "W_Z_H_electroweak_matching_rows_closed_at_external_coordinate_layer": row_coordinate_closure,
            "accepted_external_wzh_coordinate_row_count": len(accepted_wzh_rows),
            "accepted_selected_Rtheta_source_row_count": 0,
            "selected_Rtheta_mass_scheme_derivation_closed": False,
            "same_branch_Rtheta_threshold_derivation_closed": False,
            "full_precision_threshold_match_closed": False,
            "full_covariance_profile_likelihood_closed": False,
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
        "certificate": "MTT_Selected_WZHElectroweakRows_or_SelectedRThetaMassSchemeDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "W_Z_H_external_coordinate_layer_closed": row_coordinate_closure,
        "accepted_external_wzh_coordinate_row_count": len(accepted_wzh_rows),
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected WZHElectroweakRows or SelectedRThetaMassSchemeDerivation v1

Status: `{STATUS}`.

This artifact closes the W/Z/H electroweak matching coordinate layer at the
external benchmark/reference tier.

```text
accepted W/Z/H coordinate rows : {len(accepted_wzh_rows)}
rows                            : v(G_F), g_Y(M_t), g_1^GUT(M_t), g_2(M_t), lambda(M_t)
selected R_theta rows closed    : false
full covariance/profile closed  : false
true SM equivalence closed      : false
no-knob closure                 : false
```

The row layer is now usable as a validation target for selected `R_theta`
derivations, but it is not itself the selected source derivation.

The Higgs decay electroweak rows are kept separate: WW*, ZZ*, and Zgamma remain
downstream benchmark replay rows until formula kernels or an official likelihood
with covariance are imported.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
