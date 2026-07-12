"""Audit the selected Qa/SU3 visible source architecture ranking."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_visible_source_architecture_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_visible_sm_bundle_operator_source.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Visible_Source_Architecture_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_qa_su3_visible_source_architecture.py"


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
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    arch = cert["architectures"]
    rec = cert["recommended_construction"]
    open_items = cert["not_closed"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_VISIBLE_SOURCE_ARCHITECTURE_RANKED_SAME_SOURCE_BINDING_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["architectures"] == arch
            and computed["recommended_construction"] == rec
            and computed["not_closed"] == open_items,
            computed["status"],
        ),
        check(
            "template demands same-source binding",
            template["status"] == "OPEN_SELECTED_QA_SU3_VISIBLE_SM_BUNDLE_OPERATOR_SOURCE_REQUIRED"
            and "rank2_valpha_or_equivalent_visible_bundle_model"
            in template["must_bind_same_source"]
            and "selected_s3_green_schwarz_visible_support"
            in template["must_bind_same_source"],
            template["must_bind_same_source"],
        ),
        check(
            "A has strongest topological support",
            arch["A_rank2_valpha_terminal_monad_primary"]["closed_support"][
                "rank2_topological_c1_c2"
            ]
            is True
            and arch["A_rank2_valpha_terminal_monad_primary"]["closed_support"][
                "conditional_ext_math"
            ]
            is True
            and arch["A_rank2_valpha_terminal_monad_primary"]["closed_support"][
                "terminal_lane_conditional_uniqueness"
            ]
            is True,
            arch["A_rank2_valpha_terminal_monad_primary"],
        ),
        check(
            "B supplies visible support but not operator source",
            arch["B_s3_green_schwarz_visible_support"]["closed_support"][
                "selected_s3_support"
            ]
            is True
            and arch["B_s3_green_schwarz_visible_support"]["open_blockers"][
                "selected_twisted_D_E_dotD"
            ]
            is True,
            arch["B_s3_green_schwarz_visible_support"],
        ),
        check(
            "C is execution engine not source",
            arch["C_direct_hym_routec_solve"]["closed_support"]["finite_pipeline_ready"]
            is True
            and arch["C_direct_hym_routec_solve"]["open_blockers"][
                "selected_D_E_constructed"
            ]
            is True,
            arch["C_direct_hym_routec_solve"],
        ),
        check(
            "recommended path",
            rec["primary"] == "A_rank2_valpha_terminal_monad_primary"
            and rec["required_merge"] == "B_s3_green_schwarz_visible_support"
            and rec["execution_engine"] == "C_direct_hym_routec_solve",
            rec,
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_same_source_binding_proved"] is False
            and cert["guardrails"]["claims_selected_visible_bundle_constructed"] is False
            and cert["guardrails"]["claims_selected_D_E_constructed"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False,
            cert["guardrails"],
        ),
        check(
            "note records next object",
            "Selected_Qa_SU3_Same_Source_VAlpha_S3_Operator_Packet_v1" in note
            and "primary source skeleton: A" in note
            and "required same-source merge: B" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 visible source architecture audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
