"""Audit Higgs EW formula-kernel/precision-import execution gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsewformulakernelexecution_or_precisionimportrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
READINESS = PACKET_DIR / "ew_formula_kernel_execution_readiness.packet.json"
IMPORT_CONTRACT = PACKET_DIR / "ew_precision_import_row_contract.packet.json"
DIAGONAL = PACKET_DIR / "ew_three_channel_diagonal_profile_fallback.packet.json"
STRESS = PACKET_DIR / "ew_three_channel_correlation_stress_profile.packet.json"
DECISION = PACKET_DIR / "precision_import_decision_after_ew_profile.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsEWFormulaKernelExecution_or_PrecisionImportRows_v1.md"

STATUS = "MTT_SELECTED_HIGGSEWFORMULAKERNELEXECUTION_OR_PRECISIONIMPORTROWS_BUILT_PROFILE_IMPORT_GATE_VALUES_OPEN"
NEXT = "MTT_Selected_HiggsTenChannelCovarianceProfile_or_BranchingReplay_v1"
CHANNELS = {"H_to_WW_star", "H_to_ZZ_star", "H_to_Z_gamma"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    readiness = load(READINESS)
    contract = load(IMPORT_CONTRACT)
    diagonal = load(DIAGONAL)
    stress = load(STRESS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(data["target_fitting_used"] is False, "target fitting guard missing")
    require(set(row["channel"] for row in readiness["rows"]) == CHANNELS, "readiness channels mismatch")
    require(readiness["summary"]["formula_kernels_filled"] == 0, "formula kernels overfilled")
    require(readiness["summary"]["formula_kernels_open"] == 3, "formula kernel open count mismatch")
    require(set(row["channel"] for row in contract["rows"]) == CHANNELS, "contract channels mismatch")
    require(contract["summary"]["accepted_precision_import_count"] == 0, "precision imports overaccepted")
    require(contract["summary"]["central_values_used_as_replay_inputs_only"] is True, "replay-only guard missing")
    require(diagonal["summary"]["channel_count"] == 3, "diagonal channel count mismatch")
    require(diagonal["summary"]["all_rows_zero_residual_by_import_identity"] is True, "import identity residual mismatch")
    require(diagonal["summary"]["accepted_as_formula_validation"] is False, "diagonal profile overvalidated")
    require(diagonal["summary"]["accepted_as_full_correlated_profile"] is False, "diagonal profile overaccepted")
    require(abs(diagonal["summary"]["diagonal_chi_square"]) < 1e-24, "diagonal chi-square should be zero")
    require(stress["summary"]["stress_models_checked"] == 4, "stress grid count mismatch")
    require(stress["summary"]["all_models_psd_by_equicorrelation_bound"] is True, "stress PSD guard failed")
    require(stress["summary"]["accepted_as_formula_validation"] is False, "stress overvalidated")
    require(stress["summary"]["accepted_as_full_correlated_profile"] is False, "stress overaccepted")
    require(abs(stress["summary"]["min_chi_square"]) < 1e-24, "stress min chi-square should be zero")
    require(abs(stress["summary"]["max_chi_square"]) < 1e-24, "stress max chi-square should be zero")
    require(decision["formula_kernel_readiness_built"] is True, "decision readiness missing")
    require(decision["precision_import_contract_built"] is True, "decision contract missing")
    require(decision["values_promotable_to_precision_total_width_now"] is False, "precision overpromoted")
    require(data["closure_decision"]["precision_import_rows_accepted"] is False, "candidate imports overaccepted")
    require(data["closure_decision"]["precision_total_width_closed"] is False, "candidate precision total width overclosed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not formula validation" in note, "note missing validation guard")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
