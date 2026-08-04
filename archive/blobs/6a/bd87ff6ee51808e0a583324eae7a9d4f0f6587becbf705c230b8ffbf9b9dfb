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
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
DIRECTORY = VALIDATED / "ol"
CHECKPOINT = DIRECTORY / "d057.a409o.ckpt.json"
PACKET = DIRECTORY / "a409or.json"
SOURCE = ROOT / "scripts" / "rebind_q79_height4_a409o_checkpoint_to_a404.py"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def normalized_checkpoint_sha256(checkpoint: dict[str, Any]) -> str:
    normalized = copy.deepcopy(checkpoint)
    normalized.pop("A409O_A404_sha256", None)
    rendered = json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(rendered)


def main() -> int:
    packet = load(PACKET)
    checkpoint = load(CHECKPOINT)
    if packet.get("schema") != "MTTQ79HeightFourA409OAuthorityOnlyCheckpointRebind.v1":
        raise AssertionError("A409OR schema changed")
    if packet.get("status") != "A409O_AUTHORITY_ONLY_CHECKPOINT_REBIND_APPLIED":
        raise AssertionError("A409OR was not applied")
    for label, path in {
        "A404": A404,
        "checkpoint": CHECKPOINT,
        "rebind_source": SOURCE,
    }.items():
        if packet["current_authority"][label]["sha256"] != sha256(path):
            raise AssertionError(f"A409OR authority is stale: {label}")
    if checkpoint.get("A409O_A404_sha256") != sha256(A404):
        raise AssertionError("A409O checkpoint does not bind current A404")
    if (
        packet["checkpoint"]["normalized_numerical_payload_sha256"]
        != normalized_checkpoint_sha256(checkpoint)
    ):
        raise AssertionError("A409O normalized numerical checkpoint payload changed")
    if packet["proved_exact_change_paths"] != {
        "A404": ["authority.A403_common_junction_edge_ledger.sha256"],
        "A409O_checkpoint": ["A409O_A404_sha256"],
    }:
        raise AssertionError("A409OR exact change paths changed")
    scope = packet["strict_scope"]
    if not (
        scope["A404_change_proved_authority_only"]
        and scope["A409O_checkpoint_numerical_payload_preserved"]
        and scope["native_A409O_and_A412_replay_still_required"]
    ):
        raise AssertionError("A409OR required scope flag is false")
    if scope["new_transport_execution_claimed"]:
        raise AssertionError("A409OR overclaims new transport execution")
    print(
        "PASS: A409OR rebinds the complete d057 A409O checkpoint to current A404 "
        "with zero normalized numerical payload changes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
