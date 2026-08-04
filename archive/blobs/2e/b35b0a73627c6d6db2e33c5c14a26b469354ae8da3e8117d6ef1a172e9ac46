"""Audit the time-oriented m=1 visible Green-Schwarz source gate."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "attempt_time_oriented_m1_visible_gs_source.py"
VALIDATOR = REPO / "scripts" / "validate_time_oriented_m1_visible_gs_source.py"
REQUIREMENT_CERT = REPO / "certificates" / "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
TEMPLATE = REPO / "certificates" / "time_oriented_m1_visible_gs_source.template.json"
ATTEMPT = REPO / "certificates" / "time_oriented_m1_visible_gs_source.attempt.json"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_visible_gs_source_attempt.candidate.json"
CERT = REPO / "certificates" / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_Visible_Green_Schwarz_Source_Gate_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: str) -> tuple[str, bool, str]:
    return name, condition, detail


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def packet_fixture(path: Path, *, row_matches: bool, selected_source: bool) -> None:
    requirement = load_json(REQUIREMENT_CERT)
    row = requirement["derived_required_visible_row"]["Tr_F_visible_squared"]
    if not row_matches:
        row = ["0", "0", "0"]
    packet = {
        "schema": "TimeOrientedM1VisibleGreenSchwarzSource.v1",
        "status": "SELECTED_VISIBLE_GREEN_SCHWARZ_SOURCE_VERIFIED",
        "requirement_certificate": "time_oriented_m1_visible_green_schwarz_requirement_certificate.json",
        "selected_by_mtt": selected_source,
        "same_branch_as_q79_m1": True,
        "fixture_only": False,
        "curvature_rows": {
            "dH": requirement["known_rows"]["dH"],
            "Tr_R_plus_squared": requirement["known_rows"]["Tr_R_plus_squared"],
            "Tr_F_visible_squared": row,
            "residual": requirement["derived_required_visible_row"]["residual_if_supplied"],
        },
        "visible_source_evidence": {
            "source_kind": "finite_HYM_Strominger_solve",
            "selected_visible_bundle_model": selected_source,
            "same_branch_q79_f_m1": True,
            "chern_weil_row_from_source": selected_source,
            "hym_or_route_c_residual_verified": selected_source,
            "source_certificate": "unit_test_selected_visible_source.json",
        },
        "uses_observed_flavor_data": False,
        "uses_benchmark_flavor_entries": False,
    }
    path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    proc = run_script()
    checks: list[tuple[str, bool, str]] = [
        check("constructor exits 0", proc.returncode == 0, proc.stdout[:1000]),
        check("validator exists", VALIDATOR.exists(), str(VALIDATOR)),
        check("template exists", TEMPLATE.exists(), str(TEMPLATE)),
        check("attempt exists", ATTEMPT.exists(), str(ATTEMPT)),
        check("candidate exists", CANDIDATE.exists(), str(CANDIDATE)),
        check("certificate exists", CERT.exists(), str(CERT)),
        check("paper exists", PAPER.exists(), str(PAPER)),
    ]

    if ATTEMPT.exists() and CERT.exists() and CANDIDATE.exists() and PAPER.exists():
        cert = load_json(CERT)
        attempt = load_json(ATTEMPT)
        calc = cert.get("calculation_results", {})
        attempted_source = cert.get("attempted_source", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        paper = PAPER.read_text(encoding="utf-8")
        template_proc = run_validator(TEMPLATE)
        attempt_proc = run_validator(ATTEMPT)

        checks.extend(
            [
                check(
                    "status blocked selected source missing",
                    cert.get("status")
                    == "TIME_ORIENTED_M1_VISIBLE_GS_SOURCE_ATTEMPT_BLOCKED_SELECTED_SOURCE_MISSING",
                    str(cert.get("status")),
                ),
                check(
                    "attempt row filled but unselected",
                    attempted_source.get("required_visible_row_filled") is True
                    and attempted_source.get("selected_by_mtt") is False
                    and attempted_source.get("selected_visible_bundle_model") is False
                    and attempted_source.get("chern_weil_row_from_source") is False,
                    str(attempted_source),
                ),
                check(
                    "template refused as open",
                    template_proc.returncode == 2
                    and "packet is OPEN" in template_proc.stdout,
                    template_proc.stdout.strip(),
                ),
                check(
                    "attempt refused by validator",
                    attempt_proc.returncode == 1
                    and "selected_by_mtt must be true" in attempt_proc.stdout
                    and "selected visible bundle model must be supplied" in attempt_proc.stdout,
                    attempt_proc.stdout.strip(),
                ),
                check(
                    "calculation closes gate only",
                    calc.get("source_packet_schema_and_validator_created") is True
                    and calc.get("required_visible_TrF_row_inserted") is True
                    and calc.get("validator_rejects_current_attempt") is True
                    and calc.get("selected_visible_source_constructed") is False,
                    str(calc),
                ),
                check(
                    "what closes and remains",
                    closes.get("executable_selected_visible_source_gate") is True
                    and closes.get("attempt_packet_with_exact_required_row") is True
                    and still_open.get("selected_visible_bundle_model_realizing_required_row")
                    is True
                    and still_open.get("Chern_Weil_derivation_from_selected_source") is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                check(
                    "guardrails",
                    guardrails.get("claims_attempt_source_selected") is False
                    and guardrails.get("claims_visible_green_schwarz_verified") is False
                    and guardrails.get("claims_selected_D_E_dotD_constructed") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                check(
                    "paper records source gate",
                    "selected visible Green-Schwarz source packet" in paper
                    and "Chern-Weil row derived from that source" in paper
                    and "rejected by the validator" in paper,
                    "paper source gate present",
                ),
                check(
                    "attempt carries exact row",
                    attempt.get("curvature_rows", {}).get("Tr_F_visible_squared")
                    == load_json(REQUIREMENT_CERT)
                    .get("derived_required_visible_row", {})
                    .get("Tr_F_visible_squared"),
                    str(attempt.get("curvature_rows", {})),
                ),
            ]
        )

    if VALIDATOR.exists():
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            passing = tmpdir / "passing_visible_source.json"
            bad_row = tmpdir / "bad_row_visible_source.json"
            missing_source = tmpdir / "missing_source_visible_source.json"
            packet_fixture(passing, row_matches=True, selected_source=True)
            packet_fixture(bad_row, row_matches=False, selected_source=True)
            packet_fixture(missing_source, row_matches=True, selected_source=False)
            pass_proc = run_validator(passing)
            bad_row_proc = run_validator(bad_row)
            missing_source_proc = run_validator(missing_source)
            checks.extend(
                [
                    check(
                        "validator accepts selected exact-row fixture",
                        pass_proc.returncode == 0
                        and "visible Green-Schwarz source PASS" in pass_proc.stdout,
                        pass_proc.stdout.strip(),
                    ),
                    check(
                        "validator rejects wrong row",
                        bad_row_proc.returncode == 1
                        and "must equal the derived required visible row" in bad_row_proc.stdout,
                        bad_row_proc.stdout.strip(),
                    ),
                    check(
                        "validator rejects missing selected source",
                        missing_source_proc.returncode == 1
                        and "selected_by_mtt must be true" in missing_source_proc.stdout
                        and "Chern-Weil row must be derived" in missing_source_proc.stdout,
                        missing_source_proc.stdout.strip(),
                    ),
                ]
            )

    print("Time-oriented m=1 visible Green-Schwarz source gate audit")
    print("=========================================================")
    failures = 0
    for name, ok, detail in checks:
        print(f"{name:55} {'PASS' if ok else 'FAIL'}  {detail}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
