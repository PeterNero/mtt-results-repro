from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_c1_defect_functional_source_or_quadrature_data_fill_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable"
BINDING = SM_DIR / "phifinc1_minimizer_binding_reduction.packet.json"
QUADRATURE = SM_DIR / "independent_quadrature_table_template.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_phifinc1_minimizes_defect_or_quadrature_table_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_phifinc1_minimizes_defect_or_quadrature_table.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PhiFinC1MinimizesDefect_or_QuadratureTable_Import_v1.md"

STATUS = "POST_ALPHA_PHIFINC1_MINIMIZES_DEFECT_OR_QUADRATURE_TABLE_IMPORTED_BINDING_REDUCTION_OPEN"
NEXT = "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    binding = load(BINDING)
    quadrature = load(QUADRATURE)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_PhiFinC1_minimization_or_independent_quadrature_table"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["patched_spine_closure_preserved"] is True,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "PhiFinC1BindingReductionTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["PhiFinC1_minimizes_defect_functional_proved"] is False,
            candidate["promotion_decision"]["independent_quadrature_table_values_filled"] is False,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
            candidate["replay_if_I10_or_quadrature_table_proved"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            candidate["replay_if_I10_or_quadrature_table_proved"]["A_transpose_b"] == [12.0, 12.0],
            candidate["replay_if_I10_or_quadrature_table_proved"]["deltaTheta_C1"] == [1.0, 1.0],
        ]
    )

    binding_ok = all(
        [
            binding["schema"] == "MTTPhiFinC1MinimizerBindingReduction.v1",
            binding["status"] == "REDUCED_TO_MINIMIZER_TRACE_AND_C1_RESPONSE_THEOREM_SLOTS",
            binding["proved_now"] is False,
            binding["observed_data_used"] is False,
            binding["target_fitting_used"] is False,
            binding["formal_functional_available"] == "C1DefectLeakageFunctional",
            binding["new_binding_theorem_slot"]["id"] == "I10_phifinc1_minimizes_c1_defect_functional",
            set(binding["new_binding_theorem_slot"]["dependencies"])
            == {
                "I1_selected_strominger_minimizer_to_phifin_trace",
                "I5_dotD_alpha1_and_C1_response",
                "C1DefectFunctionalUniquenessTheorem",
            },
            binding["existing_source_theorem_slots"]["I1_selected_strominger_minimizer_to_phifin_trace"]["status"]
            == "APPENDIX_DRAFT_PROOF_SLOT_OPEN",
            binding["existing_source_theorem_slots"]["I5_dotD_alpha1_and_C1_response"]["status"]
            == "APPENDIX_DRAFT_PROOF_SLOT_OPEN",
            len(binding["why_not_proved_now"]) == 3,
            binding["would_close_if_proved"]["SM_parity_dynamic_packet_closes"] is True,
        ]
    )

    quadrature_ok = all(
        [
            quadrature["schema"] == "MTTIndependentQuadratureTableTemplate.v1",
            quadrature["status"] == "TEMPLATE_READY_VALUES_EMPTY",
            quadrature["values_filled_now"] is False,
            quadrature["observed_data_used"] is False,
            quadrature["target_fitting_used"] is False,
            quadrature["acceptance_tests"]["A_shape"] == [72, 2],
            quadrature["acceptance_tests"]["b_shape"] == [72],
            len(quadrature["required_values"]) == 6,
            len(quadrature["forbidden_shortcuts"]) == 3,
            set(quadrature["table_schema"].keys())
            == {"zero_mode_basis_rows", "primitive_contraction_rows", "hessian_source_rows", "sector_matrix_rows"},
            quadrature["would_close_if_filled"]["SM_parity_dynamic_packet_closes"] is True,
        ]
    )

    what_closes_now = {
        "previous_functional_source_gate_consumed": prev_ok,
        "PhiFinC1_binding_reduction_imported": imported_ok,
        "I10_theorem_slot_created": binding_ok,
        "independent_quadrature_table_template_created": quadrature_ok,
    }

    what_remains_open = {
        "prove_I1_selected_minimizer_to_PhiFin_trace": True,
        "prove_I5_selected_dotD_C1_response": True,
        "prove_I10_PhiFinC1_minimizes_defect_functional": True,
        "fill_independent_quadrature_table_values": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_claim_I10_proved": binding["proved_now"] is False,
        "does_not_claim_I1_or_I5_proved": True,
        "does_not_fill_quadrature_values": quadrature["values_filled_now"] is False,
        "does_not_promote_unpatched_A_b_or_deltaTheta": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaPhiFinC1MinimizesDefectOrQuadratureTableImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The physical Phi_fin^C1 minimization claim is reduced to theorem slot I10, "
            "depending on I1 selected minimizer-to-Phi_fin trace, I5 selected dotD/C1 "
            "response, and the already sourced C1DefectFunctionalUniquenessTheorem. "
            "Alternatively, the unpatched dynamic packet can be closed by filling an "
            "independent quadrature table with the declared schema. This imports the "
            "binding reduction and table template, not the I10 proof or table values."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "phifinc1_minimizer_binding_reduction": binding,
        "independent_quadrature_table_template": quadrature,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "I10_binding_theorem_slot_created": True,
            "I1_minimizer_trace_open": True,
            "I5_dotD_C1_response_open": True,
            "independent_quadrature_table_values_open": True,
            "frontier_is_minimizer_trace_C1_payload_theorem_or_quadrature_values": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "phifinc1_minimizer_binding_reduction": str(BINDING),
            "independent_quadrature_table_template": str(QUADRATURE),
        },
    }

    note = f"""# PostAlpha PhiFinC1 Minimizes Defect or Quadrature Table Import v1

## Result

The physical application step has been reduced to a named theorem slot.

Closed:

```text
I10 theorem slot created
I10 dependencies identified: I1, I5, C1DefectFunctionalUniquenessTheorem
independent quadrature table schema created
sufficiency of I10 or quadrature table preserved
```

Open:

```text
I1 selected minimizer-to-Phi_fin trace
I5 selected dotD/C1 response
I10 Phi_fin^C1 minimizes C1 defect functional
independent quadrature table values
unpatched dynamic C1 closure
```

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
        "certificate": "post_alpha_phifinc1_minimizes_defect_or_quadrature_table",
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
