"""Audit source-action or matter-slot routing source cutset theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem.py"
CANDIDATE = ROOT / "candidate_data" / "selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem.candidate.json"
CERT = ROOT / "certificates" / "selected_sector_zero_mode_source_action_or_matter_slot_routing_source_theorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorZeroMode_SourceAction_or_SelectedMatterSlotRouting_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_SECTOR_SOURCE_ACTION_OR_ROUTING_CUTSET_THEOREM_PROVED_SOURCE_PAYLOAD_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_SourcePayload_Search_or_Emission_Attempt_v1"


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

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("theorem proved", data["theorem"]["proved"] is True and data["cutset_closed"] is True, data["theorem"]),
        check(
            "route A requirements",
            data["route_A"]["passes_now"] is False
            and "selected source map rho_s: End0(V_alpha)->so(K_s)" in data["route_A"]["required_payload"],
            data["route_A"],
        ),
        check(
            "route B requirements",
            data["route_B"]["passes_now"] is False
            and "selected 1_M Dirac-neutrino/singlet rule" in data["route_B"]["required_payload"],
            data["route_B"],
        ),
        check(
            "shortcuts forbidden",
            "promote universal End0 carrier matrices as selected rho_s without selected zero-mode bases" in data["forbidden_shortcuts"]
            and "use observed masses, mixings, CKM/PMNS, or gauge couplings to select the route" in data["forbidden_shortcuts"],
            data["forbidden_shortcuts"],
        ),
        check(
            "payload still open",
            data["selected_payload_emitted"] is False
            and cert["selected_payload_emitted"] is False
            and data["next_required_artifact"] == NEXT,
            cert,
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "note records cutset",
            "remaining sector gate can close only through one of two same-source payloads" in note
            and "Forbidden Shortcuts" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected sector source-action/routing cutset audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
