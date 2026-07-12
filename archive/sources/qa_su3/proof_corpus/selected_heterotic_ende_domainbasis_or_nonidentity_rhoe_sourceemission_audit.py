"""Audit heterotic End(E) domain-basis or nonidentity rho_E source-emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_ende_domainbasis_or_nonidentity_rhoe_sourceemission.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_ende_domainbasis_or_nonidentity_rhoe_sourceemission.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_ende_domainbasis_or_nonidentity_rhoe_sourceemission_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_EndE_DomainBasis_or_NonIdentityRhoE_SourceEmission_v1.md"

STATUS = "HETEROTIC_ENDE_DOMAINBASIS_OR_NONIDENTITY_RHOE_SOURCEEMISSION_GATE_BUILT_VALUES_OPEN"


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
    check("gate built open", data["decision"]["sourceemission_gate_built"] is True and data["closure_claimed"] is False, data["decision"])

    lane_a = data["lanes"]["A_typed_cech_EndE_domain_basis"]
    lane_b = data["lanes"]["B_projective_twisted_nonidentity_rhoE"]
    check("lane A required fields", {"typed_f_map_matrix", "typed_g_map_matrix", "EndE_basis_vectors_or_cochains", "trace_inner_product_on_EndE"} <= set(lane_a["required_payload"]), lane_a["required_payload"])
    check("lane B required fields", {"rho_E_generator_or_boundary_matrices", "nonidentity_check", "projective_cocycle_law", "finite_response_exit"} <= set(lane_b["required_payload"]), lane_b["required_payload"])
    check("lane A support not closure", lane_a["current_support"]["monad_topology_selected"] is True and lane_a["current_support"]["typed_maps_filled"] is False and lane_a["closes_now"] is False, lane_a)
    check("lane B support not closure", lane_b["current_support"]["u1y_nonidentity_schema_built"] is True and lane_b["current_support"]["projective_rhoE_tables_supplied"] is False and lane_b["closes_now"] is False, lane_b)

    forbidden = set(data["acceptance_kernel"]["forbidden"])
    check("forbidden shortcuts", {"abstract End(E) fiber dimension as a finite basis", "identity rho_E", "Route-C nonidentity schema as heterotic rho_E values"} <= forbidden, data["acceptance_kernel"])
    check("no downstream closure", data["decision"]["E_Qa_computed"] is False and data["decision"]["same_source_identity_proved"] is False and data["decision"]["computed_threshold_value"] is False, data["decision"])
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records lanes", "Lane A" in NOTE.read_text(encoding="utf-8") and "Lane B" in NOTE.read_text(encoding="utf-8"), NOTE)

    print("\nSelected heterotic End(E) domain-basis or nonidentity rho_E source-emission audit")


if __name__ == "__main__":
    main()
