"""Audit direct-carrier constructive attempt for oriented Phi_fin."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_directcarrier_constructive_attempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt.candidate.json"
REPORT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt_report.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_directcarrier_constructive_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_DirectCarrier_SourceTheorem_ConstructiveAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTCARRIER_CONSTRUCTIVE_ATTEMPT_FULL_ORBIT_SOURCE_EMISSION_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_FullFourierOrbit_SourceEmission_or_TraceIdentity_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    report = load(REPORT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    gap = report["constructive_attempt"]["computed_gap"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("full sector products", gap["full_plus_sector_product"] == 9600 and gap["full_minus_sector_product"] == 9600 and gap["full_abs_sector_product"] == 92160000, gap)
    check("embedded product strict", gap["embedded_plus_product"] == 4 and gap["embedded_minus_product"] == 4 and gap["embedded_abs_product"] == 16, gap)
    check("missing multiplier", gap["missing_multiplier_to_full_abs_sector"] == 5760000 and cert["missing_multiplier_to_full_abs_sector"] == 5760000, cert)
    check("missing rows count", gap["missing_positive_oriented_row_count"] == 10 and len(gap["missing_positive_oriented_rows"]) == 10, gap["missing_positive_oriented_rows"])
    check("new minimal leaf", decision["new_minimal_leaf"] == "source_emits_full_oriented_positive_fourier_orbit" and cert["new_minimal_leaf"] == decision["new_minimal_leaf"], decision)
    check("orientation but no magnitude", decision["orientation_functor_closed"] is True and decision["positive_magnitude_functor_closed"] is False, decision)
    check("direct carrier open", decision["source_emits_oriented_BN_carrier"] is False and decision["direct_carrier_theorem_closed"] is False, decision)
    check("source theorem needs full orbit", "the full 27-mode B_N carrier as the selected threshold domain" in report["source_theorem_needed"]["must_emit"], report["source_theorem_needed"])
    check("no logdet promotion", decision["finitepart_trace_identity_closed"] is False and decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, decision)
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and report["closure_claimed"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records gap", "missing_multiplier_to_full_abs_sector = 5760000" in note and str(REPORT.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin direct-carrier constructive attempt audit passed")


if __name__ == "__main__":
    main()
