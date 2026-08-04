"""Audit projector source promotion and dotD transport reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_projector_source_promotion_dotd_transport_reduction.py"
PACKET = ROOT / "candidate_data" / "projector_source_promotion_dotd_transport_reduction.candidate.json"
CERT = ROOT / "certificates" / "projector_source_promotion_dotd_transport_reduction_certificate.json"
NOTE = ROOT / "proof_corpus" / "Projector_Source_Promotion_dotD_Transport_Reduction_v1.md"
STATUS = "PROJECTOR_SOURCE_PROMOTION_AND_DOTD_TRANSPORT_CLOSED_ALPHA1_DRIVER_VALUE_OPEN"


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
    check("all checks pass", all(packet["checks"].values()), packet["checks"])

    closed = packet["closed_now"]
    check(
        "projector and stationary rho_s promoted",
        closed["gauge_transported_trace"]["functional_rho_s_promoted"]
        and closed["transport_conjugation_replay"]["finite_validator_replay_closed"]
        and closed["transport_conjugation_replay"]["selected_source_verified"]
        and closed["finite_projector_source_promotion"][
            "selected_projector_source_verified"
        ]
        and closed["finite_projector_source_promotion"][
            "validator_ready_stationary_rho_s"
        ],
        closed,
    )
    check(
        "dotD source formula closed",
        closed["dotD_transport_derivative"]["transport_derivative_formula_closed"]
        and closed["dotD_transport_derivative"][
            "selected_dotD_source_verified_by_transport_derivative"
        ],
        closed["dotD_transport_derivative"],
    )
    open_items = packet["still_open"]
    check(
        "alpha1 value and full replay remain open",
        open_items["alpha1_driver_verified"] is False
        and open_items["dotD_validator_full_replay_closed"] is False
        and open_items["normalization_value_emitted"] is False
        and open_items["selected_transfer_normalization"] is False,
        open_items,
    )
    update = packet["frontier_update"]
    check(
        "frontier moved to alpha1 value",
        update["current_next"] == "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1"
        and update["parallel_transfer_next"]
        == "MTT_Selected_SectorCharge_GramTransferNormalization_Packet_v1",
        update,
    )
    check("guardrails retained", all(v is True for v in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "stationary `rho_s` is validator-ready",
        "`dotD_alpha1` transport derivative/source formula is also closed",
        "selected `alpha1` driver value",
        "C1 response",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nProjector source promotion dotD transport reduction audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
