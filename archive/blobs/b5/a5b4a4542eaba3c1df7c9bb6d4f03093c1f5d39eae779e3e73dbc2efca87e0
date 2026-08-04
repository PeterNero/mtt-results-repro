from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_shared_z64_same_source_monodromy_map_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    finite = cert["finite_data"]
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]

    require(all(cert["checks"].values()), "one or more same-source monodromy checks failed")
    require(
        cert["status"]
        == "Q79_SHARED_Z64_FINITE_MONODROMY_SOURCE_MAP_CLOSED_UNIQUE_HYM_TRANSVERSE_ACTION_OPEN",
        "same-source monodromy status changed",
    )
    require(
        finite["S3_presentation_homomorphism_generator_images"]
        == [[0, 0], [32, 32]],
        "the S3-to-Z64 homomorphism classification changed",
    )
    transpositions = [
        row for row in finite["class_table"] if row["cycle_type"] == "transposition"
    ]
    three_cycles = [
        row for row in finite["class_table"] if row["cycle_type"] == "three_cycle"
    ]
    require(len(transpositions) == 3, "transposition class size changed")
    require(all(row["Z64_image"] == 32 for row in transpositions), "transposition image changed")
    require(all(row["Z64_image"] == 0 for row in three_cycles), "three-cycle image changed")
    require(
        tiers["finite_same_source_q79_to_Z64_monodromy_map"] == "CLOSED_UNIQUE",
        "finite same-source map was lost",
    )
    require(tiers["differential_HYM_emission_of_shared_connection"] == "OPEN", "HYM overclaim")
    require(
        tiers["physical_transverse_frame_connection_identification"] == "OPEN",
        "transverse-frame overclaim",
    )
    require(guards["claims_selected_action_closed"] is False, "selected action overclaim")
    require(
        guards["claims_final_integral_branch_selected"] is False,
        "final integral branch overclaim",
    )

    print(
        "AUDIT_PASS: the selected q79 sign monodromy uniquely emits the shared "
        "Z64 half-turn; differential HYM, transverse, and action gates remain open"
    )


if __name__ == "__main__":
    main()
