"""Attempt physical dotD_alpha1 or selected End0-to-sector routing."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from build_selected_hym_operator_payload_extraction_from_diagonal_replay import fft_operators, replay_solution


ROOT = Path(__file__).resolve().parents[1]
NONS = ROOT.parent / "mtt-nonsm-constants-no-knob"
Q79 = ROOT.parent / "mtt-q79-proof-repro"
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_physical_dotd_alpha1_or_end0_sector_routing.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_physical_dotd_alpha1_or_end0_sector_routing_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_Physical_dotD_alpha1_or_End0_to_Sector_Routing_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def solve_density_scale_tangent(mesh: int, unit_rescale: float) -> dict:
    u, rho, _ = replay_solution(mesh, unit_rescale)
    solve_delta, lap_delta, deriv = fft_operators(u.shape)
    q = rho * np.exp(-2.0 * u)
    rhs = q - q.mean()
    h = np.zeros_like(u)
    residual_l2 = float("inf")
    iterations = 0
    for step in range(200):
        src = rhs - 2.0 * q * h + 2.0 * float((q * h).mean())
        next_h = solve_delta(src)
        next_h -= next_h.mean()
        h = 0.5 * next_h + 0.5 * h
        residual = lap_delta(h) + 2.0 * q * h - 2.0 * float((q * h).mean()) - rhs
        residual_l2 = float(np.linalg.norm(residual.ravel()) / math.sqrt(residual.size))
        iterations = step + 1
        if residual_l2 < 1e-12:
            break

    dotd_u_driver = {}
    for axis, label in enumerate(["x1", "y1", "x2", "y2"]):
        dh = deriv(h, axis)
        dotd_u_driver[label] = {
            "formula": f"dotD_{label}[h_ext_scale] = (partial_{label} h_ext_scale) ad(T3)",
            "l2": float(np.linalg.norm(dh.ravel()) / math.sqrt(dh.size)),
            "min": float(dh.min()),
            "max": float(dh.max()),
        }

    return {
        "h": h,
        "iterations": iterations,
        "residual_l2": residual_l2,
        "h_l2": float(np.linalg.norm(h.ravel()) / math.sqrt(h.size)),
        "h_min": float(h.min()),
        "h_max": float(h.max()),
        "h_mean_abs": float(abs(h.mean())),
        "dotd_direction_summaries": dotd_u_driver,
    }


def main() -> int:
    prev_path = ROOT / "candidate_data" / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json"
    replay_path = ROOT / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
    overlap_path = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
    constants_alpha_path = NONS / "candidate_data" / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"
    q79_sector_path = Q79 / "candidate_data" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
    visible_ah_path = Q79 / "candidate_data" / "visible_rank2_l2_appell_humbert_automorphy.candidate.json"

    prev = load(prev_path)
    replay = load(replay_path)
    overlap = load(overlap_path)
    constants_alpha = load(constants_alpha_path) if constants_alpha_path.exists() else {}
    q79_sector = load(q79_sector_path) if q79_sector_path.exists() else {}
    visible_ah = load(visible_ah_path) if visible_ah_path.exists() else {}

    mesh = int(replay["solver"]["mesh"])
    unit_rescale = float(overlap["selected_row"]["unit_rescale_factor"])
    tangent = solve_density_scale_tangent(mesh, unit_rescale)
    density_scale_tangent_closed = all(
        [
            prev["operator_payload_boundary"]["row_model_offdiagonal_T1T2_source_controlled"] is True,
            tangent["residual_l2"] < 1e-12,
            tangent["h_mean_abs"] < 1e-14,
            tangent["h_l2"] > 0,
        ]
    )

    alpha1_discrete_support = bool(
        visible_ah
        and visible_ah["construction_checks"]["c2_extension_target_is_plus_4_alpha1"] is True
        and visible_ah["construction_checks"]["central_shared_circle_trivial"] is True
    )
    constants_says_alpha_open = bool(
        constants_alpha
        and constants_alpha["transfer_checks"]["K2_q79_phi_fin_alpha1_support_available"] is True
        and constants_alpha["transfer_checks"]["K6_selected_BN_tangent_or_retarded_kernel"] is False
    )
    q79_sector_routing_open = bool(
        q79_sector
        and q79_sector["sector_charge_reduction"]["decision"]["selected_sector_charge_or_chirality_table_proved"] is False
        and q79_sector["sector_charge_reduction"]["decision"]["selected_transfer_normalization_proved"] is False
    )

    physical_dotd_alpha1_closed = False
    sector_routing_closed = False

    candidate = {
        "candidate": "MTTSelectedPhysicalDotDAlpha1OrEnd0SectorRouting",
        "status": "MTT_SELECTED_EXT_SCALE_DOTD_TANGENT_CLOSED_PHYSICAL_ALPHA1_ROUTING_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "offdiagonal_Ext_control": str(prev_path),
            "diagonal_expS_replay": str(replay_path),
            "eta00_overlap_Hodge_projector_table": str(overlap_path),
            "constants_alpha1_tangent_attempt": str(constants_alpha_path) if constants_alpha_path.exists() else None,
            "q79_sector_charge_or_chirality": str(q79_sector_path) if q79_sector_path.exists() else None,
            "q79_visible_AH_alpha1_support": str(visible_ah_path) if visible_ah_path.exists() else None,
        },
        "path_A_straight_selected_Ext_density_scale_tangent": {
            "closed": density_scale_tangent_closed,
            "equation": "L h = q - mean(q), Lh = Delta h + 2 q h - 2 mean(q h), q=rho exp(-2u)",
            "meaning": "selected continuous response to scaling the normalized Ext density in the HYM row equation",
            "iterations": tangent["iterations"],
            "residual_l2": tangent["residual_l2"],
            "h_l2": tangent["h_l2"],
            "h_min": tangent["h_min"],
            "h_max": tangent["h_max"],
            "h_mean_abs": tangent["h_mean_abs"],
            "dotD_direction_summaries": tangent["dotd_direction_summaries"],
            "promotion_to_physical_alpha1": False,
            "why_not_physical_alpha1": "alpha1 is a discrete Chern/curvature row for the selected branch; this tangent is a legal local Ext-density response but not theorem-derived as the physical same-branch alpha1 derivative.",
        },
        "path_B_physical_alpha1_or_sector_routing": {
            "physical_dotD_alpha1_closed": physical_dotd_alpha1_closed,
            "sector_routing_closed": sector_routing_closed,
            "alpha1_discrete_support_from_visible_AH": alpha1_discrete_support,
            "constants_repo_alpha1_tangent_still_open": constants_says_alpha_open,
            "q79_sector_charge_and_transfer_still_open": q79_sector_routing_open,
            "why_not_closed": "The support repos agree on the alpha1/sector-routing target, but selected sector charge/chirality, transfer normalization, and a same-branch alpha1 tangent theorem remain open.",
        },
        "operator_payload_boundary": {
            "selected_Ext_density_scale_dotD_tangent_extracted": density_scale_tangent_closed,
            "physical_dotD_alpha1_payload_extracted": physical_dotd_alpha1_closed,
            "selected_End0_to_sector_routing_values_extracted": sector_routing_closed,
            "validator_ready": False,
            "why_not_validator_ready": "A selected local HYM tangent is emitted, but the physical alpha1 driver and End0-to-sector routing are not theorem-derived.",
        },
        "what_closes_now": {
            "linearized_HYM_Ext_density_scale_tangent": density_scale_tangent_closed,
            "dotD_Frechet_replay_on_selected_tangent": density_scale_tangent_closed,
            "physical_alpha1_not_confused_with_continuous_knob": True,
            "sector_routing_support_imported_without_promotion": bool(q79_sector),
        },
        "what_remains_open": {
            "physical_dotD_alpha1_same_branch_driver": True,
            "selected_End0_to_sector_routing_values": True,
            "selected_transfer_normalization": True,
            "selected_sector_charge_or_chirality_table": True,
            "full_AH_Cech_offdiagonal_control_beyond_single_row_model": True,
            "validator_ready_sector_D_E_Riesz_Green_dotD": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_path": "Compute the selected continuous Ext-density tangent of the solved HYM row equation and its dotD Frechet replay.",
            "support_path": "Use constants/q79 repos to locate the missing physical alpha1 and sector-routing theorem; do not import their conditional/detection artifacts as proof.",
            "locked_target": "selected eta_00 row and diagonal HYM/End0 packet, no measured constants.",
            "not_used": "No observed masses, mixings, couplings, benchmark matrices, inverse-search targets, or lifted selected flags.",
        },
        "next_required_artifact": "MTT_Selected_Alpha1_Tangent_Promotion_or_SectorRouting_Normalization_Theorem_v1",
    }

    cert = {
        "certificate": "MTT_Selected_Physical_dotD_alpha1_or_End0_to_Sector_Routing_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "selected_Ext_density_scale_tangent_closed": density_scale_tangent_closed,
        "physical_dotD_alpha1_payload_extracted": physical_dotd_alpha1_closed,
        "selected_End0_to_sector_routing_values_extracted": sector_routing_closed,
        "residual_l2": tangent["residual_l2"],
        "validator_ready": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = f"""# MTT Selected Physical dotD alpha1 or End0 to Sector Routing v1

## Straight Path: Selected Ext-Density Tangent

The selected HYM row equation has a legal continuous tangent obtained by scaling
the normalized Ext density:

```text
L h = q - mean(q)
Lh = Delta h + 2 q h - 2 mean(q h)
q = rho exp(-2u)
```

The solve converges with:

```text
residual L2 = {tangent["residual_l2"]:.3e}
||h||_L2 = {tangent["h_l2"]:.12g}
h_min = {tangent["h_min"]:.12g}
h_max = {tangent["h_max"]:.12g}
```

and feeds the already-fixed Frechet schema:

```text
dotD_a[h] = (partial_a h) ad(T3)
```

## Guardrail

This is not yet physical `dotD_alpha1`.  The alpha1 row is discrete Chern/source
data for the selected branch, not an ordinary continuous knob.  Promoting this
Ext-density tangent to physical `alpha1` requires a same-branch theorem or
selected sector-routing normalization.

## Superset Path

The q79/constants repos support the same target, but keep selected sector charge,
transfer normalization, and physical alpha1 tangent open.  They are imported as
support only.

## Next Artifact

`MTT_Selected_Alpha1_Tangent_Promotion_or_SectorRouting_Normalization_Theorem_v1`.
"""

    OUT_CANDIDATE.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_PROOF.write_text(proof, encoding="utf-8")
    print(f"Wrote {OUT_CANDIDATE}")
    print(f"Wrote {OUT_CERT}")
    print(f"Wrote {OUT_PROOF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
