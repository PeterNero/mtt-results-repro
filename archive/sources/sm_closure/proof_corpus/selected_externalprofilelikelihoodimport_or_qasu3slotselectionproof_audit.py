"""Audit external profile-likelihood import or Qa/SU3 slot selection proof attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE = PACKET_DIR / "external_higgs_decay_correlation_covariance_import.packet.json"
QASU3 = PACKET_DIR / "qasu3_slot_selection_proof_attempt.packet.json"
SYNTHESIS = PACKET_DIR / "true_equivalence_frontier_synthesis.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ExternalProfileLikelihoodImport_or_QaSU3SlotSelectionProof_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_EXTERNALPROFILELIKELIHOODIMPORT_OR_QASU3SLOTSELECTIONPROOF_"
    "BUILT_CORRELATED_DECAY_COVARIANCE_SLOT_PROOF_OPEN"
)
NEXT = "MTT_Selected_AcceptedHiggsDecayCovarianceProfile_or_FirstQaSU3SelectedSlotClosure_v1"
SOURCE = "https://arxiv.org/abs/1606.00455"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_square_symmetric(matrix: list[list[float]], label: str, *, diagonal_one: bool = False) -> None:
    size = len(matrix)
    require(size > 0, f"{label} is empty")
    for i, row in enumerate(matrix):
        require(len(row) == size, f"{label} row {i} length mismatch")
        if diagonal_one:
            require(abs(row[i] - 1.0) < 1e-12, f"{label} diagonal mismatch at {i}")
        for j, value in enumerate(row):
            require(abs(value - matrix[j][i]) < 1e-12, f"{label} is not symmetric at {i},{j}")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile = load(PROFILE)
    qasu3 = load(QASU3)
    synthesis = load(SYNTHESIS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    source = profile["external_source"]
    require(source["url"] == SOURCE, "external source mismatch")
    require(source["ancillary_table"] == "tables_i.txt", "ancillary table mismatch")
    sector = profile["restricted_decay_sector"]
    require(sector["row_count"] == 9, "profile row count mismatch")
    require(len(sector["labels"]) == 9, "profile labels mismatch")
    require(len(sector["source_decay_labels"]) == 9, "source labels mismatch")
    require_square_symmetric(sector["correlation_matrix"], "correlation matrix", diagonal_one=True)
    require_square_symmetric(sector["covariance_matrix_MeV2"], "covariance matrix")
    require(len(sector["diagonal_variances_MeV2"]) == 9, "variance diagonal length mismatch")
    for index, variance in enumerate(sector["diagonal_variances_MeV2"]):
        require(variance > 0, f"nonpositive variance at row {index}")
        require(abs(variance - sector["covariance_matrix_MeV2"][index][index]) < 1e-12, f"variance mismatch at row {index}")

    result = profile["import_result"]
    require(result["external_correlated_covariance_submatrix_imported"] is True, "correlated submatrix not imported")
    require(result["covers_current_external_decay_rows"] is True, "external decay rows not covered")
    require(result["full_profile_likelihood_function_imported"] is False, "full likelihood overclaimed")
    require(result["accepted_as_Higgs_decay_covariance_profile_candidate"] is True, "profile candidate not accepted")
    require(result["accepted_as_full_true_equivalence_profile"] is False, "true-equivalence profile overclaimed")

    summary = qasu3["summary"]
    require(summary["slot_count"] == 8, "Qa/SU3 slot count mismatch")
    require(summary["support_tokens_available"] >= 7, "support tokens regressed")
    require(summary["selection_proofs_closed"] == 0, "selection proofs overclosed")
    require(summary["selected_source_values_emitted"] == 0, "selected values overemitted")
    require(summary["actual_QaSU3_operator_packet_closed"] is False, "Qa/SU3 operator packet overclosed")
    for slot, proof in qasu3["slot_selection_proofs"].items():
        require(proof["selection_proof_attempted"] is True, f"slot proof not attempted: {slot}")
        require(proof["selected_source_value_emitted"] is False, f"slot overselected: {slot}")
        require(proof["proof_status"] == "SELECTION_PROOF_OPEN", f"slot proof status mismatch: {slot}")
        require(proof["blocking_condition"], f"slot missing blocker: {slot}")
    require("support-token packet is necessary context but not sufficient" in qasu3["promotion_rule"], "promotion rule guard missing")

    require(synthesis["status"] == "HIGGS_DECAY_CORRELATED_COVARIANCE_IMPORTED_QASU3_SLOT_SELECTION_OPEN", "synthesis status mismatch")
    require("correlated covariance profile candidate" in synthesis["route_A_status"], "route A status mismatch")
    require("zero selected values emitted" in synthesis["route_B_status"], "route B status mismatch")
    require(synthesis["true_SM_equivalence_closed"] is False, "synthesis true equivalence overclosed")
    require(synthesis["no_knob_closed"] is False, "synthesis no-knob overclosed")

    decision = data["closure_decision"]
    require(decision["external_higgs_decay_covariance_profile_candidate_imported"] is True, "candidate covariance import missing")
    require(decision["full_profile_likelihood_function_imported"] is False, "candidate full likelihood overclaimed")
    require(decision["selected_operator_slot_source_values_closed"] is False, "candidate source slots overclosed")
    require(decision["actual_QaSU3_operator_packet_closed"] is False, "candidate Qa/SU3 packet overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "candidate true SM equivalence overclosed")
    require(decision["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(data["what_closes_now"]["external_correlated_covariance_submatrix_imported"] is True, "correlation import close flag missing")
    require(data["what_closes_now"]["frontier_synthesis_built"] is True, "synthesis close flag missing")
    require(data["what_remains_open"]["full_profile_likelihood_function"] is True, "likelihood gate missing")
    require(data["what_remains_open"]["selected_operator_slot_source_values"] is True, "source value gate missing")
    require(data["what_remains_open"]["actual_QaSU3_operator_packet"] is True, "operator packet gate missing")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")
    require("not a full likelihood function" in note, "note missing likelihood guard")
    require("support tokens remain support tokens" in note, "note missing support-token guard")

    for packet in [data, profile, qasu3, synthesis, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
