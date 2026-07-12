"""Audit electroweak prefactor source closure after finite H scalar transport."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_electroweakprefactorsourceclosure_or_finaltruesmaudit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INVENTORY = PACKET_DIR / "electroweak_prefactor_source_inventory.packet.json"
SEARCH = PACKET_DIR / "source_native_prefactor_expression_search.packet.json"
FINAL_GATE = PACKET_DIR / "final_hlambda_gate_after_zero_h_knob.packet.json"
NEXT_PACKET = PACKET_DIR / "next_aew_source_operator_or_threshold_convention_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ElectroweakPrefactorSourceClosure_or_FinalTrueSMAudit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ELECTROWEAK_PREFACTOR_SOURCE_CLOSURE_OR_FINAL_TRUE_SM_AUDIT_"
    "ZERO_H_KNOB_CONFIRMED_AEW_PREFACTOR_SOURCE_OPEN"
)
NEXT = "MTT_Selected_AEWSourceOperator_or_ThresholdConventionRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    inventory = load(INVENTORY)
    search = load(SEARCH)
    final_gate = load(FINAL_GATE)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("inventory", inventory),
        ("search", search),
        ("final_gate", final_gate),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "next artifact")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    decision = data["closure_decision"]
    require(decision["selected_R_H_RG_source_emitted"] is True, "selected R_H")
    require(decision["H_parameter_count_after_replacement"] == 0, "H parameter count")
    require(decision["electroweak_prefactor_search_executed"] is True, "search executed")
    require(decision["accepted_selected_prefactor_source_count"] == 0, "prefactor overaccepted")
    require(decision["selected_A_EW_source_emitted"] is False, "A_EW overemitted")
    require(decision["selected_mu_match_or_RG_scheme_emitted"] is False, "scheme overemitted")
    require(decision["strict_lambda_H_value_row_emitted"] is False, "lambda overemitted")
    require(decision["strict_K_threshold_Omega_H_lambda_emitted"] is False, "K overemitted")
    require(decision["conditional_full_H_closure_if_prefactor_source_selected"] is True, "conditional closure")

    require(inventory["H_parameter_count_after_replacement"] == 0, "inventory parameter count")
    require(inventory["source_inputs_available"]["selected_A_EW_emitted"] is False, "inventory A_EW")
    require(inventory["source_inputs_available"]["matching_scale_closed"] is False, "inventory mu")
    require(inventory["source_inputs_available"]["RG_scheme_closed"] is False, "inventory RG")

    require(search["accepted_selected_prefactor_source_count"] == 0, "search accepted count")
    require(search["best_candidate"]["accepted_as_selected_prefactor_source"] is False, "best overaccepted")
    require(search["best_candidate"]["relative_residual"] > 0.0, "best exact unexpectedly")
    require(search["best_candidate"]["relative_residual"] < 1e-3, "best clue too weak")

    require(final_gate["selected_R_H_RG_source_emitted"] is True, "final R_H")
    require(final_gate["H_parameter_count_after_replacement"] == 0, "final H count")
    require(final_gate["strict_lambda_H_value_row_emitted"] is False, "final lambda")
    require(final_gate["strict_K_threshold_Omega_H_lambda_emitted"] is False, "final K")
    require(final_gate["accepted_selected_K_source_row_count_now"] == 9, "K row count")

    for phrase in [
        "ElectroweakPrefactorFinalGateTheorem",
        "H parameter count: `0`",
        "accepted selected prefactor source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: zero-H-parameter frontier confirmed; electroweak prefactor "
        "source search found support clues but no strict lambda/K row."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
