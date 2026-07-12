"""Audit the heterotic/Strominger analytic-torsion or threshold-operator payload gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_strominger_threshold_operator_or_torsion_source.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_Strominger_AnalyticTorsion_or_ThresholdOperator_Payload_v1.md"

STATUS = "HETEROTIC_STROMINGER_ANALYTIC_TORSION_THRESHOLD_PAYLOAD_REDUCED_TO_SOURCE_OPERATOR_OR_LOCAL_SYSTEM"
NEXT = "Selected_Heterotic_Strominger_SourceOperator_or_LocalSystem_Torsion_Computation_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return proc.returncode

    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    routes = data["route_tests"]
    guards = data["guardrails"]

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("payload stays open", decision["payload_closed"] is False and data["closure_claimed"] is False, decision),
        check("internal lambda preserved only", abs(decision["internal_lambda_12_value"] - 2.6179362173268497) < 1e-12 and decision["retire_internal_replay_as_physical_threshold_source"] is True, decision),
        check("internal replay rejected", routes["A_internal_finite_quotient_replay"]["can_supply_payload_now"] is False and routes["A_internal_finite_quotient_replay"]["status"] == "REJECTED_AS_PHYSICAL_HETEROTIC_THRESHOLD", routes["A_internal_finite_quotient_replay"]),
        check("local-system route live but open", routes["B_ray_singer_or_reidemeister_local_system"]["computable_now"] is False and routes["B_ray_singer_or_reidemeister_local_system"]["selected_candidates_count"] == 0, routes["B_ray_singer_or_reidemeister_local_system"]),
        check("HYM route live but open", routes["C_hym_monad_threshold_operator"]["operator_domain_selected_for_next_gate"] is True and routes["C_hym_monad_threshold_operator"]["mu_selected"] is False and routes["C_hym_monad_threshold_operator"]["selected_spectrum_or_torsion_available"] is False, routes["C_hym_monad_threshold_operator"]),
        check("SU2 is partial only", routes["D_su2_flat_fp_partial_row"]["selected_threshold_background_flat"] is True and routes["D_su2_flat_fp_partial_row"]["can_supply_payload_now"] is False, routes["D_su2_flat_fp_partial_row"]),
        check("template names both exits", template["allowed_exit_A_local_system_torsion"]["selected_lattice_or_character"] is None and template["allowed_exit_B_threshold_operator"]["mu_or_moduli_selection"] is None, template),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note has theorem", "HYM/monad operator lane" in note and "Ray-Singer/Reidemeister finite part" in note, NOTE),
    ]
    print("\nSelected heterotic/Strominger analytic-torsion or threshold-operator payload audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
