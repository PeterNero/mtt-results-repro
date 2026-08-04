"""Audit the Qa/SU3 c-twist Deligne/Cech template."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "ctwist_deligne_cech_template_certificate.json"
DATA = REPO / "candidate_data" / "ctwist_deligne_cech_template.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_CTwist_Deligne_Cech_Template_v1.md"
SCRIPT = REPO / "scripts" / "build_ctwist_deligne_cech_template.py"


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
    modules = data["module_labels"]
    checks = [
        check("status", cert["status"] == "QA_SU3_CTWIST_DELIGNE_CECH_TEMPLATE_BUILT_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("eleven module labels", len(modules) == 11, len(modules)),
        check("T plus exists", any(item["c_twist"] == 1 for item in modules.values()), modules),
        check("T minus exists", any(item["c_twist"] == -1 for item in modules.values()), modules),
        check("P untwisted", modules["P"]["c_twist"] == 0 and modules["P"]["module"] == "ordinary", modules["P"]),
        check(
            "five products pass",
            len(data["product_checks"]) == 5 and all(item["passes_template_typing"] for item in data["product_checks"]),
            data["product_checks"],
        ),
        check(
            "required values open",
            all(value is None for value in data["required_source_values"].values())
            and all(value is False for value in data["promotion_tests"].values()),
            data["required_source_values"],
        ),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifact", cert["next_required_artifact"] in note, NOTE),
    ]
    print("\nSelected Qa/SU3 c-twist Deligne/Cech template audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
