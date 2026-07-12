"""Audit the visible complex-worldvolume spinC/W3 gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "prove_visible_complex_worldvolume_spinc_gate.py"
CANDIDATE = REPO / "candidate_data" / "visible_complex_worldvolume_spinc_gate.candidate.json"
CERT = REPO / "certificates" / "visible_complex_worldvolume_spinc_gate_certificate.json"
PAPER = REPO / "proof_corpus" / "Visible_Complex_Worldvolume_SpinC_Gate_v1.md"


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
        candidate = load_json(CANDIDATE)
        cert = load_json(CERT)
        calc = cert.get("calculation_results", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        reason = cert.get("mathematical_reason", {})
        world = cert.get("worldvolume_class", {})
        paper = PAPER.read_text(encoding="utf-8")

        divisors = world.get("gauge_stack_divisors", [])
        curves = world.get("matter_intersections", [])
        checks.extend(
            [
                check(
                    "status spinC closed DD open",
                    cert.get("status")
                    == "VISIBLE_COMPLEX_WORLDVOLUME_SPINC_W3_CLOSED_DD_IMAGES_OPEN"
                    and candidate.get("status") == cert.get("status"),
                    str(cert.get("status")),
                ),
                check(
                    "source corpus names complex class",
                    calc.get("visible_complex_divisor_source_present") is True
                    and calc.get("visible_complex_matter_curve_source_present") is True,
                    str(calc),
                ),
                check(
                    "divisors and curves W3 zero",
                    len(divisors) == 3
                    and len(curves) == 3
                    and all(item.get("spinC_verified") is True for item in divisors + curves)
                    and all(item.get("W3_zero") is True for item in divisors + curves),
                    str(world),
                ),
                check(
                    "mathematical reason recorded",
                    reason.get("complex_submanifold_spinC") is True
                    and "c1 mod 2" in reason.get("w2_mod2_c1", "")
                    and "W3=0" in reason.get("W3_zero_reason", ""),
                    str(reason),
                ),
                check(
                    "what closes and DD remains",
                    closes.get("W3_zero_for_D7_divisor_worldvolume_class") is True
                    and closes.get("spinC_for_pairwise_matter_curve_class") is True
                    and still_open.get("active_F3_squared_images_for_S1_S2_S3_and_Cij")
                    is True
                    and still_open.get("DD_B_restriction_for_complete_visible_worldvolume_packet")
                    is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                check(
                    "guardrails prevent overclaim",
                    guardrails.get("claims_complete_Freed_Witten") is False
                    and guardrails.get("claims_active_DD_restrictions") is False
                    and guardrails.get("claims_selected_visible_operator_source") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                check(
                    "paper records new frontier",
                    "W3/spinC for the visible complex-worldvolume class" in paper
                    and "active F_3^2 images" in paper
                    and "complete Freed-Witten verification" in paper,
                    "paper scope present",
                ),
            ]
        )

    print("Visible complex-worldvolume spinC gate audit")
    print("============================================")
    failures = 0
    for name, ok, detail in checks:
        print(f"{name:55} {'PASS' if ok else 'FAIL'}  {detail}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
