"""Audit the heterotic source-augmented typed maps or projective rho_E request."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_sourceaugmented_typedmaps_or_projectiverhoe_tables_request.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_sourceaugmented_typedmaps_or_projectiverhoe_tables_request.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_sourceaugmented_typedmaps_or_projectiverhoe_tables_request_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_SourceAugmented_TypedMaps_or_ProjectiveRhoE_Tables_Request_v1.md"

STATUS = "HETEROTIC_SOURCEAUGMENTED_TYPEDMAPS_OR_PROJECTIVERHOE_TABLES_REQUEST_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_TypedMapTables_or_ProjectiveRhoETables_SourceFill_v1"


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
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["legal_next_artifact"] == NEXT and cert["legal_next_artifact"] == NEXT, data["decision"])
    check("request not closure", data["decision"]["request_built"] is True and data["decision"]["closure_claimed"] is False, data["decision"])
    check("no values emitted", data["decision"]["typed_tables_emitted"] is False and data["decision"]["projective_rhoE_tables_emitted"] is False, data["decision"])

    typed = data["typed_payload"]
    projective = data["projective_payload"]
    check("typed payload complete", set(typed["required_tables"]) == {
        "cover_or_finite_domain",
        "lattice_generators_and_complex_coordinate_action",
        "factor_of_automorphy",
        "section_spaces",
        "product_constants",
        "f_coefficients",
        "g_coefficients",
        "g_f_zero_machine_check",
        "exactness_or_local_freeness_certificate",
        "EndE_cochain_or_harmonic_basis",
        "trace_inner_product_and_shared_line_policy",
        "finite_operator_exit",
    }, typed["required_tables"])
    check("typed sections carried", len(typed["required_tables"]["section_spaces"]) == 11, typed["required_tables"]["section_spaces"])
    check("typed equations hard", "g o f" in " ".join(typed["acceptance_equations"]) and "End(E)" in " ".join(typed["acceptance_equations"]), typed["acceptance_equations"])

    check("projective payload complete", set(projective["required_tables"]) == {
        "selected_Deligne_Cech_or_B_field_representative",
        "period_denominator_or_smooth_unit",
        "representative_to_central_cocycle_map",
        "rho_E_generator_or_boundary_matrices",
        "central_corner_cocycle",
        "nontrivial_central_twist",
        "metric_or_unitarity_compatibility",
        "sector_or_QaSU3_domain_maps",
        "Freed_Witten_and_Bianchi_checks",
        "finite_response",
    }, projective["required_tables"])
    check("projective equations hard", "rho_E(gamma)" in " ".join(projective["acceptance_equations"]) and "same rho_E packet" in " ".join(projective["acceptance_equations"]), projective["acceptance_equations"])

    audit = data["current_source_audit"]
    check("current source remains open", audit["selected_Qa_SU3_source_packet_found"] is False and audit["response_payload_found"] is False, audit)
    check("guardrails all true", all(data["guardrails"].values()), data["guardrails"])
    check("no downstream computation", data["decision"]["E_Qa_computed"] is False and data["decision"]["threshold_value_computed"] is False, data["decision"])
    check("note records fork", NEXT in note and "only two legal first-value lanes" in note, NOTE)

    print("\nSelected heterotic source-augmented typed maps or projective rho_E request audit")


if __name__ == "__main__":
    main()
