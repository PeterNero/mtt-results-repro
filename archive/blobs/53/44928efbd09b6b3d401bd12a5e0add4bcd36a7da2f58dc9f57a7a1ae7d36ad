"""Audit Route A source-promotion attempt for HYM projector values."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_hym_projector_source_promotion_route_a.py"
CANDIDATE = ROOT / "candidate_data" / "selected_hym_projector_source_promotion_route_a.candidate.json"
CERT = ROOT / "certificates" / "selected_hym_projector_source_promotion_route_a_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HYM_Projector_SourcePromotion_Route_A_v1.md"

STATUS = "MTT_SELECTED_HYM_PROJECTOR_SOURCE_PROMOTION_ROUTE_A_REDUCED_TO_PHIFIN_TRACE"
NEXT = "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    gates = data["route_a_gate_matrix"]
    theorem = data["theorem_attempt"]
    flags = data["honest_source_flags"]
    superset = data["superset_strategy"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "selected branch support present",
            gates["A1_selected_topological_branch_fixed"]["passes"] is True
            and gates["A2_strominger_selection_available"]["passes"] is True,
            gates,
        ),
        check(
            "finite value side closed",
            gates["A3_finite_BN_projector_values_clean"]["passes"] is True
            and cert["finite_value_side_closed"] is True
            and data["what_closes_now"]["route_A_finite_value_side_closed"] is True,
            gates["A3_finite_BN_projector_values_clean"],
        ),
        check(
            "Phi_fin trace blocks route A",
            gates["A4_PhiFin_selected_trace_emitted"]["passes"] is False
            and data["validator_status"]["phifin_selected_payload_closed"] is False
            and data["route_a_promotes_now"] is False,
            gates["A4_PhiFin_selected_trace_emitted"],
        ),
        check(
            "honest source flags still false",
            flags["de_action_selected_source_verified"] is False
            and flags["dotd_selected_dotD_source_verified"] is False
            and flags["dotd_alpha1_driver_verified"] is False
            and gates["A5_honest_operator_flags_promote"]["passes"] is False,
            flags,
        ),
        check(
            "full operator equality not proved",
            gates["A6_full_selected_strominger_operator_identified_with_BN_model_active"]["passes"] is False
            and "not prove equality" in gates["A6_full_selected_strominger_operator_identified_with_BN_model_active"]["reason"],
            gates["A6_full_selected_strominger_operator_identified_with_BN_model_active"],
        ),
        check(
            "conditional promotion recorded",
            theorem["conditional_promotion_rule"]["recorded"] is True
            and theorem["proved_now"] is False
            and "Phi_fin emits a selected minimizer trace" in theorem["conditional_promotion_rule"]["condition"],
            theorem,
        ),
        check(
            "superset constrained not selector",
            superset["classification"] == "ROUTE_A_SUPERSET_PROMOTION_ATTEMPT_REDUCED_NOT_CLOSED"
            and superset["uses_observed_constants"] is False
            and "not used to flip source flags" in superset["q79_S3_GS_Theta_SU5_constraints"]["status"],
            superset,
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and data["what_remains_open"]["Phi_fin_selected_minimizer_trace"] is True,
            data["what_remains_open"],
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "note records route A boundary",
            "Current answer: not yet." in note
            and "obstruction is not rank, basis, gap, or equivariance" in note
            and "selected `Phi_fin` trace/equivalence theorem" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected HYM projector source-promotion Route A audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
