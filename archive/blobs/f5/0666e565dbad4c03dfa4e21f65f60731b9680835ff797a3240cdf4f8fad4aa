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
DIRECTORY = VALIDATED / "ol"
A400 = VALIDATED / "n3.relative_chain_identity.a400.json"
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
A405 = VALIDATED / "n3.junction_operator_sweep.a405.json"
A410 = VALIDATED / "pt" / "a410.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
A413 = DIRECTORY / "all76.a413.json"
PACKET = DIRECTORY / "a413r.json"
SOURCE = ROOT / "scripts" / "rebind_q79_height4_a414_checkpoints_to_a413.py"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def normalized_checkpoint_sha256(checkpoint: dict[str, Any]) -> str:
    normalized = copy.deepcopy(checkpoint)
    normalized.pop("A414_A413_sha256", None)
    normalized.pop("A414_A404_sha256", None)
    rendered = json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(rendered)


def main() -> int:
    packet = load(PACKET)
    if packet.get("schema") != "MTTQ79HeightFourA413AuthorityOnlyCheckpointRebind.v1":
        raise AssertionError("A413R schema changed")
    if packet.get("status") != "A413_AUTHORITY_ONLY_CHECKPOINT_REBIND_APPLIED":
        raise AssertionError("A413R was not applied")
    expected_authorities = {
        "A400": A400,
        "A404": A404,
        "A405": A405,
        "A410": A410,
        "A411": A411,
        "A413": A413,
        "rebind_source": SOURCE,
    }
    for label, path in expected_authorities.items():
        if packet["current_authority"][label]["sha256"] != sha256(path):
            raise AssertionError(f"A413R authority is stale: {label}")
    if packet["proved_exact_change_paths"] != {
        "A400": ["authority.builder_source.sha256"],
        "A404": ["authority.A403_common_junction_edge_ledger.sha256"],
        "A405": [
            "authority.A404_manifest.sha256",
            "authority.basis_0_result.sha256",
            "authority.basis_0_snapshots.sha256",
            "authority.basis_1_result.sha256",
            "authority.basis_1_snapshots.sha256",
            "authority.basis_2_result.sha256",
            "authority.basis_2_snapshots.sha256",
            "authority.basis_3_result.sha256",
            "authority.basis_3_snapshots.sha256",
            "authority.basis_4_result.sha256",
            "authority.basis_4_snapshots.sha256",
        ],
        "A410": ["authority.A404_common_junction_manifest.sha256"],
        "A411": [
            "authority.A404_manifest.sha256",
            "authority.A405_operator_sweep.sha256",
            "authority.basis_0_snapshots.sha256",
            "authority.basis_1_snapshots.sha256",
            "authority.basis_2_snapshots.sha256",
            "authority.basis_3_snapshots.sha256",
            "authority.basis_4_snapshots.sha256",
        ],
        "A413": [
            "authority.A400_exact_relative_chain_identity.sha256",
            "authority.A404_common_junction_manifest.sha256",
            "authority.A405_entry_operators.sha256",
            "authority.A410_native_z_transitions.sha256",
            "authority.A411_terminal_trunk.sha256",
        ],
        "each_A414_checkpoint": [
            "A414_A404_sha256",
            "A414_A413_sha256",
        ],
    }:
        raise AssertionError("A413R exact change paths changed")

    current_a413_sha256 = sha256(A413)
    rows = packet["checkpoint_rows"]
    if len(rows) != 75:
        raise AssertionError("A413R checkpoint census changed")
    indices = set()
    for row in rows:
        index = int(row["distinguished_index"])
        if index == 57 or index in indices:
            raise AssertionError("A413R checkpoint index census changed")
        indices.add(index)
        path = ROOT / Path(row["checkpoint"]["path"])
        checkpoint = load(path)
        if not checkpoint.get("complete"):
            raise AssertionError(f"A413R d{index:03d} checkpoint is incomplete")
        if checkpoint.get("A414_A413_sha256") != current_a413_sha256:
            raise AssertionError(f"A413R d{index:03d} does not bind current A413")
        if checkpoint.get("A414_A404_sha256") != sha256(A404):
            raise AssertionError(f"A413R d{index:03d} does not bind current A404")
        if row["checkpoint"]["after_sha256"] != sha256(path):
            raise AssertionError(f"A413R d{index:03d} checkpoint hash is stale")
        if (
            row["normalized_checkpoint_payload_sha256"]
            != normalized_checkpoint_sha256(checkpoint)
        ):
            raise AssertionError(f"A413R d{index:03d} numerical payload changed")

    summary = packet["summary"]
    if summary != {
        "authority_fields_rebound_per_checkpoint": 2,
        "checkpoint_count": 75,
        "numerical_checkpoint_payloads_changed": 0,
    }:
        raise AssertionError("A413R summary changed")
    scope = packet["strict_scope"]
    required_true = (
        "all_A400_A404_A405_A410_A411_changes_proved_authority_only",
        "A413_change_proved_parent_authority_only",
        "all_75_complete_A414_checkpoint_payloads_preserved",
        "native_A414_and_A415_producers_still_required_after_rebind",
    )
    if not all(scope[key] for key in required_true):
        raise AssertionError("A413R required scope flag is false")
    if scope["new_numerical_transport_execution_claimed"] or scope["covariant_zero_proved"]:
        raise AssertionError("A413R overclaims its scope")
    print(
        "PASS: A413R rebinds 75 complete A414 checkpoints to current A413 "
        "with zero normalized numerical payload changes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
