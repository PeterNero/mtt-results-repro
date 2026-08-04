from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

ROLE_CERT = ROOT / "certificates" / "tt_gap_external_domain_vs_internal_aint_role_certificate.json"
DIMENSIONLESS_CERT = ROOT / "certificates" / "dimensionless_modal_gap_operator_reduction_certificate.json"
BRANCH_CERT = ROOT / "certificates" / "selected_aint_packet_branch_bridge_audit_certificate.json"
Z64_COND_CERT = ROOT / "certificates" / "conditional_z64_qg_gap_bridge_certificate.json"
Z64_IDENTITY_CERT = ROOT / "certificates" / "gr_tt_aint_z64_identity_source_hunt_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_internal_aint_complement_gap_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Internal_Aint_Complement_Gap_Theorem_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    role = load(ROLE_CERT)
    dimensionless = load(DIMENSIONLESS_CERT)
    branch = load(BRANCH_CERT)
    z64_cond = load(Z64_COND_CERT)
    z64_identity = load(Z64_IDENTITY_CERT)

    candidates = [
        {
            "id": "exact_z64_central_circle",
            "candidate_lambda_star": 15.0,
            "numeric_status": "exact_on_internal_Z64_branch",
            "required_to_promote": "prove GR/QG A_int noncoherent complement is the same exact Z64 central-circle tower",
            "currently_promoted": False,
            "blocking_certificate": str(Z64_IDENTITY_CERT),
        },
        {
            "id": "theta_nil_floor",
            "candidate_lambda_star": 0.25,
            "numeric_status": "internal_floor_or_benchmark",
            "required_to_promote": "prove the selected GR/QG A_int packet saturates the nil floor",
            "currently_promoted": False,
            "blocking_certificate": str(BRANCH_CERT),
        },
        {
            "id": "direct_product_fiber_packet",
            "candidate_lambda_star": "min_n kappa_n lambda_n",
            "numeric_status": "formula_closed_values_open",
            "required_to_promote": "compute selected kappa_n and fiber eigenvalues after quotient/projector/window",
            "currently_promoted": False,
            "blocking_certificate": str(DIMENSIONLESS_CERT),
        },
        {
            "id": "flux_fuyau_internal_gap",
            "candidate_lambda_star": "positive_gap_only",
            "numeric_status": "existence/coercivity_source_not_numeric",
            "required_to_promote": "extract the selected torsionful Laplacian spectrum and identify it with QG A_int",
            "currently_promoted": False,
            "blocking_certificate": None,
        },
    ]

    source_tests = {
        "numeric_gap_refocused_on_internal_Aint": role["decisions"][
            "numeric_gap_refocused_on_selected_internal_Aint"
        ],
        "dimensionless_Aint_formula_closed": dimensionless["verdict"]["dimensionless_operator_shape_closed"],
        "z64_conditional_bridge_closed": z64_cond["verdict"]["conditional_bridge_closed"],
        "z64_usable_now_as_GR_modal_gap": z64_cond["verdict"]["usable_now_as_GR_modal_gap"],
        "direct_z64_identity_not_sourced": (
            z64_identity["status"] == "GR_TT_AINT_Z64_IDENTITY_NOT_SOURCED_CLOSURE_STRAIN_ROUTE_REMAINS"
        ),
        "selected_global_Aint_packet_closed": branch["verdict"]["selected_global_Aint_packet_closed"],
    }

    decision_tree = {
        "route_1_fastest": {
            "name": "prove_Z64_same_branch_identity",
            "if_success": "lambda_star_internal = 15 in normalized exact-branch damping units",
            "current_state": "conditional bridge closed, GR identity not sourced",
        },
        "route_2_foundational": {
            "name": "compute_selected_product_fiber_packet",
            "if_success": "lambda_star_internal = min_n kappa_n lambda_n from selected fixed-point data",
            "current_state": "operator shape closed, selected kappas/fiber eigenvalues open",
        },
        "route_3_floor": {
            "name": "prove_nil_floor_saturation",
            "if_success": "lambda_star_internal = 0.25",
            "current_state": "bound/benchmark present, saturation not selected globally",
        },
        "route_4_flux": {
            "name": "extract_FuYau_or_flux_torsionful_gap",
            "if_success": "positive selected compactification gap becomes candidate Aint spectrum",
            "current_state": "selection/coercivity sourced, numerical spectrum and QG identity open",
        },
    }

    note = """# Selected Internal Aint Complement Gap Theorem v1

## Result

The selected TT numerical gap is now reduced to a finite internal `A_int`
decision tree.

The current corpus does not yet promote a number. It does close the target:

```text
lambda_* = first positive eigenvalue of the selected internal A_int
            on the noncoherent/Q complement.
```

## Candidate Routes

1. Prove the GR/QG `A_int` complement is the exact Z64 central-circle tower.
   Then the conditional bridge imports `lambda_* = 15`.
2. Compute the selected product-fiber packet directly:
   `lambda_A = min_n kappa_n lambda_n`.
3. Prove the selected packet saturates the nil floor, giving `lambda_* = 0.25`.
4. Extract a selected Fu-Yau/flux torsionful spectrum and identify it with QG
   `A_int`.

## Current Verdict

The fastest route is Z64 same-branch identity, because its internal exact value
is already computed conditionally. The most foundational route is direct packet
computation from selected fixed-point data. Neither is closed yet.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_internal_aint_complement_gap_theorem",
        "status": "SELECTED_INTERNAL_AINT_GAP_REDUCED_TO_BRANCH_IDENTITY_OR_PACKET_COMPUTATION",
        "input_certificates": {
            "tt_gap_role": str(ROLE_CERT),
            "dimensionless_operator_reduction": str(DIMENSIONLESS_CERT),
            "branch_bridge": str(BRANCH_CERT),
            "conditional_z64_qg_gap_bridge": str(Z64_COND_CERT),
            "z64_identity_source_hunt": str(Z64_IDENTITY_CERT),
        },
        "source_tests": source_tests,
        "candidate_routes": candidates,
        "decision_tree": decision_tree,
        "closed_now": {
            "numeric_gap_target_is_internal_Aint": True,
            "candidate_routes_ranked": True,
            "z64_import_condition_stated": True,
            "direct_packet_formula_recalled": True,
        },
        "selection_result": {
            "selected_internal_Aint_gap_computed": False,
            "selected_route": None,
            "selected_lambda_star": None,
            "reason": (
                "Z64 has an exact conditional value, nil has a floor/benchmark, and "
                "the direct packet has a closed formula. The source theorem selecting "
                "which branch is the GR/QG A_int complement remains open."
            ),
        },
        "next_gate": {
            "name": "GR_QG_Aint_Same_Branch_Identity_or_Direct_Packet_Computation",
            "preferred_order": [
                "attempt source proof that GR/QG A_int complement equals exact Z64 central-circle tower",
                "if absent, compute selected kappa_n and lambda_n from fixed-point product-fiber data",
                "test nil-floor saturation only if the selected packet collapses to the nil floor",
                "use flux/Fu-Yau torsionful spectrum as a compactification cross-check",
            ],
        },
        "guardrails": {
            "claims_z64_unconditional_GR_gap": False,
            "claims_nil_floor_saturation": False,
            "claims_direct_packet_values_known": False,
            "claims_physical_dimensionful_gap": False,
            "claims_full_GR_response_closed": False,
        },
        "note_written": str(OUT_NOTE),
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
