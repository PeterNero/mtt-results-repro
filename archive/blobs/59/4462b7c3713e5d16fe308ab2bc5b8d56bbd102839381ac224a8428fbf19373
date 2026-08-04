"""Audit the selected Qa/SU3 superset source route map."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_superset_source_route_map_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Superset_Source_Route_Map_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_superset_source_route_map.py"


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
    route_ids = {route["id"] for route in cert["routes"]}
    scans = cert["source_scans"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_SUPERSET_SOURCE_ROUTE_MAP_BUILT_PRIMARY_AUTOMORPHY_GERBE_GALERKIN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["route_decision"] == cert["route_decision"]
            and computed["minimal_next_experiment"] == cert["minimal_next_experiment"]
            and computed["closure_claimed"] == cert["closure_claimed"],
            computed["route_decision"],
        ),
        check(
            "all six route classes present",
            route_ids
            == {
                "A_source_augmented_iwasawa_automorphy",
                "B_projective_gerbe_chan_paton",
                "C_direct_operator_galerkin_inverse",
                "D_theta_color_harmonic_normalization",
                "E_m_theory_g2_superset_pushdown",
                "F_source_certified_a01_erratum",
            },
            sorted(route_ids),
        ),
        check(
            "primary route is source augmentation",
            cert["route_decision"]["primary"] == "A_source_augmented_iwasawa_automorphy"
            and cert["minimal_next_experiment"]["name"]
            == "Selected_Qa_SU3_Source_Augmentation_Packet_for_Iwasawa_Monad_Maps_v1",
            cert["route_decision"],
        ),
        check(
            "source scans find the expected adjacent evidence",
            scans["flux_iwasawa"]["terms"]["monad"] is True
            and scans["flux_iwasawa"]["terms"]["HYM"] is True
            and scans["theta_twistor_su3"]["terms"]["color_fiber"] is True
            and scans["q79_twisted_cp"]["terms"]["twisted"] is True,
            scans,
        ),
        check(
            "no closure or fitting claimed",
            cert["closure_claimed"] is False and cert["target_fitting_used"] is False,
            {"closure": cert["closure_claimed"], "target_fitting": cert["target_fitting_used"]},
        ),
        check(
            "note records superset discipline",
            "selected operator packet" in note
            and "Projective gerbe / Chan-Paton route" in note
            and "No route may use the observed `Qa/SU3` residual" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 superset source route map audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
