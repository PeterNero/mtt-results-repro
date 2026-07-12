"""Audit Route-C sector projectors and dotD on smooth B_N."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
CERT = REPO / "certificates" / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    honest_path = REPO / data["payloads"]["honest_projectors_dotd"]
    diagnostic_path = REPO / data["payloads"]["diagnostic_source_lift"]
    honest = json.loads(honest_path.read_text(encoding="utf-8"))
    diagnostic = json.loads(diagnostic_path.read_text(encoding="utf-8"))
    residuals = data["validation"]["projector_residuals"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_BUILT_SOURCE_PROMOTION_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("payloads exist", honest_path.exists() and diagnostic_path.exists(), data["payloads"]),
        check(
            "honest fails only by source flags",
            data["validation"]["honest_validator_fails_only_by_source_driver_flags"] is True
            and data["validation"]["honest"]["exit_code"] == 1,
            data["validation"]["honest"],
        ),
        check(
            "diagnostic dotD validator passes",
            data["validation"]["diagnostic_lift_validator_passes"] is True
            and data["validation"]["diagnostic_source_lift"]["exit_code"] == 0,
            data["validation"]["diagnostic_source_lift"],
        ),
        check(
            "projectors exact",
            all(
                item["idempotence_residual"] == 0.0
                and item["hermitian_residual"] == 0.0
                for item in residuals.values()
            ),
            residuals,
        ),
        check(
            "sector ranks retained",
            all(residuals[sector]["rank_trace"] == 3.0 for sector in ("Q", "u", "d", "L", "e", "N"))
            and residuals["H"]["rank_trace"] == 1.0,
            residuals,
        ),
        check(
            "honest flags false",
            honest["selected_dotD_source_verified"] is False
            and honest["alpha1_driver_verified"] is False
            and all(
                slot["selected_dotD_source_verified"] is False
                and slot["alpha1_driver_verified"] is False
                for slot in honest["dotd_response_slots"].values()
            ),
            honest["candidate_kind"],
        ),
        check(
            "diagnostic flags true but no physical source claim",
            diagnostic["selected_dotD_source_verified"] is True
            and diagnostic["alpha1_driver_verified"] is True
            and diagnostic["claims_physical_selected_source"] is False,
            diagnostic["candidate_kind"],
        ),
        check(
            "superset classification",
            data["superset_mode"]["classification"] == "CONSTRAINED_NUMERICAL_SUPERSET_REPAIR"
            and data["superset_mode"]["straight_path"]["classification"] == "PARTIAL",
            data["superset_mode"],
        ),
        check("no target fitting", data["target_fitting_used"] is False, data["target_fitting_used"]),
        check("closure not claimed", data["closure_claimed"] is False, data["what_remains_open"]),
        check(
            "remaining gates preserved",
            data["what_remains_open"]["selected_dotD_source_verified"] is True
            and data["what_remains_open"]["alpha1_driver_verified"] is True
            and data["what_remains_open"]["primitive_C1_overlap_contractions"] is True,
            data["what_remains_open"],
        ),
        check(
            "note records diagnostic scope",
            "finite response algebra only" in note
            and "honest packet is unpromoted" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C sector projectors/dotD on smooth B_N audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
