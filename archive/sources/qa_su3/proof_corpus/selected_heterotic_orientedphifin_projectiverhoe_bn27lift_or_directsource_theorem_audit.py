"""Audit projective rho_E -> BN27 lift or direct source theorem attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_projectiverhoe_bn27lift_or_directsource_theorem.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_or_directsource_theorem.candidate.json"
NOGO = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_nogo_report.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_or_directsource_theorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_ProjectiveRhoE_BN27Lift_or_DirectSourceTheorem_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_PROJECTIVERHOE_BN27LIFT_NOGO_DIRECTSOURCE_REQUIRED"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectBN27SourceTheorem_or_SmoothEQaQuotient_v1"


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
    nogo = load(NOGO)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    tests = data["lift_tests"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("orientation shadow passes only", tests["domain_lift"]["orientation_shadow_passes"] is True and tests["domain_lift"]["passes"] is False, tests["domain_lift"])
    check("missing positive rows exact", tests["domain_lift"]["missing_positive_oriented_row_count"] == 10 and tests["domain_lift"]["missing_multiplier_to_full_abs_sector"] == 5760000, tests["domain_lift"])
    check("operator lift fails", tests["operator_lift"]["C_tau_orientation_intertwiner_passes"] is True and tests["operator_lift"]["PhiFin_DE_intertwiner_passes"] is False and tests["operator_lift"]["finitepart_matches"] is False, tests["operator_lift"])
    check("source identity fails", tests["source_identity"]["passes"] is False and tests["source_identity"]["direct_source_theorem_emitted"] is False, tests["source_identity"])
    check("audit replay conditional", tests["audit_replay"]["passes"] is False and tests["audit_replay"]["would_pass_if_direct_source_or_lift_passed"] is True, tests["audit_replay"])
    check("no-go report", nogo["status"] == "PROJECTIVE_RHOE_BN27_LIFT_FAILS_CURRENT_SOURCE" and set(nogo["legal_exits"]) == {"direct_BN27_source_theorem", "smooth_EQa_quotient"}, nogo)
    check("no closures", not any(decision[key] for key in ["domain_lift_closed", "operator_lift_closed", "source_identity_closed", "projective_rhoE_BN27_lift_closed", "direct_source_theorem_closed"]), decision)
    check("no export closure", decision["selected_connection_witness_export_closed"] is False and cert["selected_connection_witness_export_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records no-go", NEXT in note and str(NOGO.relative_to(ROOT)) in note and "projective_rhoE_BN27_lift_closed = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin projective rho_E BN27 lift audit passed")


if __name__ == "__main__":
    main()
