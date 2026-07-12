"""Audit A_EW correction-factor / physical-normalization frontier run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun.py"

SLUG = "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AEWCorrectionFactorSourceTheorem_or_PhysicalNormalizationRun_v1.md"

CORRECTION_SCAN = PACKET_DIR / "aew_correction_factor_source_search.packet.json"
PHYSICAL_RUN = PACKET_DIR / "physical_normalization_or_direct_k_run.packet.json"
FRONTIER = PACKET_DIR / "active_frontier_after_aew_correction_run.packet.json"

STATUS = (
    "MTT_SELECTED_AEWCORRECTIONFACTOR_SOURCE_THEOREM_OR_PHYSICALNORMALIZATIONRUN_"
    "EXECUTED_SHARP_NEARMISS_STRICT_PEW_OPEN"
)
NEXT = "MTT_Selected_PhysicalNormalizationSourceAxiom_or_DirectKCertificate_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    correction = load(CORRECTION_SCAN)
    physical = load(PHYSICAL_RUN)
    frontier = load(FRONTIER)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, correction, physical, frontier]:
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")
        require(payload["closure_claimed"] is True, "artifact claim boundary missing")

    decision = candidate["closure_decision"]
    require(decision["correction_factor_search_executed"] is True, "correction search not executed")
    require(decision["best_base_formula"] == "8*Delta_G12/pi^2", "base formula mismatch")
    require(decision["accepted_correction_source_row_count"] == 0, "correction source row overaccepted")
    require(decision["accepted_strict_P_EW_source_rows"] == 0, "strict P_EW overaccepted")
    require(decision["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K overaccepted")
    require(decision["selected_R_H_RG_source_emitted"] is True, "finite H radial source lost")
    require(decision["strict_K_threshold_rows_closed"] == 9, "charged K row count mismatch")
    require(decision["minimal_one_primitive_ten_row_ledger_closed"] is True, "minimal one-primitive lane lost")
    require(decision["strict_no_knob_ten_row_closure"] is False, "strict ten-row overclosed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM equivalence overclosed")

    require(correction["status"] == "CORRECTION_FACTOR_SEARCH_EXECUTED_NO_ACCEPTED_SOURCE_ROW", "scan status mismatch")
    require(correction["exact_source_hits_found"] == 0, "exact hits overclaimed")
    require(correction["accepted_correction_source_row_count"] == 0, "accepted correction row mismatch")
    require(len(correction["candidate_rows"]) >= 5, "correction scan too thin")
    best = correction["candidate_rows"][0]
    require("Delta_G12^2" in best["formula"], "best correction formula changed unexpectedly")
    require(best["accepted_as_correction_source_row"] is False, "best near-miss promoted")
    require(correction["best_candidate_A_EW_relative_residual"] < 1e-10, "sharp near-miss not retained")

    require(
        physical["status"] == "PHYSICAL_NORMALIZATION_AND_DIRECT_K_RECHECK_ZERO_STRICT_ROWS",
        "physical run status mismatch",
    )
    require(physical["strict_source_required_field_count"] == 8, "strict field count mismatch")
    require(physical["strict_source_filled_field_count"] == 0, "strict field fill mismatch")
    require(physical["accepted_strict_P_EW_source_rows"] == 0, "P_EW source overaccepted")
    require(physical["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K overaccepted")
    require(physical["strict_K_rows_closed"] == 9, "strict K count mismatch")
    require(physical["minimal_one_primitive_ten_row_ledger_closed"] is True, "minimal lane not closed")
    require(physical["strict_no_knob_ten_row_closure"] is False, "strict no-knob overclosed")

    require(
        frontier["status"] == "STRICT_FRONTIER_IS_PHYSICAL_NORMALIZATION_OR_DIRECT_K_CERTIFICATE",
        "frontier status mismatch",
    )
    require("nine charged K_threshold rows" in frontier["closed_active_ledger"], "frontier lost charged K closure")
    require("selected physical gauge/action normalization P_EW or K_phys/f_ab" in frontier["still_open_strict"], "frontier lost P_EW blocker")

    require("strict charged K rows closed          : 9/10" in note, "note missing K row summary")
    require("strict no-knob ten-row closure        : false" in note, "note missing strict guard")
    require(NEXT in note, "note missing next object")

    print("AEW correction-factor source theorem audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
