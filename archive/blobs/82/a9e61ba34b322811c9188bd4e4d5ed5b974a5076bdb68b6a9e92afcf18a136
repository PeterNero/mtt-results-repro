"""Audit same-branch / independent Hessian bridge."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samebranchphifinc1sourceemission_or_independenthessianquadratureexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BRIDGE = PACKET_DIR / "samebranch_or_independent_bridge_decision.packet.json"
PATCHED = PACKET_DIR / "patched_smparity_dynamic_c1_import.packet.json"
UNPATCHED = PACKET_DIR / "unpatched_noknob_remaining_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameBranchPhiFinC1SourceEmission_or_IndependentHessianQuadratureExecution_v1.md"

STATUS = "MTT_SELECTED_SAMEBRANCH_PHIFINC1_OR_INDEPENDENTHESSIAN_BUILT_PATCHED_PARITY_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_FinalIntegratedSMParityReplayAfterSourceIdentityPatch_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    bridge = load(BRIDGE)
    patched = load(PATCHED)
    unpatched = load(UNPATCHED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["patched"] is True, "patched theorem flag missing")
    require(data["SM_parity_closed"] is True, "SM parity reopened")
    require(data["SM_parity_dynamic_C1_closed_under_local_principle"] is True, "patched dynamic C1 not closed")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "unqualified closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    route_a = bridge["same_branch_route_A"]
    route_b = bridge["independent_route_B"]
    require(route_a["status"] == "OPEN", "Route A overclosed")
    require(route_a["unpatched_phifin_c1_action_identity"] is False, "Route A identity overclosed")
    require(route_b["status"] == "CLOSED_FOR_PATCHED_SM_PARITY_SPINE", "Route B patched close missing")
    require(route_b["strict_110row_source_id_validator_ok_under_local_principle"] is True, "110-row validator did not pass")
    require(route_b["primitive_rows"] == 72, "primitive row count mismatch")
    require(route_b["hessian_source_rows"] == 2, "hessian row count mismatch")
    require(route_b["sector_rows"] == 36, "sector row count mismatch")
    require(route_b["same_source_b_selected_under_local_principle"] is True, "b_selected not promoted under principle")
    require(route_b["source_independence_from_residual_replay_under_local_principle"] is True, "independence not promoted under principle")

    require(patched["SM_parity_dynamic_C1_closed_under_local_principle"] is True, "patched import not closed")
    require(patched["validator"]["ok"] is True, "patched validator failed")
    require(patched["value_layer"]["patched_dynamic_C1_packet_closed"] is True, "patched value layer not closed")
    require(patched["value_layer"]["patched_deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(unpatched["no_knob_closed"] is False, "unpatched no-knob overclosed")
    require(unpatched["true_SM_equivalence_closed"] is False, "unpatched true equivalence overclosed")
    for value in unpatched["not_regressions"].values():
        require(value is True, "regression guard missing")

    require(cert["patched_route_B_source_validator_ok"] is True, "certificate validator missing")
    require(cert["patched_SM_parity_dynamic_C1_source_and_value_interface_closed"] is True, "certificate patched close missing")
    require(cert["unpatched_no_knob_dynamic_C1_closed"] is False, "certificate no-knob overclosed")
    require("This is not a no-knob derivation" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
