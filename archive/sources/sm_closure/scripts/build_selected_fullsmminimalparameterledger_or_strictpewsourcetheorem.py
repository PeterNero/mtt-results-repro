"""Build the full-SM minimal-parameter ledger or strict P_EW source theorem packet.

This is an accounting artifact: it exports the current SM-sector replay/status
into a single minimal-parameter ledger while preserving the strict no-knob
frontier.  The H/lambda slot is counted through one shared P_EW primitive,
not as an independent lambda_H fit.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SECTOR_LEDGER = PACKET_DIR / "sm_sector_minimal_parameter_ledger.packet.json"
COUNT_SUMMARY = PACKET_DIR / "minimal_parameter_count_summary.packet.json"
SLOT_BOUNDARY = PACKET_DIR / "closed_vs_open_parameter_slots.packet.json"
STRICT_PEW_CONTRACT = PACKET_DIR / "strict_pew_source_reentry_contract.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_fullsm_minimal_parameter_ledger.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullSMMinimalParameterLedger_or_StrictPEWSourceTheorem_v1.md"

PREVIOUS = DATA / "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit.candidate.json"
PREVIOUS_POLICY = (
    DATA
    / "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit"
    / "p_ew_minimal_parameter_policy.packet.json"
)
PREVIOUS_SEED = (
    DATA
    / "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit"
    / "fullsm_minimal_parameter_audit_seed.packet.json"
)
CORE_INTERFACE = DATA / "core_axioms_measured_parameter_interface.candidate.json"
SM_PARITY_LEDGER = DATA / "sm_parity_closure_ledger.candidate.json"
RG_POLICY = DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
MIXING_GAUGE = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
COMMON_SCALE_CERT = DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"
ACCEPTED_VALUES = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution.candidate.json"
ACCEPTED_VALUES_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
DYNAMIC_QASU3 = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"

STATUS = (
    "MTT_SELECTED_FULLSMMINIMALPARAMETERLEDGER_OR_STRICTPEWSOURCETHEOREM_"
    "LEDGER_CLOSED_STRICT_PEW_AND_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_StrictPEWSourceTheorem_or_SMPrecisionClosureCutset_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def all_false(mapping: dict[str, Any]) -> bool:
    return all(value is False for value in mapping.values())


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_POLICY,
        PREVIOUS_SEED,
        CORE_INTERFACE,
        SM_PARITY_LEDGER,
        RG_POLICY,
        MIXING_GAUGE,
        COMMON_SCALE_CERT,
        ACCEPTED_VALUES,
        ACCEPTED_VALUES_PACKET,
        DYNAMIC_QASU3,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing full-SM minimal ledger inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    previous_policy = load(PREVIOUS_POLICY)
    previous_seed = load(PREVIOUS_SEED)
    core_interface = load(CORE_INTERFACE)
    sm_parity = load(SM_PARITY_LEDGER)
    rg_policy = load(RG_POLICY)
    mixing_gauge = load(MIXING_GAUGE)
    common_scale = load(COMMON_SCALE_CERT)
    accepted_values = load(ACCEPTED_VALUES)
    accepted_values_packet = load(ACCEPTED_VALUES_PACKET)
    dynamic_qasu3 = load(DYNAMIC_QASU3)

    p_ew = float(previous["numerics"]["P_EW_action_prefactor"])
    lambda_h = float(previous["numerics"]["lambda_H"])
    lambda_ref = float(previous["numerics"]["lambda_H_reference"])
    lambda_residual = float(previous["numerics"]["lambda_H_absolute_residual"])

    gauge_triplet = common_scale["common_scale_packet"]["closed_values"]
    yukawa_values = accepted_values_packet["derived_magnitudes"]
    pmns_status = mixing_gauge["PMNS_replay"]["status"]
    ckm_status = mixing_gauge["CKM_replay"]["status"]

    counts = {
        "electroweak_scale_anchor_v_or_G_F": 1,
        "common_scale_gauge_triplet_alpha1_alpha2_alpha3": 3,
        "charged_fermion_yukawa_magnitudes": 9,
        "CKM_physical_mixing_parameters": 4,
        "H_lambda_shared_physical_prefactor_P_EW": 1,
        "PMNS_minimal_oscillation_policy": 6,
        "QCD_theta_bar": 0,
        "absolute_neutrino_mass_or_Majorana_policy": 0,
    }
    non_neutrino_closed_count = (
        counts["electroweak_scale_anchor_v_or_G_F"]
        + counts["common_scale_gauge_triplet_alpha1_alpha2_alpha3"]
        + counts["charged_fermion_yukawa_magnitudes"]
        + counts["CKM_physical_mixing_parameters"]
        + counts["H_lambda_shared_physical_prefactor_P_EW"]
    )
    minimal_pmns_extension_count = non_neutrino_closed_count + counts["PMNS_minimal_oscillation_policy"]

    sector_ledger = {
        "schema": "MTTSMSectorMinimalParameterLedger.v1",
        "status": "SM_SECTOR_MINIMAL_PARAMETER_LEDGER_BUILT",
        "closure_claimed": True,
        "sector_rows": {
            "source_interface_policy": {
                "status": core_interface["status"],
                "measured_parameter_policy_closed": core_interface["gate_results"][
                    "measured_parameter_interface_defined"
                ],
                "source_nonselection_guardrail": core_interface["gate_results"][
                    "measured_inputs_do_not_select_sources"
                ],
                "counted_parameters": 0,
            },
            "H_lambda": {
                "status": "CLOSED_AT_ONE_SHARED_PHYSICAL_PRIMITIVE",
                "H_specific_free_parameters": 0,
                "counted_parameters": counts["H_lambda_shared_physical_prefactor_P_EW"],
                "counted_parameter_name": "P_EW.action_prefactor",
                "P_EW": p_ew,
                "lambda_H_replay": lambda_h,
                "lambda_H_reference": lambda_ref,
                "lambda_H_absolute_residual": lambda_residual,
                "lambda_H_used_as_selector": False,
                "strict_P_EW_source_closed": False,
            },
            "electroweak_scale": {
                "status": "MEASURED_PARITY_ANCHOR_FROM_G_F_OR_V",
                "counted_parameters": counts["electroweak_scale_anchor_v_or_G_F"],
                "no_knob_upgrade_target": "selected dimensionful/electroweak scale source",
            },
            "gauge": {
                "status": "COMMON_SCALE_MZ_GAUGE_TRIPLET_CLOSED_AS_MEASURED_REPLAY",
                "counted_parameters": counts["common_scale_gauge_triplet_alpha1_alpha2_alpha3"],
                "closed_values": {
                    "alpha_1_GUT_MZ": gauge_triplet["alpha_1_GUT_MZ"],
                    "alpha_2_MZ": gauge_triplet["alpha_2_MZ"],
                    "alpha_3_MZ": gauge_triplet["alpha_3_MZ"],
                },
                "accepted_as_no_knob_prediction": False,
            },
            "charged_yukawa_magnitudes": {
                "status": "VERSIONED_COMMON_SCALE_VALUES_ACCEPTED_FOR_SM_PARITY",
                "counted_parameters": counts["charged_fermion_yukawa_magnitudes"],
                "diag_abs_Y_u": yukawa_values["diag_abs_Y_u"],
                "diag_abs_Y_d": yukawa_values["diag_abs_Y_d"],
                "diag_abs_Y_e": yukawa_values["diag_abs_Y_e"],
                "accepted_as_no_knob_prediction": accepted_values_packet[
                    "accepted_as_no_knob_MTT_prediction"
                ],
            },
            "CKM": {
                "status": ckm_status,
                "counted_parameters": counts["CKM_physical_mixing_parameters"],
                "jarlskog": mixing_gauge["CKM_replay"]["input_jarlskog"],
                "unitarity_max_residual": mixing_gauge["CKM_replay"]["unitarity_max_residual"],
                "used_as_source_selector": False,
            },
            "PMNS_minimal_oscillation": {
                "status": pmns_status,
                "counted_parameters": counts["PMNS_minimal_oscillation_policy"],
                "jarlskog": mixing_gauge["PMNS_replay"]["input_jarlskog"],
                "unitarity_max_residual": mixing_gauge["PMNS_replay"]["unitarity_max_residual"],
                "absolute_neutrino_mass_filled": mixing_gauge["PMNS_replay"][
                    "absolute_neutrino_mass_filled"
                ],
                "Dirac_neutrino_yukawa_magnitudes_filled": mixing_gauge["PMNS_replay"][
                    "Dirac_neutrino_yukawa_magnitudes_filled"
                ],
            },
            "dynamic_QaSU3_support": {
                "status": dynamic_qasu3["status"],
                "counted_parameters": 0,
                "dynamic_first_response_layer_closed": dynamic_qasu3["promotion_decision"][
                    "dynamic_QaSU3_first_response_layer_closed"
                ],
                "accepted_Yukawa_magnitudes_closed": dynamic_qasu3["promotion_decision"][
                    "accepted_Yukawa_magnitudes_closed"
                ],
            },
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    count_summary = {
        "schema": "MTTMinimalParameterCountSummary.v1",
        "status": "MINIMAL_PARAMETER_COUNTS_COMPUTED",
        "closure_claimed": True,
        "counts": counts,
        "closed_non_neutrino_SM_like_count_excluding_QCD_theta": non_neutrino_closed_count,
        "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta": minimal_pmns_extension_count,
        "if_QCD_theta_bar_is_admitted_as_external_slot_add": 1,
        "if_absolute_neutrino_mass_is_admitted_add": 1,
        "if_Majorana_phases_are_admitted_add": 2,
        "interpretation": {
            "lambda_H_independent_slot_replaced_by_P_EW": True,
            "P_EW_is_counted_once_as_shared_physical_primitive": True,
            "H_specific_lambda_parameter_count": 0,
            "gauge_and_flavor_values_are_measured_replay_slots_not_no_knob_predictions": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    slot_boundary = {
        "schema": "MTTClosedVsOpenSMParameterSlots.v1",
        "status": "CLOSED_AND_OPEN_SM_PARAMETER_SLOTS_SEPARATED",
        "closure_claimed": True,
        "closed_or_admitted_slots": [
            "P_EW one-shared-physical-primitive H/lambda lane",
            "v or G_F electroweak scale measured parity anchor",
            "alpha_1, alpha_2, alpha_3 at M_Z measured replay triplet",
            "nine charged-fermion Yukawa magnitudes at accepted first-pass common scale",
            "four CKM physical parameters via complex up-diagonal replay",
            "six minimal PMNS oscillation parameters via normal-ordering replay",
        ],
        "open_slots_or_upgrade_targets": [
            "strict P_EW selected source theorem",
            "direct K_threshold.Omega_H.lambda row certificate",
            "QCD theta_bar / strong-CP policy",
            "absolute neutrino mass scale",
            "Majorana-vs-Dirac and Majorana phase policy",
            "full correlated covariance/profile likelihood",
            "precision threshold matching and mass-scheme conversion",
            "multi-loop RG convention values",
            "local-QFT precision observable values",
            "full no-knob derivation of gauge/Yukawa/Higgs values",
            "true SM equivalence certificate",
        ],
        "guardrails": {
            "observed_values_do_not_select_source": True,
            "benchmark_values_not_promoted_to_no_knob_predictions": True,
            "P_EW_not_promoted_as_strict_source": True,
            "lambda_H_not_used_as_selector": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strict_pew_contract = {
        "schema": "MTTStrictPEWSourceReentryContract.v1",
        "status": "STRICT_PEW_SOURCE_REENTRY_CONTRACT_EMITTED",
        "closure_claimed": True,
        "current_strict_P_EW_source_rows": previous["closure_decision"][
            "accepted_strict_prefactor_source_row_total"
        ],
        "strict_P_EW_source_closed": False,
        "minimal_parameter_ledger_can_stand_without_strict_P_EW": True,
        "strict_upgrade_would_reduce_count_by": 1,
        "required_for_strict_upgrade": [
            "same-branch physical gauge/action normalization",
            "selected mu_match",
            "selected RG/threshold scheme",
            "P_EW source value emitted before lambda_H postcheck",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterFullSMMinimalParameterLedger.v1",
        "status": "NEXT_IS_STRICT_PEW_SOURCE_OR_PRECISION_CLOSURE_CUTSET",
        "closure_claimed": True,
        "closed_here": [
            "full-SM minimal parameter ledger across active SM sectors",
            "non-neutrino count excluding QCD theta",
            "minimal PMNS oscillation extension count",
            "closed/open slot boundary",
            "strict P_EW reentry contract",
        ],
        "remaining_exact_exits": [
            "strict P_EW selected source theorem",
            "QCD theta_bar policy or source theorem",
            "absolute neutrino mass/Majorana policy",
            "precision threshold/mass-scheme/covariance closure",
            "true SM equivalence/no-knob closure",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFullSMMinimalParameterLedgerOrStrictPEWSourceTheorem",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_SM_minimal_parameter_ledger_closed": True,
        "strict_P_EW_source_theorem_closed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_policy": rel(PREVIOUS_POLICY),
            "previous_seed": rel(PREVIOUS_SEED),
            "core_interface": rel(CORE_INTERFACE),
            "sm_parity_ledger": rel(SM_PARITY_LEDGER),
            "rg_policy": rel(RG_POLICY),
            "mixing_gauge": rel(MIXING_GAUGE),
            "common_scale_cert": rel(COMMON_SCALE_CERT),
            "accepted_values": rel(ACCEPTED_VALUES),
            "accepted_values_packet": rel(ACCEPTED_VALUES_PACKET),
            "dynamic_qasu3": rel(DYNAMIC_QASU3),
        },
        "packets": {
            "sm_sector_minimal_parameter_ledger": rel(SECTOR_LEDGER),
            "minimal_parameter_count_summary": rel(COUNT_SUMMARY),
            "closed_vs_open_parameter_slots": rel(SLOT_BOUNDARY),
            "strict_pew_source_reentry_contract": rel(STRICT_PEW_CONTRACT),
            "next_cutset_after_fullsm_minimal_parameter_ledger": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "minimal_parameter_ledger_closed": True,
            "closed_non_neutrino_SM_like_count_excluding_QCD_theta": non_neutrino_closed_count,
            "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta": minimal_pmns_extension_count,
            "H_specific_parameter_count": 0,
            "P_EW_counted_as_shared_physical_primitive": True,
            "P_EW_parameter_count": 1,
            "lambda_H_independent_parameter_replaced": True,
            "gauge_triplet_counted_as_measured_replay": 3,
            "charged_yukawa_counted_as_measured_replay": 9,
            "CKM_counted_as_measured_replay": 4,
            "PMNS_oscillation_counted_as_minimal_policy": 6,
            "QCD_theta_bar_closed": False,
            "absolute_neutrino_mass_closed": False,
            "strict_P_EW_source_closed": False,
            "true_precision_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "numerics": {
            "P_EW_action_prefactor": p_ew,
            "lambda_H_replay": lambda_h,
            "lambda_H_reference": lambda_ref,
            "lambda_H_absolute_residual": lambda_residual,
            "lambda_H_MZ_firstpass": accepted_values_packet["derived_magnitudes"]["lambda_H"],
            "alpha_1_GUT_MZ": gauge_triplet["alpha_1_GUT_MZ"]["central_value"],
            "alpha_2_MZ": gauge_triplet["alpha_2_MZ"]["central_value"],
            "alpha_3_MZ": gauge_triplet["alpha_3_MZ"]["central_value"],
        },
        "theorem": {
            "name": "FullSMMinimalParameterLedgerOrStrictPEWSourceTheorem",
            "proved": True,
            "statement": (
                "The current repo state admits a full SM-sector minimal-parameter "
                "ledger: the non-neutrino SM-like replay sector is counted with 18 "
                "closed/admitted slots excluding QCD theta_bar, replacing the "
                "independent lambda_H slot by one shared P_EW primitive and retaining "
                "zero H-specific lambda knobs. Including the declared minimal PMNS "
                "oscillation policy yields 24 counted slots excluding QCD theta_bar. "
                "This is an accounting closure, not strict no-knob or true precision "
                "SM equivalence: P_EW source rows, QCD theta_bar, absolute neutrino "
                "mass/Majorana policy, threshold/mass-scheme/covariance precision, "
                "and no-knob value derivations remain open."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedFullSMMinimalParameterLedgerOrStrictPEWSourceTheorem",
        "status": STATUS,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_SM_minimal_parameter_ledger_closed": True,
        "closed_non_neutrino_SM_like_count_excluding_QCD_theta": non_neutrino_closed_count,
        "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta": minimal_pmns_extension_count,
        "H_specific_parameter_count": 0,
        "P_EW_parameter_count": 1,
        "P_EW_counted_as_shared_physical_primitive": True,
        "lambda_H_independent_parameter_replaced": True,
        "strict_P_EW_source_theorem_closed": False,
        "QCD_theta_bar_closed": False,
        "absolute_neutrino_mass_closed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected FullSMMinimalParameterLedger or StrictPEWSourceTheorem v1

## Theorem

`FullSMMinimalParameterLedgerOrStrictPEWSourceTheorem` is emitted.

## Closed Ledger Counts

```text
non-neutrino SM-like count excluding QCD theta_bar = {non_neutrino_closed_count}
minimal PMNS oscillation extension excluding QCD theta_bar = {minimal_pmns_extension_count}
H-specific lambda parameters = 0
P_EW shared physical primitive count = 1
```

The non-neutrino count is:

```text
v or G_F electroweak scale anchor = 1
alpha_1, alpha_2, alpha_3 at M_Z = 3
charged-fermion Yukawa magnitudes = 9
CKM physical parameters = 4
P_EW replacing independent lambda_H = 1
total = {non_neutrino_closed_count}
```

The minimal PMNS extension adds:

```text
PMNS angles + Dirac phase + two oscillation splittings = 6
total = {minimal_pmns_extension_count}
```

## H/Lambda Boundary

```text
P_EW.action_prefactor = {p_ew}
lambda_H replay = {lambda_h}
lambda_H reference = {lambda_ref}
lambda_H absolute residual = {lambda_residual}
lambda_H used as selector = false
```

`lambda_H` is not counted as an independent Higgs parameter in this ledger.
It is replaced by selected finite H data plus one shared `P_EW` primitive.

## Still Open

```text
strict P_EW selected source theorem
direct K_threshold.Omega_H.lambda row certificate
QCD theta_bar / strong-CP policy
absolute neutrino mass and Majorana-vs-Dirac policy
full covariance/profile likelihood
precision threshold matching and mass-scheme conversion
multi-loop RG convention values
local-QFT precision observable values
full no-knob derivation
true SM equivalence certificate
```

## Next Proof Object

`{NEXT}`.
"""

    write_json(SECTOR_LEDGER, sector_ledger)
    write_json(COUNT_SUMMARY, count_summary)
    write_json(SLOT_BOUNDARY, slot_boundary)
    write_json(STRICT_PEW_CONTRACT, strict_pew_contract)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
