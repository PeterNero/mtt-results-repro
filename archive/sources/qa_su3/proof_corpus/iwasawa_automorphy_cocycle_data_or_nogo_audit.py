"""Audit the Iwasawa automorphy cocycle data/no-go gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "iwasawa_automorphy_cocycle_data_or_nogo_certificate.json"
TEMPLATE = REPO / "certificates" / "iwasawa_automorphy_cocycle_data.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Iwasawa_Automorphy_Cocycle_Data_or_NoGo_v1.md"
SCRIPT = REPO / "scripts" / "build_iwasawa_automorphy_cocycle_data_or_nogo.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    selected_terms = cert["selected_source_scan"]["terms"]
    theta_terms = cert["theta_adjacent_scan"]["terms"]
    flat = cert["flat_character_test"]
    nogo = cert["nogo_result"]
    gates = cert["gate_results"]
    checks = [
        check("status", cert["status"] == "QA_SU3_IWASAWA_AUTOMORPHY_COCYCLE_DATA_CURRENT_SOURCE_NO_GO", cert["status"]),
        check("script agreement", computed["nogo_result"] == cert["nogo_result"] and computed["gate_results"] == cert["gate_results"], computed["nogo_result"]),
        check("template remains open", template["status"] == "OPEN_SELECTED_QA_SU3_IWASAWA_AUTOMORPHY_COCYCLE_DATA_REQUIRED" and template["charge_to_factor_map"] is None and template["selected_geometry"]["lattice_generators"] is None, template["status"]),
        check("selected source partial geometry only", selected_terms["H3C"] is True and selected_terms["Gamma_subset"] is True and selected_terms["lattice_generators"] is False and selected_terms["factor_of_automorphy"] is False and selected_terms["charge_to_factor"] is False, selected_terms),
        check("flat character rejected", flat["cocycle_passes_formally"] is True and flat["multiplicative_charge_law_passes_formally"] is True and flat["realizes_nonzero_c1_charges"] is False and flat["nonzero_charges_count"] == 11 and gates["flat_character_shortcut"].startswith("FAIL"), flat),
        check("theta import rejected", theta_terms["real_heisenberg_nilmanifold"] is True and cert["theta_adjacent_result"]["usable_for_complex_iwasawa_line_bundle_automorphy"] is False and gates["theta_heisenberg_import"].startswith("FAIL"), cert["theta_adjacent_result"]),
        check("route open but no closure", nogo["current_source_cocycle_data_sufficient"] is False and nogo["automorphy_route_retired"] is False and nogo["source_augmentation_required"] is True and nogo["qa_su3_closed"] is False and cert["closure_claimed"] is False, nogo),
        check("note records augmentation next", cert["next_required_artifact"]["name"] in note and "flat character route rejected: yes" in note and "automorphy route retired: no" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 Iwasawa automorphy cocycle data/no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
