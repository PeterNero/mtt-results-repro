"""Audit bundle-A source selector or BN27 source declaration normal form."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bundleA_sourceselector_or_bn27_sourcedeclaration.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bundleA_sourceselector_or_bn27_sourcedeclaration.candidate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.template.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bundleA_sourceselector_or_bn27_sourcedeclaration_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BundleA_SourceSelector_or_BN27_SourceDeclaration_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BUNDLEA_SOURCESELECTOR_OR_BN27_SOURCEDECLARATION_NORMAL_FORM_BUILT_DIRECT_DECLARATION_MINIMAL_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectBN27_SourceDeclaration_Fill_or_BundleA_SourceSelector_Proof_v1"


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
    template = load(TEMPLATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    direct = data["normal_form"]["direct_BN27_source_declaration"]
    smooth = data["normal_form"]["smooth_bundle_A_selector"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("direct ranked minimal", direct["rank"] == 1 and direct["minimal_amendment"] is True and decision["minimal_next_route"] == "direct_BN27_source_declaration", direct)
    check("direct still open", direct["closed_now"] is False and decision["direct_BN27_source_declaration_closed"] is False, decision)
    check("direct carries computable support", direct["already_computable_after_declaration"]["basis_dimension"] == 27 and direct["already_computable_after_declaration"]["commutation_closed"] is True, direct)
    check("smooth larger and open", smooth["rank"] == 2 and smooth["closed_now"] is False and smooth["support"]["standard_embedding_selected_now"] is False, smooth)
    check("template open null fields", template["status"] == "OPEN_SOURCE_DECLARATION_REQUIRED" and template["source_certificate"]["same_selected_source_as_heterotic_QaSU3_threshold_branch"] is None and template["domain"]["F3xF3_rank_slot_deck_action_source_owned"] is None, template)
    check("template keeps no closure", template["finitepart"]["oriented_logdet_promoted"] is None and decision["oriented_logdet_promoted"] is False, template["finitepart"])
    check("no closures", decision["bundle_A_source_selector_closed"] is False and decision["oriented_threshold_closed"] is False and data["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records template", NEXT in note and str(TEMPLATE.relative_to(ROOT)) in note and "minimal_next_route = direct_BN27_source_declaration" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin bundle-A source selector or BN27 source declaration audit passed")


if __name__ == "__main__":
    main()
