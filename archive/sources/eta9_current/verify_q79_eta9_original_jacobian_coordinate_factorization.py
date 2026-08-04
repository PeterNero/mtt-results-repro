from __future__ import annotations

import argparse
import json
from pathlib import Path

import bind_q79_eta9_original_jacobian_coordinate_factorization as binding


ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=("H02", "H11", "H20"), required=True)
    args = parser.parse_args()
    packet_path = (
        ROOT / f"q79_eta9_original_jacobian_coordinate_factorization_{args.target}.packet.json"
    )
    recorded = json.loads(packet_path.read_text(encoding="utf-8"))
    rebuilt = binding.validate(args.target)
    binding.require(recorded == rebuilt, "packet exactly regenerates")
    binding.require(all(recorded["checks"].values()), "all checks")
    binding.require(
        recorded["exact_coordinate_identity"]["residual_nonzeros"] == 0,
        "zero exact residual",
    )
    binding.require(
        recorded["exact_coordinate_identity"]["minor_determinant_mod11"] != 0,
        "nonzero determinant",
    )
    print(
        f"Q79_ETA9_ORIGINAL_JACOBIAN_COORDINATE_FACTORIZATION_{args.target}_VERIFY_PASS"
    )


if __name__ == "__main__":
    main()
