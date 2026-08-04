"""Audit representative tree-level QFT decay rows and actual Qa/SU3 packet gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_precisionqftobservablerows_or_actualqasu3packet"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DECAYS = PACKET_DIR / "representative_tree_level_decay_observable_rows.packet.json"
QASU3 = PACKET_DIR / "actual_qasu3_packet_gate_after_qft_rows.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_tree_decay_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrecisionQFTObservableRows_or_ActualQaSU3Packet_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PRECISIONQFTOBSERVABLEROWS_OR_ACTUALQASU3PACKET_BUILT_TREE_DECAY_ROWS_PRECISION_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    decays = load(DECAYS)
    qasu3 = load(QASU3)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    higgs = decays["higgs_fermion_decay_rows"]
    w_rows = decays["w_leptonic_decay_rows"]
    require(len(higgs) == 5, "Higgs decay row count mismatch")
    require(len(w_rows) == 3, "W decay row count mismatch")
    require(decays["summary"]["all_widths_finite_nonnegative"] is True, "width positivity mismatch")
    require(decays["accepted_as_representative_local_QFT_decay_rows"] is True, "tree decay tier should close")
    require(decays["accepted_as_precision_SM_decay_widths"] is False, "precision widths overclaimed")
    h_by_id = {row["id"]: row for row in higgs}
    require(h_by_id["H_to_t_tbar_tree_closed"]["kinematically_open"] is False, "H->tt should be closed")
    require(h_by_id["H_to_b_bbar_tree"]["width_GeV"] > h_by_id["H_to_tau_tau_tree"]["width_GeV"], "H->bb should exceed H->tautau in this tree replay")
    require(h_by_id["H_to_tau_tau_tree"]["width_GeV"] > h_by_id["H_to_mu_mu_tree"]["width_GeV"], "H->tautau should exceed H->mumu")
    w_widths = {row["width_GeV"] for row in w_rows}
    require(len(w_widths) == 1, "massless W leptonic widths should match")
    require(next(iter(w_widths)) > 0.0, "W leptonic width must be positive")

    require(qasu3["qft_rows_change_source_status"] is False, "QFT rows must not change source status")
    require(qasu3["target_fitting_used"] is False, "QaSU3 gate fitting violation")
    require("ACTUAL_QASU3" in qasu3["status"], "QaSU3 status mismatch")

    require(updated["closed_now"] == ["representative tree-level local QFT decay rows"], "updated closed_now mismatch")
    require("loop-corrected local QFT correlator/S-matrix/decay rows" in updated["remaining_true_equivalence_blockers"], "loop-corrected blocker missing")
    require(updated["guardrails"]["tree_decay_rows_are_not_precision_decay_widths"] is True, "precision guard missing")
    require(updated["guardrails"]["qft_rows_do_not_select_qasu3_packet"] is True, "source guard missing")

    for key in [
        "representative_tree_level_decay_rows",
        "finite_nonnegative_decay_widths",
        "actual_qasu3_gate_rechecked",
        "superset_strategy_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"missing close flag: {key}")
    require(data["closure_decision"]["representative_tree_decay_tier_closed"] is True, "tree decay closure missing")
    require(data["closure_decision"]["precision_local_QFT_observable_values_closed"] is False, "precision QFT overclaimed")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_closed"] is False, "QaSU3 overclaimed")
    require(cert["next_required_artifact"] == "MTT_Selected_LoopCorrectedQFTObservables_or_ActualQaSU3Packet_v1", "next artifact mismatch")

    for packet in [decays, qasu3, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("tree-level" in note, "note missing tree-level wording")
    require("not precision" in note, "note missing precision guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
