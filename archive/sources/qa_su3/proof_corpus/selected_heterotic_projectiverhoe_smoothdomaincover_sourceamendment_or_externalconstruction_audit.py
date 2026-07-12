"""Audit the smooth domain/cover source-amendment or external-construction gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothdomaincover_sourceamendment_or_externalconstruction.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceamendment_or_externalconstruction.candidate.json"
CANDIDATES = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothdomaincover_external_construction_candidates.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceamendment_or_externalconstruction_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothDomainCover_SourceAmendment_or_ExternalConstruction_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHDOMAINCOVER_EXTERNAL_CONSTRUCTION_CANDIDATES_BUILT_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FiniteGoodCoverNerve_IncidenceCandidate_v1"


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
    candidates = load(CANDIDATES)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    rows = candidates["construction_candidates"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and candidates["status"] == "CANDIDATES_BUILT_SELECTION_OPEN", (data["status"], cert["status"], candidates["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("four candidates", decision["candidate_count"] == 4 and len(rows) == 4, rows)
    check("selected next finite nerve", decision["selected_next_candidate"] == "A_finite_good_cover_nerve" and candidates["selected_next_candidate"] == "A_finite_good_cover_nerve", candidates)
    check("finite nerve buildable only", rows[0]["buildable_now"] is True and all(row["buildable_now"] is False for row in rows[1:]), rows)
    check("none closes S1", decision["any_candidate_closes_S1_now"] is False and all(row["closes_S1_now"] is False for row in rows), rows)
    check("finite labels carried", len(candidates["finite_labels"]) == 11, candidates["finite_labels"])
    check("external clues carried", candidates["phifin_external_clue_status"] == "U1Y_ROUTEC_PHIFIN_EXTERNAL_CLUES_BUILT_NO_PROOF_IMPORT", candidates["phifin_external_clue_status"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records triage", NEXT in note and str(CANDIDATES.relative_to(ROOT)) in note and "will not close" in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth domain/cover external-construction audit")


if __name__ == "__main__":
    main()
