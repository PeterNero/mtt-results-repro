"""Audit oriented Phi_fin oriented-BN carrier / EndE quotient-functor attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor.candidate.json"
ATTEMPT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor_attempt.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_OrientedBN_CarrierEmission_or_EndEQuotientFunctor_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_ORIENTEDBN_CARRIER_FUNCTOR_ATTEMPT_RHOSHADOW_ONLY"
NEXT = "Selected_Heterotic_OrientedPhiFin_EndEDomain_or_NonidentityRhoE_SourceValue_Insertion_v1"


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
    attempt = load(ATTEMPT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    rho = attempt["rho_shadow_support"]
    tests = attempt["operator_functor_tests"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("rho shadow retained", all(rho.values()) and decision["rho_shadow_embedding_retained"] is True, rho)
    check("typed/projective values absent", tests["typed_cech_EndE_domain_basis_emitted"] is False and tests["projective_twisted_nonidentity_rhoE_emitted"] is False, tests)
    check("no operator functor", tests["DE_intertwines"] is False and tests["same_finitepart"] is False, tests)
    check("carrier/functor open", attempt["can_emit_oriented_BN_carrier_from_heterotic_source"] is False and attempt["can_promote_EndE_to_oriented_BN_functor"] is False, attempt)
    check("decision no closure", decision["oriented_BN_carrier_emission_closed"] is False and decision["EndE_or_rhoE_to_oriented_BN_functor_closed"] is False, decision)
    check("no finitepart promotion", decision["finitepart_identity_closed"] is False and decision["oriented_logdet_promoted"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records attempt", str(ATTEMPT.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin oriented-BN carrier/functor audit passed")


if __name__ == "__main__":
    main()
