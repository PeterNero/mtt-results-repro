"""Audit visible Chern-Weil source proof or Route-C residual/D_E value-fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_visiblechernweilsourceproof_or_routecresidualdevaluefill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EDGE_TEST = PACKET_DIR / "rank2_and_routec_edge_test.packet.json"
ATTEMPT = PACKET_DIR / "visible_chern_weil_or_routec_value_fill_attempt.packet.json"
DECISION = PACKET_DIR / "operator_source_slot_decision_after_value_fill.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VisibleChernWeilSourceProof_or_RouteCResidualAndDEValueFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_VISIBLECHERNWEILSOURCEPROOF_OR_ROUTECRESIDUALDEVALUEFILL_BUILT_SOURCE_PROMOTION_STILL_OPEN"
NEXT = "MTT_Selected_PhiFinPayload_or_GlobalDestabilizerEnumeration_ClosingRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    edge = load(EDGE_TEST)
    attempt = load(ATTEMPT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next mismatch")

    rank2 = edge["rank2_visible_bundle_edge"]
    routec = edge["routec_value_fill_edge"]
    require(rank2["closed"] is False, "rank2 edge overclosed")
    require(routec["closed"] is False, "routec edge overclosed")
    require(rank2["support_closed"]["selected_l2_ext_input"] is True, "rank2 L2 support missing")
    require(rank2["support_closed"]["central_neutral_destabilizers_obstructed"] is True, "central-neutral support missing")
    require(rank2["missing"]["global_rank_one_torsion_free_subsheaf_enumeration"] is True, "global enumeration missing not detected")
    require(rank2["missing"]["selected_HYM_or_Strominger_existence_certificate"] is True, "HYM missing not detected")
    require(routec["lower_algebra_ready"] is True, "Route-C lower algebra not ready")
    for key in [
        "fixed_q79_branch",
        "strominger_selection_support",
        "phifin_codomain_schema",
        "formal_lift_lower_validators_all_pass",
        "DE_matrix_emitted",
        "dotD_matrix_emitted",
    ]:
        require(routec["support_closed"][key] is True, f"Route-C support missing: {key}")
    for key in [
        "Phi_fin_selected_payload",
        "quotient_valid_BN_basis_certificate",
        "selected_source_flags_promoted",
        "selected_payload_closed",
        "selected_PhiFin_alpha1_payload_values",
    ]:
        require(routec["missing"][key] is True, f"Route-C missing primitive not detected: {key}")

    support = attempt["existing_support"]
    require(support["SM_parity_closed"] is True, "SM parity support lost")
    require(support["previous_operator_source_slots_closed"] == 3, "previous slot count mismatch")
    require(support["fixed_sector_source_support_exists"] is True, "fixed-sector support missing")
    require(support["MTT_strominger_selection_support_exists"] is True, "Strominger support missing")
    require(support["lower_routec_algebra_validates_under_formal_lift"] is True, "lower algebra support missing")
    result = attempt["promotion_result"]
    require(result["source_promotion_closed"] is False, "source promotion overclosed")
    require(result["fourth_operator_source_slot_closed"] is False, "fourth slot overclosed")
    require(result["same_source_Chern_Weil_row_derived"] is False, "Chern-Weil overderived")
    require(result["selected_RouteC_residual_DE_values_emitted"] is False, "Route-C values overemitted")
    require("Promoting the diagnostic formal lift would overclaim" in result["why_not_closed"], "formal-lift guard missing")

    require(decision["operator_source_slots_closed"] == 3, "decision closed slot count changed")
    require(decision["operator_source_slots_remaining"] == 5, "decision remaining slot count changed")
    require(decision["fourth_operator_source_slot_closed"] is False, "decision fourth slot overclosed")
    require(decision["lower_routec_algebra_ready"] is True, "decision lower algebra not ready")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")

    closure = data["closure_decision"]
    require(closure["fourth_QaSU3_operator_source_slot_closed"] is False, "candidate fourth slot overclosed")
    require(closure["operator_source_slots_closed_total"] == 3, "candidate closed slots mismatch")
    require(closure["operator_source_slots_remaining"] == 5, "candidate remaining slots mismatch")
    require(data["what_closes_now"]["both_edges_tested"] is True, "both-edge test not closed")
    require(data["what_closes_now"]["lower_routec_algebra_ready_for_honest_replay"] is True, "lower algebra readiness not recorded")
    require(data["what_remains_open"]["Phi_fin_selected_payload"] is True, "Phi_fin blocker missing")
    require(data["what_remains_open"]["quotient_valid_BN_basis_certificate"] is True, "basis blocker missing")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")

    require("It does not close the slot yet" in note, "note missing no-close statement")
    require("Promoting the diagnostic formal lift would be an overclaim" in note, "note missing guardrail")

    for packet in [data, edge, attempt, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
