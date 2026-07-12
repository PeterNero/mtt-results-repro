"""Audit fourth Qa/SU3 operator-source slot attempt for visible Chern-Weil source."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fourthqasu3operatorslotclosure_or_visiblechernweilsource"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ATTEMPT = PACKET_DIR / "fourth_qasu3_visible_chern_weil_slot_attempt.packet.json"
CUTSET = PACKET_DIR / "visible_chern_weil_minimal_cutset.packet.json"
DECISION = PACKET_DIR / "true_equivalence_decision_after_chern_weil_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FourthQaSU3OperatorSlotClosure_or_VisibleChernWeilSource_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FOURTHQASU3OPERATORSLOTCLOSURE_OR_VISIBLECHERNWEILSOURCE_BUILT_SLOT_STILL_OPEN_CUTSET_LOCKED"
NEXT = "MTT_Selected_VisibleChernWeilSourceProof_or_RouteCResidualAndDEValueFill_v1"
SLOT = "same_source_Chern_Weil_row_derived"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    attempt = load(ATTEMPT)
    cutset = load(CUTSET)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(attempt["attempted_slot"] == SLOT, "attempted slot mismatch")
    support = attempt["available_support"]
    for key, value in support.items():
        require(value is True, f"expected support missing: {key}")
    blockers = attempt["blocking_evidence"]
    require(blockers["visible_cw_selected_visible_operator_source_closed"] is False, "visible source overclosed")
    require(blockers["visible_cw_same_source_cut_set_requires_chern_weil"] is True, "Chern-Weil cutset missing")
    require(blockers["visible_gs_curvature_alone_insufficient"] is True, "GS insufficiency missing")
    require(blockers["rank2_same_source_chern_weil_gs_row_closed"] is False, "rank2 Chern-Weil overclosed")
    require(blockers["operator_identity_requires_chern_weil"] is True, "operator identity Chern-Weil gate missing")
    result = attempt["attempt_result"]
    require(result["fourth_operator_source_slot_closed"] is False, "fourth slot overclosed")
    require(result["selected_source_value_emitted"] is False, "selected value overemitted")
    status = attempt["slot_status_after_attempt"]
    require(status["filled_operator_slot_count"] == 3, "filled slot count changed incorrectly")
    require(status["remaining_missing_slot_count"] == 5, "remaining slot count changed incorrectly")
    require(SLOT in status["missing_slots"], "Chern-Weil slot disappeared")

    require(cutset["status"] == "VISIBLE_CHERN_WEIL_SLOT_OPEN_MINIMAL_CUTSET_LOCKED", "cutset status mismatch")
    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    for required in [
        "selected visible SM bundle/sheaf or selected Route-C source on q79/F,m=1",
        "derivation of Tr_F_visible^2 or equivalent Chern/Bianchi row from that same source",
        "non-split stability/HYM witness or selected Route-C residual with selected_source_verified true",
        "typed transition/rhoE/D_E payload tying the Chern-Weil row to operator data",
    ]:
        require(required in cutset["minimal_payload_that_would_close"], f"missing cutset payload: {required}")
    for forbidden in [
        "copying the visible GS curvature row as if it were same-source Chern-Weil derivation",
        "using closed source-level gerbe support as operator-level D_E/rhoE data",
    ]:
        require(forbidden in cutset["forbidden_shortcuts"], f"missing forbidden shortcut: {forbidden}")

    require(decision["operator_source_slots_closed"] == 3, "decision closed slots mismatch")
    require(decision["operator_source_slots_remaining"] == 5, "decision remaining slots mismatch")
    require(decision["chern_weil_slot_closed"] is False, "decision Chern-Weil overclosed")
    require(decision["visible_green_schwarz_support_retained"] is True, "decision support not retained")
    require(decision["actual_dynamic_QaSU3_operator_packet_closed"] is False, "decision dynamic overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "decision true equivalence overclosed")
    require(decision["no_knob_closed"] is False, "decision no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["fourth_QaSU3_operator_source_slot_closed"] is False, "candidate fourth slot overclosed")
    require(closure["operator_source_slots_closed_total"] == 3, "candidate closed slots mismatch")
    require(closure["operator_source_slots_remaining"] == 5, "candidate remaining slots mismatch")
    require(data["what_closes_now"]["same_source_chern_weil_no_overclaim_guardrail"] is True, "guardrail missing")
    require(data["what_closes_now"]["visible_chern_weil_minimal_cutset_locked"] is True, "cutset close flag missing")
    require(data["what_remains_open"]["same_source_Chern_Weil_row"] is True, "Chern-Weil gate missing")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")
    require("does not close" in note, "note missing no-close statement")
    require("Copying the closed curvature row would be an overclaim" in note, "note missing overclaim guard")

    for packet in [data, attempt, cutset, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
