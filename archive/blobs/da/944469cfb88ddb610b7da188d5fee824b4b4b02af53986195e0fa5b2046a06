"""Audit the Qa/SU3 Cech/Dolbeault matrix packet scaffold."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "cech_dolbeault_matrix_packet_scaffold_certificate.json"
DATA = REPO / "candidate_data" / "cech_dolbeault_matrix_packet_scaffold.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Cech_Dolbeault_Matrix_Packet_Scaffold_v1.md"
SCRIPT = REPO / "scripts" / "build_cech_dolbeault_matrix_packet_scaffold.py"


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
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    checks = [
        check("status", cert["status"] == "QA_SU3_CECH_DOLBEAULT_MATRIX_PACKET_SCAFFOLD_BUILT_SELECTED_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("eleven spaces", gates["eleven_formal_spaces_indexed"] is True and len(data["formal_basis"]) == 11, data["formal_basis"]),
        check("five products", gates["five_typed_product_blocks_indexed"] is True and len(data["product_blocks"]) == 5, data["product_blocks"]),
        check("all target P", gates["all_products_target_P_by_charge"] is True, data["product_blocks"]),
        check("gf equation", gates["gf_zero_equation_derived"] is True and "mu_1*a_1*b_1" in data["monad_matrix_shape"]["gf_zero_equation"], data["monad_matrix_shape"]),
        check("selected values open", gates["selected_bases_supplied"] is False and gates["selected_f_g_entries_supplied"] is False, gates),
        check("not promoted", gates["matrix_packet_promoted"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records no convenience solve", "Do not choose arbitrary" in note and cert["next_required_artifact"] in note, NOTE),
    ]
    print("\nSelected Qa/SU3 Cech/Dolbeault matrix packet scaffold audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
