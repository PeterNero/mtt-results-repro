"""Audit post-SM-parity true-equivalence source-upgrade kernel."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_postsmparity_trueequivalence_sourceupgrade_kernel"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
KERNEL = PACKET_DIR / "post_smparity_true_equivalence_source_upgrade_kernel.packet.json"
HYM_ACCEPTANCE = PACKET_DIR / "hym_newton_galerkin_acceptance_kernel.packet.json"
ROUTE_LOCK = PACKET_DIR / "dual_route_superset_lock.packet.json"
CUTSET = PACKET_DIR / "next_source_upgrade_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostSMParity_TrueEquivalenceSourceUpgrade_Kernel_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_POSTSMPARITY_TRUEEQUIVALENCE_SOURCEUPGRADE_KERNEL_BUILT_HYM_SOLVE_OR_PROFILE_VALUES_OPEN"
NEXT = "MTT_Selected_HYMNewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    kernel = load(KERNEL)
    hym = load(HYM_ACCEPTANCE)
    route = load(ROUTE_LOCK)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(kernel["SM_parity_status"]["closed"] is True, "SM parity not locked closed")
    require(kernel["SM_parity_status"]["must_not_reopen_for_true_equivalence"] is True, "SM parity reopen guardrail missing")
    require(kernel["SM_parity_status"]["actual_operator_packet_claimed"] is False, "actual packet overclaimed")
    require(kernel["true_equivalence_status"]["closed"] is False, "true equivalence overclosed")
    require(kernel["source_upgrade_center"]["partial_qasu3_payload_filled"] is True, "partial Qa/SU3 payload not imported")
    require(kernel["source_upgrade_center"]["actual_qasu3_operator_packet_promoted"] is False, "Qa/SU3 overpromoted")
    require(kernel["selected_next_artifact"] == NEXT, "kernel next artifact mismatch")

    require(hym["diagonal_rank2_support_imported"] is True, "diagonal support not imported")
    require(hym["full_sector_operator_payload_emitted"] is False, "full sector payload overemitted")
    require(hym["actual_QaSU3_packet_promoted"] is False, "HYM Qa/SU3 overpromoted")
    require(hym["accepted_for_true_SM_equivalence_now"] is False, "HYM accepted for true equivalence too early")
    for required in [
        "emit selected A_HYM or S/H coefficient vector in fixed gauge",
        "construct rank2-to-sector transfer functor or prove it unnecessary",
        "derive rho_E, metric, D_E, Riesz/Green, dotD, and C1/overlap data from the selected connection",
    ]:
        require(required in hym["required_payloads"], f"HYM acceptance missing payload: {required}")
    require(any("without lifted selected flags" in item for item in hym["acceptance_checks"]), "lifted-flag guardrail missing")

    require(route["straight_path"]["next_artifact"] == NEXT, "straight path next artifact mismatch")
    require(route["straight_path"]["closed_now"] is False, "straight path overclosed")
    require(route["parallel_precision_path"]["contract_ready"] is True, "precision contract not ready")
    require(route["parallel_precision_path"]["full_covariance_profile_closed"] is False, "full covariance overclosed")
    require(route["parallel_precision_path"]["closed_now"] is False, "precision path overclosed")
    require(route["true_SM_equivalence_closed"] is False, "route true equivalence overclosed")
    require(route["no_knob_closed"] is False, "route no-knob overclosed")

    require(cutset["bookkeeping_remaining"] is False, "bookkeeping incorrectly remains")
    require(cutset["value_or_source_emission_required"] is True, "source/value emission not required")
    require(cutset["primary_recommended_next_artifact"] == NEXT, "cutset primary artifact mismatch")
    require(cutset["true_SM_equivalence_closed"] is False, "cutset true equivalence overclosed")

    require(data["closure_decision"]["SM_parity_closed"] is True, "candidate SM parity missing")
    require(data["closure_decision"]["source_upgrade_kernel_built"] is True, "candidate kernel not built")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_promoted"] is False, "candidate Qa/SU3 overpromoted")
    require(data["closure_decision"]["precision_profile_complete"] is False, "candidate precision profile overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["superset_strategy"]["combining_paths"] is True, "superset path combination not recorded")
    require(data["superset_strategy"]["using_one_straight_way"] is False, "superset strategy mislabeled as straight-only")
    require("does not reopen SM-parity" in note, "note missing parity guardrail")

    for packet in [kernel, hym, route, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
