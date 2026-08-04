"""Audit the selected Qa/SU3 m=1 S3 source-origin ladder import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_m1_s3_source_origin_ladder_certificate.json"
TEMPLATE = (
    REPO
    / "certificates"
    / "selected_qa_su3_m1_spectral_projector_de_dotd_source.template.json"
)
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_M1_S3_Source_Origin_Ladder_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_m1_s3_source_origin_ladder.py"


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

    closed = cert["closed_now"]
    not_closed = cert["not_closed"]
    attempts = cert["earlier_attempts_that_correctly_refused_promotion"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_M1_S3_SOURCE_ORIGIN_LADDER_IMPORTED_SPECTRAL_DE_DOTD_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["not_closed"] == not_closed
            and computed["guardrails"] == guardrails,
            computed["status"],
        ),
        check(
            "S3 twisted source pieces are closed",
            closed["finite_S3_CP_source_class_matches_q79_m1_twist"] is True
            and closed[
                "finite_rank_two_S3_DD_obstruction_cancellable_by_twisted_CP"
            ]
            is True
            and closed["selected_S3_flat_Deligne_class"] is True
            and closed["selected_S3_pullback_restriction_table"] is True
            and closed["smooth_S3_twisted_Freed_Witten_cancellation"] is True
            and closed[
                "block_factorized_family_Higgs_projector_retention_for_this_source"
            ]
            is True
            and closed["class_restriction_validator_passed"] is True,
            closed,
        ),
        check(
            "earlier attempts refused promotion before closure",
            attempts["smooth_source_lift_attempt_refused_until_selected_cover_and_projectors"]
            is True
            and attempts[
                "class_restriction_attempt_refused_until_smooth_class_and_projectors"
            ]
            is True
            and attempts[
                "later_closure_supplies_the_missing_smooth_class_restriction_and_block_projectors"
            ]
            is True,
            attempts,
        ),
        check(
            "spectral/operator source remains open",
            not_closed["coherent_spectral_zero_mode_projector_retention"] is True
            and not_closed["selected_D_E_dotD_Riesz_Green"] is True
            and not_closed["selected_visible_Green_Schwarz_operator_source"] is True
            and not_closed["primitive_C1_contractions"] is True
            and not_closed["full_SM_closure"] is True,
            not_closed,
        ),
        check(
            "template targets the remaining true gate",
            template["schema"] == "SelectedQaSU3M1SpectralProjectorDEDotDSource.v1"
            and template["must_supply"][
                "coherent_spectral_zero_mode_projector_retention"
            ]
            is None
            and template["must_supply"]["selected_D_E_files"] is None
            and "Do not equate block-factorized projectors with coherent spectral zero-mode projectors."
            in template["forbidden_shortcuts"],
            template,
        ),
        check(
            "no overclaim",
            guardrails["claims_coherent_spectral_zero_mode_projectors"] is False
            and guardrails["claims_selected_D_E_dotD_constructed"] is False
            and guardrails["claims_visible_operator_source_constructed"] is False
            and guardrails["claims_full_SM_closure"] is False
            and guardrails["uses_observed_flavor_data"] is False,
            guardrails,
        ),
        check(
            "note records the split source-origin frontier",
            "selected smooth S3 flat Deligne class: closed" in note
            and "coherent spectral zero-mode projector retention" in note
            and "block-sector family/Higgs projector retention is not being treated as the" in note
            and "D_E/dotD" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 m=1 S3 source-origin ladder audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
