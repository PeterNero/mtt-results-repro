"""Audit the selected D_E source hunt and way-forward certificate."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "selected_de_source_hunt_certificate.json"
PAPER = ROOT / "Selected_DE_Source_Hunt_and_Way_Forward_v1.md"
SELECTED_DE = CERT_DIR / "iwasawa_selected_de_construction_attempt_certificate.json"
MISSING_DATA = CERT_DIR / "selected_missing_data_calculation_certificate.json"
DOLBEAULT = CERT_DIR / "iwasawa_dolbeault_complex_extraction_certificate.json"
MONAD = CERT_DIR / "iwasawa_monad_map_data_gate_certificate.json"
DIAGNOSTIC = CERT_DIR / "iwasawa_diagnostic_h1_three_spectral_pipeline_certificate.json"


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
    selected_de = load_json(SELECTED_DE)
    missing_data = load_json(MISSING_DATA)
    dolbeault = load_json(DOLBEAULT)
    monad = load_json(MONAD)
    diagnostic = load_json(DIAGNOSTIC)
    paper = read(PAPER)

    candidates = cert.get("candidate_results", {})
    hunt = cert.get("hunt_result", {})
    scaffold = " ".join(cert.get("route_c_minimal_scaffold", []))
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    external = cert.get("external_sources_checked_for_templates", [])

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status")
            == "SELECTED_D_E_SOURCE_NOT_FOUND_ROUTE_C_FINITE_SOLVE_RECOMMENDED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "depends on current blockers",
            "PASS"
            if selected_de.get("verdict", {}).get("selected_D_E_constructed") is False
            and missing_data.get("computed_result", {}).get("first_blocking_layer")
            == "selected_operator_source"
            else "FAIL",
            str(selected_de.get("verdict", {})),
        ),
        Gate(
            "R1 rejected",
            "PASS"
            if candidates.get("R1_printed_invariant_A01", {}).get("status") == "REJECTED"
            and dolbeault.get("literal_integrability_result", {}).get("integrable") is False
            else "FAIL",
            str(candidates.get("R1_printed_invariant_A01", {})),
        ),
        Gate(
            "repair not selected",
            "PASS"
            if candidates.get("R1_invariant_repairs", {}).get("status")
            == "DIAGNOSTIC_ONLY"
            and diagnostic.get("diagnostic_operator", {}).get("selected") is False
            else "FAIL",
            str(candidates.get("R1_invariant_repairs", {})),
        ),
        Gate(
            "R2 monad partial only",
            "PASS"
            if candidates.get("R2_monad_chern_data", {}).get("status")
            == "PARTIAL_TOPOLOGY_ONLY"
            and monad.get("typed_map_check", {}).get(
                "requires_global_holomorphic_sections_or_transition_data"
            )
            is True
            and monad.get("consequence_for_sm_closure", {}).get(
                "can_compute_H1_X_E_from_current_monad_data"
            )
            is False
            else "FAIL",
            str(candidates.get("R2_monad_chern_data", {})),
        ),
        Gate(
            "R3 abstract only",
            "PASS"
            if candidates.get("R3_HYM_Strominger_selection", {}).get("status")
            == "ABSTRACT_EXISTENCE_ONLY"
            and selected_de.get("route_evaluation", {}).get(
                "R3_direct_selected_HYM_solve", {}
            ).get("status")
            == "ABSTRACT_EXISTENCE_ONLY"
            else "FAIL",
            str(candidates.get("R3_HYM_Strominger_selection", {})),
        ),
        Gate(
            "A02 absent recorded",
            "PASS"
            if candidates.get("R4_A02_reference", {}).get("status")
            == "PLACEHOLDER_ABSENT"
            and "A02" in paper
            else "FAIL",
            str(candidates.get("R4_A02_reference", {})),
        ),
        Gate(
            "external templates not promoted",
            "PASS"
            if len(external) == 2
            and all(item.get("selected_sm_source") is False for item in external)
            and candidates.get("R5_external_instantons", {}).get("status")
            == "TEMPLATE_ONLY"
            else "FAIL",
            str(external),
        ),
        Gate(
            "hunt result",
            "PASS"
            if hunt.get("selected_D_E_source_found") is False
            and hunt.get("first_blocking_layer_confirmed") == "selected_operator_source"
            and "Route C" in hunt.get("best_next_route", "")
            else "FAIL",
            str(hunt),
        ),
        Gate(
            "route C scaffold",
            "PASS"
            if contains_all(
                scaffold,
                [
                    "FE/Galerkin",
                    "rho_E",
                    "integrability",
                    "HYM",
                    "Riesz gap",
                    "primitive C1",
                ],
            )
            else "FAIL",
            scaffold,
        ),
        Gate(
            "guardrails",
            "PASS"
            if all(value is False for value in guardrails.values())
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("source_hunt_closed") is True
            and verdict.get("selected_D_E_source_found") is False
            and verdict.get("route_c_should_be_built_next") is True
            and "finite selected-connection solve scaffold" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records source hunt",
            "PASS"
            if contains_all(
                paper,
                [
                    "Candidate R1",
                    "Candidate R2",
                    "Candidate R3",
                    "Candidate R4",
                    "Candidate R5",
                    "No current source supplies a computable selected `D_E`",
                    "build Route C as a finite selected-connection solve scaffold",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected D_E source hunt audit")
    print("==============================")
    print()
    print(f"selected_D_E_source_found={hunt.get('selected_D_E_source_found')}")
    print(f"best_next_route={hunt.get('best_next_route')}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

