"""Audit precision profile table or true SM equivalence audit."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_precisionprofiletable_or_truesmequivalenceaudit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRECISION_TABLE = PACKET_DIR / "precision_profile_equivalence_table.packet.json"
BLOCKER_MATRIX = PACKET_DIR / "true_sm_equivalence_blocker_matrix.packet.json"
LEDGER_BRIDGE = PACKET_DIR / "minimal_parameter_ledger_to_precision_bridge.packet.json"
NEXT_TARGET = PACKET_DIR / "next_after_precision_profile_table.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrecisionProfileTable_or_TrueSMEquivalenceAudit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_PRECISIONPROFILETABLE_OR_TRUESMEQUIVALENCEAUDIT_"
    "TABLE_BUILT_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_QaSU3OperatorPayload_or_StrictPEWPrecisionExit_v1"


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
    table = load(PRECISION_TABLE)
    blockers = load(BLOCKER_MATRIX)
    bridge = load(LEDGER_BRIDGE)
    next_target = load(NEXT_TARGET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("table", table),
        ("blockers", blockers),
        ("bridge", bridge),
        ("next", next_target),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_target["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["theorem"]["name"] == "PrecisionProfileTableOrTrueSMEquivalenceAuditTheorem", "name")

    decision = data["closure_decision"]
    require(decision["precision_profile_table_built"] is True, "precision table")
    require(decision["precision_policy_rows_closed"] is True, "policy rows")
    require(decision["central_value_replay_baseline_closed"] is True, "central baseline")
    require(decision["accepted_true_equivalence_rows"] == 0, "accepted true rows")
    require(decision["full_covariance_profile_likelihood_closed"] is False, "covariance overclaim")
    require(decision["threshold_mass_scheme_source_rows_closed"] is False, "threshold overclaim")
    require(decision["multi_loop_RG_values_closed"] is False, "RG overclaim")
    require(decision["local_QFT_precision_observable_table_closed"] is False, "local QFT overclaim")
    require(decision["selected_QaSU3_operator_payload_closed"] is False, "QaSU3 overclaim")
    require(decision["strict_P_EW_source_theorem_closed"] is False, "strict P_EW overclaim")
    require(decision["neutrino_absolute_source_closed"] is False, "neutrino source overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclaim")
    require(decision["full_no_knob_closed"] is False, "no-knob overclaim")

    summary = table["summary"]
    require(summary["table_rows"] == 9, "table row count")
    require(summary["accepted_true_equivalence_rows"] == 0, "table accepted rows")
    require(summary["rows_blocking_true_equivalence"] >= 8, "blocking row count")
    targets = [row["row"] for row in table["rows"]]
    for target in [
        "reference scheme and scale",
        "central-value covariance tier",
        "common-scale Yukawa/Higgs values",
        "threshold and mass-scheme source rows",
        "precision profile import / row replacement",
        "local QFT precision observable table",
        "full-loop precision observable import",
        "Qa/SU3 operator slot/value payload",
        "dynamic Qa/SU3 C1 response",
    ]:
        require(target in targets, f"missing table row {target}")

    classes = blockers["blocking_classes"]
    for key in [
        "precision_profile_likelihood",
        "threshold_mass_scheme_multiloop",
        "local_QFT_precision_observables",
        "selected_QaSU3_operator_payload",
        "strict_P_EW_or_direct_K",
        "neutrino_absolute_source",
    ]:
        require(key in classes, f"missing blocker {key}")
        require(classes[key]["closed"] is False, f"{key} overclaim")
        require(classes[key]["accepted_rows"] == 0, f"{key} accepted rows")
    require(blockers["true_SM_equivalence_closed"] is False, "blocker true overclaim")
    require(blockers["full_no_knob_closed"] is False, "blocker no-knob overclaim")

    counts = bridge["minimal_parameter_counts"]
    require(counts["non_neutrino_including_QCD_theta"] == 19, "non-neutrino count")
    require(counts["minimal_PMNS_including_QCD_theta"] == 25, "minimal PMNS")
    require(counts["Dirac_massive_neutrino_completion"] == 26, "Dirac")
    require(counts["Majorana_massive_neutrino_completion"] == 28, "Majorana")
    require(counts["if_strict_P_EW_closes_minimal_PMNS"] == 24, "strict minimal")
    require(counts["if_strict_P_EW_closes_Dirac_completion"] == 25, "strict Dirac")
    require(counts["if_strict_P_EW_closes_Majorana_completion"] == 27, "strict Majorana")
    require(
        bridge["precision_claim_policy"]["precision_equivalence_requires_more_than_parameter_counting"]
        is True,
        "precision claim policy",
    )

    require(cert["precision_profile_table_built"] is True, "cert table")
    require(cert["accepted_true_equivalence_rows"] == 0, "cert accepted rows")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob overclaim")

    for phrase in [
        "PrecisionProfileTableOrTrueSMEquivalenceAuditTheorem",
        "precision profile table built = true",
        "accepted true-equivalence rows = 0",
        "full covariance/profile likelihood closed = false",
        "selected Qa/SU3 operator payload closed = false",
        "non-neutrino including QCD theta_bar = 19",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: precision profile table built; accepted true-equivalence "
        "rows remain 0; covariance/profile, threshold/mass-scheme, local-QFT, "
        "Qa/SU3 payload, strict P_EW, neutrino source, true equivalence, and "
        "no-knob closure remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
