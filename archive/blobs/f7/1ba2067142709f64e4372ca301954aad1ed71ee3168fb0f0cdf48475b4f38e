"""Audit the Higgs covariance/profile contract and uniform formula-row manifest."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgscovarianceprofilecontract_or_uniformformularows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CONTRACT = PACKET_DIR / "higgs_covariance_profile_contract.packet.json"
MANIFEST = PACKET_DIR / "uniform_higgs_formula_row_manifest.packet.json"
DIAG = PACKET_DIR / "diagonal_profile_diagnostic.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_profile_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsCovarianceProfileContract_or_UniformFormulaRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSCOVARIANCEPROFILECONTRACT_OR_UNIFORMFORMULAROWS_BUILT_PROFILE_CONTRACT_UNIFORM_ROWS_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    contract = load(CONTRACT)
    manifest = load(MANIFEST)
    diagnostic = load(DIAG)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["precision_profile_contract_closed"] is True, "contract not closed")
    require(data["closure_decision"]["uniform_formula_rows_closed"] is False, "uniform rows overclaimed")
    require(data["closure_decision"]["cross_channel_covariance_profile_closed"] is False, "profile overclaimed")

    row_basis = contract["row_basis"]
    require(len(row_basis) == 10, "expected ten Higgs channels")
    require(contract["dimension"] == 10, "dimension mismatch")
    require(contract["diagonal_fallback_from_sidecars"]["available"] is True, "diagonal fallback missing")
    require(contract["diagonal_fallback_from_sidecars"]["accepted_as_full_profile"] is False, "diagonal fallback overclaimed")
    require(
        contract["acceptance_tests"]["cross_channel_correlations_encoded_or_profiled"] is False,
        "cross-channel correlations overclaimed",
    )
    require(
        len(contract["diagonal_fallback_from_sidecars"]["diagonal_variances_GeV2"]) == 10,
        "diagonal variance count mismatch",
    )

    rows = manifest["rows"]
    require(len(rows) == 10, "formula manifest row count mismatch")
    require([row["channel"] for row in rows] == row_basis, "formula row basis mismatch")
    require(manifest["summary"]["all_rows_have_formula_family_declared"] is True, "formula families missing")
    require(manifest["summary"]["all_rows_have_operator_attachment_declared"] is True, "operator attachments missing")
    require(manifest["summary"]["all_uniform_formula_values_filled"] is False, "uniform formula values overclaimed")
    require(
        manifest["summary"]["actual_QaSU3_required_for_color_sensitive_rows"] is True,
        "Qa/SU3 requirement missing",
    )
    require(any(row["channel"] == "H_to_gg" and "Qa/SU3" in row["operator_attachment_required"] for row in rows), "gg Qa/SU3 attachment missing")

    require(diagnostic["accepted_as_diagnostic"] is True, "diagnostic not accepted")
    require(diagnostic["accepted_as_full_covariance_profile"] is False, "diagnostic overclaimed")
    require(diagnostic["ndof_included"] == 2, "diagnostic should include only bb and cc")
    require(diagnostic["diagonal_chi2_on_independent_reference_rows"] > 0.0, "diagnostic chi2 missing")
    require(diagnostic["max_abs_pull_included"] < 2.0, "diagnostic pull unexpectedly large")

    require("fill the declared uniform formula rows" in updated["next_primary_value_gate"], "next gate mismatch")
    require("full cross-channel Higgs covariance/profile likelihood" in updated["remaining_true_equivalence_blockers"], "covariance blocker missing")
    require("uniform precision Higgs partial-width formula rows" in updated["remaining_true_equivalence_blockers"], "uniform row blocker missing")
    require(updated["guardrails"]["diagonal_diagnostic_not_full_covariance"] is True, "diagonal guard missing")

    for packet in [contract, manifest, diagnostic, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("ten-channel Higgs observable vector" in note, "note missing row-basis statement")
    require("not a full" in note, "note missing precision guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
