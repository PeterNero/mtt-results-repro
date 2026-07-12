"""Audit the selected Qa/SU3 local-system torsion source extraction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_local_system_torsion_source_extraction_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Local_System_Torsion_Source_Extraction_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_local_system_torsion_source_extraction.py"


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
    verdict = cert["verdict"]
    candidates = {item["candidate"]: item for item in cert["candidate_extraction"]}

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_LOCAL_SYSTEM_TORSION_SOURCE_EXTRACTION_UNDERDETERMINED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["candidate_extraction"] == cert["candidate_extraction"]
            and computed["blocked_formula"] == cert["blocked_formula"],
            computed["verdict"],
        ),
        check(
            "no selected candidate found",
            cert["selected_candidates_count"] == 0
            and verdict["local_system_character_selected"] is False,
            cert["selected_candidates_count"],
        ),
        check(
            "p nonzero acyclicity carried forward",
            cert["carried_forward_selected_data"]["pnonzero_physical_rule"][
                "nonzero_central_hodge_complex_acyclic"
            ]
            is True,
            cert["carried_forward_selected_data"]["pnonzero_physical_rule"],
        ),
        check(
            "q64 import blocked without bridge",
            candidates["z64_q64_15_character_channel"]["selected_for_Qa_SU3_torsion"] is False
            and "bridge theorem" in candidates["z64_q64_15_character_channel"]["reason"],
            candidates["z64_q64_15_character_channel"],
        ),
        check(
            "central tower not mistaken for local system",
            candidates["compact_nil_p_nonzero_central_momentum_tower"][
                "selected_for_Qa_SU3_torsion"
            ]
            is False
            and candidates["compact_nil_p_nonzero_central_momentum_tower"]["known_data"][
                "acyclic"
            ]
            is True,
            candidates["compact_nil_p_nonzero_central_momentum_tower"],
        ),
        check(
            "torsion formula refuses to compute",
            cert["blocked_formula"]["can_evaluate_now"] is False
            and "selected lattice/local-system character"
            in cert["blocked_formula"]["missing_terms"],
            cert["blocked_formula"],
        ),
        check(
            "negative result is scoped",
            cert["negative_result"]["not_a_mathematical_no_go"] is True
            and verdict["torsion_route_retired"] is False,
            cert["negative_result"],
        ),
        check(
            "forbidden shortcuts recorded",
            "observed Qa/SU3 residual to choose a lattice character" in cert["do_not_use"]
            and "compact Nil scalar zeta finite part as analytic torsion" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "note records underdetermination",
            "torsion route underdetermined under current corpus: yes" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 local-system torsion source extraction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
