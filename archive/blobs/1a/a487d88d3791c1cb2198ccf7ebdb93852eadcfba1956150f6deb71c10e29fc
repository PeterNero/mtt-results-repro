from __future__ import annotations

import hashlib
import json

import build_q79_eta9_targeted_original_jacobian_macaulay_campaign_status as status_builder


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def main() -> None:
    packet = json.loads(status_builder.OUT.read_text(encoding="utf-8"))
    discovered = status_builder.discover_status()
    require(packet == discovered, "campaign packet does not match current artifacts")
    require(all(packet["checks"].values()), "campaign checks")
    states = packet["groups_in_selected_order"]
    require([entry["group_index"] for entry in states] == list(range(30)), "group order")
    digest = hashlib.sha256(status_builder.OUT.read_bytes()).hexdigest()
    print("Q79_ETA9_TARGETED_ORIGINAL_JACOBIAN_MACAULAY_CAMPAIGN_STATUS_VERIFY_PASS")
    print(f"completed_columns={packet['summary']['completed_columns']}")
    print(f"packet_sha256={digest}")


if __name__ == "__main__":
    main()
