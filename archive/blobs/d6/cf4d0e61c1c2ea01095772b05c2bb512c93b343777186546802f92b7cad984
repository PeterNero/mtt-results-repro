"""Import End0 model packet and ordinary-to-projective functor no-go."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")

PREVIOUS = CERTS / "q79_sectorcharge_end0_value_route_import_certificate.json"
SM_END0 = SM / "candidate_data" / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"
QA_END0 = QA / "candidate_data" / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.candidate.json"
GR_NOGO = GR / "candidate_data" / "selected_sector_functor_or_physical_alpha1_sourcevalues.packet.json"
LOCAL_OLD = DATA / "end0_sector_functor_value_packet_reduction.candidate.json"

OUTPUT_PACKET = DATA / "end0_model_packet_and_projective_nogo_import.candidate.json"
OUTPUT_CERT = CERTS / "end0_model_packet_and_projective_nogo_import_certificate.json"
OUTPUT_NOTE = CORPUS / "End0_ModelPacket_and_ProjectiveNoGo_Import_v1.md"

STATUS = "END0_MODEL_PACKET_IMPORTED_PROJECTIVE_ORDINARY_FUNCTOR_NOGO_OPEN"
PREVIOUS_STATUS = "Q79_SECTORCHARGE_END0_VALUE_ROUTE_IMPORTED_MATTERSLOT_OVERLAP_OPEN"
NEXT = "MTT_Selected_GerbeTwisted_End0_SectorFunctor_or_PhysicalAlpha1_SourceTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_end0 = load(SM_END0)
    qa_end0 = load(QA_END0)
    gr_nogo = load(GR_NOGO)
    local_old = load(LOCAL_OLD)

    checks = {
        "L0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "L1_sm_existing_values_rejected": sm_end0["existing_value_tests"]["passes"] is False
        and sm_end0["existing_value_tests"]["bn_rejected_as_selected_End0_basis"] is True
        and sm_end0["decision"]["existing_BN_or_compact_values_promoted"] is False
        and sm_end0["decision"]["functor_contract_specified"] is True
        and sm_end0["decision"]["selected_End0_to_sector_functor_values_extracted"] is False,
        "L2_qa_model_values_constructed": qa_end0["decision"]["End0_domain_values_filled"] is True
        and qa_end0["decision"]["End0_tensor_product_carrier_constructed"] is True
        and qa_end0["decision"]["sector_projectors_constructed"] is True
        and qa_end0["decision"]["commutator_and_projector_checks_pass"] is True
        and qa_end0["decision"]["conditional_gram_normalization_theorem_proved"] is True
        and qa_end0["decision"]["selected_zero_mode_bases_emitted"] is False
        and qa_end0["decision"]["physical_dotD_alpha1_payload_extracted"] is False,
        "L3_rank_and_sector_model_shape": qa_end0["constructed_values_summary"]["rank_match"][
            "direct_sum_total_rank"
        ]
        == 19
        and qa_end0["constructed_values_summary"]["rank_match"][
            "matches_expected_sector_kernel_rank_sum"
        ]
        is True
        and qa_end0["constructed_values_summary"]["sector_T3_response_norms"]["H"]["zero_response"]
        is True
        and qa_end0["constructed_values_summary"]["sector_T3_response_norms"]["u"]["frobenius_norm"]
        == 1.4142135623730951,
        "L4_ordinary_projective_nogo_proved": gr_nogo["theorem"]["proved"] is True
        and gr_nogo["obstruction"]["closed"] is True
        and gr_nogo["attempted_positive_functor"]["ordinary_End0_to_current_BN_sector_functor_proved"]
        is False
        and gr_nogo["projective_BN_target"]["cocycle_nontrivial"] is True
        and gr_nogo["obstruction"]["numerical_gap_from_ordinary_phase"] > 1.7,
        "L5_local_old_reduction_consistent": local_old["status"]
        == "END0_SECTOR_FUNCTOR_PACKET_REDUCED_TO_SELECTED_PROJECTOR_SOURCE_PROMOTION_OPEN"
        and local_old["blocked_promotions"]["selected_End0_to_sector_functor_values_extracted"]
        is False
        and local_old["guardrails"]["does_not_claim_selected_End0_functor_values"] is True,
        "L6_no_overclaim_guardrails": qa_end0["guardrails"]["claims_A_selected_or_b_selected"] is False
        and qa_end0["guardrails"]["claims_physical_dotD_alpha1_payload_extracted"] is False
        and qa_end0["guardrails"]["claims_selected_transfer_normalization"] is False
        and qa_end0["guardrails"]["uses_observed_or_benchmark_inputs"] is False
        and gr_nogo["guardrails"]["does_not_identify_projective_BN_with_ordinary_End0"] is True
        and gr_nogo["guardrails"]["does_not_use_observed_or_benchmark_data"] is True,
    }

    return {
        "packet": "End0_ModelPacket_and_ProjectiveNoGo_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_end0_packet": str(SM_END0),
            "qa_end0_model_packet": str(QA_END0),
            "gr_ordinary_projective_nogo": str(GR_NOGO),
            "local_prior_end0_reduction": str(LOCAL_OLD.relative_to(ROOT)),
        },
        "theorem": {
            "name": "End0ModelPacketAndProjectiveNoGoImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The End0-to-sector value problem is no longer blank: a canonical "
                "model packet constructs the End0 domain, sector projectors, six "
                "matter triplets plus H singlet, and conditional Gram checks. "
                "However, existing BN/compact values remain unselected, and an "
                "ordinary End0-to-current-BN sector functor is obstructed by the "
                "nontrivial Heisenberg/Weyl projective cocycle. A positive route "
                "must be gerbe-twisted/central-extension End0 transport or direct "
                "physical alpha1 source values."
            ),
        },
        "checks": checks,
        "sm_end0_packet": sm_end0,
        "qa_end0_model_packet": qa_end0,
        "gr_ordinary_projective_nogo": gr_nogo,
        "local_prior_end0_reduction": local_old,
        "model_packet_summary": qa_end0["constructed_values_summary"],
        "projective_obstruction": gr_nogo["obstruction"],
        "repair_paths": gr_nogo["repair_paths"],
        "what_closes_now": {
            "canonical_End0_model_packet_constructed": True,
            "sector_projector_model_constructed": True,
            "rank_19_six_triplet_plus_H_singlet_shape_closed": True,
            "ordinary_End0_to_current_BN_functor_no_go": True,
            "projective_cocycle_obstruction_imported": True,
            "positive_routes_reduced_to_gerbe_twisted_or_physical_alpha1": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "gerbe_twisted_End0_to_BN_sector_functor": True,
            "operator_level_projective_source_promotion": True,
            "physical_dotD_alpha1_source_values": True,
            "selected_zero_mode_bases_K_s": True,
            "selected_source_map_rho_s": True,
            "selected_sector_charge_or_chirality_table": True,
            "selected_transfer_normalization": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_End0_to_sector_functor_values": False,
            "claims_ordinary_End0_to_current_BN_functor": False,
            "claims_physical_dotD_alpha1_payload": False,
            "claims_selected_transfer_normalization": False,
            "claims_A_selected_or_b_selected": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "End0ModelPacketAndProjectiveNoGoImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "model_rank_match": packet["model_packet_summary"]["rank_match"],
        "projective_obstruction": packet["projective_obstruction"],
        "repair_paths": packet["repair_paths"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    rank = cert["model_rank_match"]
    obstruction = cert["projective_obstruction"]
    return f"""# End0 ModelPacket and ProjectiveNoGo Import v1

Status: `{cert["status"]}`.

The End0-to-sector gate now has a concrete model packet:

```text
direct_sum_total_rank = {rank["direct_sum_total_rank"]}
sector shape          = {rank["six_matter_triplets_plus_H_singlet"]}
rank match            = {rank["matches_expected_sector_kernel_rank_sum"]}
```

But the ordinary End0-to-current-BN functor is rejected.  The current BN target
has a nontrivial projective cocycle:

```text
obstruction = {obstruction["type"]}
gap_from_ordinary_phase = {obstruction["numerical_gap_from_ordinary_phase"]}
```

So the next legal route is a gerbe-twisted/central-extension End0 sector functor
or direct physical `alpha1` source values.  Existing BN/compact matrices remain
diagnostic support only.

No observed masses, CKM/PMNS data, benchmark matrices, or target residuals are
used as selectors.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
