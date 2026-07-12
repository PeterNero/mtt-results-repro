"""Audit the U1/Y Route-C finite HYM solve or typed Cech payload gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_FiniteHYMConnectionSolve_or_TypedCechPayload_v1.md"

STATUS = "U1Y_ROUTEC_FINITE_HYM_SOLVE_PROMOTES_DE_GAP_LAYER_DOTD_ALPHA1_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_dotDAlpha1_SourceNormalization_or_End0SectorRouting_v1"


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
    guardrails = data["guardrails"]
    promoted = data["promoted_finite_routec_payload"]
    audit_checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("gap layer promoted", decision["finite_DE_gap_layer_promoted"] is True and cert["finite_DE_gap_layer_promoted"] is True, decision),
        check("BN and DE closed", promoted["finite_basis_BN"]["basis_dimension"] == 27 and promoted["DE_action"]["D_E_source_flags_are_theorem_derived"] is True, promoted),
        check("gap bounds", cert["selected_gap_lower_bound"] > 0 and cert["selected_green_norm_bound"] > 0, cert),
        check("alpha1 formula but value open", decision["analytic_alpha1_kernel_formula_proved"] is True and decision["dotD_alpha1_source_closed"] is False and decision["selected_alpha1_value_fill_closed"] is False, decision),
        check("full solve remains open", decision["full_finite_HYM_connection_solve_closed"] is False and decision["typed_cech_payload_filled"] is False, decision),
        check("no downstream closure", data["closure_claimed"] is False and decision["primitive_C1_values_computed"] is False and decision["lambda_12_computable"] is False, decision),
        check("guardrails", guardrails["promotes_dotD_value_matrices_without_alpha1_source"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents scope", "This closes only the D_E gap/Riesz/Green layer" in note and "dotD_alpha1 source normalization" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C finite HYM solve or typed Cech payload audit")
    return 0 if all(audit_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
