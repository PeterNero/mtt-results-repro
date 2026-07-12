"""Audit K_phys-anchor or smooth-operator-identity fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill_certificate.json"
OBLIGATIONS = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smooth_bundle_operator_or_kphys_remaining_obligations.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_KPhysAnchor_or_SmoothOperatorIdentity_Fill_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_KPHYS_OR_SMOOTH_IDENTITY_FILL_REDUCED_BUNDLE_OPERATOR_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_BundleConnection_RepresentationTrace_QuotientPolicy_v1"


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
    obligations = load(OBLIGATIONS)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("physical lane slot but open", data["decision"]["physical_lane_has_anchor_slot_but_no_value"] is True and data["decision"]["physical_anchor_bridge_closed"] is False, data["physical_normalization_bridge"])
    check("physical blockers all open", not any(data["physical_normalization_bridge"]["blockers"].values()), data["physical_normalization_bridge"]["blockers"])
    check("smooth lane geometry but open", data["decision"]["smooth_lane_has_geometry_but_no_bundle_operator"] is True and data["decision"]["smooth_operator_identity_closed"] is False, data["smooth_operator_identity_bridge"])
    check("smooth blockers all open", not any(data["smooth_operator_identity_bridge"]["blockers"].values()), data["smooth_operator_identity_bridge"]["blockers"])
    check("best next lane", data["decision"]["best_next_lane"] == "smooth_operator_identity_bridge" and cert["best_next_lane"] == "smooth_operator_identity_bridge", data["decision"])
    check("remaining obligations packet", obligations["next_required_artifact"] == NEXT and obligations["preferred_next_lane"] == "smooth_operator_identity_bridge", obligations)
    check("minimum next packet explicit", set(obligations["minimum_next_packet"]) == {"connection_A_components", "curvature_F_A_components", "ad_bundle_representation", "trace_normalization", "kernel_and_quotient_policy", "E_Qa_matrix_or_finite_part_table"}, obligations["minimum_next_packet"])
    check("no closure claimed", data["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert)
    check("guardrails true except target flag false", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records next object", NEXT in note and "`K_phys` is not closed" in note and "A`, `F_A`" in note, NOTE)

    print("\nSelected heterotic projective rho_E K_phys/smooth-identity fill audit")


if __name__ == "__main__":
    main()
