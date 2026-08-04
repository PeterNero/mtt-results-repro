"""Audit the Iwasawa abelian-row to nonabelian SU3 source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "iwasawa_abelian_row_to_nonabelian_source_gate_certificate.json"
DATA = REPO / "candidate_data" / "iwasawa_abelian_row_to_nonabelian_source_gate.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Iwasawa_Abelian_Row_to_Nonabelian_Source_Gate_v1.md"
SCRIPT = REPO / "scripts" / "build_iwasawa_abelian_row_to_nonabelian_source_gate.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def by_id(data: dict[str, object], row_id: str) -> dict[str, object]:
    return next(row for row in data["promotion_tests"] if row["id"] == row_id)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    result = data["result"]
    split = by_id(data, "diagonal_det_one_embedding")
    extension = by_id(data, "non_split_extension_promotion")
    checks = [
        check("status", cert["status"] == "QA_SU3_IWASAWA_ABELIAN_ROW_TO_NONABELIAN_SOURCE_GATE_BUILT_PROMOTION_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("four promotion tests", len(data["promotion_tests"]) == 4, [row["id"] for row in data["promotion_tests"]]),
        check("split rejected", split["passes"]["determinant_one_topology"] is True and split["passes"]["nonabelian_su3_structure_group"] is False, split),
        check("extension best live", data["best_live_route"]["id"] == "non_split_extension_promotion" and extension["decision"] == "BEST_LIVE_PROMOTION_ROUTE_VALUES_OPEN", extension),
        check("values open", extension["passes"]["selected_extension_class_present"] is False and extension["passes"]["selected_transition_matrices"] is False, extension),
        check("result guarded", result["abelian_row_embeds_det_one_topology"] is True and result["abelian_row_is_selected_nonabelian_source"] is False, result),
        check("no determinant", result["determinant_computable_now"] is False and result["qa_su3_closed"] is False, result),
        check("note records next", cert["next_required_artifact"] in note and "non-split extension" in note, NOTE),
        check("no fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
    ]
    print("\nSelected Qa/SU3 Iwasawa abelian row to nonabelian source gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
