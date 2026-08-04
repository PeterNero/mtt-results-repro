"""Audit HYM mu-selection or full-DeltaA spectrum theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_hym_mu_selection_or_full_deltaa_spectrum.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_hym_mu_selection_or_full_deltaa_spectrum.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_hym_mu_selection_or_full_deltaa_spectrum_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_HYM_Mu_Selection_or_Full_DeltaA_Spectrum_v1.md"

STATUS = "HETEROTIC_HYM_MU_SELECTION_NO_EXTREMUM_FULL_DELTAA_SPECTRUM_OPEN"
NEXT = "Selected_Heterotic_HYM_FullQuotientSpectrum_or_OUHessianScale_SourcePacket_v1"


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
    mono = data["monotonicity_proof"]
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("derivative positive", mono["all_terms_positive_on_domain"] is True and mono["strictly_increasing"] is True, mono)
    check("no stationary mu", mono["stationary_point_exists_on_mu_positive"] is False and decision["mu_selected"] is False, mono)
    check("samples positive derivative", all(item["d_logdet"] > 0 for item in mono["samples"].values()), mono["samples"])
    check("internal mu rejected as physical", data["source_tests"]["internal_mu_equals_one"]["can_select_physical_mu"] is False, data["source_tests"]["internal_mu_equals_one"])
    check("full spectrum still open", decision["full_deltaA_spectrum_computed"] is False and data["still_open"]["full_DeltaA_quotient_domain"] is True, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("note records theorem", "d/dmu log det' > 0" in note and NEXT in note, NOTE)

    print("\nSelected heterotic HYM mu-selection / full-DeltaA spectrum audit")


if __name__ == "__main__":
    main()
