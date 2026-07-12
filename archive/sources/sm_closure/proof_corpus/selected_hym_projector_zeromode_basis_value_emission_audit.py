"""Audit finite HYM-projector zero-mode value emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_hym_projector_zeromode_basis_value_emission.py"
CANDIDATE = ROOT / "candidate_data" / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
CERT = ROOT / "certificates" / "selected_hym_projector_zeromode_basis_value_emission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HYM_Projector_ZeroModeBasis_Value_Emission_v1.md"

STATUS = "MTT_SELECTED_HYM_PROJECTOR_ZEROMODE_VALUES_EMITTED_MODEL_ACTIVE_NOT_SELECTED"
NEXT = "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1"


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
    payload = data["finite_value_payload"]
    validator = data["validator_result"]
    closes = data["what_closes_now"]
    open_items = data["what_remains_open"]
    superset = data["superset_strategy"]
    flags = validator["selected_source_flags"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "finite projectors emitted",
            validator["finite_projector_values_emitted"] is True
            and cert["finite_projector_values_emitted"] is True
            and payload["ambient_dimension"] == 27
            and payload["zero_cluster"]["dimension"] == 3
            and payload["complement_gap"] > 0,
            payload,
        ),
        check(
            "projector and basis checks pass",
            validator["all_projector_checks_pass"] is True
            and validator["all_basis_counts_pass"] is True
            and validator["positive_complement_gap"] is True
            and validator["green_and_horizontal_flags_pass"] is True,
            validator,
        ),
        check(
            "End0 equivariance on emitted projectors",
            validator["End0_equivariance_on_emitted_projectors"] is True
            and closes["End0_equivariance_on_emitted_projectors_verified"] is True,
            validator,
        ),
        check(
            "matter and Higgs ranks",
            all(payload["sector_slots"][sector]["expected_rank"] == 3 for sector in ["Q", "u", "d", "L", "e", "N"])
            and payload["sector_slots"]["H"]["expected_rank"] == 1
            and payload["sector_slots"]["Q"]["projector_checks"]["rank_trace"] == 3
            and payload["sector_slots"]["H"]["projector_checks"]["rank_trace"] == 1,
            payload["sector_slots"],
        ),
        check(
            "source promotion still blocked",
            flags["de_action_selected_source_verified"] is False
            and flags["dotd_selected_dotD_source_verified"] is False
            and flags["dotd_alpha1_driver_verified"] is False
            and flags["de_honest_validator_promotes"] is False
            and flags["dotd_honest_validator_promotes"] is False
            and validator["selected_HYM_projector_values_promoted"] is False
            and validator["rho_candidate_promoted_to_selected_rho_s"] is False,
            flags,
        ),
        check(
            "bridge import honest",
            data["bridge_import"]["bridge_theorem_proved"] is True
            and data["bridge_import"]["bridge_requires_selected_values"] is True
            and validator["passes_bridge_validator_now"] is False,
            data["bridge_import"],
        ),
        check(
            "superset not used as selector",
            superset["classification"] == "SUPERSET_VALUE_EXTRACTION_WITH_SOURCE_PROMOTION_BLOCKED"
            and superset["uses_observed_constants"] is False
            and "not used to select these projector values" in superset["SU5_E6_q79_theta_path"]["status"],
            superset,
        ),
        check(
            "remaining frontier",
            open_items["selected_HYM_projector_source_promotion"] is True
            and open_items["full_selected_iwasawa_strominger_operator_values"] is True
            and data["next_required_artifact"] == NEXT,
            open_items,
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
            "note records boundary",
            "finite `rho_candidate -> K_s` formula is ready" in note
            and "Does Not Promote `rho_s`" in note
            and "selected_source_verified = false" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected HYM projector zero-mode value emission audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
