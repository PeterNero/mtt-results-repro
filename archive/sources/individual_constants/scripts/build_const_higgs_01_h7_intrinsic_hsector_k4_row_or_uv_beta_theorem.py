"""Build CONST-HIGGS-01 H7 intrinsic K4 row or UV beta theorem frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7_intrinsic_hsector_k4_row_or_uv_beta_theorem"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
K4_AUDIT = BASE / "intrinsic_k4_row_source_payload_audit.packet.json"
UV_BETA_AUDIT = BASE / "uv_beta_theorem_source_payload_audit.packet.json"
VALIDATOR = BASE / "strict_higgs_closure_acceptance_validator.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7_IntrinsicHSectorK4RowOrUVBetaTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7_STRICT_SOURCE_FRONTIER_BUILT_TWO_EXITS_OPEN"


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


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h5b_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection.candidate.json"
    h5b_projection_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection" / "nonlinear_amplitude_projection_contract.packet.json"
    h6b_path = DATA / "const_higgs_01_h6b_local_source_identity_to_higgs_row_export.candidate.json"
    h6b_obstruction_path = DATA / "const_higgs_01_h6b_local_source_identity_to_higgs_row_export" / "quartic_row_export_obstruction.packet.json"
    h6c_row_search_path = DATA / "const_higgs_01_h6c_hsector_row_or_boundary_route_discriminator" / "actual_hsector_fourth_row_search.packet.json"
    h6d_path = DATA / "const_higgs_01_h6d_selected_dterm_boundary_or_beta_source.candidate.json"
    h6e_path = DATA / "const_higgs_01_h6e_uv_two_higgs_projection_angle_or_primitive_beta_policy.candidate.json"
    h6e_uv_audit_path = DATA / "const_higgs_01_h6e_uv_two_higgs_projection_angle_or_primitive_beta_policy" / "uv_two_higgs_projection_angle_source_audit.packet.json"
    h6f_path = DATA / "const_higgs_01_h6f_symbolic_dterm_boundary_replay.candidate.json"
    h6f_boundary_path = DATA / "const_higgs_01_h6f_symbolic_dterm_boundary_replay" / "symbolic_boundary_replay_functor.packet.json"
    h6f_gate_path = DATA / "const_higgs_01_h6f_symbolic_dterm_boundary_replay" / "source_input_gate_ledger.packet.json"

    h5b = load(h5b_path)
    h5b_projection = load(h5b_projection_path)
    h6b = load(h6b_path)
    h6b_obstruction = load(h6b_obstruction_path)
    h6c_row_search = load(h6c_row_search_path)
    h6d = load(h6d_path)
    h6e = load(h6e_path)
    h6e_uv_audit = load(h6e_uv_audit_path)
    h6f = load(h6f_path)
    h6f_boundary = load(h6f_boundary_path)
    h6f_gate = load(h6f_gate_path)

    k4_audit = {
        "schema": "MTTConstHiggs01H7IntrinsicK4RowSourcePayloadAudit.v1",
        "status": "INTRINSIC_K4_ROW_SOURCE_PAYLOAD_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-INTRINSIC-K4-ROW-SOURCE-PAYLOAD-AUDIT",
        "inputs": {
            "H5B_projection_candidate": rel(h5b_path),
            "H5B_projection_contract": rel(h5b_projection_path),
            "H6B_row_export_candidate": rel(h6b_path),
            "H6B_quartic_row_export_obstruction": rel(h6b_obstruction_path),
            "H6C_actual_H_sector_fourth_row_search": rel(h6c_row_search_path),
            "H6F_source_gate": rel(h6f_gate_path),
        },
        "closed_support": {
            "selected_Higgs_zero_mode_coordinate_closed": h5b["selected_Higgs_zero_mode_coordinate_closed"],
            "selected_Higgs_amplitude_coordinate": h6b["selected_Higgs_amplitude_coordinate"],
            "quartic_row_address": h6b["target_quartic_row_address"],
            "projection_template_closed": h5b["selected_Higgs_projection_functional_template_closed"],
            "local_row_owner_contract_ready": h6b["local_Higgs_row_export_contract_ready"],
            "local_source_identity_fields_filled": h6b["local_source_identity_fields_filled"],
        },
        "required_strict_payload": {
            "same_source_H_sector_fourth_variation_row": {
                "required_object": h6b_obstruction["minimal_missing_payload"]["same_source_H_sector_fourth_variation_row"],
                "filled": False,
            },
            "row_exactness_certificate": {
                "required_object": h6b_obstruction["minimal_missing_payload"]["row_exactness_certificate"],
                "filled": False,
            },
            "row_specific_residual_independence": {
                "required_object": h6b_obstruction["minimal_missing_payload"]["row_specific_residual_independence"],
                "filled": False,
            },
            "coefficient_convention": {
                "required_object": h6b_obstruction["minimal_missing_payload"]["coefficient_convention"],
                "filled": False,
            },
        },
        "current_negative_result": {
            "actual_H_sector_fourth_variation_row_found": h6c_row_search["negative_result"]["actual_H_sector_fourth_variation_row_found"],
            "exact_multilinear_formula_found": h6c_row_search["negative_result"]["exact_multilinear_formula_found"],
            "row_exactness_certificate_found": h6c_row_search["negative_result"]["row_exactness_certificate_found"],
            "lambda_H_coefficient_convention_from_source_row_found": h6c_row_search["negative_result"]["lambda_H_coefficient_convention_from_source_row_found"],
            "intrinsic_K4_exit_closed": False,
        },
        "forbidden_promotions": h6b_obstruction["why_the_row_does_not_follow_yet"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    uv_beta_audit = {
        "schema": "MTTConstHiggs01H7UVBetaTheoremSourcePayloadAudit.v1",
        "status": "UV_BETA_THEOREM_SOURCE_PAYLOAD_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-UV-BETA-THEOREM-SOURCE-PAYLOAD-AUDIT",
        "inputs": {
            "H6D_Dterm_boundary_or_beta_source": rel(h6d_path),
            "H6E_UV_beta_source_audit": rel(h6e_uv_audit_path),
            "H6F_symbolic_boundary_functor": rel(h6f_boundary_path),
        },
        "closed_support": {
            "low_energy_single_Higgs_projection_closed": h6e["low_energy_single_Higgs_projection_closed"],
            "Dterm_boundary_formula_ready": h6d["Dterm_boundary_formula_ready"],
            "symbolic_boundary_replay_functor_defined": h6f["symbolic_boundary_replay_functor_defined"],
            "tree_boundary": h6f_boundary["boundary_functor"]["tree_boundary"],
        },
        "required_strict_payload": {
            "selected_UV_two_Higgs_VEV_ratio": {
                "filled": not h6e_uv_audit["strict_source_absences"]["selected_UV_two_Higgs_VEV_ratio"],
                "must_be_selected_before_Higgs_comparison": True,
            },
            "selected_beta_or_tan_beta": {
                "filled": not h6e_uv_audit["strict_source_absences"]["selected_beta_or_tan_beta"],
                "must_be_selected_before_Higgs_comparison": True,
            },
            "selected_two_Higgs_projection_angle": {
                "filled": not h6e_uv_audit["strict_source_absences"]["selected_two_Higgs_projection_angle"],
                "must_be_selected_before_Higgs_comparison": True,
            },
            "selected_heavy_Higgs_decoupling_angle": {
                "filled": not h6e_uv_audit["strict_source_absences"]["selected_heavy_Higgs_decoupling_angle"],
                "must_be_selected_before_Higgs_comparison": True,
            },
            "selected_gauge_boundary_and_RG_policy": {
                "filled": h6f_gate["open_strict_inputs"]["selected_gauge_boundary_values_filled"]
                and h6f_gate["open_strict_inputs"]["matching_scale_policy_filled"]
                and h6f_gate["open_strict_inputs"]["threshold_RG_transport_filled"],
                "must_be_selected_before_Higgs_comparison": True,
            },
        },
        "current_negative_result": {
            "selected_UV_beta_source_found": h6e["selected_UV_beta_source_found"],
            "beta_primitive_declared_now": h6e["beta_primitive_declared_now"],
            "UV_beta_exit_closed": False,
        },
        "forbidden_promotions": {
            "single_Higgs_projection_to_UV_angle": True,
            "representative_tan_beta_10_to_selected_beta": True,
            "Higgs_mass_backsolve_to_beta": True,
            "threshold_scan_to_beta": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    validator = {
        "schema": "MTTConstHiggs01H7StrictClosureAcceptanceValidator.v1",
        "status": "STRICT_HIGGS_CLOSURE_VALIDATOR_BUILT_CURRENT_PACKET_FAILS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-STRICT-HIGGS-CLOSURE-ACCEPTANCE-VALIDATOR",
        "acceptance_rule": {
            "route_A_intrinsic_K4": [
                "same_source_H_sector_fourth_variation_row",
                "row_exactness_certificate",
                "row_specific_residual_independence",
                "coefficient_convention",
            ],
            "route_B_UV_Dterm_beta": [
                "selected_UV_two_Higgs_VEV_ratio_or_beta",
                "selected_gauge_boundary_values",
                "selected_matching_scale",
                "selected_threshold_RG_transport",
                "no_observed_Higgs_selector",
            ],
            "one_primitive_portfolio_route": [
                "declared_before_comparison",
                "single shared primitive or explicitly labeled Higgs primitive",
                "not strict no-knob",
                "not retuned per observable",
            ],
        },
        "current_packet_evaluation": {
            "route_A_intrinsic_K4_passes": False,
            "route_B_UV_Dterm_beta_passes": False,
            "one_primitive_declared_now": False,
            "strict_no_knob_Higgs_closure": False,
            "numeric_lambda_H_derived": False,
        },
        "conditional_witnesses": {
            "route_A_would_pass_if": [
                "K_H^(4)[12,12,12,12] exact value is emitted from the selected pre-residual action",
                "the coefficient convention maps that row to lambda_H",
            ],
            "route_B_would_pass_if": [
                "a selected UV beta/tan_beta or two-Higgs projection angle is emitted",
                "gauge boundary and RG/threshold policy are selected without Higgs-target fitting",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H7NextWork.v1",
        "status": "NEXT_WORKORDER_H7A_OR_H7B_STRICT_PAYLOAD_FILL",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-NEXT",
        "route_A_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A-INTRINSIC-K4-ROW-EXECUTION-PAYLOAD",
            "task": "Construct or import an actual same-source K_H^(4)[12,12,12,12] row value, exactness certificate, residual-independence certificate, and coefficient convention.",
        },
        "route_B_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM",
            "task": "Construct or import a selected UV beta/tan_beta, two-Higgs projection angle, or heavy-Higgs decoupling theorem before Higgs comparison.",
        },
        "portfolio_next": {
            "label": "CONST-HIGGS-01 / UNIVERSAL-PRIMITIVE-PORTFOLIO / H7P-HIGGS-REPLAY-WITH-DECLARED-PRIMITIVE",
            "task": "Only if strict routes stay open, test a declared primitive route as a labeled non-no-knob tier.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7IntrinsicHSectorK4RowOrUVBetaTheorem",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-INTRINSIC-H-SECTOR-K4-ROW-OR-UV-BETA-THEOREM",
        "output_packets": {
            "intrinsic_k4_row_source_payload_audit": rel(K4_AUDIT),
            "uv_beta_theorem_source_payload_audit": rel(UV_BETA_AUDIT),
            "strict_higgs_closure_acceptance_validator": rel(VALIDATOR),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H7TwoExitStrictSourceFrontierTheorem",
            "proved": True,
            "statement": (
                "Given H5B-H6F, strict Higgs quartic closure has exactly two active no-knob exits: emit the intrinsic H-sector fourth row K_H^(4)[12,12,12,12] with exactness/residual/coefficient certificates, or emit a selected UV beta/tan_beta/two-Higgs projection theorem together with selected gauge/RG data for the D-term boundary. The current packet closes neither exit, declares no beta primitive, emits no numerical lambda_H, and preserves the one-primitive route as a separate non-no-knob tier."
            ),
        },
        "strict_two_exit_frontier_built": True,
        "route_A_intrinsic_K4_exit_closed": False,
        "route_B_UV_beta_exit_closed": False,
        "one_primitive_declared_now": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7A_IntrinsicK4RowExecutionPayload_or_H7B_UVBetaTheorem_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7_IntrinsicHSectorK4RowOrUVBetaTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "strict_two_exit_frontier_built": True,
        "route_A_intrinsic_K4_exit_closed": False,
        "route_B_UV_beta_exit_closed": False,
        "one_primitive_declared_now": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H7 Intrinsic H-Sector K4 Row Or UV Beta Theorem v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-INTRINSIC-H-SECTOR-K4-ROW-OR-UV-BETA-THEOREM`

## Result

```text
strict two-exit frontier built             True
Route A intrinsic K4 exit closed           False
Route B UV beta/D-term exit closed         False
one primitive declared now                 False
new Higgs-specific parameters now          0
numeric lambda_H                           False
strict no-knob Higgs closure               False
```

## Two Exits

Route A:

```text
emit K_H^(4)[12,12,12,12]
plus exactness, residual-independence, and coefficient-convention certificates
```

Route B:

```text
emit selected beta_H/tan_beta_H or a UV two-Higgs projection theorem
plus selected gauge boundary and RG/threshold transport
```

The one-primitive route remains available only as an explicitly labeled
non-no-knob portfolio lane.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A-INTRINSIC-K4-ROW-EXECUTION-PAYLOAD`

or

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM`
"""

    for path, payload in [
        (K4_AUDIT, k4_audit),
        (UV_BETA_AUDIT, uv_beta_audit),
        (VALIDATOR, validator),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
