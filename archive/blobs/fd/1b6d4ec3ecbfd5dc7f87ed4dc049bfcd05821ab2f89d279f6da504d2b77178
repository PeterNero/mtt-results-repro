"""Audit Higgs precision sidecars and uniform-formula-row gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsprecisionsidecars_or_uniformformularows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SIDECARS = PACKET_DIR / "higgs_channel_uncertainty_sidecars.packet.json"
ENVELOPE = PACKET_DIR / "hybrid_total_width_diagonal_envelope.packet.json"
GATE = PACKET_DIR / "uniform_formula_row_precision_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_sidecars.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsPrecisionSidecars_or_UniformFormulaRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSPRECISIONSIDECARS_OR_UNIFORMFORMULAROWS_BUILT_SIDECARS_UNIFORM_ROWS_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    sidecars = load(SIDECARS)
    envelope = load(ENVELOPE)
    gate = load(GATE)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["sidecar_bookkeeping_closed"] is True, "sidecars not closed")
    require(data["closure_decision"]["full_covariance_profile_closed"] is False, "full covariance overclaimed")
    require(data["closure_decision"]["precision_total_width_closed"] is False, "precision total width overclaimed")

    rows = sidecars["rows"]
    require(len(rows) == 10, "expected sidecar for every hybrid row")
    require(sidecars["summary"]["all_hybrid_rows_have_sidecars"] is True, "missing sidecars")
    require(sidecars["summary"]["all_sidecars_diagonal_only"] is True, "sidecars should be diagonal only")
    require(sidecars["accepted_as_precision_sidecars"] is True, "sidecars not accepted")
    require(sidecars["accepted_as_full_covariance_profile"] is False, "full covariance overclaimed")
    for row in rows:
        require(row["relative_uncertainty"] > 0.0, "relative uncertainty must be positive")
        require(row["absolute_uncertainty_GeV"] > 0.0, "absolute uncertainty must be positive")
        require(row["accepted_as_uncertainty_sidecar"] is True, "row sidecar not accepted")
        require(row["accepted_as_full_covariance_profile"] is False, "row covariance overclaimed")

    require(envelope["diagonal_sigma_GeV"] > 0.0, "diagonal sigma missing")
    require(envelope["accepted_as_diagonal_uncertainty_envelope"] is True, "envelope not accepted")
    require(envelope["accepted_as_full_covariance_profile"] is False, "envelope overclaimed")
    require(abs(envelope["pull_vs_reference_diagonal_only"]) < 2.0, "diagonal pull unexpectedly large")

    require(gate["precision_promotion_accepted"] is False, "precision promotion overclaimed")
    require("uniform precision Higgs partial-width formula rows" in updated["remaining_true_equivalence_blockers"], "uniform row blocker missing")
    require("full cross-channel Higgs covariance/profile likelihood" in updated["remaining_true_equivalence_blockers"], "covariance blocker missing")
    require(updated["guardrails"]["diagonal_sidecars_not_full_covariance"] is True, "diagonal guard missing")

    for packet in [sidecars, envelope, gate, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("diagonal-only" in note, "note missing diagonal-only guard")
    require("not precision" in note, "note missing precision guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
