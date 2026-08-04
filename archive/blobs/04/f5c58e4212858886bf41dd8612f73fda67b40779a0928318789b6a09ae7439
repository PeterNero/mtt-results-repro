from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
THETA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\18 Theta-Closure & Execution Program\_md_v3_corrected")
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

DIMENSIONLESS_GAP = ROOT / "certificates" / "dimensionless_modal_gap_operator_reduction_certificate.json"

QG = OBSIDIAN / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
THETA_I = THETA / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md"
Z64_DAMPING = NONSM / "proof_corpus" / "Damping_Hessian_Z64_Block_Identification_v1.md"
PHYSICAL_ACTION = NONSM / "certificates" / "physical_action_normalization_gate_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_aint_packet_branch_bridge_audit_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def gap_row(name: str, value: float, status: str) -> dict[str, float | str]:
    return {
        "branch": name,
        "lambda_star": value,
        "sqrt_lambda_star": math.sqrt(value),
        "tau0_if_saturated": 1.0 / value,
        "status": status,
    }


def main() -> None:
    prior = json.loads(DIMENSIONLESS_GAP.read_text(encoding="utf-8"))
    qg = read(QG)
    theta_i = read(THETA_I)
    z64 = read(Z64_DAMPING)
    physical_action = json.loads(PHYSICAL_ACTION.read_text(encoding="utf-8"))

    source_tests = {
        "qg_defines_global_aint_packet": has(
            qg,
            "A := \\kappa_1\\Delta_{B_1} + \\kappa_2\\Delta_{B_2} + \\kappa_3\\Delta_{B_3}",
            "\\lambda_\\ast := \\min_n \\kappa_n\\lambda_{n,\\ast}",
        ),
        "theta_nil_saturates_floor_in_benchmark": has(
            theta_i,
            "lambda_{\\mathrm{nil}} = \\frac{1}{4} = 0.25",
            "The nil sector saturates the minimal gap",
        ),
        "theta_warns_explicit_realizations_need_not_saturate": has(
            theta_i,
            "explicit realizations of the nil sector may",
            "exceed this bound and need not saturate it",
        ),
        "theta_nil_kappa_is_overlap_weight_not_aint_kappa": has(
            theta_i,
            "\\kappa_n\\,\\mathcal{S}_n is the effective nil overlap weight",
            "not assumed equal to a simple metric area",
        ),
        "z64_exact_branch_has_lambda_15": has(
            z64,
            "lambda_* = 15 alpha",
            "lambda_* = 15.",
        ),
        "physical_action_marks_lambda15_internal_only": physical_action["canonical_internal_normalization"]["lambda_star"] == 15.0
        and physical_action["verdict"]["physical_absolute_dimensionful_predictions_closed"] is False,
    }

    branches = [
        gap_row(
            "theta_nil_floor_benchmark",
            0.25,
            "INTERNAL_FLOOR_SATURATED_IN_THETA_BENCHMARK_NOT_SELECTED_GLOBAL_AINT_PACKET",
        ),
        gap_row(
            "z64_central_circle_exact_branch",
            15.0,
            "INTERNAL_EXACT_BRANCH_DAMPING_VALUE_GR_MODAL_GAP_BRIDGE_OPEN",
        ),
    ]

    import_decisions = {
        "can_import_qg_Aint_shape": True,
        "can_import_theta_nil_floor_as_universal_bound": True,
        "can_import_theta_nil_floor_as_selected_global_saturation": False,
        "can_import_z64_lambda15_as_internal_exact_branch_value": True,
        "can_import_z64_lambda15_as_physical_modal_gap": False,
        "can_replace_GR_modal_gap_with_z64_without_bridge": False,
    }

    missing_bridge = {
        "name": "Selected_Aint_Branch_Bridge_Theorem",
        "must_show": [
            "which selected branch supplies the GR/QG A_int operator",
            "whether its noncoherent complement is the nil floor branch, the Z64 central-circle branch, or another quotient",
            "the selected kappa_1,kappa_2,kappa_3 in the same operator convention",
            "the selected fiber eigenvalues lambda_{n,*} after quotienting zero modes",
            "whether lambda_* is exactly 0.25, exactly 15, or a distinct selected value",
            "why the chosen value is not transferred across incompatible normalizations",
        ],
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_aint_packet_branch_bridge_audit",
        "status": "AINT_PACKET_BRANCHES_CLASSIFIED_SELECTED_BRANCH_BRIDGE_OPEN",
        "input_certificates": {
            "dimensionless_modal_gap_operator_reduction": str(DIMENSIONLESS_GAP),
            "physical_action_normalization": str(PHYSICAL_ACTION),
        },
        "source_files": {
            "qg": str(QG),
            "theta_i": str(THETA_I),
            "z64_damping": str(Z64_DAMPING),
        },
        "source_tests": source_tests,
        "branch_gap_table": branches,
        "import_decisions": import_decisions,
        "missing_bridge": missing_bridge,
        "verdict": {
            "operator_shape_closed": prior["verdict"]["dimensionless_operator_shape_closed"],
            "selected_global_Aint_packet_closed": False,
            "strongest_candidate": "z64_central_circle_exact_branch",
            "why_not_closed": (
                "The Z64 value lambda_*=15 is selected in normalized exact-branch "
                "damping units, while the QG/GR A_int packet uses a global "
                "noncoherent complement min_n kappa_n lambda_n. A bridge theorem "
                "must identify these before substitution."
            ),
        },
        "guardrails": {
            "claims_lambda15_is_GR_modal_gap": False,
            "claims_nil_floor_saturates_all_selected_branches": False,
            "claims_physical_modal_gap": False,
            "forbids_cross_branch_substitution_without_bridge": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
