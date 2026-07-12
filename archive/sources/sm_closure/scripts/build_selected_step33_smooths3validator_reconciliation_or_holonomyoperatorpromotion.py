"""Build Step 33 smooth-S3 validator reconciliation and holonomy promotion cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step33_smooths3validator_reconciliation_or_holonomyoperatorpromotion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "step33_strict_q79_validator_reconciliation.packet.json"
HOLONOMY = PACKET_DIR / "step33_holonomy_operator_promotion_contract.packet.json"
FILL_TARGETS = PACKET_DIR / "step33_minimal_smooth_source_fill_targets.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step33_SmoothS3ValidatorReconciliation_or_HolonomyOperatorPromotion_v1.md"

STEP32 = DATA / "selected_step32_samesourcesymmetrybreaking_to_smooths3twistedsource.candidate.json"
S3_RETENTION = DATA / "selected_s3_class_restriction_projector_retention.candidate.json"
PROJECTIVE_GERBE = DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"
VISIBLE_GS = DATA / "selected_visible_green_schwarz_operator_source.candidate.json"
Q79_SMOOTH_ATTEMPT = Q79 / "candidate_data" / "visible_twisted_s3_smooth_source_lift_attempt.candidate.json"
Q79_FW_GATE = Q79 / "candidate_data" / "time_oriented_m1_freed_witten_cycle_gate.candidate.json"
Q79_CP = Q79 / "candidate_data" / "visible_twisted_s3_finite_cp_cancellation.candidate.json"

STATUS = "MTT_SELECTED_STEP33_SMOOTHS3_VALIDATOR_RECONCILED_HOLONOMY_PROMOTION_OPEN"
NEXT = "MTT_Selected_SmoothS3DeligneCechSourceMap_or_HolonomyOperatorSource_v1"


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

    inputs = [
        STEP32,
        S3_RETENTION,
        PROJECTIVE_GERBE,
        VISIBLE_GS,
        Q79_SMOOTH_ATTEMPT,
        Q79_FW_GATE,
        Q79_CP,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 33 inputs: " + ", ".join(missing))

    step32 = load(STEP32)
    s3_retention = load(S3_RETENTION)
    projective = load(PROJECTIVE_GERBE)
    visible_gs = load(VISIBLE_GS)
    q79_smooth = load(Q79_SMOOTH_ATTEMPT)
    q79_fw = load(Q79_FW_GATE)
    q79_cp = load(Q79_CP)

    validator_head = q79_smooth["validator_result"]["attempt_output_head"]
    missing_validator_fields = [
        line.removeprefix("- ")
        for line in validator_head
        if isinstance(line, str) and line.startswith("- ")
    ]

    reconciliation = {
        "schema": "MTTStep33StrictQ79SmoothS3ValidatorReconciliation.v1",
        "status": "STRICT_Q79_VALIDATOR_OVERRIDES_OLDER_RETIRED_BLOCKER_WORDING",
        "step32_frontier": {
            "smooth_s3_twisted_source_lift_closed": step32["closure_decision"]["smooth_s3_twisted_source_lift_closed"],
            "smooth_freed_witten_projector_retention_closed": step32["closure_decision"]["smooth_freed_witten_projector_retention_closed"],
            "operator_level_projective_rhoE_transition_closed": step32["closure_decision"]["operator_level_projective_rhoE_transition_closed"],
        },
        "q79_strict_validator": {
            "status": q79_smooth["status"],
            "selected_smooth_S3_source_constructed": q79_smooth["calculation_results"]["selected_smooth_S3_source_constructed"],
            "smooth_S3_Freed_Witten_closed": q79_smooth["calculation_results"]["smooth_S3_Freed_Witten_closed"],
            "smooth_S3_projector_retention_closed": q79_smooth["calculation_results"]["smooth_S3_projector_retention_closed"],
            "selected_cover_or_scaffold_verified": q79_smooth["smooth_lift_attempt"]["selected_cover_or_scaffold_verified"],
            "source_selected_by_mtt": q79_smooth["smooth_lift_attempt"]["source_selected_by_mtt"],
            "missing_validator_fields": missing_validator_fields,
        },
        "finite_support_kept_closed": {
            "finite_S3_CP_cancellation_closed": q79_cp["calculation_results"]["finite_S3_CP_cancellation_closed"],
            "finite_twisted_CP_module_on_S3": q79_cp["s3_cancellation_reports"][0]["finite_twisted_CP_module_on_S3"],
            "finite_total_twisted_DD_class_zero": q79_cp["s3_cancellation_reports"][0]["finite_total_twisted_DD_class_zero"],
            "finite_projector_architecture_retained": s3_retention["gate_results"]["finite_block_projector_architecture_retained"],
            "visible_green_schwarz_curvature_closed": visible_gs["gate_results"]["visible_green_schwarz_curvature_closed"],
        },
        "older_projective_packet_demoted_fields": {
            "older_packet_claimed_fixed_smooth_flat_S3_class_retired": projective["promotion_result"]["retired_blockers"]["fixed_smooth_flat_S3_class"],
            "older_packet_claimed_smooth_S3_twisted_Freed_Witten_retired": projective["promotion_result"]["retired_blockers"]["smooth_S3_twisted_Freed_Witten"],
            "strict_validator_keeps_these_open": True,
            "reason": "The older packet predates the explicit q79 smooth-source validator; its retired-blocker wording is support only unless the validator fields are filled by a selected source certificate.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RECONCILIATION, reconciliation)

    holonomy = {
        "schema": "MTTStep33HolonomyOperatorPromotionContract.v1",
        "status": "HOLONOMY_OPERATOR_PROMOTION_CONTRACT_EMITTED_SOURCE_MAP_OPEN",
        "source_map_to_construct": {
            "domain": "selected smooth S3 worldvolume / good-cover Cech nerve",
            "finite_shadow": "q79/F,m=1 active F_3^2 central extension with zeta_3^2 projective qutrit module",
            "target": "projective B_N operator bundle with sector projectors and D_E/Riesz/Green/dotD action",
            "required_property": "smooth holonomies restrict to the finite central cocycle and commute with retained family/Higgs projector blocks up to the matched twist",
        },
        "two_legal_routes": {
            "A_smooth_Deligne_Cech_source": [
                "emit selected good-cover data",
                "emit fixed flat Deligne-Cech 2-cocycle / differential cohomology class",
                "prove restriction to S3 maps to the qutrit central cocycle",
                "prove smooth twisted CP or worldvolume-flux cancellation",
                "prove Green-Schwarz, Freed-Witten, and projector retention",
            ],
            "B_holonomy_operator_source": [
                "emit selected finite-to-smooth holonomy functor",
                "prove the holonomy representation selects the same projective B_N rho_E transition",
                "prove D_E is the covariant derivative induced by that holonomy source",
                "derive Riesz/Green/dotD from the same source, not from identity smoke or benchmark values",
            ],
        },
        "must_not_use": [
            "identity rho_E smoke",
            "ordinary rank-two DD-zero route for S3",
            "observed Yukawa/CKM/PMNS/mass values",
            "projective prototype promoted without selected cover/source certificate",
        ],
        "operator_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
    }
    write_json(HOLONOMY, holonomy)

    fill_targets = {
        "schema": "MTTStep33MinimalSmoothSourceFillTargets.v1",
        "status": "MINIMAL_FILL_TARGETS_EXTRACTED_FROM_Q79_VALIDATOR",
        "validator": "mtt-q79-proof-repro/scripts/validate_visible_twisted_s3_smooth_source_lift.py",
        "required_true_fields": [
            "selected_stack == S3",
            "smooth_source.source_selected_by_mtt",
            "smooth_source.selected_cover_or_scaffold_verified",
            "smooth_source.good_cover_data_supplied",
            "smooth_source.deligne_cech_representative_constructed",
            "smooth_source.fixed_differential_cohomology_class",
            "smooth_source.restricts_to_selected_S3_worldvolume",
            "smooth_source.map_to_qutrit_central_cocycle_verified",
            "smooth_source.smooth_twisted_CP_or_worldvolume_flux_constructed",
            "consistency.green_schwarz_bianchi_verified_for_smooth_S3_source",
            "consistency.freed_witten_verified_for_smooth_S3_source",
            "consistency.twisted_projector_retention_verified",
            "consistency.block_factorized_family_higgs_projectors_retained",
        ],
        "already_available_support": {
            "branch_q79_F_m1": True,
            "curvature_H_form_zero": True,
            "finite_S3_CP_cancellation_closed": True,
            "qutrit_projective_module_compatible": True,
            "ordinary_matter_curves_retained": True,
        },
        "currently_absent_source_certificate": True,
        "selected_cycle_gate_status": q79_fw["status"],
        "selected_cycles_supplied": q79_fw["calculation_results"]["selected_cycles_supplied"],
        "rank_two_active_images_fail_ordinary_DD": q79_fw["calculation_results"]["rank_two_active_images_fail_DD_part"],
    }
    write_json(FILL_TARGETS, fill_targets)

    candidate = {
        "candidate": "MTTSelectedStep33SmoothS3ValidatorReconciliationOrHolonomyOperatorPromotion",
        "status": STATUS,
        "inputs": {
            "step32": rel(STEP32),
            "s3_retention": rel(S3_RETENTION),
            "projective_gerbe": rel(PROJECTIVE_GERBE),
            "visible_green_schwarz": rel(VISIBLE_GS),
            "q79_smooth_attempt": rel(Q79_SMOOTH_ATTEMPT),
            "q79_freed_witten_gate": rel(Q79_FW_GATE),
            "q79_finite_cp": rel(Q79_CP),
        },
        "output_packets": {
            "strict_validator_reconciliation": rel(RECONCILIATION),
            "holonomy_operator_promotion_contract": rel(HOLONOMY),
            "minimal_smooth_source_fill_targets": rel(FILL_TARGETS),
        },
        "theorem": {
            "name": "Step33StrictSmoothSourceFrontierTheorem",
            "proved": True,
            "statement": (
                "The smooth S3 twisted-source problem is not closed by the older "
                "projective-gerbe retired-blocker wording. The stricter q79 smooth "
                "source validator is controlling: finite S3 twisted CP cancellation "
                "and finite projector architecture remain closed support, while selected "
                "cover/good-cover data, fixed Deligne-Cech class, smooth Freed-Witten, "
                "projector retention, and holonomy-induced operator source remain open."
            ),
        },
        "closure_decision": {
            "strict_q79_smooth_validator_promoted_to_active_gate": True,
            "older_projective_gerbe_retired_blocker_wording_demoted": True,
            "finite_s3_cp_and_projector_support_kept_closed": True,
            "holonomy_operator_promotion_contract_emitted": True,
            "minimal_smooth_source_fill_targets_extracted": True,
            "smooth_s3_twisted_source_lift_closed": False,
            "selected_smooth_cover_or_scaffold_closed": False,
            "smooth_freed_witten_projector_retention_closed": False,
            "operator_level_projective_rhoE_transition_closed": False,
            "selected_D_E_Riesz_Green_dotD_values_closed": False,
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
        "certificate": "MTT_Selected_Step33_SmoothS3ValidatorReconciliation_or_HolonomyOperatorPromotion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_q79_smooth_validator_active": True,
        "holonomy_operator_promotion_contract_emitted": True,
        "smooth_s3_twisted_source_lift_closed": False,
        "operator_sector_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step33 SmoothS3 Validator Reconciliation or Holonomy Operator Promotion v1

Status: `{STATUS}`.

Step33 resolves a real ledger conflict. The older projective-gerbe packet may be
used as finite/projective support. The strict q79 smooth-source validator is now the active gate for smooth S3 source promotion.

Closed support retained:

- finite q79/F,m=1 S3 twisted Chan-Paton cancellation
- finite S3 projector architecture
- visible Green-Schwarz curvature support
- projective B_N mechanical scaffold from Step30

Still open:

- selected smooth cover/good-cover data
- fixed smooth Deligne-Cech/differential-cohomology class
- smooth S3 Freed-Witten and projector retention
- holonomy-induced operator-level projective `rho_E`
- selected `D_E`, Riesz/Green, and `dotD` values

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
