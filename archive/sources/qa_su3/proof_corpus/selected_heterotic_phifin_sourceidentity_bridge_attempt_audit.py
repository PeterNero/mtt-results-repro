"""Audit the heterotic Phi_fin source-identity bridge attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_phifin_sourceidentity_bridge_attempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_phifin_sourceidentity_bridge_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_phifin_sourceidentity_bridge_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_PhiFin_SourceIdentity_Bridge_Attempt_v1.md"

STATUS = "HETEROTIC_PHIFIN_SOURCEIDENTITY_BRIDGE_ATTEMPT_SUPPORT_FILLED_IDENTITY_OPEN"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    cert = load(CERT)

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("support imported only", data["decision"]["support_imported_without_promotion"] is True and data["closure_claimed"] is False, data["decision"])
    check("monad topology retained", data["monad_topology"]["c1_zero"] and data["monad_topology"]["c2_zero"] and data["monad_topology"]["c3_integral_equals_6"], data["monad_topology"])
    check("27-mode support closed", data["decision"]["u1y_27mode_gap_layer_closed"] and data["decision"]["u1y_trace_equality_closed"], data["imported_27mode_support"])
    check("transport support closed", data["decision"]["transport_projector_replay_closed"], data["imported_27mode_support"]["transport_replay"])

    subclaims = data["tested_subclaims"]
    check("gap support not promoted", subclaims["Riesz_Green_gap_preserved_on_imported_layer"]["proved_for_imported_gap_layer"] is True and subclaims["Riesz_Green_gap_preserved_on_imported_layer"]["proved_for_heterotic_QaSU3"] is False, subclaims["Riesz_Green_gap_preserved_on_imported_layer"])
    check("trace support not promoted", subclaims["D_E_trace_equality_on_27mode_gap_layer"]["proved_for_imported_gap_layer"] is True and subclaims["D_E_trace_equality_on_27mode_gap_layer"]["proved_for_heterotic_QaSU3"] is False, subclaims["D_E_trace_equality_on_27mode_gap_layer"])
    check("EndE functor open", data["decision"]["heterotic_EndE_to_BN_functor_emitted"] is False and subclaims["monad_EndE_to_BN_functor"]["proved_for_heterotic_QaSU3"] is False, subclaims["monad_EndE_to_BN_functor"])
    check("rhoE open", data["decision"]["heterotic_nonidentity_rhoE_emitted"] is False and subclaims["rho_E_or_transition_data_nonidentity"]["proved_for_heterotic_QaSU3"] is False, subclaims["rho_E_or_transition_data_nonidentity"])
    check("finite part open", data["decision"]["heterotic_finite_part_regularization_emitted"] is False and subclaims["finite_part_regularization"]["proved_for_heterotic_QaSU3"] is False, subclaims["finite_part_regularization"])

    missing = data["minimal_missing_packet"]
    check("minimal packet names three groups", set(missing) == {"EndE_to_BN_functor", "nonidentity_rhoE_or_transition_data", "operator_and_finite_part"}, missing)
    check("no closure", data["decision"]["same_source_identity_proved"] is False and data["decision"]["E_Qa_computed"] is False and data["decision"]["computed_threshold_value"] is False, data["decision"])
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records next", cert["next_required_artifact"] in NOTE.read_text(encoding="utf-8"), NOTE)

    print("\nSelected heterotic Phi_fin source-identity bridge attempt audit")


if __name__ == "__main__":
    main()
