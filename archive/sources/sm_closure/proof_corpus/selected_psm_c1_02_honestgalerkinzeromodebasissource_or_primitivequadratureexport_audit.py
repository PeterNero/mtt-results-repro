"""Audit PSM-C1-02 SI-1u-B1 stationary basis-source import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_psm_c1_02_honestgalerkinzeromodebasissource_or_primitivequadratureexport.py"

SLUG = "selected_psm_c1_02_honestgalerkinzeromodebasissource_or_primitivequadratureexport"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
STATIONARY_IMPORT = BASE / "route_b1_stationary_transported_basis_source_import.packet.json"
HONEST_DECISION = BASE / "route_b1_honest_galerkin_basis_decision.packet.json"
PRIMITIVE_WORK = BASE / "route_b2_primitive_quadrature_export_workorder.packet.json"
PROMOTION_STATE = BASE / "unpatched_source_promotion_state_after_b1.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_HonestGalerkinZeroModeBasisSource_or_PrimitiveQuadratureExport_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_B1_STATIONARY_PROJECTOR_BASIS_SOURCE_IMPORTED_PRIMITIVE_QUADRATURE_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_PrimitiveQuadratureExport_or_UnpatchedSourcePromotionPacket_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "global closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    stationary = load(STATIONARY_IMPORT)
    honest = load(HONEST_DECISION)
    primitive = load(PRIMITIVE_WORK)
    state = load(PROMOTION_STATE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1u-B1", "SOURCE-IDENTITY/SI-1u-B2", "SOURCE-IDENTITY/SI-1u-A"], "routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")

    closes = candidate["what_closes_now"]
    require(closes["SI1u_B1_stationary_transported_basis_source_imported"] is True, "B1 import not closed")
    require(closes["raw_untransported_BN_basis_rejected_not_reused"] is True, "raw BN guard missing")
    require(closes["canonical_qutrit_matrix_unit_basis_disqualified_as_honest_HYM_basis"] is True, "canonical guard missing")
    require(closes["selected_projector_source_verified_imported"] is True, "projector source import missing")

    remains = candidate["what_remains_open"]
    require(remains["SI1u_B2_independent_72_primitive_galerkin_quadrature_rows"] is True, "B2 overclosed")
    require(remains["unpatched_source_promotion_packet_passes"] is True, "unpatched remaining flag missing")

    closure = candidate["closure_decision"]
    require(closure["b1_stationary_projector_basis_source_imported"] is True, "closure B1 import missing")
    require(closure["b1_dynamic_honest_galerkin_export_closed"] is False, "dynamic Galerkin overclosed")
    require(closure["b2_primitive_quadrature_closed"] is False, "primitive quadrature overclosed")
    require(closure["unpatched_source_promotion_packet_passes"] is False, "unpatched packet overaccepted")
    require(closure["conditional_unpatched_packet_passes_if_source_owners_supplied"] is True, "conditional target missing")

    require(stationary["status"] == "STATIONARY_TRANSPORTED_PROJECTOR_BASIS_SOURCE_IMPORTED", "stationary status mismatch")
    require(stationary["selected_projector_source_verified"] is True, "stationary source not verified")
    require(stationary["validator_ready_stationary_rho_s"] is True, "stationary rho not ready")
    require(stationary["selected_dotD_source_verified"] is False, "dotD overclosed in B1")
    require(stationary["alpha1_driver_verified"] is False, "alpha1 overclosed in B1")
    require(stationary["all_stationary_slots_verified"] is True, "stationary slots incomplete")
    require(len(stationary["sector_basis_labels"]) == 7, "sector basis count mismatch")
    require("raw untransported B_N basis promotion" in stationary["boundary"]["not_proved"], "raw BN boundary missing")

    require(honest["old_zero_mode_selected_source_verified"] is False, "old zero mode oververified")
    require(honest["old_zero_mode_disqualified_as_honest_hym_basis"] is True, "old basis not disqualified")
    require(honest["new_stationary_transported_source_basis_verified"] is True, "new stationary basis missing")
    require(honest["new_basis_is_projector_stationary_not_dynamic_c1_rows"] is True, "stationary/dynamic split missing")
    require(honest["honest_independent_galerkin_export_closed"] is False, "honest Galerkin overclosed")

    require(primitive["route_label"] == "SOURCE-IDENTITY/SI-1u-B2", "primitive route mismatch")
    require(len(primitive["must_emit_next"]) == 7, "primitive workorder incomplete")
    require("current_unpatched_source_promotion_validator_result.passes true" in primitive["success_target"], "success target mismatch")

    require(state["current_unpatched_packet_passes"] is False, "current packet overaccepted")
    require(state["conditional_unpatched_packet_passes"] is True, "conditional packet missing")
    require(state["b1_stationary_source_basis_imported"] is True, "state B1 missing")
    require(state["b2_primitive_quadrature_required"] is True, "state B2 missing")
    require(state["unpatched_source_promotion_packet_closed"] is False, "state overclosed")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2", "next primary mismatch")
    require(next_work["parallel"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A", "parallel label mismatch")
    require(next_work["carry_forward"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B1", "carry-forward label mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["b1_stationary_projector_basis_source_imported"] is True, "cert B1 missing")
    require(cert["b1_dynamic_honest_galerkin_export_closed"] is False, "cert dynamic overclosed")
    require(cert["b2_primitive_quadrature_closed"] is False, "cert primitive overclosed")
    require(cert["unpatched_source_promotion_packet_passes"] is False, "cert unpatched overaccepted")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B1`" in note, "note B1 label missing")
    require("Next label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2`" in note, "note B2 label missing")
    require("constrained route merge, not knobs" in note, "note superset guard missing")
    require("Still open:" in note and "`R_Z`, `R_X`, `b_selected`" in note, "note open boundary missing")

    for packet in [candidate, stationary, honest, primitive, state, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
