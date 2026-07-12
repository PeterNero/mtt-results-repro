from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

T1T2_CERT = ROOT / "certificates" / "selected_t1t2_covariant_green_or_rank2sector_transfer_certificate.json"
T1T2_PACKET = ROOT / "candidate_data" / "selected_t1t2_covariant_green_or_rank2sector_transfer.packet.json"
ADJOINT_PACKET = ROOT / "candidate_data" / "selected_hym_newton_galerkin_or_adjoint_functor_import.packet.json"
END0_BASIS_PACKET = ROOT / "candidate_data" / "selected_end0_basis_table_or_bn_identification_import.packet.json"
PHIFIN_SCAFFOLD_PACKET = ROOT / "candidate_data" / "phifin_operator_payload_scaffold_import.packet.json"
ROUTEC_DOTD_PACKET = ROOT / "candidate_data" / "routec_sector_projectors_dotd_on_smooth_bn_import.packet.json"
MATTER_TEMPLATE = ROOT / "candidate_data" / "selected_matter_payload_import_interface.template.json"

OUT_CERT = ROOT / "certificates" / "selected_rank2_to_rank3_sector_transfer_or_physical_dotd_alpha1_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_rank2_to_rank3_sector_transfer_or_physical_dotd_alpha1.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Rank2_to_Rank3_Sector_Transfer_or_Physical_dotD_alpha1_From_HYM_v1.md"

STATUS = "ABSTRACT_RANK2_TO_RANK3_ADJOINT_TRANSFER_CLOSED_SECTOR_ALPHA1_VALUES_OPEN"
NEXT = "MTT_Selected_SectorFunctor_or_PhysicalAlpha1_SourceValues_From_Selected_HYM_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    t1t2_cert = load(T1T2_CERT)
    t1t2 = load(T1T2_PACKET)
    adjoint = load(ADJOINT_PACKET)
    end0_basis = load(END0_BASIS_PACKET)
    phifin = load(PHIFIN_SCAFFOLD_PACKET)
    routec_dotd = load(ROUTEC_DOTD_PACKET)
    matter = load(MATTER_TEMPLATE)

    abstract_transfer_closed = all(
        [
            adjoint["what_closes_now"]["abstract_rank2_to_rank3_transfer_functor"] is True,
            adjoint["adjoint_transfer"]["continuous_parameters_added"] == 0,
            adjoint["adjoint_transfer"]["carrier_rank"] == 3,
            adjoint["adjoint_transfer"]["curvature_rule"] == "F_ad(A)=ad(F_A)",
            adjoint["promotion"]["abstract_transfer_promotable"] is True,
        ]
    )
    end0_green_closed = all(
        [
            t1t2_cert["status"] == "SELECTED_T1T2_COVARIANT_GREEN_CLOSED_RANK2_SECTOR_TRANSFER_OPEN",
            t1t2["theorem"]["proved"] is True,
            t1t2["operator_payload_boundary"]["coupled_T1T2_covariant_Riesz_Green_extracted"] is True,
            t1t2["reduced_projector_and_green"]["green_residual_l2"] < 1.0e-12,
        ]
    )
    bn_rejected_as_end0 = (
        end0_basis["path_A_BN"]["result"] == "REJECTED_AS_SELECTED_END0_TABLE"
        and end0_basis["guardrails"]["does_not_identify_projective_BN_with_ordinary_End0"] is True
    )
    dotd_rows = list(phifin["dotD_projector_summary"].values())
    phifin_scaffold_shape_available = all(
        [
            len(dotd_rows) >= 1,
            all(row["dotD_alpha1_matrix_shape"] == [27, 27] for row in dotd_rows),
            all(row["sector_projector_shape"] == [27, 27] for row in dotd_rows),
            all(row["horizontal_gauge_verified"] is True for row in dotd_rows),
            all(row["green_operator_verified"] is True for row in dotd_rows),
        ]
    )
    phifin_selected_alpha1_values_absent = (
        phifin["source_flags"]["dotD_alpha1_driver_verified"] is False
        and phifin["source_flags"]["dotD_selected_source_verified"] is False
        and phifin["source_flags"]["D_E_selected_source_verified"] is False
    )
    routec_same_basis_dotd_shape_available = (
        routec_dotd["closed_now"]["dotD_alpha1_matrix_in_same_basis_emitted"] is True
        and routec_dotd["verdict"]["dotD_alpha1_on_same_basis_built"] is True
        and routec_dotd["what_remains_open"]["alpha1_driver_verified"] is True
    )
    matter_slot_still_open = (
        matter["required_slots"]["selected_DE_Riesz_Green_dotD"]["filled"] is False
        and matter["required_slots"]["selected_sector_projectors_and_zero_modes"]["filled"] is False
    )

    theorem_closed = all(
        [
            abstract_transfer_closed,
            end0_green_closed,
            bn_rejected_as_end0,
            phifin_scaffold_shape_available,
            phifin_selected_alpha1_values_absent,
            routec_same_basis_dotd_shape_available,
            matter_slot_still_open,
        ]
    )

    packet = {
        "theorem": {
            "name": "SelectedRank2ToRank3SectorTransferOrPhysicalDotDAlpha1Reduction",
            "proved": theorem_closed,
            "closure_claimed": False,
            "statement": (
                "The selected diagonal rank-2 HYM branch now has a complete End0 "
                "adjoint Green split: T3 plus coupled T1/T2. The abstract rank-2 "
                "to rank-3 adjoint transfer is closed and adds no continuous knob: "
                "A maps to ad(A), F maps to ad(F), and the carrier rank is 3. "
                "However this is not yet finite sector-value emission. The existing "
                "B_N/qutrit scaffold has 27x27 sector/dotD shapes, but it remains "
                "projective and unselected as an ordinary End0 finite table, and "
                "the physical alpha1 driver/source values are absent."
            ),
        },
        "closed_abstract_transfer": {
            "closed": abstract_transfer_closed,
            "source_rank": adjoint["adjoint_transfer"]["source_rank"],
            "target_carrier": adjoint["adjoint_transfer"]["carrier"],
            "carrier_rank": adjoint["adjoint_transfer"]["carrier_rank"],
            "curvature_rule": adjoint["adjoint_transfer"]["curvature_rule"],
            "continuous_parameters_added": adjoint["adjoint_transfer"]["continuous_parameters_added"],
            "su2_adjoint_matrices": adjoint["first_coefficient_solve"]["su2_adjoint_matrices"],
            "meaning": "This closes functorial rank2-to-rank3 adjoint transfer as structure, not finite sector values.",
        },
        "closed_End0_green_payload_available_for_transfer": {
            "closed": end0_green_closed,
            "T3_green_closed": True,
            "T1T2_green_closed": t1t2["operator_payload_boundary"]["coupled_T1T2_covariant_Riesz_Green_extracted"],
            "T1T2_green_residual_l2": t1t2["reduced_projector_and_green"]["green_residual_l2"],
            "green_norm_bound": t1t2["reduced_projector_and_green"]["green_operator_norm_bound"],
            "basis": ["T1", "T2", "T3"],
            "role": "This gives selected End0 operator response data before any sector functor is applied.",
        },
        "finite_sector_transfer_status": {
            "values_emitted": False,
            "closed": False,
            "blocking_reason": (
                "The only available finite 27x27 sector scaffold is B_N/qutrit and "
                "gerbe-twisted projective. It is retained as a shape scaffold but "
                "rejected as the selected ordinary End0 differential table."
            ),
            "BN_rejected_as_selected_End0_table": bn_rejected_as_end0,
            "BN_support_retained": end0_basis["path_A_BN"]["support_retained"],
            "needed_to_emit_values": [
                "selected functor from ordinary End0 basis T1,T2,T3 to sector projectors/zero modes",
                "proof that the sector projector basis is the image of the selected End0 response basis",
                "same-branch finite matrices for D_E, Riesz/Green, dotD after the sector functor",
                "source-provenance check excluding lifted selected flags",
            ],
        },
        "physical_dotD_alpha1_status": {
            "closed": False,
            "values_emitted": False,
            "scaffold_shape_available": phifin_scaffold_shape_available,
            "routec_dotD_alpha1_same_basis_shape_available": routec_same_basis_dotd_shape_available,
            "alpha1_driver_verified": False,
            "selected_source_verified": False,
            "blocking_reason": (
                "The smooth B_N/PhiFin and Route-C artifacts emit diagnostic "
                "dotD_alpha1 matrix shapes, but the alpha1 driver and selected "
                "source flags remain false/open."
            ),
        },
        "matter_interface_impact": {
            "selected_DE_Riesz_Green_dotD_shape_now_available_on_End0": end0_green_closed,
            "selected_DE_Riesz_Green_dotD_filled_in_matter_template": False,
            "selected_sector_projectors_and_zero_modes_filled": False,
            "why_not_filled": (
                "The matter template asks for same-branch sector-valued payloads. "
                "The current theorem closes End0 response and abstract adjoint "
                "transfer only; it does not supply selected sector projectors, "
                "zero modes, physical alpha1, or primitive overlap values."
            ),
        },
        "what_closes_now": {
            "previous_gate_reduced_to_rank2_sector_or_alpha1": t1t2["next_required_artifact"]
            == "MTT_Selected_Rank2_to_Rank3_Sector_Transfer_or_Physical_dotD_alpha1_From_HYM_v1",
            "abstract_rank2_to_rank3_adjoint_transfer": abstract_transfer_closed,
            "no_new_continuous_parameter_from_transfer": abstract_transfer_closed,
            "End0_T1T2T3_green_payload_available_before_sector_functor": end0_green_closed,
            "finite_sector_transfer_blocker_identified": bn_rejected_as_end0,
            "physical_alpha1_value_blocker_identified": phifin_selected_alpha1_values_absent,
            "matter_template_not_overfilled": matter_slot_still_open,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_sector_functor_values": True,
            "sector_projectors_and_zero_modes_from_selected_End0": True,
            "physical_dotD_alpha1_source_values": True,
            "primitive_C1_overlap_contractions": True,
            "validator_ready_sector_DE_Riesz_Green_dotD": True,
        },
        "guardrails": {
            "does_not_promote_abstract_transfer_as_finite_values": True,
            "does_not_identify_projective_BN_with_ordinary_End0": True,
            "does_not_promote_diagnostic_dotD_alpha1_shapes": True,
            "does_not_fill_matter_template_without_sector_values": True,
            "does_not_use_observed_or_benchmark_data": True,
        },
        "input_artifacts": {
            "t1t2_cert": str(T1T2_CERT),
            "t1t2_packet": str(T1T2_PACKET),
            "adjoint_packet": str(ADJOINT_PACKET),
            "end0_basis_packet": str(END0_BASIS_PACKET),
            "phifin_scaffold_packet": str(PHIFIN_SCAFFOLD_PACKET),
            "routec_dotd_packet": str(ROUTEC_DOTD_PACKET),
            "matter_template": str(MATTER_TEMPLATE),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "theorem_closed": theorem_closed,
        "abstract_transfer_closed": abstract_transfer_closed,
        "end0_green_closed": end0_green_closed,
        "bn_rejected_as_end0": bn_rejected_as_end0,
        "phifin_shapes_available": phifin_scaffold_shape_available,
        "alpha1_values_absent": phifin_selected_alpha1_values_absent,
        "matter_slot_open": matter_slot_still_open,
        "sector_values_not_emitted": packet["finite_sector_transfer_status"]["values_emitted"] is False,
        "physical_alpha1_not_emitted": packet["physical_dotD_alpha1_status"]["values_emitted"] is False,
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_rank2_to_rank3_sector_transfer_or_physical_dotd_alpha1",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "abstract_rank2_to_rank3_transfer_closed": abstract_transfer_closed,
        "finite_sector_transfer_values_closed": False,
        "physical_dotD_alpha1_values_closed": False,
        "End0_green_payload_available": end0_green_closed,
        "validator_ready": False,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Rank2 to Rank3 Sector Transfer or Physical dotD alpha1 From HYM v1

## Result

The abstract rank2-to-rank3 transfer is now closed in the selected diagonal HYM
branch:

```text
A |-> ad(A)
F_A |-> ad(F_A)
End_0(V_alpha) has basis T1,T2,T3 and rank 3
continuous parameters added = 0
```

Together with the already closed `T3` and `T1/T2` Green packets, this gives a
selected End0 operator response before any sector functor is applied.

## Boundary

This does not emit finite sector values. The available `B_N`/qutrit scaffold is
still projective and is rejected as the selected ordinary End0 differential
table. The PhiFin/Route-C artifacts contain useful `27x27` diagnostic
`dotD_alpha1` shapes, but the physical alpha1 driver and selected source values
remain absent.

So the matter interface is not filled yet: sector projectors, zero modes,
physical `dotD_alpha1`, and primitive C1 contractions remain open.

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
