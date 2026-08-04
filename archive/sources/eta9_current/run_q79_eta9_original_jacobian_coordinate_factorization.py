from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def wsl_path(path: Path) -> str:
    resolved = path.resolve()
    drive = resolved.drive.rstrip(":").lower()
    require(len(drive) == 1, "single-letter Windows drive")
    tail = resolved.as_posix().split(":", 1)[1]
    return f"/mnt/{drive}{tail}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=("H02", "H11", "H20"), default="H02")
    parser.add_argument("--timeout", type=float, default=7200.0)
    parser.add_argument("--progress-seconds", type=float, default=10.0)
    args = parser.parse_args()
    require(args.timeout > 0, "positive timeout")

    csc_packet_path = ROOT / f"q79_eta9_original_jacobian_macaulay_{args.target}_csc.packet.json"
    csc_packet = json.loads(csc_packet_path.read_text(encoding="utf-8"))
    require(all(csc_packet["checks"].values()), "CSC packet checks")
    csc_path = Path(csc_packet["binary"]["path"])
    executable = ROOT / "compute_q79_eta9_original_jacobian_coordinate_factorization"
    require(csc_path.is_file(), "CSC binary exists")
    require(executable.is_file(), "factorizer executable exists")

    exact_path = ROOT / f"q79_eta9_original_jacobian_coordinate_factorization_{args.target}.exact.out"
    factor_path = ROOT / f"q79_eta9_original_jacobian_coordinate_factorization_{args.target}.factor.bin"
    command = " ".join(
        shlex.quote(item)
        for item in (
            wsl_path(executable),
            "--input",
            wsl_path(csc_path),
            "--output",
            wsl_path(exact_path),
            "--factorization",
            wsl_path(factor_path),
            "--column-order",
            "nnz",
            "--progress-seconds",
            str(args.progress_seconds),
        )
    )
    print(
        f"Starting exact {args.target} B103-plus-original-Jacobian coordinate factorization",
        flush=True,
    )
    subprocess.run(["wsl", "sh", "-lc", command], check=True, timeout=args.timeout)
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "bind_q79_eta9_original_jacobian_coordinate_factorization.py"),
            "--target",
            args.target,
        ],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "verify_q79_eta9_original_jacobian_coordinate_factorization.py"),
            "--target",
            args.target,
        ],
        cwd=ROOT,
        check=True,
    )
    print(
        f"Q79_ETA9_ORIGINAL_JACOBIAN_COORDINATE_FACTORIZATION_{args.target}_RUN_PASS",
        flush=True,
    )


if __name__ == "__main__":
    main()
