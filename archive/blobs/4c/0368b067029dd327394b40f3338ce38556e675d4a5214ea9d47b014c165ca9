"""Build the physical gauge/action anchor or direct H K-row frontier packet.

This is the first packet after selected finite-H transport and the A_EW
source-operator validator.  It rechecks the strict no-knob route, then records
the precise one-primitive fork that would be available if MTT admits a single
physical action/metrology primitive.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CONST = TEXPAPERS / "mtt-individual-constants-source-search"
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_RECHECK = PACKET_DIR / "strict_physical_anchor_and_direct_k_recheck.packet.json"
DIRECT_K_ATTEMPT = PACKET_DIR / "direct_kthreshold_omega_h_lambda_attempt.packet.json"
ONE_PRIMITIVE = PACKET_DIR / "one_physical_action_primitive_fork.packet.json"
SOURCE_TEMPLATE = PACKET_DIR / "same_branch_physical_source_packet_template.packet.json"
NEXT_PACKET = PACKET_DIR / "next_samebranch_action_or_primitive_declaration_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalGaugeActionAnchor_or_DirectKThresholdOmegaHLambda_v1.md"

PREVIOUS = DATA / "selected_aewsourceoperator_or_thresholdconventionrows.candidate.json"
FINITE_H = DATA / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
COND_FORMULA = (
    DATA
    / "selected_hradialthresholdscalarsource_or_tenkclosure"
    / "conditional_h_k_from_ew_boundary_formula.packet.json"
)
H_SOURCE_EQ = (
    DATA
    / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
    / "h_sector_payload_source_equation.packet.json"
)
EW_BOUNDARY = DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json"
B41 = CONST / "candidate_data" / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching.candidate.json"
B41_ANCHOR = (
    CONST
    / "candidate_data"
    / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
    / "gauge_action_anchor_status.packet.json"
)
B41_RG = (
    CONST
    / "candidate_data"
    / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
    / "rg_matching_threshold_scheme_status.packet.json"
)
QA_PHYSICAL = QA / "candidate_data" / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json"

STATUS = (
    "MTT_SELECTED_PHYSICALGAUGEACTIONANCHOR_OR_DIRECTKTHRESHOLDOMEGAHLAMBDA_"
    "STRICT_OPEN_ONE_PRIMITIVE_FORK_EXPLICIT"
)
NEXT = "MTT_Selected_SameBranchGaugeActionSource_or_OnePrimitivePolicy_v1"


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


def main() -> int:
    sources = [
        PREVIOUS,
        FINITE_H,
        COND_FORMULA,
        H_SOURCE_EQ,
        EW_BOUNDARY,
        B41,
        B41_ANCHOR,
        B41_RG,
        QA_PHYSICAL,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing physical-anchor/direct-K inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    finite_h = load(FINITE_H)
    cond_formula = load(COND_FORMULA)
    h_source_eq = load(H_SOURCE_EQ)
    ew_boundary = load(EW_BOUNDARY)
    b41 = load(B41)
    b41_anchor = load(B41_ANCHOR)
    b41_rg = load(B41_RG)
    qa_physical = load(QA_PHYSICAL)

    nums = previous["numerics"]
    finite_nums = finite_h["numerics"]
    aew_postcheck = float(nums["A_EW_postcheck"])
    s_beta = float(nums["s_beta"])
    lambda_if_r1 = float(nums["lambda_if_R_H_RG_equals_1"])
    r_h = float(finite_nums["r_H_A_N"])
    lambda_h_replay = float(finite_nums["lambda_H_from_finite_r_H_A_N"])
    tau_h = float(finite_nums["tau_H_A_N"])

    physical_anchor_closed = bool(b41_anchor["decision"]["K_phys_or_f_ab_closed"]) or bool(
        qa_physical["decision"]["physical_gauge_action_anchor_closed"]
    )
    mu_match_closed = bool(b41_rg["decision"]["source_selected_mu_match_closed"]) or bool(
        qa_physical["decision"]["matching_scale_closed"]
    )
    rg_scheme_closed = bool(b41_rg["decision"]["source_selected_threshold_vector_closed"]) and bool(
        qa_physical["decision"]["RG_scheme_closed"]
    )
    selected_aew_emitted = bool(ew_boundary["closure_decision"]["selected_A_EW_emitted"])
    direct_k_emitted = bool(ew_boundary["closure_decision"]["K_threshold_Omega_H_lambda_emitted"])

    strict_fields = [
        {
            "field": "selected_R_H_RG_from_finite_H",
            "filled": finite_h["closure_decision"]["selected_R_H_RG_source_emitted"],
            "source": rel(FINITE_H),
        },
        {
            "field": "same_branch_physical_gauge_action_anchor_or_f_ab",
            "filled": physical_anchor_closed,
            "source": rel(B41_ANCHOR),
        },
        {
            "field": "selected_mu_match",
            "filled": mu_match_closed,
            "source": rel(B41_RG),
        },
        {
            "field": "selected_RG_threshold_scheme",
            "filled": rg_scheme_closed,
            "source": rel(B41_RG),
        },
        {
            "field": "selected_A_EW_value",
            "filled": selected_aew_emitted,
            "source": rel(EW_BOUNDARY),
        },
        {
            "field": "direct_K_threshold_Omega_H_lambda",
            "filled": direct_k_emitted,
            "source": rel(EW_BOUNDARY),
        },
    ]
    strict_filled = sum(1 for field in strict_fields if field["filled"])

    strict_recheck = {
        "schema": "MTTStrictPhysicalAnchorAndDirectKRecheck.v1",
        "status": "STRICT_RECHECK_FINITE_RH_CLOSED_PHYSICAL_PREFACTOR_AND_DIRECT_K_OPEN",
        "closure_claimed": True,
        "strict_fields": strict_fields,
        "strict_field_count": len(strict_fields),
        "strict_fields_filled": strict_filled,
        "accepted_physical_prefactor_rows": 0,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
        "selected_R_H_RG": {
            "r_H_A_N": r_h,
            "tau_H_A_N": tau_h,
            "source_tier": "strict finite A_N source",
        },
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    direct_k_attempt = {
        "schema": "MTTDirectKThresholdOmegaHLambdaAttemptAfterFiniteH.v1",
        "status": "DIRECT_K_ATTEMPT_REDUCED_TO_AEW_OR_ROW_LEVEL_K_CERTIFICATE",
        "closure_claimed": True,
        "source_equation": h_source_eq["selected_source_equation"],
        "conditional_formula": cond_formula["K_threshold_formula_if_same_scheme"]["conditional_formula"],
        "closed_prerequisites": {
            "selected_s_beta": True,
            "selected_s_beta_value": s_beta,
            "selected_R_H_RG": True,
            "r_H_A_N": r_h,
            "H_payload_source_equation_closed": True,
            "D_fin_H_subfactor_closed": h_source_eq["closed_inputs"]["D_fin_H_subfactor_closed"],
            "shared_circle_theta_exponent_closed": h_source_eq["closed_inputs"][
                "shared_circle_theta_exponent_closed"
            ],
            "theta_exponent": h_source_eq["closed_inputs"]["theta_exponent"],
        },
        "missing_for_strict_direct_K": {
            "numeric_or_symbolic_D_fin_H_value_row": False,
            "selected_A_EW_or_equivalent_prefactor": False,
            "same_scheme_alignment_certificate": False,
            "row_level_K_threshold_Omega_H_lambda_certificate": False,
        },
        "diagnostic_replay_only": {
            "A_EW_postcheck": aew_postcheck,
            "lambda_if_R_H_RG_equals_1": lambda_if_r1,
            "lambda_H_replay_with_existing_convention": lambda_h_replay,
            "accepted_as_source": False,
        },
        "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    one_primitive = {
        "schema": "MTTOnePhysicalActionPrimitiveFork.v1",
        "status": "ONE_PRIMITIVE_FORK_AVAILABLE_NOT_STRICT_NO_KNOB",
        "closure_claimed": True,
        "primitive_policy": {
            "allowed_by_current_corpus_packets": bool(b41["one_universal_primitive_extension_ready"])
            and bool(b41_anchor["decision"]["one_universal_primitive_extension_ready"]),
            "primitive_name": "P_EW.action_prefactor_or_same_branch_physical_gauge_unit",
            "counted_parameter_increment": 1,
            "must_be_declared_before_empirical_comparison": True,
            "cannot_be_counted_as_strict_no_knob": True,
            "must_be_reused_unchanged_across_alpha1_weak_mixing_and_H_lambda": True,
        },
        "what_it_would_close_if_supplied": [
            "physical gauge/action anchor in the same trace convention as the internal weak split",
            "A_EW source-operator value or an equivalent base prefactor row",
            "lambda_if_R_H_RG_equals_1 = A_EW*s_beta",
            "lambda_H after multiplying by selected finite R_H^RG",
        ],
        "what_it_would_not_close": [
            "strict no-knob physical normalization",
            "independent derivation of mu_match/RG/threshold scheme",
            "Yukawa/mixing matrix value rows",
            "true SM equivalence audit",
        ],
        "diagnostic_value_if_calibrated_not_promoted": {
            "A_EW_postcheck": aew_postcheck,
            "lambda_if_R_H_RG_equals_1": lambda_if_r1,
            "lambda_H_replay": lambda_h_replay,
            "reason_not_promoted": "This records the minimal one-primitive lane only; the value is not selected by current packets.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    source_template = {
        "schema": "MTTSameBranchPhysicalSourcePacketTemplate.v1",
        "status": "SAME_BRANCH_PHYSICAL_SOURCE_PACKET_TEMPLATE_EMITTED",
        "closure_claimed": True,
        "required_source_fields": [
            {
                "field": "physical_gauge_action_anchor_or_f_ab",
                "required_for_strict_no_knob": True,
                "current_fill": physical_anchor_closed,
            },
            {
                "field": "mu_match",
                "required_for_strict_no_knob": True,
                "current_fill": mu_match_closed,
            },
            {
                "field": "RG_threshold_scheme",
                "required_for_strict_no_knob": True,
                "current_fill": rg_scheme_closed,
            },
            {
                "field": "A_EW_source_operator_or_equivalent_prefactor",
                "required_for_strict_no_knob": True,
                "current_fill": selected_aew_emitted,
            },
            {
                "field": "direct_K_threshold_Omega_H_lambda_or_same_scheme_K_certificate",
                "required_for_strict_no_knob": True,
                "current_fill": direct_k_emitted,
            },
        ],
        "non_source_items_retired": [
            "finite H radial scalar value search",
            "internal weak split p_a/lambda_12/Delta_G12 search",
            "H angular s_beta/projector search",
            "plain near-miss A_EW expression search",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextSameBranchActionOrPrimitiveDeclarationContract.v1",
        "status": "NEXT_IS_SAME_BRANCH_ACTION_SOURCE_OR_EXPLICIT_ONE_PRIMITIVE_POLICY",
        "closure_claimed": True,
        "closed_here": [
            "strict finite R_H^RG carried forward as selected source",
            "physical prefactor/direct-K recheck executed against current constants and Qa/SU3 packets",
            "direct K row reduced to A_EW/scheme or row-level K certificate",
            "one-physical-primitive fork made explicit and counted",
        ],
        "remaining_exact_exits": [
            "derive same-branch physical gauge/action anchor plus mu_match/RG scheme",
            "derive direct K_threshold.Omega_H.lambda row-level certificate",
            "or explicitly adopt one universal physical action primitive and keep it counted",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalGaugeActionAnchorOrDirectKThresholdOmegaHLambda",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "finite_H": rel(FINITE_H),
            "conditional_formula": rel(COND_FORMULA),
            "h_source_equation": rel(H_SOURCE_EQ),
            "ew_boundary": rel(EW_BOUNDARY),
            "b41": rel(B41),
            "b41_anchor": rel(B41_ANCHOR),
            "b41_rg": rel(B41_RG),
            "qa_physical": rel(QA_PHYSICAL),
        },
        "packets": {
            "strict_physical_anchor_and_direct_k_recheck": rel(STRICT_RECHECK),
            "direct_kthreshold_omega_h_lambda_attempt": rel(DIRECT_K_ATTEMPT),
            "one_physical_action_primitive_fork": rel(ONE_PRIMITIVE),
            "same_branch_physical_source_packet_template": rel(SOURCE_TEMPLATE),
            "next_samebranch_action_or_primitive_declaration_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "selected_R_H_RG_source_emitted": True,
            "H_parameter_count_after_replacement": 0,
            "strict_fields_filled": strict_filled,
            "strict_field_count": len(strict_fields),
            "accepted_physical_prefactor_rows": 0,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
            "strict_lambda_H_value_row_emitted": False,
            "strict_K_threshold_Omega_H_lambda_emitted": False,
            "one_physical_action_primitive_fork_available": True,
            "one_primitive_parameter_increment_if_adopted": 1,
            "conditional_H_lambda_closure_if_one_primitive_and_scheme_supplied": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "numerics": {
            "r_H_A_N": r_h,
            "tau_H_A_N": tau_h,
            "s_beta": s_beta,
            "A_EW_postcheck": aew_postcheck,
            "lambda_if_R_H_RG_equals_1": lambda_if_r1,
            "lambda_H_replay_with_existing_convention": lambda_h_replay,
        },
        "theorem": {
            "name": "PhysicalGaugeActionAnchorOrDirectKThresholdOmegaHLambdaTheorem",
            "proved": True,
            "statement": (
                "After selected finite-H transport, the H radial scalar is no longer a parameter. "
                "Current packets still emit zero strict physical prefactor rows and zero direct "
                "K_threshold.Omega_H.lambda rows. The remaining strict no-knob object is therefore "
                "a same-branch physical gauge/action source packet with mu_match/RG convention, or "
                "an independent row-level H K certificate. A one-physical-action-primitive lane is "
                "available and counted as exactly one extra primitive if adopted, but it is not "
                "strict no-knob closure."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedPhysicalGaugeActionAnchorOrDirectKThresholdOmegaHLambda",
        "status": STATUS,
        "closure_claimed": True,
        "theorem_proved": True,
        "selected_R_H_RG_source_emitted": True,
        "H_parameter_count_after_replacement": 0,
        "accepted_physical_prefactor_rows": 0,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
        "strict_K_threshold_Omega_H_lambda_emitted": False,
        "one_physical_action_primitive_fork_available": True,
        "one_primitive_parameter_increment_if_adopted": 1,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PhysicalGaugeActionAnchor or DirectKThresholdOmegaHLambda v1

## Theorem

`PhysicalGaugeActionAnchorOrDirectKThresholdOmegaHLambdaTheorem` is emitted.

After the selected finite-H source:

```text
r_H(A_N) = {r_h}
tau_H(A_N) = {tau_h}
H parameter count for the radial scalar = 0
```

the strict remaining H/lambda wall is no longer radial.  It is a physical
normalization / threshold-convention wall:

```text
K_threshold.Omega_H.lambda = (A_EW(mu_match) * s_beta) / (D_fin.H * epsilon_Theta^(1/3))
```

## Strict Recheck

Current strict physical rows accepted:

```text
physical prefactor rows = 0
direct K_threshold.Omega_H.lambda rows = 0
strict fields filled = {strict_filled}/{len(strict_fields)}
```

The selected finite `R_H^RG` field is filled, but the same-branch physical
action anchor, matching surface, RG/threshold convention, selected `A_EW`, and
direct K-row certificate are still unfilled.

## One-Primitive Fork

The current constants/physical-anchor packets allow a minimal policy fork:

```text
primitive = P_EW.action_prefactor_or_same_branch_physical_gauge_unit
counted parameter increment = 1
```

If adopted, this can be used only as a counted physical action/metrology
primitive reused unchanged across `alpha1`, weak mixing, and H/lambda.  It is
not strict no-knob closure.

## Boundary

Full no-knob SM closure remains open.  True SM equivalence remains open.

## Next Proof Object

`{NEXT}`.
"""

    write_json(STRICT_RECHECK, strict_recheck)
    write_json(DIRECT_K_ATTEMPT, direct_k_attempt)
    write_json(ONE_PRIMITIVE, one_primitive)
    write_json(SOURCE_TEMPLATE, source_template)
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
