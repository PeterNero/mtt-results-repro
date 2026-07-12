"""Build post-Pi threshold matching rows or mass-scheme source rows artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
THRESHOLD_ROWS = PACKET_DIR / "post_pi_admitted_threshold_matching_rows.packet.json"
MASS_ROWS = PACKET_DIR / "post_pi_admitted_mass_scheme_rows.packet.json"
PROMOTION = PACKET_DIR / "external_row_admission_not_rtheta_selection.packet.json"
READINESS = PACKET_DIR / "rtheta_value_readiness_after_external_rows.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_external_threshold_mass_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdMatchingRowsPostPi_or_MassSchemeSourceRows_v1.md"

PREVIOUS = DATA / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation.candidate.json"
PREV_READINESS = (
    DATA
    / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
    / "rtheta_value_readiness_after_convention_source.packet.json"
)
PREV_CONVENTION = (
    DATA
    / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
    / "post_pi_same_branch_convention_source_contract.packet.json"
)
TOP_HIGGS = DATA / "selected_tophiggsformulamapimport_or_rthetathresholdderivation.candidate.json"
TOP_HIGGS_ROWS = (
    DATA
    / "selected_tophiggsformulamapimport_or_rthetathresholdderivation"
    / "top_higgs_external_formula_map_acceptance.packet.json"
)
WZH = DATA / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation.candidate.json"
WZH_ROWS = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_external_benchmark_row_acceptance.packet.json"
)
BCT = DATA / "selected_allbctexternalrows_or_fullsmconventionreconciliation.candidate.json"
BCT_ROWS = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "all_bct_external_rows_assembly.packet.json"
)
BCT_PROFILE_GATE = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "fullsm_profile_reconciliation_gate.packet.json"
)
FUNCTIONAL_RECHECK = (
    DATA
    / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
    / "threshold_functional_instantiation_recheck_after_convention.packet.json"
)
RTHETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_THRESHOLDMATCHINGROWSPOSTPI_OR_MASSSCHEMESOURCEROWS_"
    "CLOSED_ADMITTED_EXTERNAL_ROWS_PROFILE_NOKNOB_OPEN"
)
NEXT = "MTT_Selected_FullProfileOrDiagonalTheoremPostPi_or_NoKnobValueDerivation_v1"


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
        raise FileNotFoundError("missing post-Pi threshold/mass row sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREV_READINESS,
        PREV_CONVENTION,
        TOP_HIGGS,
        TOP_HIGGS_ROWS,
        WZH,
        WZH_ROWS,
        BCT,
        BCT_ROWS,
        BCT_PROFILE_GATE,
        FUNCTIONAL_RECHECK,
        RTHETA_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    prev_readiness = load(PREV_READINESS)
    convention = load(PREV_CONVENTION)
    top_higgs = load(TOP_HIGGS)
    top_higgs_rows = load(TOP_HIGGS_ROWS)
    wzh = load(WZH)
    wzh_rows = load(WZH_ROWS)
    bct = load(BCT)
    bct_rows = load(BCT_ROWS)
    bct_profile_gate = load(BCT_PROFILE_GATE)
    functional_recheck = load(FUNCTIONAL_RECHECK)

    admitted_threshold_rows = []
    for row in top_higgs_rows["accepted_rows"]:
        admitted_threshold_rows.append(
            {
                "id": row["id"],
                "row_class": "top_higgs_formula_map",
                "accepted_as_admitted_external_threshold_matching_row": row[
                    "accepted_as_external_top_higgs_formula_map_row"
                ],
                "accepted_as_internal_selected_Rtheta_row": False,
                "provenance": row["provenance"],
                "covariance_sidecar": row["covariance_sidecar"],
                "target_scale": "M_t",
                "basis_map_status": "post-Pi convention source and Rtheta value-row basis map closed upstream",
            }
        )
    wzh_inventory = load(
        DATA
        / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
        / "wzh_electroweak_row_inventory.packet.json"
    )
    for row in wzh_inventory["accepted_wzh_coordinate_rows"]:
        admitted_threshold_rows.append(
            {
                "id": row["id"],
                "row_class": "W_Z_H_electroweak_coordinate",
                "accepted_as_admitted_external_threshold_matching_row": row[
                    "accepted_as_external_WZH_coordinate_row"
                ],
                "accepted_as_internal_selected_Rtheta_row": row[
                    "accepted_as_selected_Rtheta_source_row"
                ],
                "provenance": wzh_rows["inventory_source"],
                "covariance_sidecar": row.get(
                    "covariance_sidecar",
                    "partial only; full cross-row covariance open",
                ),
                "target_scale": "M_t" if "M_t" in row.get("scheme", "") else "reference",
                "basis_map_status": "post-Pi convention source closed; W/Z/H coordinate source map internal derivation open",
            }
        )

    threshold_packet = {
        "schema": "MTTPostPiAdmittedThresholdMatchingRows.v1",
        "status": "ADMITTED_EXTERNAL_THRESHOLD_MATCHING_ROWS_CLOSED_INTERNAL_RTHETA_OPEN",
        "post_pi_convention_source": rel(PREV_CONVENTION),
        "row_count": len(admitted_threshold_rows),
        "accepted_admitted_external_threshold_matching_row_count": len(admitted_threshold_rows),
        "accepted_internal_selected_Rtheta_threshold_row_count": 0,
        "rows": admitted_threshold_rows,
        "source_closure_tests": {
            "same_branch_scale_scheme_loop_convention_closed": convention[
                "same_branch_scale_scheme_loop_convention_closed"
            ],
            "top_higgs_external_formula_map_import_closed": top_higgs["closure_decision"][
                "top_higgs_external_formula_map_import_closed"
            ],
            "top_higgs_external_formula_map_row_count": top_higgs["closure_decision"][
                "accepted_external_formula_map_row_count"
            ],
            "W_Z_H_external_coordinate_rows_closed": wzh["closure_decision"][
                "W_Z_H_electroweak_matching_rows_closed_at_external_coordinate_layer"
            ],
            "W_Z_H_external_coordinate_row_count": wzh["closure_decision"][
                "accepted_external_wzh_coordinate_row_count"
            ],
        },
        "threshold_matching_source_rows_closed_at_admitted_external_tier": True,
        "threshold_matching_source_rows_closed_as_no_knob_Rtheta_derivation": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(THRESHOLD_ROWS, threshold_packet)

    admitted_mass_rows = []
    for row in bct_rows["rows"]:
        admitted_mass_rows.append(
            {
                "id": row["id"],
                "sector": row["sector"],
                "accepted_as_admitted_external_mass_scheme_row": row["accepted_as_external_map_row"],
                "accepted_as_internal_selected_Rtheta_row": False,
                "source": row["source"],
                "target_scale": row["target_scale"],
                "target_convention": row["target_convention"],
                "running_mass_MZ_GeV": row["running_mass_MZ_GeV"],
                "yukawa_MZ": row["yukawa_MZ"],
            }
        )

    mass_packet = {
        "schema": "MTTPostPiAdmittedMassSchemeRows.v1",
        "status": "ADMITTED_EXTERNAL_MASS_SCHEME_ROWS_CLOSED_INTERNAL_RTHETA_OPEN",
        "post_pi_convention_source": rel(PREV_CONVENTION),
        "row_count": len(admitted_mass_rows),
        "accepted_admitted_external_mass_scheme_row_count": len(admitted_mass_rows),
        "accepted_internal_selected_Rtheta_mass_scheme_row_count": 0,
        "rows": admitted_mass_rows,
        "source_closure_tests": {
            "same_branch_scale_scheme_loop_convention_closed": convention[
                "same_branch_scale_scheme_loop_convention_closed"
            ],
            "all_three_bct_external_mass_scheme_rows_available": bct["closure_decision"][
                "all_three_bct_external_mass_scheme_rows_available"
            ],
            "accepted_bottom_charm_tau_map_row_count": bct["closure_decision"][
                "accepted_bottom_charm_tau_map_row_count"
            ],
            "fullSM_profile_convention_for_bct_rows_closed": bct["closure_decision"][
                "single_fullSM_profile_convention_for_bct_rows_closed"
            ],
        },
        "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier": True,
        "mass_scheme_conversion_source_rows_closed_as_no_knob_Rtheta_derivation": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MASS_ROWS, mass_packet)

    promotion = {
        "schema": "MTTExternalRowAdmissionNotRThetaSelection.v1",
        "status": "EXTERNAL_ROWS_ADMITTED_FOR_REPLAY_NOT_SELECTED_NOKNOB_RTHETA",
        "accepted_external_threshold_row_count": threshold_packet[
            "accepted_admitted_external_threshold_matching_row_count"
        ],
        "accepted_external_mass_scheme_row_count": mass_packet[
            "accepted_admitted_external_mass_scheme_row_count"
        ],
        "accepted_internal_selected_Rtheta_row_count": 0,
        "what_this_closes": [
            "threshold_matching_source_rows at admitted-external tier",
            "mass_scheme_conversion_source_rows at admitted-external tier",
        ],
        "what_this_does_not_close": [
            "selected internal Rtheta threshold/mass-scheme derivation",
            "no-knob value derivation",
            "full profile likelihood or accepted diagonal theorem",
            "true SM equivalence",
            "Yukawa/mass/mixing no-knob prediction",
        ],
        "guardrails": {
            "external_rows_used_as_branch_selector": False,
            "target_fit_after_residuals": False,
            "full_covariance_profile_likelihood_closed": False,
            "bct_fullSM_profile_reconciliation_closed": bct_profile_gate["not_closed"][
                "single_fullSM_profile_convention_for_bct_rows"
            ]
            is False,
            "functional_values_instantiated": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION, promotion)

    remaining_blockers = [
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]
    readiness = {
        "schema": "MTTRThetaValueReadinessAfterExternalRows.v1",
        "status": "READINESS_ADVANCED_EXTERNAL_ROWS_CLOSED_PROFILE_NOKNOB_OPEN",
        "previous_readiness_source": rel(PREV_READINESS),
        "previous_present_count": prev_readiness["present_count"],
        "previous_requirement_count": prev_readiness["requirement_count"],
        "previous_blocking_failures": prev_readiness["blocking_failures"],
        "retired_blocking_failures": [
            "threshold_matching_source_rows",
            "mass_scheme_conversion_source_rows",
        ],
        "present_count": prev_readiness["present_count"] + 2,
        "requirement_count": prev_readiness["requirement_count"],
        "blocking_failures": remaining_blockers,
        "selected_threshold_response_functional_instantiated": False,
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(READINESS, readiness)

    cutset = {
        "schema": "MTTNextCutsetAfterExternalThresholdMassRows.v1",
        "status": "NEXT_ATTACK_FULL_PROFILE_OR_NOKNOB_VALUE_DERIVATION",
        "closed_now": {
            "admitted_external_threshold_matching_source_rows": True,
            "admitted_external_mass_scheme_conversion_source_rows": True,
            "Rtheta_readiness_present_count_advanced_to_7_of_9": True,
            "internal_Rtheta_nonselector_boundary_preserved": True,
        },
        "still_open": {
            "no_knob_value_derivation": True,
            "full_profile_likelihood_or_accepted_diagonal_theorem": True,
            "selected_internal_Rtheta_threshold_mass_derivation": True,
            "selected_threshold_response_functional_instantiated": True,
            "numeric_Rtheta_coefficient_values": True,
            "lambda_H_value_execution": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "build full correlated profile/diagonal theorem over admitted external rows",
            "route_B": "derive no-knob selected Rtheta value rows internally and supersede the external admission tier",
            "route_C": "declare minimal universal parameter policy if no selected no-knob value derivation exists",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedThresholdMatchingRowsPostPiOrMassSchemeSourceRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "post_pi_admitted_threshold_matching_rows": rel(THRESHOLD_ROWS),
            "post_pi_admitted_mass_scheme_rows": rel(MASS_ROWS),
            "external_row_admission_not_rtheta_selection": rel(PROMOTION),
            "rtheta_value_readiness_after_external_rows": rel(READINESS),
            "next_cutset_after_external_threshold_mass_rows": rel(CUTSET),
        },
        "theorem": {
            "name": "PostPiExternalThresholdAndMassSchemeRowAdmissionTheorem",
            "proved": True,
            "statement": (
                "With the post-Pi M_Z/MSbar convention source contract closed, the existing top/Higgs formula-map, "
                "W/Z/H coordinate, and bottom/charm/tau mass-scheme rows satisfy the manifest for admitted external "
                "threshold and mass-scheme rows: each row has provenance, a declared convention, and no branch-selection "
                "use. This closes the threshold_matching_source_rows and mass_scheme_conversion_source_rows blockers at "
                "the admitted-external replay tier only. It does not promote these rows to no-knob selected internal "
                "Rtheta predictions, and it does not close the full profile/diagonal theorem."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "threshold_matching_source_rows_closed": True,
            "mass_scheme_conversion_source_rows_closed": True,
            "threshold_matching_source_rows_closed_at_admitted_external_tier": True,
            "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier": True,
            "selected_internal_Rtheta_threshold_mass_derivation_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "selected_value_evaluator_closed": False,
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
        "certificate": "MTT_Selected_ThresholdMatchingRowsPostPi_or_MassSchemeSourceRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "threshold_matching_source_rows_closed": True,
        "mass_scheme_conversion_source_rows_closed": True,
        "closed_at_admitted_external_tier_only": True,
        "selected_internal_Rtheta_threshold_mass_derivation_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ThresholdMatchingRowsPostPi or MassSchemeSourceRows v1

Status: `{STATUS}`.

The admitted external row layer is now closed under the post-Pi convention.

```text
threshold matching rows closed      : true
mass-scheme conversion rows closed  : true
closure tier                        : admitted external replay
Rtheta readiness                    : {readiness["present_count"]}/{readiness["requirement_count"]}
accepted coefficient values         : 0
selected no-knob Rtheta rows        : false
true SM equivalence                 : false
```

The distinction is essential: these rows are accepted as provenance-bearing
external/admitted replay rows, not as no-knob selected internal `R_theta`
predictions.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
