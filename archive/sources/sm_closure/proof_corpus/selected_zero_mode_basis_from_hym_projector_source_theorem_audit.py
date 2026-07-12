"""Audit the selected zero-mode basis from HYM projector theorem reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_zero_mode_basis_from_hym_projector_source_theorem.py"
CANDIDATE = ROOT / "candidate_data" / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"
CERT = ROOT / "certificates" / "selected_zero_mode_basis_from_hym_projector_source_theorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_ZEROMODE_BASIS_HYM_PROJECTOR_THEOREM_REDUCED_VALUES_OPEN"
NEXT = "MTT_Selected_HYM_Projector_ZeroModeBasis_Value_Emission_v1"


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
    theorem = data["theorem"]
    validator = data["finite_acceptance_validator"]
    blockers = data["current_blockers"]
    support = data["current_support"]
    superset = data["superset_strategy"]
    decision = data["promotion_decision"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "bridge theorem proved but values open",
            theorem["bridge_theorem_proved"] is True
            and theorem["selected_values_emitted"] is False
            and cert["bridge_theorem_proved"] is True
            and cert["selected_projector_values_emitted"] is False,
            theorem,
        ),
        check(
            "current support imported",
            support["canonical_rho_candidate_constructed"] is True
            and support["selected_End0_basis_available"] is True
            and support["same_T3_lane_matches_rho_candidate"] is True
            and support["full_diagonal_End0_Riesz_Green_closed"] is True
            and support["representation_choice_conditionally_closed"] is True,
            support,
        ),
        check(
            "projector values still block promotion",
            blockers["selected_zero_mode_bases_emitted"] is False
            and blockers["coherent_spectral_projector_retention"] is False
            and blockers["zero_mode_slot_values_filled"] is False
            and blockers["selected_HYM_operator_source_verified"] is False,
            blockers,
        ),
        check(
            "finite acceptance validator locked",
            validator["passes_now"] is False
            and len(validator["required_slots"]) == 7
            and validator["required_slots"]["Q"]["required_rank"] == 3
            and validator["required_slots"]["H"]["required_rank"] == 1
            and "End0-equivariance holds for T1,T2,T3 on every retained matter carrier"
            in validator["global_required_checks"],
            validator,
        ),
        check(
            "promotion decision honest",
            decision["bridge_theorem_closes"] is True
            and decision["canonical_rho_candidate_promotes_now"] is False
            and decision["promotes_after_next_artifact_if_validator_passes"] is True
            and decision["next_required_artifact"] == NEXT,
            decision,
        ),
        check(
            "superset roles constrained",
            superset["classification"] == "SUPERSET_CONSTRAINED_BRIDGE_NOT_MULTI_SOURCE_PROOF"
            and superset["straight_End0_path"]["role"].startswith("supplies")
            and "cannot promote rho_s" in superset["SU5_E6_q79_theta_path"]["proof_status"]
            and superset["uses_observed_constants"] is False,
            superset,
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
            "note records theorem and boundary",
            "promotes uniquely to the selected physical sector source map `rho_s`" in note
            and "We are using a constrained superset strategy" in note
            and "coherent_spectral_projector_retention = false" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected zero-mode basis from HYM projector theorem audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
