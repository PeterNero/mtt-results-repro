"""Build PSM-C1-02 SI-1u-B1 stationary basis-source promotion.

This imports the already-proved finite projector source-promotion theorem into
the PSM-C1-02 frontier.  It closes the stationary transported
zero-mode/projector source basis boundary, while preserving the dynamic
primitive quadrature/Galerkin rows as the next open gate.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_honestgalerkinzeromodebasissource_or_primitivequadratureexport"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STATIONARY_IMPORT = BASE / "route_b1_stationary_transported_basis_source_import.packet.json"
HONEST_DECISION = BASE / "route_b1_honest_galerkin_basis_decision.packet.json"
PRIMITIVE_WORK = BASE / "route_b2_primitive_quadrature_export_workorder.packet.json"
PROMOTION_STATE = BASE / "unpatched_source_promotion_state_after_b1.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_HonestGalerkinZeroModeBasisSource_or_PrimitiveQuadratureExport_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_unpatchedkernelexecutionplan_or_honestgalerkinexport.candidate.json"
FINITE_PROMOTION = DATA / "selected_finite_projector_source_promotion.candidate.json"
RAW_BN_REJECTION = DATA / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"
ZERO_MODE_INPUT = DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "zero_mode_basis.packet.json"
CURRENT_PSM_PACKET = DATA / "selected_psm_c1_02_selectedsourcepromotionpacket" / "current_unpatched_source_promotion_validator_result.packet.json"
CONDITIONAL_PSM_PACKET = DATA / "selected_psm_c1_02_selectedsourcepromotionpacket" / "conditional_unpatched_source_promotion_validator_result.packet.json"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_B1_STATIONARY_PROJECTOR_BASIS_SOURCE_IMPORTED_PRIMITIVE_QUADRATURE_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_PrimitiveQuadratureExport_or_UnpatchedSourcePromotionPacket_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    finite = load(FINITE_PROMOTION)
    raw_rejection = load(RAW_BN_REJECTION)
    zero_mode = load(ZERO_MODE_INPUT)
    current = load(CURRENT_PSM_PACKET)
    conditional = load(CONDITIONAL_PSM_PACKET)

    sector_slots = finite["promoted_sector_slots"]
    all_stationary_slots_verified = all(
        slot["source_verified_by_transport_conjugation"]
        and slot["stationary_rho_s_promoted"]
        and slot["projector_idempotent"]
        and slot["projector_self_adjoint"]
        and slot["green_operator_valid"]
        and not slot["finite_raw_truncation_replay_used"]
        for slot in sector_slots.values()
    )

    stationary_import = {
        "schema": "MTTPSMC102SI1uB1StationaryTransportedBasisSourceImport.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-B1",
        "status": "STATIONARY_TRANSPORTED_PROJECTOR_BASIS_SOURCE_IMPORTED",
        "imported_from": rel(FINITE_PROMOTION),
        "raw_untransported_equality_rejected_by": rel(RAW_BN_REJECTION),
        "finite_promotion_status": finite["status"],
        "theorem_name": finite["theorem"]["name"],
        "selected_projector_source_verified": finite["promotion_decision"]["selected_projector_source_verified"],
        "validator_ready_stationary_rho_s": finite["promotion_decision"]["validator_ready_stationary_rho_s"],
        "selected_dotD_source_verified": finite["promotion_decision"]["selected_dotD_source_verified"],
        "alpha1_driver_verified": finite["promotion_decision"]["alpha1_driver_verified"],
        "all_stationary_slots_verified": all_stationary_slots_verified,
        "sector_basis_labels": {
            sector: slot["selected_basis_labels"] for sector, slot in sector_slots.items()
        },
        "boundary": {
            "proved": [
                "transported stationary zero-mode basis labels",
                "selected projectors P_s^sel = U P_s^model U^-1",
                "selected Riesz/Green replay on transported complements",
                "stationary rho_s source verification",
            ],
            "not_proved": [
                "raw untransported B_N basis promotion",
                "dynamic dotD/alpha1 derivative promotion in this artifact",
                "primitive C1 overlap contractions",
                "full honest Galerkin C1 value emission",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    honest_decision = {
        "schema": "MTTPSMC102SI1uB1HonestGalerkinBasisDecision.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-B1",
        "status": "B1_PARTIALLY_CLOSED_STATIONARY_SOURCE_BASIS_IMPORTED_DYNAMIC_GALERKIN_OPEN",
        "old_zero_mode_input": rel(ZERO_MODE_INPUT),
        "old_zero_mode_status": zero_mode["status"],
        "old_zero_mode_selected_source_verified": zero_mode["selected_source_verified"],
        "old_zero_mode_disqualified_as_honest_hym_basis": True,
        "new_stationary_transported_source_basis_verified": True,
        "new_basis_is_projector_stationary_not_dynamic_c1_rows": True,
        "honest_independent_galerkin_export_closed": False,
        "reason": (
            "The transported finite projector theorem supplies selected stationary source projectors and "
            "basis labels. It does not compute the 72 primitive C1 quadrature rows, Hessian source rows, "
            "or sector assembly matrices from an independent Galerkin execution."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    primitive_work = {
        "schema": "MTTPSMC102SI1uB2PrimitiveQuadratureExportWorkorder.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-B2",
        "status": "NEXT_GATE_PRIMITIVE_QUADRATURE_EXPORT_REQUIRED",
        "inputs_now_legal": [
            "stationary transported zero-mode/projector source packet",
            "closed static SM-slot/Weyl routing from prior ledger",
            "alpha1/dotD replay imported elsewhere as closed support",
        ],
        "must_emit_next": [
            "selected measure-pairing source owner",
            "selected quadrature rule source owner",
            "phase R_Z primitive row source owner",
            "shift R_X primitive row source owner",
            "b_selected Hessian source owner",
            "sector row assembly source owner",
            "emitted-before-residual-replay proof flag",
        ],
        "success_target": "make current_unpatched_source_promotion_validator_result.passes true without using observed data or locked residual replay as source",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    promotion_state = {
        "schema": "MTTPSMC102SourcePromotionStateAfterB1.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u",
        "status": "SOURCE_PROMOTION_PACKET_STILL_OPEN_AFTER_STATIONARY_BASIS_IMPORT",
        "current_unpatched_packet_passes": current["passes"],
        "conditional_unpatched_packet_passes": conditional["passes"],
        "b1_stationary_source_basis_imported": True,
        "b2_primitive_quadrature_required": True,
        "unpatched_source_promotion_packet_closed": False,
        "global_true_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1uB1.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_HonestGalerkinZeroModeBasisSource_or_PrimitiveQuadratureExport_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
            "task": "Compute independent primitive Galerkin/quadrature contractions and source-owner flags for the 72 primitive rows.",
        },
        "parallel": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A",
            "task": "Continue deriving the local source principles from selected action text.",
        },
        "carry_forward": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B1",
            "task": "Use the imported stationary transported basis/projector source packet as legal support for B2, without promoting dynamic rows from it alone.",
        },
        "status": "NEXT_WORKORDER_PRIMITIVE_QUADRATURE_EXPORT",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102HonestGalerkinZeroModeBasisSourceOrPrimitiveQuadratureExport",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1u-B1", "SOURCE-IDENTITY/SI-1u-B2", "SOURCE-IDENTITY/SI-1u-A"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "output_packets": {
            "stationary_transported_basis_source_import": rel(STATIONARY_IMPORT),
            "honest_galerkin_basis_decision": rel(HONEST_DECISION),
            "primitive_quadrature_export_workorder": rel(PRIMITIVE_WORK),
            "source_promotion_state_after_b1": rel(PROMOTION_STATE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "PSMC102SI1uB1StationaryBasisSourceImportTheorem",
            "proved": True,
            "statement": (
                "For PSM-C1-02, the selected stationary zero-mode/projector source basis may be imported "
                "from the finite projector source-promotion theorem, because the raw untransported B_N "
                "basis is rejected and the transported packet P_s^sel=U P_s^model U^-1 is source-verified "
                "by exact transport conjugation. This closes B1 only at the stationary projector/source tier; "
                "primitive C1 quadrature and full honest Galerkin export remain open."
            ),
        },
        "what_closes_now": {
            "SI1u_B1_stationary_transported_basis_source_imported": True,
            "raw_untransported_BN_basis_rejected_not_reused": True,
            "canonical_qutrit_matrix_unit_basis_disqualified_as_honest_HYM_basis": True,
            "selected_projector_source_verified_imported": True,
            "validator_ready_stationary_rho_s_imported": True,
            "primitive_quadrature_workorder_emitted": True,
        },
        "what_remains_open": {
            "SI1u_B2_independent_72_primitive_galerkin_quadrature_rows": True,
            "selected_measure_pairing_source_owner": True,
            "selected_quadrature_rule_source_owner": True,
            "phase_R_Z_and_shift_R_X_source_owner_rows": True,
            "b_selected_hessian_source_owner": True,
            "sector_row_assembly_source_owner": True,
            "emitted_before_residual_replay_proof": True,
            "unpatched_source_promotion_packet_passes": True,
            "true_SM_equivalence_or_no_knob_closure": True,
        },
        "closure_decision": {
            "b1_stationary_projector_basis_source_imported": True,
            "b1_dynamic_honest_galerkin_export_closed": False,
            "b2_primitive_quadrature_closed": False,
            "unpatched_source_promotion_packet_passes": False,
            "conditional_unpatched_packet_passes_if_source_owners_supplied": True,
            "global_closure_claimed": False,
        },
        "superset_strategy": {
            "classification": "SUPERSET_ROUTE_MERGE_WITH_LOCKED_TARGET",
            "route_from_HYM_End0": "selected HYM/End0 gauge transport supplies U and stationary source projectors",
            "route_from_finite_BN": "finite B_N projector values supply exact model projectors before transport",
            "route_from_PSM_C1": "PSM-C1-02 supplies the dynamic primitive row target that still must be emitted",
            "knob_policy": "These routes constrain one selected packet; no observed constants or adjustable knobs are used.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_HonestGalerkinZeroModeBasisSource_or_PrimitiveQuadratureExport_v1",
        "active_label": "PSM-C1-02",
        "active_routes": candidate["active_routes"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "b1_stationary_projector_basis_source_imported": True,
        "b1_dynamic_honest_galerkin_export_closed": False,
        "b2_primitive_quadrature_closed": False,
        "unpatched_source_promotion_packet_passes": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 HonestGalerkinZeroModeBasisSource or PrimitiveQuadratureExport v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B1`

Next label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2`

Parallel label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Result

`SI-1u-B1` is now closed at the stationary source tier.  The selected finite
projector source-promotion theorem gives the transported packet
`P_s^sel = U P_s^model U^-1`, selected basis labels, selected Riesz/Green replay,
and validator-ready stationary `rho_s`.

This does not promote the old canonical qutrit matrix-unit basis into an honest
HYM basis.  That old packet remains support-only.  It also does not compute the
dynamic primitive `C1` rows.

## Superset Use

This is a constrained route merge, not knobs.  The HYM/End0 route supplies the
selected transport, the finite `B_N` route supplies model projector values, and
the PSM-C1 route supplies the dynamic target that remains to be emitted.

## Boundary

Closed now:

- `SI-1u-B1`: stationary transported zero-mode/projector source basis.
- Raw untransported `B_N` equality remains rejected.
- Canonical qutrit matrix-unit support remains disqualified as honest HYM basis.

Still open:

- `SI-1u-B2`: independent primitive Galerkin/quadrature rows.
- selected measure-pairing and quadrature source owners.
- `R_Z`, `R_X`, `b_selected`, and sector row source owners.
- emitted-before-residual-replay proof.

Next artifact: `{NEXT}`
"""

    for path, obj in [
        (STATIONARY_IMPORT, stationary_import),
        (HONEST_DECISION, honest_decision),
        (PRIMITIVE_WORK, primitive_work),
        (PROMOTION_STATE, promotion_state),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
