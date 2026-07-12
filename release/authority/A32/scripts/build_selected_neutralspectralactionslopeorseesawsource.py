"""Execute and discriminate the remaining neutral spectral/seesaw source routes."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
SLUG = "selected_neutralspectralactionslopeorseesawsource"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_spectral_and_seesaw_source_discrimination.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralSpectralActionSlopeOrSeesawSource_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_SPECTRAL_AND_SEESAW_CANDIDATES_EXECUTED_TRANSFER_FUNCTOR_OPEN"
NEXT = "MTT_Selected_NeutralCircleToMassCostTransferOrRealStructureFunctor_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def three_basin_ratio(phi: float) -> float:
    values = sorted(math.cos(phi + 2.0 * math.pi * k / 3.0) for k in range(3))
    gaps = [values[1] - values[0], values[2] - values[1]]
    return min(gaps) / (values[2] - values[0])


def main() -> int:
    predecessor = load(
        ROOT / "candidate_data" / "selected_neutralphysicalunitornilanchorprojector"
        / "neutral_scale_invariant_obstruction_and_spectral_repair.packet.json"
    )
    ontology = load(
        ROOT / "candidate_data" / "selected_neutrinoandstrongcp_strictupgradeattack"
        / "neutrino_operator_ontology_and_absolute_scale_cutset.packet.json"
    )
    phase = load(Q79 / "certificates" / "iwasawa_c6_global_phase_block_certificate.json")
    branch = load(Q79 / "certificates" / "time_oriented_conjugate_branch_selection_certificate.json")
    tau_source = load(
        CONSTANTS / "candidate_data" / "const_gr_01_absolute_scale_g2_modal_gap_dimensional_anchor_packet_fill"
        / "same_branch_tau_rod_clock_bridge.packet.json"
    )

    postcheck = predecessor["scale_invariant_obstruction"]["normal_ordering_postcheck_ratio"]
    tau_int = tau_source["relative_values"]["tau_int"]
    tau_exact = math.log(448.0) / 15.0
    canonical_spt_ratio = 1.0 / (math.exp(3.0 * tau_int) + 1.0)
    q79 = branch["residue_calculation"]["selected_residues"]["crt_q"]
    q369 = branch["residue_calculation"]["conjugate_residues"]["q"]
    q7 = branch["residue_calculation"]["selected_residues"]["q_7"]
    qmod = branch["residue_calculation"]["modulus"]
    phase_rows = {
        "q79_global_phase": three_basin_ratio(2.0 * math.pi * q79 / qmod),
        "q369_conjugate_phase": three_basin_ratio(2.0 * math.pi * q369 / qmod),
        "q7_over_qmod_drift": three_basin_ratio(2.0 * math.pi * q7 / qmod),
        "A29_relative_phase_pi_over_6": three_basin_ratio(math.pi / 6.0),
    }

    checks = {
        "predecessor_no_go_proved": predecessor["theorem"]["proved"],
        "tau_role_structurally_closed": tau_source["verdict"]["structural_bridge_closed"],
        "tau_internal_exact_identity": abs(tau_int - tau_exact) < 1e-15,
        "q79_time_oriented_branch_selected": branch["calculation_results"]["time_oriented_retarded_branch_selects_q79"],
        "q79_phase_is_unit_modulus_zero_action": phase["calculation_results"]["unit_modulus"] and phase["calculation_results"]["pure_flat_action_S"] == 0,
        "q79_phase_cannot_set_magnitude": phase["physical_implications"]["C6_phase_alone_cannot_set_mass_or_mixing_magnitudes"],
        "cp_character_reuse_as_majorana_forbidden": ontology["guards"]["CP_character_reused_as_Majorana_character"] is False,
        "canonical_spt_candidate_misses_postcheck": abs(canonical_spt_ratio - postcheck) > 0.1,
        "all_circle_phase_candidates_miss_exact_postcheck": all(abs(value - postcheck) > 1e-6 for value in phase_rows.values()),
    }
    theorem_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedNeutralSpectralActionSlopeOrSeesawSource.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralPhysicalUnitOrNilAnchorProjector_v1",
        "theorem": {
            "name": "NeutralSpectralAndSeesawSourceDiscriminationTheorem",
            "proved": theorem_proved,
            "statement": "The selected proper-time role, retarded q79/conjugate circle phase, q7 residue, and A29 relative phase can all be executed as source-motivated neutral shape candidates, but none supplies the required physical hierarchy under an already proved neutral mass-cost transfer. The canonical point-support SPT slope beta=tau_int gives the wrong ratio, the circle candidates fail the exact postcheck, and the selected CP character is not the separately typed Majorana self-character. Therefore neither a spectral slope nor a seesaw block is selected by the current packets; the exact missing object is a typed neutral circle/proper-time-to-mass-cost transfer or a neutral real-structure functor.",
        },
        "source_checks": checks,
        "spectral_action_route": {
            "selected_tau_role": True,
            "tau_int_formula": "log(448)/15",
            "tau_int": tau_int,
            "canonical_point_support_trial": "mu(tau)=delta(tau-tau_int), with diagnostic inverse-survival cost exp(tau*Delta_lambda)-1",
            "canonical_beta_trial": tau_int,
            "canonical_ratio_trial": canonical_spt_ratio,
            "postcheck_ratio": postcheck,
            "ratio_residual": canonical_spt_ratio - postcheck,
            "SPT_measure_mu_selected_for_neutral_mass": False,
            "inverse_survival_mass_cost_map_selected": False,
            "selected_beta_emitted": False,
            "classification": "SOURCE_MOTIVATED_TRIAL_REJECTED_AS_EXACT_NEUTRAL_COMPLETION",
        },
        "circle_drift_route": {
            "three_basin_formula": "lambda_k=x+A*cos(phi+2*pi*k/3)",
            "ratio_rule": "min(adjacent sorted gaps)/(max-min)",
            "candidate_ratios": phase_rows,
            "postcheck_ratio": postcheck,
            "closest_candidate": "q7_over_qmod_drift",
            "closest_absolute_residual": abs(phase_rows["q7_over_qmod_drift"] - postcheck),
            "selected_circle_to_nil_drift_map_emitted": False,
            "exact_candidate_selected": False,
            "classification": "CLOSE_NUMERICAL_CLUE_NOT_A_SOURCE_THEOREM",
        },
        "majorana_seesaw_route": {
            "ambient_character_group": "Z1344",
            "majorana_self_character_equation": ontology["closed"]["Majorana_character_criterion"],
            "admissible_self_characters": ontology["closed"]["ambient_Z1344_Majorana_characters"],
            "selected_CP_characters_are_not_Majorana_self_characters": ontology["closed"]["CP_characters_are_not_Majorana_self_characters"],
            "q79_or_q369_reused_as_majorana_character": False,
            "selected_neutral_real_structure_emitted": False,
            "selected_ML_or_MR_rows_emitted": False,
            "selected_seesaw_block_emitted": False,
            "classification": "TYPED_REAL_STRUCTURE_SOURCE_OPEN",
        },
        "route_reduction": {
            "retired_shortcuts": [
                "identify beta with tau_int without a neutral SPT-to-mass-cost theorem",
                "identify q79, q369, q7/qmod, or pi/6 directly with the nil drift because a numerical ratio is nearby",
                "reuse a CP/retarded circle character as the Majorana self-character",
            ],
            "lawful_exits": [
                "derive the selected neutral SPT measure and mass-cost transfer, thereby emitting beta",
                "derive the neutral overlap-bundle real structure and emit or exclude M_L/M_R",
                "derive a selected central-circle-to-nil-drift functor and then attach the one universal physical scale",
            ],
        },
        "what_closes_here": {
            "canonical_selected_tau_trial_executed": theorem_proved,
            "selected_circle_phase_trials_executed": theorem_proved,
            "CP_to_Majorana_character_shortcut_rejected": theorem_proved,
            "remaining_transfer_functor_typed": theorem_proved,
            "selected_spectral_action_slope_beta": False,
            "selected_neutral_real_structure": False,
            "Dirac_only_action_completeness": False,
            "selected_Majorana_seesaw_blocks": False,
            "physical_scale_selected": False,
        },
        "neutral_overlap_OK_gates_closed": predecessor["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": predecessor["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": predecessor["readiness_subfields_closed"],
        "readiness_subfields_total": predecessor["readiness_subfields_total"],
        "new_physical_value_fields_closed_here": 0,
        "accepted_route_exit_count": 0,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralSpectralActionSlopeOrSeesawSource_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "tau_int": tau_int,
        "canonical_spt_ratio": canonical_spt_ratio,
        "postcheck_ratio": postcheck,
        "circle_candidate_ratios": phase_rows,
        "closest_circle_candidate_residual": packet["circle_drift_route"]["closest_absolute_residual"],
        "CP_to_Majorana_character_shortcut_rejected": theorem_proved,
        "selected_beta_closed": False,
        "selected_neutral_real_structure_closed": False,
        "selected_seesaw_block_closed": False,
        "neutral_overlap_OK_gates_closed": packet["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": packet["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": packet["readiness_subfields_closed"],
        "readiness_subfields_total": packet["readiness_subfields_total"],
        "new_physical_value_fields_closed_here": 0,
        "accepted_route_exit_count": 0,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Spectral Action Slope or Seesaw Source v1

## Executed routes

The source-owned internal neutral orbit is already `[1,4,7]`. This successor
executes every presently sourced shape clue without promoting a postcheck.

The same-branch proper-time object has the exact internal value
`tau_int=log(448)/15={tau_int}`. The canonical point-support SPT trial gives

```text
r_SPT = 1/(exp(3 tau_int)+1) = {canonical_spt_ratio}
```

and therefore does not reproduce the downstream ratio `{postcheck}`. More
importantly, the corpus has not selected the SPT measure or proved that inverse
survival odds are the neutral mass-squared cost.

The three-basin circle trials give `{phase_rows}`. The closest is the selected
`q7/qmod` residue, with absolute residual
`{packet['circle_drift_route']['closest_absolute_residual']}`. This is a useful
clue, not an exact source theorem.

## Majorana guard

The retarded `q79/q369` labels are CP/circle characters. The strict ontology
packet explicitly forbids reusing them as the separately typed Majorana
self-character. A Majorana or seesaw completion still requires a selected real
structure on the neutral overlap bundle and emitted `M_L` or `M_R` rows.

## Exact frontier

The generic phrase "spectral action or seesaw" is now retired. The next object
must construct one of two typed morphisms:

1. a neutral circle/proper-time-to-mass-cost transfer that selects the SPT
   measure and emits the spectral slope; or
2. a neutral overlap-bundle real-structure functor that emits or excludes the
   Majorana blocks.

No physical neutral value row is accepted here. Next artifact: `{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
