"""Audit the U1/Y Route-C selected visible operator source or primitive C1 gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_selected_visible_operator_source_or_primitive_c1_contractions.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_selected_visible_operator_source_or_primitive_c1_contractions.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_selected_visible_operator_source_or_primitive_c1_contractions_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SelectedVisibleOperatorSource_or_PrimitiveC1Contractions_v1.md"

STATUS = "U1Y_ROUTEC_VISIBLE_OPERATOR_OR_PRIMITIVE_C1_REDUCED_SOURCE_CERT_OR_TYPED_DE_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedSourceCertificate_or_TypedDEConstruction_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    reduction = data["reduction"]
    guardrails = data["guardrails"]
    audit_checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("subvalidators carried", decision["selected_ordered_source_subvalidator_passes"] is True and decision["selected_s3_class_subvalidator_passes"] is True, decision),
        check("arithmetic not source", decision["current_routec_arithmetic_passes_if_selected_flags_supplied"] is True and decision["selected_source_certificate_emitted"] is False, decision),
        check("visible source open", decision["selected_visible_operator_source_validator_passes"] is False and decision["selected_DE_Green_dotD_source_proved"] is False, decision),
        check("primitive C1 open", decision["primitive_c1_contract_atom_count"] == 24 and decision["primitive_c1_missing_atom_count"] == 24 and decision["primitive_c1_matrices_emitted"] is False, decision),
        check("source gate next", reduction["de_green_dotd_source_lane"]["next_required_artifact"] == "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1", reduction["de_green_dotd_source_lane"]),
        check("no downstream closure", data["closure_claimed"] is False and decision["A_selected_or_b_selected_emitted"] is False and decision["lambda_12_computable"] is False, decision),
        check("guardrails", guardrails["promotes_diagnostic_selected_flags"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents slots", "Primitive C1 Slots" in note and "Do not promote diagnostic selected-source flags" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C visible operator/primitive C1 audit")
    return 0 if all(audit_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
