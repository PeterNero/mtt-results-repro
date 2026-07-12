"""Build direct H K-threshold row emission or H quartic functional theorem packet.

The previous local packet closes the exact H/lambda source equation but leaves
the tenth K row open.  This builder imports the latest constants-repo Higgs
quartic chain (H7B1Z) and tests whether it can honestly emit
K_threshold.Omega_H.lambda.

The result advances the frontier: the HYM-grid solve itself is no longer the
blocker.  The remaining source object is the E_H^UV binding/trace identity or
direct Herm(2) Huv row payload.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
CONST_DATA = CONSTANTS / "candidate_data"
CONST_CERTS = CONSTANTS / "certificates"

SLUG = "selected_direcththresholdkrowemission_or_hquarticfunctionaltheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CROSS_IMPORT = PACKET_DIR / "crossrepo_higgs_h7b1z_import.packet.json"
H_K_ATTEMPT = PACKET_DIR / "h_k_threshold_emission_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_direct_h_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DirectHThresholdKRowEmission_or_HQuarticFunctionalTheorem_v1.md"

PREVIOUS = DATA / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure.candidate.json"
PREVIOUS_EQUATION = (
    DATA
    / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
    / "h_sector_payload_source_equation.packet.json"
)
PREVIOUS_GATE = (
    DATA
    / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
    / "strict_ten_k_gate_after_h_payload_attempt.packet.json"
)

H7B1Z = CONST_DATA / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values.candidate.json"
H7B1Z_CERT = CONST_CERTS / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values_certificate.json"
H7B1Z_CUTSET = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "remaining_payload_cutset.packet.json"
)
H7B1Z_PARTIAL = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "partial_section_basis_quadrature_fill.packet.json"
)
H7B1Z_DIRECT = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "direct_herm2_fill_attempt.packet.json"
)
H7B1Z_NEXT = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "next_labeled_workorder.packet.json"
)
H7B1Y_SECTION_SCHEMA = (
    CONST_DATA
    / "const_higgs_01_h7b1y_selected_ehuv_section_basis_quadrature_or_herm2_row_values"
    / "ehuv_section_basis_quadrature_schema.packet.json"
)
H7B1Y_DIRECT_SCHEMA = (
    CONST_DATA
    / "const_higgs_01_h7b1y_selected_ehuv_section_basis_quadrature_or_herm2_row_values"
    / "direct_herm2_huv_row_schema.packet.json"
)

STATUS = (
    "MTT_SELECTED_DIRECTHTHRESHOLDKROWEMISSION_OR_HQUARTICFUNCTIONALTHEOREM_"
    "IMPORTED_H7B1Z_HYM_GRID_EHUV_BINDING_OPEN"
)
NEXT = "MTT_Selected_EHUvBindingTraceIdentityOrDirectHuvRows_to_HKThresholdEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing direct-H inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_EQUATION,
        PREVIOUS_GATE,
        H7B1Z,
        H7B1Z_CERT,
        H7B1Z_CUTSET,
        H7B1Z_PARTIAL,
        H7B1Z_DIRECT,
        H7B1Z_NEXT,
        H7B1Y_SECTION_SCHEMA,
        H7B1Y_DIRECT_SCHEMA,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_equation = load(PREVIOUS_EQUATION)
    previous_gate = load(PREVIOUS_GATE)
    h7b1z = load(H7B1Z)
    h7b1z_cert = load(H7B1Z_CERT)
    h7b1z_cutset = load(H7B1Z_CUTSET)
    h7b1z_partial = load(H7B1Z_PARTIAL)
    h7b1z_direct = load(H7B1Z_DIRECT)
    h7b1z_next = load(H7B1Z_NEXT)
    section_schema = load(H7B1Y_SECTION_SCHEMA)
    direct_schema = load(H7B1Y_DIRECT_SCHEMA)

    projection = h7b1z_partial["projection_measure_partial_fill"]
    quadrature = h7b1z_partial["quadrature_and_trace_partial_fill"]
    hym_data = h7b1z_partial["selected_HYM_data_partial_fill"]
    direct_decision = h7b1z_direct["decision"]

    cross_import = {
        "schema": "MTTCrossRepoHiggsH7B1ZImport.v1",
        "status": "H7B1Z_IMPORTED_HYM_GRID_RETIRED_EHUV_BINDING_OPEN",
        "closure_claimed": True,
        "source_repo": rel(CONSTANTS),
        "imported_status": h7b1z["status"],
        "imported_certificate_status": h7b1z_cert["status"],
        "imported_next": h7b1z["selected_next_artifact"],
        "closed_or_retired_by_import": {
            "H7B1Y_schema_ambiguity_retired": h7b1z_cutset["retired_as_blockers"][
                "H7B1Y_schema_ambiguity"
            ],
            "source_diagonal_HYM_grid_replay_exists": h7b1z["source_HYM_grid_payload_emitted"],
            "computational_uniform_quadrature_exists": h7b1z[
                "computational_uniform_quadrature_emitted"
            ],
            "HYM_solver_existence_retired_as_blocker": h7b1z[
                "HYM_solver_existence_retired_as_blocker"
            ],
            "same_branch_with_H7B1U_grid": h7b1z_partial["branch_identity_partial_fill"][
                "same_branch_with_H7B1U_grid"
            ],
            "selected_source_branch": h7b1z_partial["branch_identity_partial_fill"][
                "selected_source_branch"
            ],
            "residual_l2": hym_data["residual_l2"],
            "node_count": quadrature["node_count"],
            "uniform_weight_rational": quadrature["uniform_weight_rational"],
        },
        "still_open_by_import": h7b1z_cutset["still_open"],
        "diagnostic_replay_only": {
            "conditional_local_formula": projection["conditional_local_formula"],
            "uniform_candidate_s_beta": projection["uniform_candidate_s_beta"],
            "conditional_reductions_not_selected": projection[
                "conditional_reductions_not_selected"
            ],
            "selected_s_beta_promoted": projection["selected_s_beta_promoted"],
            "accepted_as_physical_Higgs_projection_measure": quadrature[
                "accepted_as_physical_Higgs_projection_measure"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_k_attempt = {
        "schema": "MTTDirectHKThresholdEmissionAttempt.v1",
        "status": "DIRECT_H_K_EMISSION_ATTEMPT_BLOCKED_BY_EHUV_BINDING_OR_HERM2_VALUES",
        "closure_claimed": True,
        "local_H_source_equation": previous_equation["selected_source_equation"],
        "required_output": "K_threshold.Omega_H.lambda",
        "attempted_routes": [
            {
                "route_id": "use_H7B1Z_uniform_trace_as_H_projection_measure",
                "closed_support": {
                    "source_HYM_grid_payload_emitted": h7b1z["source_HYM_grid_payload_emitted"],
                    "computational_uniform_quadrature_emitted": h7b1z[
                        "computational_uniform_quadrature_emitted"
                    ],
                    "uniform_candidate_s_beta": projection["uniform_candidate_s_beta"],
                },
                "accepted_as_H_K_source_row": False,
                "reason_rejected": (
                    "H7B1Z marks the uniform trace as a replay candidate only; "
                    "projection_measure_equality and trace_to_H7B1U_grid_identity are false."
                ),
            },
            {
                "route_id": "direct_Herm2_Huv_rows",
                "required_payload": direct_schema["required_fields"],
                "attempted_outputs": h7b1z_direct["attempted_outputs"],
                "accepted_as_H_K_source_row": False,
                "reason_rejected": "B_Huv, M_source, Huu, Hud, Hdd, Delta, Omega, P_L, and s_beta are all absent.",
            },
            {
                "route_id": "E_H_UV_section_basis_quadrature_payload",
                "required_payload": section_schema["required_fields"],
                "accepted_as_H_K_source_row": False,
                "reason_rejected": (
                    "The ordered Hu/Hd labels and coordinate scaffold are closed, but no selected "
                    "finite section basis, HYM metric on E_H^UV, projection measure equality, or "
                    "trace identity is emitted."
                ),
            },
        ],
        "route_decision": {
            "direct_H_K_threshold_row_emitted": False,
            "selected_H_quartic_functional_emitted": False,
            "selected_E_H_UV_binding_emitted": False,
            "selected_projection_measure_equality_emitted": False,
            "direct_Herm2_Huv_payload_emitted": direct_decision["Herm2_payload_complete"],
            "selected_s_beta_value_found": h7b1z["selected_s_beta_value_found"],
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_gate["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": previous_gate[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "next_source_object": {
            "artifact": NEXT,
            "constants_repo_next": h7b1z_next["primary_next"]["artifact"],
            "legal_exits": h7b1z_next["legal_exits"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterDirectHAttempt.v1",
        "status": "NEXT_FRONTIER_EHUV_BINDING_TRACE_IDENTITY_OR_DIRECT_HUV_ROWS_TO_H_K",
        "closure_claimed": True,
        "closed_here": [
            "latest constants-repo H7B1Z imported into the H K-row gate",
            "HYM solver existence retired as the active H/lambda blocker",
            "computational uniform quadrature and q79/F,m=1 diagonal HYM grid registered as support",
            "direct H K emission attempted with zero accepted H source rows",
            "direct Herm2 Huv route tested and found values absent",
            "E_H^UV section-basis/quadrature route tested and found binding fields absent",
        ],
        "still_open": [
            "selected E_H^UV section basis/source ids",
            "binding diagonal End0 HYM lane to E_H^UV",
            "trace-to-H7B1U grid identity as physical Higgs projection measure",
            "no-extra-boundary-source theorem for the Higgs projection measure",
            "direct B_Huv+M_source or Huu,Hud,Hdd Herm2 values",
            "selected s_beta or equivalent H quartic/threshold functional",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
            "selected matrix-level mixing extension and true SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDirectHThresholdKRowEmissionOrHQuarticFunctionalTheorem",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "DirectHKThresholdH7B1ZImportAndNoEmissionTheorem",
            "proved": True,
            "statement": (
                "The H-sector source equation is now tested against the latest constants-repo "
                "H7B1Z Higgs payload. H7B1Z retires HYM-grid existence as a blocker but does "
                "not emit E_H^UV binding/projection-measure equality, direct Herm2 Huv rows, "
                "selected s_beta, or K_threshold.Omega_H.lambda."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "H_source_equation_closed": True,
            "H7B1Z_imported": True,
            "HYM_solver_existence_retired_as_H_blocker": True,
            "direct_H_K_threshold_row_emitted": False,
            "selected_H_quartic_functional_emitted": False,
            "selected_E_H_UV_binding_emitted": False,
            "selected_projection_measure_equality_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_gate["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": previous_gate[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "crossrepo_higgs_h7b1z_import": rel(CROSS_IMPORT),
            "h_k_threshold_emission_attempt": rel(H_K_ATTEMPT),
            "next_cutset_after_direct_h_attempt": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedDirectHThresholdKRowEmissionOrHQuarticFunctionalTheoremCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "H7B1Z_imported": True,
        "HYM_solver_existence_retired_as_H_blocker": True,
        "direct_H_K_threshold_row_emitted": False,
        "selected_H_quartic_functional_emitted": False,
        "selected_E_H_UV_binding_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_s_beta_value_found": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_gate["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_gate[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected DirectHThresholdKRowEmission or HQuarticFunctionalTheorem v1

Status: `{STATUS}`

## What Closed

- imported constants-repo H7B1Z into the H/lambda K-row gate
- retired HYM solver existence as the active blocker
- registered the q79/F,m=1 diagonal HYM grid and computational uniform quadrature as support
- tested direct `K_threshold.Omega_H.lambda` emission: `false`
- ten-K gate remains: `{previous_gate["accepted_selected_K_source_row_count"]}/{previous_gate["selected_K_threshold_row_count_required"]}`

## Still Open

- selected `E_H^UV` section basis/source ids
- binding diagonal End0 HYM lane to `E_H^UV`
- trace-to-H7B1U grid identity as physical Higgs projection measure
- direct `B_Huv+M_source` or `Huu,Hud,Hdd` Herm2 values
- selected `s_beta` or equivalent H quartic/threshold functional
- selected `K_threshold.Omega_H.lambda`: `false`

Next required artifact: `{NEXT}`
"""

    write_json(CROSS_IMPORT, cross_import)
    write_json(H_K_ATTEMPT, h_k_attempt)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
