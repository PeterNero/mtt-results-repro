"""Audit the U1/Y Route-C Phi_fin external clue synthesis."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_u1y_routec_phifin_external_clues_certificate.json"
DATA = REPO / "candidate_data" / "selected_u1y_routec_phifin_external_clues.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_PhiFin_External_Clues_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_phifin_external_clues.py"

STATUS = "U1Y_ROUTEC_PHIFIN_EXTERNAL_CLUES_BUILT_NO_PROOF_IMPORT"
NEXT = "Selected_U1Y_RouteC_FiniteEmissionMorphism_PhiFin_Subpacket_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    stages = cert["construction_stages"]
    anchors = data["external_anchors"]
    guardrails = data["guardrails"]
    computed_paths = [line for line in proc.stdout.splitlines() if line.startswith("wrote ")]
    checks = [
        check("status", cert["status"] == STATUS and data["status"] == STATUS, cert["status"]),
        check("script reruns", len(computed_paths) == 3, proc.stdout),
        check("next artifact", cert["next_required_artifact"] == NEXT and data["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("external anchor coverage", len(anchors) >= 6 and cert["external_anchor_count"] == len(anchors), len(anchors)),
        check("balanced clues present", any(anchor["container"] == "balanced_bergman_hym" for anchor in anchors), anchors),
        check("FEEC/Galerkin clues present", any(anchor["container"] == "commuting_galerkin_projection" for anchor in anchors) and any(anchor["container"] == "spectral_gap_riesz_green" for anchor in anchors), anchors),
        check("Strominger/Fu-Yau clues present", sum(1 for anchor in anchors if anchor["container"] == "smooth_strominger_source") >= 2, anchors),
        check("five construction stages", stages == ["domain_lock", "finite_basis", "projection_commuting_square", "finite_operator_payload", "error_gap_certificate"], stages),
        check("acceptance contract imported", data["local_contract"]["name"] == "Phi_fin" and "selected_source_verified becomes a theorem-derived field, not a lifted flag" in data["local_contract"]["acceptance_tests"], data["local_contract"]),
        check("honest no closure", data["closure_claimed"] is False and cert["Phi_fin_closed"] is False and cert["lambda_12_closed"] is False and data["what_closes_now"]["Phi_fin"] is False, cert),
        check("target fitting excluded", data["target_fitting_used"] is False and guardrails["uses_observed_data"] is False and guardrails["uses_benchmark_data"] is False, guardrails),
        check("note records external guardrail", "External sources are container evidence only" in note and "Do not use observed masses" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C Phi_fin external clues audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
