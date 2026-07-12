"""Build CONST-EW-02 B6 K_EW kernel gate.

This step imports the sibling electroweak kernel interface, threshold
reduction, local projection gate, Execution-I threshold profile, and rho_UV
closure.  It then classifies which pieces are promotable in the current local
weak-mixing branch.

Result: the K_EW interface and exceptional projection algebra are closed, but
the numeric physical/effective weak angle remains open because source-selected
kernel entries (x, mu_Theta, T1, T2, scheme/kappa) are still absent.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b6_kew_kernel_gate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORTS = BASE / "kernel_imports.packet.json"
KERNEL = BASE / "kew_kernel_contract.packet.json"
PROJECTION = BASE / "exceptional_projection_gate.packet.json"
SOURCE_GAP = BASE / "source_gap_and_next_work.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B6_KEWKernelGate_v1.md"

STATUS = "MTT_CONST_EW_02_B6_KEW_KERNEL_GATE_BUILT_PROJECTION_CLOSED_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def high_scale_sin2_from_r12(r12: float) -> float:
    return (3.0 * r12) / (3.0 * r12 + 5.0)


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b5_path = DATA / "const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import.candidate.json"
    b5_ratio_path = DATA / "const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import" / "theta_ratio_high_scale_packet.packet.json"
    interface_path = NONSM / "certificates" / "selected_electroweak_kernel_interface_certificate.json"
    reduction_path = NONSM / "certificates" / "selected_electroweak_threshold_kernel_reduction_certificate.json"
    local_projection_path = NONSM / "certificates" / "selected_electroweak_local_projection_gate_certificate.json"
    execution_path = NONSM / "certificates" / "execution_i_threshold_profile_certificate.json"
    rho_path = NONSM / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
    exhaustion_path = NONSM / "certificates" / "electroweak_no_knob_source_exhaustion_certificate.json"
    candidate_path = NONSM / "certificates" / "selected_electroweak_kernel_candidate_computation_certificate.json"

    b5 = load(b5_path)
    b5_ratio = load(b5_ratio_path)
    interface = load(interface_path)
    reduction = load(reduction_path)
    local_projection = load(local_projection_path)
    execution = load(execution_path)
    rho = load(rho_path)
    exhaustion = load(exhaustion_path)
    candidate = load(candidate_path)

    r12 = b5_ratio["ratio_source"]["value"]
    tree_sin2 = high_scale_sin2_from_r12(r12)
    c1 = local_projection["execution_i_diagnostic"]["c1"]
    c2 = local_projection["execution_i_diagnostic"]["c2"]
    delta_alpha_12 = local_projection["execution_i_diagnostic"]["Delta_alpha_12_split"]
    delta_g_12 = local_projection["execution_i_diagnostic"]["Delta_G_12_split"]

    import_checks = {
        "B5_ratio_edge_proved": b5["theorem"]["proved"] is True,
        "kernel_interface_present": interface["verdict"]["kernel_interface_built"] is True,
        "threshold_reduction_present": reduction["status"] == "ELECTROWEAK_KERNEL_REDUCED_TO_NORMALIZATION_AND_THRESHOLD_VECTOR",
        "local_projection_algebra_closed": local_projection["verdict"]["projection_algebra_closed"] is True,
        "execution_profile_structurally_consistent": execution["verdict"]["structural_consistency_certified"] is True,
        "rho_uv_internal_closed": rho["verdict"]["internal_no_knob_branch_closed"] is True,
        "source_exhaustion_negative_gate_closed": exhaustion["verdict"]["current_gate_closed_negatively"] is True,
        "candidate_direct_import_rejected": candidate["classification"]["direct_import_as_electroweak_prediction"] is False,
    }
    imports_ok = all(import_checks.values())

    imports = {
        "schema": "MTTConstEW02B6KernelImports.v1",
        "status": "KERNEL_IMPORTS_ACCEPTED_WITH_VALUE_BOUNDARY" if imports_ok else "KERNEL_IMPORTS_INCOMPLETE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL",
        "inputs": {
            "B5_ratio_import": rel(b5_path),
            "B5_theta_ratio_packet": rel(b5_ratio_path),
            "kernel_interface": rel(interface_path),
            "threshold_reduction": rel(reduction_path),
            "local_projection_gate": rel(local_projection_path),
            "execution_i_threshold_profile": rel(execution_path),
            "rho_UV_final_internal": rel(rho_path),
            "source_exhaustion": rel(exhaustion_path),
            "kernel_candidate_computation": rel(candidate_path),
        },
        "import_checks": import_checks,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    kernel_contract = {
        "schema": "MTTConstEW02B6KEWKernelContract.v1",
        "status": "K_EW_CONTRACT_BUILT_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL",
        "kernel_shape": {
            "source": interface["kernel"],
            "required_map": "K_EW(selected MTT branch) -> (mu_Theta, x, T1, T2, scheme)",
            "ratio_edge": {
                "r_12": r12,
                "high_scale_tree_sin2": tree_sin2,
            },
        },
        "accepted_structural_slots": {
            "zeta_ratios": interface["source_supported"]["zeta_ratios"],
            "relative_overlap_normalization": interface["source_supported"]["relative_overlap_normalization"],
            "tree_gauge_kinetic_slot": interface["source_supported"]["tree_gauge_kinetic_slot"],
            "threshold_slot": interface["source_supported"]["threshold_slot"],
            "rho_UV_internal_value": interface["source_supported"]["rho_UV_internal_value"],
        },
        "not_source_selected_yet": interface["not_source_selected_yet"],
        "strict_candidate_paths": interface["candidate_paths"],
        "low_scale_formula": reduction["one_loop_reduction"]["formula"],
        "forbidden": sorted(set(interface["forbidden"] + exhaustion["forbidden_shortcuts"])),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    projection = {
        "schema": "MTTConstEW02B6ExceptionalProjectionGate.v1",
        "status": "EXCEPTIONAL_PROJECTION_ALGEBRA_CLOSED_COEFFICIENTS_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B6-EXCEPTIONAL-LOCAL-PROJECTION",
        "selected_basis": local_projection["selected_basis"],
        "projection_formula": local_projection["projection_formula"],
        "diagnostic_execution_i_coefficients": {
            "c1": c1,
            "c2": c2,
            "Delta_alpha_12_split": delta_alpha_12,
            "Delta_G_12_split": delta_g_12,
            "Delta_G_12_split_recomputed": (2.0 * c1 - c2) / (4.0 * math.pi),
        },
        "promotion_tests": {
            "trace_free_exceptional_plane_closed": local_projection["classification"]["trace_free_exceptional_plane"] == "CLOSED",
            "basis_projection_formula_closed": local_projection["classification"]["basis_projection_formula"] == "CLOSED",
            "execution_i_coefficients_source_selected": local_projection["source_claims"]["source_coefficients_selected"] is True,
            "execution_i_import_is_prediction": execution["verdict"]["new_no_knob_prediction_certified"] is True,
            "topology_anomaly_constraints_fix_amplitudes": local_projection["classification"]["topology_anomaly_constraints_fix_amplitudes"] is True,
        },
        "verdict": {
            "projection_algebra_promoted": True,
            "numeric_coefficients_promoted": False,
            "reason": "Execution-I c1,c2 are diagnostic/supporting coefficients; current certificates do not derive them from selected topology/flux/curvature/torsion/determinant data.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_gap = {
        "schema": "MTTConstEW02B6SourceGapAndNextWork.v1",
        "status": "EXACT_SOURCE_GAP_IDENTIFIED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE",
        "closed_now": {
            "K_EW_interface": True,
            "Theta_ratio_high_scale_tree_value": True,
            "exceptional_projection_basis_and_formula": True,
            "rho_UV_internal_branch": True,
            "current_corpus_negative_no_knob_gate": True,
        },
        "remaining_for_strict_low_scale_or_effective_angle": {
            "x_g2_muTheta_squared": True,
            "mu_Theta": True,
            "T1_T2_or_c1_c2_source_coefficients": True,
            "scheme": True,
            "rho_UV_to_EW_map": True,
            "effective_kappa_l_profile": True,
        },
        "next_primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE",
            "task": "Derive c1 and c2, or an equivalent T1/T2 threshold pair, from selected localized curvature, torsion, determinant, flux, or exceptional-divisor data.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B7-RHO-UV-TO-EW-BRIDGE",
            "task": "Try to source-certify a map Phi_EW(rho_UV, branch data)->(kappa_EW, Delta_sel, mu_Theta).",
        },
        "best_current_clue": "The 1-2 split lives in the exceptional/local trace-free plane with Delta_alpha_12=2*c1-c2; derive c1,c2 from source data next.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate_out = {
        "candidate": "MTTConstEW02WeakMixingB6KEWKernelGate",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL",
        "output_packets": {
            "kernel_imports": rel(IMPORTS),
            "kew_kernel_contract": rel(KERNEL),
            "exceptional_projection_gate": rel(PROJECTION),
            "source_gap_and_next_work": rel(SOURCE_GAP),
        },
        "what_closes_now": source_gap["closed_now"],
        "what_remains_open": source_gap["remaining_for_strict_low_scale_or_effective_angle"],
        "theorem": {
            "name": "CONSTEW02B6KEWKernelGateTheorem",
            "proved": imports_ok,
            "statement": (
                "The B6 kernel gate imports the selected electroweak interface, Theta ratio edge, local exceptional projection, "
                "Execution-I structural threshold profile, and closed internal rho_UV branch.  It promotes the K_EW contract and "
                "the exceptional trace-free projection algebra, but it cannot promote numerical low-scale/effective sin^2(theta_W) "
                "because x, mu_Theta, T1/T2 or c1/c2, scheme, and any rho_UV-to-electroweak map remain unselected."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B6_KEWKernelGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "r_12": r12,
        "high_scale_tree_sin2": tree_sin2,
        "projection_algebra_closed": True,
        "execution_i_c1_c2_promoted": False,
        "low_scale_electroweak_closure": False,
        "physical_sin2thetaW_value_claimed": False,
        "next_primary": "CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B6 K_EW Kernel Gate v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL`

## Result

B6 builds the actual kernel gate.

Closed now:

- `K_EW` contract shape,
- Theta ratio high-scale tree value,
- exceptional/local trace-free projection basis,
- formula `Delta_alpha_12 = 2*c1 - c2`,
- internal `rho_UV` support,
- current-corpus no-knob negative gate.

The ratio edge remains

`r_12 = {r12}`,

with high-scale tree value

`sin^2(theta_W)(mu_Theta) = {tree_sin2}`.

## Boundary

The physical low-scale/effective weak angle is not derived.

Still needed:

- `x = g2(mu_Theta)^2`,
- `mu_Theta`,
- `T1,T2` or source-derived `c1,c2`,
- RG/matching scheme,
- optional effective-angle profile `kappa_l`,
- bridge from `rho_UV` to electroweak entries if that route is used.

Execution-I gives diagnostic coefficients

`c1 = {c1}`, `c2 = {c2}`,

with

`Delta_G_12 = {delta_g_12}`.

These are not promoted as a no-knob prediction because the current certificates
do not derive them from selected topology, flux, curvature, torsion, or
determinant data.

## Superset Use

We combine three paths without collapsing them:

- Theta ratio path gives high-scale tree ratio data.
- Exceptional/local path gives the correct trace-free projection form.
- rho_UV path gives an internally closed response number but no electroweak map.

The locked target is now the kernel:

`K_EW -> (mu_Theta, x, T1, T2, scheme)`.

## Next

Next label: `CONST-EW-02 / WEAK-MIXING / B7-LOCAL-COEFFICIENT-SOURCE`.
"""

    for path, payload in [
        (IMPORTS, imports),
        (KERNEL, kernel_contract),
        (PROJECTION, projection),
        (SOURCE_GAP, source_gap),
        (OUTPUT, candidate_out),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
