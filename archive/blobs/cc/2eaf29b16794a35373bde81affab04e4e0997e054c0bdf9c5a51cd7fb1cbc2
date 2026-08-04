"""Audit threshold-scheme value rows / source-selected universal anchor attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thresholdschemevaluerows_or_sourceselecteduniversalanchorexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_BASIS_PACKET = PACKET_DIR / "selected_anchor_source_basis.packet.json"
ANCHOR_SEARCH_PACKET = PACKET_DIR / "one_to_three_anchor_model_search.packet.json"
OVERFIT_GUARD_PACKET = PACKET_DIR / "overfit_exact_replay_guard.packet.json"
THRESHOLD_GATE_PACKET = PACKET_DIR / "threshold_value_row_acceptance_gate.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_anchor_search.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThresholdSchemeValueRows_or_SourceSelectedUniversalAnchorExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_THRESHOLDSCHEMEVALUEROWS_OR_SOURCESELECTEDUNIVERSALANCHOREXECUTION_"
    "BUILT_ANCHOR_SEARCH_NO_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_InternalThresholdResponseFunctionalValueRows_or_ExternalSourceImportDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str, *, allow_target_fit: bool = False) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    if allow_target_fit:
        require(packet.get("target_fitting_used") is True, f"{label} diagnostic fit flag missing")
    else:
        require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its audit theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    source_basis = load(SOURCE_BASIS_PACKET)
    anchor_search = load(ANCHOR_SEARCH_PACKET)
    overfit = load(OVERFIT_GUARD_PACKET)
    threshold_gate = load(THRESHOLD_GATE_PACKET)
    cutset = load(CUTSET_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("source basis", source_basis),
        ("threshold gate", threshold_gate),
        ("cutset", cutset),
    ]:
        guard(packet, label)
    guard(anchor_search, "anchor search", allow_target_fit=True)
    guard(overfit, "overfit guard", allow_target_fit=True)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    sources = source_basis["available_selected_structural_sources"]
    require(len(sources) == 5, "source basis count mismatch")
    require(all(row["selected_at_source_tier"] is True for row in sources), "source basis not selected")
    require(all(row["emits_threshold_value_rows"] is False for row in sources), "source basis overemits values")
    require(source_basis["current_value_emitting_anchor_count"] == 0, "value anchors overcounted")

    require(anchor_search["charged_row_count"] == 9, "anchor search row count mismatch")
    require(anchor_search["policy_feature_count_limit"] == 3, "policy feature limit mismatch")
    policy = anchor_search["policy_result"]
    require(policy["one_to_three_current_source_anchor_sufficient"] is False, "1-3 anchor lane overclosed")
    require(policy["accepted_source_anchor_row_count"] == 0, "source anchor rows overaccepted")
    require(policy["best_policy_max_multiplicative_error_factor"] > 2.0, "1-3 diagnostic too strong for no-go")
    for key in ["1", "2", "3", "8", "9"]:
        require(key in anchor_search["best_by_feature_count"], f"missing best count {key}")
        require(
            anchor_search["best_by_feature_count"][key]["accepted_as_source_anchor_model"] is False,
            f"fit overaccepted for {key}",
        )

    require(overfit["accepted_as_source_rows"] is False, "overfit replay accepted")
    require(overfit["near_exact_model"]["feature_count"] == 8, "near-exact model feature count mismatch")
    require(overfit["exact_charged_replay_model"]["feature_count"] == 9, "exact model feature count mismatch")
    require(overfit["exact_charged_replay_model"]["max_multiplicative_error_factor"] < 1.0000001, "exact replay missing")
    for phrase in [
        "eight/nine coefficients for nine charged rows are row-replay, not selected source data",
        "coefficients are solved from Step72 diagnostic postcheck targets",
        "lambda_H remains outside the charged exact replay",
    ]:
        require(phrase in overfit["why_forbidden"], f"overfit guard missing {phrase}")

    require(threshold_gate["requirement_count"] == 9, "threshold requirement count mismatch")
    require(threshold_gate["present_count"] == 4, "threshold present count mismatch")
    for key in [
        "accepted_threshold_scheme_value_row_count",
        "accepted_source_anchor_row_count",
        "accepted_omega_source_row_count",
    ]:
        require(threshold_gate[key] == 0, f"threshold overaccepted {key}")
    require(threshold_gate["accepted_lambda_H_value_row"] is False, "lambda_H overaccepted")
    require(threshold_gate["full_no_knob_closed"] is False, "no-knob overclosed")

    for phrase in [
        "selected same-branch scale/scheme/loop convention at true-precision tier",
        "selected threshold matching value rows",
        "selected mass-scheme conversion value rows",
        "selected profile/diagonal likelihood value functional",
        "external source import decision if internal functional cannot be derived",
    ]:
        require(phrase in cutset["still_missing"], f"cutset missing {phrase}")
    for phrase in [
        "promote one-to-three target-scored coefficients as selected anchors",
        "use exact eight/nine coefficient replay as no-knob proof",
        "hide row-specific fits inside T_scheme.*",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing {phrase}")

    decision = data["closure_decision"]
    for key in [
        "selected_anchor_source_basis_built",
        "one_to_three_anchor_model_search_executed",
        "overfit_exact_replay_guard_built",
        "threshold_value_row_acceptance_gate_built",
    ]:
        require(decision[key] is True, f"decision did not close {key}")
        require(cert[key] is True, f"certificate did not close {key}")
    require(decision["one_to_three_current_source_anchor_sufficient"] is False, "decision overclosed 1-3 anchor")
    for key in [
        "accepted_threshold_scheme_value_row_count",
        "accepted_source_anchor_row_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(decision[key] == 0, f"decision overaccepted {key}")
        require(cert[key] == 0, f"certificate overaccepted {key}")
    for key in [
        "accepted_lambda_H_value_row",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")

    for phrase in [
        "best 1-3 anchor max error factor",
        "accepted source-anchor rows      : 0",
        "threshold value rows accepted    : 0",
        "exact charged replay appears only",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
