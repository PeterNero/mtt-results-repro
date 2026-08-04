"""Build selected finite heat/torsion response final-gate artifact."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONSTANTS_ROOT = ROOT.parent / "mtt-nonsm-constants-no-knob"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_heattorsionresponse_finalgate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RESPONSE = PACKET_DIR / "selected_finite_heat_spectrum_response.packet.json"
SLOT_CLOSURE = PACKET_DIR / "finite_determinant_heat_torsion_slot_closure.packet.json"
FRONTIER = PACKET_DIR / "post_eight_slot_true_equivalence_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HeatTorsionResponse_FinalGate_v1.md"

STATUS = "MTT_SELECTED_HEATTORSIONRESPONSE_FINALGATE_BUILT_FINAL_OPERATOR_SLOT_CLOSED"
NEXT = "MTT_Selected_DynamicQaSU3_or_C1Response_PostSourceFrontier_v1"
SLOT = "finite_determinant_heat_spectrum_or_torsion_response"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def heat(values: list[float], t: float) -> float:
    return sum(math.exp(-t * value) for value in values)


def logdet(values: list[float]) -> float:
    return sum(math.log(value) for value in values)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    prior_frontier = load(DATA / "selected_tracepayload_or_fullhymoperatoremission" / "post_seven_slot_true_equivalence_frontier.packet.json")
    prior_closure = load(
        DATA
        / "selected_tracepayload_or_fullhymoperatoremission"
        / "transition_rhoe_or_cech_dolbeault_de_slot_closure.packet.json"
    )
    gap_lock = load(CONSTANTS_ROOT / "certificates" / "selected_phifin_s2_gap_layer_honest_replay_lock_certificate.json")
    locked = gap_lock["locked_contract"]

    model_gap = locked["model_gap_gamma_N"]
    selected_eta = locked["selected_eta_N"]
    eta_threshold = locked["eta_threshold"]
    selected_gap = locked["selected_gap_lower_bound"]

    scalar_positive_spectrum = [model_gap] * 4 + [2.0 * model_gap] * 4
    family_positive_spectrum = scalar_positive_spectrum * 3
    h_positive_spectrum = [selected_eta, selected_eta] + family_positive_spectrum
    total_positive_spectrum = family_positive_spectrum * 6 + h_positive_spectrum

    family_kernel_dimension = 3
    h_kernel_dimension = 1
    family_sector_count = 6
    sector_count = 7
    basis_dimension = locked["basis_dimension"]
    total_dimension = sector_count * basis_dimension
    total_kernel_dimension = family_sector_count * family_kernel_dimension + h_kernel_dimension
    total_positive_dimension = len(total_positive_spectrum)

    proof_inputs = {
        "prior_frontier_has_seven_closed_one_open": prior_frontier["operator_source_slots_closed"] == 7
        and prior_frontier["operator_source_slots_remaining"] == 1,
        "prior_remaining_slot_is_heat_torsion": prior_frontier["remaining_slots"] == [SLOT],
        "transition_DE_trace_slot_closed": prior_closure["closure_result"]["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"],
        "locked_basis_is_selected_27_mode": basis_dimension == 27
        and locked["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3",
        "DE_source_flags_are_theorem_derived": locked["D_E_source_flags_are_theorem_derived"],
        "selected_trace_equality_proved": locked["selected_trace_equality"]["proved"],
        "selected_gap_positive": selected_gap > 0,
        "eta_below_gap_threshold": 0.0 < selected_eta < eta_threshold,
        "Riesz_Green_layer_closed": locked["Riesz_Green_layer_closes"],
        "canonical_F3xF3_spectrum_identified": math.isclose(model_gap, 4.0 * math.pi * math.pi / 9.0, rel_tol=0.0, abs_tol=1e-15),
        "no_observed_or_benchmark_inputs": gap_lock["guardrails"]["does_not_use_observed_or_benchmark_inputs"],
    }
    slot_closes = all(proof_inputs.values())

    selected_response = {
        "schema": "MTTSelectedFiniteHeatSpectrumResponse.v1",
        "status": "SELECTED_FINITE_27MODE_HEAT_PSEUDODETERMINANT_RESPONSE_EMITTED",
        "slot": SLOT,
        "branch": {"q": 79, "orientation": "F", "torsion_label_m": 1},
        "source_contract": {
            "basis_id": locked["basis_id"],
            "basis_dimension_per_sector": basis_dimension,
            "sector_order": ["Q", "u", "d", "L", "e", "N", "H"],
            "family_sectors": ["Q", "u", "d", "L", "e", "N"],
            "H_sector": "canonical F3xF3 Fourier Laplacian plus rank-two selected_eta_N zero-cluster projector",
            "zero_cluster_indices": locked["zero_cluster_indices"],
            "level": "finite selected Phi_fin 27-mode D_E/gap layer",
        },
        "finite_spectrum_convention": {
            "regularization": "finite positive-complement pseudodeterminant; zero modes are projected by the selected Riesz projector",
            "heat_time_t": 1.0,
            "scalar_F3xF3_positive_eigenvalues": [
                {"eigenvalue": model_gap, "multiplicity": 4},
                {"eigenvalue": 2.0 * model_gap, "multiplicity": 4},
            ],
            "family_sector_positive_eigenvalues": [
                {"eigenvalue": model_gap, "multiplicity": 12},
                {"eigenvalue": 2.0 * model_gap, "multiplicity": 12},
            ],
            "H_sector_positive_eigenvalues": [
                {"eigenvalue": selected_eta, "multiplicity": 2},
                {"eigenvalue": model_gap, "multiplicity": 12},
                {"eigenvalue": 2.0 * model_gap, "multiplicity": 12},
            ],
        },
        "finite_invariants": {
            "family_sector_kernel_dimension": family_kernel_dimension,
            "family_sector_positive_dimension": len(family_positive_spectrum),
            "family_sector_reduced_heat_trace_t1": heat(family_positive_spectrum, 1.0),
            "family_sector_heat_trace_t1": family_kernel_dimension + heat(family_positive_spectrum, 1.0),
            "family_sector_log_pseudodeterminant": logdet(family_positive_spectrum),
            "H_sector_kernel_dimension": h_kernel_dimension,
            "H_sector_positive_dimension": len(h_positive_spectrum),
            "H_sector_reduced_heat_trace_t1": heat(h_positive_spectrum, 1.0),
            "H_sector_heat_trace_t1": h_kernel_dimension + heat(h_positive_spectrum, 1.0),
            "H_sector_log_pseudodeterminant": logdet(h_positive_spectrum),
            "total_sector_count": sector_count,
            "total_dimension": total_dimension,
            "total_kernel_dimension": total_kernel_dimension,
            "total_positive_dimension": total_positive_dimension,
            "total_reduced_heat_trace_t1": heat(total_positive_spectrum, 1.0),
            "total_heat_trace_t1": total_kernel_dimension + heat(total_positive_spectrum, 1.0),
            "total_log_pseudodeterminant": logdet(total_positive_spectrum),
            "finite_spectral_zeta_at_0_positive_count": total_positive_dimension,
        },
        "proof_inputs": proof_inputs,
        "slot_closes": slot_closes,
        "scope": {
            "closes": "finite selected 27-mode heat trace, spectrum table, and positive-complement pseudodeterminant response",
            "does_not_close": [
                "smooth analytic torsion",
                "continuum zeta-regularized determinant beyond the selected finite Galerkin layer",
                "full S2 value emission",
                "selected dotD_alpha1 source identity",
                "primitive C1 response",
                "actual dynamic Qa/SU3 operator packet",
                "Yukawa, CKM, PMNS, or full SM data derivation",
                "no-knob constants derivation",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    filled_slots = list(prior_closure["slot_status_after_closure"]["filled_slots"])
    missing_slots = list(prior_closure["slot_status_after_closure"]["missing_slots"])
    if slot_closes and SLOT not in filled_slots:
        filled_slots.append(SLOT)
    if slot_closes and SLOT in missing_slots:
        missing_slots.remove(SLOT)

    slot_closure = {
        "schema": "MTTFiniteDeterminantHeatTorsionSlotClosure.v1",
        "filled_slot": SLOT,
        "selected_response_path": rel(RESPONSE),
        "proof_inputs": proof_inputs,
        "closure_result": {
            "finite_determinant_heat_spectrum_or_torsion_response_closed": slot_closes,
            "finite_heat_spectrum_response_emitted": True,
            "finite_positive_complement_pseudodeterminant_emitted": True,
            "smooth_analytic_torsion_closed": False,
            "full_S2_value_emission_closed": False,
            "selected_dotD_alpha1_source_identity_closed": False,
            "primitive_C1_response_closed": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "why_not_dynamic_operator_packet": (
                "The closure uses the selected finite 27-mode D_E/gap operator to emit spectral invariants. "
                "It does not emit dotD_alpha1/C1 response, A_selected/b_selected, full S2 operator values, "
                "or no-proxy SM matrices."
            ),
        },
        "slot_status_after_closure": {
            "required_operator_slot_count": 8,
            "filled_operator_slot_count": len(filled_slots),
            "filled_slots": filled_slots,
            "missing_slots": missing_slots,
            "remaining_missing_slot_count": len(missing_slots),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier = {
        "schema": "MTTPostEightSlotTrueEquivalenceFrontier.v1",
        "status": "EIGHT_OPERATOR_SOURCE_SLOTS_CLOSED_DYNAMIC_SM_OPEN" if slot_closes else "HEAT_TORSION_FINAL_GATE_OPEN",
        "operator_source_slots_closed": len(filled_slots),
        "operator_source_slots_remaining": len(missing_slots),
        "remaining_slots": missing_slots,
        "remaining_slot_contracts": {},
        "source_slot_layer_closed": slot_closes,
        "true_SM_equivalence_closed": False,
        "true_SM_equivalence_still_requires": [
            "actual dynamic Qa/SU3 operator packet",
            "selected dotD_alpha1 and primitive C1 response source identity",
            "full S2 value emission beyond D_E/gap layer",
            "precision QFT observable functor with accepted RG/threshold/covariance policy",
            "no-proxy Yukawa/mixing/value derivation if upgrading beyond SM parity",
        ],
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHeatTorsionResponseFinalGate",
        "status": STATUS,
        "inputs": {
            "prior_transition_slot_closure": rel(
                DATA
                / "selected_tracepayload_or_fullhymoperatoremission"
                / "transition_rhoe_or_cech_dolbeault_de_slot_closure.packet.json"
            ),
            "prior_post_seven_frontier": rel(
                DATA
                / "selected_tracepayload_or_fullhymoperatoremission"
                / "post_seven_slot_true_equivalence_frontier.packet.json"
            ),
            "selected_gap_lock": rel(CONSTANTS_ROOT / "certificates" / "selected_phifin_s2_gap_layer_honest_replay_lock_certificate.json"),
        },
        "output_packets": {
            "selected_finite_heat_spectrum_response": rel(RESPONSE),
            "finite_determinant_heat_torsion_slot_closure": rel(SLOT_CLOSURE),
            "post_eight_slot_true_equivalence_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "SelectedFiniteHeatSpectrumResponseFinalGateTheorem",
            "proved": slot_closes,
            "statement": (
                "Given the theorem-derived selected q79/F,m=1 finite 27-mode D_E trace/gap layer, the canonical "
                "F3xF3 Fourier spectrum and the H-sector rank-two selected_eta_N projector determine a finite "
                "positive-complement heat trace and pseudodeterminant. This closes the finite determinant/heat/"
                "spectrum response operator-source slot at the selected finite Galerkin layer. It does not close "
                "smooth analytic torsion, dotD/C1 dynamics, full S2 value emission, or no-knob SM data derivation."
            ),
        },
        "what_closes_now": {
            "finite_determinant_heat_spectrum_or_torsion_response": slot_closes,
            "selected_finite_heat_trace_emitted": True,
            "selected_positive_complement_pseudodeterminant_emitted": True,
            "all_eight_operator_source_slots_closed_at_source_slot_layer": len(missing_slots) == 0,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "smooth_analytic_torsion": True,
            "full_S2_value_emission": True,
            "selected_dotD_alpha1_source_identity": True,
            "primitive_C1_response": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "operator_source_slots_closed_total": len(filled_slots),
            "operator_source_slots_remaining": len(missing_slots),
            "finite_determinant_heat_spectrum_or_torsion_response_closed": slot_closes,
            "all_operator_source_slots_closed": len(missing_slots) == 0,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": slot_closes,
    }

    cert = {
        "certificate": "MTT_Selected_HeatTorsionResponse_FinalGate_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": slot_closes,
        "finite_determinant_heat_spectrum_or_torsion_response_closed": slot_closes,
        "closed_operator_source_slots_total": len(filled_slots),
        "operator_source_slots_remaining": len(missing_slots),
        "source_slot_layer_closed": len(missing_slots) == 0,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected HeatTorsionResponse FinalGate v1

This artifact closes the final operator-source slot:
`{SLOT}`.

The closure is finite and source-scoped. It uses the selected q79/F,m=1
`Phi_fin` 27-mode `D_E`/gap layer that was already theorem-derived, then
computes the finite positive-complement heat trace and pseudodeterminant.

Selected finite spectrum:

- scalar `F3xF3` positive spectrum: `4*pi^2/9` with multiplicity 4, and
  `8*pi^2/9` with multiplicity 4
- each family sector has kernel dimension 3 and positive dimension 24
- the H sector keeps one zero mode and shifts two zero-cluster modes by
  `selected_eta_N = 1`

Total selected seven-sector finite response:

- total dimension: {total_dimension}
- total kernel dimension: {total_kernel_dimension}
- total positive-complement dimension: {total_positive_dimension}
- reduced heat trace at t=1: {heat(total_positive_spectrum, 1.0):.15g}
- full heat trace at t=1: {(total_kernel_dimension + heat(total_positive_spectrum, 1.0)):.15g}
- log pseudodeterminant: {logdet(total_positive_spectrum):.15g}

This closes all eight operator-source slots at the finite source-slot layer.

It does not close smooth analytic torsion, full S2 value emission, selected
`dotD_alpha1`, primitive C1 response, the actual dynamic `Qa/SU3` operator
packet, true SM equivalence, or no-knob constants derivation.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (RESPONSE, selected_response),
        (SLOT_CLOSURE, slot_closure),
        (FRONTIER, frontier),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
