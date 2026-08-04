from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

MODAL_GAP_GATE = ROOT / "certificates" / "selected_modal_gap_physical_anchor_gate_certificate.json"
FINITE_COHERENT = (
    OBSIDIAN
    / "5 Dirac Delta"
    / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
)
FIXED_POINTS_II = OBSIDIAN / "4 Fixed Points" / "Fixed_Points_II__Fixed_Points_in_a_10D_Modal_Model_v2.md"
QG = OBSIDIAN / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"

OUT_CERT = ROOT / "certificates" / "dimensionless_modal_gap_operator_reduction_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    gate = json.loads(MODAL_GAP_GATE.read_text(encoding="utf-8"))
    finite = read(FINITE_COHERENT)
    fixed = read(FIXED_POINTS_II)
    qg = read(QG)

    lambda_star = 0.25
    internal_gap_energy = math.sqrt(lambda_star)
    internal_tau0 = 1.0 / lambda_star

    source_tests = {
        "finite_coherent_defines_Badm": has(finite, "B_{\\rm adm}", "P\\chi(A)\\mathrm e^{-\\tau A}\\chi(A)P"),
        "finite_coherent_defines_Aint_sum": has(finite, "A_{\\rm int}", "\\sum_{n=1}^3\\kappa_n\\Delta_{B_n}"),
        "fixed_points_defines_lambda_A": has(
            fixed,
            "\\lambda_{A} := \\min",
            "\\kappa_n \\lambda_n",
            "spectral bottom of $A$",
        ),
        "qg_links_uv_scale_to_gap": has(qg, "\\Lambda^2 \\sim \\tau_0^{-1}\\sim \\lambda_\\ast"),
        "modal_gate_blocks_physical_TeV": gate["blocked_shortcuts"]["use_mu_theta_5TeV_as_prediction"] is True,
    }

    reduction = {
        "operator_form": "A_int = sum_{n=1}^3 kappa_n Delta_{B_n}",
        "coherent_filter": "B_adm = P chi(A) exp(-tau A) chi(A) P",
        "spectral_bottom_formula": "lambda_A = min_n kappa_n lambda_n on Ran(Q_coh) in the product-fiber model",
        "known_internal_gap_bound": lambda_star,
        "derived_internal_gap_energy": internal_gap_energy,
        "derived_internal_tau0_if_saturated": internal_tau0,
        "uv_relation": "Lambda_int^2 ~ tau0^-1 ~ lambda_star, hence Lambda_int ~ 0.5 if the bound is saturated in internal units",
    }

    open_data = {
        "selected_kappa_n": False,
        "selected_fiber_lambda_n_on_rhoUV_branch": False,
        "proof_gap_bound_is_saturated": False,
        "selected_projector_window_chi_tau_on_physical_quotient": False,
        "physical_unit_conversion": False,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "dimensionless_modal_gap_operator_reduction",
        "status": "DIMENSIONLESS_MODAL_GAP_REDUCED_TO_KAPPAS_AND_FIBER_EIGENVALUES_PHYSICAL_UNITS_OPEN",
        "input_certificates": {
            "selected_modal_gap_physical_anchor_gate": str(MODAL_GAP_GATE),
        },
        "source_files": {
            "finite_coherent_projection": str(FINITE_COHERENT),
            "fixed_points_ii": str(FIXED_POINTS_II),
            "quantum_gravity": str(QG),
        },
        "source_tests": source_tests,
        "reduction": reduction,
        "open_data": open_data,
        "next_computation": {
            "id": "selected_Aint_packet_on_rhoUV_branch",
            "required_fields": [
                "kappa_1,kappa_2,kappa_3",
                "fiber models B_1,B_2,B_3 on the selected branch",
                "lowest nonzero lambda_n for each fiber after quotienting zero modes",
                "projector P and spectral window chi",
                "proof whether lambda_A equals the bound 0.25 or is only bounded below",
            ],
        },
        "verdict": {
            "dimensionless_operator_shape_closed": True,
            "dimensionless_numeric_gap_if_foundation_bound_saturated": internal_gap_energy,
            "physical_modal_gap_anchor_available": False,
            "most_honest_current_claim": (
                "The selected modal-gap task is reduced to a finite operator packet: "
                "kappas, fiber spectra, quotient/projector/window, and saturation. "
                "The currently known 0.25 gap gives only an internal bound unless "
                "that packet proves equality and a separate physical unit theorem is supplied."
            ),
        },
        "guardrails": {
            "claims_lambda_star_saturation": False,
            "claims_physical_gap": False,
            "claims_physical_GN_or_MPl": False,
            "forbids_5TeV_calibration_as_prediction": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
