"""Audit oriented Phi_fin EndE-domain / nonidentity-rhoE source-value insertion."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_endedomain_or_nonidentityrhoe_sourcevalue_insertion.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_endedomain_or_nonidentityrhoe_sourcevalue_insertion.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_endedomain_or_nonidentityrhoe_sourcevalue_insertion_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_endedomain_or_nonidentityrhoe_sourcevalue_insertion_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_EndEDomain_or_NonidentityRhoE_SourceValue_Insertion_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEVALUE_INSERTION_FINITE_RHOE_IMPORTED_ORIENTED_FUNCTOR_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_FiniteRhoE_to_OrientedBN_Functor_or_SmoothRepresentative_v1"


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
    packet = load(PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    typed = packet["lane_typed_EndE"]
    projective = packet["lane_projective_rhoE"]
    transfer = packet["oriented_transfer_tests"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("finite projective value inserted", decision["finite_projective_rhoE_source_value_inserted"] is True and projective["source_value_inserted"] is True, projective)
    check("nonidentity finite data present", projective["nonidentity_central_twist"] is True and projective["tau_values"]["F1"] == 1 and projective["trace_normalization"], projective)
    check("typed lane remains open", decision["typed_EndE_domain_inserted"] is False and typed["source_value_inserted"] is False, typed)
    check("oriented transfer remains open", transfer["rho_shadow_available"] is True and transfer["D_E_intertwines_with_oriented_BN"] is False and transfer["finitepart_matches_oriented_BN"] is False, transfer)
    check("no oriented closure", decision["oriented_BN_carrier_emission_closed"] is False and decision["EndE_or_rhoE_to_oriented_BN_functor_closed"] is False, decision)
    check("no logdet promotion", decision["finitepart_trace_identity_closed"] is False and decision["oriented_logdet_promoted"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records packet", str(PACKET.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin EndE/nonidentity-rhoE source-value insertion audit passed")


if __name__ == "__main__":
    main()
