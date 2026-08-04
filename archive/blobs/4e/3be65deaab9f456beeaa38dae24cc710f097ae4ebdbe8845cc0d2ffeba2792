"""Audit the selected Qa/SU3 spectral fallback reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_spectral_fallback_reduction_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_spectral_fallback_source_solve.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Spectral_Fallback_Reduction_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_spectral_fallback_reduction.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    closed = cert["closed_now"]
    open_items = cert["not_closed"]
    honest = cert["honest_current_q79_validator_exit_codes"]
    smoke = cert["conditional_smoke_result"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_SPECTRAL_FALLBACK_REDUCED_TO_SELECTED_SOURCE_SOLVE",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == cert["closed_now"]
            and computed["not_closed"] == cert["not_closed"]
            and computed["honest_current_q79_validator_exit_codes"] == honest,
            computed["status"],
        ),
        check(
            "template targets selected source solve",
            template["status"] == "OPEN_SELECTED_QA_SU3_SPECTRAL_FALLBACK_SOURCE_SOLVE_REQUIRED"
            and "selected_D_E_source" in template["must_supply"]
            and "selected_source_flags_justified_not_lifted" in template["must_supply"],
            template,
        ),
        check(
            "finite protocol reduced",
            closed["spectral_fallback_input_contract_closed"] is True
            and closed["finite_galerkin_execution_protocol_closed"] is True
            and closed["current_q79_branch_finite_pipeline_conditionally_validates"] is True,
            closed,
        ),
        check(
            "honest algebra pass/fail boundary",
            honest == {
                "de_action": 1,
                "dotd_response": 1,
                "reduced_green": 1,
                "rhoE_mesh": 0,
                "rhoE_metric": 0,
                "riesz_gap": 1,
                "route_c_residual": 1,
                "sector_maps": 0,
            },
            honest,
        ),
        check(
            "failures are selected source failures",
            closed["honest_failures_are_selected_source_failures"] is True
            and smoke["selected_origin_still_missing"] is True
            and smoke["route_c_residual_values_are_smoke_not_solve"] is True,
            smoke,
        ),
        check(
            "remaining values explicit",
            open_items["selected_D_E_source"] is True
            and open_items["basis_B_N_values"] is True
            and open_items["dotD_alpha1_values"] is True
            and open_items["primitive_overlap_or_C1_contractions"] is True,
            open_items,
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_selected_D_E_constructed"] is False
            and cert["guardrails"]["claims_route_c_residual_solve"] is False
            and cert["guardrails"]["uses_lifted_flags_as_proof"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False,
            cert["guardrails"],
        ),
        check(
            "note records exact next object",
            "Selected_Qa_SU3_RouteC_Source_Solve_or_Typed_Operator_v1" in note
            and "The lifted Route C smoke files are not a proof source" in note
            and "selected_source_verified" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 spectral fallback reduction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
