"""Audit the BN central-rank operator / smooth E_Qa source-emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_BN_CentralRankOperator_or_SmoothEQa_SourceEmission_v1.md"

STATUS = "HETEROTIC_BN_CENTRALRANKOPERATOR_SOURCEEMISSION_SIGNED_INTERTWINER_CLOSED_POSITIVE_FINITEPART_OPEN"
NEXT = "Selected_Heterotic_Ctau_PositiveFinitePart_or_SmoothDiracConvention_SourceTheorem_v1"


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
    selected = data["selected_operator"]
    opts = data["regularization_options"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("signed identity closed", decision["C_tau_signed_intertwiner_closed"] is True and decision["operator_identity_closed_for_signed_layer"] is True, decision)
    check("all embedded labels intertwine", all(item["intertwines"] for item in selected["embedded_checks"].values()), selected["embedded_checks"])
    check("full spectrum exact", selected["full_BN_spectrum"] == {"-1": 9, "0": 9, "1": 9}, selected["full_BN_spectrum"])
    check("embedded spectrum exact", selected["embedded_11_spectrum"] == {"-1": 4, "0": 3, "1": 4}, selected["embedded_11_spectrum"])
    check("positive finitepart open", decision["positive_finitepart_for_C_tau_closed"] is False and decision["operator_identity_closed_for_positive_finitepart_layer"] is False, decision)
    check("direct signed determinant rejected", opts["C_tau_signed"]["positive_definite"] is False and opts["C_tau_signed"]["finite_positive_logdet_available"] is False, opts["C_tau_signed"])
    check("square route loses sign", opts["C_tau_square_or_absolute"]["positive_semidefinite"] is True and opts["C_tau_square_or_absolute"]["loses_orientation_sign"] is True, opts["C_tau_square_or_absolute"])
    check("shift route not selected", opts["two_I_plus_C_tau"]["positive_definite"] is True and opts["two_I_plus_C_tau"]["source_selected_shift"] is False, opts["two_I_plus_C_tau"])
    check("dirac route primary", decision["chiral_dirac_eta_route_ranked_primary"] is True and opts["chiral_Dirac_pair"]["source_selected_Dirac_convention"] is False, opts["chiral_Dirac_pair"])
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records fork", "Regularization Fork" in note and "chiral Dirac" in note and NEXT in note, NOTE)

    print("\nSelected heterotic BN central-rank operator / smooth E_Qa source-emission audit")


if __name__ == "__main__":
    main()
