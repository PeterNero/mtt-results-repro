"""Audit PhiFinC1 dynamic-transfer proof / first independent row formula run gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinc1dynamictransferidentityproof_or_firstindependentrowformularun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PHIFIN = PACKET_DIR / "phifinc1_dynamic_transfer_identity_proof_attempt.packet.json"
FIRST_ROW = PACKET_DIR / "first_independent_row_formula_run_attempt.packet.json"
DECISION = PACKET_DIR / "phifinc1_or_firstrow_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1DynamicTransferIdentityProof_or_FirstIndependentRowFormulaRun_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_phifinc1dynamictransferidentityproof_or_firstindependentrowformularun.py"

STATUS = "MTT_SELECTED_PHIFINC1DYNAMICTRANSFERIDENTITYPROOF_OR_FIRSTINDEPENDENTROWFORMULARUN_ATTEMPTED_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1PrimitiveOverlap_or_FirstRowKernelFormulaSource_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    phifin = load(PHIFIN)
    first_row = load(FIRST_ROW)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require("stationary `Phi_fin` trace is closed" in note, "note misses stationary trace result")

    require(phifin["status"] == "STATIONARY_PHIFIN_TRACE_CLOSED_DIFFERENTIATED_C1_IDENTITY_OPEN", "PhiFin status mismatch")
    require(phifin["stationary_trace_layer_closed"] is True, "stationary trace not closed")
    require(phifin["stationary_trace_sufficient_for_C1_transfer_identity"] is False, "stationary trace overpromoted")
    require(phifin["selected_identity_proved_now"] is False, "PhiFin identity overproved")
    require(len(phifin["target_identity"]) == 7, "target identity count mismatch")
    require(len(phifin["minimal_missing_equations"]) == 4, "missing equations mismatch")
    require("primitive C1 overlap contractions" in phifin["missing_dynamic_objects"], "primitive overlap missing")
    require(phifin["if_future_identity_proved_then_values"]["A_transpose_b"] == [12.0, 12.0], "PhiFin b mismatch")

    require(first_row["status"] == "FIRST_ROW_ALGEBRAIC_VALUE_READY_INDEPENDENT_FORMULA_SOURCE_OPEN", "first row status mismatch")
    require(first_row["row_id"] == "u:phase:r0c0", "first row id mismatch")
    require(first_row["matrix_coordinate"] == {"row": 0, "column": 0}, "first row coordinate mismatch")
    require(abs(first_row["algebraic_support_value"] - (4.0 / 3.0)) < 1e-12, "first row algebraic value mismatch")
    require(first_row["value_source"] == "R_Z", "first row value source mismatch")
    require(all(first_row["available_support"].values()), "first row support missing")
    require(first_row["selected_primitive_kernel_formula"] is None, "first row formula overfilled")
    require(first_row["selected_trace_or_pairing_source"] is None, "first row pairing overfilled")
    require(first_row["computed_complex_entry_value_independent"] is None, "first row independent value overfilled")
    require(first_row["exactness_or_error_bound_certificate"] is None, "first row cert overfilled")
    require(first_row["provenance_independent_of_residual_projector_replay"] is False, "first row provenance overfilled")
    require(first_row["first_row_independently_executed_now"] is False, "first row overexecuted")

    require(decision["status"] == "PHIFINC1_IDENTITY_AND_FIRST_ROW_ATTEMPTED_NEITHER_CLOSED", "decision status mismatch")
    require(decision["stationary_PhiFin_trace_closed"] is True, "decision stationary not closed")
    require(decision["differentiated_PhiFinC1_identity_closed"] is False, "decision PhiFin overclosed")
    require(decision["first_independent_row_formula_executed"] is False, "decision first row overclosed")
    require(decision["source_gap_not_numeric_gap"] is True, "source-gap conclusion missing")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    for label, payload in [
        ("candidate", data),
        ("phifin", phifin),
        ("first_row", first_row),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
