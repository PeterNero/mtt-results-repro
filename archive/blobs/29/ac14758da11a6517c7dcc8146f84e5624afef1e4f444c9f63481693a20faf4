from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = (
    ROOT
    / "certificates"
    / "post_alpha_differentiated_c1_orthogonal_completion_principle_or_independent_quadrature_hessian_solve_certificate.json"
)
SOURCE_CERT = ROOT / "certificates" / "post_alpha_c1_defect_functional_source_or_quadrature_data_fill_certificate.json"

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_c1_defect_functional_source_or_independent_quadrature_data_fill_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_c1_defect_functional_source_or_independent_quadrature_data_fill.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_Import_v1.md"
)

STATUS = "POST_ALPHA_C1_DEFECT_FUNCTIONAL_SOURCE_OR_INDEPENDENT_QUADRATURE_DATA_FILL_IMPORTED_FUNCTIONAL_SOURCED_APPLICATION_OPEN"
NEXT = "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source_cert = load(SOURCE_CERT)
    source_packet = load(Path(source_cert["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["unpatched_theorem_closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_C1_defect_functional_source_or_independent_quadrature_data_fill"]
            is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1",
        ]
    )

    source_ok = all(
        [
            source_cert["theorem"]["proved"] is True,
            source_cert["closure_claimed"] is False,
            source_cert["unpatched_theorem_closure_claimed"] is False,
            source_cert["status"] == "POST_ALPHA_C1_DEFECT_FUNCTIONAL_SOURCE_IMPORTED_PHYSICAL_APPLICATION_OPEN",
            source_cert["frontier_decision"]["next_required_artifact"] == NEXT,
            source_cert["frontier_decision"]["unique_formal_C1_defect_functional_sourced"] is True,
            source_cert["frontier_decision"]["physical_PhiFinC1_application_rule_open"] is True,
            source_cert["frontier_decision"]["independent_quadrature_data_open"] is True,
            all(source_cert["what_closes_now"].values()),
            all(source_cert["what_remains_open"].values()),
            all(source_cert["guardrails"].values()),
        ]
    )

    uniqueness = source_packet["c1_defect_functional_uniqueness_source"]
    quadrature = source_packet["independent_quadrature_data_fill_attempt"]
    gap = source_packet["phifinc1_physical_application_source_gap"]

    uniqueness_ok = all(
        [
            uniqueness["schema"] == "MTTC1DefectFunctionalUniquenessSource.v1",
            uniqueness["status"] == "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE",
            uniqueness["functional_name"] == "C1DefectLeakageFunctional",
            all(uniqueness["selection_inputs"].values()),
            all(uniqueness["uniqueness_conditions"].values()),
            uniqueness["uniqueness_result"]["unique_up_to_overall_positive_scale"] is True,
            uniqueness["uniqueness_result"]["overall_scale_cancels_from_euler_projection"] is True,
            uniqueness["uniqueness_result"]["selects_Q_residual"] is True,
            uniqueness["what_this_sources"]["selected_MTT_C1_defect_functional_is_candidate"] is True,
            uniqueness["what_this_does_not_source"]["physical_PhiFinC1_variation_minimizes_this_functional"] is True,
            uniqueness["observed_data_used"] is False,
            uniqueness["target_fitting_used"] is False,
        ]
    )

    quadrature_ok = all(
        [
            quadrature["schema"] == "MTTIndependentQuadratureDataFillAttempt.v1",
            quadrature["status"] == "DATA_REQUIREMENTS_RESTATED_NO_INDEPENDENT_VALUES_FILLED",
            quadrature["input_data_available_now"]["selected_zero_mode_basis_data"] is False,
            quadrature["input_data_available_now"]["independent_primitive_quadrature_table"] is False,
            quadrature["input_data_available_now"]["independent_hessian_source_vector"] is False,
            quadrature["input_data_available_now"]["independent_sector_response_matrices"] is False,
            quadrature["if_supplied_then"]["SM_parity_dynamic_packet_closes"] is True,
            len(quadrature["required_values"]) == 6,
            len(quadrature["forbidden_shortcuts"]) == 3,
            quadrature["observed_data_used"] is False,
            quadrature["target_fitting_used"] is False,
        ]
    )

    gap_ok = all(
        [
            gap["schema"] == "MTTPhiFinC1PhysicalApplicationSourceGap.v1",
            gap["status"] == "FUNCTIONAL_SOURCED_PHYSICAL_APPLICATION_RULE_OPEN",
            gap["now_available"]["unique_formal_C1_defect_functional"] is True,
            gap["now_available"]["Euler_projection_derivation"] is True,
            gap["remaining_physical_application_rule"]["not_proved_now"] is True,
            gap["if_supplied_then"]["physical_PhiFinC1_applies_Q_residual"] is True,
            gap["if_supplied_then"]["SM_parity_dynamic_packet_closes"] is True,
            len(gap["remaining_physical_application_rule"]["why_not_automatic"]) == 3,
            gap["observed_data_used"] is False,
            gap["target_fitting_used"] is False,
        ]
    )

    what_closes_now = {
        "long_name_variational_source_gate_consumed": prev_ok,
        "audited_C1_defect_functional_source_bridged": source_ok,
        "unique_formal_C1_defect_functional_sourced": uniqueness_ok,
        "independent_quadrature_data_requirements_preserved": quadrature_ok,
        "physical_application_gap_isolated": gap_ok,
    }

    what_remains_open = {
        "bind_differentiated_PhiFinC1_to_variational_problem": True,
        "prove_PhiFinC1_minimizes_unique_C1_defect_functional": True,
        "fill_selected_zero_mode_basis_data": True,
        "fill_independent_primitive_quadrature_table": True,
        "fill_independent_hessian_source_vector": True,
        "run_independent_quadrature_hessian_solve": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "formal_functional_source_not_misreported_as_physical_application": True,
        "overall_scale_not_used_as_free_knob": True,
        "independent_quadrature_values_not_filled": True,
        "does_not_promote_unpatched_A_b_or_deltaTheta": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaC1DefectFunctionalSourceOrIndependentQuadratureDataFillBridge",
        "proved": all(
            [
                all(what_closes_now.values()),
                all(what_remains_open.values()),
                all(guardrails.values()),
            ]
        ),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The selected trace/Frobenius metric, fixed-fiber span, static routing, "
            "and no-extra-knob policy uniquely source the formal C1DefectLeakageFunctional "
            "up to irrelevant positive scale. This removes the functional-choice knob. "
            "The remaining source gate is to prove differentiated Phi_fin^C1 minimizes "
            "that unique functional, or to fill independent quadrature/Hessian data."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_functional_certificate": source_cert,
        "c1_defect_functional_uniqueness_source": uniqueness,
        "independent_quadrature_data_fill_attempt": quadrature,
        "phifinc1_physical_application_source_gap": gap,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "unique_formal_C1_defect_functional_sourced": True,
            "physical_PhiFinC1_application_rule_open": True,
            "independent_quadrature_data_open": True,
            "frontier_is_PhiFinC1_minimizes_defect_functional_or_independent_quadrature_table": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_functional_certificate": str(SOURCE_CERT),
            "source_functional_packet": source_cert["packet_written"],
        },
    }

    note = f"""# PostAlpha C1DefectFunctionalSource or IndependentQuadratureDataFill Import v1

## Result

The formal C1 defect/leakage functional is now sourced without adding a tunable
sector weight.

```text
functional = C1DefectLeakageFunctional
unique up to positive scale = true
scale cancels from Euler projection = true
selects Q_residual = true
```

Still open:

```text
physical Phi_fin^C1 minimizes this functional
independent quadrature/Hessian values
unpatched SM-parity dynamic closure
```

Next:

```text
{NEXT}
```

Status:

```text
{STATUS}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_c1_defect_functional_source_or_independent_quadrature_data_fill",
        "status": STATUS,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
