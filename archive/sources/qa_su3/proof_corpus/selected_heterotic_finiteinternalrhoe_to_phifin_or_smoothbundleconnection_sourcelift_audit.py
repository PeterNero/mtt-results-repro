"""Audit finite-internal rho_E to Phi_fin or smooth bundle-connection source-lift gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_finiteinternalrhoe_to_phifin_or_smoothbundleconnection_sourcelift.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_finiteinternalrhoe_to_phifin_or_smoothbundleconnection_sourcelift.candidate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_finiteinternalrhoe_to_phifin_or_smoothbundleconnection_sourcelift_required_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_finiteinternalrhoe_to_phifin_or_smoothbundleconnection_sourcelift_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_FiniteInternalRhoE_to_PhiFin_or_SmoothBundleConnection_SourceLift_v1.md"

STATUS = "HETEROTIC_FINITEINTERNALRHOE_TO_PHIFIN_OR_SMOOTHBUNDLE_SOURCE_LIFT_BUILT_FUNCTOR_OPEN"
NEXT = "Selected_Heterotic_EndE_to_BN_LabelEmbedding_or_SmoothTransitionConnection_ValuePacket_v1"


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
    template = load(TEMPLATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    comparison = data["dimension_comparison"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and template["status"] == "OPEN_VALUES_REQUIRED", (data["status"], cert["status"], template["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("dimension mismatch recorded", comparison["finite_internal_label_count"] == 11 and comparison["PhiFin_BN_basis_dimension"] == 27 and comparison["dimension_match"] is False, comparison)
    check("finite packet retained", decision["finite_internal_packet_remains_closed"] is True and cert["finite_internal_packet_remains_closed"] is True, decision)
    check("functor not constructed", decision["finite_internal_to_PhiFin_functor_constructed"] is False and data["lane_A_functor"]["closes_now"] is False, data["lane_A_functor"])
    check("embedding required", data["lane_A_functor"]["candidate_label_embedding"]["required_matrix_shape"] == [27, 11] and template["lane_A_label_embedding_or_EndE_to_BN_functor"]["embedding_matrix_27x11_or_projection_pair"] is None, template["lane_A_label_embedding_or_EndE_to_BN_functor"])
    check("smooth lift not constructed", decision["smooth_bundle_connection_lift_constructed"] is False and data["lane_B_smooth_bundle_lift"]["closes_now"] is False, data["lane_B_smooth_bundle_lift"])
    check("smooth required values open", all(value is None for value in template["lane_B_smooth_bundle_or_transition_lift"].values()), template["lane_B_smooth_bundle_or_transition_lift"])
    check("no operator closure", decision["E_Qa_computed"] is False and decision["smooth_finitepart_computed"] is False and decision["physical_threshold_value_claimed"] is False, decision)
    check("forbidden promotions", "identify 11 internal labels with the 27-mode B_N basis by dimension-free assertion" in template["forbidden_promotions"], template["forbidden_promotions"])
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and template["closure_claimed"] is False, cert)
    check("note records bridge", NEXT in note and "27 x 11" in note and str(TEMPLATE.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic finite-internal rho_E to PhiFin / smooth source-lift audit")


if __name__ == "__main__":
    main()
