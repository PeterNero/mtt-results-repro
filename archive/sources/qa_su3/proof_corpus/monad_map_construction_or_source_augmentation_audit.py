"""Audit the selected Qa/SU3 monad map-construction/source-augmentation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "monad_map_construction_or_source_augmentation_certificate.json"
DATA = REPO / "candidate_data" / "monad_map_construction_or_source_augmentation.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Monad_Map_Construction_or_Source_Augmentation_v1.md"
SCRIPT = REPO / "scripts" / "build_monad_map_construction_or_source_augmentation.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    result = data["construction_result"]
    table = data["charge_table"]
    selected_scan = data["source_scan"]["usable_for_monad_map_construction"]
    checks = [
        check("status", cert["status"] == "QA_SU3_MONAD_MAP_CONSTRUCTION_BLOCKED_SECTION_RING_OR_SOURCE_AUGMENTATION_REQUIRED", cert["status"]),
        check("script agreement", computed["charge_table"] == cert["charge_table"], computed["charge_table"]),
        check("five rows", len(table) == 5, len(table)),
        check("first row", table[0]["required_f_section_charge"] == [-3, 0, 1] and table[0]["required_g_section_charge"] == [2, 1, -1], table[0]),
        check("middle row", table[2]["required_f_section_charge"] == [0, -1, 0] and table[2]["required_g_section_charge"] == [-1, 2, 0], table[2]),
        check("last row", table[4]["required_f_section_charge"] == [1, 1, 1] and table[4]["required_g_section_charge"] == [-2, 0, -1], table[4]),
        check("all composite charges", all(row["composite_charge_gi_fi"] == [-1, 1, 0] for row in table), table),
        check("charge compatibility", result["charge_level_compatibility_passed"] is True and data["gate_results"]["charge_compatibility"].startswith("PASS"), result),
        check("blocked by missing sections", result["section_data_found"] is False and result["source_augmentation_required"] is True, result),
        check("selected source lacks section ring", selected_scan["selected_source_has_section_ring"] is False and selected_scan["selected_source_has_line_bundle_sections"] is False, selected_scan),
        check("no closure", result["qa_su3_closed"] is False and cert["closure_claimed"] is False, cert),
        check("note records next", cert["next_required_artifact"] in note and "section data found: no" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 monad map construction/source augmentation audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
