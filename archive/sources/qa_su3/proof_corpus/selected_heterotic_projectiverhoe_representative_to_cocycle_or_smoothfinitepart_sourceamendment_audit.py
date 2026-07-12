"""Audit the projective rho_E representative-to-cocycle source-amendment packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_representative_to_cocycle_or_smoothfinitepart_sourceamendment.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_representative_to_cocycle_or_smoothfinitepart_sourceamendment.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_representative_to_cocycle_or_smoothfinitepart_sourceamendment_certificate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_finite_representative_to_cocycle_packet.json"
MISSING = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_representative_to_cocycle_smooth_missing_leaves.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_RepresentativeToCocycleMap_or_SmoothFinitePart_SourceAmendment_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_REPRESENTATIVE_TO_COCYCLE_FINITE_MAP_CLOSED_SMOOTH_FINITEPART_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothTransitionTables_or_ComplementQuotient_NoDoubleCount_v1"


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
    missing = load(MISSING)
    note = NOTE.read_text(encoding="utf-8")

    tau = packet["central_cocycle_map"]["tau_values"]
    products = packet["central_cocycle_map"]["product_checks"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("finite map closed", data["decision"]["finite_representative_to_cocycle_map_closed"] is True and cert["finite_representative_to_cocycle_map_closed"] is True, data["decision"])
    check("tau table complete", set(tau) == {"F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"}, tau)
    check("nontrivial tau", any(value != 0 for value in tau.values()) and tau["P"] == 0, tau)
    check("five product checks", len(products) == 5 and all(row["twist_cancels_to_P"] and row["additive_defect"] == 0 for row in products.values()), products)
    check("character denominator", packet["finite_representative"]["character_denominator"] == 3 and packet["finite_representative"]["primitive_covector"] == [0, 0, 1], packet["finite_representative"])
    check("finite response attached", packet["finite_response_attached"]["internal_finite_part"] == "log(2008)" and packet["finite_response_attached"]["chi_Qa"] == "1", packet["finite_response_attached"])
    check("smooth still open", data["decision"]["smooth_transition_tables_emitted"] is False and data["decision"]["smooth_finitepart_computed"] is False and cert["smooth_finitepart_computed"] is False, data["decision"])
    check("smooth missing list", missing["status"] == "FINITE_MAP_CLOSED_SMOOTH_VALUES_OPEN" and len(missing["smooth_still_missing"]) >= 10, missing)
    check("cross checks", data["cross_checks"]["previous_smooth_packet_open"] is True and data["cross_checks"]["previous_trace_lift_no_go_retained"] is True and data["cross_checks"]["all_product_defects_zero"] is True, data["cross_checks"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["decision"]["E_Qa_computed"] is False, data["decision"])
    check("note documents finite not smooth", NEXT in note and "finite quotient theorem" in note and "smooth transition-table theorem" in note, NOTE)

    print("\nSelected heterotic projective rho_E representative-to-cocycle source amendment audit")


if __name__ == "__main__":
    main()
