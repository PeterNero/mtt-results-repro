"""Audit BN27 full-operator/source-flags/quotient-functor value construction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_fulloperatorformula_sourceflags_or_quotientfunctor_valueconstruction.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_fulloperatorformula_sourceflags_or_quotientfunctor_valueconstruction.candidate.json"
TRANSFER = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_quotient_finitepart_transfer_boundary.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_fulloperatorformula_sourceflags_or_quotientfunctor_valueconstruction_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_FullOperatorFormula_SourceFlags_or_QuotientFunctor_ValueConstruction_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_QUOTIENT_FINITEPART_SUPPORT_IMPORTED_SOURCE_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_DirectFinitePartFunctional_or_SourceOwnedLogdetTheorem_v1"


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
    transfer = load(TRANSFER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("support imported", decision["quotient_finitepart_support_imported"] is True and all(transfer["importable_as_support"].values()), transfer["importable_as_support"])
    check("transfer not identity", all(value is False for value in transfer["not_importable_as_BN27_source_identity"].values()), transfer["not_importable_as_BN27_source_identity"])
    check("full formula open", decision["full_selected_operator_formula_closed_for_BN27"] is False and data["lane_evaluation"]["lane_A_full_operator_formula"]["closed_now"] is False, data["lane_evaluation"]["lane_A_full_operator_formula"])
    check("source flags open", decision["theorem_derived_selected_source_flags_for_full_BN27"] is False and data["lane_evaluation"]["lane_B_theorem_derived_full_source_flags"]["closed_now"] is False, data["lane_evaluation"]["lane_B_theorem_derived_full_source_flags"])
    check("quotient/source functor open", decision["quotient_or_source_identity_functor_closed_for_BN27"] is False and data["lane_evaluation"]["lane_C_quotient_functor_value_construction"]["closed_now"] is False, data["lane_evaluation"]["lane_C_quotient_functor_value_construction"])
    check("direct finitepart ranked next", data["lane_evaluation"]["lane_D_direct_finitepart_functional_on_BN27"]["ranked_next"] is True and decision["direct_finitepart_functional_on_BN27_closed"] is False, data["lane_evaluation"]["lane_D_direct_finitepart_functional_on_BN27"])
    check("no BN27 closure", decision["BN27_source_identity_closed"] is False and data["closure_claimed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records transfer", NEXT in note and str(TRANSFER.relative_to(ROOT)) in note and "oriented_logdet_promoted = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 full-operator/source-flags/quotient-functor audit passed")


if __name__ == "__main__":
    main()
