"""Audit full-Fourier-orbit source-emission or trace-identity gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_fullfourierorbit_sourceemission_or_traceidentity.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_fullfourierorbit_sourceemission_or_traceidentity.candidate.json"
TRACE = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_fullfourierorbit_sourceemission_or_traceidentity_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_FullFourierOrbit_SourceEmission_or_TraceIdentity_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_FULLFOURIERORBIT_TRACEIDENTITY_CLOSED_SOURCEEMISSION_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_FullFourierOrbit_SourceSelection_Theorem_or_NoGo_v1"


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
    trace = load(TRACE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    source = data["source_emission_attempt"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("trace products", trace["plus_sector_product"] == 9600 and trace["minus_sector_product"] == 9600 and trace["oriented_abs_sector_product"] == 92160000, trace)
    check("sector counts", len(trace["plus_sector_values"]) == 8 and len(trace["minus_sector_values"]) == 8, trace)
    check("relative trace closed", trace["identity_closed_relative_to_full_orbit_source"] is True and decision["trace_identity_closed_relative_to_full_orbit_source"] is True and cert["trace_identity_closed_relative_to_full_orbit_source"] is True, decision)
    check("source emission open", decision["source_emits_full_oriented_positive_fourier_orbit"] is False and source["full_sixteen_positive_oriented_fourier_modes"]["closed"] is False, source)
    check("carrier open", decision["source_emits_oriented_BN_carrier"] is False and source["full_27_mode_BN_carrier_as_selected_threshold_domain"]["closed"] is False, source)
    check("positive magnitude open", decision["positive_magnitude_source_owned"] is False and source["PhiFin_positive_magnitude_source_owned"]["closed"] is False, source)
    check("single leaf", decision["remaining_single_leaf"] == "source_emits_full_oriented_positive_fourier_orbit" and cert["remaining_single_leaf"] == decision["remaining_single_leaf"], decision)
    check("no promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records trace", "trace_identity_closed_relative_to_full_orbit_source = true" in note and str(TRACE.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin full-Fourier-orbit trace-identity audit passed")


if __name__ == "__main__":
    main()
