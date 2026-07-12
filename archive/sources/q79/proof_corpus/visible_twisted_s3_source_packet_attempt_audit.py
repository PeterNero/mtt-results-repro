"""Audit the selected S3 twisted D7 source-packet attempt."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "attempt_visible_twisted_s3_source_packet.py"
VALIDATOR = REPO / "scripts" / "validate_visible_twisted_s3_source_packet.py"
TEMPLATE = REPO / "certificates" / "visible_twisted_s3_source_packet.template.json"
ATTEMPT = REPO / "certificates" / "visible_twisted_s3_source_packet.attempt.json"
CANDIDATE = REPO / "candidate_data" / "visible_twisted_s3_source_packet_attempt.candidate.json"
CERT = REPO / "certificates" / "visible_twisted_s3_source_packet_attempt_certificate.json"
PAPER = ROOT / "Visible_Twisted_S3_Source_Packet_Attempt_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def run_constructor() -> subprocess.CompletedProcess[str]:
    return run([sys.executable, str(SCRIPT)])


def run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return run([sys.executable, str(VALIDATOR), str(path)])


def selected_fixture_from_attempt(path: Path, *, stack: str = "S3", selected: bool = True) -> None:
    packet = copy.deepcopy(load_json(ATTEMPT))
    packet["status"] = "SELECTED_VISIBLE_TWISTED_S3_SOURCE_VERIFIED"
    packet["selected_stack"] = stack
    packet["worldvolume_evidence"]["twisted_projective_D7_stack"] = stack
    packet["source_evidence"].update(
        {
            "source_selected_by_mtt": selected,
            "fixed_differential_cohomology_class": selected,
            "geometric_Deligne_Cech_or_worldvolume_flux_source_constructed": selected,
            "physical_worldvolume_flux_or_twisted_CP_source_constructed": selected,
            "map_to_central_cocycle_verified": selected,
            "source_certificate": "unit_test_selected_s3_source_certificate.json",
        }
    )
    packet["consistency_evidence"].update(
        {
            "green_schwarz_bianchi_verified_for_S3_source": selected,
            "freed_witten_verified_for_S3_source": selected,
            "twisted_projector_retention_verified": selected,
        }
    )
    write_json(path, packet)


def main() -> int:
    proc = run_constructor()
    checks: list[Gate] = [
        Gate("constructor exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("validator exists", "PASS" if VALIDATOR.exists() else "FAIL", str(VALIDATOR)),
        Gate("template exists", "PASS" if TEMPLATE.exists() else "FAIL", str(TEMPLATE)),
        Gate("attempt exists", "PASS" if ATTEMPT.exists() else "FAIL", str(ATTEMPT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
    ]

    cert = load_json(CERT)
    attempt = load_json(ATTEMPT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)
    template_proc = run_validator(TEMPLATE) if TEMPLATE.exists() else None
    attempt_proc = run_validator(ATTEMPT) if ATTEMPT.exists() else None

    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    s3_attempt = cert.get("s3_source_attempt", {})

    checks.extend(
        [
            Gate(
                "status blocked selected S3 source",
                "PASS"
                if cert.get("status")
                == "VISIBLE_TWISTED_S3_SOURCE_PACKET_ATTEMPT_BLOCKED_SELECTED_SOURCE_OPEN"
                else "FAIL",
                str(cert.get("status")),
            ),
            Gate(
                "selector closed but source open",
                "PASS"
                if cert.get("selected_stack", {}).get("stack") == "S3"
                and cert.get("selected_stack", {}).get("selected_stack_by_mtt") is True
                and cert.get("selected_stack", {}).get("selected_source_by_mtt") is False
                else "FAIL",
                str(cert.get("selected_stack", {})),
            ),
            Gate(
                "template refused as open",
                "PASS"
                if template_proc is not None
                and template_proc.returncode == 2
                and "packet is OPEN" in template_proc.stdout
                else "FAIL",
                "" if template_proc is None else template_proc.stdout.strip(),
            ),
            Gate(
                "attempt refused by validator",
                "PASS"
                if attempt_proc is not None
                and attempt_proc.returncode == 1
                and "source_evidence.source_selected_by_mtt must be true" in attempt_proc.stdout
                and "freed_witten_verified_for_S3_source" in attempt_proc.stdout
                and "twisted_projector_retention_verified" in attempt_proc.stdout
                else "FAIL",
                "" if attempt_proc is None else attempt_proc.stdout.strip(),
            ),
            Gate(
                "S3 assignments collected",
                "PASS"
                if s3_attempt.get("active_pair") == ["T1", "T2"]
                and len(s3_attempt.get("supporting_s3_assignments", [])) == 2
                and s3_attempt.get("finite_projective_CP_module_matches_m1_twist") is True
                else "FAIL",
                str(s3_attempt),
            ),
            Gate(
                "calculation closes gate only",
                "PASS"
                if calc.get("source_packet_schema_and_validator_created") is True
                and calc.get("attempt_refused_until_selected_source") is True
                and calc.get("minimal_equivariant_stack_S3_closed") is True
                and calc.get("selected_S3_source_constructed") is False
                and calc.get("S3_projector_retention_closed") is False
                else "FAIL",
                str(calc),
            ),
            Gate(
                "what closes and remains",
                "PASS"
                if closes.get("executable_selected_S3_source_gate") is True
                and closes.get("minimal_equivariant_twisted_D7_stack") == "S3"
                and still_open.get("selected_S3_Deligne_Cech_or_worldvolume_flux_source")
                is True
                and still_open.get("S3_twisted_projector_retention") is True
                else "FAIL",
                str({"closes": closes, "still_open": still_open}),
            ),
            Gate(
                "guardrails",
                "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
                str(guardrails),
            ),
            Gate(
                "attempt packet exact branch",
                "PASS"
                if attempt.get("branch", {}).get("q") == 79
                and attempt.get("branch", {}).get("orientation") == "F"
                and attempt.get("branch", {}).get("torsion_label_m") == 1
                and attempt.get("selected_stack") == "S3"
                else "FAIL",
                str(attempt.get("branch", {})),
            ),
            Gate(
                "candidate mirrors certificate",
                "PASS"
                if candidate.get("status") == cert.get("status")
                and candidate.get("validator_result") == cert.get("validator_result")
                else "FAIL",
                str(CANDIDATE),
            ),
            Gate(
                "paper records sharp blocker",
                "PASS"
                if all(
                    needle in paper
                    for needle in [
                        "selected S3 source packet",
                        "selector-level result",
                        "not yet constructed",
                        "would make the packet pass",
                    ]
                )
                else "FAIL",
                str(PAPER),
            ),
        ]
    )

    if VALIDATOR.exists() and ATTEMPT.exists():
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            passing = tmpdir / "passing_s3_source.json"
            bad_stack = tmpdir / "bad_stack_source.json"
            missing_source = tmpdir / "missing_source.json"
            selected_fixture_from_attempt(passing)
            selected_fixture_from_attempt(bad_stack, stack="S2")
            selected_fixture_from_attempt(missing_source, selected=False)
            pass_proc = run_validator(passing)
            bad_stack_proc = run_validator(bad_stack)
            missing_source_proc = run_validator(missing_source)
            checks.extend(
                [
                    Gate(
                        "validator accepts selected fixture",
                        "PASS"
                        if pass_proc.returncode == 0
                        and "visible twisted S3 source PASS" in pass_proc.stdout
                        else "FAIL",
                        pass_proc.stdout.strip(),
                    ),
                    Gate(
                        "validator rejects wrong stack",
                        "PASS"
                        if bad_stack_proc.returncode == 1
                        and "selected_stack must be S3" in bad_stack_proc.stdout
                        else "FAIL",
                        bad_stack_proc.stdout.strip(),
                    ),
                    Gate(
                        "validator rejects missing source",
                        "PASS"
                        if missing_source_proc.returncode == 1
                        and "source_evidence.source_selected_by_mtt must be true"
                        in missing_source_proc.stdout
                        else "FAIL",
                        missing_source_proc.stdout.strip(),
                    ),
                ]
            )

    print("Visible twisted S3 source-packet attempt audit")
    print("==============================================")
    width = max(len(gate.label) for gate in checks)
    status_width = max(len(gate.status) for gate in checks)
    failures: list[Gate] = []
    for gate in checks:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
