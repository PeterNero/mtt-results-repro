"""Build the sector-charge / Gram-transfer normalization packet.

This packet is the next gate after the alpha1 transfer-normalization fill
attempt.  It separates forced algebraic normalization from selected source
emission:

* the adjoint triplet and trace Gram normalization are forced once rho_s is
  selected;
* the sector charge/chirality table and selected zero-mode/rho_s source are
  still not emitted, so transfer normalization cannot yet promote alpha1.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

ALPHA1_CUTSET = DATA / "selected_alpha1_sourcestrength_or_transfernormalization_fill_attempt.candidate.json"
SECTOR_CHARGE = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
TENSOR_CARRIER = DATA / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct.candidate.json"
ADJOINT_THEOREM = DATA / "selected_sector_zero_mode_adjointtriplet_realization_theorem.candidate.json"
VALUE_FILL = DATA / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill.candidate.json"
SOURCE_PAYLOAD = DATA / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json"
SOURCE_ACTION_CUTSET = DATA / "selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem.candidate.json"

OUTPUT = DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
CERT = CERTS / "selected_sectorcharge_gram_transfernormalization_packet_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorCharge_GramTransferNormalization_Packet_v1.md"

STATUS = "MTT_SELECTED_SECTORCHARGE_GRAM_TRANSFERNORMALIZATION_PACKET_BUILT_SOURCE_CHARGE_OPEN"
NEXT = "MTT_Selected_SectorCharge_or_ZeroModeBasis_SourceEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def build_note(data: dict[str, Any]) -> str:
    return f"""# MTT Selected Sector-Charge / Gram-Transfer Normalization Packet v1

Status: `{STATUS}`

Next artifact: `{NEXT}`

## Result

The packet separates three issues that were previously bundled together:

1. **Gram normalization:** conditionally fixed. If selected `rho_s` is emitted
   as the adjoint action on selected three-dimensional matter zero modes, the
   invariant trace convention forces `G_s=I_3` and
   `||rho_s(T_i)||_F^2=2`; unit transfer uses `rho_s(T_i)/sqrt(2)`.
2. **Sector charge/chirality:** still open. Current selected `Phi_fin` and
   Route-C projector/dotD data treat `u,d,e,N` uniformly, so the
   `{{u,e}}|{{d,nuD}}` split is not selected by current source data.
3. **Transfer normalization:** still open as selected physical data. Scalar
   normalization is algebraically determined after `rho_s`, but no selected
   zero-mode/rho_s source or sector charge table emits it yet.

## Promotion Decision

No alpha1 driver is promoted. The packet proves that the remaining problem is
not numerical scalar choice; it is selected source emission for sector charge
or selected zero-mode/rho_s carriers.

## Minimal Open Fields

```json
{json.dumps(data["minimal_open_fields"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    alpha1 = load(ALPHA1_CUTSET)
    sector_charge = load(SECTOR_CHARGE)
    tensor = load(TENSOR_CARRIER)
    adjoint = load(ADJOINT_THEOREM)
    value_fill = load(VALUE_FILL)
    source_payload = load(SOURCE_PAYLOAD)
    source_action = load(SOURCE_ACTION_CUTSET)

    gram = value_fill["conditional_gram_normalization_theorem"]
    tensor_norm = tensor["normalization_boundary"]
    tensor_validation = tensor["validation"]
    sector_result = sector_charge["certificate_result"]
    source_chain = source_payload["source_chain"]

    matter_norms = tensor_validation["sector_T3_response_norms"]
    matter_sectors = ["Q", "u", "d", "L", "e", "N"]
    equal_matter_norms = (
        tensor_validation["matter_T3_norms_equal"] is True
        and all(abs(matter_norms[s]["frobenius_norm"] - 2**0.5) < 1e-12 for s in matter_sectors)
        and matter_norms["H"]["zero_response"] is True
    )

    gram_conditionally_forced = (
        gram["proved"] is True
        and tensor_validation["all_lie_checks_pass"] is True
        and tensor_validation["all_projectors_idempotent"] is True
        and equal_matter_norms
    )
    selected_rho_s_emitted = source_payload["promotion_decision"]["selected_source_map_emitted"] is True
    selected_zero_modes_emitted = source_payload["promotion_decision"]["selected_zero_mode_bases_emitted"] is True
    selected_sector_charge = sector_result["selected_certificate_closed"] is True
    selected_transfer_normalization = (
        gram_conditionally_forced
        and selected_rho_s_emitted
        and selected_zero_modes_emitted
        and selected_sector_charge
    )

    minimal_open_fields = {
        "selected_sector_charge_or_chirality_table": {
            "closed": selected_sector_charge,
            "required_partition": {
                "phase_route": sector_result["phase_route_required"],
                "shift_route": sector_result["shift_route_required"],
            },
            "why_open": sector_result["why_not_closed"],
        },
        "selected_zero_mode_bases_K_s": {
            "closed": selected_zero_modes_emitted,
            "required": source_payload["conditional_promotion_rule"]["proof_obligation_remaining"][0],
            "why_open": source_payload["promotion_decision"]["why_not_promoted"],
        },
        "selected_rho_s_source_map": {
            "closed": selected_rho_s_emitted,
            "candidate_constructed": source_payload["promotion_decision"]["canonical_source_map_constructed"],
            "conditional_rule_recorded": source_payload["conditional_promotion_rule"]["recorded"],
        },
        "selected_1M_Dirac_neutrino_rule": {
            "closed": False,
            "required_by": "nuD singlet routing in the sector-charge packet",
            "why_open": "The current matter-slot route has no selected 1_M Dirac-neutrino/singlet rule.",
        },
    }

    data = {
        "candidate": "MTTSelectedSectorChargeGramTransferNormalizationPacket",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "alpha1_cutset": rel(ALPHA1_CUTSET),
            "sector_charge": rel(SECTOR_CHARGE),
            "tensor_carrier": rel(TENSOR_CARRIER),
            "adjoint_theorem": rel(ADJOINT_THEOREM),
            "value_fill": rel(VALUE_FILL),
            "source_payload": rel(SOURCE_PAYLOAD),
            "source_action_cutset": rel(SOURCE_ACTION_CUTSET),
        },
        "sector_charge_packet": {
            "selected": selected_sector_charge,
            "required_phase_route": sector_result["phase_route_required"],
            "required_shift_route": sector_result["shift_route_required"],
            "strongest_structural_match": sector_result["strongest_structural_match"],
            "current_selected_data_uniform": sector_charge["current_mtt_data_tests"][
                "phifin_distinguishes_u_e_from_d_N"
            ]
            is False
            and sector_charge["current_mtt_data_tests"]["projector_dotd_uniformity"][
                "all_right_family_payloads_identical"
            ]
            is True,
            "why_not_selected": sector_result["why_not_closed"],
        },
        "gram_transfer_packet": {
            "conditional_gram_theorem_proved": gram["proved"],
            "gram_conditionally_forced_after_rho_s": gram_conditionally_forced,
            "selected_rho_s_emitted": selected_rho_s_emitted,
            "selected_zero_mode_bases_emitted": selected_zero_modes_emitted,
            "raw_T3_frobenius_norm_per_matter_sector": tensor_norm[
                "raw_T3_frobenius_norm_per_matter_sector"
            ],
            "unit_trace_transfer": "rho_s(T_i)/sqrt(2) per selected matter triplet after G_s=I_3",
            "H_singlet_zero_response": matter_norms["H"]["zero_response"],
            "matter_T3_norms_equal": tensor_validation["matter_T3_norms_equal"],
            "physical_transfer_normalization_selected": selected_transfer_normalization,
            "why_not_selected": tensor_norm["why_open"],
        },
        "source_action_route": {
            "cutset_closed": source_action["cutset_closed"],
            "route_A_passes_now": source_action["route_A"]["passes_now"],
            "route_B_passes_now": source_action["route_B"]["passes_now"],
            "source_map_candidate_constructed": source_payload["promotion_decision"][
                "canonical_source_map_constructed"
            ],
            "minimal_new_theorem_needed": source_payload["promotion_decision"][
                "minimal_new_theorem_needed"
            ],
            "coherent_spectral_zero_mode_retention": source_chain[
                "coherent_spectral_zero_mode_retention"
            ],
        },
        "transfer_to_alpha1_decision": {
            "selected_transfer_normalization": selected_transfer_normalization,
            "typed_BN_alpha1_tangent_emitted": False,
            "honest_dotD_replay_closed": False,
            "alpha1_driver_verified": False,
            "reason": "Gram scalar is conditionally fixed, but selected sector charge and selected zero-mode/rho_s source emission are still open.",
        },
        "minimal_open_fields": minimal_open_fields,
        "what_closes_now": {
            "conditional_Gram_transfer_scalar_fixed_after_rho_s": gram_conditionally_forced,
            "sector_charge_gap_is_independent_source_data": True,
            "selected_transfer_requires_source_not_scalar_fit": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_sector_charge_or_chirality_table": True,
            "selected_zero_mode_bases_K_s": True,
            "selected_rho_s_source_map": True,
            "selected_1M_Dirac_neutrino_rule": True,
            "typed_BN_alpha1_tangent": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "classification": "CONDITIONAL_GRAM_CLOSURE_PLUS_SOURCE_CHARGE_CUTSET",
            "straight_path": "selected zero-mode/rho_s source action emits Gram normalization",
            "alternative_path": "selected matter-slot sector charge/chirality emits transfer routing",
            "locked_target": "typed alpha1 transfer normalization without observed constants or lifted flags",
            "uses_observed_constants": False,
        },
    }

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": "MTTSelectedSectorChargeGramTransferNormalizationPacket",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "conditional_gram_transfer_scalar_fixed_after_rho_s": gram_conditionally_forced,
        "selected_sector_charge": selected_sector_charge,
        "selected_transfer_normalization": selected_transfer_normalization,
        "alpha1_driver_verified": False,
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(build_note(data), encoding="utf-8")
    print(json.dumps({"status": STATUS, "candidate": rel(OUTPUT), "certificate": rel(CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
