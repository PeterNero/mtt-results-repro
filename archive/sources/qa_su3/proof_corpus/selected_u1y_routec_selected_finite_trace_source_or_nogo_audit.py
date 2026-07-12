"""Audit the selected finite-trace source/no-go gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_selected_finite_trace_source_or_nogo.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_selected_finite_trace_source_or_nogo_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SelectedFiniteTrace_SourceOrNoGo_v1.md"

STATUS = "U1Y_ROUTEC_SELECTED_FINITE_TRACE_SOURCE_NOGO_BUILT_27MODE_PREFIX_VALUES_SOURCE_TRACE_OPEN"
NEXT = "Selected_U1Y_RouteC_TraceEquals27Mode_or_FullHYMReplay_v1"


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
    lane = data["smooth_27mode_lane"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("old smoke rejected", data["old_smoke_lane"]["status"] == "REJECTED_AS_SELECTED_TRACE" and cert["old_smoke_trace_selected"] is False, data["old_smoke_lane"]),
        check("27mode prefix present", cert["smooth_27mode_prefix_values_present"] is True and cert["basis_dimension"] == 27 and cert["zero_cluster_dimension"] == 3, cert),
        check("nonidentity rhoE prefix imported", lane["rhoe"]["identity_smoke_replaced"] is True and lane["rhoe"]["nonidentity_projective_rhoE_candidate_built"] is True, lane["rhoe"]),
        check("DE/dotD prefix values present", lane["de"]["matrix_emitted"] is True and lane["dotd"]["matrix_emitted"] is True and lane["dotd"]["sector_projectors_emitted"] is True, lane),
        check("source trace still open", decision["selected_trace_equality_proved"] is False and decision["full_selected_operator_formula_proved"] is False and decision["selected_finite_connection_solve_closed"] is False, decision),
        check("legal closing routes named", set(data["accepted_closing_routes"]) == {"finite_trace_identification", "full_HYM_Newton_replay", "typed_monad_Cech_payload"}, data["accepted_closing_routes"]),
        check("no closure or lambda", cert["Phi_fin_closed"] is False and cert["lambda_12_closed"] is False and data["closure_claimed"] is False, cert),
        check("guardrails exclude overpromotion", guardrails["claims_model_active_operator_is_full_selected_operator"] is False and guardrails["uses_lifted_flags_as_proof"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records cutset", "selected_trace_equality" in note and "Do not compute `lambda_12`" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C selected finite-trace source/no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
