"""Audit CONST-EW-02 B37 RA-2 boundary/RB-4 independent source artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b37_ra2_boundary_or_rb4_independent_source"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
RA2 = BASE / "route_a_ra2_boundary_source_reduction.packet.json"
RB4 = BASE / "route_b_rb4_independent_source_payload_contract.packet.json"
BOUNDARY = BASE / "weak_mixing_b37_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B37_RA2_Boundary_or_RB4_IndependentSource_v1.md"

STATUS = "MTT_CONST_EW_02_B37_RA2_BOUNDARY_OR_RB4_INDEPENDENT_SOURCE_BUILT"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    ra2 = load(RA2)
    rb4 = load(RB4)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("ra2", ra2),
        ("rb4", rb4),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["RA2_formal_boundary_source_support_closed"] is True, "RA2 formal support missing")
    require(candidate["RA2_physical_boundary_source_cancellation_promoted"] is False, "RA2 physical overpromoted")
    require(candidate["RB4_strict_independent_payload_contract_imported"] is True, "RB4 contract missing")
    require(candidate["RB4_independent_values_filled"] is False, "RB4 values overfilled")
    require(candidate["source_promotion_closed_now"] is False, "source promotion overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    formal = ra2["formal_support_closed"]
    require(formal["unique_formal_C1_defect_functional_sourced"] is True, "defect functional support")
    require(formal["euler_projection_scale_independence_verified"] is True, "Euler scale independence")
    require(formal["algebraic_finite_trace_boundary_cancellation"] is True, "finite boundary")
    require(ra2["physical_promotion_still_open"]["physical_PhiFinC1_action_identity"] is True, "physical action should remain open")
    require(ra2["physical_promotion_still_open"]["same_source_b_selected_emission"] is True, "b_selected should remain open")
    require(ra2["physical_promotion_still_open"]["absence_of_extra_physical_boundary_or_source_term"] is True, "boundary/source should remain open")
    require(ra2["route_A_promoted_now"] is False, "Route A overpromoted")

    contract = rb4["strict_payload_contract"]
    counts = contract["required_stage_counts"]
    require(counts["strict_payload_rows"] == 110, "strict row count")
    require(counts["primitive_contractions"] == 72, "primitive count")
    require(counts["hessian_source"] == 2, "hessian count")
    require(counts["sector_matrices"] == 36, "sector count")
    require(rb4["validator_rejects_unfilled_template"] is True, "validator should reject unfilled template")
    require(rb4["route_B_independent_quadrature_promoted_now"] is False, "Route B overpromoted")
    require(rb4["locked_target_values_used_as_source"] is False, "locked target used as source")
    require("replay-backed residual rows" in contract["forbidden_provenance"], "forbidden provenance guard")

    require(boundary["closed_or_sharpened_now"]["RA2_formal_C1_defect_functional_source"] is True, "boundary RA2 formal")
    require(boundary["closed_or_sharpened_now"]["RA2_physical_boundary_source_cancellation_promoted"] is False, "boundary RA2 physical")
    require(boundary["closed_or_sharpened_now"]["RB4_values_or_source_ids_filled"] is False, "boundary RB4 values")
    require(boundary["still_open"]["110_independent_payload_values"] is True, "110 values should remain open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle should remain open")
    require("not treating formal finite trace cancellation as physical action identity" in boundary["anti_cycle_delta_from_B36"]["not_repeated"], "anti-cycle guard")

    require(cert["status"] == STATUS, "cert status")
    require(cert["RA2_formal_boundary_source_support_closed"] is True, "cert RA2")
    require(cert["RA2_physical_boundary_source_cancellation_promoted"] is False, "cert RA2 physical")
    require(cert["RB4_strict_independent_payload_contract_imported"] is True, "cert RB4")
    require(cert["RB4_independent_values_filled"] is False, "cert values")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B38-ROUTEA-PHYSICAL-PHIFINC1-ACTION-IDENTITY", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B38-ROUTEB-FILLED-INDEPENDENT-QUADRATURE-PAYLOAD", "next parallel")
    require("Superset Use" in note and "B38" in note, "note next/superset")

    print("CONST-EW-02 B37 RA2 boundary/RB4 independent source audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
