"""Audit the End0-to-sector functor value-packet reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_end0_sector_functor_value_packet_reduction.py"
PACKET = ROOT / "candidate_data" / "end0_sector_functor_value_packet_reduction.candidate.json"
CERT = ROOT / "certificates" / "end0_sector_functor_value_packet_reduction_certificate.json"
NOTE = ROOT / "proof_corpus" / "End0_SectorFunctor_Value_Packet_Reduction_v1.md"
STATUS = "END0_SECTOR_FUNCTOR_PACKET_REDUCED_TO_SELECTED_PROJECTOR_SOURCE_PROMOTION_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    check("status", cert["status"] == STATUS, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem agrees", packet["theorem"] == cert["theorem"], cert["theorem"])
    check("reduction theorem proved", cert["theorem"]["proved"] is True, cert["theorem"])

    checks = packet["reduction_checks"]
    check("all reduction checks pass", all(checks.values()), checks)

    support = packet["closed_support"]
    check(
        "carrier and representation support closed",
        support["End0_tensor_product_carrier"]["constructed"]
        and support["End0_tensor_product_carrier"]["sector_projectors_constructed"]
        and support["adjoint_triplet_realization"]["theorem_proved"]
        and support["adjoint_triplet_realization"][
            "conditional_representation_choice_closed"
        ],
        support,
    )
    check(
        "source map and projectors are support not selected",
        support["canonical_source_map"]["constructed"]
        and support["canonical_source_map"]["selected_source_map_emitted"] is False
        and support["model_active_projectors"]["finite_projector_values_emitted"]
        and support["model_active_projectors"][
            "selected_HYM_projector_values_promoted"
        ]
        is False,
        support,
    )
    blocked = packet["blocked_promotions"]
    check(
        "promotions remain blocked",
        all(v is False for v in blocked.values()),
        blocked,
    )
    update = packet["frontier_update"]
    check(
        "frontier names projector and transfer gates",
        update["old_next"] == "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1"
        and update["current_next_primary"]
        == "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1"
        and update["current_next_parallel"]
        == "MTT_Selected_SectorCharge_or_ZeroModeBasis_SourceEmission_v1",
        update,
    )
    check("guardrails retained", all(v is True for v in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "End0 tensor-product carrier",
        "adjoint triplet",
        "model-active HYM projector values",
        "selected source promotion",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nEnd0 sector functor value-packet reduction audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
