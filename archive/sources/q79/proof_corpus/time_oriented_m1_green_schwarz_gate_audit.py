"""Audit the time-oriented m=1 Green-Schwarz gate."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "analyze_time_oriented_m1_green_schwarz_gate.py"
VALIDATOR = REPO / "scripts" / "validate_time_oriented_m1_visible_green_schwarz_curvature.py"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_green_schwarz_gate.candidate.json"
CERT = REPO / "certificates" / "time_oriented_m1_green_schwarz_gate_certificate.json"
TEMPLATE = REPO / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature.template.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_Green_Schwarz_Gate_v1.md"


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


def write_packet(path: Path, *, residual_zero: bool) -> None:
    residual = [0, 0] if residual_zero else [1, 0]
    dH = ["-4", "0"] if residual_zero else ["-3", "0"]
    packet = {
        "schema": "TimeOrientedM1VisibleGreenSchwarzCurvature.v1",
        "status": "SELECTED_VISIBLE_GREEN_SCHWARZ_CURVATURE_VERIFIED",
        "selected_by_mtt": True,
        "same_branch_as_q79_m1": True,
        "flat_gerbe_certificate": "time_oriented_m1_flat_gerbe_promotion_certificate.json",
        "green_schwarz_gate_certificate": "time_oriented_m1_green_schwarz_gate_certificate.json",
        "selected_visible_source_certificate": "unit_test_selected_visible_source.json",
        "curvature_basis": ["alpha_1", "alpha_2"],
        "alpha_prime_over_4_absorbed": True,
        "flat_m1_torsion_curvature_zero": True,
        "dH_coefficients": dH,
        "tr_R_plus_squared_coefficients": ["8", "0"],
        "tr_F_visible_squared_coefficients": ["12", "0"],
        "bianchi_residual_coefficients": residual,
        "bianchi_residual_zero": residual_zero,
        "route_c_or_hym_source_certificate": "unit_test_selected_visible_source.json",
        "projector_retention_certificate": "unit_test_projector_retention.json",
        "uses_observed_flavor_data": False,
        "uses_benchmark_flavor_entries": False,
    }
    path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    proc = run_script()
    checks: list[tuple[str, bool, str]] = [
        check("constructor exits 0", proc.returncode == 0, proc.stdout[:1000]),
        check("candidate exists", CANDIDATE.exists(), str(CANDIDATE)),
        check("certificate exists", CERT.exists(), str(CERT)),
        check("template exists", TEMPLATE.exists(), str(TEMPLATE)),
        check("validator exists", VALIDATOR.exists(), str(VALIDATOR)),
        check("paper exists", PAPER.exists(), str(PAPER)),
    ]

    if CANDIDATE.exists() and CERT.exists() and TEMPLATE.exists() and PAPER.exists():
        candidate = load_json(CANDIDATE)
        cert = load_json(CERT)
        calc = cert.get("calculation_results", {})
        flat = cert.get("flat_torsion_curvature_effect", {})
        charge = cert.get("charge_sector_preservation", {})
        visible = cert.get("visible_operator_source_status", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        paper = PAPER.read_text(encoding="utf-8")
        template_proc = run_validator(TEMPLATE)

        checks.extend(
            [
                check(
                    "status preservation closed visible open",
                    cert.get("status")
                    == "TIME_ORIENTED_M1_GREEN_SCHWARZ_GATE_PRESERVATION_CLOSED_VISIBLE_SOURCE_OPEN"
                    and candidate.get("status") == cert.get("status"),
                    str(cert.get("status")),
                ),
                check(
                    "flat torsion curvature invisible",
                    flat.get("curvature_H_form") == "0"
                    and flat.get("delta_dH_from_m1_flat_torsion") == 0
                    and flat.get("changes_green_schwarz_curvature_equation") is False
                    and flat.get("can_cancel_missing_visible_curvature_residual") is False,
                    str(flat),
                ),
                check(
                    "closed charge sector preserved",
                    charge.get("z7_charge_sector_status") == "CLOSED_CHARGE_SECTOR"
                    and charge.get("charge_sector_green_schwarz_bianchi_verified") is True
                    and charge.get("preserved_under_flat_m1_torsion") is True,
                    str(charge),
                ),
                check(
                    "visible operator source remains open",
                    visible.get("selected_hym_operator_source_verified") is False
                    and visible.get("route_c_q79_branch_available") is True
                    and visible.get("selected_D_E_dotD_open") is True,
                    str(visible),
                ),
                check(
                    "calculation separates preservation from visible closure",
                    calc.get("flat_m1_adds_no_deRham_H_flux") is True
                    and calc.get("charge_sector_bianchi_preserved") is True
                    and calc.get("visible_green_schwarz_verified") is False
                    and calc.get("green_schwarz_not_a_torsion_label_selector") is True,
                    str(calc),
                ),
                check(
                    "what closes and remains",
                    closes.get("m1_flat_torsion_preserves_GS_curvature_bianchi") is True
                    and closes.get("no_hidden_GS_repair_from_flat_torsion") is True
                    and still_open.get("selected_visible_gauge_bundle_curvature_TrFvis_squared")
                    is True
                    and still_open.get("selected_route_c_or_hym_operator_source") is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                check(
                    "template is open",
                    template_proc.returncode == 2
                    and "packet is OPEN" in template_proc.stdout,
                    template_proc.stdout.strip(),
                ),
                check(
                    "guardrails no overclaim",
                    guardrails.get("claims_visible_green_schwarz_verified") is False
                    and guardrails.get("claims_selected_visible_bundle_constructed") is False
                    and guardrails.get("claims_selected_D_E_dotD_constructed") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                check(
                    "paper records residual formula",
                    "residual = dH - (Tr R_+^2 - Tr F_visible^2)" in paper
                    and "not a curvature dial" in paper,
                    "paper formula present",
                ),
            ]
        )

    if VALIDATOR.exists():
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            passing = tmpdir / "passing_visible_gs.json"
            failing = tmpdir / "failing_visible_gs.json"
            write_packet(passing, residual_zero=True)
            write_packet(failing, residual_zero=False)
            pass_proc = run_validator(passing)
            fail_proc = run_validator(failing)
            checks.extend(
                [
                    check(
                        "validator accepts exact zero residual fixture",
                        pass_proc.returncode == 0
                        and "visible Green-Schwarz curvature PASS" in pass_proc.stdout,
                        pass_proc.stdout.strip(),
                    ),
                    check(
                        "validator rejects nonzero residual fixture",
                        fail_proc.returncode == 1
                        and "Bianchi residual is nonzero" in fail_proc.stdout,
                        fail_proc.stdout.strip(),
                    ),
                ]
            )

    print("Time-oriented m=1 Green-Schwarz gate audit")
    print("==========================================")
    failures = 0
    for name, ok, detail in checks:
        print(f"{name:52} {'PASS' if ok else 'FAIL'}  {detail}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
