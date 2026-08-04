"""Audit ten-channel Higgs covariance/profile and branching-ratio replay gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TOTAL = PACKET_DIR / "ten_channel_total_width_diagonal_profile.packet.json"
BRANCHING = PACKET_DIR / "ten_channel_branching_ratio_replay.packet.json"
JACOBIAN = PACKET_DIR / "branching_ratio_diagonal_covariance_jacobian.packet.json"
DECISION = PACKET_DIR / "precision_total_width_and_branching_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsTenChannelCovarianceProfile_or_BranchingReplay_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSTENCHANNELCOVARIANCEPROFILE_OR_BRANCHINGREPLAY_BUILT_DIAGONAL_REPLAY_PRECISION_OPEN"
NEXT = "MTT_Selected_HiggsPrecisionRows_or_FullCorrelatedProfile_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    total = load(TOTAL)
    branching = load(BRANCHING)
    jacobian = load(JACOBIAN)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(data["target_fitting_used"] is False, "target fitting guard missing")

    require(total["summary"]["channel_count"] == 10, "total profile channel count mismatch")
    require(total["summary"]["computed_proxy_channel_count"] == 7, "computed channel count mismatch")
    require(total["summary"]["external_fill_channel_count"] == 3, "external fill count mismatch")
    require(total["summary"]["accepted_as_total_width_replay_scaffold"] is True, "total replay scaffold missing")
    require(total["summary"]["accepted_as_precision_total_width"] is False, "precision total width overclaimed")
    require(total["summary"]["accepted_as_full_correlated_profile"] is False, "full profile overclaimed")
    require(total["summary"]["diagonal_total_sigma_GeV"] > 0.0, "total sigma missing")
    require(abs(total["summary"]["relative_residual_to_reference"] - 0.1067259673689987) < 1e-12, "total residual changed unexpectedly")

    require(len(branching["rows"]) == 10, "branching row count mismatch")
    require(abs(branching["summary"]["branching_ratio_sum"] - 1.0) < 1e-12, "branching ratios do not sum to one")
    require(branching["summary"]["accepted_as_branching_replay_scaffold"] is True, "branching scaffold missing")
    require(branching["summary"]["accepted_as_precision_branching_ratios"] is False, "precision branching overclaimed")
    require(branching["summary"]["normalization_uses_current_mixed_proxy_import_widths"] is True, "mixed scaffold guard missing")

    require(jacobian["summary"]["input_dimension"] == 10, "jacobian input dimension mismatch")
    require(jacobian["summary"]["output_dimension"] == 10, "jacobian output dimension mismatch")
    require(jacobian["summary"]["propagates_total_width_normalization_uncertainty"] is True, "normalization propagation missing")
    require(jacobian["summary"]["accepted_as_diagonal_error_propagation"] is True, "diagonal propagation missing")
    require(jacobian["summary"]["accepted_as_full_correlated_profile"] is False, "jacobian overaccepted")
    require(len(jacobian["jacobian_dBR_dGamma"]) == 10, "jacobian row count mismatch")
    require(all(len(row) == 10 for row in jacobian["jacobian_dBR_dGamma"]), "jacobian column count mismatch")
    require(all(value >= 0.0 for value in jacobian["output_diagonal_variances"].values()), "negative BR variance")

    require(decision["total_width_replay_built"] is True, "decision total replay missing")
    require(decision["branching_ratio_replay_built"] is True, "decision branching replay missing")
    require(decision["diagonal_covariance_propagation_built"] is True, "decision covariance propagation missing")
    require(decision["precision_total_width_closed"] is False, "decision precision total width overclosed")
    require(decision["precision_branching_ratios_closed"] is False, "decision precision branching overclosed")
    require(decision["values_promotable_to_precision_now"] is False, "precision overpromoted")

    require(data["closure_decision"]["branching_ratio_replay_built"] is True, "candidate branching replay missing")
    require(data["closure_decision"]["precision_total_width_closed"] is False, "candidate total width overclosed")
    require(data["closure_decision"]["precision_branching_ratios_closed"] is False, "candidate branching overclosed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not precision branching ratios" in note, "note missing precision guard")

    for packet in [total, branching, jacobian, decision, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
