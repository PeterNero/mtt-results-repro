"""Audit the visible Green-Schwarz requirement derived from the m=1 gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "derive_time_oriented_m1_visible_gs_requirement.py"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_visible_green_schwarz_requirement.candidate.json"
CERT = REPO / "certificates" / "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_Visible_Green_Schwarz_Requirement_v1.md"


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


def main() -> int:
    proc = run_script()
    checks: list[tuple[str, bool, str]] = [
        check("constructor exits 0", proc.returncode == 0, proc.stdout[:1000]),
        check("candidate exists", CANDIDATE.exists(), str(CANDIDATE)),
        check("certificate exists", CERT.exists(), str(CERT)),
        check("paper exists", PAPER.exists(), str(PAPER)),
    ]

    if CANDIDATE.exists() and CERT.exists() and PAPER.exists():
        cert = load_json(CERT)
        candidate = load_json(CANDIDATE)
        known = cert.get("known_rows", {})
        required = cert.get("derived_required_visible_row", {})
        calc = cert.get("calculation_results", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        paper = PAPER.read_text(encoding="utf-8")
        required_row = required.get("Tr_F_visible_squared", [])

        checks.extend(
            [
                check(
                    "status requirement derived source open",
                    cert.get("status")
                    == "TIME_ORIENTED_M1_VISIBLE_GS_REQUIREMENT_DERIVED_SOURCE_OPEN"
                    and candidate.get("status") == cert.get("status"),
                    str(cert.get("status")),
                ),
                check(
                    "known alpha1-only rows",
                    known.get("dH") == ["-4*r3^2", "0", "0"]
                    and known.get("Tr_R_plus_squared")
                    == ["8*r3^2/(r1^2*r2^2)", "0", "0"],
                    str(known),
                ),
                check(
                    "required TrF row derived",
                    required.get("rule") == "Tr F_visible^2 = Tr R_+^2 - dH"
                    and required_row
                    == ["8*r3^2/(r1^2*r2^2) + 4*r3^2", "0", "0"]
                    and required.get("residual_if_supplied") == ["0", "0", "0"],
                    str(required),
                ),
                check(
                    "calculation reduces to one coefficient",
                    calc.get("green_schwarz_preservation_gate_closed") is True
                    and calc.get("rplus_and_dH_have_alpha1_support_only") is True
                    and calc.get("alpha2_alpha3_visible_curvature_forced_zero_in_invariant_basis")
                    is True
                    and calc.get("visible_gauge_curvature_reduced_to_one_alpha1_coefficient")
                    is True
                    and calc.get("visible_curvature_packet_validator_can_pass_now") is False,
                    str(calc),
                ),
                check(
                    "closes requirement only",
                    closes.get("coefficient_level_visible_TrF_requirement") is True
                    and closes.get("single_missing_alpha1_visible_gauge_row_identified") is True
                    and still_open.get("selected_visible_bundle_or_HYM_source_for_required_TrF_row")
                    is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                check(
                    "guardrails no overclaim",
                    guardrails.get("claims_required_row_is_selected_visible_bundle") is False
                    and guardrails.get("claims_visible_green_schwarz_verified") is False
                    and guardrails.get("claims_selected_D_E_dotD_constructed") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                check(
                    "paper records equation",
                    "Tr F_visible^2 = Tr R_+^2 - dH" in paper
                    and "8*r3^2/(r1^2*r2^2) + 4*r3^2" in paper
                    and "not enough" in paper,
                    "paper requirement present",
                ),
            ]
        )

    print("Time-oriented m=1 visible Green-Schwarz requirement audit")
    print("=========================================================")
    failures = 0
    for name, ok, detail in checks:
        print(f"{name:52} {'PASS' if ok else 'FAIL'}  {detail}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
