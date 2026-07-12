"""Attempt same-branch emission of U10/Ubar5 and the 1_M Dirac rule.

This artifact pushes beyond the dual-route gate.  It imports the strongest
selected stationary source result currently available: symbolic
transport-conjugation promotes projector/Riesz/Green/source identities and a
validator-ready sector rho_s packet.  Then it tests whether that selected
stationary rho_s is enough to emit the ordered SU(5) matter-slot polarization
and the 1_M Dirac-neutrino shift rule.

Result expected from current corpus: no full promotion.  The missing object is
not generic selected source anymore; it is a selected matter-slot
transversality/readout functional from the same source.
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

PREVIOUS = DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"
TRANSPORT = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
MATTER_THEOREM = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
SECTOR_CHARGE_CERT = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
ONE_M_RULE = DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json"
SU5_TRANS_CERT = Q79 / "certificates" / "su5_matter_slot_transversality_certificate.json"
SU5_SOURCE_CERT = Q79 / "certificates" / "selected_su5_source_proof_attempt_certificate.json"

OUTPUT = DATA / "selected_u10ubar5_1m_samebranch_emission_attempt.candidate.json"
CERT = CERTS / "selected_u10ubar5_1m_samebranch_emission_attempt_certificate.json"
NOTE = CORPUS / "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1.md"

STATUS = "MTT_SELECTED_U10UBAR5_1M_SAMEBRANCH_EMISSION_ATTEMPT_REDUCED_TO_MATTERSLOT_TRANSVERSALITY_READOUT"
NEXT = "MTT_Selected_MatterSlot_Transversality_Readout_Functional_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    transport = load(TRANSPORT)
    gauge_trace = load(GAUGE_TRACE)
    dotd = load(DOTD_PROBE)
    matter = load(MATTER_THEOREM)
    sector_cert = load(SECTOR_CHARGE_CERT)
    one_m = load(ONE_M_RULE)
    trans = load(SU5_TRANS_CERT)
    su5_source = load(SU5_SOURCE_CERT)

    stationary_selected_source = {
        "selected_projector_source_verified": transport["promotion_decision"]["selected_projector_source_verified"],
        "selected_riesz_green_source_verified": transport["what_closes_now"]["selected_riesz_green_source_verified"],
        "selected_rho_s_validator_ready": transport["validator_result"]["selected_rho_s_validator_ready"],
        "selected_source_verified": transport["validator_result"]["selected_source_verified"],
        "functional_rho_s_promotion": gauge_trace["what_closes_now"]["functional_rho_s_promotion"],
        "selected_functional_zero_mode_bases": gauge_trace["what_closes_now"]["selected_functional_zero_mode_bases"],
    }
    stationary_source_closed = all(stationary_selected_source.values())

    dynamic_source = {
        "selected_dotD_source_formula_closed": dotd["promotion_decision"]["selected_dotD_source_formula_closed"],
        "selected_dotD_source_verified": dotd["promotion_decision"]["selected_dotD_source_verified_by_transport_derivative"],
        "alpha1_driver_verified": dotd["promotion_decision"]["alpha1_driver_verified"],
    }

    finite_su5_support = {
        "finite_transversality_theorem_closed": trans["calculation_results"]["finite_transversality_theorem_closed"],
        "retarded_q79_orientation_closed": trans["calculation_results"]["retarded_q79_orientation_closed"],
        "U_10": trans["calculation_results"]["selected_packet"]["U_10"],
        "U_bar5": trans["calculation_results"]["selected_packet"]["U_bar5"],
        "selected_mtt_source_present_in_q79_cert": trans["calculation_results"]["selected_mtt_source_present"],
        "selected_ordered_su5_packet_closed_in_q79_cert": trans["calculation_results"]["selected_ordered_su5_packet_closed"],
    }

    one_m_support = {
        "structural_1M_Dirac_rule_candidate_closed": one_m["decision"]["structural_1M_Dirac_rule_candidate_closed"],
        "selected_1M_Dirac_rule_closed": one_m["decision"]["selected_1M_Dirac_rule_closed"],
        "proposed_shift_route": one_m["structural_rule_candidate"]["proposed_shift_route"],
    }

    readout_tests = {
        "selected_source_can_emit_generic_rho_s": stationary_source_closed,
        "selected_source_emits_matter_slot_transversality_functional": False,
        "selected_source_distinguishes_10M_clock_from_bar5M_shift": False,
        "selected_source_attaches_1M_to_Dirac_shift_channel": False,
        "current_selected_sector_data_uniform": sector_cert["superset_paths"]["route_B"]["evidence"][
            "current_projector_dotd_payload_uniform"
        ],
        "matter_slot_charge_table_closed": matter["matter_slot_charge"]["selected_charge_table_closed"],
        "q79_selected_U10_Ubar5_source_claimed": su5_source["guardrails"]["claims_selected_U10_Ubar5"],
    }

    promoted = (
        stationary_source_closed
        and readout_tests["selected_source_emits_matter_slot_transversality_functional"]
        and readout_tests["selected_source_distinguishes_10M_clock_from_bar5M_shift"]
        and readout_tests["selected_source_attaches_1M_to_Dirac_shift_channel"]
    )

    minimal_readout_contract = {
        "name": "SelectedMatterSlotTransversalityReadoutFunctional",
        "domain": "same selected q79/F,m=1 stationary sector source with validator-ready rho_s and transported zero-mode bases",
        "must_compute": {
            "tau_10_clock": "nonzero/selected readout on 10_M slots giving U_10=I_3",
            "tau_bar5_shift": "transverse selected readout on bar5_M slots giving U_bar5=F",
            "tau_1M_Dirac_shift": "Dirac-neutrino readout attaching 1_M=N^c to the bar5_M 1_M 5_H channel",
            "phase_shift_partition": {"phase": ["u", "e"], "shift": ["d", "nuD"]},
            "normalization_link": "same readout must feed sector Gram/transfer normalization, not a scalar fit",
        },
        "acceptance_conditions": [
            "constructed from selected rho_s/K_s/projector/Green source data or equivalent selected SU(5) source identity",
            "reproduces U_10=I_3 and U_bar5=F as outputs, not hypotheses",
            "emits the 1_M Dirac shift rule as selected, not merely structural",
            "does not use locked C1 splitter columns, observed masses, CKM/PMNS, or benchmark matrices",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedU10Ubar51MSameBranchEmissionAttempt",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "transport_conjugation_replay": rel(TRANSPORT),
            "gauge_transported_phifin_trace": rel(GAUGE_TRACE),
            "dotd_transport_derivative_probe": rel(DOTD_PROBE),
            "matter_slot_charge_overlap_theorem": rel(MATTER_THEOREM),
            "sector_charge_or_chirality_certificate": rel(SECTOR_CHARGE_CERT),
            "one_M_dirac_rule_attempt": rel(ONE_M_RULE),
            "q79_su5_transversality_certificate": rel(SU5_TRANS_CERT),
            "q79_selected_su5_source_attempt_certificate": rel(SU5_SOURCE_CERT),
        },
        "superset_strategy": {
            "mode": "SAME_BRANCH_PROMOTION_ATTEMPT_WITH_SELECTED_STATIONARY_SOURCE",
            "using_one_straight_path": False,
            "straight_selected_source_path": "transported End0/HYM rho_s and zero-mode bases",
            "support_path": "q79 SU(5)/E6 finite transversality plus structural 1_M Dirac rule",
            "locked_target": "promote U_10/U_bar5/1_M sector routing only if emitted by same selected source readout",
            "observed_data_used": False,
            "target_fitting_used": False,
            "diagnostic_lift_used_as_proof": False,
        },
        "stationary_selected_source": stationary_selected_source,
        "dynamic_source_boundary": dynamic_source,
        "finite_su5_support": finite_su5_support,
        "one_M_support": one_m_support,
        "readout_tests": readout_tests,
        "minimal_readout_contract": minimal_readout_contract,
        "selection_decision": {
            "selected_stationary_source_available": stationary_source_closed,
            "selected_U10_Ubar5_1M_samebranch_emitted": promoted,
            "selected_U10_Ubar5_polarization_closed": False,
            "selected_1M_Dirac_neutrino_source_rule_closed": False,
            "selected_sector_charge_or_chirality_closed": False,
            "selected_transfer_normalization_promoted": False,
            "closure_claimed": False,
            "reason": (
                "The same branch now supplies selected stationary rho_s/projector/Riesz/Green support, "
                "but no current artifact defines the matter-slot transversality readout that turns that "
                "source into selected U_10, U_bar5, and 1_M Dirac shift outputs."
            ),
        },
        "what_closes_now": {
            "stationary_selected_source_imported_as_closed": stationary_source_closed,
            "generic_rho_s_no_longer_primary_blocker": stationary_source_closed,
            "finite_U10_Ubar5_support_retained": True,
            "structural_1M_rule_retained": one_m_support["structural_1M_Dirac_rule_candidate_closed"],
            "missing_object_sharpened_to_readout_functional": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_matter_slot_transversality_readout_functional": True,
            "selected_10M_clock_readout": True,
            "selected_bar5M_shift_readout": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_sector_charge_or_chirality_table": True,
            "selected_overlap_transfer_normalization": True,
            "selected_A_selected_and_b_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem_attempt": {
            "name": "SelectedU10Ubar51MSourcePromotionSameBranchEmission",
            "fully_proved": False,
            "proved_support": [
                "selected stationary rho_s/projector/Riesz/Green source identities are available from transport conjugation",
                "finite q79 SU(5) transversality still gives U_10=I_3 and U_bar5=F under readout/source hypothesis",
                "structural 1_M=N^c Dirac-neutrino rule still fixes the intended nuD shift side",
            ],
            "open_sublemma": "SelectedMatterSlotTransversalityReadoutFunctional",
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
                "stationary_selected_source_closed": stationary_source_closed,
                "selected_U10_Ubar5_1M_samebranch_emitted": promoted,
                "next_required_artifact": NEXT,
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected U10/Ubar5/1M Same-Branch Emission Attempt

Status: `MTT_SELECTED_U10UBAR5_1M_SAMEBRANCH_EMISSION_ATTEMPT_REDUCED_TO_MATTERSLOT_TRANSVERSALITY_READOUT`

This pushes the previous gate using the strongest selected source currently in
the repo.

## What Improves

The generic source obstruction is no longer quite the right description.  The
symbolic transport-conjugation replay supplies selected stationary
projector/Riesz/Green/source identities and a validator-ready sector `rho_s`
packet.  The gauge-transported `Phi_fin` trace also promotes the functional
zero-mode/projector picture.

So the missing object is now more specific than "selected source".

## What Still Fails

The selected stationary `rho_s` is still uniform at the matter-slot routing
level.  It does not by itself emit:

- `10_M` clock readout,
- `bar5_M` shift readout,
- `1_M=N^c` Dirac-neutrino shift readout,
- selected `U_10=I_3`, `U_bar5=F` as source outputs,
- selected sector route `u,e | d,nuD`.

The q79 finite transversality theorem and the structural E6/SU(5) dictionary
remain correct support, but they are not the selected readout functional.

## New Minimal Object

The next proof target is:

`SelectedMatterSlotTransversalityReadoutFunctional`.

It must be built from the same selected q79/F,m=1 source, either through the
transported `rho_s/K_s` zero-mode data or through an equivalent selected SU(5)
source identity.  It must output the matter-slot transversality packet, not
take it as a hypothesis, and it must not use observed constants, benchmark
matrices, locked C1 splitter columns, or diagnostic lifted flags.

Next artifact: `MTT_Selected_MatterSlot_Transversality_Readout_Functional_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
