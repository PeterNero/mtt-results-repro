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
A411 = VALIDATED / "jop" / "trunk.a411.json"
DIRECTORY = VALIDATED / "ol"
SOURCE = DIRECTORY / "ha.src.a418.json"
CHECKPOINT = DIRECTORY / "ha.a418.ckpt.json"
PACKET = DIRECTORY / "ha.a418r.json"
REBIND_SOURCE = ROOT / "scripts" / "rebind_q79_height4_a418_checkpoint_to_current_source.py"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def normalized_checkpoint_sha256(checkpoint: dict[str, Any]) -> str:
    normalized = copy.deepcopy(checkpoint)
    normalized.pop("A418_source_sha256", None)
    normalized.pop("path_name", None)
    rendered = json.dumps(normalized, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(rendered)


def main() -> int:
    packet = load(PACKET)
    source = load(SOURCE)
    checkpoint = load(CHECKPOINT)
    if packet.get("schema") != "MTTQ79HeightFourA418AuthorityOnlyCheckpointRebind.v1":
        raise AssertionError("A418R schema changed")
    if packet.get("status") != "A418_AUTHORITY_ONLY_CHECKPOINT_REBIND_APPLIED":
        raise AssertionError("A418R was not applied")
    for label, path in {
        "A404": A404,
        "A411": A411,
        "source": SOURCE,
        "checkpoint": CHECKPOINT,
        "rebind_source": REBIND_SOURCE,
    }.items():
        if packet["current_authority"][label]["sha256"] != sha256(path):
            raise AssertionError(f"A418R authority is stale: {label}")
    if source["authority"]["A404_operational_path"]["sha256"] != sha256(A404):
        raise AssertionError("A418 source A404 authority is stale")
    if source["authority"]["A411_terminal_trunk"]["sha256"] != sha256(A411):
        raise AssertionError("A418 source A411 authority is stale")
    if checkpoint.get("A418_source_sha256") != sha256(SOURCE):
        raise AssertionError("A418 checkpoint source authority is stale")
    expected_path_name = (
        "A418 selected A-handle hub-to-endpoint dps=100 "
        f"source={sha256(SOURCE)[:16]} "
        f"builder={checkpoint['A418_builder_sha256'][:16]}"
    )
    if checkpoint.get("path_name") != expected_path_name:
        raise AssertionError("A418 checkpoint path-name authority is stale")
    if (
        packet["checkpoint"]["normalized_numerical_payload_sha256"]
        != normalized_checkpoint_sha256(checkpoint)
    ):
        raise AssertionError("A418 normalized numerical checkpoint payload changed")
    if packet["proved_exact_change_paths"] != {
        "A418_source": [
            "authority.A404_operational_path.sha256",
            "authority.A411_terminal_trunk.sha256",
        ],
        "A418_checkpoint": [
            "A418_source_sha256",
            "path_name",
        ],
    }:
        raise AssertionError("A418R exact change paths changed")
    scope = packet["strict_scope"]
    if not (
        scope["A418_source_change_proved_authority_only"]
        and scope["A418_checkpoint_numerical_payload_preserved"]
        and scope["native_A418_replay_still_required"]
    ):
        raise AssertionError("A418R required scope flag is false")
    if scope["new_transport_execution_claimed"]:
        raise AssertionError("A418R overclaims new transport execution")
    print(
        "PASS: A418R rebinds the complete A418 checkpoint to current A404/A411 "
        "with zero normalized numerical payload changes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
