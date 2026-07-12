"""Audit positive-magnitude source-ownership / smooth-EQa emission attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission.candidate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission_contract.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_PositiveMagnitude_SourceOwnership_or_SmoothEQa_Emission_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_POSITIVEMAGNITUDE_SOURCEOWNERSHIP_AND_SMOOTHEQA_EMISSION_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1"


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
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    direct = data["lanes"]["direct_source_owned_operator"]
    smooth = data["lanes"]["smooth_EQa_emission"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("exact values retained", decision["oriented_table_values_ready_to_consume"] is True and decision["oriented_abs_sector_logdet_exact"] == "log(92160000)", decision)
    check("direct support filled", direct["same_branch_certificate_closed"] is True and direct["orientation_bound_to_same_threshold_complex"] is True and direct["direct_response_D_E_support_materialized"] is True, direct)
    check("direct true blockers open", direct["oriented_BN_carrier_emitted"] is False and direct["EndE_or_rhoE_to_oriented_BN_functor"] is False and direct["positive_PhiFin_magnitude_owned"] is False and direct["finitepart_trace_identity"] is False, direct)
    check("smooth geometry filled", smooth["R_plus_curvature_filled"] is True and smooth["geometric_tensor_payload_filled"] is True, smooth)
    check("smooth payload blockers open", smooth["bundle_connection_A_filled"] is False and smooth["bundle_curvature_F_A_filled"] is False and smooth["E_Qa_matrix_filled"] is False and smooth["kernel_and_quotient_policy_filled"] is False, smooth)
    check("contract exact value", contract["known_exact_values_to_consume"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", contract)
    check("contract forbids shortcuts", "use observed couplings, matching scales, or residual fits" in contract["forbidden_shortcuts"], contract["forbidden_shortcuts"])
    check("no promotion", decision["source_owned_positive_PhiFin_magnitude"] is False and decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, (decision, cert))
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records contract", str(CONTRACT.relative_to(ROOT)) in note and NEXT in note and "log(92160000)" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin positive-magnitude sourceownership/smooth-EQa emission audit passed")


if __name__ == "__main__":
    main()
