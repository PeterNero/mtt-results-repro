from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_c1_orthogonal_completion_or_independent_hessian_solve_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_c1defectfunctionalsource_or_independentquadraturedatafill_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_c1defectfunctionalsource_or_independentquadraturedatafill"
FUNCTIONAL_SOURCE = SM_DIR / "c1_defect_functional_uniqueness_source.packet.json"
QUADRATURE_ATTEMPT = SM_DIR / "independent_quadrature_data_fill_attempt.packet.json"
APPLICATION_GAP = SM_DIR / "phifinc1_physical_application_source_gap.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_c1_defect_functional_source_or_quadrature_data_fill_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_c1_defect_functional_source_or_quadrature_data_fill.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_C1DefectFunctionalSource_or_QuadratureDataFill_Import_v1.md"

STATUS = "POST_ALPHA_C1_DEFECT_FUNCTIONAL_SOURCE_IMPORTED_PHYSICAL_APPLICATION_OPEN"
NEXT = "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    functional = load(FUNCTIONAL_SOURCE)
    quadrature = load(QUADRATURE_ATTEMPT)
    gap = load(APPLICATION_GAP)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_C1_defect_functional_source_or_independent_quadrature_data_fill"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["patched_spine_closure_preserved"] is True,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "C1DefectFunctionalUniquenessTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["selected_C1_defect_functional_formal_source_promoted"] is True,
            candidate["promotion_decision"]["physical_PhiFinC1_application_rule_proved"] is False,
            candidate["promotion_decision"]["independent_quadrature_data_filled"] is False,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
        ]
    )

    functional_ok = all(
        [
            functional["schema"] == "MTTC1DefectFunctionalUniquenessSource.v1",
            functional["status"] == "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE",
            functional["functional_name"] == "C1DefectLeakageFunctional",
            functional["observed_data_used"] is False,
            functional["target_fitting_used"] is False,
            all(functional["selection_inputs"].values()),
            all(functional["uniqueness_conditions"].values()),
            all(functional["uniqueness_result"].values()),
            all(functional["what_this_sources"].values()),
            all(functional["what_this_does_not_source"].values()),
        ]
    )

    quadrature_ok = all(
        [
            quadrature["schema"] == "MTTIndependentQuadratureDataFillAttempt.v1",
            quadrature["status"] == "DATA_REQUIREMENTS_RESTATED_NO_INDEPENDENT_VALUES_FILLED",
            quadrature["observed_data_used"] is False,
            quadrature["target_fitting_used"] is False,
            quadrature["input_data_available_now"]["selected_zero_mode_basis_data"] is False,
            quadrature["input_data_available_now"]["independent_primitive_quadrature_table"] is False,
            quadrature["input_data_available_now"]["independent_hessian_source_vector"] is False,
            quadrature["input_data_available_now"]["independent_sector_response_matrices"] is False,
            len(quadrature["required_values"]) == 6,
            len(quadrature["forbidden_shortcuts"]) == 3,
            quadrature["if_supplied_then"]["SM_parity_dynamic_packet_closes"] is True,
        ]
    )

    gap_ok = all(
        [
            gap["schema"] == "MTTPhiFinC1PhysicalApplicationSourceGap.v1",
            gap["status"] == "FUNCTIONAL_SOURCED_PHYSICAL_APPLICATION_RULE_OPEN",
            gap["observed_data_used"] is False,
            gap["target_fitting_used"] is False,
            all(gap["now_available"].values()),
            gap["remaining_physical_application_rule"]["not_proved_now"] is True,
            len(gap["remaining_physical_application_rule"]["why_not_automatic"]) == 3,
            gap["if_supplied_then"]["SM_parity_dynamic_packet_closes"] is True,
            gap["if_supplied_then"]["physical_PhiFinC1_applies_Q_residual"] is True,
        ]
    )

    what_closes_now = {
        "previous_variational_reduction_consumed": prev_ok,
        "C1_defect_functional_uniqueness_imported": imported_ok,
        "unique_formal_defect_functional_sourced": functional_ok,
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
    }

    guardrails = {
        "formal_functional_source_not_misreported_as_physical_application": True,
        "overall_scale_not_used_as_free_knob": True,
        "independent_quadrature_values_not_filled": True,
        "does_not_promote_unpatched_A_b_or_deltaTheta": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaC1DefectFunctionalSourceOrQuadratureDataFillImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The selected trace/Frobenius metric, fixed-fiber span, static routing, "
            "and no-extra-knob policy uniquely source the quadratic C1 defect/leakage "
            "functional up to overall positive scale, and that scale cancels from the "
            "Euler projection. This sources the formal variational object selecting "
            "Q_residual. It does not yet prove that differentiated Phi_fin^C1 is "
            "physically governed by this functional, nor does it fill independent "
            "quadrature/Hessian values."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "c1_defect_functional_uniqueness_source": functional,
        "independent_quadrature_data_fill_attempt": quadrature,
        "phifinc1_physical_application_source_gap": gap,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "unique_formal_C1_defect_functional_sourced": True,
            "physical_PhiFinC1_application_rule_open": True,
            "independent_quadrature_data_open": True,
            "frontier_is_PhiFinC1_minimization_or_independent_quadrature_table": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "c1_defect_functional_uniqueness_source": str(FUNCTIONAL_SOURCE),
            "independent_quadrature_data_fill_attempt": str(QUADRATURE_ATTEMPT),
            "phifinc1_physical_application_source_gap": str(APPLICATION_GAP),
        },
    }

    note = f"""# PostAlpha C1 Defect Functional Source or Quadrature Data Fill Import v1

## Result

The formal C1 defect/leakage functional is now sourced uniquely.

Closed:

```text
unique quadratic defect functional up to positive scale
no extra sector weights or knobs
overall scale cancels in Euler projection
formal Q_residual selection from the functional
```

Open:

```text
Phi_fin^C1 physically minimizes the functional
independent quadrature/Hessian data
unpatched dynamic C1 closure
```

The next step is no longer to invent a functional. It is to prove the physical
application rule, or fill independent quadrature rows.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_c1_defect_functional_source_or_quadrature_data_fill",
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
