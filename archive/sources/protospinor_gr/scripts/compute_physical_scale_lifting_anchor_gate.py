from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

BRIDGE_CERT = ROOT / "certificates" / "absolute_normalization_bridge_from_nonsm_certificate.json"
FINAL_RHO_CERT = NONSM / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
HORIZONTAL_CERT = NONSM / "certificates" / "selected_horizontal_scale_law_certificate.json"
CHAR_COV_CERT = NONSM / "certificates" / "selected_character_channel_covariance_closure_certificate.json"
PHYSICAL_ACTION_CERT = NONSM / "certificates" / "physical_action_normalization_gate_certificate.json"
DIM_OBSTRUCTION_CERT = NONSM / "certificates" / "dimensionful_constant_obstruction_certificate.json"

OUT_CERT = ROOT / "certificates" / "physical_scale_lifting_anchor_gate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    bridge = load_json(BRIDGE_CERT)
    final_rho = load_json(FINAL_RHO_CERT)
    horizontal = load_json(HORIZONTAL_CERT)
    char_cov = load_json(CHAR_COV_CERT)
    physical_action = load_json(PHYSICAL_ACTION_CERT)
    dim_obstruction = load_json(DIM_OBSTRUCTION_CERT)

    rho_values = final_rho["selected_values"]
    internal_branch_closed = final_rho["verdict"]["internal_no_knob_branch_closed"]
    character_cov_closed = char_cov["verdict"]["character_channel_covariance_closed"]
    selected_scale_law_closed = horizontal["closed"]["scale_law_selected"]
    physical_anchor_closed = physical_action["verdict"]["physical_absolute_dimensionful_predictions_closed"]
    no_go_without_anchor = physical_action["verdict"]["no_go_without_external_dimensional_anchor"]

    # The internal scale-lifting value is dimensionless. It can rescale internal
    # branch units but cannot by itself map those units to SI Newton/Planck units.
    internal_scale_lift_closed = internal_branch_closed and character_cov_closed and selected_scale_law_closed
    physical_scale_lift_closed = internal_scale_lift_closed and physical_anchor_closed

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "physical_scale_lifting_anchor_gate",
        "status": "INTERNAL_SCALE_LIFT_IMPORTED_PHYSICAL_DIMENSIONAL_ANCHOR_STILL_OPEN",
        "input_certificates": {
            "absolute_normalization_bridge": str(BRIDGE_CERT),
            "final_internal_rho_uv": str(FINAL_RHO_CERT),
            "selected_horizontal_scale_law": str(HORIZONTAL_CERT),
            "selected_character_channel_covariance": str(CHAR_COV_CERT),
            "physical_action_normalization": str(PHYSICAL_ACTION_CERT),
            "dimensionful_obstruction": str(DIM_OBSTRUCTION_CERT),
        },
        "imported_internal_scale_lift": {
            "R_star": rho_values["R_star"],
            "r3": rho_values["r3"],
            "v1_tilde": rho_values["v1_tilde"],
            "rho_UV": rho_values["rho_UV"],
            "s_star_from_rho": rho_values["s_star_from_rho"],
            "scale_law": final_rho["selected_branch"]["scale_law"],
            "character_channel_covariance_premise": char_cov["identification_premise"],
        },
        "closed_tests": {
            "selected_character_channel_covariance_closed": character_cov_closed,
            "selected_horizontal_scale_law_closed": selected_scale_law_closed,
            "internal_rho_uv_branch_closed": internal_branch_closed,
            "internal_scale_lifting_number_available": internal_scale_lift_closed,
            "GR_internal_normalization_already_closed": bridge["guardrails"][
                "claims_internal_dimensionless_normalization_closure"
            ],
            "GR_kappa_not_independent": bridge["relation_to_current_GR_branch"]["kappa_not_independent"],
        },
        "open_tests": {
            "physical_absolute_dimensionful_anchor_closed": physical_anchor_closed,
            "internal_to_SI_unit_map_selected": False,
            "measured_G_N_predicted_without_G_N_input": False,
            "measured_M_Pl_predicted_without_M_Pl_input": False,
            "physical_scale_lift_closed": physical_scale_lift_closed,
        },
        "dimensional_analysis": {
            "why_internal_rho_does_not_predict_GN": (
                "rho_UV and s_star are dimensionless internal branch quantities. "
                "They select a scale inside normalized MTT action units, but do not "
                "supply the conversion from those units to SI length/mass/action units."
            ),
            "what_would_close_physical_units": [
                "a target-independent dimensional anchor selected by MTT",
                "or a theorem that the normalized action unit is physically fixed by an observable not being predicted",
                "or a reformulation that makes only dimensionless ratios the claimed outputs",
            ],
        },
        "verdict": {
            "what_is_now_carried_home": (
                "The internal scale-lifting branch is imported into the GR normalization "
                "program: internal rho_UV, R_star, and s_star are available without target data."
            ),
            "what_remains": dim_obstruction["verdict"]["next_required_object"],
            "physical_absolute_prediction_closed": physical_scale_lift_closed,
            "no_backsolve_guard_active": no_go_without_anchor,
            "next_allowed_artifact": "Target_Independent_Dimensional_Anchor_Candidate_v1",
        },
        "guardrails": {
            "claims_internal_scale_lift_closed": internal_scale_lift_closed,
            "claims_physical_Newton_prediction": False,
            "claims_physical_Planck_prediction": False,
            "claims_dimensionful_anchor_closed": False,
            "forbids_observed_GN_backsolve": True,
            "forbids_observed_MPl_backsolve": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
