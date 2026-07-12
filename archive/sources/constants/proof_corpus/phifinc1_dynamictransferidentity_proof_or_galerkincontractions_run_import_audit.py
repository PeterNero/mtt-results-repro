"""Audit PhiFinC1 dynamic-transfer identity attempt / Galerkin run import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_import.candidate.json"
CERT = ROOT / "certificates" / "phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.py"

STATUS = "PHIFINC1_DYNAMIC_TRANSFER_ATTEMPT_IMPORTED_STATIONARY_TRACE_CLOSED_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    stationary = data["stationary_trace_import"]
    require(stationary["selected_source_verified"] is True, "stationary source not verified")
    require(stationary["selected_riesz_green_source_verified"] is True, "Riesz/Green missing")
    require(stationary["functional_gauge_transported_trace_proved"] is True, "transported trace missing")
    require(stationary["selected_dotD_source_verified_inside_stationary_transport_replay"] is False, "dotD overclaimed")
    require(stationary["alpha1_driver_verified_inside_stationary_transport_replay"] is False, "alpha1 overclaimed")

    boundary = data["phifin_payload_boundary"]
    require(boundary["all_support_shapes_present"] is True, "support shapes missing")
    require(boundary["all_selected_values_emitted"] is False, "values overemitted")
    require(boundary["primitive_C1_contractions_selected"] is False, "primitive C1 selected")

    identity = data["PhiFinC1_identity_attempt"]
    require(identity["stationary_trace_sufficient_for_C1_transfer_identity"] is False, "stationary sufficient overclaim")
    require(identity["selected_identity_proved_now"] is False, "identity overproved")
    require(identity["normal_form_values_not_promoted_now"] is True, "normal form promoted")
    require(len(identity["missing_dynamic_objects"]) == 5, "missing object count mismatch")

    theorem = data["partial_promotion_theorem"]
    require(theorem["proved"] is True, "partial theorem not proved")
    require(theorem["corollary_now"]["stationary_source_layer_closed"] is True, "stationary corollary missing")
    require(theorem["corollary_now"]["C1_dynamic_layer_closed"] is False, "C1 dynamic overclosed")
    require(theorem["corollary_now"]["selected_A_b_delta_promoted"] is False, "A/b/delta promoted")

    guardrails = data["guardrails"]
    require(guardrails["stationary_source_layer_promoted"] is True, "stationary layer not promoted")
    require(guardrails["selected_PhiFinC1_identity_claimed"] is False, "PhiFinC1 identity claimed")
    require(guardrails["selected_A_selected_claimed"] is False, "A claimed")
    require(guardrails["selected_b_selected_claimed"] is False, "b claimed")
    require(guardrails["selected_deltaTheta_C1_claimed"] is False, "delta claimed")
    require(guardrails["honest_Galerkin_C1_contractions_claimed"] is False, "Galerkin claimed")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")
    require(guardrails["full_SM_closure_claimed"] is False, "closure claimed")
    require("stationary PhiFin trace" in note, "note missing stationary boundary")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
