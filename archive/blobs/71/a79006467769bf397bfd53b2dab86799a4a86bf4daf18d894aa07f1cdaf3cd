"""Audit the matrix-construction route ledger."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "matrix_construction_routes_certificate.json"
PAPER = ROOT / "Matrix_Construction_Routes_for_SM_Closure_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def route_map(cert: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {route["id"]: route for route in cert.get("routes", [])}


def joined(route: dict[str, Any]) -> str:
    parts: list[str] = [route.get("id", ""), route.get("matrix_object", "")]
    for key in ("construction", "strengths", "blockers"):
        parts.extend(str(item) for item in route.get(key, []))
    return " ".join(parts)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    routes = route_map(cert)

    expected_routes = {
        "route_A_algebraic_cohomology_cup_product",
        "route_B_physical_normalization_numeric_harmonic",
        "route_C_modular_selection_texture",
        "route_D_iwasawa_invariant_form_galerkin",
        "route_E_spectral_green_operator_response",
        "route_F_dual_triangulation_consistency",
    }
    expected_urls = {
        "https://arxiv.org/abs/hep-th/0601204",
        "https://arxiv.org/abs/2401.15078",
        "https://arxiv.org/abs/2402.13563",
        "https://arxiv.org/abs/2504.09773",
        "https://arxiv.org/abs/2603.00864",
    }

    refs = {ref.get("url") for ref in cert.get("external_inspirations", [])}
    recommended_steps = [step.get("step") for step in cert.get("recommended_path", [])]

    route_a = joined(routes.get("route_A_algebraic_cohomology_cup_product", {}))
    route_b = joined(routes.get("route_B_physical_normalization_numeric_harmonic", {}))
    route_c = joined(routes.get("route_C_modular_selection_texture", {}))
    route_d = joined(routes.get("route_D_iwasawa_invariant_form_galerkin", {}))
    route_e = joined(routes.get("route_E_spectral_green_operator_response", {}))
    route_f = joined(routes.get("route_F_dual_triangulation_consistency", {}))

    all_routes_have_fields = all(
        route.get("status")
        and route.get("matrix_object")
        and route.get("construction")
        and route.get("strengths")
        and route.get("blockers")
        for route in routes.values()
    )

    discipline = cert.get("discipline", {})

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "MATRIX_CONSTRUCTION_ROUTES_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "expected route ids",
            "PASS" if set(routes) == expected_routes else "FAIL",
            ", ".join(sorted(routes)),
        ),
        Gate(
            "external primary references recorded",
            "PASS" if refs == expected_urls else "FAIL",
            ", ".join(sorted(str(url) for url in refs)),
        ),
        Gate(
            "route fields complete",
            "PASS" if all_routes_have_fields else "FAIL",
            "status, object, construction, strengths, and blockers are present",
        ),
        Gate(
            "route A algebraic content",
            "PASS"
            if all(token in route_a for token in ["cohomology", "cup", "Yoneda", "Cech"])
            else "FAIL",
            "cohomology/cup/Yoneda/Cech route checked",
        ),
        Gate(
            "route B physical metric content",
            "PASS"
            if all(token in route_b for token in ["harmonic", "kinetic", "L2", "canonical"])
            else "FAIL",
            "harmonic representatives and kinetic normalization checked",
        ),
        Gate(
            "route C selection texture content",
            "PASS"
            if all(token in route_c for token in ["modular", "selection", "texture"])
            else "FAIL",
            "modular and selection-rule texture route checked",
        ),
        Gate(
            "route D Iwasawa alpha1 content",
            "PASS"
            if all(token in route_d for token in ["Iwasawa", "alpha_1", "Galerkin"])
            else "FAIL",
            "Iwasawa invariant alpha_1 Galerkin route checked",
        ),
        Gate(
            "route E calculator interface",
            "PASS"
            if "selected_c1_primitive_contractions.template.json" in route_e
            and "dotD" in route_e
            and "Green" in route_e
            else "FAIL",
            "C1 primitive-contraction interface checked",
        ),
        Gate(
            "route F independent agreement",
            "PASS"
            if "independent" in route_f and "agree" in route_f
            else "FAIL",
            "dual triangulation checked",
        ),
        Gate(
            "recommended first artifact",
            "PASS"
            if recommended_steps
            and recommended_steps[0] == "selected_zero_mode_basis_and_dotD_certificate"
            else "FAIL",
            ", ".join(str(step) for step in recommended_steps),
        ),
        Gate(
            "discipline forbids proxy closure",
            "PASS"
            if discipline.get("claims_selected_numeric_matrices") is False
            and discipline.get("claims_full_sm_closure") is False
            and discipline.get("uses_observed_masses_or_mixings_as_inputs") is False
            and discipline.get("uses_execution_ii_benchmark_entries_as_inputs") is False
            and discipline.get("allows_post_hoc_texture_fitting") is False
            else "FAIL",
            str(discipline),
        ),
        Gate(
            "next artifact recorded",
            "PASS"
            if cert.get("verdict", {}).get("next_artifact") == "Selected Zero-Mode Basis and dotD Certificate"
            else "FAIL",
            str(cert.get("verdict", {})),
        ),
        Gate(
            "paper contains all routes",
            "PASS" if all(route_id in paper for route_id in expected_routes) else "FAIL",
            "route IDs appear in paper",
        ),
        Gate(
            "paper refuses overclaim",
            "PASS"
            if "This note does not compute the missing matrices." in paper
            and "benchmark" in paper
            and "texture" in paper
            else "FAIL",
            "values remain open in prose",
        ),
    ]

    print("Matrix construction route audit")
    print("===============================")
    print()
    print(f"route_count={len(routes)}")
    print(f"external_reference_count={len(refs)}")
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
