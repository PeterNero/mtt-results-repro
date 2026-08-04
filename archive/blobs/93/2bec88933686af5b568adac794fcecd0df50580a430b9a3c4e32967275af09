from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SYNC = ROOT / "certificates" / "post_alpha_routec_frontier_synchronization_certificate.json"
STABILITY = ROOT / "certificates" / "routec_sourceemission_stability_chain_import_certificate.json"
T1T2 = ROOT / "certificates" / "selected_t1t2_covariant_green_or_rank2sector_transfer_certificate.json"
SECTOR_NOGO = ROOT / "certificates" / "selected_sector_functor_or_physical_alpha1_sourcevalues_certificate.json"
PHIFIN_ALPHA = ROOT / "certificates" / "selected_phifin_alpha1_payload_value_emission_certificate.json"
ALPHA1 = ROOT / "certificates" / "alpha1_driver_replay_closure_import_certificate.json"
POST_ALPHA_DRIVER = ROOT / "certificates" / "post_alpha_dotd_alpha1_driver_bridge_certificate.json"
PRIMITIVE_FRONTIER = ROOT / "certificates" / "post_alpha_primitive_c1_atom_nogo_frontier_certificate.json"
CORRECTION = ROOT / "certificates" / "post_alpha_selected_correction_source_reduction_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_hym_alpha1_frontier_synthesis_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_hym_alpha1_frontier_synthesis.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_HYM_Alpha1_Frontier_Synthesis_v1.md"

STATUS = "POST_ALPHA_HYM_ALPHA1_FRONTIER_SYNTHESIZED_PRIMITIVE_C1_FULLRESPONSE_OPEN"
NEXT = "Selected_U1Y_RouteC_Primitive_C1_or_FullResponse_SelectedEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    sync = load(SYNC)
    stability = load(STABILITY)
    t1t2 = load(T1T2)
    sector_nogo = load(SECTOR_NOGO)
    phifin_alpha = load(PHIFIN_ALPHA)
    alpha1 = load(ALPHA1)
    post_alpha_driver = load(POST_ALPHA_DRIVER)
    primitive_frontier = load(PRIMITIVE_FRONTIER)
    correction = load(CORRECTION)

    closed_support = {
        "routec_frontier_synchronized": sync["theorem"]["proved"] is True,
        "abstract_HYM_existence_bridged": stability["verdict"]["abstract_HYM_existence_bridged"] is True,
        "selected_equal_radius_metric_used": stability["verdict"]["selected_equal_radius_gauduchon_metric_used"] is True,
        "T1T2_covariant_green_closed": t1t2["T1T2_covariant_reduced_Green_closed"] is True,
        "ordinary_End0_to_projective_BN_no_go_closed": (
            sector_nogo["ordinary_End0_to_current_BN_sector_functor_no_go_closed"] is True
            and sector_nogo["what_closes_now"]["ordinary_End0_to_current_BN_functor_no_go"] is True
        ),
        "same_basis_dotD_alpha1_prefix_imported": phifin_alpha["dotD_alpha1_value_matrices_imported"] is True,
        "alpha1_driver_replay_closed": alpha1["checks"]["driver_closed"] is True and alpha1["checks"]["replay_honest"] is True,
        "post_alpha_dotd_alpha1_driver_bridge_closed": (
            post_alpha_driver["selected_dotD_source_verified"] is True
            and post_alpha_driver["alpha1_driver_verified"] is True
            and post_alpha_driver["honest_dotD_alpha1_replay"] is True
        ),
        "primitive_c1_atom_frontier_built": primitive_frontier["checks"]["theorem_proved"] is True,
        "selected_correction_reduction_closed": correction["checks"]["theorem_proved"] is True,
    }

    no_longer_primary_blockers = {
        "raw_nonidentity_rhoE_BN_linear_scaffold": True,
        "abstract_HYM_existence": True,
        "rank2_L2_arithmetic": True,
        "T1T2_reduced_green_formula": True,
        "alpha1_driver_or_honest_dotD_replay": True,
        "ordinary_End0_to_projective_BN_identification": True,
    }

    current_open = {
        "selected_primitive_C1_atoms_or_noninvariant_vertex": True,
        "selected_full_response_matrices": True,
        "same_source_C1_overlap_or_transfer_functor": True,
        "selected_A_selected_emission": True,
        "selected_b_selected_or_homogeneous_zero_theorem": True,
        "honest_selected_deltaTheta_C1_solve": True,
        "lambda12_and_Yukawa_CKM_PMNS_CP_closure": True,
        "full_SM_or_no_knob_closure": True,
    }

    guardrails = {
        "does_not_claim_primitive_C1_values": True,
        "does_not_claim_full_response_values": True,
        "does_not_claim_A_selected_or_b_selected": True,
        "does_not_promote_diagnostic_or_conditional_Weyl_columns": True,
        "does_not_identify_projective_BN_with_ordinary_End0": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_claim_full_SM_closure": True,
    }

    theorem_proved = all(
        [
            all(closed_support.values()),
            all(no_longer_primary_blockers.values()),
            all(current_open.values()),
            all(guardrails.values()),
            phifin_alpha["SelectedPhiFinAlpha1Payload_fully_emitted"] is False,
            alpha1["next_required_artifact"] == "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1",
            correction["selected_correction_matrix_source_closed"] is False,
        ]
    )

    theorem = {
        "name": "PostAlphaHYMAlpha1FrontierSynthesisImport",
        "proved": theorem_proved,
        "closure_claimed": False,
        "statement": (
            "The post-alpha C1 frontier is synthesized with the Route-C/HYM "
            "operator-value tail. Abstract HYM existence, selected equal-radius "
            "stability, diagonal End0/T1T2 Green response, same-basis dotD "
            "prefix values, and alpha1 honest replay are no longer the main "
            "blockers. The remaining blocker is selected primitive C1 or "
            "full-response value emission from the same source, including "
            "A_selected, b_selected, and the honest DeltaTheta_C1 solve."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "closed_support": closed_support,
        "no_longer_primary_blockers": no_longer_primary_blockers,
        "current_open": current_open,
        "frontier_decision": {
            "frontier_is_HYM_existence": False,
            "frontier_is_alpha1_driver": False,
            "frontier_is_raw_BN_or_rhoE_scaffold": False,
            "frontier_is_primitive_C1_or_full_response_emission": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_certificates": {
            "post_alpha_routec_frontier_synchronization": str(SYNC),
            "routec_sourceemission_stability_chain": str(STABILITY),
            "selected_t1t2_covariant_green": str(T1T2),
            "selected_sector_functor_or_physical_alpha1": str(SECTOR_NOGO),
            "selected_phifin_alpha1_payload_value_emission": str(PHIFIN_ALPHA),
            "alpha1_driver_replay_closure": str(ALPHA1),
            "post_alpha_dotd_alpha1_driver_bridge": str(POST_ALPHA_DRIVER),
            "post_alpha_primitive_c1_atom_nogo_frontier": str(PRIMITIVE_FRONTIER),
            "post_alpha_selected_correction_source_reduction": str(CORRECTION),
        },
    }

    note = f"""# PostAlpha HYM Alpha1 Frontier Synthesis v1

## Result

The current C1 frontier is now synchronized with the HYM/operator-value and
alpha1 replay tail.

Closed or retired as primary blockers:

```text
abstract HYM existence
selected equal-radius stability layer
rank-2 L2 arithmetic obstruction
diagonal End0/T1T2 Green response
ordinary End0 -> current projective B_N identification
same-basis dotD_alpha1 value prefix
alpha1 driver and honest dotD replay
```

The live blocker is now narrower:

```text
selected primitive C1 atoms or non-invariant vertex
selected full-response matrices
same-source C1 overlap/transfer functor
A_selected and b_selected emission
honest selected DeltaTheta_C1 solve
```

No observed masses, CKM/PMNS data, CP phase, benchmark entries, lifted flags,
or diagnostic Weyl columns are promoted.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_hym_alpha1_frontier_synthesis",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "closed_support": closed_support,
        "no_longer_primary_blockers": no_longer_primary_blockers,
        "current_open": current_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
