"""Audit the V_alpha/S3 symmetry-breaking route triage."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "valpha_s3_symmetry_breaking_route_triage_certificate.json"
CANDIDATE = REPO / "candidate_data" / "valpha_s3_symmetry_breaking_route_triage.candidate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_orientation_carrying_de_dotd_source.template.json"
NOTE = REPO / "proof_corpus" / "VAlpha_S3_Symmetry_Breaking_Route_Triage_v1.md"
SCRIPT = REPO / "scripts" / "analyze_valpha_s3_symmetry_breaking_route_triage.py"


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
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    closed = cert["closed_now"]
    routes = cert["route_ranking"]
    wall = cert["wall_route"]
    de_dotd = cert["de_dotd_route"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "VALPHA_S3_SYMMETRY_BREAKING_TRIAGE_DE_DOTD_PRIMARY_SOURCE_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["route_ranking"] == routes
            and computed["de_dotd_route"] == de_dotd,
            computed["status"],
        ),
        check(
            "closed reductions imported",
            closed["two_block_selector_reduction_closed"] is True
            and closed["equal_radius_import_rejected_as_target_wall"] is True
            and closed["finite_dotD_response_validator_ready"] is True
            and closed["m1_deresponse_stack_coherent_conditionally"] is True,
            closed,
        ),
        check(
            "wall route classified",
            wall["target_radius_condition"] == "r1:r2 = sqrt(2):1"
            and wall["target_p_ratio"] == "1:2"
            and wall["equal_radius_matches_target"] is False,
            wall,
        ),
        check(
            "de dotd primary",
            de_dotd["status"] == "PRIMARY_LIVE_ROUTE_SOURCE_OPEN"
            and de_dotd["m1_target_status"]
            == "TIME_ORIENTED_M1_DERESPONSE_TARGET_COHERENT_SELECTED_SOURCE_OPEN"
            and de_dotd["dotd_validator_status"]
            == "IWASAWA_DOTD_RESPONSE_VALIDATOR_FORMULATED_DATA_OPEN",
            de_dotd,
        ),
        check(
            "route ranking",
            routes[0]["route"] == "selected_orientation_carrying_D_E_dotD"
            and routes[1]["route"] == "non_equal_radius_gauduchon_wall"
            and routes[2]["route"] == "ordered_integral_cech_automorphy_source"
            and routes[3]["route"] == "holonomy_sensitive_pic0_rule_only",
            routes,
        ),
        check(
            "template exists and forbids shortcuts",
            template["schema"] == "SelectedQaSU3OrientationCarryingDEDotDSource.v1"
            and template["operator_data"]["selected_D_E_action"] is None
            and "Do not use observed CP sign to choose between conjugate packets."
            in template["forbidden_shortcuts"],
            template,
        ),
        check(
            "guardrails",
            all(value is False for value in guardrails.values()),
            guardrails,
        ),
        check(
            "note records ranking",
            "selected orientation-carrying D_E/dotD" in note
            and "r1:r2=sqrt(2):1" in note
            and "equal-radius" in note
            and "observed CP sign" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["status"] == cert["status"]
            and candidate["route_ranking"] == cert["route_ranking"],
            candidate["status"],
        ),
    ]

    print("\nV_alpha/S3 symmetry-breaking route triage audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
