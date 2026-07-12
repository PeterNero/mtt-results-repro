"""Audit precision value emission attempt or Qa/SU3 source payload fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRECISION_VALUES = PACKET_DIR / "partial_precision_value_emission.packet.json"
QASU3_ATTEMPT = PACKET_DIR / "qasu3_source_payload_fill_attempt.packet.json"
PROMOTION = PACKET_DIR / "true_equivalence_promotion_decision_after_value_attempt.packet.json"
CUTSET = PACKET_DIR / "next_value_completion_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrecisionValueEmissionAttempt_or_QaSU3SourcePayloadFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PRECISIONVALUEEMISSIONATTEMPT_OR_QASU3SOURCEPAYLOADFILL_BUILT_PARTIAL_VALUES_QASU3_OPEN"
NEXT = "MTT_Selected_FullProfileMatrixReconstruction_or_QaSU3ActualPacketSearch_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    precision = load(PRECISION_VALUES)
    qasu3 = load(QASU3_ATTEMPT)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(precision["row_count"] == 6, "precision row count mismatch")
    require(precision["passes_coarse_diagonal_profile"] is True, "diagonal profile not passing")
    require(precision["passes_core_correlation_envelope"] is True, "core envelope not passing")
    require(precision["passes_extreme_correlation_stress_envelope"] is False, "extreme envelope unexpectedly passing")
    require(precision["accepted_as_value_emission_attempt"] is True, "value attempt not accepted")
    require(precision["accepted_as_full_true_equivalence_profile"] is False, "full profile overaccepted")
    for row in precision["value_rows"]:
        require(row["accepted_as_partial_precision_value"] is True, "row not accepted as partial value")
        require(row["accepted_as_full_correlated_profile_value"] is False, "row overaccepted as full correlated value")

    require(qasu3["source_payload_filled"] is False, "Qa/SU3 source payload overfilled")
    require(qasu3["accepted_as_actual_QaSU3_operator_upgrade"] is False, "Qa/SU3 overaccepted")
    require(qasu3["accepted_for_true_SM_equivalence"] is False, "Qa/SU3 true equivalence overaccepted")
    require(qasu3["accepted_for_no_knob"] is False, "Qa/SU3 no-knob overaccepted")
    require(all(value is None for value in qasu3["source_payload_fields"].values()), "Qa/SU3 fields unexpectedly filled")

    require(promotion["route_A_precision_values"]["partial_values_emitted"] is True, "route A partial missing")
    require(promotion["route_A_precision_values"]["full_profile_values_filled"] is False, "route A full overfilled")
    require(promotion["route_A_precision_values"]["can_close_true_SM_equivalence_now"] is False, "route A overcloses")
    require(promotion["route_B_qasu3_payload"]["source_payload_filled"] is False, "route B overfilled")
    require(promotion["route_B_qasu3_payload"]["can_close_true_SM_equivalence_now"] is False, "route B overcloses")
    require(promotion["true_SM_equivalence_closed"] is False, "promotion overcloses true equivalence")
    require(promotion["no_knob_closed"] is False, "promotion overcloses no-knob")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    require("full non-Higgs covariance/profile matrix or likelihood workspace" in cutset["remaining_minimal_payloads"], "full profile payload missing")
    require("actual selected Qa/SU3 source/operator packet" in cutset["remaining_minimal_payloads"], "Qa/SU3 payload missing")
    require(cutset["true_SM_equivalence_closed"] is False, "cutset true overclosed")

    require(data["closure_decision"]["partial_precision_values_emitted"] is True, "candidate partial values missing")
    require(data["closure_decision"]["qasu3_source_payload_filled"] is False, "candidate Qa/SU3 overfilled")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true overclosed")
    require(cert["partial_precision_values_emitted"] is True, "certificate partial missing")
    require(cert["qasu3_source_payload_filled"] is False, "certificate Qa/SU3 overfilled")
    require("full covariance/profile likelihood is still absent" in note, "note missing guardrail")

    for packet in [precision, qasu3, promotion, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
