from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREV = (
    ROOT
    / "certificates"
    / "post_alpha_c1_defect_functional_source_or_independent_quadrature_data_fill_certificate.json"
)
SOURCE_CERT = ROOT / "certificates" / "post_alpha_phifinc1_minimizes_defect_or_quadrature_table_certificate.json"

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_phifinc1_minimizes_defect_functional_or_independent_quadrature_table_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_phifinc1_minimizes_defect_functional_or_independent_quadrature_table.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_Import_v1.md"
)

STATUS = "POST_ALPHA_PHIFINC1_MINIMIZES_DEFECT_FUNCTIONAL_OR_INDEPENDENT_QUADRATURE_TABLE_IMPORTED_BINDING_REDUCTION_OPEN"
NEXT = "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1"


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
            prev["frontier_decision"][
                "frontier_is_PhiFinC1_minimizes_defect_functional_or_independent_quadrature_table"
            ]
            is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1",
        ]
    )

    source_ok = all(
        [
            source_cert["theorem"]["proved"] is True,
            source_cert["closure_claimed"] is False,
            source_cert["unpatched_theorem_closure_claimed"] is False,
            source_cert["status"] == "POST_ALPHA_PHIFINC1_MINIMIZES_DEFECT_OR_QUADRATURE_TABLE_IMPORTED_BINDING_REDUCTION_OPEN",
            source_cert["frontier_decision"]["next_required_artifact"] == NEXT,
            source_cert["frontier_decision"]["I10_binding_theorem_slot_created"] is True,
            source_cert["frontier_decision"]["I1_minimizer_trace_open"] is True,
            source_cert["frontier_decision"]["I5_dotD_C1_response_open"] is True,
            source_cert["frontier_decision"]["independent_quadrature_table_values_open"] is True,
            all(source_cert["what_closes_now"].values()),
            all(source_cert["what_remains_open"].values()),
            all(source_cert["guardrails"].values()),
        ]
    )

    binding = source_packet["phifinc1_minimizer_binding_reduction"]
    quadrature = source_packet["independent_quadrature_table_template"]

    binding_ok = all(
        [
            binding["schema"] == "MTTPhiFinC1MinimizerBindingReduction.v1",
            binding["status"] == "REDUCED_TO_MINIMIZER_TRACE_AND_C1_RESPONSE_THEOREM_SLOTS",
            binding["proved_now"] is False,
            binding["new_binding_theorem_slot"]["id"] == "I10_phifinc1_minimizes_c1_defect_functional",
            set(binding["new_binding_theorem_slot"]["dependencies"])
            == {
                "I1_selected_strominger_minimizer_to_phifin_trace",
                "I5_dotD_alpha1_and_C1_response",
                "C1DefectFunctionalUniquenessTheorem",
            },
            binding["would_close_if_proved"]["SM_parity_dynamic_packet_closes"] is True,
            binding["observed_data_used"] is False,
            binding["target_fitting_used"] is False,
        ]
    )

    quadrature_ok = all(
        [
            quadrature["schema"] == "MTTIndependentQuadratureTableTemplate.v1",
            quadrature["status"] == "TEMPLATE_READY_VALUES_EMPTY",
            quadrature["values_filled_now"] is False,
            quadrature["acceptance_tests"]["A_shape"] == [72, 2],
            quadrature["acceptance_tests"]["b_shape"] == [72],
            len(quadrature["required_values"]) == 6,
            quadrature["would_close_if_filled"]["SM_parity_dynamic_packet_closes"] is True,
            quadrature["observed_data_used"] is False,
            quadrature["target_fitting_used"] is False,
        ]
    )

    what_closes_now = {
        "long_name_C1_defect_functional_source_gate_consumed": prev_ok,
        "audited_PhiFinC1_binding_reduction_bridged": source_ok,
        "I10_binding_theorem_slot_created": binding_ok,
        "independent_quadrature_table_template_created": quadrature_ok,
    }

    what_remains_open = {
        "prove_I1_selected_minimizer_to_PhiFin_trace": True,
        "prove_I5_selected_dotD_C1_response": True,
        "prove_I10_PhiFinC1_minimizes_defect_functional": True,
        "fill_independent_quadrature_table_values": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_claim_I10_proved": True,
        "does_not_claim_I1_or_I5_proved": True,
        "does_not_fill_quadrature_values": True,
        "does_not_promote_unpatched_A_b_or_deltaTheta": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_true_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaPhiFinC1MinimizesDefectFunctionalOrIndependentQuadratureTableBridge",
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
            "The long-name chain now imports the I10 binding reduction: proving "
            "Phi_fin^C1 minimizes the unique C1 defect functional is reduced to I1 "
            "selected minimizer-to-PhiFin trace and I5 selected dotD/C1 response, or "
            "can be bypassed by an independent quadrature table. The bridge creates "
            "the theorem slot and table template only."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_binding_certificate": source_cert,
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
            "previous_long_name_certificate": str(PREV),
            "source_binding_certificate": str(SOURCE_CERT),
            "source_binding_packet": source_cert["packet_written"],
        },
    }

    note = f"""# PostAlpha PhiFinC1MinimizesDefectFunctional or IndependentQuadratureTable Import v1

## Result

The physical binding problem is reduced to a precise theorem slot.

```text
I10 = Phi_fin^C1 minimizes the unique C1 defect functional
dependencies = I1, I5, C1DefectFunctionalUniquenessTheorem
quadrature table alternative = template ready, values empty
```

Still open:

```text
I1 selected minimizer-to-Phi_fin trace
I5 selected dotD/C1 response
I10 proof
independent quadrature table values
unpatched SM-parity dynamic closure
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_phifinc1_minimizes_defect_functional_or_independent_quadrature_table",
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
