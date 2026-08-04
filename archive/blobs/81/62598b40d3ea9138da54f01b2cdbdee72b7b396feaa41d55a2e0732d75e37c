from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
DIRECTORY = VALIDATED / "jop"
A403 = VALIDATED / "n3.common_junction_edge_ledger.a403.json"
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
PACKET = DIRECTORY / "a404r.json"
SOURCE = ROOT / "scripts" / "rebind_q79_height4_a405_artifacts_to_a404.py"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized_sha256(value: dict[str, Any], kind: str) -> str:
    normalized = copy.deepcopy(value)
    if kind == "checkpoint":
        normalized.pop("A405_manifest_sha256", None)
    elif kind == "snapshots":
        normalized.pop("A404_manifest_sha256", None)
    elif kind == "result":
        authority = normalized["authority"]
        authority["A404_manifest"].pop("sha256", None)
        authority["completed_checkpoint"].pop("sha256", None)
        authority["snapshot_packet"].pop("sha256", None)
    else:
        raise ValueError(kind)
    rendered = json.dumps(
        normalized, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(rendered).hexdigest()


def main() -> int:
    packet = load(PACKET)
    if packet.get("schema") != "MTTQ79HeightFourA404AuthorityOnlyA405Rebind.v1":
        raise AssertionError("A404R schema changed")
    if packet.get("status") != "A404_AUTHORITY_ONLY_A405_REBIND_APPLIED":
        raise AssertionError("A404R was not applied")
    for label, path in {"A403": A403, "A404": A404, "rebind_source": SOURCE}.items():
        if packet["current_authority"][label]["sha256"] != sha256(path):
            raise AssertionError(f"A404R authority is stale: {label}")
    if packet["summary"] != {
        "artifact_count": 15,
        "basis_count": 5,
        "normalized_numerical_payloads_changed": 0,
        "solver_reruns": 0,
    }:
        raise AssertionError("A404R summary changed")

    current_a404_sha256 = sha256(A404)
    for row in packet["basis_rows"]:
        column = int(row["basis_column_zero_based"])
        artifacts = row["artifacts"]
        checkpoint_path = ROOT / artifacts["checkpoint"]["path"]
        snapshots_path = ROOT / artifacts["snapshots"]["path"]
        result_path = ROOT / artifacts["result"]["path"]
        checkpoint = load(checkpoint_path)
        snapshots = load(snapshots_path)
        result = load(result_path)
        if checkpoint["A405_manifest_sha256"] != current_a404_sha256:
            raise AssertionError(f"A404R checkpoint {column} is stale")
        if snapshots["A404_manifest_sha256"] != current_a404_sha256:
            raise AssertionError(f"A404R snapshots {column} are stale")
        if result["authority"]["A404_manifest"]["sha256"] != current_a404_sha256:
            raise AssertionError(f"A404R result {column} is stale")
        if result["authority"]["completed_checkpoint"]["sha256"] != sha256(
            checkpoint_path
        ):
            raise AssertionError(f"A404R checkpoint hash {column} is stale")
        if result["authority"]["snapshot_packet"]["sha256"] != sha256(snapshots_path):
            raise AssertionError(f"A404R snapshot hash {column} is stale")
        for kind, value in (
            ("checkpoint", checkpoint),
            ("snapshots", snapshots),
            ("result", result),
        ):
            if artifacts[kind]["after_sha256"] != sha256(
                {"checkpoint": checkpoint_path, "snapshots": snapshots_path, "result": result_path}[kind]
            ):
                raise AssertionError(f"A404R written {kind} hash {column} is stale")
            if artifacts[kind]["normalized_payload_sha256"] != normalized_sha256(
                value, kind
            ):
                raise AssertionError(
                    f"A404R normalized {kind} payload {column} changed"
                )
    scope = packet["strict_scope"]
    required_true = (
        "A403_change_proved_A400_authority_only",
        "A404_change_proved_A403_authority_only",
        "all_five_completed_A405_artifact_triples_preserved",
        "native_A405_aggregate_and_audit_still_required",
    )
    if not all(scope[key] for key in required_true):
        raise AssertionError("A404R required scope flag is false")
    if scope["new_numerical_transport_execution_claimed"] or scope["covariant_zero_proved"]:
        raise AssertionError("A404R overclaims its scope")
    print(
        "PASS: A404R rebinds 15 completed A405 artifacts with zero "
        "normalized numerical payload changes and zero solver reruns"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
