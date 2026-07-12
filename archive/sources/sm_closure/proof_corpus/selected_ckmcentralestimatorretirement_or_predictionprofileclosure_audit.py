from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ckmcentralestimatorretirement_or_predictionprofileclosure"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(f"candidate_data/{SLUG}/ckm_prediction_profile_closure.packet.json")
    cert = load(f"certificates/{SLUG}_certificate.json")

    require(packet["selected_prediction"]["selected_Pi_CKM_weight_rows"] == 3, "selected CKM rows")
    require(packet["selected_prediction"]["source_owned"] is True, "source ownership")
    require(packet["selected_prediction"]["target_fitting_used"] is False, "target fit")
    require(packet["profile_postcheck"]["maximum_absolute_z_score"] < 0.001, "CKM profile")
    require(packet["requirement_decision"]["exact_equality_to_measured_central_estimator_is_theory_obligation"] is False, "invalid central requirement")
    require(packet["requirement_decision"]["U4_correct_prediction_with_uncertainty_standard_closed"] is True, "U4 standard")
    require(packet["requirement_decision"]["exact_arithmetic_equality_to_frozen_replay_closed"] is False, "exact equality overclaim")
    require(all(value is False for value in packet["guards"].values()), "guard")
    require(cert["U4_correct_standard_closed"] is True, "certificate U4")
    require(cert["exact_central_arithmetic_equality_claimed"] is False, "certificate exact overclaim")

    print(json.dumps({
        "selected_CKM_rows": cert["selected_Pi_CKM_rows"],
        "maximum_profile_z_score": cert["maximum_profile_z_score"],
        "U4_correct_standard_closed": True,
        "exact_central_arithmetic_equality_claimed": False,
    }, indent=2))
    print("CKM prediction-profile closure audit passed")


if __name__ == "__main__":
    main()
