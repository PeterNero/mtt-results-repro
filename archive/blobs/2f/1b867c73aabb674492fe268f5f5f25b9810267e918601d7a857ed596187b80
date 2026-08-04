"""Audit the selected Qa/SU3 symmetry-breaking route triage."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_symmetry_breaking_route_triage_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_orientation_carrying_de_dotd_source.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Symmetry_Breaking_Route_Triage_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_symmetry_breaking_route_triage.py"


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
    closed = cert["closed_now"]
    routes = cert["route_ranking"]
    wall = cert["wall_route"]
    dotd = cert["de_dotd_route"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_SYMMETRY_BREAKING_TRIAGE_DE_DOTD_PRIMARY_WALL_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["route_ranking"] == routes
            and computed["wall_route"] == wall
            and computed["not_closed"] == cert["not_closed"],
            computed["status"],
        ),
        check(
            "wall dictionary imported",
            closed["target_wall_dictionary_imported"] is True
            and closed["target_wall_requires_r1_over_r2_sqrt2"] is True
            and wall["target_radius_condition"] == "r1:r2 = sqrt(2):1"
            and wall["target_p_ratio"] == "1:2",
            wall,
        ),
        check(
            "equal radius rejected as target wall",
            closed["equal_radius_constants_import_rejected_as_target_wall"] is True
            and wall["constants_matches_target_wall"] is False
            and wall["constants_no_go_theorem"]
            == "The closed constants selected radius cannot be the visible L2 target-wall selector.",
            wall,
        ),
        check(
            "dotD route has executable validator",
            closed["orientation_dependencies_compared"] is True
            and closed["m_label_to_q_label_conditional_map_formulated"] is True
            and closed["finite_dotD_response_validator_ready"] is True
            and dotd["dotd_validator_status"]
            == "IWASAWA_DOTD_RESPONSE_VALIDATOR_FORMULATED_DATA_OPEN",
            dotd["dotd_validator_status"],
        ),
        check(
            "route ranking is explicit",
            routes[0]["route"] == "selected_orientation_carrying_D_E_dotD"
            and routes[1]["route"] == "non_equal_radius_gauduchon_wall"
            and routes[2]["route"] == "ordered_integral_cech_automorphy_source"
            and routes[3]["route"] == "holonomy_sensitive_pic0_rule_only",
            routes,
        ),
        check(
            "template forbids observed branch choice",
            template["schema"] == "SelectedQaSU3OrientationCarryingDEDotDSource.v1"
            and "Do not use observed CP sign to choose between conjugate packets."
            in template["forbidden_shortcuts"]
            and template["must_supply"]["selected_D_E_action"] is None,
            template,
        ),
        check(
            "no overclaim",
            guardrails["claims_unique_m_label_now"] is False
            and guardrails["claims_selected_DE_or_dotD_constructed"] is False
            and guardrails["claims_equal_radius_selects_target"] is False
            and guardrails["claims_full_SM_closure"] is False,
            guardrails,
        ),
        check(
            "note records primary route",
            "D_E/dotD" in note
            and "r1:r2=sqrt(2):1" in note
            and "equal-radius" in note
            and "observed CP sign" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 symmetry-breaking route triage audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
