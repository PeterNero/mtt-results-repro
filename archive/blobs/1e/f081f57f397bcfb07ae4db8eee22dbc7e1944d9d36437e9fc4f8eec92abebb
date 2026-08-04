"""Audit local-QFT tree observable rows and final true-SM-equivalence gap."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_localqftobservablerows_or_finaltruesmequivalencegap"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROWS = PACKET_DIR / "tree_level_local_qft_observable_rows.packet.json"
GAP = PACKET_DIR / "final_true_sm_equivalence_gap_matrix.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_qft_tree_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LocalQFTObservableRows_or_FinalTrueSMEquivalenceGap_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_LOCALQFTOBSERVABLEROWS_OR_FINALTRUESMEQUIVALENCEGAP_BUILT_TREE_QFT_ROWS_PRECISION_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    rows = load(ROWS)
    gap = load(GAP)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    observable_rows = rows["observable_rows"]
    require(len(observable_rows) == 5, "observable row count mismatch")
    require(rows["all_tree_identity_rows_closed"] is True, "tree rows should close")
    require(rows["accepted_as_local_QFT_observable_values_tier"] == "TREE_IDENTITY_TIER_ONLY", "tier mismatch")
    require(rows["not_accepted_as_precision_correlator_or_smatrix_suite"] is True, "precision overclaimed")
    ids = {row["id"] for row in observable_rows}
    for expected in [
        "vev_from_fermi_constant",
        "higgs_curvature_tree_identity",
        "charged_yukawa_mass_identities",
        "gauge_alpha_to_coupling_normalization",
        "ckm_pmns_unitarity_observable_checks",
    ]:
        require(expected in ids, f"missing observable row: {expected}")
    for row in observable_rows:
        require(row["closed_tree_identity"] is True, f"tree row not closed: {row['id']}")
    gauge = next(row for row in observable_rows if row["id"] == "gauge_alpha_to_coupling_normalization")
    require(gauge["max_abs_residual"] < 1e-15, "gauge normalization residual too large")
    yukawa = next(row for row in observable_rows if row["id"] == "charged_yukawa_mass_identities")
    require(yukawa["number_of_mass_rows"] == 9, "mass row count mismatch")
    require(yukawa["max_abs_residual_GeV"] == 0.0, "mass residual mismatch")
    higgs = next(row for row in observable_rows if row["id"] == "higgs_curvature_tree_identity")
    require(abs(higgs["residual"]) < 1e-9, "higgs curvature residual too large")

    require("tree-level local QFT identity observable rows" in gap["closed_now"], "tree QFT closure missing")
    remaining_ids = {row["id"] for row in gap["remaining_true_equivalence_gates"]}
    for expected in [
        "published_or_reconstructed_correlated_profile",
        "precision_correlator_smatrix_decay_observable_rows",
        "multi_loop_threshold_convention_values",
        "QM_GR_measurement_response_interfaces",
        "actual_selected_QaSU3_operator_packet",
    ]:
        require(expected in remaining_ids, f"missing final gap: {expected}")
    require(gap["guardrails"]["tree_identity_tier_not_full_QFT_equivalence"] is True, "tree-tier guard missing")
    require(gap["guardrails"]["true_SM_equivalence_closed"] is False, "true SM overclaimed")

    require(updated["closed_now"] == ["local QFT tree identity observable rows"], "updated closed_now mismatch")
    require("precision local QFT correlator/S-matrix/decay rows" in updated["remaining_true_equivalence_blockers"], "precision QFT blocker missing")
    require(updated["guardrails"]["tree_identity_rows_are_not_precision_observables"] is True, "precision guard missing")

    for key in [
        "local_QFT_tree_identity_observable_rows",
        "propagator_coupling_normalization_tree_tier",
        "mixing_unitarity_observable_checks",
        "final_true_equivalence_gap_matrix_sharpened",
        "superset_strategy_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"missing close flag: {key}")
    require(data["closure_decision"]["tree_QFT_identity_tier_closed"] is True, "tree tier closure missing")
    require(data["closure_decision"]["precision_local_QFT_observable_values_closed"] is False, "precision QFT overclaimed")
    require(cert["next_required_artifact"] == "MTT_Selected_PrecisionQFTObservableRows_or_ActualQaSU3Packet_v1", "next artifact mismatch")

    for packet in [rows, gap, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("tree identity rows" in note, "note missing tree identity wording")
    require("not precision" in note, "note missing precision guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
