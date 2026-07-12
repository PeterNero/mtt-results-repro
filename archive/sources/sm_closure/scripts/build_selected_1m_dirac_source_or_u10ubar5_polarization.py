"""Build the selected 1_M Dirac source / U10-Ubar5 polarization gate.

This is the source-promotion step after the structural 1_M Dirac-neutrino rule.
It tests two legal promotion routes:

Route A: q79 SU(5)/E6 polarization source, where finite transversality gives
         U_10=I_3 and U_bar5=F under a selected-source hypothesis.
Route B: HYM/projector zero-mode source, where selected zero-mode projectors
         could derive the sector partition without importing SU(5) as a proof.

The artifact is deliberately conservative: support can close, but selected
promotion requires theorem-derived same-branch source emission.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

PREVIOUS = DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json"
GRAM = DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
MATTER_THEOREM = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
SU5_TRANS_CERT = Q79 / "certificates" / "su5_matter_slot_transversality_certificate.json"
SU5_SOURCE_CERT = Q79 / "certificates" / "selected_su5_source_proof_attempt_certificate.json"
TIME_ORIENTED_CERT = Q79 / "certificates" / "time_oriented_conjugate_branch_selection_certificate.json"
E6_DICT_CERT = Q79 / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"
HYM_BRIDGE = DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"
HYM_VALUES = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
SOURCE_PAYLOAD = DATA / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json"

OUTPUT = DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"
CERT = CERTS / "selected_1m_dirac_source_or_u10ubar5_polarization_certificate.json"
NOTE = CORPUS / "MTT_Selected_1M_DiracNeutrino_Source_or_U10Ubar5Polarization_v1.md"

STATUS = "MTT_SELECTED_1M_DIRAC_SOURCE_OR_U10UBAR5_POLARIZATION_GATE_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    gram = load(GRAM)
    matter = load(MATTER_THEOREM)
    trans = load(SU5_TRANS_CERT)
    su5_source = load(SU5_SOURCE_CERT)
    time_oriented = load(TIME_ORIENTED_CERT)
    e6 = load(E6_DICT_CERT)
    hym_bridge = load(HYM_BRIDGE)
    hym_values = load(HYM_VALUES)
    source_payload = load(SOURCE_PAYLOAD)

    trans_calc = trans["calculation_results"]
    su5_calc = su5_source["calculation_results"]
    hym_validator = hym_values["validator_result"]
    previous_rule = previous["structural_rule_candidate"]

    route_a_support_closed = (
        trans_calc["finite_transversality_theorem_closed"] is True
        and trans_calc["retarded_q79_orientation_closed"] is True
        and trans_calc["selected_packet"]["U_10"] == "I_3"
        and trans_calc["selected_packet"]["U_bar5"] == "F"
        and previous_rule["one_M_maps_to_Nc"] is True
        and previous_rule["dirac_operator_uses_bar5_1M_5H"] is True
    )
    route_a_selected_closed = (
        trans_calc["selected_mtt_source_present"] is True
        and trans_calc["selected_ordered_su5_packet_closed"] is True
        and su5_calc["selected_projection_tensor_promoted"] is True
        and su5_source["guardrails"]["claims_selected_U10_Ubar5"] is True
    )

    route_b_support_closed = (
        hym_values["what_closes_now"]["finite_model_active_projector_values_emitted"] is True
        and hym_validator["all_projector_checks_pass"] is True
        and hym_validator["all_basis_counts_pass"] is True
        and hym_validator["End0_equivariance_on_emitted_projectors"] is True
        and hym_bridge["theorem"]["bridge_theorem_proved"] is True
    )
    route_b_selected_closed = (
        hym_validator["selected_HYM_projector_values_promoted"] is True
        and hym_validator["rho_candidate_promoted_to_selected_rho_s"] is True
        and all(hym_validator["selected_source_flags"].values())
    )

    selected_1m_rule_closed = (
        route_a_selected_closed
        and previous["decision"]["selected_1M_Dirac_rule_closed"] is True
    )
    selected_sector_closed = route_a_selected_closed or route_b_selected_closed
    transfer_promoted = selected_sector_closed and gram["gram_transfer_packet"]["physical_transfer_normalization_selected"] is True

    route_a = {
        "name": "SU5_E6_q79_polarization_route",
        "support_closed": route_a_support_closed,
        "selected_closed": route_a_selected_closed,
        "finite_packet": trans_calc["selected_packet"],
        "structural_1M_rule_available": previous["what_closes_now"]["structural_1M_Dirac_rule_candidate"],
        "source_flags": {
            "selected_mtt_source_present": trans_calc["selected_mtt_source_present"],
            "selected_ordered_su5_packet_closed": trans_calc["selected_ordered_su5_packet_closed"],
            "selected_projection_tensor_promoted": su5_calc["selected_projection_tensor_promoted"],
            "claims_selected_U10_Ubar5": su5_source["guardrails"]["claims_selected_U10_Ubar5"],
        },
        "promotion_test": [
            "finite q79 transversality must be closed",
            "same-branch selected source must emit ordered 10_M/bar5_M matter-slot packet",
            "U_10=I_3 and U_bar5=F must be source outputs, not conditional fixture values",
            "1_M=N^c Dirac rule must be selected as a same-source neutrino slot rule",
        ],
        "verdict": (
            "Route A is the best current route: finite algebra and structural 1_M rule close, "
            "but selected source promotion is still absent."
        ),
    }

    route_b = {
        "name": "HYM_projector_zero_mode_source_route",
        "support_closed": route_b_support_closed,
        "selected_closed": route_b_selected_closed,
        "projector_payload_summary": {
            "finite_projector_values_emitted": hym_validator["finite_projector_values_emitted"],
            "selected_HYM_projector_values_promoted": hym_validator["selected_HYM_projector_values_promoted"],
            "rho_candidate_promoted_to_selected_rho_s": hym_validator["rho_candidate_promoted_to_selected_rho_s"],
            "selected_source_flags": hym_validator["selected_source_flags"],
        },
        "promotion_test": [
            "same selected HYM/Strominger operator values must emit D_E,s for all sectors",
            "selected Riesz projectors and ordered zero-mode bases K_s must be theorem-derived",
            "rho_s must be promoted from rho_candidate in the selected bases",
            "matter-slot routing must be derived from those selected sector actions, not from the locked C1 target",
        ],
        "verdict": (
            "Route B has strong finite projector support, but current values are model-active "
            "and fail selected-source promotion."
        ),
    }

    same_branch_contract = {
        "must_emit": {
            "selected_q79_or_conjugate_branch": True,
            "selected_ordered_matter_slot_packet": ["10_M_clock", "bar5_M_shift", "1_M_Dirac_shift"],
            "selected_polarization_values": {"U_10": "I_3", "U_bar5": "F"},
            "selected_sector_route": {"phase": ["u", "e"], "shift": ["d", "nuD"]},
            "selected_zero_mode_or_SU5_source_identity": True,
            "selected_overlap_transfer_normalization": True,
        },
        "forbidden_inputs": [
            "observed flavor data",
            "benchmark Yukawa or CKM matrices",
            "locked splitter columns as source selectors",
            "diagnostic lifted selected-source flags",
            "conditional transversality treated as selected source",
        ],
    }

    candidate = {
        "candidate": "MTTSelected1MDiracSourceOrU10Ubar5PolarizationGate",
        "status": STATUS,
        "inputs": {
            "previous_1M_rule_attempt": rel(PREVIOUS),
            "sectorcharge_gram_transfer_packet": rel(GRAM),
            "matter_slot_charge_overlap_theorem": rel(MATTER_THEOREM),
            "q79_su5_transversality_certificate": rel(SU5_TRANS_CERT),
            "q79_selected_su5_source_attempt_certificate": rel(SU5_SOURCE_CERT),
            "q79_time_oriented_branch_selection_certificate": rel(TIME_ORIENTED_CERT),
            "q79_e6_dictionary_certificate": rel(E6_DICT_CERT),
            "hym_projector_bridge": rel(HYM_BRIDGE),
            "hym_projector_value_emission": rel(HYM_VALUES),
            "sector_zero_mode_source_payload": rel(SOURCE_PAYLOAD),
        },
        "superset_strategy": {
            "mode": "DUAL_ROUTE_SOURCE_PROMOTION_GATE",
            "using_one_straight_path": False,
            "primary_route": "Route A: q79 SU(5)/E6 polarization with structural 1_M Dirac rule.",
            "cross_check_route": "Route B: selected HYM/projector zero-mode source route.",
            "locked_target": "emit selected u,e | d,nuD sector charge/chirality and transfer normalization without target fitting",
            "observed_data_used": False,
            "target_fitting_used": False,
            "diagnostic_lift_used_as_proof": False,
        },
        "route_A_SU5_E6_polarization": route_a,
        "route_B_HYM_projector_zero_mode": route_b,
        "same_branch_promotion_contract": same_branch_contract,
        "selection_decision": {
            "selected_U10_Ubar5_polarization_closed": route_a_selected_closed,
            "selected_1M_Dirac_neutrino_source_rule_closed": selected_1m_rule_closed,
            "selected_sector_charge_or_chirality_closed": selected_sector_closed,
            "selected_transfer_normalization_promoted": transfer_promoted,
            "alpha1_driver_promoted": False,
            "closure_claimed": False,
            "reason": (
                "Both legal routes are reduced to selected same-branch source emission. Route A has the "
                "right finite q79 packet and structural 1_M rule; Route B has model-active projectors. "
                "Neither currently emits selected source values."
            ),
        },
        "what_closes_now": {
            "route_A_finite_polarization_support": route_a_support_closed,
            "route_A_structural_1M_rule_support": previous["what_closes_now"]["structural_1M_Dirac_rule_candidate"],
            "route_B_projector_support": route_b_support_closed,
            "same_branch_promotion_contract_built": True,
            "exact_remaining_source_obligation_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_U10_clock_source": True,
            "selected_Ubar5_shift_source": True,
            "selected_1M_Dirac_neutrino_shift_source": True,
            "selected_ordered_matter_slot_packet": True,
            "selected_zero_mode_projector_or_SU5_source_identity": True,
            "selected_overlap_transfer_normalization": True,
            "selected_A_selected_and_b_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem_attempt": {
            "name": "SelectedU10Ubar5PolarizationAnd1MDiracSourceRule",
            "fully_proved": False,
            "proved_support": [
                "finite q79 transversality gives U_10=I_3 and U_bar5=F under source hypothesis",
                "E6/SU(5) dictionary structurally places 1_M=N^c in the Dirac-neutrino channel",
                "model-active HYM/projector values have rank/gap/equivariance support",
            ],
            "open_sublemma": "Selected same-branch source emission of U_10, U_bar5, and 1_M Dirac shift rule",
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "closure_claimed": False,
                "target_fitting_used": False,
                "route_A_support_closed": route_a_support_closed,
                "route_A_selected_closed": route_a_selected_closed,
                "route_B_support_closed": route_b_support_closed,
                "route_B_selected_closed": route_b_selected_closed,
                "selected_sector_charge_or_chirality_closed": selected_sector_closed,
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected 1_M DiracNeutrino Source or U10/Ubar5 Polarization

Status: `MTT_SELECTED_1M_DIRAC_SOURCE_OR_U10UBAR5_POLARIZATION_GATE_BUILT_SOURCE_PROMOTION_OPEN`

This artifact attempts the next source-promotion gate after the structural
`1_M` Dirac-neutrino rule.

## Route A: SU(5)/E6 Polarization

Route A is the primary route.  The q79 finite transversality certificate gives,
under a selected-source hypothesis:

- `U_10 = I_3`,
- `U_bar5 = F`,
- retarded q79 orientation rather than the conjugate branch.

Together with the E6/SU(5) dictionary, this structurally gives:

- `10_M` clock/phase side: `u,e`,
- `bar5_M` shift side: `d`,
- `1_M=N^c` Dirac-neutrino shift side: `nuD`.

This route does not close yet because the selected source that emits the
ordered `10_M/bar5_M/1_M` packet is still absent.

## Route B: HYM / Zero-Mode Projectors

Route B tries to derive the same sector partition from selected zero-mode
projectors and the selected sector source map `rho_s`.  The current repo has
strong finite support: model-active projectors, ordered basis ids, rank/gap
checks, and End0 equivariance.  But these values are not yet promoted as
selected HYM/Strominger projectors, so this route also remains open.

## What This Achieves

The remaining proof object is now precise:

`Selected same-branch source emission of U_10, U_bar5, and the 1_M Dirac shift rule`.

The source must emit the sector route `u,e | d,nuD` and the overlap/transfer
normalization from the same branch.  Conditional transversality, model-active
projectors, diagnostic lifted flags, observed constants, and locked splitter
columns cannot promote the result.

Next artifact: `MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
