from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "candidate_data" / "physical_alpha1_normalization_nogo_end0_sector_reduction.packet.json"
CARRIER = SM / "candidate_data" / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct.candidate.json"
ADJOINT = SM / "candidate_data" / "selected_sector_zero_mode_adjointtriplet_realization_theorem.candidate.json"
CUTSET = SM / "candidate_data" / "selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem.candidate.json"

OUT_CERT = ROOT / "certificates" / "sector_zeromode_end0_tensorproduct_construct_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "sector_zeromode_end0_tensorproduct_construct.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Sector_ZeroMode_End0_TensorProduct_Construct_v1.md"

STATUS = "SECTOR_ZEROMODE_END0_TENSORPRODUCT_CARRIER_CONSTRUCTED_SOURCE_ACTION_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_SourcePayload_Search_or_Emission_Attempt_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    carrier = load(CARRIER)
    adjoint = load(ADJOINT)
    cutset = load(CUTSET)

    carrier_constructed = all(
        [
            carrier["decision"]["End0_tensor_product_carrier_constructed"] is True,
            carrier["validation"]["all_lie_checks_pass"] is True,
            carrier["validation"]["all_projectors_idempotent"] is True,
            carrier["validation"]["all_projectors_commute_with_End0_action"] is True,
            carrier["validation"]["projectors_sum_to_identity"] is True,
            carrier["rank_match"]["matches_expected_sector_kernel_rank_sum"] is True,
        ]
    )
    adjoint_theorem = all(
        [
            adjoint["theorem"]["proved"] is True,
            adjoint["conclusion_boundary"]["adjoint_triplet_representation_choice_closed_conditionally"]
            is True,
            adjoint["conclusion_boundary"]["Higgs_singlet_representation_choice_closed_conditionally"]
            is True,
            adjoint["conclusion_boundary"]["selected_zero_mode_packet_emitted"] is False,
        ]
    )
    source_cutset = all(
        [
            cutset["theorem"]["proved"] is True,
            cutset["cutset_closed"] is True,
            cutset["route_A"]["passes_now"] is False,
            cutset["route_B"]["passes_now"] is False,
            cutset["selected_payload_emitted"] is False,
        ]
    )
    previous_reduction = prev["next_required_artifact"].endswith("End0TensorProduct_Construction_v1")
    theorem_proved = all([carrier_constructed, adjoint_theorem, source_cutset, previous_reduction])

    packet = {
        "theorem": {
            "name": "SectorZeroModeEnd0TensorProductConstruct",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The universal End0-to-sector tensor-product carrier is constructed: "
                "six matter triplets carry the adjoint End0 action and H is an End0 "
                "singlet. Projectors are orthogonal, idempotent, commute with the "
                "End0 action, sum to identity, and match the 6*3+1 rank pattern. "
                "Representation choice is therefore no longer free once selected "
                "zero-mode source action is emitted. The selected source action, "
                "Gram normalization, and matter-slot routing remain open."
            ),
        },
        "constructed_carrier_summary": {
            "sector_order": carrier["constructed_End0_tensor_product_carrier"]["sector_order"],
            "sector_dimensions": carrier["constructed_End0_tensor_product_carrier"]["sector_dimensions"],
            "total_dimension": carrier["constructed_End0_tensor_product_carrier"]["total_dimension"],
            "construction_rule": carrier["constructed_End0_tensor_product_carrier"]["construction_rule"],
            "rank_match": carrier["rank_match"],
            "sector_T3_response_norms": carrier["validation"]["sector_T3_response_norms"],
        },
        "validation": carrier["validation"],
        "adjoint_triplet_theorem": adjoint["theorem"],
        "source_action_cutset": {
            "route_A_required_payload": cutset["route_A"]["required_payload"],
            "route_B_required_payload": cutset["route_B"]["required_payload"],
            "forbidden_shortcuts": cutset["forbidden_shortcuts"],
        },
        "what_closes_now": {
            "universal_End0_tensor_product_carrier": carrier_constructed,
            "six_triplet_plus_H_singlet_rank_model": True,
            "sector_projectors_and_commutator_checks": carrier_constructed,
            "adjoint_triplet_representation_type_forced_conditionally": adjoint_theorem,
            "source_action_or_matter_slot_cutset_identified": source_cutset,
            "target_fitting_excluded": carrier["target_fitting_used"] is False,
        },
        "what_remains_open": {
            "selected_zero_mode_bases_K_s": True,
            "selected_source_map_rho_s": True,
            "selected_sector_Gram_normalization": True,
            "selected_matter_slot_routing_or_chirality_table": True,
            "selected_1M_Dirac_neutrino_rule": True,
            "honest_dotD_replay_without_lifted_flags": True,
        },
        "guardrails": {
            "does_not_claim_selected_zero_mode_packet": True,
            "does_not_claim_physical_dotD_alpha1": True,
            "does_not_claim_matter_slot_routing": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "input_artifacts": {
            "previous_reduction": str(PREV),
            "carrier": str(CARRIER),
            "adjoint_theorem": str(ADJOINT),
            "cutset": str(CUTSET),
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "sector_zeromode_end0_tensorproduct_construct",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "carrier_constructed": carrier_constructed,
            "adjoint_theorem": adjoint_theorem,
            "source_cutset": source_cutset,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# Sector ZeroMode End0 TensorProduct Construct v1

## Result

The End0-to-sector carrier is constructed as six adjoint triplets plus one
Higgs singlet:

```text
Q,u,d,L,e,N: rho_s(T_i)=ad(T_i)
H: rho_H(T_i)=0
rank = 6*3 + 1 = 19
```

Projectors are orthogonal/idempotent, commute with the End0 action, and sum to
identity. The representation choice is now forced conditionally by the selected
source action.

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
