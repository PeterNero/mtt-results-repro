"""Audit the C_tau positive finite-part / smooth Dirac convention theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_Ctau_PositiveFinitePart_or_SmoothDiracConvention_SourceTheorem_v1.md"

STATUS = "HETEROTIC_CTAU_DIRAC_CONVENTION_POSITIVE_FINITEPART_CLOSED_TRIVIAL_MAGNITUDE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_ProductOperator_or_SmoothEQa_MagnitudeSource_v1"


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
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    packet = data["dirac_packet"]
    request = data["oriented_product_request"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("convention closed", decision["ctau_positive_finitepart_convention_closed"] is True and decision["ctau_chiral_dirac_convention_source_selected"] is True, decision)
    check("full spectrum", packet["spectra"]["full_BN"]["C_tau_square_positive_complement"] == {"1": 18} and packet["spectra"]["full_BN"]["Dirac_square_positive_complement"] == {"1": 36}, packet["spectra"]["full_BN"])
    check("embedded spectrum", packet["spectra"]["embedded_11"]["C_tau_square_positive_complement"] == {"1": 8} and packet["spectra"]["embedded_11"]["Dirac_square_positive_complement"] == {"1": 16}, packet["spectra"]["embedded_11"])
    check("trivial logdet", decision["ctau_logdet_value_full_BN"] == 0.0 and decision["ctau_logdet_value_embedded_11"] == 0.0, decision)
    check("eta zero", decision["ctau_eta_value_full_BN"] == 0 and decision["ctau_eta_value_embedded_11"] == 0, decision)
    check("orientation not magnitude", decision["ctau_supplies_orientation"] is True and decision["ctau_supplies_nonzero_threshold_magnitude"] is False, decision)
    check("product still open", decision["oriented_phifin_product_operator_closed"] is False and request["required_to_close_next"]["source_emits_oriented_operator"] is None, request)
    check("forbidden shortcuts", "use C_tau Dirac logdet 0 as the heterotic threshold magnitude" in request["forbidden_shortcuts"], request["forbidden_shortcuts"])
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records theorem", "ctau_positive_finitepart_convention_closed = true" in note and NEXT in note, NOTE)

    print("\nSelected heterotic C_tau positive finite-part / smooth Dirac convention source-theorem audit")


if __name__ == "__main__":
    main()
