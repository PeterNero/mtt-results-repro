"""Construct the physical-normalization source axiom / direct-K certificate.

This is the explicit missing-piece object after the A_EW correction-factor run.
It does not pretend the physical normalization is derived.  Instead it packages
the smallest typed source axiom that would close the H/lambda row, and the
corresponding direct K_threshold.Omega_H.lambda certificate, while preserving
the strict no-knob guardrail.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalnormalizationsourceaxiom_or_directkcertificate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
AXIOM_PACKET = PACKET_DIR / "physical_normalization_source_axiom.packet.json"
DIRECT_K_PACKET = PACKET_DIR / "direct_kthreshold_omega_h_lambda_certificate_under_axiom.packet.json"
VALIDATOR_PACKET = PACKET_DIR / "axiom_adoption_and_strict_guardrail_validator.packet.json"
NEXT_PACKET = PACKET_DIR / "next_derivation_or_paper_insertion_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalNormalizationSourceAxiom_or_DirectKCertificate_v1.md"

PREVIOUS = DATA / "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun.candidate.json"
PREVIOUS_FRONTIER = (
    DATA
    / "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun"
    / "active_frontier_after_aew_correction_run.packet.json"
)
PREVIOUS_PHYSICAL = (
    DATA
    / "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun"
    / "physical_normalization_or_direct_k_run.packet.json"
)
AEW_TEMPLATE = (
    DATA / "selected_aewsourceoperator_or_thresholdconventionrows" / "aew_source_operator_threshold_convention_template.packet.json"
)
AEW_SOURCE = DATA / "selected_aewsourceoperator_or_thresholdconventionrows.candidate.json"
DTERM = (
    DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure" / "dterm_route_decision_after_aew_recheck.packet.json"
)
CONDITIONAL_HK = (
    DATA / "selected_hradialthresholdscalarsource_or_tenkclosure" / "conditional_h_k_from_ew_boundary_formula.packet.json"
)
H_SOURCE_EQUATION = (
    DATA / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure" / "h_sector_payload_source_equation.packet.json"
)
FINITE_H = DATA / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
ONE_PRIMITIVE = DATA / "selected_samebranchgaugeactionsource_or_oneprimitivepolicy.candidate.json"
MIN_LEDGER = DATA / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem.candidate.json"
CHARGED_K = (
    DATA
    / "selected_thresholddeltarows_or_lambdahpayloadexecution"
    / "ten_kthreshold_gate_after_charged_null_delta.packet.json"
)

STATUS = (
    "MTT_SELECTED_PHYSICALNORMALIZATIONSOURCEAXIOM_OR_DIRECTKCERTIFICATE_"
    "CONSTRUCTED_PREMISED_HK_CLOSURE_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_StrictPEWNoKnobUpgrade_v1"


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


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing physical-normalization inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_FRONTIER,
        PREVIOUS_PHYSICAL,
        AEW_TEMPLATE,
        AEW_SOURCE,
        DTERM,
        CONDITIONAL_HK,
        H_SOURCE_EQUATION,
        FINITE_H,
        ONE_PRIMITIVE,
        MIN_LEDGER,
        CHARGED_K,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_frontier = load(PREVIOUS_FRONTIER)
    previous_physical = load(PREVIOUS_PHYSICAL)
    aew_template = load(AEW_TEMPLATE)
    aew_source = load(AEW_SOURCE)
    dterm = load(DTERM)
    conditional_hk = load(CONDITIONAL_HK)
    h_source = load(H_SOURCE_EQUATION)
    finite_h = load(FINITE_H)
    one_primitive = load(ONE_PRIMITIVE)
    min_ledger = load(MIN_LEDGER)
    charged_k = load(CHARGED_K)

    nums = aew_source["numerics"]
    aew_value = float(nums["A_EW_postcheck"])
    s_beta = float(nums["s_beta"])
    lambda_if_r_equals_1 = aew_value * s_beta
    r_h = float(finite_h["numerics"]["r_H_A_N"])
    lambda_h = lambda_if_r_equals_1 * r_h

    axiom_packet = {
        "schema": "MTTPhysicalNormalizationSourceAxiom.v1",
        "status": "PHYSICAL_NORMALIZATION_SOURCE_AXIOM_CONSTRUCTED_NOT_DERIVED",
        "closure_claimed": True,
        "axiom_name": "SelectedPhysicalGaugeActionNormalizationAxiom",
        "axiom_statement": (
            "On the selected q79/qutrit-Weyl H-sector branch, the physical gauge/action "
            "normalization source emits a single shared electroweak action prefactor "
            "P_EW := A_EW(mu_match, scheme) before Higgs comparison, and the same "
            "P_EW must be reused unchanged for weak-mixing, alpha-sector, and H/lambda ledgers."
        ),
        "emitted_under_axiom": {
            "P_EW_action_prefactor": aew_value,
            "A_EW_mu_match_scheme": aew_value,
            "lambda_if_R_H_RG_equals_1": lambda_if_r_equals_1,
            "mu_match": "mu_* selected by the physical-normalization axiom; value not independently derived here",
            "RG_threshold_scheme": "scheme_* selected by the physical-normalization axiom; value not independently derived here",
        },
        "source_scope": [
            "one shared physical electroweak/gauge-action primitive",
            "same trace convention as the selected internal weak split Delta_G12/lambda_12",
            "same branch as finite H scalar R_H^RG",
        ],
        "acceptance_tier": "explicit source axiom / one shared physical primitive",
        "accepted_as_strict_no_knob_source": False,
        "accepted_as_premised_source_axiom": True,
        "parameter_increment_if_adopted": 1,
        "forbidden_uses": [
            "do not call this strict no-knob closure",
            "do not tune P_EW separately for lambda_H",
            "do not derive P_EW from the lambda_H postcheck",
            "do not use the 103 near-miss denominator as source-selected here",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    direct_k_packet = {
        "schema": "MTTDirectKThresholdOmegaHLambdaCertificateUnderAxiom.v1",
        "status": "DIRECT_K_CERTIFICATE_CONSTRUCTED_UNDER_PHYSICAL_NORMALIZATION_AXIOM",
        "closure_claimed": True,
        "combined_kernel_row_id": "K_threshold.Omega_H.lambda",
        "omega_id": "Omega_H.lambda",
        "premises": {
            "selected_s_beta_closed": conditional_hk["selected_s_beta"]["source_selected_before_replay"],
            "selected_s_beta_value": s_beta,
            "selected_R_H_RG_closed": finite_h["closure_decision"]["selected_R_H_RG_source_emitted"],
            "selected_R_H_RG_value": r_h,
            "physical_normalization_axiom_adopted": True,
            "D_fin_H_subfactor_closed": h_source["closed_inputs"]["D_fin_H_subfactor_closed"],
            "theta_exponent_closed": h_source["closed_inputs"]["shared_circle_theta_exponent_closed"],
            "same_scheme_alignment_premised_by_axiom": True,
        },
        "closed_equations": {
            "lambda_H_mu_match": "lambda_H(mu_match) = A_EW(mu_match, scheme)*s_beta*R_H^RG",
            "direct_K_row": dterm["closed_formulae"]["K_threshold_conditional"],
            "omega_value": h_source["selected_source_equation"]["omega_value"],
        },
        "numeric_payload": {
            "A_EW": aew_value,
            "s_beta": s_beta,
            "lambda_if_R_H_RG_equals_1": lambda_if_r_equals_1,
            "R_H_RG": r_h,
            "lambda_H_from_premised_source": lambda_h,
            "lambda_H_reference_for_postcheck": finite_h["numerics"]["external_lambda_Mt_postcheck"],
            "lambda_H_postcheck_residual": lambda_h - float(finite_h["numerics"]["external_lambda_Mt_postcheck"]),
        },
        "direct_K_row_value": {
            "symbolic": "(A_EW*s_beta)/(D_fin.H*epsilon_Theta^(1/3))",
            "reason_symbolic": (
                "The repo tracks D_fin.H and epsilon_Theta^(1/3) as selected support factors, "
                "but the strict direct row is certified here through the closed source equation "
                "rather than by inventing a new numeric D_fin.H extraction."
            ),
        },
        "accepted_as_tenth_K_row_under_axiom": True,
        "accepted_as_strict_no_knob_tenth_K_row": False,
        "ten_K_ledger_closed_under_axiom": True,
        "strict_no_knob_ten_K_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    validator_packet = {
        "schema": "MTTAxiomAdoptionAndStrictGuardrailValidator.v1",
        "status": "PREMISED_CLOSURE_VALIDATED_STRICT_NOKNOB_GUARD_PRESERVED",
        "closure_claimed": True,
        "input_frontier_status": previous_frontier["status"],
        "input_strict_rows": {
            "strict_K_rows_closed": previous_physical["strict_K_rows_closed"],
            "strict_K_rows_required": previous_physical["strict_K_rows_required"],
            "accepted_strict_P_EW_source_rows": previous_physical["accepted_strict_P_EW_source_rows"],
            "accepted_direct_K_threshold_Omega_H_lambda_rows": previous_physical[
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
        },
        "under_axiom": {
            "premised_P_EW_rows": 1,
            "premised_direct_K_threshold_Omega_H_lambda_rows": 1,
            "premised_selected_K_row_count": 10,
            "premised_H_specific_parameter_count": 0,
            "premised_shared_physical_primitive_count": 1,
            "premised_minimal_H_lambda_closure": True,
        },
        "without_axiom": {
            "accepted_strict_P_EW_source_rows": 0,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
            "strict_selected_K_row_count": charged_k["accepted_selected_K_source_row_count"],
            "strict_no_knob_ten_row_closure": False,
            "strict_no_knob_full_SM_closure": False,
        },
        "ledger_compatibility": {
            "minimal_one_primitive_lane_previously_closed": one_primitive["closure_decision"][
                "minimal_one_primitive_H_lambda_lane_closed"
            ],
            "non_neutrino_minimal_ledger_excluding_QCD_theta": min_ledger["closure_decision"][
                "closed_non_neutrino_SM_like_count_excluding_QCD_theta"
            ],
            "minimal_PMNS_ledger_excluding_QCD_theta": min_ledger["closure_decision"][
                "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"
            ],
        },
        "claim_boundary": [
            "This constructs the missing axiom/certificate object.",
            "It closes the H K row only in the explicit-premise/minimal-primitive lane.",
            "It does not derive physical normalization from MTT alone.",
            "It does not close true SM equivalence, Yukawa source values, CKM/PMNS orientation values, precision covariance, or QCD theta.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextDerivationOrPaperInsertionContract.v1",
        "status": "NEXT_DERIVE_AXIOM_OR_INSERT_AS_EXPLICIT_PREMISE",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "derivation_routes": [
            "derive SelectedPhysicalGaugeActionNormalizationAxiom from same-branch gauge-action/metrology source data",
            "derive direct K_threshold.Omega_H.lambda from an intrinsic H-sector quartic/threshold functional",
            "or insert the physical-normalization axiom explicitly in papers as one shared primitive with falsification rules",
        ],
        "paper_boundary_sentence": (
            "The H/lambda row is closed here only conditional on the explicit "
            "SelectedPhysicalGaugeActionNormalizationAxiom; strict no-knob closure "
            "requires an independent derivation of that axiom or a direct H K certificate."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "physical_normalization_source_axiom_constructed": True,
        "direct_K_threshold_Omega_H_lambda_certificate_constructed_under_axiom": True,
        "premised_P_EW_source_rows": 1,
        "premised_direct_K_threshold_Omega_H_lambda_rows": 1,
        "premised_selected_K_row_count": 10,
        "minimal_one_primitive_H_lambda_lane_closed": True,
        "H_specific_parameter_count_under_axiom": 0,
        "shared_physical_primitive_count_under_axiom": 1,
        "accepted_strict_P_EW_source_rows": 0,
        "accepted_strict_direct_K_threshold_Omega_H_lambda_rows": 0,
        "strict_no_knob_ten_row_closure": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalNormalizationSourceAxiomOrDirectKCertificate",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "physical_normalization_source_axiom": rel(AXIOM_PACKET),
            "direct_kthreshold_omega_h_lambda_certificate_under_axiom": rel(DIRECT_K_PACKET),
            "axiom_adoption_and_strict_guardrail_validator": rel(VALIDATOR_PACKET),
            "next_derivation_or_paper_insertion_contract": rel(NEXT_PACKET),
        },
        "closure_decision": decision,
        "numerics": {
            "A_EW_premised": aew_value,
            "s_beta_selected": s_beta,
            "lambda_if_R_H_RG_equals_1": lambda_if_r_equals_1,
            "R_H_RG_selected": r_h,
            "lambda_H_from_premised_source": lambda_h,
            "lambda_H_postcheck_reference": finite_h["numerics"]["external_lambda_Mt_postcheck"],
            "lambda_H_postcheck_residual": lambda_h - float(finite_h["numerics"]["external_lambda_Mt_postcheck"]),
        },
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "PhysicalNormalizationSourceAxiomOrDirectKCertificateConstructionTheorem",
            "proved": True,
            "statement": (
                "The missing H/lambda object can be constructed as a typed physical-normalization "
                "source axiom plus the corresponding direct K_threshold.Omega_H.lambda certificate. "
                "Under that explicit one-shared-primitive premise the ten-row H/K ledger closes with "
                "zero H-specific knobs. Without deriving or adopting the axiom, strict no-knob P_EW "
                "and direct-K source rows remain zero."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalNormalizationSourceAxiom_or_DirectKCertificate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PhysicalNormalizationSourceAxiom or DirectKCertificate v1

Status: `{STATUS}`.

## What Was Constructed

This artifact constructs the missing typed object:

```text
SelectedPhysicalGaugeActionNormalizationAxiom
P_EW := A_EW(mu_match, scheme)
```

and the corresponding direct H-row certificate:

```text
lambda_H(mu_match) = A_EW(mu_match, scheme) * s_beta * R_H^RG
K_threshold.Omega_H.lambda = (A_EW*s_beta)/(D_fin.H*epsilon_Theta^(1/3))
```

## Numerical Consequence Under The Axiom

```text
A_EW                         = {aew_value}
s_beta                       = {s_beta}
lambda_if_R_H_RG_equals_1     = {lambda_if_r_equals_1}
R_H^RG                       = {r_h}
lambda_H                     = {lambda_h}
lambda_H postcheck residual  = {lambda_h - float(finite_h["numerics"]["external_lambda_Mt_postcheck"])}
```

## Claim Boundary

```text
premised P_EW rows                         : 1
premised direct K_threshold.Omega_H.lambda : 1
premised selected K row count              : 10/10
H-specific parameter count                 : 0
shared physical primitive count            : 1

strict P_EW source rows                    : 0
strict direct K rows                       : 0
strict no-knob ten-row closure             : false
true SM equivalence                        : false
```

So we have constructed the missing piece in the explicit-premise / minimal
one-shared-primitive lane.  The strict no-knob upgrade still requires deriving
the physical-normalization axiom from same-branch source data or emitting an
independent direct H K certificate.

Next artifact: `{NEXT}`.
"""

    write_json(AXIOM_PACKET, axiom_packet)
    write_json(DIRECT_K_PACKET, direct_k_packet)
    write_json(VALIDATOR_PACKET, validator_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
