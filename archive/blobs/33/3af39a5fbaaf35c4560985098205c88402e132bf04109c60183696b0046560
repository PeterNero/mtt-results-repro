"""Validate the finite C1 source-identity theorem fork artifact."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "selected_finitec1_sourceidentity_theorem_fork.import.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    closure = packet["closure_claimed"]
    support = packet["available_support"]
    obstruction = packet["unpatched_obstructions"]
    route_a = packet["route_A_unpatched_proof_obligations"]
    route_b = packet["route_B_explicit_source_principle"]

    require(packet["status"] == "CONSTRUCTED_THEOREM_FORK_PATCH_READY_UNPATCHED_PROOF_OPEN", "bad status")
    require(packet["target_fitting_used"] is False, "target fitting must be false")
    require(packet["observed_physical_data_used_as_selector"] is False, "observed selector must be false")

    require(closure["patched_dynamic_C1"] is True, "patched dynamic C1 closure should be retained")
    require(closure["SM_parity_under_declared_standard"] is True, "declared SM parity closure should be retained")
    require(closure["unpatched_dynamic_C1"] is False, "unpatched dynamic C1 must remain open")
    require(closure["SelectedFiniteC1SourceIdentityTheorem"] is False, "source identity theorem must remain open")
    require(closure["true_SM_equivalence"] is False, "true SM equivalence must remain open")
    require(closure["full_no_knob_SM_closure"] is False, "full no-knob closure must remain open")

    require(support["formal_110_rows_executed"] is True, "formal 110-row support missing")
    require(support["primitive_72_postcheck_values_loaded"] is True, "primitive postcheck support missing")
    require(support["strict_validator_passes_under_explicit_principle"] is True, "principle validator support missing")

    require(obstruction["physical_action_identity_open"] is True, "physical action identity should be open")
    require(obstruction["same_source_b_selected_open"] is True, "b_selected source should be open")
    require(obstruction["non_replay_row_provenance_open"] is True, "row provenance should be open")

    for key, value in route_a.items():
        require(value is True, f"route A obligation missing: {key}")

    require(route_b["paper_ready"] is True, "source principle patch should be paper-ready")
    require(route_b["accepted_as_proof_here"] is False, "patch must not be accepted as proof here")
    require(route_b["consequences_if_inserted"]["declared_SM_parity_replay_closes"] is True, "patched consequence missing")
    require(route_b["consequences_if_inserted"]["full_no_knob_closure_still_open"] is True, "no-knob guardrail missing")

    print("Finite C1 source-identity theorem fork PASS")
    print("status", packet["status"])
    print("next", packet["next_required_artifact"])


if __name__ == "__main__":
    main()
