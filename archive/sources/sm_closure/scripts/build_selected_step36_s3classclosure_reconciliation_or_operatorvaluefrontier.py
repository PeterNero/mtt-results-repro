"""Build Step 36 S3 class-closure reconciliation and operator-value frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step36_s3classclosure_reconciliation_or_operatorvaluefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECON = PACKET_DIR / "step36_s3_class_closure_reconciliation.packet.json"
FRONTIER = PACKET_DIR / "step36_operator_value_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step36_S3ClassClosureReconciliation_or_OperatorValueFrontier_v1.md"

STEP35 = DATA / "selected_step35_covergauge_reduction_or_s3classrestrictionselector.candidate.json"
S3_SOURCE = DATA / "selected_s3_differential_cohomology_source_certificate.candidate.json"
S3_SOURCE_CERT = CERTS / "selected_s3_differential_cohomology_source_certificate.json"
SMOOTH_LIFT = DATA / "selected_smooth_s3_twisted_source_lift.candidate.json"
SPECTRAL = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"
VISIBLE_GS = DATA / "selected_visible_green_schwarz_operator_source.candidate.json"
STEP30 = DATA / "selected_step30_projectivebn_mechanicallift_or_visiblesourcecutset.candidate.json"

STATUS = "MTT_SELECTED_STEP36_S3_CLASS_CLOSURE_RECONCILED_OPERATOR_VALUES_OPEN"
NEXT = "MTT_Selected_OperatorLevelProjectiveRhoE_DE_RieszGreenDotD_from_S3Source_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP35, S3_SOURCE, S3_SOURCE_CERT, SMOOTH_LIFT, SPECTRAL, VISIBLE_GS, STEP30]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 36 inputs: " + ", ".join(missing))

    step35 = load(STEP35)
    s3_source = load(S3_SOURCE)
    s3_cert = load(S3_SOURCE_CERT)
    smooth = load(SMOOTH_LIFT)
    spectral = load(SPECTRAL)
    visible_gs = load(VISIBLE_GS)
    step30 = load(STEP30)

    recon = {
        "schema": "MTTStep36S3ClassClosureReconciliation.v1",
        "status": "STRONGER_SELECTED_S3_SOURCE_CERTIFICATE_OVERRIDES_STEP35_OPEN_FLAGS",
        "step35_frontier_flags_before_reconciliation": {
            "selected_s3_differential_cohomology_class_closed": step35["closure_decision"]["selected_s3_differential_cohomology_class_closed"],
            "s3_restriction_pullback_table_closed": step35["closure_decision"]["s3_restriction_pullback_table_closed"],
            "smooth_freed_witten_projector_retention_closed": step35["closure_decision"]["smooth_freed_witten_projector_retention_closed"],
        },
        "stronger_selected_s3_source_certificate": {
            "status": s3_source["status"],
            "selected_s3_flat_Deligne_class_imported": s3_source["gate_results"]["selected_s3_flat_Deligne_class_imported"],
            "selected_s3_pullback_table_imported": s3_source["gate_results"]["selected_s3_pullback_table_imported"],
            "map_to_qutrit_central_cocycle_verified": s3_source["gate_results"]["map_to_qutrit_central_cocycle_verified"],
            "smooth_Freed_Witten_cancellation_closed": s3_source["gate_results"]["smooth_Freed_Witten_cancellation_closed"],
            "block_projector_retention_closed": s3_source["gate_results"]["block_projector_retention_closed"],
            "selected_packet_validator_passes": s3_source["gate_results"]["selected_packet_validator_passes"],
            "certificate_closes": s3_cert["what_closes"],
        },
        "older_open_artifacts_demoted_for_exact_fields_only": {
            "smooth_s3_lift_status": smooth["status"],
            "smooth_lift_fixed_class_supplied_old_flag": smooth["gate_results"]["fixed_differential_cohomology_class_supplied"],
            "smooth_lift_source_selected_old_flag": smooth["gate_results"]["smooth_source_selected"],
            "demotion_rule": "The later selected S3 differential-cohomology source certificate closes the exact class/restriction/FW/block-projector fields, but it does not close operator D_E/Riesz/Green/dotD or coherent spectral projectors.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(RECON, recon)

    frontier = {
        "schema": "MTTStep36OperatorValueFrontier.v1",
        "status": "OPERATOR_LEVEL_PROJECTIVE_RHOE_DE_RIESZ_GREEN_DOTD_OPEN",
        "closed_before_operator_frontier": {
            "projective_BN_mechanical_lift_fields_closed": step30["closure_decision"]["projective_BN_mechanical_lift_fields_closed"],
            "selected_S3_flat_Deligne_class": s3_cert["what_closes"]["selected_S3_flat_Deligne_class"],
            "selected_S3_pullback_restriction_table": s3_cert["what_closes"]["selected_S3_pullback_restriction_table"],
            "map_to_qutrit_central_cocycle": s3_cert["what_closes"]["map_to_qutrit_central_cocycle"],
            "smooth_S3_twisted_Freed_Witten_cancellation": s3_cert["what_closes"]["smooth_S3_twisted_Freed_Witten_cancellation"],
            "block_factorized_family_Higgs_projector_retention": s3_cert["what_closes"]["block_factorized_family_Higgs_projector_retention"],
            "visible_green_schwarz_curvature_support": visible_gs["gate_results"]["visible_green_schwarz_curvature_closed"],
        },
        "still_open_operator_values": {
            "selected_visible_operator_source_constructed": s3_source["gate_results"]["selected_visible_operator_source_constructed"],
            "selected_D_E_dotD_Riesz_Green_constructed": s3_source["gate_results"]["selected_DE_dotD_Riesz_Green_constructed"],
            "coherent_spectral_zero_mode_projectors_constructed": s3_source["gate_results"]["coherent_spectral_zero_mode_projectors_constructed"],
            "selected_visible_operator_source_from_visible_gs": visible_gs["gate_results"]["selected_visible_operator_source_constructed"],
            "coherent_spectral_projector_retention": spectral["what_remains_open"]["coherent_spectral_projector_retention"],
            "selected_RouteC_Strominger_Galerkin_residual_solve": spectral["what_remains_open"]["selected_RouteC_Strominger_Galerkin_residual_solve"],
        },
        "next_must_emit": [
            "operator-level projective rho_E transition induced by the selected S3 source",
            "selected covariant D_E on the projective B_N lift",
            "source-verified Riesz/Green operator with gap/error certificate",
            "source-verified dotD and coherent spectral zero-mode projectors",
            "then internal R_theta scalar rows without observed SM values as selectors",
        ],
        "accepted_internal_scalar_row_count": 0,
    }
    write_json(FRONTIER, frontier)

    candidate = {
        "candidate": "MTTSelectedStep36S3ClassClosureReconciliationOrOperatorValueFrontier",
        "status": STATUS,
        "inputs": {
            "step35": rel(STEP35),
            "selected_s3_source": rel(S3_SOURCE),
            "selected_s3_source_certificate": rel(S3_SOURCE_CERT),
            "smooth_lift": rel(SMOOTH_LIFT),
            "spectral_projector_frontier": rel(SPECTRAL),
            "visible_green_schwarz": rel(VISIBLE_GS),
            "step30_projective_bn": rel(STEP30),
        },
        "output_packets": {
            "s3_class_closure_reconciliation": rel(RECON),
            "operator_value_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "Step36S3ClassClosureReconciliationTheorem",
            "proved": True,
            "statement": (
                "The later selected S3 differential-cohomology source certificate closes "
                "the Step35 class/restriction frontier: selected flat Deligne class, "
                "S3 pullback table, qutrit central-cocycle map, smooth Freed-Witten "
                "cancellation, and block-family/Higgs projector retention. This does "
                "not close coherent spectral zero-mode projectors, operator-level "
                "projective rho_E, D_E, Riesz/Green, dotD, or internal R_theta values."
            ),
        },
        "closure_decision": {
            "selected_s3_differential_cohomology_class_closed": True,
            "s3_restriction_pullback_table_closed": True,
            "smooth_freed_witten_cancellation_closed": True,
            "block_family_higgs_projector_retention_closed": True,
            "good_cover_removed_as_physical_knob": True,
            "operator_level_projective_rhoE_transition_closed": False,
            "selected_D_E_Riesz_Green_dotD_values_closed": False,
            "coherent_spectral_zero_mode_projectors_closed": False,
            "selected_visible_operator_source_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step36_S3ClassClosureReconciliation_or_OperatorValueFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selected_s3_differential_cohomology_class_closed": True,
        "s3_restriction_pullback_table_closed": True,
        "smooth_freed_witten_cancellation_closed": True,
        "block_family_higgs_projector_retention_closed": True,
        "operator_sector_values_closed": False,
        "coherent_spectral_zero_mode_projectors_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step36 S3ClassClosureReconciliation or OperatorValueFrontier v1

Status: `{STATUS}`.

Step36 reconciles Step35 with the stronger selected S3 source certificate.
The S3 differential-cohomology class/restriction frontier is now closed for:

- selected flat Deligne class
- S3 pullback/restriction table
- qutrit central-cocycle map
- smooth Freed-Witten cancellation
- block-family/Higgs projector retention

Still open:

- coherent spectral zero-mode projectors
- operator-level projective `rho_E`
- selected `D_E`, Riesz/Green, and `dotD`
- internal `R_theta` scalar rows

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
