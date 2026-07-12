"""Audit the strict-global / true-SM frontier separation after AH8."""

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
BUILDER = ROOT / "scripts" / "build_selected_strictglobalcechhym_or_truesmafterah8.py"

SLUG = "selected_strictglobalcechhym_or_truesmafterah8"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictGlobalCechHYMProvenance_or_TrueSMClosureAfterAH8_v1.md"
AH8_LOCK = PACKET_DIR / "ah8_consumed_nonreopen_lock.packet.json"
STRICT_CUTSET = PACKET_DIR / "strict_global_literal_witness_cutset.packet.json"
TRUE_SM_ROUTE = PACKET_DIR / "true_sm_after_ah8_route_split.packet.json"
NEXT_PACKET = PACKET_DIR / "next_literal_witness_or_precision_values_after_ah8.packet.json"

STATUS = "MTT_SELECTED_STRICTGLOBALCECHHYM_OR_TRUESMAFTERAH8_AH8_CONSUMED_STRICT_WITNESSES_AND_PRECISION_VALUES_OPEN"
NEXT = "MTT_Selected_LiteralGoodCoverHYMGlobalWitness_or_PrecisionValueSourceAfterAH8_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    ah8 = load(AH8_LOCK)
    strict = load(STRICT_CUTSET)
    true_sm = load(TRUE_SM_ROUTE)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, ah8, strict, true_sm, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["AH8_consumed_and_locked"] is True, "AH8 not locked")
    require(decision["BN27_AH_equivalent_matrix_row_no_longer_blocker"] is True, "BN27 row still marked blocker")
    require(decision["strict_global_reduced_to_two_literal_witness_families"] is True, "strict cutset not reduced")
    require(decision["literal_good_cover_Cech_witness_family_closed"] is False, "Cech witness overclosed")
    require(decision["literal_global_HYM_witness_family_closed"] is False, "HYM witness overclosed")
    require(decision["strict_global_closed"] is False, "strict global overclosed")
    require(decision["minimal_parameter_ledger_closed"] is True, "ledger regressed")
    require(decision["precision_profile_table_built"] is True, "precision table regressed")
    require(decision["qasu3_source_slot_layer_closed"] is True, "Qa/SU3 source slots regressed")
    require(decision["precision_value_source_rows_closed"] is False, "precision rows overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(ah8["AH_equivalent_BN27_lane_closed"] is True, "AH8 packet not closed")
    require(ah8["accepted_count"] == 8, "AH8 accepted count")
    require("two-premise AH-equivalent" in ah8["accepted_scope"], "AH8 scope")
    for item in [
        "finite projected A_N exactness",
        "transported D_E/dotD/projector/rho_s source flags",
        "projected Route-C full-sector offdiagonal control",
        "AH-equivalent BN27 HYM row acceptance",
    ]:
        require(item in ah8["do_not_reopen"], f"missing non-reopen item: {item}")

    require(strict["strict_global_closed"] is False, "strict packet overclosed")
    require(strict["strict_global_can_be_closed_by_existing_support_packets"] is False, "support packets overpromoted")
    require(strict["strict_original_connection_tables_accepted"] == 4, "strict original count changed")
    require(strict["one_premise_connection_tables_accepted"] == 6, "one-premise count changed")
    require(strict["AH_equivalent_connection_tables_accepted"] == 8, "AH count changed")
    families = strict["literal_witness_families_required"]
    require(len(families) == 2, "literal witness family count")
    require(families[0]["accepted_now"] is False, "Cech family accepted")
    require(families[1]["accepted_now"] is False, "HYM family accepted")
    for field in ["good_cover", "A_ij", "B_i", "g_ijk", "h_ij", "transition_functions"]:
        require(field in families[0]["required_fields"], f"Cech field missing: {field}")
    for field in ["connection_coefficients", "endomorphism_E", "finite_determinant_part"]:
        require(field in families[1]["required_fields"], f"HYM field missing: {field}")

    require(true_sm["BN27_AH_equivalent_matrix_row_no_longer_blocker"] is True, "true-SM route reopens BN27")
    require(true_sm["true_SM_equivalence_closed"] is False, "true-SM route overclosed")
    require(true_sm["minimal_parameter_ledger_closed"] is True, "route ledger")
    require(true_sm["precision_profile_table_built"] is True, "route precision")
    require(true_sm["qasu3_source_slot_layer_closed"] is True, "route Qa/SU3 slots")
    require(true_sm["accepted_true_equivalence_rows"] == 0, "accepted true-equivalence rows changed")
    require("selected_QaSU3_operator_payload_closed" in true_sm["remaining_precision_value_gates"], "precision blocker missing")
    require("selected_C1_response_closed" in true_sm["remaining_qasu3_value_gates"], "Qa/SU3 blocker missing")

    for blocked in [
        "do not treat AH representative as literal good-cover data",
        "do not treat finite projected HYM representative as continuum/global coefficients",
        "do not treat minimal parameter ledger as true precision equivalence",
    ]:
        require(blocked in next_packet["blocked_replays"], f"blocked replay missing: {blocked}")

    require(cert["AH8_consumed_and_locked"] is True, "cert AH8")
    require(cert["strict_global_reduced_to_two_literal_witness_families"] is True, "cert strict cutset")
    require(cert["strict_global_closed"] is False, "cert strict")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("AH-equivalent BN27 connection-table lane is consumed and locked" in note, "note AH8 lock")
    require("literal good-cover Deligne-Cech data" in note, "note Cech")
    require("literal global HYM/projective connection data" in note, "note HYM")
    require(NEXT in note, "note next")

    print("Strict-global / true-SM after-AH8 audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
