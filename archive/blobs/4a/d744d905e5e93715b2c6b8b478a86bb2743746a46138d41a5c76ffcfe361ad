"""Audit direct BN27 source declaration fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector.candidate.json"
FILLED = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.fill_attempt.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_DirectBN27_SourceDeclaration_Fill_or_BundleA_Selector_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTBN27_SOURCEDECLARATION_FILL_SUPPORT_FILLED_SOURCE_OWNERSHIP_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceOwned_BN27_Certificate_or_BundleA_Selector_v1"


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
    filled = load(FILLED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("support filled", decision["support_values_filled"] is True and filled["domain"]["basis_dimension"] == 27 and filled["domain"]["oriented_nonzero_count"] == 16, filled["domain"])
    check("operator support present", filled["operators"]["C_tau_and_PhiFin_DE_commute"] is True and len(filled["operators"]["D_E_diagonal_on_oriented_nonzero_BN"]) == 16 and len(filled["operators"]["positive_spectrum"]) == 16, filled["operators"].keys())
    check("trace support present", filled["finitepart"]["finitepart_trace_identity_relative_to_full_orbit_source"] is True and filled["finitepart"]["oriented_abs_sector_product"] == 92160000 and filled["finitepart"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", filled["finitepart"])
    check("source fields false", all(value is False for value in decision["source_owned_fields"].values()), decision["source_owned_fields"])
    check("closure blocked", decision["direct_BN27_source_declaration_closed"] is False and filled["audit_replay"]["closure_replay_allowed"] is False and data["closure_claimed"] is False, decision)
    check("logdet not promoted", filled["finitepart"]["oriented_logdet_promoted"] is False and decision["oriented_logdet_promoted"] is False, filled["finitepart"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records filled packet", NEXT in note and str(FILLED.relative_to(ROOT)) in note and "support_values_filled = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin direct BN27 source declaration fill audit passed")


if __name__ == "__main__":
    main()
