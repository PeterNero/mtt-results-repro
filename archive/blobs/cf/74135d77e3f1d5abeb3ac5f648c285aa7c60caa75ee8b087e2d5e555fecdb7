"""Audit oriented Phi_fin source-owned positive operator / E_Qa payload frontier."""

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
BUILDER = ROOT / "scripts" / "build_selected_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.py"

SLUG = "selected_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1.md"

SINGLE_FRONTIER = PACKET_DIR / "single_source_ownership_frontier.packet.json"
SOURCE_REQUEST = PACKET_DIR / "threshold_identity_source_request.packet.json"
LEAF_REQUEST = PACKET_DIR / "sourceleaf_directcarrier_or_bundleA_request.packet.json"
NEXT_CONTRACT = PACKET_DIR / "sourceownership_theorem_or_smootheqa_quotient_contract.packet.json"

STATUS = (
    "MTT_SELECTED_ORIENTEDPHIFIN_SOURCEOWNEDPOSITIVEOPERATOR_OR_EQAPAYLOAD_FILL_"
    "BUILT_SINGLE_SOURCE_OWNERSHIP_FRONTIER_OPEN"
)
NEXT = "MTT_Selected_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    single = load(SINGLE_FRONTIER)
    request = load(SOURCE_REQUEST)
    leaf = load(LEAF_REQUEST)
    next_contract = load(NEXT_CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_contract["next_required_artifact"] == NEXT, "next contract mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, single, request, leaf, next_contract]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["previous_frontier_honored"] is True, "previous frontier not honored")
    require(decision["operator_payload_ready"] is True, "operator payload not ready")
    require(decision["support_closed_count"] == 10, "support count mismatch")
    require(decision["support_required_count"] == 10, "support required count mismatch")
    require(decision["all_value_side_support_closed"] is True, "value-side support not closed")
    require(decision["single_source_ownership_frontier_built"] is True, "single frontier not built")
    for key in [
        "source_ownership_theorem_closed",
        "smooth_EQa_quotient_closed",
        "direct_source_owned_positive_operator_closed",
        "smooth_EQa_payload_closed",
        "direct_carrier_leaf_closed",
        "bundle_A_leaf_closed",
        "oriented_threshold_value_promoted",
        "finitepart_trace_identity_closed",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclosed: {key}")
    require(decision["strict_P_EW_source_rows"] == 0, "strict P_EW overaccepted")
    require(decision["strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K overaccepted")

    require(
        single["status"] == "SINGLE_SOURCE_OWNERSHIP_FRONTIER_IMPORTED_SUPPORT_COMPLETE_SOURCE_OPEN",
        "single frontier status mismatch",
    )
    require(single["operator_payload_ready"] is True, "single payload not ready")
    require(single["support_closed_count"] == single["support_required_count"] == 10, "single support count mismatch")
    require(all(value is True for value in single["support_closed"].values()), "not all support closed")
    require(all(value is False for value in single["not_yet_source_owned"].values()), "source-owned field overclosed")
    for value in single["accepted_final_rows"].values():
        require(value == 0, "single final row overaccepted")

    require(request["status"] == "SOURCE_REQUEST_IMPORTED_ALL_ALGEBRAIC_SUPPORT_CLOSED", "request status mismatch")
    require(request["acceptance_rule"]["observed_data_allowed"] is False, "observed data allowed")
    require(request["acceptance_rule"]["otherwise_keep_as_support_only"] is True, "support-only guard missing")
    require(request["acceptance_rule"]["promote_threshold_magnitude_if_all_fields_selected_same_source"] is True, "acceptance rule missing")
    require(all(value is True for value in request["closed_support"].values()), "request support not closed")
    for field in request["open_source_fields"].values():
        require(field["closed"] is False, "request source field overclosed")
    require(
        request["support_values"]["oriented_abs_logdet_support_value"] == 18.339036754911856,
        "oriented support value mismatch",
    )

    require(leaf["status"] == "FIRST_SOURCE_LEAVES_IDENTIFIED_BOTH_OPEN", "leaf status mismatch")
    require(leaf["first_direct_leaf"] == "source_emits_oriented_BN_carrier", "direct leaf mismatch")
    require(leaf["first_smooth_leaf"] == "selected_bundle_connection_A", "smooth leaf mismatch")
    require(leaf["direct_leaf_closed"] is False, "direct leaf overclosed")
    require(leaf["bundle_A_leaf_closed"] is False, "bundle A leaf overclosed")
    for attempt in leaf["direct_leaf_attempt"].values():
        require(attempt["closed"] is False, "direct attempt overclosed")
    for attempt in leaf["smooth_leaf_attempt"].values():
        require(attempt["closed"] is False, "smooth attempt overclosed")

    require(
        next_contract["status"] == "NEXT_IS_SOURCEOWNERSHIP_THEOREM_OR_SMOOTHEQA_QUOTIENT",
        "next contract status mismatch",
    )
    require(any("same-source theorem" in item for item in next_contract["must_emit_one_of"]), "same-source target missing")
    require(any("bundle connection" in item for item in next_contract["must_emit_one_of"]), "bundle A target missing")
    require("oriented logdet table value as a promoted threshold without trace identity" in next_contract["must_not_use"], "logdet guard missing")
    require("observed coupling, mass, or benchmark data" in next_contract["must_not_use"], "observed guard missing")

    require("closed value/support fields          : 10/10" in note, "note missing support count")
    require(NEXT in note, "note missing next artifact")

    print("Oriented Phi_fin source-owned positive operator / E_Qa payload audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
