from __future__ import annotations

import hashlib
import json

import build_q79_eta9_targeted_original_jacobian_transform_coverage as coverage_builder


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def main() -> None:
    packet = json.loads(coverage_builder.OUT.read_text(encoding="utf-8"))
    discovered = coverage_builder.discover_coverage()
    require(packet == discovered, "coverage packet does not match current certificate files")
    require(all(packet["checks"].values()), "coverage checks")
    coverage = packet["coverage"]
    certified = coverage["certified_column_indices_zero_based"]
    missing = coverage["remaining_column_indices_zero_based"]
    require(len(certified) == coverage["certified_columns"], "certified count")
    require(len(missing) == coverage["remaining_columns"], "remaining count")
    require(sorted(certified + missing) == list(range(225)), "coverage partition")
    require(not set(certified).intersection(missing), "coverage overlap")
    digest = hashlib.sha256(coverage_builder.OUT.read_bytes()).hexdigest()
    semantic_digest = hashlib.sha256(canonical(packet).encode("utf-8")).hexdigest()
    print("Q79_ETA9_TARGETED_ORIGINAL_JACOBIAN_TRANSFORM_COVERAGE_VERIFY_PASS")
    print(f"certified_columns={coverage['certified_columns']}")
    print(f"remaining_columns={coverage['remaining_columns']}")
    print(f"packet_sha256={digest}")
    print(f"semantic_sha256={semantic_digest}")


if __name__ == "__main__":
    main()
