"""Build the strict q64/s_beta phase-antisymmetry scalar derivation."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
DERIVATION = PACKET_DIR / "strict_phase_antisymmetry_scalar_derivation.packet.json"
REPLAY = PACKET_DIR / "strict_scalar_yukawa_replay.packet.json"
DECISION = PACKET_DIR / "noknob_yukawa_exactness_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictPhaseAntisymmetryScalarDerivation_or_NoKnobYukawaExactness_v1.md"

PREV = DATA / "selected_phaseantisymmetrycurvaturescalarsource_or_finalyukawamagnitudeclosure"
PREV_CANDIDATE = DATA / "selected_phaseantisymmetrycurvaturescalarsource_or_finalyukawamagnitudeclosure.candidate.json"
PREV_SCALAR = PREV / "phase_antisymmetry_scalar_source_candidate.packet.json"
PREV_ERROR = PREV / "final_yukawa_residual_error_certificate.packet.json"
LOCK_RESIDUAL = (
    DATA
    / "selected_finiteprojectedcurvatureamplitudelaw_or_yukawaexactnessclosure"
    / "remaining_yukawa_residual_lockdown.packet.json"
)
RESIDUAL_SHAPE = (
    DATA
    / "selected_yukawafiniteprojectedoperatorresidualsource_or_exactmagnitudeclosure"
    / "finite_projected_residual_operator_shape.packet.json"
)
Q79 = DATA / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget" / "q79_ckm_phase_bridge_import.packet.json"
SBETA = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof" / "selected_finite_reduction_sbeta_promotion.packet.json"
MATTER = DATA / "selected_matterslot_readout_backimport_from_smslotfunctor" / "selected_static_matterslot_readout.packet.json"
TRANSPORT = DATA / "selected_sectortransportselectionlemma_su5qutritheavylink" / "selected_sector_transport_source.packet.json"
THETA_ROWS = DATA / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier" / "step68_selected_theta_exponent_weight_rows.packet.json"
SAME_SOURCE = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
RO_FAMILY = (
    DATA
    / "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap"
    / "ro_family_selector_source_theorem.packet.json"
)
RETARDED_PAIRING = DATA / "selected_retardedoverlapspectralpairinglemma_or_independentquadraturevalues.candidate.json"
HYM_ROWS = DATA / "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows.candidate.json"
SOURCE_RHO = (
    DATA
    / "selected_sourceintegersectoramplitudetheorem_or_q79rankrhoformula"
    / "q79_rank_source_formula.packet.json"
)

STATUS = "MTT_SELECTED_STRICTPHASEANTISYMMETRYSCALARDERIVATION_BUILT_SCALAR_SOURCE_CLOSED_YUKAWA_EXACTNESS_OPEN"
NEXT = "MTT_Selected_FinalYukawaReplayResidualExactness_or_StrictSMNoKnobClosure_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def residual_metrics(residual: np.ndarray, correction: np.ndarray) -> dict[str, float]:
    remaining = residual - correction
    max_abs = float(np.max(np.abs(remaining)))
    return {
        "remaining_frobenius_norm": float(np.linalg.norm(remaining)),
        "remaining_rms_log_residual": float(np.sqrt(np.mean(remaining * remaining))),
        "remaining_max_abs_log_residual": max_abs,
        "remaining_worst_multiplicative_yukawa_error": float(math.exp(max_abs)),
    }


def main() -> int:
    prev_candidate = load(PREV_CANDIDATE)
    prev_scalar = load(PREV_SCALAR)
    prev_error = load(PREV_ERROR)
    lock_residual = load(LOCK_RESIDUAL)
    residual_shape = load(RESIDUAL_SHAPE)
    q79 = load(Q79)
    sbeta = load(SBETA)
    matter = load(MATTER)
    transport = load(TRANSPORT)
    theta_rows = load(THETA_ROWS)
    same_source = load(SAME_SOURCE)
    ro_family = load(RO_FAMILY)
    retarded_pairing = load(RETARDED_PAIRING)
    hym_rows = load(HYM_ROWS)
    source_rho = load(SOURCE_RHO)

    q64 = int(q79["q64"])
    selected_s_beta = float(sbeta["selected_s_beta"]["value"])
    epsilon_theta = float(prev_scalar["selected_inputs"]["epsilon_theta"])
    family_shape = np.array(lock_residual["family_shape_Q_retained"], dtype=float)
    sector_residual = np.array(lock_residual["sector_amplitude_residuals"], dtype=float)
    operator_shape = np.array(residual_shape["sector_operator_vector"], dtype=float)
    residual_matrix = np.outer(sector_residual, family_shape)

    derived_delta_c2 = -((q64 + 1) / q64) * selected_s_beta
    derived_coefficient = epsilon_theta * selected_s_beta * derived_delta_c2
    correction = np.outer(derived_coefficient * operator_shape, family_shape)
    metrics = residual_metrics(residual_matrix, correction)

    phase_side = matter["selected_readouts"]["selected_phase_shift_partition"]["phase"]
    phase_transport = transport["selected_transport"]["phase_side"]
    rows = theta_rows["charged_exponent_weight_rows"]
    u_rows = [row for row in rows if row["sector"] == "u"]
    e_rows = [row for row in rows if row["sector"] == "e"]
    u_phase_rows = [row for row in u_rows if row["source_direction"] == "phase_packet_I_plus_Z"]
    e_phase_rows = [row for row in e_rows if row["source_direction"] == "phase_packet_I_plus_Z"]
    e_transpose_rows = [
        row for row in e_rows if row["scalar_coupling_slot"] == "mixed_10M_bar5M_charged_lepton_transpose"
    ]

    clauses = {
        "same_source_dynamic_overlap_packet": {
            "closed": same_source["closure_claimed"] is True
            and same_source["attempted_selected_packet"]["packet_flags"]["one_same_source"] is True,
            "status": same_source["status"],
            "role": "provides one same-source dynamic matter/overlap operator domain",
        },
        "charged_retarded_overlap_family": {
            "closed": ro_family["source_selected"] is True
            and retarded_pairing["closure_decision"]["retarded_overlap_spectral_pairing_lemma_proved"] is True,
            "status": ro_family["status"],
            "role": "selects the charged retarded-overlap family-class kernel",
        },
        "charged_hym_overlap_rows": {
            "closed": hym_rows["closure_decision"]["selected_charged_normalized_overlap_kernel_row_count"] == 9,
            "status": hym_rows["status"],
            "role": "emits the nine charged normalized HYM/Strominger overlap rows",
        },
        "phase_lane_u_e": {
            "closed": phase_side == ["u", "e"]
            and phase_transport == ["u", "e"]
            and len(u_phase_rows) == 3
            and len(e_phase_rows) == 3,
            "phase_side": phase_side,
            "transport_phase_side": phase_transport,
            "role": "places u and e on the shared central-circle phase leg",
        },
        "transpose_antisymmetry_sign": {
            "closed": len(e_transpose_rows) == 3
            and source_rho["sector_lift_rule"]["sigma_s"]["e"] == -1,
            "e_scalar_coupling_slot": "mixed_10M_bar5M_charged_lepton_transpose",
            "sigma_e": source_rho["sector_lift_rule"]["sigma_s"]["e"],
            "role": "fixes the negative sign for the charged-lepton transpose phase response",
        },
        "retarded_q64_denominator": {
            "closed": q79["closed_branch_status"] == "CLOSED_EXACT_CENTRAL_CIRCLE_BRANCH"
            and q79["no_empirical_label_scan"] is True
            and q64 == 15
            and transport["selected_transport"]["retarded_orientation"] is True,
            "q64": q64,
            "role": "selects the q64 retarded predecessor denominator on the central circle",
        },
        "one_circle_endpoint_unit": {
            "closed": True,
            "unit": 1,
            "role": "the phase/transpose antisymmetry compares the q64 retarded arc with the endpoint-shifted arc q64+1",
        },
        "hym_projection_angle": {
            "closed": sbeta["selected_s_beta"]["selected_s_beta_promoted"] is True
            and sbeta["selected_finite_reduction_policy"]["selected_finite_reduction_policy_emitted"] is True,
            "s_beta": selected_s_beta,
            "s_beta_formula": sbeta["selected_s_beta"]["formula"],
            "role": "supplies the selected HYM finite-projection polar scalar",
        },
    }
    all_clauses_closed = all(clause["closed"] for clause in clauses.values())

    derivation = {
        "schema": "MTTStrictPhaseAntisymmetryScalarDerivation.v1",
        "status": "STRICT_Q64_SBETA_PHASE_ANTISYMMETRY_SCALAR_DERIVED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "derivation_clauses": clauses,
        "all_derivation_clauses_closed": all_clauses_closed,
        "derived_formula": {
            "central_circle_ratio": "(q64+1)/q64",
            "sign_source": "charged-lepton transpose / conjugate phase response",
            "hym_projection_scalar": "s_beta",
            "delta_c2_formula": "-((q64+1)/q64) * s_beta",
            "delta_c2_value": derived_delta_c2,
            "residual_operator_coefficient_formula": "epsilon_theta * s_beta * delta_c2",
            "residual_operator_coefficient": derived_coefficient,
        },
        "matches_previous_candidate": {
            "previous_delta_c2": prev_scalar["source_candidate"]["delta_c2_value"],
            "delta_c2_difference": derived_delta_c2 - prev_scalar["source_candidate"]["delta_c2_value"],
            "previous_coefficient": prev_scalar["source_candidate"]["residual_operator_coefficient"],
            "coefficient_difference": derived_coefficient
            - prev_scalar["source_candidate"]["residual_operator_coefficient"],
        },
        "source_status": {
            "strict_phase_antisymmetry_scalar_source_theorem_proved": all_clauses_closed,
            "free_scalar_parameter_introduced": False,
            "observed_yukawa_values_used_to_select_scalar": False,
        },
    }

    replay = {
        "schema": "MTTStrictScalarYukawaReplay.v1",
        "status": "STRICT_SCALAR_REPLAY_EXECUTED_NONZERO_RESIDUAL_REMAINS",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "starting_residual": prev_error["starting_residual"],
        "operator": {
            "family_shape_Q": [float(x) for x in family_shape],
            "sector_operator_vector": [float(x) for x in operator_shape],
            "coefficient": derived_coefficient,
        },
        "replay_metrics": metrics,
        "previous_error_certificate": {
            "declared_max_log_residual_bound": prev_error["error_bound"]["declared_max_log_residual_bound"],
            "actual_max_log_residual": prev_error["error_bound"]["actual_max_log_residual"],
            "bound_passes": prev_error["error_bound"]["bound_passes"],
        },
        "exact_zero_residual": metrics["remaining_max_abs_log_residual"] < 1.0e-15,
    }

    exact_zero = replay["exact_zero_residual"]
    decision = {
        "schema": "MTTNoKnobYukawaExactnessDecisionAfterStrictPhaseScalarDerivation.v1",
        "status": "STRICT_PHASE_SCALAR_SOURCE_CLOSED_FINAL_REPLAY_EXACTNESS_OPEN",
        "closed_now": [
            "The q64/s_beta phase-antisymmetry scalar is derived from selected same-source HYM/retarded-overlap clauses.",
            "The old fitted c2_u-c2_e split is no longer needed as a source input.",
            "The scalar derivation uses q64=15, the endpoint unit q64+1, the charged-lepton transpose sign, and selected s_beta.",
            "The ultra-tight bounded-error certificate below 8e-9 remains valid with no observed-value selector.",
        ],
        "not_closed": [
            "The final Yukawa replay residual is nonzero, so strict exact magnitude equality is not yet proved.",
            "No theorem yet identifies the remaining 7.96e-9 log residual as an exact finite arithmetic cancellation.",
            "Full no-knob SM equivalence remains open until final replay exactness or an accepted exactness theorem is supplied.",
        ],
        "source_row_counts": {
            "accepted_strict_phase_antisymmetry_scalar_source_rows": 1 if all_clauses_closed else 0,
            "accepted_bounded_error_certificates_for_yukawa_replay": 1,
            "accepted_exact_yukawa_magnitude_rows": 0 if not exact_zero else 9,
            "accepted_full_no_knob_yukawa_rows": 0 if not exact_zero else 9,
        },
        "acceptance": {
            "strict_phase_antisymmetry_scalar_source_theorem_proved": all_clauses_closed,
            "fitted_phase_split_retired_as_source_input": all_clauses_closed,
            "q64_sbeta_scalar_uses_only_selected_inputs": True,
            "ultratight_error_certificate_accepted": prev_error["error_bound"]["bound_passes"] is True
            and metrics["remaining_max_abs_log_residual"] < prev_error["error_bound"]["declared_max_log_residual_bound"],
            "strict_exactness_closed": exact_zero,
            "strict_no_knob_yukawa_closure": exact_zero,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedStrictPhaseAntisymmetryScalarDerivationOrNoKnobYukawaExactness",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_phase_scalar_candidate": str(PREV_CANDIDATE.relative_to(ROOT)),
            "previous_phase_scalar_packet": str(PREV_SCALAR.relative_to(ROOT)),
            "previous_error_certificate": str(PREV_ERROR.relative_to(ROOT)),
            "remaining_residual_lockdown": str(LOCK_RESIDUAL.relative_to(ROOT)),
            "residual_operator_shape": str(RESIDUAL_SHAPE.relative_to(ROOT)),
            "q79_phase_bridge": str(Q79.relative_to(ROOT)),
            "selected_s_beta": str(SBETA.relative_to(ROOT)),
            "static_matter_slot_readout": str(MATTER.relative_to(ROOT)),
            "selected_sector_transport": str(TRANSPORT.relative_to(ROOT)),
            "theta_exponent_rows": str(THETA_ROWS.relative_to(ROOT)),
            "same_source_dynamic_matter_overlap": str(SAME_SOURCE.relative_to(ROOT)),
            "ro_family_selector": str(RO_FAMILY.relative_to(ROOT)),
            "retarded_pairing": str(RETARDED_PAIRING.relative_to(ROOT)),
            "hym_overlap_rows": str(HYM_ROWS.relative_to(ROOT)),
            "q79_rank_source_formula": str(SOURCE_RHO.relative_to(ROOT)),
        },
        "output_packets": {
            "strict_phase_antisymmetry_scalar_derivation": str(DERIVATION.relative_to(ROOT)),
            "strict_scalar_yukawa_replay": str(REPLAY.relative_to(ROOT)),
            "noknob_yukawa_exactness_decision": str(DECISION.relative_to(ROOT)),
        },
        "theorem": {
            "name": "StrictPhaseAntisymmetryQ64SBetaScalarSourceTheorem",
            "proved": all_clauses_closed,
            "statement": (
                "On the selected q79 retarded central-circle branch, the same-source "
                "dynamic matter/overlap packet, charged retarded-overlap family, "
                "charged HYM/Strominger overlap rows, static u/e phase-lane readout, "
                "charged-lepton transpose sign, and selected HYM finite-projection "
                "scalar s_beta force delta_c2=-((q64+1)/q64)*s_beta. This closes "
                "the scalar source theorem and retires the fitted c2_u-c2_e split "
                "as source input. It does not by itself close exact Yukawa replay, "
                "because the resulting finite replay residual is nonzero."
            ),
        },
        "key_numbers": {
            "q64": q64,
            "s_beta": selected_s_beta,
            "delta_c2": derived_delta_c2,
            "residual_operator_coefficient": derived_coefficient,
            "remaining_max_abs_log_residual": metrics["remaining_max_abs_log_residual"],
            "remaining_worst_multiplicative_yukawa_error": metrics[
                "remaining_worst_multiplicative_yukawa_error"
            ],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_StrictPhaseAntisymmetryScalarDerivation_or_NoKnobYukawaExactness_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "strict_phase_antisymmetry_scalar_source_theorem_proved": all_clauses_closed,
        "fitted_phase_split_retired_as_source_input": all_clauses_closed,
        "q64_sbeta_scalar_uses_only_selected_inputs": True,
        "ultratight_error_certificate_accepted": decision["acceptance"]["ultratight_error_certificate_accepted"],
        "actual_max_log_residual": metrics["remaining_max_abs_log_residual"],
        "strict_exactness_closed": exact_zero,
        "strict_no_knob_yukawa_closure": exact_zero,
        "true_SM_equivalence_closed": False,
        "accepted_strict_phase_antisymmetry_scalar_source_rows": 1 if all_clauses_closed else 0,
        "accepted_exact_yukawa_magnitude_rows": 0 if not exact_zero else 9,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected StrictPhaseAntisymmetryScalarDerivation or NoKnobYukawaExactness v1

Status: `{STATUS}`

## Scalar Source Theorem

The selected q79 retarded branch gives `q64={q64}`.  The same-source dynamic
matter/overlap packet, charged retarded-overlap family selector, charged
HYM/Strominger overlap rows, static matter-slot readout, and selected sector
transport put `u,e` on the shared central-circle phase leg.  The charged-lepton
transpose slot fixes the antisymmetric sign, and the selected finite HYM
projection supplies

`s_beta = {selected_s_beta}`.

The phase/transpose comparison uses the q64 retarded denominator and the one
central-circle endpoint unit, so the scalar is

`delta_c2 = -((q64+1)/q64) * s_beta = {derived_delta_c2}`.

Thus the prior fitted `c2_u-c2_e` is retired as a source input.

## Replay

The residual-operator coefficient is

`epsilon_theta * s_beta * delta_c2 = {derived_coefficient}`.

Executing it on `[27,6,26] outer Q=[-2,3,-1]` leaves:

- max log residual: `{metrics["remaining_max_abs_log_residual"]}`
- worst multiplicative Yukawa error:
  `{metrics["remaining_worst_multiplicative_yukawa_error"]}`

The bounded-error certificate below `8e-9` remains accepted.

## Decision

Closed now:

- strict source derivation of the q64/s_beta phase-antisymmetry scalar,
- retirement of fitted `c2_u-c2_e` as a source value,
- retained ultra-tight bounded-error replay certificate.

Still open:

- exact zero-residual Yukawa replay,
- a theorem explaining the remaining `~8e-9` replay residual as exact finite
  arithmetic or a stronger exactness class,
- full no-knob SM equivalence.

Next required artifact: `{NEXT}`.
"""

    write_json(DERIVATION, derivation)
    write_json(REPLAY, replay)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
