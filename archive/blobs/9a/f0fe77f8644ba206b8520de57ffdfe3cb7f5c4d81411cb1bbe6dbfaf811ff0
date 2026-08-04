from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_officialjointlikelihoodtransport_or_declareddiagonalprofilefinality"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(f"candidate_data/{SLUG}/official_joint_source_block_audit.packet.json")
    cert = load(f"certificates/{SLUG}_certificate.json")

    coordinates = [coordinate for block in packet["source_partitions"] for coordinate in block["coordinates"]]
    require(len(coordinates) == len(set(coordinates)) == 15, "source partition")
    require(packet["transport_state"]["frozen_Jacobian_shape"] == [8, 15], "Jacobian shape")
    require(packet["transport_state"]["output_covariance_shape"] == [8, 8], "covariance shape")
    require(packet["transport_state"]["output_covariance_positive_definite"] is True, "covariance")
    require(packet["decision"]["declared_diagonal_source_profile_is_reproducible_baseline"] is True, "baseline")
    require(packet["decision"]["declared_diagonal_source_profile_is_official_joint_likelihood"] is False, "joint overclaim")
    require(packet["decision"]["invent_unpublished_cross_authority_correlations"] is False, "invented correlations")
    require(packet["decision"]["official_joint_likelihood_strict_upgrade_closed"] is False, "strict U3 overclaim")
    require(cert["U3_local_execution_exhausted"] is True, "U3 local exit")
    require(cert["next_active_upgrade"] == "U2_literal_global_Cech_HYM_QaSU3", "next upgrade")

    print(json.dumps({
        "source_coordinates": 15,
        "authority_blocks": 3,
        "frozen_transport": "8x15 -> 8x8",
        "declared_diagonal_profile_finality": True,
        "official_joint_likelihood": False,
        "next_active_upgrade": cert["next_active_upgrade"],
    }, indent=2))
    print("official-joint likelihood source-block audit passed")


if __name__ == "__main__":
    main()
