"""Audit the selected Qa/SU3 non-split Iwasawa monad source construction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_nonsplit_extension_source_construction_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_NonSplit_Extension_Source_Construction_v1.md"
SCRIPT = REPO / "scripts" / "construct_selected_qa_su3_nonsplit_extension_source.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    monad = cert["monad_computation"]
    closed = cert["what_this_closes"]
    open_items = cert["what_remains_open"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_NONSPLIT_IWASAWA_MONAD_SOURCE_FOUND_OPERATOR_PACKET_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["monad_computation"] == cert["monad_computation"]
            and computed["what_remains_open"] == cert["what_remains_open"],
            computed["monad_computation"],
        ),
        check(
            "source file supports monad",
            cert["source_scan"]["present"] is True
            and "monad" in cert["source_scan"]["terms_found"]
            and "SU(3)" in cert["source_scan"]["terms_found"],
            cert["source_scan"],
        ),
        check(
            "Chern character recomputed",
            monad["c1_zero"] is True
            and monad["c2_zero"] is True
            and monad["c3_integral_equals_6"] is True,
            monad,
        ),
        check(
            "source construction progress recorded",
            closed["non_split_rank3_su3_candidate_found_in_corpus"] is True
            and closed["integer_chern_character_recomputed"] is True,
            closed,
        ),
        check(
            "operator packet remains open",
            open_items["qa_su3_threshold_representation_identified"] is False
            and open_items["operator_packet_filled"] is False
            and open_items["endomorphism_E_computed"] is False
            and open_items["qa_su3_closed"] is False,
            open_items,
        ),
        check(
            "guardrails prevent overclaim",
            "Do not claim full Qa/SU3 or SM closure from HYM existence alone." in cert["guardrails"]
            and "Do not replace endomorphism_E by Chern classes alone." in cert["guardrails"],
            cert["guardrails"],
        ),
        check(
            "note records transfer gate",
            "Selected_Qa_SU3_Monad_to_Operator_Packet_Transfer_Gate_v1" in note
            and "Qa/SU3 closed: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 non-split extension source construction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
