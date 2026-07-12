"""Audit BN27 source identity direct theorem or external connection construction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction.candidate.json"
ROOTS = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceidentity_minimal_root_cutset.json"
EXTERNAL = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_connectionvalues_externalconstruction_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SourceIdentity_DirectSourceTheorem_or_ConnectionValuesExternalConstruction_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEIDENTITY_DIRECTSOURCE_OR_EXTERNALCONSTRUCTION_ROOTCUTSET_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SelectedTraceEquality_FullOperatorFormula_or_SourceFlagTheorem_v1"


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
    roots = load(ROOTS)
    external = load(EXTERNAL)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("support already closed", all(roots["already_closed_as_support"].values()), roots["already_closed_as_support"])
    check("minimal roots present", set(roots["minimal_roots"].keys()) == {
        "selected_trace_equality_to_27mode_operator",
        "full_selected_iwasawa_strominger_operator_formula",
        "theorem_derived_selected_source_flags",
        "source_object_named_S_QaSU3_BN27",
    }, roots["minimal_roots"])
    check("minimal roots remain open", all(item["current_status"] is False for item in roots["minimal_roots"].values()), roots["minimal_roots"])
    check("common cutset includes source flags", "theorem_derived_selected_source_flags" in roots["common_cutset_with_electroweak_qastack"] and "selected_trace_equality" in roots["common_cutset_with_electroweak_qastack"], roots["common_cutset_with_electroweak_qastack"])
    check("external request has routes", set(external["external_connection_values_route"].keys()) == {"typed_cech", "direct_hym_or_strominger", "finite_routec_solve", "acceptance_fields"}, external["external_connection_values_route"])
    check("no closure", decision["BN27_source_identity_closed"] is False and decision["all_minimal_roots_closed"] is False and data["closure_claimed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records outputs", NEXT in note and str(ROOTS.relative_to(ROOT)) in note and str(EXTERNAL.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 source-identity direct theorem / external construction audit passed")


if __name__ == "__main__":
    main()
