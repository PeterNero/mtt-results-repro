from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from mtt_qm_source import build as qm  # noqa: E402


Step = tuple[str, str, Callable[[], dict]]


STEPS: tuple[Step, ...] = (
    ("source_freshness", "source_freshness.certificate.json", qm.source_freshness),
    ("free_dirac_net", "framed_q79_free_dirac_car_net.certificate.json", qm.framed_q79_free_dirac_car_net),
    ("classical_bv", "q79_continuum_sm_classical_bv_composition.certificate.json", qm.q79_continuum_sm_classical_bv_composition),
    ("hyperbolic_bv", "q79_sm_gaugefixed_hyperbolic_bv_equicausal.certificate.json", qm.q79_sm_gaugefixed_hyperbolic_bv_equicausal),
    ("renormalized_qme", "q79_sm_renormalized_timeordering_local_qme.certificate.json", qm.q79_sm_renormalized_timeordering_local_qme),
    ("formal_state", "q79_sm_local_formal_physical_state.certificate.json", qm.q79_sm_local_formal_physical_state),
    ("state_gluing", "q79_sm_local_formal_state_space_gluing.certificate.json", qm.q79_sm_local_formal_state_space_gluing),
    ("state_transport", "q79_sm_equicausal_formal_state_transport.certificate.json", qm.q79_sm_equicausal_formal_state_transport),
    ("free_cstar", "q79_sm_free_physical_cstar_reference_and_nonpromotion.certificate.json", qm.q79_sm_free_physical_cstar_reference_and_nonpromotion),
    ("finite_regulator", "q79_sm_gauge_compatible_finite_bv_regulator_criterion.certificate.json", qm.q79_sm_gauge_compatible_finite_bv_regulator_criterion),
    ("local_regulator", "q79_sm_local_auxiliary_elliptic_bv_regulator.certificate.json", qm.q79_sm_local_auxiliary_elliptic_bv_regulator),
    ("finite_shell", "q79_sm_finite_shell_bv_pushforward_regulator_comparison.certificate.json", qm.q79_sm_finite_shell_bv_pushforward_regulator_comparison),
    ("gauge_orbit", "q79_sm_based_gauge_frame_regulator_orbit.certificate.json", qm.q79_sm_based_gauge_frame_regulator_orbit),
    ("diffeomorphism_orbit", "q79_sm_diffeomorphism_transported_regulator_orbit.certificate.json", qm.q79_sm_diffeomorphism_transported_regulator_orbit),
    ("metric_rigidity", "q79_cauchy_normal_euclidean_metric_rigidity.certificate.json", qm.q79_cauchy_normal_euclidean_metric_rigidity),
    ("temporal_companion", "q79_temporal_companion_free_shell_independence.certificate.json", qm.q79_temporal_companion_free_shell_independence),
    ("determinant_phase", "q79_sm_determinant_phase_torsor_quotient.certificate.json", qm.q79_sm_determinant_phase_torsor_quotient),
    ("boundary_crossing", "q79_sm_boundary_crossing_line_reduction.certificate.json", qm.q79_sm_boundary_crossing_line_reduction),
    ("boundary_source", "q79_bulk_to_boundary_dirac_family_source_cutset.certificate.json", qm.q79_bulk_to_boundary_dirac_family_source_cutset),
    ("boundaryless_gluing", "q79_boundaryless_bv_bfv_gluing_phase_reduction.certificate.json", qm.q79_boundaryless_bv_bfv_gluing_phase_reduction),
    ("cofinal_cutoff", "q79_cofinal_free_bv_cutoff_and_interacting_counterterm_cutset.certificate.json", qm.q79_cofinal_free_bv_cutoff_and_interacting_counterterm_cutset),
    ("heat_counterterm", "q79_heat_kernel_counterterm_seed_and_qme_induction_cutset.certificate.json", qm.q79_heat_kernel_counterterm_seed_and_qme_induction_cutset),
    ("heat_kernel", "q79_costello_gaugefixing_laplace_and_interior_heat_kernel.certificate.json", qm.q79_gaugefixed_laplace_and_interior_heat_kernel),
    ("first_counterterm", "q79_firstorder_costello_bv_graphwise_counterterm.certificate.json", qm.q79_firstorder_costello_bv_graphwise_counterterm),
    ("euclidean_cutset", "q79_euclidean_reflection_free_physical_os_el_cutset.certificate.json", qm.q79_euclidean_reflection_free_physical_os_el_cutset),
    ("lorentzian_bridge", "q79_lorentzian_spectral_sp_qme_cauchy_bridge.certificate.json", qm.q79_lorentzian_spectral_sp_qme_cauchy_bridge),
    ("fixed_coupling", "q79_fixed_coupling_regulated_cstar_promotion_criterion.certificate.json", qm.q79_fixed_coupling_regulated_cstar_promotion_criterion),
    ("first_tangent", "q79_auxiliary_spectral_fixed_coupling_eg_first_tangent_bridge.certificate.json", qm.q79_auxiliary_spectral_fixed_coupling_eg_first_tangent_bridge),
    ("ward_reduction", "q79_uniform_gauss_ghostzero_brst_ward_defect_reduction.certificate.json", qm.q79_uniform_gauss_ghostzero_brst_ward_defect_reduction),
    ("orbitwise_measure", "q79_orbitwise_finite_spectral_chiral_measure_cutset.certificate.json", qm.q79_orbitwise_finite_spectral_chiral_measure_cutset),
    ("physical_family", "q79_physical_family_source_dependency_analytic_completion_cutset.certificate.json", qm.q79_physical_family_source_dependency_analytic_completion_cutset),
    ("projective_naturality", "q79_covariant_projective_module_hym_symbol_naturality_cutset.certificate.json", qm.q79_covariant_projective_module_hym_symbol_naturality_cutset),
    ("cech_compiler", "q79_explicit_cech_projector_connection_compiler_cutset.certificate.json", qm.q79_explicit_cech_projector_connection_compiler_cutset),
    ("strain_quotient", "q79_intrinsic_spectral_strain_quotient_shorted_hessian_cutset.certificate.json", qm.q79_intrinsic_spectral_strain_quotient_shorted_hessian_cutset),
)


def accepted(payload: dict) -> bool:
    if "all_current" in payload:
        return bool(payload["all_current"])
    return bool(payload.get("all_checks_pass", False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rebuild the source-sensitive QFT certificate chain in dependency order"
    )
    parser.add_argument(
        "--start",
        choices=[step[0] for step in STEPS],
        default="source_freshness",
        help="First step to rebuild; all later consumers are rebuilt.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    start = next(index for index, step in enumerate(STEPS) if step[0] == args.start)
    report = []
    all_pass = True
    for name, filename, compute in STEPS[start:]:
        began = time.monotonic()
        payload = compute()
        path = ROOT / "certificates" / filename
        qm.write_json(path, payload)
        passed = accepted(payload)
        elapsed = round(time.monotonic() - began, 3)
        report.append({"step": name, "path": str(path), "passed": passed, "seconds": elapsed})
        print(json.dumps(report[-1]), flush=True)
        all_pass = all_pass and passed
        if not passed:
            print(f"failed closed at {name}; later consumers were not rebuilt", file=sys.stderr)
            break
    print(json.dumps({"all_pass": all_pass, "steps": len(report)}, indent=2))
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
