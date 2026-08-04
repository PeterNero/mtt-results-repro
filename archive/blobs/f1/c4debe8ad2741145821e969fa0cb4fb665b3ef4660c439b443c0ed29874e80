"""Audit accepted bounded-error certificate for the q79/rank Yukawa law."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_yukawaboundederrorcertificate_or_residualoperatorfrontier"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ERROR_CERT = PACKET_DIR / "accepted_bounded_yukawa_error_certificate.packet.json"
TIER = PACKET_DIR / "exactness_tier_decision.packet.json"
NEXT_CONTRACT = PACKET_DIR / "residual_operator_frontier_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_YukawaBoundedErrorCertificate_or_ResidualOperatorFrontier_v1.md"

STATUS = "MTT_SELECTED_YUKAWA_BOUNDED_ERROR_CERTIFICATE_ACCEPTED_RESIDUAL_OPERATOR_FRONTIER_OPEN"
NEXT = "MTT_Selected_YukawaFiniteProjectedOperatorResidualSource_or_ExactMagnitudeClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    error_cert = load(ERROR_CERT)
    tier = load(TIER)
    next_contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(error_cert["status"] == "BOUNDED_ERROR_CERTIFICATE_ACCEPTED_FOR_LOCKED_Q79_RANK_LAW", "error cert status")
    require(error_cert["observed_data_used_as_selector"] is False, "error cert observed guard")
    require(error_cert["target_fitting_used"] is False, "error cert target guard")
    source = error_cert["independent_source_object"]
    require(source["source_law_locked_before_certificate"] is True, "source law not locked")
    require(source["finite_cutoff_exactness_blocker_retired_for_A_N"] is True, "finite cutoff not retired")
    require(source["residual_operator_not_used_to_select_source_law"] is True, "selector guard")

    bound = error_cert["error_bound"]
    require(bound["declared_max_log_residual_bound"] == 4.0e-6, "declared bound")
    require(bound["actual_max_log_residual"] < bound["declared_max_log_residual_bound"], "bound fail")
    require(bound["actual_max_log_residual"] > 3.5e-6, "unexpected residual")
    require(bound["actual_worst_multiplicative_yukawa_error"] < bound["declared_worst_multiplicative_factor_bound"], "factor bound")
    require(bound["bound_passes"] is True, "bound pass flag")

    structure = error_cert["residual_structure_certificate"]
    require(structure["family_shape_Q"] == [-2.0, 3.0, -1.0], "family Q")
    require(structure["residual_rank"] == 1, "rank")
    require(structure["factorization"] == "R_remaining_{s,g}=delta_eta_s*Q_g", "factorization")
    require(structure["max_sector_amplitude_abs"] > 1.0e-6, "sector residual")

    floor = error_cert["floor_comparison"]
    require(floor["below_imported_H_scalar_replay_floor"] is False, "floor overclaimed")
    require(floor["residual_floor_ratio"] > 1.0e6, "floor ratio")

    accepted_as = error_cert["accepted_as"]
    require(accepted_as["bounded_error_certificate_for_locked_source_law"] is True, "bounded certificate")
    require(accepted_as["sm_parity_or_approximation_tier_certificate"] is True, "tier certificate")
    require(accepted_as["strict_exactness_certificate"] is False, "strict exactness overclaimed")
    require(accepted_as["strict_no_knob_yukawa_closure"] is False, "strict no-knob overclaimed")

    require(tier["status"] == "BOUNDED_ERROR_ACCEPTED_STRICT_EXACTNESS_REJECTED", "tier status")
    require(len(tier["accepted_now"]) == 3, "accepted count")
    require(len(tier["rejected_now"]) == 3, "rejected count")
    tier_acceptance = tier["tier_acceptance"]
    require(tier_acceptance["bounded_error_certificate_accepted"] is True, "tier bounded")
    require(tier_acceptance["strict_exactness_closed"] is False, "tier exactness")
    require(tier_acceptance["residual_operator_frontier_open"] is True, "frontier")
    require(tier_acceptance["strict_no_knob_yukawa_closure"] is False, "tier no-knob")
    require(tier_acceptance["true_SM_equivalence_closed"] is False, "tier true SM")
    counts = tier["source_row_counts"]
    require(counts["accepted_bounded_error_certificates"] == 1, "bounded count")
    require(counts["accepted_strict_exactness_certificates"] == 0, "strict cert count")
    require(counts["accepted_residual_operator_rows"] == 0, "residual rows")
    require(counts["accepted_full_no_knob_yukawa_rows"] == 0, "no-knob rows")

    require(next_contract["status"] == "RESIDUAL_OPERATOR_SOURCE_CONTRACT_FIXED_AFTER_BOUNDED_ERROR", "next status")
    require(next_contract["next_required_artifact"] == NEXT, "next contract")
    require(len(next_contract["must_emit_one_of"]) == 3, "must emit")
    require(len(next_contract["forbidden_routes"]) == 3, "forbidden")
    require(next_contract["fixed_target"]["family_shape_Q"] == [-2.0, 3.0, -1.0], "fixed target Q")

    theorem = data["theorem"]
    require(theorem["name"] == "YukawaBoundedErrorCertificateTheorem", "theorem name")
    require(theorem["proved"] is True, "theorem proved")
    closure = data["closure_decision"]
    require(closure["bounded_error_certificate_accepted"] is True, "candidate bounded")
    require(closure["strict_exactness_closed"] is False, "candidate exactness")
    require(closure["residual_operator_frontier_open"] is True, "candidate frontier")
    require(closure["strict_no_knob_yukawa_closure"] is False, "candidate no-knob")

    require(cert["bounded_error_certificate_accepted"] is True, "cert bounded")
    require(cert["actual_max_log_residual"] < cert["declared_max_log_residual_bound"], "cert bound")
    require(cert["strict_exactness_closed"] is False, "cert exactness")
    require(cert["accepted_residual_operator_rows"] == 0, "cert residual rows")
    require(cert["strict_no_knob_yukawa_closure"] is False, "cert no-knob")

    for phrase in [
        "accepted bounded-error",
        "not strict no-knob",
        "`R_remaining_s,g = delta_eta_s * Q_g`",
        "`[27,6,26]`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
