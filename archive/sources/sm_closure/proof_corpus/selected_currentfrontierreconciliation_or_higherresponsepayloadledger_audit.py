"""Audit current frontier reconciliation and higher-response payload ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_currentfrontierreconciliation_or_higherresponsepayloadledger"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SCOPE = PACKET_DIR / "scope_reconciliation_after_first_response.packet.json"
PAYLOAD = PACKET_DIR / "higher_response_payload_ledger_update.packet.json"
NEXT = PACKET_DIR / "next_cutset_after_current_frontier_reconciliation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CurrentFrontierReconciliation_or_HigherResponsePayloadLedger_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_CURRENTFRONTIERRECONCILIATION_OR_HIGHERRESPONSEPAYLOADLEDGER_"
    "BUILT_FIRST_RESPONSE_RETIRED_HIGHER_RESPONSE_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_HigherResponsePayloadRows_SourcePromotion_or_FullS2ValueExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    scope = load(SCOPE)
    payload = load(PAYLOAD)
    next_cutset = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True, "theorem should be proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")

    first = scope["first_response_scope"]
    for key in [
        "VSD01_source_stack_closed",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "all_72_primitive_rows_exact",
        "formal_110_rows_executed",
        "same_source_dynamic_matter_packet_closed",
        "dynamic_QaSU3_first_response_layer_closed",
    ]:
        require(first[key] is True, f"first-response field not closed: {key}")
    require(first["sector_matrix_rows"] == 36, "sector matrix row count mismatch")

    for key, value in scope["retired_first_response_labels"].items():
        require(value is True, f"first-response label not retired: {key}")

    reinterpret = scope["postsource_frontier_reinterpretation"]
    require(reinterpret["old_postsource_open_flags_are_not_source_assembly_absence"] is True, "reinterpretation missing")
    require(reinterpret["route_test_missing_A_b_deltaTheta_is_stale_for_first_response"] is True, "route test stale flag missing")
    require("full-S2" in reinterpret["still_open_meaning"], "full-S2 meaning missing")

    higher = scope["full_S2_higher_response_scope"]
    require(higher["first_response_only_is_insufficient_for_scalar_values"] is True, "first-response no-go missing")
    require(higher["higher_response_Rtheta_functional_contract_closed"] is True, "higher response contract missing")
    require(higher["higher_response_Rtheta_executed"] is False, "higher response overexecuted")
    require(higher["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(higher["full_no_knob_closed"] is False, "no-knob overclosed")

    require(payload["previous_inventory"]["old_accepted_dynamic_payload_row_count"] == 0, "old count mismatch")
    require(payload["counts"]["closed_first_response_rows"] == 4, "first-response row count mismatch")
    require(payload["counts"]["closed_higher_response_scalar_payload_rows"] == 0, "scalar rows overclosed")
    require(payload["counts"]["retired_first_response_labels"] == 5, "retired label count mismatch")
    require("finite_Hessian_C1_source" in payload["closed_first_response_rows"], "hessian row missing")
    require("primitive_C1_contractions" in payload["closed_first_response_rows"], "primitive row missing")
    require("sector_response_matrices" in payload["closed_first_response_rows"], "sector row missing")
    require("scalar_Rtheta_value_rows" in payload["still_open_payload_rows"], "scalar rows should remain open")
    require("HYM_projector_zero_mode_basis_values" in payload["still_open_payload_rows"], "HYM payload should remain open")
    require(payload["guardrail"]["do_not_reuse_first_response_as_scalar_mass_fit"] is True, "scalar fit guard missing")
    require(payload["guardrail"]["do_not_count_surrogate_or_profile_values_as_no_knob_derivation"] is True, "profile guard missing")

    require(next_cutset["recommended_next"]["artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(len(next_cutset["lanes"]) == 3, "lane count mismatch")
    require(next_cutset["still_open"]["higher_response_Rtheta_execution"] is True, "higher response not open")
    require(next_cutset["still_open"]["full_S2_value_emission"] is True, "full S2 not open")
    require(next_cutset["still_open"]["full_no_knob"] is True, "no-knob not open")

    closure = data["closure_decision"]
    require(closure["first_response_scope_closed"] is True, "first response not closed")
    for key in [
        "higher_response_payload_rows_closed",
        "full_S2_value_execution_closed",
        "Yukawa_mass_mixing_value_closure",
        "lambda_H_value_execution",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require(data["what_closes_now"]["stale_first_response_A_b_deltaTheta_blockers_retired"] is True, "stale blockers not retired")
    require(data["what_closes_now"]["higher_response_payload_ledger_updated"] is True, "ledger update missing")
    require(data["closure_claimed"] is False, "candidate should not claim full closure")
    require(cert["closure_claimed"] is False, "certificate should not claim closure")

    for packet in [data, scope, payload, next_cutset, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("first-response closure packets" in note, "note reconciliation missing")
    require("Not closed:" in note, "note open frontier missing")
    require("first response is not a scalar mass fit" in note, "note guardrail missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
