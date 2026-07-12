"""Audit the selected Route-C/Strominger Galerkin solve spec artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_strominger_galerkin_solve_spec.candidate.json"
CERT = REPO / "certificates" / "selected_routec_strominger_galerkin_solve_spec_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    mesh = data["mesh_scaffold"]
    residual = data["residual_acceptance"]
    spectral = data["spectral_acceptance"]
    stages = data["execution_stages"]
    outputs = data["output_manifest"]
    open_items = data["what_remains_open"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_STROMINGER_GALERKIN_SOLVE_SPEC_BUILT_VALUES_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check(
            "superset executable spec",
            data["superset_mode"]["classification"] == "SUPERSET_REPAIR_EXECUTABLE_SPEC"
            and data["superset_mode"]["superset_repair"]["repair_object"]
            == "first selected small-N nonlinear residual solve or symbolic selected ansatz",
            data["superset_mode"],
        ),
        check(
            "no target fitting",
            data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False
            and data["superset_mode"]["diagnostic_backfit_only"]["used"] is False,
            data["superset_mode"]["diagnostic_backfit_only"],
        ),
        check(
            "mesh counts reproduced",
            mesh["matches_certificate_counts"] is True
            and mesh["counts"]["mesh_N"] == 1
            and mesh["counts"]["closed_cell_nodes"] == 64
            and mesh["counts"]["complex_rho_entries_table_ansatz"] == 1296,
            mesh,
        ),
        check(
            "residual contract complete",
            set(residual["residual_slots"].keys())
            == {
                "rho_cocycle",
                "metric_compatibility",
                "integrability_F02",
                "hym_primitive",
                "bianchi_alpha1",
                "strominger_residual",
                "mtt_gradient",
            }
            and set(residual["positive_gates"].keys()) == {"mtt_hessian_min_eigenvalue", "riesz_gap_min"},
            residual,
        ),
        check(
            "spectral contract complete",
            "eta_total" in spectral["error_budget"]
            and "epsilon_low" in spectral["pass_rule"]
            and "gamma_gap" in spectral["pass_rule"],
            spectral,
        ),
        check(
            "stage order",
            [stage["stage"] for stage in stages]
            == [
                "S0_selected_source",
                "S1_basis_and_domain",
                "S2_connection_metric_rhoE",
                "S3_sector_operators",
                "S4_spectral_projectors",
                "S5_alpha1_response",
                "S6_c1_contractions",
            ],
            stages,
        ),
        check(
            "output manifest complete",
            set(outputs.keys())
            == {
                "route_c_residual",
                "rhoE_mesh",
                "rhoE_metric",
                "sector_maps",
                "de_action",
                "riesz_gap",
                "reduced_green",
                "dotd_response",
                "spectral_galerkin_data",
                "c1_primitive_contractions",
            },
            outputs,
        ),
        check(
            "promotion guardrail linked",
            data["promotion_gate"]["must_pass_after_outputs_exist"] is True
            and Path(data["promotion_gate"]["script"]).exists(),
            data["promotion_gate"],
        ),
        check(
            "values still open",
            open_items["actual_selected_small_N_solve_or_symbolic_ansatz"] is True
            and open_items["selected_rhoE_metric_connection_values"] is True
            and open_items["zero_mode_bases_and_C1_primitives"] is True,
            open_items,
        ),
        check(
            "closure not claimed",
            cert["closure_claimed"] is False and cert["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
            cert,
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1"
            and cert["primary_next_artifact"] == data["next_required_artifact"],
            cert,
        ),
        check(
            "note records executable spec",
            "The selected Route-C/Strominger Galerkin solve is now an executable spec" in note
            and "Next artifact: `MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1`" in note,
            NOTE,
        ),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected Route-C/Strominger Galerkin solve spec audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
