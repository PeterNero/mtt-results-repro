"""Audit the post-invariant-obstruction way-forward decision."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "post_invariant_way_forward_certificate.json"
TEMPLATE = CERT_DIR / "iwasawa_selected_cohomology_data.template.json"
PAPER = ROOT / "Post_Invariant_Obstruction_Way_Forward_for_Iwasawa_SM_Closure_v1.md"


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
    template = load_json(TEMPLATE)
    paper = read(PAPER)

    blocked = cert.get("blocked_shortcuts", {})
    primary = cert.get("selected_primary_route", {})
    fallback = cert.get("selected_fallback_route", {})
    schema = cert.get("next_artifact_schema", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    template_gates = template.get("success_gates", {})

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "WAY_FORWARD_SELECTED_MONAD_CECH_PRIMARY_SPECTRAL_FALLBACK"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "blocked shortcuts recorded",
            "PASS"
            if blocked.get("literal_A01") == "fails integrability"
            and "h1=2" in blocked.get("one_index_A01_repair", "")
            and "h1=2" in blocked.get("three_entry_torsion_support_A01", "")
            and "net chirality" in blocked.get("c3_index_as_basis", "")
            else "FAIL",
            str(blocked),
        ),
        Gate(
            "primary route selected",
            "PASS"
            if primary.get("id") == "typed_monad_cech_cohomology"
            and contains_all(
                " ".join(primary.get("required_inputs", [])),
                ["typed f_i", "typed g_i", "g o f = 0"],
            )
            and contains_all(
                " ".join(primary.get("construction_steps", [])),
                ["long exact cohomology", "H^1(X,E)", "sector projections"],
            )
            else "FAIL",
            str(primary),
        ),
        Gate(
            "fallback route selected",
            "PASS"
            if fallback.get("id") == "non_invariant_spectral_galerkin"
            and "monad sections" in fallback.get("trigger", "")
            and contains_all(
                " ".join(fallback.get("required_inputs", [])),
                ["finite basis beyond left-invariant forms", "Riesz projector", "dotD_alpha1"],
            )
            else "FAIL",
            str(fallback),
        ),
        Gate(
            "next schema strict",
            "PASS"
            if schema.get("name") == "Iwasawa_Selected_Cohomology_Data_Certificate"
            and set(schema.get("allowed_modes", [])) == {"typed_monad_cech", "non_invariant_spectral_galerkin"}
            and "h1_E_equals_three" in schema.get("required_success_fields", [])
            and "anti_family_middle_cohomology_vanishes" in schema.get("required_success_fields", [])
            else "FAIL",
            str(schema),
        ),
        Gate(
            "template present",
            "PASS"
            if template.get("certificate") == "IwasawaSelectedCohomologyDataTemplate"
            and set(template.get("allowed_modes", [])) == {"typed_monad_cech", "non_invariant_spectral_galerkin"}
            and template_gates.get("h1_E_equals_three") is False
            and template_gates.get("anti_family_middle_cohomology_vanishes") is False
            else "FAIL",
            str(template.get("certificate")),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("uses_benchmark_yukawa_entries") is False
            and guardrails.get("uses_observed_masses_or_mixings") is False
            and guardrails.get("silently_repairs_A01") is False
            and guardrails.get("uses_index_as_zero_mode_basis") is False
            and guardrails.get("allows_free_dotD") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("strategy_question_answered") is True
            and "typed monad/Cech" in verdict.get("primary_next_move", "")
            and verdict.get("values_computed") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records way forward",
            "PASS"
            if contains_all(
                paper,
                [
                    "The primary path is",
                    "typed monad sections",
                    "long exact cohomology",
                    "Fallback Route",
                    "Iwasawa_Selected_Cohomology_Data_Certificate",
                    "stop trying to repair the sparse invariant A01",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Post-invariant obstruction way-forward audit")
    print("===========================================")
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
