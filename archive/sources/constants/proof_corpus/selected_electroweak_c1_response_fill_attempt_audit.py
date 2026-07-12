"""Audit the attempted fill of the selected electroweak C1 response template."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_C1_Response_Fill_Attempt_v1.md"
CERT = REPO / "certificates" / "selected_electroweak_c1_response_fill_attempt_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_electroweak_c1_response.template.json"
CALCULATOR = REPO / "scripts" / "compute_electroweak_c1_response.py"
HETEROTIC = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
EXECUTION_I = OBSIDIAN / "18 Theta-Closure & Execution Program" / "Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v2.md"
SUPERSET = Q79 / "proof_corpus" / "Superset_Determinations_in_Modal_Triplet_Theory_v2.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run_template() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CALCULATOR), str(TEMPLATE)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = load_json(CERT)
    template = load_json(TEMPLATE)
    note = read(NOTE)
    heterotic = read(HETEROTIC)
    execution_i = read(EXECUTION_I)
    superset = read(SUPERSET)
    run = run_template()

    required_terms = list(cert["term_status"].keys())
    checks = [
        check(
            "certificate status",
            cert["status"] == "PEW_ALPHA1_TEMPLATE_FILL_BLOCKED_SELECTED_THRESHOLD_DATA_MISSING",
            cert["status"],
        ),
        check(
            "template remains open",
            template["status"] == "OPEN"
            and all(template["raw_response_per_v1"]["terms"][term] is None for term in required_terms),
            template["raw_response_per_v1"]["terms"],
        ),
        check(
            "calculator refuses template",
            run.returncode == 2
            and all(f"raw_response_per_v1.terms.{term}" in run.stdout for term in required_terms),
            run.stdout.splitlines(),
        ),
        check(
            "heterotic source does not compute thresholds",
            contains_all(heterotic, ["g^{-2}=\\mathrm{Re}\\,S", "threshold corrections", "we do not attempt to compute here"]),
            "f=S plus thresholds not computed",
        ),
        check(
            "Execution I coefficients are matching coefficients",
            contains_all(execution_i, ["Solving for exact matching", "c_1 = 0.31", "c_2 = -0.27"]),
            "matching-derived exceptional coefficients",
        ),
        check(
            "superset source is minimum-norm diagnostic",
            contains_all(superset, ["Minimum--Norm Threshold Diagnostics", "crossing conditions", "unique minimum--norm solution"]),
            "threshold diagnostic not selected local response",
        ),
        check(
            "term classifications block fill",
            all(item["status"] != "CLOSED_VALUE" for item in cert["term_status"].values())
            and cert["verdict"]["template_filled"] is False,
            cert["term_status"],
        ),
        check(
            "trace-only closure recorded",
            cert["closed_reduction"]["universal_trace_drops_from_lambda_12"] is True
            and "lambda_12 = p_1 - p_2" in note,
            cert["closed_reduction"],
        ),
        check(
            "no numeric electroweak closure",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        ),
        check(
            "note states exact next data object",
            "SelectedElectroweakC1PrimitiveResponseCertificate" in note
            and "PEW_ALPHA1_TEMPLATE_FILL_BLOCKED_SELECTED_THRESHOLD_DATA_MISSING" in note,
            "next primitive response certificate",
        ),
    ]

    print("\nSelected electroweak C1 response fill attempt audit")
    print("===================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())

