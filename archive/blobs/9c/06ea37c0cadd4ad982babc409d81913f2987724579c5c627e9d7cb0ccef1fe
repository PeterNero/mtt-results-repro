"""Audit the post-D_E export dependency cut."""

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
BUILDER = ROOT / "scripts" / "build_selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart.py"

SLUG = "selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostDEExport_RemainingDependencyCut_or_SourceOwnedFinitepart_v1.md"
DEPENDENCY_PACKET = PACKET_DIR / "remaining_four_dependency_cut.packet.json"
LOGDET_PACKET = PACKET_DIR / "logdet_no_lift_strict_gate_after_4of8.packet.json"
NEXT_PACKET = PACKET_DIR / "next_sourceowned_finitepart_or_cechhym_contract.packet.json"

STATUS = (
    "MTT_SELECTED_POSTDEEXPORT_REMAININGDEPENDENCYCUT_OR_SOURCEOWNEDFINITEPART_"
    "FOUR_OF_EIGHT_RETAINED_SOURCEOWNEDFINITEPART_OR_CECHHYM_REQUIRED"
)
NEXT = "MTT_Selected_SourceOwnedFinitepartKernelPolicy_or_CechHYMConnectionValues_v1"
ACCEPTED = [
    "typed_f_sections",
    "typed_g_sections",
    "g_after_f_zero_exactness_certificate",
    "BN27_DE_Riesz_Green_kernel_trace_export",
]
REMAINING = [
    "cech_transition_cocycles",
    "selected_HYM_or_projective_connection_coefficients",
    "finitepart_log92160000_identity_from_values",
    "no_lifted_flags_connection_replay",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    dependency = load(DEPENDENCY_PACKET)
    logdet = load(LOGDET_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, dependency, logdet, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    require(dependency["current_count"] == "4/8", "dependency count")
    require(dependency["accepted_rows"] == ACCEPTED, "dependency accepted rows")
    require(dependency["remaining_rows"] == REMAINING, "dependency remaining rows")
    require(dependency["dependency_classes"]["geometric_connection_values"]["closed_now"] is False, "geometric overclosed")
    require(dependency["dependency_classes"]["finitepart_and_replay_provenance"]["closed_now"] is False, "provenance overclosed")
    require(
        dependency["dependency_classes"]["finitepart_and_replay_provenance"]["exact_arithmetic_available"] is True,
        "exact arithmetic missing",
    )
    require(
        dependency["dependency_classes"]["finitepart_and_replay_provenance"]["conditional_replay_available"] is True,
        "conditional replay missing",
    )

    require(logdet["exact_values"]["oriented_abs_sector_product"] == 92160000, "oriented product mismatch")
    require(logdet["exact_values"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", "oriented log mismatch")
    gate = logdet["sourceowned_logdet_gate"]
    require(gate["direct_finitepart_arithmetic_closed"] is True, "direct arithmetic not closed")
    require(gate["sourceowned_logdet_minimal_packet_built"] is True, "minimal logdet packet missing")
    for key in [
        "source_object_named_S_QaSU3_BN27",
        "kernel_trace_source_owned",
        "source_owned_finitepart_functional_closed",
        "source_owned_logdet_closed",
    ]:
        require(gate[key] is False, f"logdet overclaim: {key}")

    no_lift = logdet["no_lift_gate"]
    require(no_lift["no_lift_replay_conditional_closed"] is True, "conditional no-lift missing")
    require(no_lift["operator_coemission_conditional_closed"] is True, "conditional coemission missing")
    require(no_lift["source_branch_identity_closed"] is False, "source branch overclosed")
    require(no_lift["same_source_export_to_BN27_validators"] is False, "validator export overclosed")
    require(no_lift["open_validator_count"] == 5, "open validator count changed")
    require(logdet["strict_rows_promoted_now"] == [], "strict row promoted unexpectedly")

    decision = candidate["closure_decision"]
    require(decision["accepted_final_same_source_connection_tables"] == 4, "decision accepted count")
    require(decision["required_final_same_source_connection_tables"] == 8, "decision required count")
    require(decision["accepted_rows"] == ACCEPTED, "decision accepted rows")
    require(decision["remaining_rows"] == REMAINING, "decision remaining rows")
    require(decision["exact_log92160000_arithmetic_available"] is True, "decision exact arithmetic")
    require(decision["conditional_no_lift_replay_available"] is True, "decision conditional no-lift")
    require(decision["new_rows_promoted"] == 0, "decision promoted new rows")
    for key in [
        "source_owned_logdet_closed",
        "kernel_trace_policy_source_owned",
        "source_owned_finitepart_functional_closed",
        "source_branch_identity_closed",
        "same_source_export_to_BN27_validators",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")
        require(cert[key] is False, f"cert overclaim: {key}")

    require(next_packet["current_count"] == "4/8", "next current count")
    require(next_packet["remaining_rows"] == REMAINING, "next remaining rows")
    require("frontier remains `4/8`" in note, "note missing 4/8")
    require(NEXT in note, "note missing next artifact")

    print("Post-D_E export dependency-cut audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
