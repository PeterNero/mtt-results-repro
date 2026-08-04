"""Audit the selected Qa/SU3 VAlpha/S3 mod-3 compatibility import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_valpha_s3_mod3_compatibility_import_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_valpha_s3_integral_lift_or_physical_quotient.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_VAlpha_S3_Mod3_Compatibility_Import_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_valpha_s3_mod3_compatibility.py"


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
    finite = cert["finite_compatibility"]
    limit = cert["valpha_mod3_limit"]
    not_closed = cert["not_closed"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_VALPHA_S3_MOD3_COMPATIBILITY_IMPORTED_INTEGRAL_LIFT_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["finite_compatibility"] == finite
            and computed["valpha_mod3_limit"] == limit
            and computed["not_closed"] == not_closed,
            computed["status"],
        ),
        check(
            "finite compatibility imported",
            closed["finite_active_qutrit_quotient_compatible_with_valpha_blocks"]
            is True
            and closed["selected_s3_commutator_is_nondegenerate_mod3"] is True
            and closed["selected_s3_pullback_table_is_bilinear"] is True
            and closed["s3_commutator_gl2_equivalent_to_valpha_g1g2"] is True
            and closed["s3_commutator_gl2_equivalent_to_valpha_g3g4"] is True,
            closed,
        ),
        check(
            "finite table shape",
            finite["active_quotient"] == "F_3^2"
            and finite["entry_count"] == 81
            and finite["commutator_determinant_mod3"] == 1
            and finite["gl2_transform_count_g1g2"] == 24
            and finite["gl2_transform_count_g3g4"] == 24
            and finite["direct_matrix_equality_g1g2"] is False
            and finite["direct_matrix_equality_g3g4"] is False,
            finite,
        ),
        check(
            "mod3 limitation explicit",
            limit["blocks_equal_mod3"] is True
            and limit["cannot_distinguish_integral_base_order_from_mod3_data"]
            is True,
            limit,
        ),
        check(
            "integral gate remains open",
            not_closed["same_source_valpha_s3_binding"] is True
            and not_closed["integral_ordered_L3_K2_source_selection"] is True
            and not_closed["base_factor_order_selection"] is True
            and not_closed["Pic0_selection_or_quotient"] is True
            and not_closed["selected_D_E_dotD_Riesz_Green"] is True
            and not_closed["full_SM_closure"] is True,
            not_closed,
        ),
        check(
            "template names next required object",
            template["schema"]
            == "SelectedQaSU3VAlphaS3IntegralLiftOrPhysicalQuotient.v1"
            and template["must_supply"][
                "typed_cech_or_appell_humbert_transition_data"
            ]
            is None
            and "Do not treat GL(2,F3) equivalence as integral equality."
            in template["forbidden_shortcuts"],
            template["schema"],
        ),
        check(
            "no overclaim",
            cert["guardrails"]["claims_integral_source_selection"] is False
            and cert["guardrails"]["claims_same_source_binding"] is False
            and cert["guardrails"]["claims_pic0_resolved"] is False
            and cert["guardrails"]["claims_full_SM_closure"] is False,
            cert["guardrails"],
        ),
        check(
            "note records reduction",
            "F_3^2" in note
            and "GL(2,F3)" in note
            and "Integral lift or physical quotient" in note
            and "does not prove same-source binding" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 VAlpha/S3 mod-3 compatibility import audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
