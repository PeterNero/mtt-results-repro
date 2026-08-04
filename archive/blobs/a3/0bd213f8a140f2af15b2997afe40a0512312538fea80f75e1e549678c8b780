"""Audit the time-oriented m=1 Freed-Witten cycle gate."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "analyze_time_oriented_m1_freed_witten_cycle_gate.py"
VALIDATOR = REPO / "scripts" / "validate_time_oriented_m1_selected_cycle_restrictions.py"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_freed_witten_cycle_gate.candidate.json"
CERT = REPO / "certificates" / "time_oriented_m1_freed_witten_cycle_gate_certificate.json"
TEMPLATE = REPO / "certificates" / "time_oriented_m1_selected_cycle_restrictions.template.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_Freed_Witten_Cycle_Gate_v1.md"


@dataclass
class Gate:
    name: str
    passed: bool
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_constructor() -> subprocess.CompletedProcess[str]:
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


def write_temp_packet(path: Path, cycles: list[dict[str, Any]]) -> None:
    packet = {
        "schema": "TimeOrientedM1SelectedCycleRestrictions.v1",
        "status": "SELECTED_CYCLES_VERIFIED",
        "selected_by_mtt": True,
        "flat_gerbe_certificate": "time_oriented_m1_flat_gerbe_promotion_certificate.json",
        "source_certificate": "unit-test-fixture",
        "uses_observed_flavor_data": False,
        "uses_benchmark_flavor_entries": False,
        "cycles": cycles,
    }
    path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    proc = run_constructor()
    gates: list[Gate] = [
        Gate("constructor exits 0", proc.returncode == 0, proc.stdout[:1000]),
        Gate("candidate exists", CANDIDATE.exists(), str(CANDIDATE)),
        Gate("certificate exists", CERT.exists(), str(CERT)),
        Gate("template exists", TEMPLATE.exists(), str(TEMPLATE)),
        Gate("validator exists", VALIDATOR.exists(), str(VALIDATOR)),
        Gate("paper exists", PAPER.exists(), str(PAPER)),
    ]

    if CANDIDATE.exists() and CERT.exists() and TEMPLATE.exists() and PAPER.exists():
        candidate = load_json(CANDIDATE)
        cert = load_json(CERT)
        theorem = cert.get("finite_restriction_theorem", {})
        distribution = cert.get("subgroup_distribution", {})
        calc = cert.get("calculation_results", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        paper = PAPER.read_text(encoding="utf-8")
        template_proc = run_validator(TEMPLATE)

        gates.extend(
            [
                Gate(
                    "status formulated cycles open",
                    cert.get("status")
                    == "TIME_ORIENTED_M1_FREED_WITTEN_CYCLE_GATE_FORMULATED_SELECTED_CYCLES_OPEN",
                    cert.get("status", ""),
                ),
                Gate(
                    "finite theorem rank criterion",
                    theorem.get("DD_restriction_zero_iff")
                    == "rank(image(pi1(Y)->F_3^2)) <= 1"
                    and theorem.get("commutator_form")
                    == "omega((a,b),(c,d)) = a*d - b*c mod 3",
                    str(theorem),
                ),
                Gate(
                    "subgroup distribution exact",
                    distribution.get("zero_subgroup_count") == 1
                    and distribution.get("rank_one_line_count") == 4
                    and distribution.get("rank_two_subgroup_count") == 1
                    and distribution.get("all_rank_one_restrictions_DD_zero") is True
                    and distribution.get("all_rank_two_pair_witnesses_DD_nonzero") is True,
                    str(distribution),
                ),
                Gate(
                    "samples include obstruction",
                    any(
                        sample.get("id") == "full_active_g1_g2_cycle"
                        and sample.get("DD_restriction_zero") is False
                        for sample in candidate.get("sample_cycle_restrictions", [])
                    ),
                    str(candidate.get("sample_cycle_restrictions", [])),
                ),
                Gate(
                    "template is open",
                    template_proc.returncode == 2
                    and "OPEN" in template_proc.stdout,
                    template_proc.stdout.strip(),
                ),
                Gate(
                    "calculation closes finite gate only",
                    calc.get("finite_DD_restriction_decision_procedure_closed") is True
                    and calc.get("selected_cycles_supplied") is False
                    and calc.get("Freed_Witten_verified") is False,
                    str(calc),
                ),
                Gate(
                    "what closes and what remains",
                    closes.get("DD_B_restriction_calculator_for_m1_flat_gerbe") is True
                    and closes.get("future_selected_cycle_packet_schema_and_validator") is True
                    and still_open.get("selected_cycle_or_brane_list") is True
                    and still_open.get("W3_zero_or_spinC_certificate_per_cycle") is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                Gate(
                    "guardrails no overclaim",
                    guardrails.get("claims_selected_cycles_supplied") is False
                    and guardrails.get("claims_Freed_Witten_verified") is False
                    and guardrails.get("claims_selected_D_E_dotD_constructed") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                Gate(
                    "paper records filled packet requirement",
                    "cycle id" in paper
                    and "image in F_3^2" in paper
                    and "W3(Y)=0 or spinC certificate" in paper,
                    "packet requirement text present",
                ),
            ]
        )

    if VALIDATOR.exists():
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            passing = tmpdir / "passing_cycles.json"
            write_temp_packet(
                passing,
                [
                    {
                        "id": "fixture_kernel",
                        "selected_by_mtt": True,
                        "pi1_image_generators_F3_2": [[0, 0]],
                        "dd_restriction_zero_claim": True,
                        "W3_zero": True,
                        "spinC_verified": False,
                    },
                    {
                        "id": "fixture_g1_line",
                        "selected_by_mtt": True,
                        "pi1_image_generators_F3_2": [[1, 0]],
                        "dd_restriction_zero_claim": True,
                        "W3_zero": False,
                        "spinC_verified": True,
                    },
                    {
                        "id": "fixture_diagonal_line",
                        "selected_by_mtt": True,
                        "pi1_image_generators_F3_2": [[1, 1]],
                        "dd_restriction_zero_claim": True,
                        "W3_zero": True,
                        "spinC_verified": False,
                    },
                ],
            )
            passing_proc = run_validator(passing)
            failing = tmpdir / "failing_cycles.json"
            write_temp_packet(
                failing,
                [
                    {
                        "id": "fixture_full_active",
                        "selected_by_mtt": True,
                        "pi1_image_generators_F3_2": [[1, 0], [0, 1]],
                        "dd_restriction_zero_claim": True,
                        "W3_zero": True,
                        "spinC_verified": False,
                    }
                ],
            )
            failing_proc = run_validator(failing)
            gates.extend(
                [
                    Gate(
                        "validator accepts isotropic selected fixtures",
                        passing_proc.returncode == 0
                        and "selected-cycle restriction PASS" in passing_proc.stdout,
                        passing_proc.stdout.strip(),
                    ),
                    Gate(
                        "validator rejects full active image",
                        failing_proc.returncode == 1
                        and "DD(B)|Y is nonzero" in failing_proc.stdout,
                        failing_proc.stdout.strip(),
                    ),
                ]
            )

    for gate in gates:
        status = "PASS" if gate.passed else "FAIL"
        print(f"[{status}] {gate.name}: {gate.detail}")

    return 0 if all(gate.passed for gate in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
