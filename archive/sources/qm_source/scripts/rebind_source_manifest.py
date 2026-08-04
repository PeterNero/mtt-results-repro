from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "source_manifest.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rebind one explicitly selected QM source after native verification."
    )
    parser.add_argument("--source-id", required=True)
    args = parser.parse_args()

    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if payload.get("schema") != "MTTQMSourceManifest.v1":
        raise AssertionError("unexpected source manifest schema")
    rows = [
        row for row in payload.get("sources", []) if row.get("id") == args.source_id
    ]
    if len(rows) != 1:
        raise AssertionError(f"expected one source row for {args.source_id}")

    row = rows[0]
    path = (ROOT / row["path"]).resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    previous = row["sha256"]
    current = digest(path)
    row["sha256"] = current
    MANIFEST.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(f"source_id={args.source_id}")
    print(f"previous_sha256={previous}")
    print(f"current_sha256={current}")
    print(f"WROTE: {MANIFEST}")


if __name__ == "__main__":
    main()
