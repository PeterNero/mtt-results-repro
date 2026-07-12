"""Audit the primitive C1 atom-payload fill/no-go gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo_certificate.json"
MISSING = REPO / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_missing_leaves.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Primitive_C1_AtomPayload_Fill_or_NoGo_v1.md"

STATUS = "U1Y_ROUTEC_PRIMITIVE_C1_ATOMPAYLOAD_FILL_NOGO_CURRENT_CORPUS_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_SourceValue_Theorem_or_SelectedNonInvariantTensor_v1"


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
    missing = json.loads(MISSING.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    guards = data["guardrails"]
    fill = data["fill_attempt"]
    zero = data["canonical_zero_branch"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("fill no-go", cert["current_corpus_supplies_selected_atom_payload"] is False and fill["open_atom_matrices"] == 24, fill),
        check("canonical zero rejected", zero["all_c1_matrices_zero_for_canonical_tensor"] is True and zero["accepted_as_selected_atom_payload"] is False and cert["canonical_zero_branch_selected"] is False, zero),
        check("missing leaves complete", cert["missing_leaf_count"] == 40 and len(missing["missing_leaves"]) == 40, missing["missing_leaves"][:3]),
        check("A and b not computable", cert["A_selected_computable"] is False and cert["b_selected_computable"] is False, cert),
        check("guardrails hold", all(value is False for value in guards.values()) and data["target_fitting_used"] is False, guards),
        check(
            "note records diagnostic zero boundary",
            "canonical" in note and "remains diagnostic" in note and "Do not promote canonical zero" in note,
            NOTE,
        ),
    ]
    print("\nSelected U1/Y Route-C primitive C1 atom-payload fill/no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
