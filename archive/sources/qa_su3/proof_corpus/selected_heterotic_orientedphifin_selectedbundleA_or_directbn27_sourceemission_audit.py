"""Audit selected bundle A or direct BN27 source-emission attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SelectedBundleA_or_DirectBN27_SourceEmission_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SELECTEDBUNDLEA_OR_DIRECTBN27_EMISSION_ATTEMPT_REJECTS_UNSELECTED_SUBSTITUTES"
NEXT = "Selected_Heterotic_OrientedPhiFin_BundleA_SourceSelector_or_BN27_SourceDeclaration_v1"


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
    request = load(REQUEST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    attempts = data["emission_attempts"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("direct BN27 absent", attempts["direct_BN27_source_declaration"]["candidate_available"] is False and attempts["direct_BN27_source_declaration"]["closes"] is False, attempts["direct_BN27_source_declaration"])
    check("standard embedding rejected", attempts["standard_embedding_A_equals_GammaPlus"]["geometric_values_available"] is True and attempts["standard_embedding_A_equals_GammaPlus"]["closes"] is False and decision["standard_embedding_promoted"] is False, attempts["standard_embedding_A_equals_GammaPlus"])
    check("finite rhoE rejected as smooth A", attempts["finite_projective_rhoE_as_smooth_transition"]["orientation_shadow_available"] is True and attempts["finite_projective_rhoE_as_smooth_transition"]["threshold_lift_available"] is False and decision["finite_projective_rhoE_promoted_to_smooth_A"] is False, attempts["finite_projective_rhoE_as_smooth_transition"])
    check("request names selector options", set(request["minimal_selector_options"]) == {"smooth_bundle_A_selector", "direct_BN27_source_declaration"}, request)
    check("no closures", decision["direct_BN27_source_emitted"] is False and decision["selected_bundle_A_emitted"] is False and decision["oriented_threshold_closed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records request", NEXT in note and str(REQUEST.relative_to(ROOT)) in note and "standard_embedding_promoted = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin selected bundle A or direct BN27 source-emission audit passed")


if __name__ == "__main__":
    main()
