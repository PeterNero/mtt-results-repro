"""Audit the primitive-class C1 observable / higher-order response gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1.md"

STATUS = "U1Y_ROUTEC_PRIMITIVECLASS_C1OBSERVABLE_NO_SPLIT_HIGHERORDER_SOURCE_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1"


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
    tests = data["primitive_layer_tests"]
    decision = data["decision"]
    guards = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("primitive scalar identity", tests["all_yy_star_scalar_identity"] is True and tests["max_traceless_norm_sq"] == 0.0, tests),
        check("primitive no split", tests["mass_splitting_test_passes"] is False and tests["mixing_commutator_test_passes"] is False and tests["cp_odd_test_passes"] is False, tests),
        check("higher-order required", decision["higher_order_or_full_response_source_emission_required"] is True and cert["higher_order_or_full_response_source_emission_required"] is True, decision),
        check("downstream not computable", cert["primitive_class_can_emit_A_selected"] is False and cert["primitive_class_can_emit_b_selected"] is False and cert["primitive_class_can_emit_lambda_12"] is False, cert),
        check("acceptance tests imported", data["higher_order_contract"]["criterion_imported"] is True and data["higher_order_contract"]["full_response_acceptance_tests_locked"] is True, data["higher_order_contract"]),
        check("guardrails hold", all(value is False for value in guards.values()) and data["target_fitting_used"] is False, guards),
        check("note records support boundary", "Diagnostic splitters" in note and "support only" in note and "Y_s Y_s^* = c I" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C primitive-class C1 observable / higher-order source-emission audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
