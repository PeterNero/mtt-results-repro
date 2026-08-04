"""Audit the Iwasawa spectral Galerkin operator gate."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_spectral_operator_gate_certificate.json"
RECOVERY = CERT_DIR / "iwasawa_typed_monad_section_recovery_certificate.json"
TEMPLATE = CERT_DIR / "iwasawa_spectral_galerkin_data.template.json"
PAPER = ROOT / "Iwasawa_Spectral_Galerkin_Operator_Gate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    cert = load_json(CERT)
    recovery = load_json(RECOVERY)
    template = load_json(TEMPLATE)
    paper = read(PAPER)

    decisions = cert.get("closed_decisions", {})
    routes = cert.get("admissible_operator_routes", {})
    contract = cert.get("galerkin_contract", {})
    missing = cert.get("currently_missing", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    template_gates = template.get("success_gates", {})

    route_keys_ok = set(routes) == {
        "R1_corrected_non_invariant_Dolbeault_operator",
        "R2_typed_monad_sections",
        "R3_direct_selected_HYM_solve",
    }
    contract_text = " ".join(
        [
            contract.get("finite_matrix", ""),
            " ".join(contract.get("basis_requirements", [])),
            contract.get("projector_rule", ""),
            contract.get("error_rule", ""),
            " ".join(contract.get("success_condition", [])),
        ]
    )
    missing_ok = all(value is True for value in missing.values()) and set(missing) == {
        "selected_operator_D_E",
        "non_invariant_basis_B_N",
        "operator_matrix_L_N",
        "Riesz_projector",
        "gap_and_error_bound",
        "Psi_i_representatives",
    }

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "SPECTRAL_FALLBACK_REDUCED_TO_SELECTED_OPERATOR_AND_BASIS_DATA"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "fallback imported",
            "PASS"
            if recovery.get("route_decision", {}).get("non_invariant_spectral_galerkin_fallback_triggered") is True
            and decisions.get("fallback_is_now_active") is True
            else "FAIL",
            str(decisions),
        ),
        Gate(
            "blocked shortcuts imported",
            "PASS"
            if decisions.get("left_invariant_sparse_A01_route_retired") is True
            and decisions.get("typed_monad_route_not_closed_from_current_corpus") is True
            and decisions.get("rank_one_seed_not_enough_for_family_basis") is True
            else "FAIL",
            str(decisions),
        ),
        Gate(
            "three operator routes",
            "PASS" if route_keys_ok else "FAIL",
            ", ".join(sorted(routes)),
        ),
        Gate(
            "R1 checks",
            "PASS"
            if contains_all(
                " ".join(routes.get("R1_corrected_non_invariant_Dolbeault_operator", {}).get("required_checks", [])),
                ["barpartial_E^2", "Bianchi", "HYM", "not a sparse invariant typo repair"],
            )
            else "FAIL",
            str(routes.get("R1_corrected_non_invariant_Dolbeault_operator", {})),
        ),
        Gate(
            "R2 checks",
            "PASS"
            if contains_all(
                " ".join(routes.get("R2_typed_monad_sections", {}).get("required_checks", [])),
                ["typed f_i", "g o f = 0", "exactness", "HYM connection"],
            )
            else "FAIL",
            str(routes.get("R2_typed_monad_sections", {})),
        ),
        Gate(
            "R3 checks",
            "PASS"
            if contains_all(
                " ".join(routes.get("R3_direct_selected_HYM_solve", {}).get("required_checks", [])),
                ["fixed Chern", "residual bounds", "gauge-fixing", "self-adjointness"],
            )
            else "FAIL",
            str(routes.get("R3_direct_selected_HYM_solve", {})),
        ),
        Gate(
            "Galerkin matrix rule",
            "PASS" if "L_N = P_N D_E^* D_E P_N" in contract.get("finite_matrix", "") else "FAIL",
            contract.get("finite_matrix", ""),
        ),
        Gate(
            "basis requirements",
            "PASS"
            if contains_all(
                contract_text,
                [
                    "compact Iwasawa lattice",
                    "left-invariant seed forms",
                    "non-invariant modes",
                    "bundle fiber data",
                    "Gram matrix",
                ],
            )
            else "FAIL",
            contract_text,
        ),
        Gate(
            "projector and error rules",
            "PASS"
            if "Riesz projector" in contract.get("projector_rule", "")
            and "residual norms" in contract.get("error_rule", "")
            else "FAIL",
            str(contract),
        ),
        Gate(
            "success conditions",
            "PASS"
            if contains_all(
                contract_text,
                [
                    "exactly three selected family modes",
                    "anti-family",
                    "Psi_1,Psi_2,Psi_3",
                    "sector projection maps",
                    "dotD_alpha1",
                    "reduced Green operator",
                ],
            )
            else "FAIL",
            contract_text,
        ),
        Gate(
            "currently missing values",
            "OPEN" if missing_ok else "FAIL",
            str(missing),
        ),
        Gate(
            "template aligns",
            "PASS"
            if template.get("certificate") == "IwasawaSpectralGalerkinDataTemplate"
            and template_gates.get("selected_operator_constructed") is False
            and template_gates.get("basis_extends_beyond_left_invariant_forms") is False
            else "FAIL",
            str(template.get("success_gates", {})),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("uses_literal_failed_A01") is False
            and guardrails.get("uses_rank_one_seed_as_full_basis") is False
            and guardrails.get("uses_scalar_central_circle_modes_as_zero_modes") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("closes_spectral_fallback_input_contract") is True
            and verdict.get("closes_spectral_computation") is False
            and "D_E" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "selected operator D_E",
                    "Admissible Sources For D_E",
                    "L_N = P_N D_E^* D_E P_N",
                    "Riesz projector",
                    "supply or construct one admissible selected operator D_E",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa spectral Galerkin operator gate audit")
    print("============================================")
    print()
    print(f"route_count={len(routes)}")
    print(f"missing_count={len(missing)}")
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
