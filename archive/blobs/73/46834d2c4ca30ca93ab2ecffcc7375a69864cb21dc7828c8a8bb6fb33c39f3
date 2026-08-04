"""Audit the Deligne/Cech cover-gauge reduction for the Iwasawa S3 route."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "prove_iwasawa_deligne_cover_gauge_reduction.py"
CANDIDATE = REPO / "candidate_data" / "iwasawa_deligne_cover_gauge_reduction.candidate.json"
CERT = REPO / "certificates" / "iwasawa_deligne_cover_gauge_reduction_certificate.json"
PAPER = REPO / "proof_corpus" / "Iwasawa_Deligne_Cover_Gauge_Reduction_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run_constructor() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    proc = run_constructor()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    reduction = cert.get("mathematical_reduction", {})
    inputs = cert.get("inputs_checked", {})
    guardrails = cert.get("guardrails", {})

    gates = [
        Gate("constructor exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status closed class restriction open",
            "PASS"
            if cert.get("status")
            == "IWASAWA_DELIGNE_COVER_GAUGE_REDUCTION_CLOSED_CLASS_RESTRICTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies checked",
            "PASS" if all(value is not None for value in cert.get("dependency_statuses", {}).values()) else "FAIL",
            str(cert.get("dependency_statuses", {})),
        ),
        Gate(
            "inputs support reduction",
            "PASS"
            if inputs.get("standard_deck_scaffold_valid") is True
            and inputs.get("finite_q79_F_m1_class_fixed") is True
            and inputs.get("conditional_flat_Deligne_model_exists") is True
            and inputs.get("smooth_lift_gate_already_waits_for_source") is True
            else "FAIL",
            str(inputs),
        ),
        Gate(
            "cover role is auxiliary",
            "PASS"
            if reduction.get("good_cover_role") == "auxiliary representative for Cech/Deligne data"
            and reduction.get("curvature_H_form") == "0"
            and reduction.get("torsion_order") == 3
            else "FAIL",
            str(reduction),
        ),
        Gate(
            "cover blocker reduced",
            "PASS"
            if closes.get("particular_good_cover_need_not_be_MTT_selected") is True
            and closes.get("cover_refinement_invariance_for_Deligne_Cech_representatives") is True
            and closes.get("selected_cover_blocker_reduced_to_selected_class_and_restriction")
            is True
            and closes.get("good_cover_is_execution_scaffold_not_physical_knob") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "source theorem still open",
            "PASS"
            if still_open.get("fixed_smooth_S3_differential_cohomology_class") is True
            and still_open.get("restriction_of_the_flat_class_to_selected_S3_worldvolume")
            is True
            and still_open.get("smooth_S3_Freed_Witten_cancellation") is True
            and still_open.get("twisted_projector_retention_for_block_factorized_sectors")
            is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("what_this_closes") == cert.get("what_this_closes")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "paper records reduction",
            "PASS"
            if all(
                needle in paper
                for needle in [
                    "cover choice = auxiliary representative choice",
                    "selected object = differential-cohomology class",
                    "not a selected smooth S3 source",
                    "projector retention remains open",
                ]
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa Deligne cover-gauge reduction audit")
    print("===========================================")
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
