"""Audit the Iwasawa automorphy/section-ring construction attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_iwasawa_automorphy_or_section_ring_construction_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_iwasawa_automorphy_section_ring.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Iwasawa_Automorphy_or_Section_Ring_Construction_v1.md"
SCRIPT = REPO / "scripts" / "construct_selected_qa_su3_iwasawa_automorphy_or_section_ring.py"


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
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    result = cert["construction_result"]
    routes = cert["route_assessment"]
    gates = cert["gate_results"]
    relation = cert["symbolic_rank_one_relation"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_IWASAWA_AUTOMORPHY_SECTION_RING_CONSTRUCTION_SYMBOLIC_ONLY_VALUES_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["construction_result"] == cert["construction_result"]
            and computed["route_assessment"] == cert["route_assessment"]
            and computed["gate_results"] == cert["gate_results"],
            computed["construction_result"],
        ),
        check(
            "template remains open",
            template["status"] == "OPEN_SELECTED_QA_SU3_IWASAWA_AUTOMORPHY_OR_SECTION_RING_REQUIRED"
            and template["section_space_dimensions"] is None
            and template["multiplication_constants"] is None,
            template["status"],
        ),
        check(
            "routes retired or left open correctly",
            routes["literal_constant_route"] == "REJECTED_NONZERO_CHARGES"
            and routes["torus_theta_shortcut"] == "REJECTED_NO_IWASAWA_TRANSFER_THEOREM"
            and routes["automorphy_route"] == "OPEN_REQUIRES_FACTOR_OF_AUTOMORPHY_COCYCLE",
            routes,
        ),
        check(
            "symbolic relation built",
            result["symbolic_rank_one_relation_built"] is True
            and len(relation["terms"]) == 5
            and relation["relation"].startswith("m1*u1*v1")
            and cert["product_charge_check"]["all_products_land_in_P"] is True,
            relation,
        ),
        check(
            "actual automorphy values still open",
            gates["automorphy_cocycle"].startswith("FAIL")
            and gates["section_space_dimensions"].startswith("FAIL")
            and gates["multiplication_constants"].startswith("FAIL")
            and result["actual_automorphy_factors_found"] is False
            and result["section_dimensions_found"] is False,
            {"gates": gates, "result": result},
        ),
        check(
            "no closure claimed",
            result["literal_constant_route_retired"] is True
            and result["torus_theta_shortcut_retired_until_transfer_theorem"] is True
            and result["automorphy_schema_built"] is True
            and result["explicit_f_g_constructed"] is False
            and result["g_f_zero_proved"] is False
            and result["qa_su3_closed"] is False
            and result["target_fitting_used"] is False,
            result,
        ),
        check(
            "note records cocycle next",
            "Selected_Qa_SU3_Iwasawa_Automorphy_Cocycle_Data_or_NoGo_v1" in note
            and "symbolic rank-one relation built: yes" in note
            and "actual automorphy factors found: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 Iwasawa automorphy/section-ring construction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
