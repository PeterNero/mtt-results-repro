#!/usr/bin/env python3
"""Append an SMS right-hand side as the last matrix column."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def checksum(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--rhs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--prime", type=int, default=101)
    args = parser.parse_args()

    rhs = [int(value) % args.prime for value in args.rhs.read_text(encoding="ascii").splitlines()]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    matrix_nonzeros = 0
    terminated = False
    with args.matrix.open("r", encoding="ascii") as source, args.output.open(
        "w", encoding="ascii", newline="\n"
    ) as target:
        row_text, column_text, marker = source.readline().split()
        rows = int(row_text)
        columns = int(column_text)
        require(marker == "M", "SMS header")
        require(len(rhs) == rows, "RHS dimension")
        target.write(f"{rows} {columns + 1} M\n")
        for line in source:
            row_text, column_text, value_text = line.split()
            row = int(row_text)
            column = int(column_text)
            value = int(value_text)
            if row == column == value == 0:
                terminated = True
                break
            require(1 <= row <= rows and 1 <= column <= columns, "SMS entry")
            require(value % args.prime, "nonzero SMS entry")
            target.write(f"{row} {column} {value % args.prime}\n")
            matrix_nonzeros += 1
        require(terminated, "SMS terminator")
        rhs_nonzeros = 0
        for row, value in enumerate(rhs, start=1):
            if value:
                target.write(f"{row} {columns + 1} {value}\n")
                rhs_nonzeros += 1
        target.write("0 0 0\n")

    packet = {
        "schema": "MTTQ79SMSAugmentedRankInput.v1",
        "date": "2026-07-20",
        "field": f"F_{args.prime}",
        "matrix": checksum(args.matrix),
        "right_hand_side": checksum(args.rhs),
        "augmented_matrix": checksum(args.output),
        "dimensions": {
            "rows": rows,
            "matrix_columns": columns,
            "augmented_columns": columns + 1,
            "matrix_nonzeros": matrix_nonzeros,
            "rhs_nonzeros": rhs_nonzeros,
            "augmented_nonzeros": matrix_nonzeros + rhs_nonzeros,
        },
        "decision_rule": {
            "rank_A_equals_rank_augmented": "the degree-bounded system is consistent",
            "rank_augmented_equals_rank_A_plus_one": "the requested unit identity needs a higher degree bound",
        },
    }
    args.packet.parent.mkdir(parents=True, exist_ok=True)
    args.packet.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print("Q79_SMS_AUGMENT_PASS")
    print(args.output)


if __name__ == "__main__":
    main()
