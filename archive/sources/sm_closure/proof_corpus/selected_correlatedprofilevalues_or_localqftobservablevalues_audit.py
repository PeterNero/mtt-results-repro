"""Audit correlation envelope and local-QFT observable value gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_correlatedprofilevalues_or_localqftobservablevalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE = PACKET_DIR / "correlation_robust_profile_envelope.packet.json"
QFT = PACKET_DIR / "local_qft_observable_value_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_correlation_envelope.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CorrelatedProfileValues_or_LocalQFTObservableValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_CORRELATEDPROFILEVALUES_OR_LOCALQFTOBSERVABLEVALUES_BUILT_CORRELATION_ENVELOPE_QFT_VALUES_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile = load(PROFILE)
    qft = load(QFT)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    basis = profile["basis_reduction"]
    require("g_Y_Mt" in basis["independent_outputs"], "gY must remain independent")
    require(basis["redundant_outputs_removed"] == ["g_1_GUT_Mt"], "g1 redundancy not removed")
    require(len(basis["independent_outputs"]) == 5, "compressed independent basis should have five rows")
    require(profile["input_correlation_model"]["rho_values"][0] == -0.3, "rho scan lower endpoint mismatch")
    require(profile["input_correlation_model"]["rho_values"][-1] == 0.9, "rho scan upper endpoint mismatch")
    require(len(profile["scan_rows"]) == len(profile["input_correlation_model"]["rho_values"]), "scan/rho length mismatch")
    diagonal_row = next(row for row in profile["scan_rows"] if row["rho_equicorrelation"] == 0.0)
    require(abs(diagonal_row["chi2"] - basis["compressed_diagonal_chi2_without_redundant_g1_row"]) < 1e-12, "compressed diagonal chi2 mismatch")
    for row in profile["scan_rows"]:
        require(row["degrees_of_freedom"] == 5, "compressed dof mismatch")
        require(row["chi2"] >= 0.0, "negative chi2")
    envelope = profile["chi2_envelope"]
    require(envelope["min_chi2"] <= envelope["max_chi2"], "bad chi2 envelope")
    require(envelope["passes_core_correlation_envelope"] is True, "core correlation envelope should pass")
    require(envelope["passes_extreme_correlation_stress_envelope"] is False, "extreme stress envelope should remain open")
    require(profile["accepted_as_full_correlated_profile"] is False, "full correlated profile overclaimed")

    reqs = qft["required_value_rows"]
    require(qft["already_available"]["local_qft_observable_functor_interface"] is True, "QFT functor interface missing")
    require(qft["can_close_local_qft_observable_values_now"] is False, "QFT values overclaimed")
    require(any(row["id"] == "correlators_not_source_data_guard" and row["closed"] is True for row in reqs), "correlator guard missing")
    require(any(row["id"] == "representative_scattering_or_decay_rows" and row["closed"] is False for row in reqs), "observable rows should remain open")

    require("hypercharge basis reduction for correlated profile" in updated["closed_now"], "basis reduction not closed")
    require("correlation-robust profile envelope" in updated["closed_now"], "correlation envelope not closed")
    require("published/reconstructed correlated profile likelihood values" in updated["remaining_true_equivalence_blockers"], "published profile blocker missing")
    require("local QFT observable value rows" in updated["remaining_true_equivalence_blockers"], "QFT value blocker missing")
    require(updated["guardrails"]["hypercharge_not_double_counted"] is True, "hypercharge guard missing")
    require(updated["guardrails"]["correlation_envelope_is_not_published_profile"] is True, "profile guard missing")

    for key in [
        "hypercharge_basis_reduction",
        "correlation_robust_profile_envelope",
        "coarse_correlation_envelope_passes",
        "extreme_correlation_stress_envelope_open",
        "local_qft_observable_value_gate_built",
        "superset_strategy_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"missing close flag: {key}")
    require(data["closure_decision"]["full_correlated_profile_closed"] is False, "full profile overclaimed")
    require(data["closure_decision"]["local_QFT_observable_values_closed"] is False, "QFT values overclaimed")
    require(cert["next_required_artifact"] == "MTT_Selected_LocalQFTObservableRows_or_FinalTrueSMEquivalenceGap_v1", "next artifact mismatch")

    for packet in [profile, qft, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("must not be double-counted" in note, "note missing hypercharge basis guard")
    require("local-QFT observable value gate" in note, "note missing QFT gate")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
