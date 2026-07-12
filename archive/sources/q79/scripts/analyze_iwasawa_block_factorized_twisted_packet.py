"""Analyze the block-factorized Iwasawa twisted packet candidate.

The packet is the first executable version of the route forced by the qutrit
obstruction: keep the nontrivial zeta_3 projective twist in the family block,
and keep the Higgs as a separate ordinary rank-one line.  This closes the
finite architecture check, not selected MTT promotion.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKET = ROOT / "candidate_data" / "iwasawa_block_factorized_twisted_packet.candidate.json"
ROUTE_CERT = ROOT / "certificates" / "iwasawa_block_factorized_twist_route_certificate.json"


def run(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def parse_report(output: str) -> dict[str, Any]:
    match = re.search(r"block_factorized_report=(\{.*\})", output)
    if not match:
        raise ValueError("missing block_factorized_report in validator output")
    return json.loads(match.group(1))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def analyze(packet_path: Path = DEFAULT_PACKET) -> dict[str, Any]:
    code, output = run(
        [
            sys.executable,
            str(ROOT / "scripts" / "validate_iwasawa_block_factorized_twisted_packet.py"),
            str(packet_path),
        ]
    )
    report = parse_report(output) if code == 0 else {}
    route_cert = load_json(ROUTE_CERT)
    projective_report = report.get("family_twist_block", {}).get("projective_report", {})
    coupling = report.get("coupling_rule", {})

    return {
        "calculation": "IwasawaBlockFactorizedTwistedPacketCandidateAnalysis",
        "packet_path": str(packet_path),
        "packet_validator_exit": code,
        "block_factorized_candidate_valid": report.get("block_factorized_candidate_valid") is True,
        "family_projective_gerbe_gluing_passes": projective_report.get(
            "projective_gerbe_gluing_passes"
        )
        is True,
        "family_central_twist_nontrivial": projective_report.get("central_twist_is_nontrivial")
        is True,
        "family_strict_vector_bundle_gluing_passes": projective_report.get(
            "strict_vector_bundle_gluing_passes"
        )
        is True,
        "family_nontrivial_corner_count": projective_report.get("nontrivial_central_twist_count"),
        "higgs_line_rank_one_projector": report.get("higgs_line_block", {}).get(
            "rank_one_projector"
        )
        is True,
        "higgs_line_strict_gluing_passes": report.get("higgs_line_block", {}).get(
            "ordinary_line_strict_gluing_passes"
        )
        is True,
        "sector_partition_complete": report.get("sector_partition", {}).get(
            "covers_all_sm_slots"
        )
        is True,
        "naive_rank4_direct_sum_rejected": route_cert.get("what_this_closes", {}).get(
            "naive_direct_sum_repair_rejected"
        )
        is True,
        "finite_invariant_pairing_rule": coupling.get("finite_invariant_pairing_rule"),
        "same_twist_all_family_allowed_for_trivial_Higgs": coupling.get(
            "same_twist_all_family_allowed_for_trivial_Higgs"
        )
        is True,
        "conjugate_orientation_pairing_required": coupling.get(
            "conjugate_orientation_pairing_required"
        )
        is True,
        "selected_sector_orientation_assignment_supplied": coupling.get(
            "selected_sector_orientation_assignment_supplied"
        )
        is True,
        "single_rank4_scalar_projective_carrier_allowed": coupling.get(
            "single_rank4_scalar_projective_carrier_allowed"
        )
        is True,
        "selected_source_promotion_ready": report.get("selected_source_promotion_ready") is True,
        "full_sm_data_ready": report.get("full_sm_data_ready") is True,
        "remaining_selected_inputs": [
            "selected Deligne/Cech gerbe or B-field representative on the fixed Iwasawa sector",
            "full Green-Schwarz Bianchi and Freed-Witten checks for that representative",
            "selected D_E and dotD contracts on the block-factorized carrier",
            "primitive C1 response contractions",
            "Yukawa overlap weights and kinetic/RG matching",
        ],
        "verdict": {
            "finite_block_architecture_closed": code == 0
            and report.get("block_factorized_candidate_valid") is True,
            "selected_mtt_promotion_closed": False,
            "full_sm_closure_closed": False,
            "next_step": "replace the candidate gerbe holonomy map with a selected differential-cohomology representative and compute D_E/dotD on the factorized blocks",
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
