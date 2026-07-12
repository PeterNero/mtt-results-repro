"""Audit the oriented Phi_fin product-operator / smooth E_Qa magnitude source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource.candidate.json"
TABLE = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_ProductOperator_or_SmoothEQa_MagnitudeSource_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SIMULTANEOUS_TABLE_BUILT_SOURCE_MAGNITUDE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceEmission_or_SmoothEQa_ThresholdIdentity_v1"


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
    table = load(TABLE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    gap = data["source_gap"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("same domain and commutation", decision["same_BN_domain_for_Ctau_and_PhiFin_positive_gap"] is True and table["commutation"]["commutator_zero"] is True, table["commutation"])
    check("table dimensions", table["basis_dimension"] == 27 and len(table["entries"]) == 27, table["basis_dimension"])
    check("ctau counts", table["counts"]["C_tau_spectrum"] == {"-1": 9, "0": 9, "1": 9}, table["counts"])
    check("positive table exists", table["counts"]["PhiFin_positive_count"] > 0 and decision["oriented_product_table_built"] is True, table["counts"])
    check("source magnitude open", gap["same_source_threshold_identity_closed"] is False and decision["heterotic_threshold_magnitude_promoted"] is False, gap)
    check("operator source not emitted", decision["oriented_product_operator_source_emitted"] is False and cert["oriented_product_operator_source_emitted"] is False, cert)
    check("computed logdets finite", isinstance(decision["PhiFin_all_positive_logdet"], float) and isinstance(decision["oriented_abs_sector_logdet_sum"], float), decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records theorem", "commutation_closed = true" in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin product-operator / smooth E_Qa magnitude-source audit")


if __name__ == "__main__":
    main()
