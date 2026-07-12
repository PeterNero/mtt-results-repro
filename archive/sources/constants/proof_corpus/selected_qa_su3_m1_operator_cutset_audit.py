"""Audit the selected Qa/SU3 m=1 operator cut-set import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_m1_operator_cutset_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_m1_cw_operator_source.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_M1_Operator_Cutset_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_m1_operator_cutset.py"


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
    cut_set = cert["cut_set"]
    branch_status = cert["branch_status"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_M1_OPERATOR_CUTSET_IMPORTED_CW_SOURCE_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["cut_set"] == cut_set
            and computed["branch_status"] == branch_status,
            computed["status"],
        ),
        check(
            "symbolic curvature and branch reachability closed",
            closed["selected_s3_source_support_closed"] is True
            and closed["old_s3_gerbe_fw_projector_blockers_retired"] is True
            and closed["visible_green_schwarz_curvature_row_closed"] is True
            and closed["visible_gs_zero_symbolic_bianchi_residual"] is True
            and closed["finite_q79_and_q369_reach_validator_layer"] is True
            and closed["orientation_reduced_to_conjugate_pair"] is True,
            closed,
        ),
        check(
            "selected operator source remains the cut set",
            cut_set["selected_visible_bundle_or_sheaf_model"] is True
            and cut_set["Chern_Weil_row_derived_from_selected_source"] is True
            and cut_set["HYM_or_Route_C_residual_for_visible_source"] is True
            and cut_set["coherent_spectral_zero_mode_projectors"] is True
            and cut_set["selected_D_E_dotD_Riesz_Green"] is True
            and cut_set["same_branch_dotD_alpha1_driver"] is True
            and cut_set["primitive_C1_contractions"] is True,
            cut_set,
        ),
        check(
            "branch selection remains open",
            len(branch_status["branch_packets"]) == 2
            and branch_status["unique_m1_vs_m2_selection_open"] is True
            and branch_status["subvalidator_exit_codes"]["selected_D_E_action"] == 1
            and branch_status["subvalidator_exit_codes"]["selected_dotD_alpha1"] == 1
            and "same_branch_derivative_verified must be true"
            in branch_status["orientation_attempt_first_open_items"],
            branch_status,
        ),
        check(
            "template targets Chern-Weil/operator source",
            template["schema"] == "SelectedQaSU3M1ChernWeilOperatorSource.v1"
            and template["must_supply"][
                "chern_weil_derivation_of_visible_TrF_row"
            ]
            is None
            and template["must_supply"]["same_branch_dotD_alpha1_response"] is None
            and "Do not treat Green-Schwarz curvature closure as selected operator-source closure."
            in template["forbidden_shortcuts"],
            template,
        ),
        check(
            "no overclaim",
            guardrails["claims_selected_visible_operator_source_constructed"]
            is False
            and guardrails["claims_chern_weil_row_derived_from_selected_bundle"]
            is False
            and guardrails["claims_coherent_spectral_projectors_constructed"]
            is False
            and guardrails["claims_selected_D_E_dotD_constructed"] is False
            and guardrails["uses_observed_flavor_data"] is False,
            guardrails,
        ),
        check(
            "note records the remaining cut set",
            "visible Green-Schwarz curvature row: closed" in note
            and "selected visible Chern-Weil/operator source" in note
            and "q79 and q369 packets form a conjugate pair" in note
            and "retarded boundary condition" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 m=1 operator cut-set audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
