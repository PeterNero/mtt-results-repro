"""Audit the exact-complement or smooth rho_E transition value-packet attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket_certificate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_ExactComplementQuotient_or_SmoothRhoETransitionTables_ValuePacket_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_VALUEPACKET_ATTEMPT_INTERNAL_PROJECTION_CLOSED_SMOOTH_TABLES_EXACT_QUOTIENT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_ExactComplementFactorization_or_GoodCoverTransitionTables_SourceSearch_v1"


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
    cert = load(CERT)
    packet = load(PACKET)
    note = NOTE.read_text(encoding="utf-8")

    projection = packet["lane_B_exact_complement_quotient"]["finite_projection_family_internal"]
    smooth_lane = packet["lane_A_smooth_transition_tables"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("internal projection closed", data["decision"]["internal_projection_family_closed"] is True and projection["closed_for_internal_quotient"] is True, projection)
    check("eleven labels", len(projection["codomain"]) == 11 and projection["codomain"][0] == "F1" and projection["codomain"][-1] == "P", projection["codomain"])
    check("finite values retained", packet["finite_internal_values"]["finite_internal_part"] == "log(2008)" and packet["finite_internal_values"]["chi_Qa"] == "1", packet["finite_internal_values"])
    check("smooth lane open", smooth_lane["rho_E_overlap_or_generator_boundary_tables"] is None and smooth_lane["cocycle_law_checked_on_smooth_tables"] is False, smooth_lane)
    check("exact quotient open", data["decision"]["exact_smooth_complement_quotient_closed"] is False and packet["lane_B_exact_complement_quotient"]["heat_zeta_torsion_factorization_theorem"] is None, packet["lane_B_exact_complement_quotient"])
    check("E and smooth finite part open", data["decision"]["E_Qa_computed"] is False and data["decision"]["smooth_finitepart_computed"] is False, data["decision"])
    check("hard blockers listed", len(data["decision"]["remaining_hard_blockers"]) == 5 and "smooth rho_E overlap/generator transition tables" in data["decision"]["remaining_hard_blockers"], data["decision"]["remaining_hard_blockers"])
    check("cross checks", all(data["cross_checks"].values()), data["cross_checks"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["decision"]["smooth_transition_tables_emitted"] is False, data["decision"])
    check("note records two remaining routes", NEXT in note and "good-cover/transition-table" in note and "complement-factorization" in note, NOTE)

    print("\nSelected heterotic projective rho_E exact-complement or smooth-transition value-packet audit")


if __name__ == "__main__":
    main()
