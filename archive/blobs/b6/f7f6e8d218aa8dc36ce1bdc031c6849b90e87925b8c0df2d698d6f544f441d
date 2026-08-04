"""Audit the selected C1 response extraction attempt."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "selected_c1_response_extraction_attempt_certificate.json"
TEMPLATE = CERT_DIR / "selected_c1_response_data_certificate.template.json"
RPLUS_CERT = CERT_DIR / "c1_iwasawa_rplus_support_certificate.json"
INSERTION_CERT = CERT_DIR / "c1_curvature_insertion_formula_certificate.json"
RANK_CERT = CERT_DIR / "c1_alpha1_rank_lift_criterion_certificate.json"
CKM_CERT = CERT_DIR / "ckm_leading_noncommutation_criterion_certificate.json"
PAPER = ROOT / "Selected_C1_Response_Data_Extraction_Attempt_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def det2(block: list[list[int]]) -> int:
    return block[0][0] * block[1][1] - block[0][1] * block[1][0]


def main() -> None:
    cert = load_json(CERT)
    template = load_json(TEMPLATE)
    rplus = load_json(RPLUS_CERT)
    insertion = load_json(INSERTION_CERT)
    rank = load_json(RANK_CERT)
    ckm = load_json(CKM_CERT)
    paper = read(PAPER)

    attempt = cert.get("attempt_result", {})
    driver = cert.get("computed_driver_row", {})
    missing = cert.get("missing_selected_operator_data", {})
    witness = cert.get("underdetermination_witness", {})
    zero_minor = det2(witness.get("zero_response_map", {}).get("light_block", [[0, 0], [0, 0]]))
    nonzero_minor = det2(witness.get("nonzero_response_map", {}).get("light_block", [[0, 0], [0, 0]]))

    template_operator_data = template.get("operator_data", {})
    template_responses = template.get("response_matrices", {})
    v_c1 = template_operator_data.get("selected_V_C1_functional")
    hess = template_operator_data.get("Hess_Xi_blocks")

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status") == "C1_RESPONSE_EXTRACTION_BLOCKED_MISSING_SELECTED_OPERATOR_DATA"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "Rplus support dependency",
            "SUPPORT-CLOSED"
            if rplus.get("status") == "C1_IWASAWA_RPLUS_INVARIANT_SUPPORT_CLOSED_OVERLAPS_OPEN"
            else "FAIL",
            str(rplus.get("status")),
        ),
        Gate(
            "insertion formula dependency",
            "FORMULATED-OPEN"
            if insertion.get("status") == "C1_CURVATURE_INSERTION_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(insertion.get("status")),
        ),
        Gate(
            "rank criterion dependency",
            "CRITERION-CLOSED"
            if rank.get("status") == "C1_ALPHA1_RANK_LIFT_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(rank.get("status")),
        ),
        Gate(
            "CKM criterion dependency",
            "CRITERION-CLOSED"
            if ckm.get("status") == "CKM_LEADING_NONCOMMUTATION_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(ckm.get("status")),
        ),
        Gate(
            "alpha1 driver computed",
            "PASS"
            if attempt.get("alpha1_driver_row_computed") is True
            and driver.get("alpha_2_component") == 0
            and driver.get("alpha_3_component") == 0
            else "FAIL",
            driver.get("Tr_grav_Rplus_squared", ""),
        ),
        Gate(
            "operator data not computed",
            "EXPECTED"
            if attempt.get("M_C1_alpha1_entries_computed") is False
            and all(value is None for value in missing.values())
            else "FAIL",
            ", ".join(missing.keys()),
        ),
        Gate(
            "V_C1 curvature piece identified",
            "PARTIAL"
            if isinstance(v_c1, dict)
            and "K_constraint_Rplus_piece" in v_c1
            and "Lambda_constraint_Rplus_piece" in v_c1
            else "FAIL",
            "Green-Schwarz Rplus pieces recorded",
        ),
        Gate(
            "Hess_Xi principal blocks identified",
            "PARTIAL"
            if isinstance(hess, dict)
            and "principal_symbol_blocks" in hess
            and "coercivity" in hess
            else "FAIL",
            "twisted/YM Laplacian blocks recorded",
        ),
        Gate(
            "template remains open",
            "OPEN" if template.get("status") == "OPEN" else "FAIL",
            str(template.get("status")),
        ),
        Gate(
            "template has operator slots",
            "PASS"
            if {
                "selected_V_C1_functional",
                "Hess_Xi_blocks",
                "dotD_Q",
                "dotD_H",
            }.issubset(template_operator_data)
            else "FAIL",
            ", ".join(template_operator_data.keys()),
        ),
        Gate(
            "template has response slots",
            "PASS"
            if {
                "M_u_C1_alpha1",
                "M_d_C1_alpha1",
                "M_e_C1_alpha1",
                "M_nuD_C1_alpha1",
            }.issubset(template_responses)
            else "FAIL",
            ", ".join(template_responses.keys()),
        ),
        Gate(
            "dotD operators still open",
            "EXPECTED"
            if template_operator_data.get("dotD_Q") is None
            and template_operator_data.get("dotD_H") is None
            else "FAIL",
            "sector Dirac/operator variations not supplied",
        ),
        Gate(
            "response matrices still open",
            "EXPECTED"
            if all(value is None for value in template_responses.values())
            else "FAIL",
            "M_u,d,e,nuD remain null",
        ),
        Gate(
            "underdetermination witness",
            "PASS"
            if zero_minor == 0 and nonzero_minor == 1
            else "FAIL",
            f"zero_minor={zero_minor}, nonzero_minor={nonzero_minor}",
        ),
        Gate(
            "forbidden shortcuts",
            "PASS" if len(cert.get("forbidden_shortcuts", [])) >= 5 else "FAIL",
            f"{len(cert.get('forbidden_shortcuts', []))} shortcuts forbidden",
        ),
        Gate(
            "paper states blocked status",
            "PASS"
            if "C1_RESPONSE_EXTRACTION_BLOCKED_MISSING_SELECTED_OPERATOR_DATA" in paper
            else "FAIL",
            "explicit status present",
        ),
        Gate(
            "paper names template",
            "PASS"
            if "selected_c1_response_data_certificate.template.json" in paper
            else "FAIL",
            "template named",
        ),
    ]

    print("Selected C1 response extraction attempt audit")
    print("=============================================")
    print()
    print(f"status={cert.get('status')}")
    print(f"closed_driver={driver.get('Tr_grav_Rplus_squared')}")
    print(f"zero_minor={zero_minor}")
    print(f"nonzero_minor={nonzero_minor}")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
