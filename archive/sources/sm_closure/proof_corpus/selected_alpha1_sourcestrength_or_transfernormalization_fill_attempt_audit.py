"""Audit alpha1 source-strength or transfer-normalization fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_alpha1_sourcestrength_or_transfernormalization_fill_attempt.py"
CANDIDATE = ROOT / "candidate_data" / "selected_alpha1_sourcestrength_or_transfernormalization_fill_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_alpha1_sourcestrength_or_transfernormalization_fill_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Alpha1_SourceStrength_or_TransferNormalization_FillAttempt_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_SOURCESTRENGTH_OR_TRANSFERNORMALIZATION_ATTEMPT_BUILT_TRANSFER_CUTSET_OPEN"
NEXT = "MTT_Selected_SectorCharge_GramTransferNormalization_Packet_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    route_a = data["route_A_same_source_source_strength"]
    route_b = data["route_B_typed_transfer_normalization"]
    cutset = data["minimal_cutset"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "route A tested but not closed",
            route_a["attempted"] is True
            and route_a["closed"] is False
            and route_a["source_identity_selected"] is True
            and route_a["candidate_value"]["lambda_alpha1_candidate"] == 1.0
            and "coordinate convention" in route_a["forbidden_shortcut"],
            route_a,
        ),
        check(
            "route B tested but not closed",
            route_b["attempted"] is True
            and route_b["closed"] is False
            and route_b["transfer_checks"]["K1_ckm_retarded_kernel_pattern_available"] is True
            and route_b["transfer_checks"]["K4_selected_sector_charge_or_chirality"] is False
            and route_b["transfer_checks"]["K5_selected_transfer_normalization"] is False,
            route_b,
        ),
        check(
            "cutset is sharp",
            cutset["route_A_same_source_coordinate"]["source_identity_selected"] is True
            and cutset["route_B_typed_transfer"]["selected_sector_charge_or_chirality"] is False
            and cutset["route_B_typed_transfer"]["selected_transfer_normalization"] is False
            and cutset["shared_final_replay"]["source_only_fails_only_by_alpha1_driver"] is True,
            cutset,
        ),
        check(
            "no promotion",
            data["no_promotion_decision"]["selected_value_emitted"] is False
            and data["no_promotion_decision"]["alpha1_driver_verified"] is False
            and cert["alpha1_driver_verified"] is False,
            data["no_promotion_decision"],
        ),
        check(
            "no target fitting or closure",
            data["target_fitting_used"] is False
            and data["closure_claimed"] is False
            and cert["target_fitting_used"] is False
            and cert["closure_claimed"] is False,
            cert,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "sector-charge plus Gram/transfer-normalization packet" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected alpha1 source-strength or transfer-normalization fill attempt audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
