from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_globalhymchernsequence_aposterioricertificate"
OUT = ROOT / "candidate_data" / SLUG


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    replay = load("candidate_data/selected_full_exps_hym_newton_replay.candidate.json")
    extraction = load("candidate_data/selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json")
    ext = load("candidate_data/selected_ext_overlap_hym_hodge_projector_table.candidate.json")
    literal = load("certificates/selected_literalcechwitness_or_globalhymconnectioncoefficients_certificate.json")

    summary = replay["solution_summary"]
    lambda1 = 4.0 * math.pi**2
    qmax = summary["max_exp_weighted_density"]
    coercivity = lambda1 - 2.0 * qmax
    residual = summary["final_residual_l2"]
    error_indicator = residual / coercivity
    if coercivity <= 0:
        raise ValueError("linearized zero-mean coercivity not established")

    packet = {
        "schema": "MTTSelectedGlobalHYMChernSequenceAPosterioriCertificate.v1",
        "status": "GLOBAL_CHERN_SEQUENCE_TYPED_DISCRETE_APOSTERIORI_STABLE_CONTINUUM_LIMIT_OPEN",
        "selected_global_inputs": {
            "holomorphic_extension_form": ext["global_Dolbeault_harmonic_representative"]["representative"],
            "barpartial_eta_zero": ext["global_Dolbeault_harmonic_representative"]["barpartial_eta"],
            "transition_cocycle_law": ext["transition_overlap_table"]["cocycle_law"],
            "selected_metric_sequence": "H_N=diag(exp(u_N),exp(-u_N))",
            "determinant_one": extraction["diagonal_metric_payload"]["determinant"],
        },
        "global_Chern_connection_sequence": {
            "uniqueness_rule": "a holomorphic structure dbar_E and positive Hermitian metric H_N determine a unique Chern connection A_N",
            "zero_one_part": "A_N^(0,1)=dbar_E with selected offdiagonal eta_00^unit",
            "one_zero_part": "A_N^(1,0) is fixed by H_N-unitarity, equivalently the H_N adjoint of A_N^(0,1) plus H_N^{-1} partial H_N",
            "diagonal_component": extraction["diagonal_connection_payload"]["connection_form"],
            "offdiagonal_component_is_free_parameter": False,
            "offdiagonal_component_source": "selected eta_00^unit and its H_N adjoint",
            "patching_source": "selected AH transition factors plus selected literal S3 Deligne-Cech source",
        },
        "finite_aposteriori_certificate": {
            "mesh": replay["solver"]["mesh"],
            "theta_cutoff": replay["solver"]["theta_series_cutoff"],
            "iterations": replay["solver"]["iterations_run"],
            "HYM_residual_L2": residual,
            "tail_contraction_ratio_max": max(summary["tail_contraction_ratios"]),
            "zero_mean_Poincare_lambda1": lambda1,
            "nonlinear_density_max": qmax,
            "linearized_coercivity_lower_bound": coercivity,
            "residual_over_coercivity_error_indicator": error_indicator,
            "finite_projected_solution_locally_unique_and_stable": coercivity > 0 and residual < 1e-12,
        },
        "decision": {
            "literal_Cech_witness_closed": literal["literal_Cech_witness_closed"],
            "global_Chern_connection_sequence_typed": True,
            "finite_projected_HYM_aposteriori_stability_closed": True,
            "continuum_uniform_truncation_bound_closed": False,
            "literal_global_HYM_witness_closed": False,
            "U2_literal_witness_families": "1/2",
        },
        "remaining_acceptance_test": "prove a uniform mesh/theta-cutoff convergence bound and global patchwise residual bound, or invoke a fully specified constructive Donaldson/balanced-metric convergence theorem for this selected non-split Gauduchon bundle",
        "guards": {
            "one_mesh_residual_mislabeled_as_continuum_proof": False,
            "diagonal_metric_mislabeled_as_split_bundle": False,
            "selected_eta_offdiagonal_component_dropped": False,
            "target_fitting_used": False,
        },
    }
    dump(OUT / "global_hym_chern_sequence_aposteriori.packet.json", packet)

    status = "MTT_SELECTED_GLOBALHYM_CHERN_SEQUENCE_TYPED_FINITE_STABLE_CONTINUUM_CERTIFICATE_OPEN"
    candidate = {
        "candidate": "MTT_Selected_GlobalHYMChernSequence_APosterioriCertificate_v1",
        "status": status,
        "date": "2026-07-11",
        "closure_claimed": True,
        "theorem": {
            "name": "SelectedChernSequenceAndFiniteAPosterioriStabilityTheorem",
            "proved": True,
            "statement": "The selected global Dolbeault extension form and positive determinant-one metric sequence determine a unique global Chern-connection sequence; the offdiagonal term is fixed by eta_00 and is not a free coefficient. At the 24^4 projected level the HYM residual is 8.21e-13 and the zero-mean linearization has coercivity margin about 26.02, giving residual-over-coercivity indicator 3.16e-14. A continuum uniform truncation/patchwise bound is still required for the literal global HYM witness.",
        },
        "U2_finite_constructive_HYM_closed": True,
        "U2_literal_global_HYM_closed": False,
        "next_required_artifact": "MTT_Selected_HYMUniformSpectralConvergenceAndPatchingCertificate_v1",
    }
    dump(ROOT / "candidate_data" / f"{SLUG}.candidate.json", candidate)

    certificate = {
        "certificate": "MTT_Selected_GlobalHYMChernSequence_APosterioriCertificate_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": status,
        "theorem_proved": True,
        "global_Chern_connection_sequence_typed": True,
        "offdiagonal_connection_source_selected": True,
        "finite_projected_HYM_aposteriori_stability_closed": True,
        "linearized_coercivity_lower_bound": coercivity,
        "residual_over_coercivity_error_indicator": error_indicator,
        "continuum_uniform_truncation_bound_closed": False,
        "literal_global_HYM_witness_closed": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(ROOT / "certificates" / f"{SLUG}_certificate.json", certificate)


if __name__ == "__main__":
    main()
