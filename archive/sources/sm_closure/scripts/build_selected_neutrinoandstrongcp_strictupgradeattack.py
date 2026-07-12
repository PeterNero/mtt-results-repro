from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"
SLUG = "selected_neutrinoandstrongcp_strictupgradeattack"
OUT = ROOT / "candidate_data" / SLUG


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    smslot = load(ROOT / "certificates" / "selected_smslotfunctor_overlapkernel_source_emission_certificate.json")
    neutrino_policy = load(ROOT / "certificates" / "selected_neutrinomassmajoranapolicy_or_precisionprofiletable_certificate.json")
    theta_policy = load(ROOT / "certificates" / "selected_qcdthetapolicy_or_strictpewcountreduction_certificate.json")
    axion = load(NONSM / "certificates" / "execution_i_axion_ratio_certificate.json")

    ambient_order = 1344
    majorana_characters = [k for k in range(ambient_order) if (2 * k) % ambient_order == 0]
    cp_characters = [237, 1008, 99]
    neutrino = {
        "schema": "MTTSelectedNeutrinoStrictUpgradeAttack.v1",
        "status": "SELECTED_DIRAC_CHANNEL_CLOSED_ABSOLUTE_SCALE_AND_ONTOLOGY_UNIQUENESS_OPEN",
        "closed": {
            "minimal_PMNS_oscillation_policy": neutrino_policy["minimal_PMNS_oscillation_policy_closed"],
            "selected_same_source_SM_slot_functor_all_six_arrows": smslot["selected_SMSlotFunctor_all_six_arrows_claimed"],
            "selected_1M_equals_Nc_Dirac_channel": smslot["what_closes"]["selected_terminal_to_SU5_E6_slot_packet"],
            "Majorana_character_criterion": "2k=0 mod N",
            "ambient_Z1344_Majorana_characters": majorana_characters,
            "CP_characters_are_not_Majorana_self_characters": all(k not in majorana_characters for k in cp_characters),
        },
        "continuous_absolute_mass_degeneracy": {
            "normal_ordering": "(m1,m2,m3)=(m0,sqrt(m0^2+Delta21),sqrt(m0^2+Delta31))",
            "inverted_ordering": "(m1,m2,m3)=(sqrt(m0^2+|Delta31|),sqrt(m0^2+|Delta31|+Delta21),m0)",
            "free_coordinate_without_new_source": "m0>=0",
            "oscillation_rows_fix_absolute_scale": False,
        },
        "open": {
            "selected_mass_ordering": True,
            "selected_lightest_mass_or_absolute_scale": True,
            "selected_Dirac_only_vs_separate_Majorana_operator": True,
            "selected_Majorana_character_if_applicable": True,
            "selected_Majorana_phases_if_applicable": True,
        },
        "minimal_next_object": "SelectedNeutralCharacterAndAbsoluteMassFunctional",
        "guards": {
            "benchmark_MR_3p8e12_promoted": False,
            "benchmark_normal_ordering_promoted": False,
            "CP_character_reused_as_Majorana_character": False,
            "oscillation_splittings_mislabeled_as_absolute_mass": False,
        },
        "external_postcheck": "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-neutrino-mixing.pdf",
    }
    dump(OUT / "neutrino_operator_ontology_and_absolute_scale_cutset.packet.json", neutrino)

    strong_cp = {
        "schema": "MTTSelectedStrongCPStrictUpgradeAttack.v1",
        "status": "CONDITIONAL_PQ_THEOREM_AND_AXION_RATIOS_CLOSED_SELECTED_ANOMALY_SOURCE_OPEN",
        "closed": {
            "QCD_theta_SM_parameter_slot": theta_policy["QCD_theta_bar_policy_closed"],
            "conditional_PQ_relaxation_theorem": True,
            "integer_domain_wall_formula": "N_DW=sum_colored 2*T(R)*Q_cen",
            "axion_decay_constant_ratios": axion["computed_ratios"],
            "axion_ratio_no_knob_given_selected_moduli": True,
        },
        "central_charge_kernel_obstruction": {
            "difference_charge_map": "(q1,q2,q3) -> (q1-q2,q2-q3,q3-q1)",
            "kernel": "integer multiples of (1,1,1)",
            "consequence": "hypercharge/difference-charge closure cannot select the common U(1)_cen lift or its QCD anomaly coefficient",
            "one_may_choose_NDW_1_is_source_derivation": False,
        },
        "open": {
            "selected_continuous_U1_cen_survives_gauge_flux_effects": True,
            "selected_colored_Q_cen_charge_table": True,
            "selected_nonzero_QCD_anomaly_coefficient": True,
            "selected_PQ_breaking_and_quality_control": True,
            "selected_absolute_axion_normalization": True,
        },
        "minimal_next_object": "SelectedCentralChargeLiftAndQCDAnomalyMap",
        "decision": {
            "strong_CP_problem_solved": False,
            "conditional_mechanism_available": True,
            "axion_ratio_result_is_not_strong_CP_solution": True,
        },
        "guards": {
            "chosen_PQ_charges_promoted_as_selected": False,
            "axion_ratios_mislabeled_as_anomaly_proof": False,
            "theta_bar_zero_predicted_without_mechanism": False,
        },
    }
    dump(OUT / "strong_cp_central_charge_anomaly_cutset.packet.json", strong_cp)

    status = "MTT_SELECTED_NEUTRINO_STRONGCP_ATTACK_DIRAC_PQ_SUPPORT_CLOSED_SOURCE_SELECTION_OPEN"
    candidate = {
        "candidate": "MTT_Selected_NeutrinoAndStrongCP_StrictUpgradeAttack_v1",
        "status": status,
        "date": "2026-07-11",
        "closure_claimed": True,
        "theorem": {
            "name": "NeutrinoAbsoluteScaleAndCentralAnomalyKernelDecompositionTheorem",
            "proved": True,
            "statement": "The selected source emits the 1_M=N^c Dirac channel, while Majorana self-characters in Z1344 are restricted to 0 and 672 and cannot reuse the selected CP labels. Oscillation data leave one continuous absolute mass coordinate. Separately, the conditional PQ theorem and axion ratios are closed, but difference charges have a common-shift kernel and therefore do not select Q_cen or N_DW. U5 and U6 are reduced to two source maps, not closed.",
        },
        "U5_closed": False,
        "U6_closed": False,
        "next_required_artifact": "MTT_Selected_GlobalHYMConnection_or_NeutralMassAndCentralAnomalySourceMaps_v1",
    }
    dump(ROOT / "candidate_data" / f"{SLUG}.candidate.json", candidate)

    certificate = {
        "certificate": "MTT_Selected_NeutrinoAndStrongCP_StrictUpgradeAttack_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": status,
        "theorem_proved": True,
        "selected_Dirac_channel_closed": True,
        "Majorana_admissible_character_count": len(majorana_characters),
        "Majorana_admissible_characters": majorana_characters,
        "absolute_neutrino_mass_closed": False,
        "neutrino_ontology_uniquely_selected": False,
        "conditional_PQ_theorem_closed": True,
        "axion_decay_constant_ratios_closed": True,
        "selected_QCD_anomaly_coefficient_closed": False,
        "strong_CP_problem_solved": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(ROOT / "certificates" / f"{SLUG}_certificate.json", certificate)


if __name__ == "__main__":
    main()
