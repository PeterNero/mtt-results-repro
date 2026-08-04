"""Audit the selected Qa/SU3 monad map construction/source augmentation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_monad_map_construction_or_source_augmentation_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Monad_Map_Construction_or_Source_Augmentation_v1.md"
SCRIPT = REPO / "scripts" / "construct_selected_qa_su3_monad_map_or_source_augmentation.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    result = cert["construction_result"]
    gates = cert["gate_results"]
    rows = cert["charge_table"]
    tools = cert["source_scan"]["usable_for_monad_map_construction"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_MONAD_MAP_CONSTRUCTION_BLOCKED_SECTION_RING_OR_SOURCE_AUGMENTATION_REQUIRED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["charge_table"] == cert["charge_table"]
            and computed["gate_results"] == cert["gate_results"]
            and computed["construction_result"] == cert["construction_result"],
            computed["construction_result"],
        ),
        check(
            "five charge rows computed",
            len(rows) == 5 and all(row["composite_charge_matches_K2_minus_K1"] for row in rows),
            rows,
        ),
        check(
            "composite charge is K2 minus K1",
            cert["selected_line_data"]["kappa_2_minus_kappa_1"] == [-1, 1, 0]
            and all(row["composite_charge_gi_fi"] == [-1, 1, 0] for row in rows),
            cert["selected_line_data"],
        ),
        check(
            "selected source lacks section construction tools",
            tools["selected_source_has_section_ring"] is False
            and tools["selected_source_has_effective_cone"] is False
            and tools["selected_source_has_line_bundle_sections"] is False
            and gates["section_ring_or_effective_cone"] == "FAIL_NOT_FOUND_IN_SELECTED_MONAD_SOURCE",
            tools,
        ),
        check(
            "maps are not constructed",
            result["explicit_f_g_constructed"] is False
            and result["g_f_zero_checked"] is False
            and gates["actual_f_sections"].startswith("FAIL")
            and gates["actual_g_sections"].startswith("FAIL")
            and gates["gf_zero"].startswith("FAIL"),
            {"result": result, "gates": gates},
        ),
        check(
            "monad route not retired but augmentation required",
            result["monad_route_retired"] is False
            and result["source_augmentation_required"] is True
            and result["qa_su3_closed"] is False
            and result["target_fitting_used"] is False,
            result,
        ),
        check(
            "note records next section-ring interface",
            "Selected_Qa_SU3_Iwasawa_Line_Bundle_Section_Ring_Interface_v1" in note
            and "charge-level compatibility passed: yes" in note
            and "section data found: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 monad map construction/source augmentation audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
