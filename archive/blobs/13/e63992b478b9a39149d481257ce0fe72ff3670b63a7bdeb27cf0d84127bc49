"""Audit heterotic projective rho_E source-selection/direct-identity frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_sourceselection_theorem_or_directoperatoridentity.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_sourceselection_theorem_or_directoperatoridentity.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_sourceselection_theorem_or_directoperatoridentity_certificate.json"
MISSING = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_sourceselection_remaining_obligations.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SourceSelectionTheorem_or_DirectOperatorIdentity_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCE_SELECTION_OR_DIRECT_OPERATOR_IDENTITY_ATTEMPT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FinitePhysicalQuotient_SourceTheorem_v1"


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
    missing = load(MISSING)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("all lanes evaluated", data["decision"]["all_three_lanes_evaluated"] is True and cert["all_three_lanes_evaluated"] is True, data["decision"])
    check("strongest lane selected", data["decision"]["strongest_lane"] == "finite_physical_quotient_selection" and cert["strongest_lane"] == "finite_physical_quotient_selection", cert)

    finite = data["lane_evaluation"]["finite_physical_quotient_selection"]
    smooth = data["lane_evaluation"]["smooth_representative_map"]
    direct = data["lane_evaluation"]["direct_operator_identity"]
    check("finite lane partial", finite["status"] == "PARTIAL" and finite["support_count"] == 2 and finite["required_count"] == 4, finite)
    check("finite source identity still open", "selected_domain_exactly_finite_galerkin_labels" in finite["missing"] and "finite_rhoE_packet_selected_not_validator_only" in finite["missing"], finite["missing"])
    check("smooth lane open", smooth["status"] == "OPEN" and smooth["closed"] is False, smooth)
    check("direct lane open", direct["status"] == "OPEN" and direct["closed"] is False, direct)
    check("no closure promoted", data["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert)
    check("guardrails true", all(data["guardrails"].values()), data["guardrails"])
    check("obligation packet mirrors strongest lane", missing["strongest_lane"] == "finite_physical_quotient_selection" and missing["finite_physical_quotient_selection"]["missing"] == finite["missing"], missing)
    check("finite values carried forward", data["finite_values_carried_forward"]["finite_part"]["finite_trace_tau_squared"] == 8 and data["finite_values_carried_forward"]["Riesz_projector"][2][2] == 1, data["finite_values_carried_forward"])
    check("note records frontier", NEXT in note and "finite physical quotient source theorem" in note, NOTE)

    print("\nSelected heterotic projective rho_E source-selection/direct-identity audit")


if __name__ == "__main__":
    main()
