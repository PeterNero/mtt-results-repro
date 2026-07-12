"""Audit the U1/Y Route-C Phi_fin finite-emission subpacket."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_finite_emission_morphism_phifin_subpacket.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_finite_emission_morphism_phifin_subpacket.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_finite_emission_morphism_phifin_subpacket_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_FiniteEmissionMorphism_PhiFin_Subpacket_v1.md"

STATUS = "U1Y_ROUTEC_PHIFIN_SUBPACKET_BUILT_SELECTED_FINITE_TRACE_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedFiniteTrace_SourceOrNoGo_v1"


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
    stage_passes = cert["stage_passes"]
    decision = data["decision"]
    acceptance = data["acceptance_tests"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("domain lock only closed stage", stage_passes["domain_lock"] is True and sum(1 for value in stage_passes.values() if value is True) == 1, stage_passes),
        check("finite trace scaffold present", decision["finite_trace_scaffold_constructed"] is True and cert["finite_trace_scaffold_constructed"] is True, decision),
        check("Phi_fin not promoted", decision["Phi_fin_constructed"] is False and cert["Phi_fin_constructed"] is False and data["closure_claimed"] is False, decision),
        check("gap scaffold recorded", cert["min_complement_gap"] > 0 and cert["max_truncation_error_bound"] == 0.0, cert),
        check("selected verification blocks promotion", cert["selected_false_count"] > 0 and acceptance["selected_source_verified_theorem_derived"] is False, acceptance),
        check("payload acceptance refused honestly", acceptance["validators_pass_honestly"] is False and acceptance["primitive_C1_overlap_tensors_emitted_or_reduced"] is False, acceptance),
        check("guardrails exclude lambda and fitting", guardrails["claims_lambda12"] is False and guardrails["promotes_smoke_data"] is False and guardrails["uses_observed_data"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records no-promotion theorem", "cannot be promoted" in note and "Do not compute `lambda_12`" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C Phi_fin finite-emission subpacket audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
