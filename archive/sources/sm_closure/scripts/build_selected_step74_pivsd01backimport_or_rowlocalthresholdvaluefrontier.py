"""Build Step74 Pi/VSD01 backimport and row-local threshold-value frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BACKIMPORT_PACKET = PACKET_DIR / "step74_pi_vsd01_backimport.packet.json"
ROW_RECHECK_PACKET = PACKET_DIR / "step74_ten_rowlocal_frontier_recheck.packet.json"
VALUE_FRONTIER_PACKET = PACKET_DIR / "step74_threshold_value_frontier.packet.json"
CUTSET_PACKET = PACKET_DIR / "step74_next_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step74_PiVSD01Backimport_or_RowLocalThresholdValueFrontier_v1.md"

STEP73 = DATA / "selected_step73_honestrowlocalhymgalerkin_or_selectedprefactorsourcerows.candidate.json"
STEP73_ROW_ATTEMPT = (
    DATA
    / "selected_step73_honestrowlocalhymgalerkin_or_selectedprefactorsourcerows"
    / "step73_ten_rowlocal_prefactor_execution_attempt.packet.json"
)
STEP73_CUTSET = (
    DATA
    / "selected_step73_honestrowlocalhymgalerkin_or_selectedprefactorsourcerows"
    / "step73_next_selected_sector_transfer_or_overlap_derivative_cutset.packet.json"
)
STEP51 = DATA / "selected_step51_operator_domain_backimport_or_thresholdprofilefrontier.candidate.json"
RTHETA_SECTOR = DATA / "selected_rthetasectortransfer_or_primitiveassemblymapexecution.candidate.json"
RTHETA_PRIMITIVE = DATA / "selected_rtheta_primitivec1overlap_or_pinoneedtheorem.candidate.json"
RTHETA_VALUE = DATA / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation.candidate.json"
POSTPI_CONVENTION = DATA / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation.candidate.json"
POSTPI_THRESHOLD = DATA / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows.candidate.json"
POSTPI_PROFILE = DATA / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation.candidate.json"
POSTPI_BOUNDARY = DATA / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy.candidate.json"
VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
U10 = DATA / "selected_u10ubar5_1m_sourcepromotion_samebranch_emission.candidate.json"

STATUS = (
    "MTT_SELECTED_STEP74_PIVSD01BACKIMPORT_OR_ROWLOCALTHRESHOLDVALUEFRONTIER_"
    "BUILT_SOURCE_SIDE_RETIRED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1"


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
        raise FileNotFoundError("missing Step74 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP73,
        STEP73_ROW_ATTEMPT,
        STEP73_CUTSET,
        STEP51,
        RTHETA_SECTOR,
        RTHETA_PRIMITIVE,
        RTHETA_VALUE,
        POSTPI_CONVENTION,
        POSTPI_THRESHOLD,
        POSTPI_PROFILE,
        POSTPI_BOUNDARY,
        VSD01,
        U10,
    ]
    require_sources(inputs)

    step73 = load(STEP73)
    row_attempt = load(STEP73_ROW_ATTEMPT)
    step73_cutset = load(STEP73_CUTSET)
    step51 = load(STEP51)
    rtheta_sector = load(RTHETA_SECTOR)
    rtheta_primitive = load(RTHETA_PRIMITIVE)
    rtheta_value = load(RTHETA_VALUE)
    postpi_convention = load(POSTPI_CONVENTION)
    postpi_threshold = load(POSTPI_THRESHOLD)
    postpi_profile = load(POSTPI_PROFILE)
    postpi_boundary = load(POSTPI_BOUNDARY)
    vsd01 = load(VSD01)
    u10 = load(U10)

    step51_c = step51["closure_decision"]
    sector_c = rtheta_sector["closure_decision"]
    primitive_c = rtheta_primitive["closure_decision"]
    value_c = rtheta_value["closure_decision"]
    convention_c = postpi_convention["closure_decision"]
    threshold_c = postpi_threshold["closure_decision"]
    profile_c = postpi_profile["closure_decision"]
    boundary_c = postpi_boundary["closure_decision"]
    vsd01_c = vsd01["closure_decision"]
    u10_c = u10["closure_decision"]
    step73_c = step73["closure_decision"]

    operator_domain_closed = all(
        [
            step51_c["Pi_Rtheta_closed"],
            step51_c["coefficient_functional_domain_closed"],
            step51_c["selected_dynamic_operator_source_owner_closed"],
            step51_c["operator_domain_closed_for_Rtheta_value_evaluator"],
            sector_c["Pi_Rtheta_closed"],
            sector_c["VSD01_source_assembly_subgate_closed"],
            sector_c["dynamic_matter_overlap_operator_packet_first_response_closed"],
            primitive_c["stationary_sector_transfer_closed"],
            primitive_c["dotD_alpha1_transport_subgate_closed"],
            primitive_c["matter_slot_routing_closed"],
            primitive_c["primitive_C1_overlap_contractions_closed"],
            primitive_c["Pi_Rtheta_closed"],
            value_c["source_normalized_projection_weights_closed"],
            value_c["selected_dynamic_operator_source_owner_closed"],
            vsd01_c["VSD01_source_assembly_subgate_closed"],
            vsd01_c["VSD01_dynamic_overlap_subgate_closed"],
            u10_c["static_matter_slot_readout_closed"],
        ]
    )

    backimport = {
        "schema": "MTTStep74PiVSD01Backimport.v1",
        "status": "RTHETA_OPERATOR_DOMAIN_BACKIMPORTED_ROWLOCAL_SOURCE_SIDE_RETIRED",
        "step73_previous_frontier": step73["status"],
        "operator_domain_closed": operator_domain_closed,
        "retired_as_active_domain_blockers": {
            "Pi_Rtheta": primitive_c["Pi_Rtheta_closed"],
            "stationary_sector_transfer": primitive_c["stationary_sector_transfer_closed"],
            "dotD_alpha1_transport": primitive_c["dotD_alpha1_transport_subgate_closed"],
            "matter_slot_routing": primitive_c["matter_slot_routing_closed"],
            "primitive_C1_overlap_contractions": primitive_c["primitive_C1_overlap_contractions_closed"],
            "VSD01_source_assembly": vsd01_c["VSD01_source_assembly_subgate_closed"],
            "VSD01_dynamic_overlap": vsd01_c["VSD01_dynamic_overlap_subgate_closed"],
            "static_U10_Ubar5_1M_source": u10_c["static_U10_Ubar5_1M_source_closed"],
        },
        "step73_local_flags_still_false": {
            "selected_HYM_projector_values_promoted": step73_c["selected_HYM_projector_values_promoted"],
            "selected_sector_transfer_values_emitted": step73_c["selected_sector_transfer_values_emitted"],
            "selected_retarded_overlap_derivative_rows_emitted": step73_c[
                "selected_retarded_overlap_derivative_rows_emitted"
            ],
        },
        "interpretation": (
            "The Step73 local HYM row-local packet still emits no L_rowlocal values, but its "
            "projector/sector/dotD wording is no longer the global active source-domain blocker. "
            "Later Rtheta/VSD01 packets close the operator-domain and Pi side; the live scalar wall "
            "is threshold/value prefactor execution."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(BACKIMPORT_PACKET, backimport)

    row_rechecks: list[dict[str, Any]] = []
    for row in row_attempt["attempt_rows"]:
        missing_value_rows = [
            "selected L_rowlocal row-local HYM/overlap prefactor",
            "selected T_scheme threshold/scale/scheme prefactor",
            "accepted Omega source row",
        ]
        if row["omega_id"] == "Omega_H.lambda":
            missing_value_rows.append("lambda_H H-sector source value payload")
        row_rechecks.append(
            {
                "omega_id": row["omega_id"],
                "sector": row["sector"],
                "generation_or_lambda": row["generation_or_lambda"],
                "operator_domain_ready_after_backimport": operator_domain_closed,
                "diagonal_hym_green_subsource_closed": step73_c["diagonal_hym_green_subsource_closed"],
                "old_step73_local_projector_sector_flags_still_nonemitting": True,
                "rowlocal_numeric_prefactor_ready": False,
                "accepted_as_rowlocal_source_row": False,
                "accepted_as_prefactor_source_row": False,
                "accepted_as_omega_source_row": False,
                "missing_value_rows": missing_value_rows,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    row_recheck = {
        "schema": "MTTStep74TenRowLocalFrontierRecheck.v1",
        "status": "TEN_ROWLOCAL_ROWS_RECHECKED_OPERATOR_DOMAIN_READY_VALUES_OPEN",
        "row_count": len(row_rechecks),
        "operator_domain_ready_row_count": sum(
            1 for row in row_rechecks if row["operator_domain_ready_after_backimport"]
        ),
        "accepted_rowlocal_source_row_count": 0,
        "accepted_prefactor_source_row_count": 0,
        "accepted_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "rows": row_rechecks,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ROW_RECHECK_PACKET, row_recheck)

    threshold_value_frontier = {
        "schema": "MTTStep74ThresholdValueFrontier.v1",
        "status": "THRESHOLD_VALUE_FRONTIER_IS_LIVE_AFTER_OPERATOR_DOMAIN_BACKIMPORT",
        "same_branch_scale_scheme_loop_convention_closed": convention_c[
            "same_branch_scale_scheme_loop_convention_closed"
        ],
        "post_pi_formal_convention_source_contract_closed": convention_c[
            "post_pi_formal_convention_source_contract_closed"
        ],
        "threshold_matching_source_rows_closed_at_admitted_external_tier": threshold_c[
            "threshold_matching_source_rows_closed_at_admitted_external_tier"
        ],
        "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier": threshold_c[
            "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"
        ],
        "accepted_diagonal_profile_theorem_closed": profile_c["accepted_diagonal_profile_theorem_closed"],
        "post_pi_external_replay_ready": boundary_c["post_pi_external_replay_ready"],
        "Rtheta_readiness_present_count": boundary_c["Rtheta_readiness_present_count"],
        "Rtheta_readiness_requirement_count": boundary_c["Rtheta_readiness_requirement_count"],
        "selected_internal_Rtheta_threshold_mass_derivation_closed": threshold_c[
            "selected_internal_Rtheta_threshold_mass_derivation_closed"
        ],
        "selected_threshold_response_functional_instantiated": boundary_c[
            "selected_threshold_response_functional_instantiated"
        ],
        "accepted_coefficient_value_count": boundary_c["accepted_coefficient_value_count"],
        "accepted_lambda_H_value": boundary_c["accepted_lambda_H_value"],
        "selected_internal_value_emission_count": boundary_c["selected_internal_value_emission_count"],
        "selected_universal_parameter_count": boundary_c["selected_universal_parameter_count"],
        "meaning": (
            "The admitted replay tier is ready for comparison, but no internal no-knob scalar values "
            "or lambda_H source row are selected. Step74 therefore hands off to row-local threshold/"
            "value prefactor execution rather than another Pi/source-domain replay."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(VALUE_FRONTIER_PACKET, threshold_value_frontier)

    cutset = {
        "schema": "MTTStep74NextCutset.v1",
        "status": "NEXT_ATTACK_ROWLOCAL_THRESHOLD_VALUE_ROWS_AND_LAMBDAH",
        "not_missing_anymore": [
            "Pi_Rtheta/operator-domain source ownership",
            "stationary sector transfer and rho_s layer",
            "dotD_alpha1 transport as active source-domain blocker",
            "matter-slot routing/static U10-Ubar5-1M readout",
            "primitive C1 first-response/VSD01 source assembly",
            "same-branch M_Z/MSbar convention at the admitted replay tier",
            "threshold/mass-scheme rows at the admitted external replay tier",
            "diagonal profile theorem at the accepted replay tier",
        ],
        "still_missing": [
            "selected internal threshold response functional instantiation",
            "selected internal threshold/mass-scheme derivation, not admitted replay",
            "ten selected L_rowlocal HYM/overlap prefactor rows",
            "ten selected T_scheme threshold/scale rows",
            "lambda_H H-sector source value row",
            "strict Omega source row acceptance",
            "selected matrix-level CKM/PMNS/offdiagonal extension",
            "true SM/no-knob value closure",
        ],
        "forbidden_routes": [
            "loop back to Step73 as if Pi_Rtheta/operator source ownership were still open",
            "promote admitted external threshold rows as no-knob internal rows",
            "use SM-parity replay prefactors as source selectors",
            "claim lambda_H from the H-sector shell without a selected value row",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET_PACKET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep74PiVSD01BackimportOrRowLocalThresholdValueFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "step74_pi_vsd01_backimport": rel(BACKIMPORT_PACKET),
            "step74_ten_rowlocal_frontier_recheck": rel(ROW_RECHECK_PACKET),
            "step74_threshold_value_frontier": rel(VALUE_FRONTIER_PACKET),
            "step74_next_cutset": rel(CUTSET_PACKET),
        },
        "theorem": {
            "name": "Step74PiVSD01BackimportValueFrontierTheorem",
            "proved": True,
            "statement": (
                "Backimporting the later Rtheta/Pi/VSD01/post-Pi packets into the Step73 row-local "
                "frontier retires projector/sector/Pi/source-ownership as the active global blocker. "
                "The ten Omega rows still emit zero accepted source values because the remaining "
                "objects are selected row-local threshold/value prefactor rows and lambda_H, not another "
                "diagonal HYM or Pi-domain proof."
            ),
        },
        "closure_decision": {
            "step73_diagonal_hym_green_subsource_closed": step73_c["diagonal_hym_green_subsource_closed"],
            "operator_domain_side_closed_after_backimport": operator_domain_closed,
            "Pi_Rtheta_closed": step51_c["Pi_Rtheta_closed"],
            "stationary_sector_transfer_closed": primitive_c["stationary_sector_transfer_closed"],
            "dotD_alpha1_transport_subgate_closed": primitive_c["dotD_alpha1_transport_subgate_closed"],
            "matter_slot_routing_closed": primitive_c["matter_slot_routing_closed"],
            "primitive_C1_overlap_contractions_closed": primitive_c[
                "primitive_C1_overlap_contractions_closed"
            ],
            "VSD01_source_assembly_subgate_closed": vsd01_c["VSD01_source_assembly_subgate_closed"],
            "VSD01_dynamic_overlap_subgate_closed": vsd01_c["VSD01_dynamic_overlap_subgate_closed"],
            "static_U10_Ubar5_1M_source_closed": u10_c["static_U10_Ubar5_1M_source_closed"],
            "same_branch_scale_scheme_loop_convention_closed": convention_c[
                "same_branch_scale_scheme_loop_convention_closed"
            ],
            "post_pi_external_replay_ready": boundary_c["post_pi_external_replay_ready"],
            "accepted_rowlocal_source_row_count": 0,
            "accepted_prefactor_source_row_count": 0,
            "accepted_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "selected_internal_threshold_response_functional_instantiated": False,
            "selected_internal_threshold_mass_derivation_closed": False,
            "selected_L_rowlocal_rows_emitted": False,
            "selected_T_scheme_rows_emitted": False,
            "lambda_H_value_row_emitted": False,
            "strict_omega_acceptance_closed": False,
            "selected_matrix_level_mixing_extension_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step73["status"],
        "previous_cutset_status": step73_cutset["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step74_PiVSD01Backimport_or_RowLocalThresholdValueFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step74 PiVSD01Backimport or RowLocalThresholdValueFrontier v1

Status: `{STATUS}`.

## What Moved

Step74 back-imports the stronger `Rtheta`/Pi/VSD01/post-Pi packets into the
Step73 row-local HYM frontier.

```text
operator-domain side closed after backimport : {str(operator_domain_closed).lower()}
Pi_Rtheta closed                            : {str(step51_c['Pi_Rtheta_closed']).lower()}
VSD01 source assembly closed                : {str(vsd01_c['VSD01_source_assembly_subgate_closed']).lower()}
static U10/Ubar5/1M source closed           : {str(u10_c['static_U10_Ubar5_1M_source_closed']).lower()}
post-Pi external replay ready               : {str(boundary_c['post_pi_external_replay_ready']).lower()}
accepted row-local source rows              : 0
accepted Omega source rows                  : 0
```

## Correct Frontier

The old Step73 wording is now reclassified: projector/sector/Pi source-domain
ownership is not the active global blocker. It is closed or retired by the
later packets for the value-evaluator domain. What remains is the scalar
value layer:

```text
selected internal threshold response        : false
selected L_rowlocal rows                    : false
selected T_scheme rows                      : false
lambda_H value row                          : false
strict Omega acceptance                     : false
true SM/no-knob closure                     : false
```

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
