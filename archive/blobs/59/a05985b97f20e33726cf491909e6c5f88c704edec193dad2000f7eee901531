from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_CERT = ROOT / "certificates" / "selected_sector_functor_or_physical_alpha1_sourcevalues_certificate.json"
PREV_PACKET = ROOT / "candidate_data" / "selected_sector_functor_or_physical_alpha1_sourcevalues.packet.json"
SOURCE_ALPHA1 = SM / "candidate_data" / "selected_source_origin_and_alpha1_driver.candidate.json"
C1_EMISSION_PACKET = ROOT / "candidate_data" / "routec_selected_c1_response_operator_emission_import.packet.json"
DELTATHETA_PACKET = ROOT / "candidate_data" / "routec_deltatheta_c1_solve_gate_import.packet.json"
PHIFIN_PACKET = ROOT / "candidate_data" / "phifin_operator_payload_scaffold_import.packet.json"

OUT_CERT = ROOT / "certificates" / "selected_physical_dotd_alpha1_sourcevalues_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_physical_dotd_alpha1_sourcevalues.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Physical_dotD_alpha1_SourceValues_From_Selected_HYM_v1.md"

STATUS = "PHYSICAL_DOTD_ALPHA1_SOURCE_VALUES_REDUCED_TO_SELECTED_PHIFIN_ALPHA1_PAYLOAD_VALUES_OPEN"
NEXT = "MTT_Selected_PhiFin_Alpha1_Payload_Value_Emission_From_Selected_HYM_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def all_false(values: dict) -> bool:
    return all(value is False for value in values.values())


def all_null(values: dict) -> bool:
    return all(value is None for value in values.values())


def main() -> None:
    prev_cert = load(PREV_CERT)
    prev = load(PREV_PACKET)
    source_alpha1 = load(SOURCE_ALPHA1)
    c1 = load(C1_EMISSION_PACKET)
    deltatheta = load(DELTATHETA_PACKET)
    phifin = load(PHIFIN_PACKET)

    source_reduction_closed = all(
        [
            source_alpha1["theorem"]["proved"] is True,
            source_alpha1["status"]
            == "MTT_SELECTED_SOURCE_ORIGIN_AND_ALPHA1_DRIVER_REDUCED_TO_SELECTED_PHIFIN_ALPHA1_PAYLOAD",
            source_alpha1["superset_mode"]["superset_repair"]["repair_object"]
            == "SelectedPhiFinAlpha1Payload",
            source_alpha1["target_fitting_used"] is False,
            source_alpha1["what_closes_now"]["source_and_alpha1_reduced_to_one_payload"] is True,
        ]
    )
    direct_values_absent = all(
        [
            c1["verdict"]["A_selected_emitted"] is False,
            c1["verdict"]["b_selected_emitted"] is False,
            c1["emission_audit"]["required_operator_slots"][
                "evaluated_grad_V_C1_alpha1_source_vector"
            ]
            is False,
            c1["emission_audit"]["extraction_attempt_missing_nulls"][
                "evaluated_grad_V_C1_alpha1_source_vector"
            ]
            is True,
            all_null(deltatheta["missing_selected_operator_data"]),
            deltatheta["verdict"]["selected_operator_available"] is False,
        ]
    )
    diagnostic_shapes_retained = all(
        [
            phifin["verdict"]["phi_fin_finite_operator_scaffold_imported"] is True,
            phifin["source_flags"]["dotD_alpha1_driver_verified"] is False,
            all(
                row["dotD_alpha1_matrix_shape"] == [27, 27]
                for row in phifin["dotD_projector_summary"].values()
            ),
        ]
    )
    selected_flags_still_open = all(
        [
            all_false(source_alpha1["source_origin_audit"]["phifin_selected_payload_flags"]),
            all_false(source_alpha1["alpha1_driver_audit"]["selected_values"]),
            source_alpha1["what_remains_open"]["selected_PhiFin_alpha1_payload"] is True,
            source_alpha1["what_remains_open"]["same_branch_dotD_alpha1_derivative"] is True,
        ]
    )

    reduction_closed = all(
        [
            prev_cert["ordinary_End0_to_current_BN_sector_functor_no_go_closed"] is True,
            prev["repair_paths"]["path_B_physical_alpha1_source_values"]["required"] is True,
            source_reduction_closed,
            direct_values_absent,
            diagnostic_shapes_retained,
            selected_flags_still_open,
        ]
    )

    packet = {
        "theorem": {
            "name": "SelectedPhysicalDotDAlpha1SourceValuesReduction",
            "proved": reduction_closed,
            "closure_claimed": False,
            "statement": (
                "The direct physical dotD_alpha1 route has been tested. Current "
                "artifacts prove that source-origin and alpha1-driver promotion "
                "are not independent knobs; both reduce to one missing object, "
                "SelectedPhiFinAlpha1Payload, emitted from the selected q79/F,m=1 "
                "S3/GS Strominger-HYM branch. The finite dotD_alpha1 matrix shapes "
                "and alpha1 driver row exist diagnostically, but the physical "
                "source vector values, same-branch derivative proof, A_selected, "
                "and b_selected are still not emitted."
            ),
        },
        "direct_alpha1_route": {
            "attempted": True,
            "values_emitted": False,
            "closed": False,
            "reduced_to": "SelectedPhiFinAlpha1Payload",
            "source_reduction_closed": source_reduction_closed,
            "direct_values_absent": direct_values_absent,
            "diagnostic_shapes_retained": diagnostic_shapes_retained,
            "selected_flags_still_open": selected_flags_still_open,
        },
        "selected_phifin_alpha1_payload_contract": source_alpha1["unified_payload_contract"],
        "current_value_status": {
            "evaluated_grad_V_C1_alpha1_source_vector": None,
            "A_selected_emitted": c1["verdict"]["A_selected_emitted"],
            "b_selected_emitted": c1["verdict"]["b_selected_emitted"],
            "selected_operator_available": deltatheta["verdict"]["selected_operator_available"],
            "rank_test_computable": deltatheta["verdict"]["rank_test_computable"],
            "least_squares_solution_computable": deltatheta["verdict"][
                "least_squares_solution_computable"
            ],
            "selected_payload_flags": source_alpha1["source_origin_audit"][
                "phifin_selected_payload_flags"
            ],
            "alpha1_selected_values": source_alpha1["alpha1_driver_audit"]["selected_values"],
        },
        "diagnostic_support": {
            "dotD_alpha1_shapes_27x27": diagnostic_shapes_retained,
            "alpha1_driver_row_computed": c1["schema_checks"]["alpha1_driver_row_computed"],
            "operator_level_source_support": source_alpha1["alpha1_driver_audit"][
                "operator_level_support"
            ],
            "rank_lift_condition": source_alpha1["alpha1_driver_audit"][
                "rank_lift_condition"
            ],
            "single_driver_not_algebraically_fatal": source_alpha1["alpha1_driver_audit"][
                "operator_level_support"
            ]["single_driver_not_algebraically_fatal"],
        },
        "why_values_cannot_be_promoted_now": {
            "same_branch_dotD_alpha1_derivative_open": source_alpha1["what_remains_open"][
                "same_branch_dotD_alpha1_derivative"
            ],
            "finite_C1_source_vector_and_Hessian_blocks_open": source_alpha1[
                "what_remains_open"
            ]["finite_C1_source_vector_and_Hessian_blocks"],
            "zero_mode_bases_and_primitive_contractions_open": source_alpha1[
                "what_remains_open"
            ]["zero_mode_bases_and_primitive_contractions"],
            "source_origin_selected_flags_open": source_alpha1["what_remains_open"][
                "source_origin_selected_flags"
            ],
            "selected_PhiFin_alpha1_payload_open": source_alpha1["what_remains_open"][
                "selected_PhiFin_alpha1_payload"
            ],
        },
        "what_closes_now": {
            "previous_gate_repair_path_B_invoked": prev["next_required_artifact"]
            == "MTT_Selected_GerbeTwisted_End0_SectorFunctor_or_PhysicalAlpha1_SourceTheorem_v1",
            "source_and_alpha1_reduced_to_one_payload": source_reduction_closed,
            "direct_physical_alpha1_values_absence_proved": direct_values_absent,
            "diagnostic_alpha1_shapes_retained_without_promotion": diagnostic_shapes_retained,
            "selected_payload_contract_imported": True,
            "target_fitting_excluded": source_alpha1["target_fitting_used"] is False
            and c1["verdict"]["observed_flavor_data_used"] is False
            and deltatheta["verdict"]["observed_flavor_data_used"] is False,
        },
        "what_remains_open": {
            "selected_PhiFin_alpha1_payload_value_emission": True,
            "same_branch_dotD_alpha1_derivative": True,
            "finite_C1_source_vector_and_Hessian_blocks": True,
            "selected_zero_mode_bases_and_primitive_contractions": True,
            "A_selected_and_b_selected": True,
            "honest_replay_without_lifted_flags": True,
        },
        "guardrails": {
            "does_not_promote_diagnostic_dotD_alpha1_shapes": True,
            "does_not_promote_alpha1_driver_row_as_values": True,
            "does_not_emit_A_selected_or_b_selected": True,
            "does_not_use_observed_or_benchmark_data": True,
            "does_not_fill_matter_template": True,
        },
        "input_artifacts": {
            "previous_cert": str(PREV_CERT),
            "previous_packet": str(PREV_PACKET),
            "source_alpha1": str(SOURCE_ALPHA1),
            "c1_emission_packet": str(C1_EMISSION_PACKET),
            "deltatheta_packet": str(DELTATHETA_PACKET),
            "phifin_packet": str(PHIFIN_PACKET),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "reduction_closed": reduction_closed,
        "source_reduction_closed": source_reduction_closed,
        "direct_values_absent": direct_values_absent,
        "diagnostic_shapes_retained": diagnostic_shapes_retained,
        "selected_flags_still_open": selected_flags_still_open,
        "A_selected_not_emitted": packet["current_value_status"]["A_selected_emitted"] is False,
        "b_selected_not_emitted": packet["current_value_status"]["b_selected_emitted"] is False,
        "alpha1_source_vector_null": packet["current_value_status"][
            "evaluated_grad_V_C1_alpha1_source_vector"
        ]
        is None,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_physical_dotd_alpha1_sourcevalues",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "direct_physical_dotD_alpha1_source_values_closed": False,
        "reduced_to_SelectedPhiFinAlpha1Payload": True,
        "selected_payload_values_emitted": False,
        "validator_ready": False,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Physical dotD alpha1 SourceValues From Selected HYM v1

## Result

The direct physical `dotD_alpha1` route does not emit values yet. It reduces to
one precise missing object:

```text
SelectedPhiFinAlpha1Payload
```

This is good news structurally: source-origin promotion and alpha1-driver
promotion are not independent knobs. They are both consequences of the same
selected finite trace of the q79/F,m=1 S3/GS Strominger-HYM branch.

## Boundary

Current artifacts still have:

```text
evaluated_grad_V_C1_alpha1_source_vector = null
A_selected emitted = false
b_selected emitted = false
same-branch dotD_alpha1 derivative = open
```

The existing `27x27` `dotD_alpha1` matrices and alpha1 driver row remain
diagnostic support only.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
