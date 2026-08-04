"""Audit oriented Phi_fin End(E)-basis / nonidentity-rhoE value insertion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_ende_basis_or_nonidentityrhoe_valueinsertion.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_ende_basis_or_nonidentityrhoe_valueinsertion.candidate.json"
INSERTION = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_ende_basis_or_nonidentityrhoe_valueinsertion_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_ende_basis_or_nonidentityrhoe_valueinsertion_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_EndE_Basis_or_NonidentityRhoE_ValueInsertion_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_ENDE_OR_RHOE_VALUEINSERTION_CURRENT_SOURCE_NOGO_REPAIR_SPLIT"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectFiniteResponse_or_ProjectiveRhoE_SourceAmendment_v1"


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
    insertion = load(INSERTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    lane_a = insertion["lane_A_typed_EndE_basis"]
    lane_b = insertion["lane_B_nonidentity_projective_rhoE"]
    lane_c = insertion["lane_C_direct_same_source_finite_response"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("insertion attempted", decision["value_insertion_attempted"] is True and decision["repair_split_built"] is True, decision)
    check("lane A blocked", lane_a["attempted"] is True and lane_a["value_inserted"] is False and lane_a["support_strength"]["typed_sourcefill_filled_leaf_count"] > 0, lane_a)
    check("lane B blocked", lane_b["attempted"] is True and lane_b["value_inserted"] is False and lane_b["support_strength"]["twist_cancellation_context"] is True, lane_b)
    check("lane C promoted as repair", lane_c["attempted"] is False and lane_c["required_payload"]["no_double_count_replay"] is True, lane_c)
    check("no values inserted", decision["typed_EndE_basis_inserted"] is False and decision["nonidentity_projective_rhoE_inserted"] is False and decision["direct_same_source_finite_response_inserted"] is False, decision)
    check("source theorem still open", decision["oriented_source_theorem_closed"] is False and decision["new_oriented_leaf_closed"] is False, decision)
    check("selected next repair", decision["selected_next_repair"] == "C_direct_same_source_finite_response_or_B_projective_rhoE_source_amendment", decision)
    check("legal repairs retained", len(insertion["legal_minimal_repairs"]) == 3, insertion["legal_minimal_repairs"])
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records packet", str(INSERTION.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin EndE/rhoE value insertion audit")


if __name__ == "__main__":
    main()
