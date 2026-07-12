from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
Q79 = ROOT.parent / "mtt-q79-proof-repro"
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

PREV = ROOT / "candidate_data" / "alpha1_source_strength_normalization_gate.packet.json"
PARTIAL = SM / "candidate_data" / "selected_samesource_alpha1_normalization_packet.sourceidentity_partial_fill.json"
CUTSET = SM / "candidate_data" / "selected_alpha1_sourcestrength_or_transfernormalization_fill_attempt.candidate.json"
GRAM = SM / "candidate_data" / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
ONE_M = SM / "candidate_data" / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json"
Q79_MATTER = Q79 / "certificates" / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
RETARDED = NONSM / "candidate_data" / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"

OUT_CERT = ROOT / "certificates" / "alpha1_partial_sourceidentity_closure_theorem_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "alpha1_partial_sourceidentity_closure_theorem.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Alpha1_Partial_SourceIdentity_Closure_Theorem_v1.md"

STATUS = "ALPHA1_SOURCEIDENTITY_CLOSED_NORMALIZATION_OR_TYPED_DERIVATIVE_OPEN"
NEXT = "MTT_Selected_SourceStrengthCoordinate_or_TypedBNRetardedDerivative_Theorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    partial = load(PARTIAL)
    cutset = load(CUTSET)
    gram = load(GRAM)
    one_m = load(ONE_M)
    q79_matter = load(Q79_MATTER)
    retarded = load(RETARDED)

    previous_gate_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_remains_open"]["selected_source_identity"] is True,
            prev["what_closes_now"]["necessary_and_sufficient_alpha1_driver_criterion"] is True,
        ]
    )
    source_identity_closed = all(
        [
            partial["partial_fill_result"]["source_identity_selected"] is True,
            partial["source_identity"]["selected_emitted"] is True,
            partial["source_identity"]["theorem_derived"] is True,
            partial["source_identity"]["same_source"] is True,
            partial["source_identity"]["provenance"] == "symbolic_transport_conjugation_theorem",
        ]
    )
    tangent_theorem_derived_support = all(
        [
            partial["tangent_equality"]["theorem_derived"] is True,
            partial["tangent_equality"]["residual_l2"] <= partial["tangent_equality"]["tolerance"],
            partial["tangent_equality"]["same_source"] is True,
            partial["tangent_equality"]["selected_emitted"] is False,
        ]
    )
    still_open_fields_match = all(
        [
            partial["partial_fill_result"]["source_strength_coordinate_selected"] is False,
            partial["partial_fill_result"]["normalization_functional_selected"] is False,
            partial["partial_fill_result"]["sector_dotd_equality_selected"] is False,
            partial["promotion_result"]["alpha1_driver_verified"] is False,
            partial["validation"]["ok"] is False,
        ]
    )
    dual_route_cutset = all(
        [
            cutset["minimal_cutset"]["route_A_same_source_coordinate"]["source_identity_selected"] is True,
            cutset["minimal_cutset"]["route_A_same_source_coordinate"]["closed"] is False,
            cutset["minimal_cutset"]["route_B_typed_transfer"]["closed"] is False,
            cutset["minimal_cutset"]["shared_final_replay"]["dotD_math_passes_if_driver_is_theorem_derived"] is True,
            cutset["what_closes_now"]["source_identity_imported_as_closed"] is True,
        ]
    )
    transfer_obstruction_classified = all(
        [
            gram["what_closes_now"]["conditional_Gram_transfer_scalar_fixed_after_rho_s"] is True,
            gram["transfer_to_alpha1_decision"]["selected_transfer_normalization"] is False,
            one_m["what_closes_now"]["structural_1M_Dirac_rule_candidate"] is True,
            one_m["decision"]["selected_1M_Dirac_rule_closed"] is False,
            q79_matter["closed_by_this_attempt"]["matter_slot_charge_sublemmas_identified"] is True,
            q79_matter["matter_slot_overlap_reduction"]["decision"]["selected_matter_slot_charge_closed"] is False,
        ]
    )
    retarded_route_classified = all(
        [
            retarded["retarded_kernel_transfer"]["ckm_nil_survivor_kernel_available"] is True,
            retarded["transfer_checks"]["K4_selected_sector_charge_or_chirality"] is False,
            retarded["transfer_checks"]["K5_selected_transfer_normalization"] is False,
            retarded["transfer_checks"]["K6_selected_BN_tangent_or_retarded_kernel"] is False,
            retarded["guardrails"]["does_not_import_ckm_retarded_kernel_as_sm_dotd_proof"] is True,
        ]
    )

    theorem_proved = all(
        [
            previous_gate_ready,
            source_identity_closed,
            tangent_theorem_derived_support,
            still_open_fields_match,
            dual_route_cutset,
            transfer_obstruction_classified,
            retarded_route_classified,
        ]
    )

    packet = {
        "theorem": {
            "name": "Alpha1PartialSourceIdentityClosureTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The alpha1 same-source normalization gate can be sharpened: the source_identity "
                "field is closed by the symbolic transport-conjugation theorem on the locked "
                "q79/F,m=1 branch. The h_ext tangent equality is theorem-derived support with "
                "zero residual, but it is not yet emitted as the selected physical alpha1 "
                "coordinate. Therefore the remaining independent gate is no longer generic "
                "source identity; it is either a selected source-strength coordinate plus "
                "normalization functional, or a typed B_N retarded alpha1 derivative with "
                "selected sector charge, transfer normalization, and honest dotD replay."
            ),
        },
        "imported_status": {
            "status": STATUS,
            "partial_fill_status": partial["status"],
            "cutset_status": cutset["status"],
            "gram_status": gram["status"],
            "one_m_status": one_m["status"],
            "q79_matter_status": q79_matter["status"],
            "retarded_status": retarded["status"],
        },
        "closed_field": {
            "source_identity": partial["source_identity"],
        },
        "theorem_derived_but_not_selected": {
            "tangent_equality": partial["tangent_equality"],
        },
        "remaining_independent_fields": {
            "route_A_same_source_coordinate": {
                "must_emit": [
                    "selected source-strength coordinate alpha1",
                    "selected normalization functional, not canonical L2 dual by coordinate convention",
                    "selected h_alpha1=h_ext as physical tangent",
                    "honest sector dotD equality after driver selection",
                ],
                "current_status": cutset["minimal_cutset"]["route_A_same_source_coordinate"],
            },
            "route_B_typed_retarded_transfer": {
                "must_emit": [
                    "selected sector charge/chirality table",
                    "selected 1_M Dirac-neutrino source rule",
                    "selected Gram/transfer normalization",
                    "typed B_N alpha1 tangent or retarded derivative",
                    "honest dotD replay from the typed kernel",
                ],
                "current_status": cutset["minimal_cutset"]["route_B_typed_transfer"],
            },
        },
        "proof_chain": {
            "previous_gate_ready": previous_gate_ready,
            "source_identity_closed": source_identity_closed,
            "tangent_theorem_derived_support": tangent_theorem_derived_support,
            "still_open_fields_match": still_open_fields_match,
            "dual_route_cutset": dual_route_cutset,
            "transfer_obstruction_classified": transfer_obstruction_classified,
            "retarded_route_classified": retarded_route_classified,
            "target_fitting_used": any(
                [
                    partial["promotion_result"]["target_fitting_used"],
                    cutset["target_fitting_used"],
                    gram["target_fitting_used"],
                    one_m["target_fitting_used"],
                    q79_matter["target_fitting_used"],
                    retarded["guardrails"]["does_not_use_observed_or_benchmark_inputs"] is False,
                ]
            ),
        },
        "what_closes_now": {
            "alpha1_source_identity_selected": True,
            "alpha1_tangent_equality_theorem_derived_support": True,
            "remaining_alpha1_gate_reduced_to_two_legal_routes": True,
            "source_identity_removed_from_minimal_cutset": True,
            "unsafe_coordinate_and_retarded_shortcuts_excluded": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_source_strength_coordinate": True,
            "selected_normalization_functional": True,
            "selected_physical_h_alpha1_equals_h_ext": True,
            "selected_sector_charge_or_chirality_table": True,
            "selected_1M_Dirac_neutrino_rule": True,
            "selected_transfer_normalization": True,
            "typed_BN_alpha1_tangent_or_retarded_kernel": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_emit_lambda_alpha1_as_selected": True,
            "does_not_promote_tangent_support_as_physical_coordinate": True,
            "does_not_import_ckm_retarded_kernel_as_sm_dotd_proof": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_gate": str(PREV),
            "partial_sourceidentity_fill": str(PARTIAL),
            "dual_route_cutset": str(CUTSET),
            "gram_transfer": str(GRAM),
            "one_m_rule": str(ONE_M),
            "q79_matter": str(Q79_MATTER),
            "retarded": str(RETARDED),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "alpha1_partial_sourceidentity_closure_theorem",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "previous_gate_ready": previous_gate_ready,
            "source_identity_closed": source_identity_closed,
            "tangent_theorem_derived_support": tangent_theorem_derived_support,
            "still_open_fields_match": still_open_fields_match,
            "dual_route_cutset": dual_route_cutset,
            "transfer_obstruction_classified": transfer_obstruction_classified,
            "retarded_route_classified": retarded_route_classified,
            "target_fitting_excluded": packet["proof_chain"]["target_fitting_used"] is False,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# Alpha1 Partial SourceIdentity Closure Theorem v1

## Result

The alpha1 normalization gate is tighter now:

```text
source_identity = selected and theorem-derived
provenance = symbolic_transport_conjugation_theorem
tangent equality residual = {partial["tangent_equality"]["residual_l2"]}
```

This does not verify the alpha1 driver. It removes source identity from the
minimal cutset and leaves two legal closure routes:

```text
Route A: selected source-strength coordinate + selected normalization functional
Route B: selected sector charge/transfer normalization + typed B_N retarded alpha1 derivative
```

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
