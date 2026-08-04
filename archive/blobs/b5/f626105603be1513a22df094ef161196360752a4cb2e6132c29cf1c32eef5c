"""Audit the selected S3 class/restriction packet attempt."""

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
SCRIPT = REPO / "scripts" / "attempt_visible_twisted_s3_class_restriction_packet.py"
VALIDATOR = REPO / "scripts" / "validate_visible_twisted_s3_class_restriction_packet.py"
TEMPLATE = REPO / "certificates" / "visible_twisted_s3_class_restriction_packet.template.json"
ATTEMPT = REPO / "certificates" / "visible_twisted_s3_class_restriction_packet.attempt.json"
CANDIDATE = REPO / "candidate_data" / "visible_twisted_s3_class_restriction_packet_attempt.candidate.json"
CERT = REPO / "certificates" / "visible_twisted_s3_class_restriction_packet_attempt_certificate.json"
PAPER = ROOT / "Visible_Twisted_S3_Class_Restriction_Packet_Attempt_v1.md"


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


def selected_fixture_from_attempt(path: Path, *, selected: bool = True) -> None:
    packet = copy.deepcopy(load_json(ATTEMPT))
    packet["status"] = "SELECTED_VISIBLE_TWISTED_S3_CLASS_RESTRICTION_VERIFIED"
    packet["class_data"].update(
        {
            "fixed_smooth_flat_gerbe_class": selected,
            "same_class_as_finite_m1_deck_cocycle": selected,
            "map_to_qutrit_central_cocycle_verified": selected,
            "differential_cohomology_class_certificate": "unit_test_selected_s3_class.json",
        }
    )
    packet["s3_restriction"].update(
        {
            "S3_pullback_table_supplied": selected,
            "smooth_Freed_Witten_cancellation_verified": selected,
        }
    )
    packet["projector_retention"].update(
        {
            "projector_retention_proved_for_selected_source": selected,
            "family_higgs_blocks_retained": selected,
        }
    )
    write_json(path, packet)


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    attempt = load_json(ATTEMPT)
    paper = read(PAPER)
    template_proc = run([sys.executable, str(VALIDATOR), str(TEMPLATE)])
    attempt_proc = run([sys.executable, str(VALIDATOR), str(ATTEMPT)])

    summary = cert.get("attempt_summary", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("constructor exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("validator exists", "PASS" if VALIDATOR.exists() else "FAIL", str(VALIDATOR)),
        Gate("template exists", "PASS" if TEMPLATE.exists() else "FAIL", str(TEMPLATE)),
        Gate("attempt exists", "PASS" if ATTEMPT.exists() else "FAIL", str(ATTEMPT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status blocked smooth class projectors",
            "PASS"
            if cert.get("status")
            == "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_PACKET_ATTEMPT_BLOCKED_SMOOTH_CLASS_PROJECTORS_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "template refused as open",
            "PASS"
            if template_proc.returncode == 2
            and "class/restriction packet is OPEN" in template_proc.stdout
            else "FAIL",
            template_proc.stdout.strip(),
        ),
        Gate(
            "attempt refused by validator",
            "PASS"
            if attempt_proc.returncode == 1
            and "class_data.fixed_smooth_flat_gerbe_class must be true"
            in attempt_proc.stdout
            and "s3_restriction.S3_pullback_table_supplied must be true"
            in attempt_proc.stdout
            and "projector_retention.projector_retention_proved_for_selected_source"
            in attempt_proc.stdout
            else "FAIL",
            attempt_proc.stdout.strip(),
        ),
        Gate(
            "finite inputs carried forward",
            "PASS"
            if summary.get("cover_choice_auxiliary_closed") is True
            and summary.get("finite_S3_CP_cancellation_closed") is True
            and summary.get("S3_active_image_rank_over_F3") == 2
            and summary.get("finite_twisted_DD_cancellation_zero") is True
            and summary.get("W3_spinC_zero") is True
            else "FAIL",
            str(summary),
        ),
        Gate(
            "smooth class still open",
            "PASS"
            if summary.get("fixed_smooth_flat_gerbe_class") is False
            and summary.get("S3_pullback_table_supplied") is False
            and summary.get("smooth_Freed_Witten_cancellation_verified") is False
            and summary.get("projector_retention_proved") is False
            else "FAIL",
            str(summary),
        ),
        Gate(
            "calculation closes gate not source",
            "PASS"
            if calc.get("class_restriction_schema_and_validator_created") is True
            and calc.get("attempt_refused_until_smooth_class_and_projectors") is True
            and calc.get("selected_smooth_S3_class_restriction_packet_constructed") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "what closes and remains",
            "PASS"
            if closes.get("executable_selected_S3_class_restriction_gate") is True
            and closes.get("finite_S3_CP_and_W3_inputs_inserted_into_gate") is True
            and still_open.get("fixed_smooth_flat_gerbe_class") is True
            and still_open.get("block_sector_projector_retention") is True
            else "FAIL",
            str({"closes": closes, "still_open": still_open}),
        ),
        Gate("guardrails", "PASS" if all(value is False for value in guardrails.values()) else "FAIL", str(guardrails)),
        Gate(
            "attempt exact branch",
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
            "paper records precise blocker",
            "PASS"
            if all(
                needle in paper
                for needle in [
                    "selected S3 class/restriction packet",
                    "not selected yet",
                    "smooth Freed-Witten cancellation",
                    "projector retention remains open",
                ]
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    if VALIDATOR.exists() and ATTEMPT.exists():
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            passing = tmpdir / "passing_s3_class_restriction.json"
            missing = tmpdir / "missing_s3_class_restriction.json"
            selected_fixture_from_attempt(passing, selected=True)
            selected_fixture_from_attempt(missing, selected=False)
            pass_proc = run([sys.executable, str(VALIDATOR), str(passing)])
            missing_proc = run([sys.executable, str(VALIDATOR), str(missing)])
            gates.extend(
                [
                    Gate(
                        "validator accepts selected fixture",
                        "PASS"
                        if pass_proc.returncode == 0
                        and "class/restriction PASS" in pass_proc.stdout
                        else "FAIL",
                        pass_proc.stdout.strip(),
                    ),
                    Gate(
                        "validator rejects missing selected fixture",
                        "PASS"
                        if missing_proc.returncode == 1
                        and "class_data.fixed_smooth_flat_gerbe_class must be true"
                        in missing_proc.stdout
                        else "FAIL",
                        missing_proc.stdout.strip(),
                    ),
                ]
            )

    print("Visible twisted S3 class/restriction packet attempt audit")
    print("=========================================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
