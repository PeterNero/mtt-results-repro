"""Audit Higgs off-shell/Zgamma route-A or precision import decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsoffshellzgammaroutea_or_precisionimportdecision"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DECISION = PACKET_DIR / "offshell_zgamma_route_a_vs_import_decision.packet.json"
IMPORT_REPLAY = PACKET_DIR / "offshell_zgamma_import_replay_status.packet.json"
REMAINING = PACKET_DIR / "remaining_three_route_a_kernel_contract.packet.json"
FINAL_STATUS = PACKET_DIR / "higgs_route_a_ten_row_status_after_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_offshell_zgamma_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsOffshellZGammaRouteA_or_PrecisionImportDecision_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSOFFSHELLZGAMMAROUTEA_OR_PRECISIONIMPORTDECISION_BUILT_REMAINING_THREE_IMPORT_REPLAY_ROUTEA_OPEN"
NEXT = "MTT_Selected_HiggsFinalSMParityProfilePolicy_or_RemainingRouteAKernels_v1"
OPEN_ROWS = ["H_to_Z_gamma", "H_to_WW_star", "H_to_ZZ_star"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    decision = load(DECISION)
    import_replay = load(IMPORT_REPLAY)
    remaining = load(REMAINING)
    final_status = load(FINAL_STATUS)
    updated = load(UPDATED_TRUE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(decision["route_A_rows_closed_total"] == 7, "route-A closed count mismatch")
    require(decision["route_A_rows_remaining"] == OPEN_ROWS, "remaining row basis mismatch")
    require(decision["import_replay_allowed_for_SM_parity"] is True, "import replay not allowed")
    require(decision["import_replay_counts_as_route_A_derivative"] is False, "import replay counted as route-A")
    require(decision["full_route_A_ten_row_engine_closed"] is False, "full route-A overclosed")
    require(len(decision["rows"]) == 3, "decision row count mismatch")

    for row in decision["rows"]:
        require(row["channel"] in OPEN_ROWS, "unknown decision row")
        require(row["route_A_kernel_executable_now"] is False, "route-A kernel overfilled")
        require(row["route_A_kernel_filled"] is False, "route-A kernel filled unexpectedly")
        require(row["precision_import_available_as_replay_input"] is True, "import replay missing")
        require(row["precision_import_accepted_as_formula_derivative"] is False, "import accepted as derivative")

    require(import_replay["accepted_as_SM_parity_downstream_replay_layer"] is True, "SM-parity replay missing")
    require(import_replay["accepted_as_precision_profile_closure"] is False, "precision overclosed")
    require(import_replay["accepted_as_route_A_derivative_closure"] is False, "route-A overclosed")
    require(len(import_replay["rows"]) == 3, "import replay row count mismatch")
    for row in import_replay["rows"]:
        require(row["channel"] in OPEN_ROWS, "unknown import row")
        require(row["accepted_as_SM_parity_downstream_replay_value"] is True, "row replay not accepted")
        require(row["accepted_as_precision_total_width_row"] is False, "row precision overaccepted")
        require(row["accepted_as_route_A_formula_value"] is False, "row route-A overaccepted")

    require(remaining["route_A_kernel_contract_complete"] is True, "remaining contract incomplete")
    require(remaining["route_A_kernel_values_filled"] is False, "remaining values overfilled")
    require(remaining["row_count"] == 3, "remaining row count mismatch")

    require(final_status["route_A_rows_executed_count"] == 7, "final executed count mismatch")
    require(final_status["route_A_rows_remaining_count"] == 3, "final remaining count mismatch")
    require(final_status["route_A_rows_remaining"] == OPEN_ROWS, "final remaining rows mismatch")
    require(final_status["SM_parity_import_replay_available_for_remaining_three"] is True, "final import replay missing")
    require(final_status["full_route_A_ten_row_engine_closed"] is False, "final route-A overclosed")

    require(updated["guardrails"]["remaining_three_import_replay_built"] is True, "updated import replay missing")
    require(updated["guardrails"]["remaining_three_route_A_kernels_open"] is True, "updated open guard missing")
    require(updated["guardrails"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(updated["guardrails"]["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["remaining_three_import_replay_accepted_for_SM_parity"] is True, "candidate import replay missing")
    require(data["closure_decision"]["remaining_three_import_replay_accepted_as_route_A"] is False, "candidate route-A overaccepted")
    require(data["closure_decision"]["route_A_rows_closed_total"] == 7, "candidate route-A count mismatch")
    require(cert["route_A_rows_closed_total"] == 7, "certificate route-A count mismatch")
    require("seven of ten" in note, "note missing route-A count")

    for packet in [decision, import_replay, remaining, final_status, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
