"""Audit the finite good-cover nerve incidence candidate for smooth rhoE S1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_finitegoodcovernerve_incidencecandidate.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidencecandidate.candidate.json"
NERVE = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidence_table.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidencecandidate_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_FiniteGoodCoverNerve_IncidenceCandidate_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_FINITEGOODCOVERNERVE_INCIDENCE_CANDIDATE_BUILT_EMBEDDING_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_GoodCoverEmbedding_or_DeligneRepresentative_SourceProof_v1"


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
    nerve = load(NERVE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and nerve["status"] == "FINITE_NERVE_INCIDENCE_CANDIDATE_ONLY", (data["status"], cert["status"], nerve["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("three-node nerve", nerve["cover_nodes"] == ["U0", "U1", "U2"] and nerve["nerve_is_two_simplex"] is True, nerve["cover_nodes"])
    check("overlaps nonempty", nerve["all_pair_overlaps_nonempty"] is True and nerve["all_triple_overlaps_nonempty"] is True, (nerve["pair_overlaps"], nerve["triple_overlaps"]))
    check("eleven label shadows", len(nerve["label_shadow"]) == 11 and decision["all_labels_shadow_tau"] is True, nerve["label_shadow"])
    check("formal incidence only", data["closes_request_fields"]["selected_good_cover_index_set"] is True and data["closes_request_fields"]["proof_Z3_shadow_is_induced_by_cover"] is False, data["closes_request_fields"])
    check("smooth embedding fields open", all(value is None for value in nerve["smooth_embedding_fields"].values()), nerve["smooth_embedding_fields"])
    check("still open exact", all(data["still_open"].values()) and "embedding_as_selected_compact_Iwasawa_Nil_good_cover" in data["still_open"], data["still_open"])
    check("does not close S1", decision["closes_S1"] is False and cert["closes_S1"] is False and decision["smooth_good_cover_selected"] is False, decision)
    check("not claimed blocks promotion", "selected compact Iwasawa/Nil good-cover embedding" in nerve["not_claimed"] and "smooth rho_E transition matrices" in nerve["not_claimed"], nerve["not_claimed"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records incidence", NEXT in note and str(NERVE.relative_to(ROOT)) in note and "not a selected compact" in note, NOTE)

    print("\nSelected heterotic projective rho_E finite good-cover nerve incidence candidate audit")


if __name__ == "__main__":
    main()
