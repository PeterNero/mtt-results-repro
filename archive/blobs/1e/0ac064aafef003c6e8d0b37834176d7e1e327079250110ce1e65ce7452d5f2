"""Audit the primitive C1 atom emission interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_primitive_c1_atom_emission_interface.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_emission_interface.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_primitive_c1_atom_emission_interface_certificate.json"
TEMPLATE = REPO / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload.template.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Primitive_C1_Atom_Emission_Interface_v1.md"

STATUS = "U1Y_ROUTEC_PRIMITIVE_C1_ATOM_EMISSION_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_AtomPayload_Fill_or_NoGo_v1"
SECTORS = {"u", "d", "e", "nuD"}
TERMS = {
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
}


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def matrix_is_open_3x3(matrix: object) -> bool:
    return (
        isinstance(matrix, list)
        and len(matrix) == 3
        and all(isinstance(row, list) and len(row) == 3 and all(value is None for value in row) for row in matrix)
    )


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
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    guards = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("assembly theorem only", cert["assembly_theorem_proved"] is True and cert["primitive_C1_atoms_emitted"] is False, cert),
        check("sector order", set(data["sector_order"]) == SECTORS and set(template["sectors"]) == SECTORS, data["sector_order"]),
        check("term order", set(data["term_order"]) == TERMS, data["term_order"]),
        check(
            "template contains 24 open 3x3 atoms",
            sum(matrix_is_open_3x3(template["sectors"][sector]["atoms"][term]) for sector in SECTORS for term in TERMS) == 24,
            template["sectors"],
        ),
        check("A and b not computable", cert["A_selected_computable"] is False and cert["b_selected_computable"] is False, cert),
        check("guardrails hold", all(value is False for value in guards.values()) and data["target_fitting_used"] is False, guards),
        check("note records no fitting", "Do not fill atoms from masses" in note and "does not emit" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C primitive C1 atom emission interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
