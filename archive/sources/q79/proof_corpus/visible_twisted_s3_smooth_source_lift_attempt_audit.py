"""Audit the smooth selected S3 source-lift attempt."""

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
SCRIPT = REPO / "scripts" / "attempt_visible_twisted_s3_smooth_source_lift.py"
VALIDATOR = REPO / "scripts" / "validate_visible_twisted_s3_smooth_source_lift.py"
TEMPLATE = REPO / "certificates" / "visible_twisted_s3_smooth_source_lift.template.json"
ATTEMPT = REPO / "certificates" / "visible_twisted_s3_smooth_source_lift.attempt.json"
CANDIDATE = REPO / "candidate_data" / "visible_twisted_s3_smooth_source_lift_attempt.candidate.json"
CERT = REPO / "certificates" / "visible_twisted_s3_smooth_source_lift_attempt_certificate.json"
PAPER = ROOT / "Visible_Twisted_S3_Smooth_Source_Lift_Attempt_v1.md"


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
    packet["status"] = "SELECTED_VISIBLE_TWISTED_S3_SMOOTH_SOURCE_LIFT_VERIFIED"
    packet["smooth_source"].update(
        {
            "source_selected_by_mtt": selected,
            "selected_cover_or_scaffold_verified": selected,
            "good_cover_data_supplied": selected,
            "deligne_cech_representative_constructed": selected,
            "fixed_differential_cohomology_class": selected,
            "restricts_to_selected_S3_worldvolume": selected,
            "map_to_qutrit_central_cocycle_verified": selected,
            "smooth_twisted_CP_or_worldvolume_flux_constructed": selected,
            "source_certificate": "unit_test_selected_smooth_s3_source.json",
        }
    )
    packet["consistency"].update(
        {
            "green_schwarz_bianchi_verified_for_smooth_S3_source": selected,
            "freed_witten_verified_for_smooth_S3_source": selected,
            "twisted_projector_retention_verified": selected,
            "block_factorized_family_higgs_projectors_retained": selected,
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

    calc = cert.get("calculation_results", {})
    lift = cert.get("smooth_lift_attempt", {})
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
            "status blocked selected cover/projectors",
            "PASS"
            if cert.get("status")
            == "VISIBLE_TWISTED_S3_SMOOTH_SOURCE_LIFT_ATTEMPT_BLOCKED_SELECTED_COVER_PROJECTORS_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "template refused as open",
            "PASS"
            if template_proc.returncode == 2
            and "smooth source lift packet is OPEN" in template_proc.stdout
            else "FAIL",
            template_proc.stdout.strip(),
        ),
        Gate(
            "attempt refused by validator",
            "PASS"
            if attempt_proc.returncode == 1
            and "smooth_source.source_selected_by_mtt must be true" in attempt_proc.stdout
            and "selected_cover_or_scaffold_verified" in attempt_proc.stdout
            and "twisted_projector_retention_verified" in attempt_proc.stdout
            else "FAIL",
            attempt_proc.stdout.strip(),
        ),
        Gate(
            "conditional smooth model available",
            "PASS"
            if lift.get("conditional_flat_gerbe_representative_exists") is True
            and lift.get("finite_S3_CP_cancellation_closed") is True
            and lift.get("standard_deck_scaffold_valid") is True
            and lift.get("standard_deck_scaffold_selected") is False
            else "FAIL",
            str(lift),
        ),
        Gate(
            "calculation closes gate not source",
            "PASS"
            if calc.get("smooth_source_lift_schema_and_validator_created") is True
            and calc.get("conditional_smooth_flat_S3_model_available") is True
            and calc.get("selected_smooth_S3_source_constructed") is False
            and calc.get("smooth_S3_projector_retention_closed") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "what closes and remains",
            "PASS"
            if closes.get("executable_smooth_S3_source_lift_gate") is True
            and closes.get("conditional_flat_Deligne_Cech_model_attached_to_S3_finite_CP")
            is True
            and still_open.get("MTT_selected_cover_or_scaffold") is True
            and still_open.get("smooth_S3_twisted_projector_retention") is True
            else "FAIL",
            str({"closes": closes, "still_open": still_open}),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
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
                    "conditional smooth-source model",
                    "not selected yet",
                    "selected cover or scaffold",
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
            passing = tmpdir / "passing_smooth_s3_source.json"
            missing = tmpdir / "missing_smooth_s3_source.json"
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
                        and "smooth source lift PASS" in pass_proc.stdout
                        else "FAIL",
                        pass_proc.stdout.strip(),
                    ),
                    Gate(
                        "validator rejects missing selected fixture",
                        "PASS"
                        if missing_proc.returncode == 1
                        and "smooth_source.source_selected_by_mtt must be true"
                        in missing_proc.stdout
                        else "FAIL",
                        missing_proc.stdout.strip(),
                    ),
                ]
            )

    print("Visible twisted S3 smooth source-lift attempt audit")
    print("===================================================")
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
