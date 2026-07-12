"""Audit selected SM-slot functor overlap-kernel source emission."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
CERT = ROOT / "certificates" / "selected_smslotfunctor_overlapkernel_source_emission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SelectedSMSlotFunctor_OverlapKernel_SourceEmission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_smslotfunctor_overlapkernel_source_emission.py"

STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_ALL_SIX_ARROWS_EMITTED_OPERATOR_PAYLOADS_OPEN"
NEXT = "MTT_SelectedSMSlotFunctor_DownstreamOperatorPayloads_or_SMParityLedger_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note does not name next artifact")

    kernel = data["selected_overlap_kernel"]
    require(kernel["status"] == "EMITTED_SOURCE_ARROW", "A5 was not emitted")
    require(kernel["selected"] is True, "A5 not selected")

    pre = kernel["preconditions"]
    required_preconditions = [
        "first_four_arrows_closed",
        "transported_projector_source_promoted",
        "all_matter_projectors_selected",
        "conditional_gram_theorem_proved",
        "gram_condition_satisfied_by_selected_rho_s",
        "selected_ext_unit_row_closed",
        "selected_hodge_projector_row_closed",
        "theta_quadrature_norm_available",
    ]
    for key in required_preconditions:
        require(pre[key] is True, f"A5 precondition failed: {key}")

    norm = kernel["normalization_values"]
    require(norm["matter_triplet_rank"] == 3, "matter triplet rank mismatch")
    require(
        math.isclose(norm["raw_Ti_frobenius_norm"], math.sqrt(2), rel_tol=0, abs_tol=1e-12),
        "raw Ti Frobenius norm mismatch",
    )
    require(
        "rho_s(T_i)/sqrt(2)" in norm["unit_trace_transfer"],
        "unit transfer mismatch",
    )
    require(norm["eta_00_unit_L2_norm"] == 1, "eta_00 unit L2 norm mismatch")

    same_source = data["same_source_consistency"]
    require(same_source["status"] == "EMITTED_SOURCE_ARROW", "A6 was not emitted")
    require(
        same_source["selected_same_source_consistency_map"] is True,
        "A6 same-source map not selected",
    )
    for key, value in same_source["closed_parts"].items():
        require(value is True, f"A6 closed part failed: {key}")
    require(
        "Yukawa magnitudes, CKM/PMNS, masses, or full SM no-knob closure"
        in same_source["downstream_not_included"],
        "A6 boundary does not exclude downstream flavor closure",
    )

    arrow_status = data["arrow_status"]
    require(arrow_status["closed_count"] == 6, "closed arrow count mismatch")
    require(arrow_status["open_count"] == 0, "open arrow count mismatch")
    require(arrow_status["all_six_closed"] is True, "all six arrows not marked closed")

    for sector, checks in data["matter_projector_checks"].items():
        require(checks["rank"] == 3, f"{sector} rank mismatch")
        require(checks["projector_idempotent"] is True, f"{sector} not idempotent")
        require(checks["projector_self_adjoint"] is True, f"{sector} not self-adjoint")
        require(
            checks["source_verified_by_transport_conjugation"] is True,
            f"{sector} source transport verification missing",
        )
        require(checks["stationary_rho_s_promoted"] is True, f"{sector} rho_s not promoted")

    require(data["closure_claimed"] is False, "full closure overclaimed")
    require(
        data["selected_SMSlotFunctor_all_six_arrows_claimed"] is True,
        "SM-slot six-arrow closure not claimed",
    )
    require(
        data["downstream_operator_or_flavor_closure_claimed"] is False,
        "downstream operator/flavor closure overclaimed",
    )
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not marked proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
