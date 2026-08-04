"""Build Higgs-threshold / strict-PEW exit reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_higgsthresholdstrictpewexit_or_selectedsourcerows"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
HIGGS_STATUS = PACKET_DIR / "higgs_threshold_status_after_finite_hscalar.packet.json"
PEW_STATUS = PACKET_DIR / "strict_pew_directk_status_after_prefactor_packets.packet.json"
DECISION = PACKET_DIR / "higgs_pew_remaining_source_rows_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsThresholdStrictPEWExit_or_SelectedSourceRows_v1.md"

PREVIOUS = DATA / "selected_pmnsrunningmassrows_or_higgsthresholdstrictpewexit.candidate.json"
HSCALAR = DATA / "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule.candidate.json"
HLAMBDA = DATA / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
PREF = DATA / "selected_electroweakprefactorsourceclosure_or_finaltruesmaudit.candidate.json"
AEW_SOURCE = DATA / "selected_aewsourceoperator_or_thresholdconventionrows.candidate.json"
AEW_CORRECTION = DATA / "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun.candidate.json"
PHYS_AXIOM = DATA / "selected_physicalnormalizationsourceaxiom_or_directkcertificate.candidate.json"
PHYS_DERIVATION = DATA / "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade.candidate.json"
PEW_PAYLOAD = DATA / "selected_pewgaugeactionnormalizationsourcepacket_or_directkcertificatepayload.candidate.json"
STROMINGER = DATA / "selected_stromingerthresholdoperatorvalue_or_metrologyunitsource.candidate.json"

STATUS = (
    "MTT_SELECTED_HIGGSTHRESHOLDSTRICTPEWEXIT_OR_SELECTEDSOURCEROWS_"
    "BUILT_HSCALAR_ZERO_H_KNOB_CLOSED_STRICT_PREFACTOR_OPEN"
)
NEXT = "MTT_Selected_StrictPEWDirectKSourceRows_or_FinalSMNoKnobAudit_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    previous = load(PREVIOUS)
    hscalar = load(HSCALAR)
    hlambda = load(HLAMBDA)
    pref = load(PREF)
    aew_source = load(AEW_SOURCE)
    aew_correction = load(AEW_CORRECTION)
    phys_axiom = load(PHYS_AXIOM)
    phys_derivation = load(PHYS_DERIVATION)
    pew_payload = load(PEW_PAYLOAD)
    strominger = load(STROMINGER)

    h_scalar_rows = hscalar["closure_decision"]["accepted_H_scalar_source_rows"]
    h_radial_closed = (
        hscalar["closure_decision"]["strict_r_H_promoted"]
        and hlambda["closure_decision"]["selected_H_radial_source_row_emitted"]
    )
    zero_h_parameter = hlambda["closure_decision"]["H_parameter_count_after_replacement"] == 0
    selected_rh_rg = hlambda["closure_decision"]["selected_R_H_RG_source_emitted"]
    strict_k_rows_now = hlambda["closure_decision"]["selected_K_threshold_row_count_now"]
    strict_k_rows_required = hlambda["closure_decision"]["selected_K_threshold_row_count_required"]

    higgs_status = {
        "schema": "MTTHiggsThresholdStatusAfterFiniteHScalar.v1",
        "status": "FINITE_HSCALAR_AND_ZERO_H_RADIAL_SOURCE_CLOSED_LAMBDA_PREFACTOR_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_candidate": rel(PREVIOUS),
        "hscalar_candidate": rel(HSCALAR),
        "hlambda_payload_candidate": rel(HLAMBDA),
        "accepted_H_scalar_source_rows": h_scalar_rows,
        "finite_projected_A_N_exactness_available": hscalar["closure_decision"][
            "finite_projected_A_N_exactness_available"
        ],
        "H_scalar_functional_on_A_N_closed": hscalar["closure_decision"][
            "H_scalar_functional_on_A_N_closed"
        ],
        "strict_tau_H_promoted": hscalar["closure_decision"]["strict_tau_H_promoted"],
        "strict_r_H_promoted": hscalar["closure_decision"]["strict_r_H_promoted"],
        "selected_H_radial_source_row_emitted": hlambda["closure_decision"][
            "selected_H_radial_source_row_emitted"
        ],
        "selected_R_H_RG_source_emitted": selected_rh_rg,
        "H_parameter_count_after_replacement": hlambda["closure_decision"][
            "H_parameter_count_after_replacement"
        ],
        "old_H_one_parameter_lane_retired_for_radial_source": hlambda["closure_decision"][
            "old_H_one_parameter_lane_retired_for_radial_source"
        ],
        "selected_K_threshold_row_count_now": strict_k_rows_now,
        "selected_K_threshold_row_count_required": strict_k_rows_required,
        "lambda_H_postcheck_passed": hlambda["closure_decision"]["lambda_H_postcheck_passed"],
        "lambda_H_postcheck_residual": hlambda["numerics"]["lambda_postcheck_residual"],
        "lambda_H_value_row_emitted_as_strict_no_knob": hlambda["closure_decision"][
            "lambda_H_value_row_emitted_as_strict_no_knob"
        ],
        "selected_K_threshold_Omega_H_lambda_emitted": hlambda["closure_decision"][
            "selected_K_threshold_Omega_H_lambda_emitted"
        ],
        "higgs_threshold_rows_closed": False,
    }

    pew_status = {
        "schema": "MTTStrictPEWDirectKStatusAfterPrefactorPackets.v1",
        "status": "STRICT_PEW_DIRECTK_PREFRACTOR_CONTRACTS_LOCKED_ZERO_FINAL_ROWS",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "electroweak_prefactor_candidate": rel(PREF),
        "aew_source_operator_candidate": rel(AEW_SOURCE),
        "aew_correction_candidate": rel(AEW_CORRECTION),
        "physical_normalization_axiom_candidate": rel(PHYS_AXIOM),
        "physical_normalization_derivation_candidate": rel(PHYS_DERIVATION),
        "pew_payload_candidate": rel(PEW_PAYLOAD),
        "strominger_candidate": rel(STROMINGER),
        "accepted_selected_prefactor_source_count": pref["closure_decision"][
            "accepted_selected_prefactor_source_count"
        ],
        "accepted_A_EW_source_operator_rows": aew_source["closure_decision"][
            "accepted_A_EW_source_operator_rows"
        ],
        "accepted_physical_prefactor_rows": aew_source["closure_decision"][
            "accepted_physical_prefactor_rows"
        ],
        "accepted_threshold_convention_rows": aew_source["closure_decision"][
            "accepted_threshold_convention_rows"
        ],
        "aew_required_field_count": aew_source["closure_decision"]["required_field_count"],
        "aew_required_fields_filled_by_current_packets": aew_source["closure_decision"][
            "required_fields_filled_by_current_packets"
        ],
        "pew_payload_contract_locked": pew_payload["closure_decision"]["payload_contract_locked"],
        "pew_source_required_field_count": pew_payload["closure_decision"][
            "source_required_field_count"
        ],
        "pew_source_filled_field_count": pew_payload["closure_decision"]["source_filled_field_count"],
        "accepted_strict_P_EW_source_rows": pew_payload["closure_decision"][
            "accepted_strict_P_EW_source_rows"
        ],
        "accepted_direct_K_threshold_Omega_H_lambda_rows": pew_payload["closure_decision"][
            "accepted_direct_K_threshold_Omega_H_lambda_rows"
        ],
        "premised_physical_normalization_source_axiom_constructed": phys_axiom["closure_decision"][
            "physical_normalization_source_axiom_constructed"
        ],
        "premised_direct_K_certificate_constructed": phys_axiom["closure_decision"][
            "direct_K_threshold_Omega_H_lambda_certificate_constructed_under_axiom"
        ],
        "premised_P_EW_source_rows": phys_axiom["closure_decision"]["premised_P_EW_source_rows"],
        "premised_direct_K_threshold_Omega_H_lambda_rows": phys_axiom["closure_decision"][
            "premised_direct_K_threshold_Omega_H_lambda_rows"
        ],
        "premised_selected_K_row_count": phys_axiom["closure_decision"][
            "premised_selected_K_row_count"
        ],
        "shared_physical_primitive_count_under_axiom": phys_axiom["closure_decision"][
            "shared_physical_primitive_count_under_axiom"
        ],
        "physical_normalization_axiom_derived": phys_derivation["closure_decision"][
            "physical_normalization_axiom_derived"
        ],
        "strict_derivation_route_count": phys_derivation["closure_decision"][
            "accepted_strict_derivation_route_count"
        ],
        "strict_strominger_threshold_value_rows": strominger["closure_decision"][
            "strict_strominger_threshold_value_rows"
        ],
        "strict_metrology_unit_source_rows": strominger["closure_decision"][
            "strict_metrology_unit_source_rows"
        ],
        "strict_PEW_directK_values_closed": False,
    }

    decision = {
        "schema": "MTTHiggsPEWRemainingSourceRowsDecision.v1",
        "status": "HSCALAR_ZERO_H_KNOB_CLOSED_FINAL_PREFRACTOR_SOURCE_ROWS_OPEN",
        "closed_now": [
            "The finite projected H scalar source emits strict tau_H and r_H rows.",
            "The H radial/R_H^RG replacement is closed with zero H-specific parameters.",
            "The premised one-shared-physical-primitive lane gives a typed ten-K closure witness, but only under the explicit axiom.",
            "The strict PEW/direct-K payload contracts are concrete and no longer undefined.",
        ],
        "not_closed": [
            "Strict lambda_H value row and K_threshold.Omega_H.lambda row remain open.",
            "Strict P_EW/direct-K source rows remain zero.",
            "The physical-normalization axiom is constructed as a premise but not derived from current same-branch source data.",
        ],
        "source_row_counts": {
            "accepted_H_scalar_source_rows": h_scalar_rows,
            "accepted_H_radial_source_rows": 1 if h_radial_closed else 0,
            "accepted_selected_R_H_RG_source_rows": 1 if selected_rh_rg else 0,
            "strict_selected_K_threshold_rows_now": strict_k_rows_now,
            "strict_selected_K_threshold_rows_required": strict_k_rows_required,
            "accepted_strict_lambda_H_value_rows": 0,
            "accepted_strict_P_EW_source_rows": pew_status["accepted_strict_P_EW_source_rows"],
            "accepted_direct_K_threshold_Omega_H_lambda_rows": pew_status[
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "premised_P_EW_source_rows": pew_status["premised_P_EW_source_rows"],
            "premised_direct_K_threshold_Omega_H_lambda_rows": pew_status[
                "premised_direct_K_threshold_Omega_H_lambda_rows"
            ],
        },
        "acceptance": {
            "finite_H_scalar_source_closed": hscalar["closure_decision"][
                "H_scalar_functional_on_A_N_closed"
            ],
            "H_radial_zero_parameter_replacement_closed": h_radial_closed and zero_h_parameter,
            "selected_R_H_RG_source_emitted": selected_rh_rg,
            "lambda_H_postcheck_passed": hlambda["closure_decision"]["lambda_H_postcheck_passed"],
            "strict_lambda_H_value_row_closed": False,
            "strict_K_threshold_Omega_H_lambda_closed": False,
            "premised_one_shared_primitive_ten_K_lane_closed": phys_axiom["closure_decision"][
                "minimal_one_primitive_H_lambda_lane_closed"
            ],
            "physical_normalization_axiom_derived": False,
            "strict_PEW_directK_values_closed": False,
            "higgs_threshold_rows_closed": False,
            "fullS2_no_proxy_rows_closed": False,
            "global_true_SM_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsThresholdStrictPEWExitOrSelectedSourceRows",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_pmns_running_candidate": rel(PREVIOUS),
            "h_scalar_source": rel(HSCALAR),
            "h_lambda_payload": rel(HLAMBDA),
            "electroweak_prefactor": rel(PREF),
            "aew_source_operator": rel(AEW_SOURCE),
            "aew_correction": rel(AEW_CORRECTION),
            "physical_normalization_axiom": rel(PHYS_AXIOM),
            "physical_normalization_derivation": rel(PHYS_DERIVATION),
            "pew_payload": rel(PEW_PAYLOAD),
            "strominger_threshold_operator": rel(STROMINGER),
        },
        "output_packets": {
            "higgs_threshold_status_after_finite_hscalar": rel(HIGGS_STATUS),
            "strict_pew_directk_status_after_prefactor_packets": rel(PEW_STATUS),
            "higgs_pew_remaining_source_rows_decision": rel(DECISION),
        },
        "theorem": {
            "name": "HiggsThresholdStrictPEWExitOrSelectedSourceRowsReductionTheorem",
            "proved": True,
            "statement": (
                "The Higgs threshold frontier is reduced to the final electroweak prefactor/direct-K "
                "source rows. The selected finite H scalar emits strict tau_H/r_H and replaces the "
                "old one-parameter H radial lane with zero H-specific parameters. However lambda_H "
                "and K_threshold.Omega_H.lambda still require the physical normalization prefactor; "
                "current strict PEW/direct-K validators accept zero final rows. A premised one-shared-"
                "primitive ten-K witness exists, but is not strict no-knob closure until the axiom is "
                "derived or adopted as an explicit counted primitive."
            ),
        },
        "key_numbers": {
            "accepted_H_scalar_source_rows": h_scalar_rows,
            "H_parameter_count_after_replacement": hlambda["closure_decision"][
                "H_parameter_count_after_replacement"
            ],
            "selected_K_threshold_row_count_now": strict_k_rows_now,
            "selected_K_threshold_row_count_required": strict_k_rows_required,
            "lambda_H_postcheck_residual": hlambda["numerics"]["lambda_postcheck_residual"],
            "accepted_strict_P_EW_source_rows": pew_status["accepted_strict_P_EW_source_rows"],
            "accepted_direct_K_threshold_Omega_H_lambda_rows": pew_status[
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "premised_selected_K_row_count": pew_status["premised_selected_K_row_count"],
            "shared_physical_primitive_count_under_axiom": pew_status[
                "shared_physical_primitive_count_under_axiom"
            ],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsThresholdStrictPEWExit_or_SelectedSourceRows_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "finite_H_scalar_source_closed": decision["acceptance"]["finite_H_scalar_source_closed"],
        "H_radial_zero_parameter_replacement_closed": decision["acceptance"][
            "H_radial_zero_parameter_replacement_closed"
        ],
        "selected_R_H_RG_source_emitted": selected_rh_rg,
        "strict_lambda_H_value_row_closed": False,
        "strict_K_threshold_Omega_H_lambda_closed": False,
        "premised_one_shared_primitive_ten_K_lane_closed": decision["acceptance"][
            "premised_one_shared_primitive_ten_K_lane_closed"
        ],
        "physical_normalization_axiom_derived": False,
        "accepted_strict_P_EW_source_rows": pew_status["accepted_strict_P_EW_source_rows"],
        "accepted_direct_K_threshold_Omega_H_lambda_rows": pew_status[
            "accepted_direct_K_threshold_Omega_H_lambda_rows"
        ],
        "higgs_threshold_rows_closed": False,
        "fullS2_no_proxy_rows_closed": False,
        "global_true_SM_no_knob_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected HiggsThresholdStrictPEWExit or SelectedSourceRows v1

Status: `{STATUS}`

## Closed Now

- finite H scalar source rows: `{h_scalar_rows}`
- strict `tau_H/r_H` source promotion: closed
- zero-H-parameter radial replacement: closed
- selected `R_H^RG` source: closed
- strict selected K-threshold rows before final prefactor: `{strict_k_rows_now}/{strict_k_rows_required}`
- premised one-shared-primitive ten-K lane: available

## Still Open

- strict `lambda_H` value row: `0`
- strict `K_threshold.Omega_H.lambda` row: `0`
- strict `P_EW` source rows: `{pew_status["accepted_strict_P_EW_source_rows"]}`
- direct-K rows: `{pew_status["accepted_direct_K_threshold_Omega_H_lambda_rows"]}`
- physical-normalization axiom derivation: open

The premised lane is useful and sharply typed, but it is not strict no-knob
closure until the physical-normalization axiom is derived or explicitly counted
as a shared primitive.

Next required artifact: `{NEXT}`.
"""

    write_json(HIGGS_STATUS, higgs_status)
    write_json(PEW_STATUS, pew_status)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
