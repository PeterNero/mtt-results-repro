"""Audit the sector-charge / Gram-transfer normalization packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_sectorcharge_gram_transfernormalization_packet.py"
CANDIDATE = ROOT / "candidate_data" / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
CERT = ROOT / "certificates" / "selected_sectorcharge_gram_transfernormalization_packet_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorCharge_GramTransferNormalization_Packet_v1.md"

STATUS = "MTT_SELECTED_SECTORCHARGE_GRAM_TRANSFERNORMALIZATION_PACKET_BUILT_SOURCE_CHARGE_OPEN"
NEXT = "MTT_Selected_SectorCharge_or_ZeroModeBasis_SourceEmission_v1"


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
    charge = data["sector_charge_packet"]
    gram = data["gram_transfer_packet"]
    decision = data["transfer_to_alpha1_decision"]
    open_fields = data["minimal_open_fields"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "conditional Gram forced",
            gram["conditional_gram_theorem_proved"] is True
            and gram["gram_conditionally_forced_after_rho_s"] is True
            and gram["matter_T3_norms_equal"] is True
            and abs(gram["raw_T3_frobenius_norm_per_matter_sector"] - 2**0.5) < 1e-12,
            gram,
        ),
        check(
            "sector charge still open",
            charge["selected"] is False
            and charge["current_selected_data_uniform"] is True
            and charge["required_phase_route"] == ["u", "e"]
            and charge["required_shift_route"] == ["d", "nuD"],
            charge,
        ),
        check(
            "transfer not promoted",
            gram["physical_transfer_normalization_selected"] is False
            and decision["selected_transfer_normalization"] is False
            and decision["alpha1_driver_verified"] is False
            and cert["selected_transfer_normalization"] is False,
            decision,
        ),
        check(
            "open fields are source fields",
            open_fields["selected_zero_mode_bases_K_s"]["closed"] is False
            and open_fields["selected_rho_s_source_map"]["closed"] is False
            and open_fields["selected_1M_Dirac_neutrino_rule"]["closed"] is False,
            open_fields,
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
            and "not numerical scalar choice" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected sector-charge / Gram-transfer normalization packet audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
