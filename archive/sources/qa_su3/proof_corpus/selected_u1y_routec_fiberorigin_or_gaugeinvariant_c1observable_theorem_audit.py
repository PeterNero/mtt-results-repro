"""Audit the fiber-origin / gauge-invariant C1 observable theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_FiberOrigin_or_GaugeInvariantC1Observable_Theorem_v1.md"

STATUS = "U1Y_ROUTEC_FIBERCLASS_C1_OBSERVABLE_QUOTIENT_CLOSED_MATRIX_REPRESENTATIVE_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


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
    obs = data["spectral_observable_summary"]
    guards = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("quotient closed", cert["fiberclass_quotient_for_current_C1_spectral_observables_closed"] is True and decision["shift0_allowed_as_computation_gauge"] is True, decision),
        check("absolute origin open", cert["absolute_fiber_origin_selected"] is False and decision["absolute_fiber_origin_used_as_hidden_knob"] is False, decision),
        check("spectral invariance", obs["rank_invariant"] is True and obs["YYstar_scalar_identity_invariant"] is True and obs["current_layer_flavor_splitting_possible"] is False, obs),
        check("matrix representative open", cert["selected_matrix_representative_for_full_C1_operator"] is False and data["downstream_boundary"]["can_promote_fixed_fiber_representative_for_full_C1_matrix_operator"] is False, data["downstream_boundary"]),
        check("no downstream computation", cert["A_selected_computable"] is False and cert["b_selected_computable"] is False and cert["lambda_12_computable"] is False, cert),
        check("guardrails hold", all(value is False for value in guards.values()) and data["target_fitting_used"] is False, guards),
        check("note records hidden knob boundary", "hidden absolute fiber-origin knob" in note and "not a full selected matrix representative" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C fiber-origin/gauge-invariant C1 observable audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
