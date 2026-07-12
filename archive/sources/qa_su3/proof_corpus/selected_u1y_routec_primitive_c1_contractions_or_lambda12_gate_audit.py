"""Audit the post-alpha primitive C1 / lambda12 gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1.md"

STATUS = "U1Y_ROUTEC_PRIMITIVE_C1_LAMBDA12_GATE_POST_ALPHA_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    prefix = data["post_alpha_prefix"]
    primitive = data["primitive_status"]
    lam = data["lambda12_status"]
    guards = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("post alpha prefix closed", cert["alpha1_and_honest_dotD_prefix_closed"] is True and all(value is True for key, value in prefix.items() if isinstance(value, bool)), prefix),
        check("primitive remains open", cert["primitive_C1_contractions_closed"] is False and primitive["missing_atom_count"] == 24 and primitive["all_primitive_atoms_emitted"] is False, primitive),
        check("four sectors six atoms", set(data["atom_table"]) == {"u", "d", "e", "nuD"} and all(len(row["missing_terms"]) == 6 for row in data["atom_table"].values()), data["atom_table"]),
        check("A and b open", cert["A_selected_emitted"] is False and cert["b_selected_emitted"] is False, cert),
        check("lambda open", cert["lambda_12_closed"] is False and cert["lambda_12_computable"] is False and lam["electroweak_lane_A_lambda12_closed"] is False, lam),
        check("guardrails hold", guards["claims_lambda12"] is False and guards["uses_diagnostic_lambda12_values"] is False and data["target_fitting_used"] is False, guards),
        check("note records boundary", "Do not treat closed `alpha1`" in note and "selected lambda12 spectral table" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C primitive C1 / lambda12 post-alpha audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
