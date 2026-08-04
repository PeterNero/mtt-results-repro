from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_baselinecostmultiplicitysourceandnoncentralspectatorexclusion"
STATUS = (
    "MTT_SELECTED_SHARED_Z21_BASELINE_MULTIPLICITY_TRACE_AND_EXPLICIT_PARENT_FUNCTIONAL_CLOSED_"
    "PHYSICAL_GAUGE_HESSIAN_RESTRICTION_AND_STRICT_SPECTATOR_COMPLETENESS_OPEN"
)
NEXT = "MTT_Selected_SharedCircleClosureHessianToGaugeZeroModeRestrictionAndCountertermCompleteness_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    shared = load(ROOT / "candidate_data" / SLUG / "shared_z21_marginal_and_unique_character_trace.packet.json")
    action = load(ROOT / "candidate_data" / SLUG / "common_modecount_schur_casimir_parent_functional.packet.json")
    spectators = load(ROOT / "candidate_data" / SLUG / "sector_partition_spectator_completeness_and_strict_gate.packet.json")
    execution = load(ROOT / "candidate_data" / SLUG / "baseline_plus_defect_gauge_execution.packet.json")
    gate = load(ROOT / "candidate_data" / SLUG / "remaining_physical_hessian_restriction_gate.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_BaselineCostMultiplicitySourceAndNoncentralSpectatorExclusion_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(shared["ambient_carrier"]["later_authority_closes_old_sevenfold_row_obligation"], "Z7 successor")
    check(shared["minimal_shared_odd_marginal"]["group"] == "Z21 ~= Z3 x Z7", "Z21")
    check(shared["minimal_shared_odd_marginal"]["bijective"], "CRT")
    check(shared["trace_theorem"]["proved"], "trace theorem")
    check(shared["trace_theorem"]["family_projector_regular_trace"] == 3, "family multiplicity")
    check(shared["trace_theorem"]["q_projector_regular_trace"] == 7, "q multiplicity")
    check(shared["typing_guard"]["A76_Z4_to_Z3_shortcut_rejected"], "Z4 guard")
    check(action["exact_baselines"]["c_e_residual_to_3"] < 1e-14, "c_e")
    check(action["exact_baselines"]["c_q_residual_to_14_over_3"] < 1e-14, "c_q")
    check(action["colored_lane"]["C2_residual_to_4_over_3_identity"] < 1e-14, "Casimir")
    check(not action["physical_selection_boundary"]["current_MTT_corpus_proves_this_parent_is_the_physical_gauge_zero_mode_Hessian"], "parent overclaim")
    check(spectators["basis_theorem"]["spans_entire_partition_invariant_diagonal_space"], "spectator span")
    check(not spectators["strict_all_spectator_completeness_closed"], "spectator overclaim")
    check(execution["baseline_residual"] < 1e-14 and execution["total_residual"] < 1e-14, "A80 replay")
    check(all(gate["closed"].values()), "closed gate")
    check(all(gate["open"].values()), "open gate")
    check(not gate["strict_baseline_source_closed"], "strict baseline overclaim")
    check(not gate["strict_spectator_completeness_closed"], "strict completeness overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict values")
    check(cert["new_continuous_parameters"] == cert["new_discrete_parameters"] == 0, "parameters")
    for phrase in ["Later-authority correction", "Shared-circle multiplicity theorem", "Exact parent functional", "Spectator theorem and exact boundary", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("baseline multiplicity/source and spectator audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
