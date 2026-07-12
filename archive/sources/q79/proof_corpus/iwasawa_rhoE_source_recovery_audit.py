"""Audit the attempted recovery of Iwasawa rho_E transition data."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_rhoE_source_recovery_certificate.json"
BUNDLE_CONTRACT = CERT_DIR / "iwasawa_bundle_fe_gluing_contract_certificate.json"
RHO_TEMPLATE = CERT_DIR / "iwasawa_bundle_rhoE_data.template.json"
MONAD_GATE = CERT_DIR / "iwasawa_monad_map_data_gate_certificate.json"
TYPED_RECOVERY = CERT_DIR / "iwasawa_typed_monad_section_recovery_certificate.json"
SELECTED_DE = CERT_DIR / "iwasawa_selected_de_construction_attempt_certificate.json"
SPECTRAL_GATE = CERT_DIR / "iwasawa_spectral_operator_gate_certificate.json"
PAPER = ROOT / "Iwasawa_RhoE_Source_Recovery_Attempt_v1.md"


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
    bundle_contract = load_json(BUNDLE_CONTRACT)
    rho_template = load_json(RHO_TEMPLATE)
    monad_gate = load_json(MONAD_GATE)
    typed_recovery = load_json(TYPED_RECOVERY)
    selected_de = load_json(SELECTED_DE)
    spectral_gate = load_json(SPECTRAL_GATE)
    paper = read(PAPER)

    recovered = cert.get("recovered_inputs", {})
    not_recovered = cert.get("not_recovered", {})
    routes = cert.get("route_evaluation", {})
    shortcuts = cert.get("invalid_shortcuts", {})
    template_status = cert.get("rhoE_template_status", {})
    minimal = cert.get("minimal_new_data_to_close", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    route_text = " ".join(
        str(value)
        for route in routes.values()
        for value in route.values()
    )
    shortcut_text = " ".join(shortcuts.values())
    minimal_text = " ".join(str(value) for values in minimal.values() for value in values)
    open_text = " ".join(not_recovered)

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status")
            == "IWASAWA_RHOE_SOURCE_RECOVERY_BLOCKED_SELECTED_TRANSITIONS_MISSING"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if bundle_contract.get("status")
            == "IWASAWA_BUNDLE_FE_GLUING_CONTRACT_FORMULATED_RHOE_DATA_OPEN"
            and rho_template.get("status") == "OPEN"
            and monad_gate.get("status")
            == "IWASAWA_MONAD_MAP_DATA_GATE_BLOCKED_TYPED_MAP_SECTIONS_MISSING"
            and typed_recovery.get("status")
            == "TYPED_MONAD_SECTIONS_NOT_RECOVERED_SPECTRAL_FALLBACK_TRIGGERED"
            and selected_de.get("status")
            == "SELECTED_D_E_CONSTRUCTION_BLOCKED_BY_MISSING_CONNECTION_DATA_DIAGNOSTIC_PIPELINE_READY"
            and spectral_gate.get("status")
            == "SPECTRAL_FALLBACK_REDUCED_TO_SELECTED_OPERATOR_AND_BASIS_DATA"
            else "FAIL",
            "bundle contract, rho template, monad gate, typed recovery, D_E attempt, spectral gate imported",
        ),
        Gate(
            "recovered structural inputs",
            "PASS"
            if all(recovered.values())
            and recovered.get("bundle_FE_rhoE_input_contract") is True
            else "FAIL",
            str(recovered),
        ),
        Gate(
            "rhoE data absent",
            "OPEN"
            if all(not_recovered.values())
            and contains_all(
                open_text,
                [
                    "rho_E_g1_function_or_matrix",
                    "rho_E_g6_function_or_matrix",
                    "transition_functions_for_L_i_K1_K2",
                    "Cech_cocycle_cover_data",
                    "sector_projection_maps_Q_u_d_L_e_N_H",
                    "selected_D_E_action_on_rhoE_glued_basis",
                ],
            )
            else "FAIL",
            str(not_recovered),
        ),
        Gate(
            "route evaluation",
            "PASS"
            if routes.get("R1_corrected_A01_or_connection", {}).get("status") == "BLOCKED"
            and routes.get("R2_typed_monad_Cech_transitions", {}).get("status") == "BLOCKED"
            and routes.get("R3_direct_HYM_solve", {}).get("status") == "ABSTRACT_EXISTENCE_ONLY"
            and contains_all(
                route_text,
                [
                    "not integrable",
                    "typed f_i,g_i sections",
                    "HYM existence",
                    "does not provide a computable",
                ],
            )
            else "FAIL",
            route_text,
        ),
        Gate(
            "invalid shortcuts",
            "PASS"
            if contains_all(
                shortcut_text,
                [
                    "schema smoke test",
                    "c1(E)=0",
                    "local left-invariant frame",
                    "q79 CP character",
                    "Execution II",
                ],
            )
            else "FAIL",
            shortcut_text,
        ),
        Gate(
            "template remains open",
            "OPEN"
            if template_status.get("status") == "OPEN"
            and template_status.get("all_generator_entries_null") is True
            and template_status.get("all_sector_projection_entries_null") is True
            and all(value is None for value in rho_template.get("generator_data", {}).values())
            and all(value is None for value in rho_template.get("sector_projection_maps", {}).values())
            else "FAIL",
            str(template_status),
        ),
        Gate(
            "minimal close data",
            "PASS"
            if contains_all(
                minimal_text,
                [
                    "explicit selected rho_E(g_j,z)",
                    "typed line-bundle transition functions",
                    "selected HYM/Strominger connection",
                    "bundle-glued FE basis",
                    "Riesz projector",
                ],
            )
            else "FAIL",
            minimal_text,
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_rho_E_recovered") is False
            and guardrails.get("promotes_identity_rhoE_to_selected_bundle") is False
            and guardrails.get("promotes_c1_zero_to_trivial_bundle") is False
            and guardrails.get("promotes_generic_constant_maps_to_global_typed_maps") is False
            and guardrails.get("uses_q79_as_bundle_transition") is False
            and guardrails.get("uses_benchmark_or_observed_data") is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("rho_E_recovered_from_current_corpus") is False
            and verdict.get("rho_E_input_contract_closed") is True
            and verdict.get("selected_bundle_FE_space_constructed") is False
            and "rho_E" in verdict.get("next_step", "")
            and "D_E" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records blocker",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa rho_E Source Recovery Attempt",
                    "IWASAWA_RHOE_SOURCE_RECOVERY_BLOCKED_SELECTED_TRANSITIONS_MISSING",
                    "rho_E(g1,z)",
                    "transition functions for L_i,K1,K2",
                    "c1(E)=0 implies rho_E is trivial",
                    "q79 character = rho_E",
                    "selected bundle transition data",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa rho_E source recovery audit")
    print("===================================")
    print()
    print(f"generator_entries_null={all(value is None for value in rho_template.get('generator_data', {}).values())}")
    print(f"sector_entries_null={all(value is None for value in rho_template.get('sector_projection_maps', {}).values())}")
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
