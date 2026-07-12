"""Audit the finite C1 response matrix reduction."""

from __future__ import annotations

import importlib.util
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "c1_finite_response_matrix_reduction_certificate.json"
TEMPLATE = ROOT.parent / "certificates" / "selected_c1_primitive_contractions.template.json"
SELECTED_C1_TEMPLATE = ROOT.parent / "certificates" / "selected_c1_response_data_certificate.template.json"
CALCULATOR = ROOT.parent / "scripts" / "compute_c1_response_matrices.py"


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


def load_calculator():
    spec = importlib.util.spec_from_file_location("compute_c1_response_matrices", CALCULATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load calculator: {CALCULATOR}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def zero() -> list[list[int]]:
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def sample_complete_data() -> dict[str, Any]:
    sectors: dict[str, Any] = {}
    for sector in ("u", "d", "e", "nuD"):
        sectors[sector] = {
            "theta_overlap_variation": zero(),
            "left_zero_mode_response": zero(),
            "right_zero_mode_response": zero(),
            "higgs_zero_mode_response": zero(),
            "explicit_vertex": zero(),
            "basis_connection": zero(),
        }

    sectors["u"]["theta_overlap_variation"] = [
        [1, 0, 2],
        [0, 1, 3],
        [0, 0, 0],
    ]
    sectors["d"]["theta_overlap_variation"] = [
        [2, 1, 5],
        [1, 1, 8],
        [0, 0, 0],
    ]
    sectors["e"]["theta_overlap_variation"] = [
        [1, 2, 0],
        [3, 5, 0],
        [0, 0, 0],
    ]
    sectors["nuD"]["theta_overlap_variation"] = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    return {"sectors": sectors}


def main() -> None:
    cert = load_json(CERT)
    primitive_template = load_json(TEMPLATE)
    selected_c1_template = load_json(SELECTED_C1_TEMPLATE)
    paper = read(ROOT / "C1_Finite_Response_Matrix_Reduction_Theorem_v1.md")
    calculator = load_calculator()

    matrices = calculator.compute_response(sample_complete_data())
    summary = calculator.summarize(matrices)

    schema = cert.get("primitive_contraction_schema", {})
    finite = cert.get("finite_reduction_theorem", {})
    selected_operator_data = selected_c1_template.get("operator_data", {})
    selected_responses = selected_c1_template.get("response_matrices", {})

    missing_template_terms = []
    for sector, sector_data in primitive_template.get("sectors", {}).items():
        for term, value in sector_data.items():
            if value is None:
                missing_template_terms.append(f"{sector}.{term}")

    gates = [
        Gate(
            "certificate status",
            "REDUCED-OPEN"
            if cert.get("status") == "FINITE_C1_RESPONSE_REDUCED_TO_PRIMITIVE_CONTRACTIONS_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "finite formula recorded",
            "PASS"
            if "B_s,Theta" in finite.get("matrix_formula", "")
            and "dotPsi" in finite.get("horizontal_zero_mode_rule", "")
            else "FAIL",
            finite.get("matrix_formula", ""),
        ),
        Gate(
            "required term schema",
            "PASS"
            if set(schema.get("required_3x3_terms_per_sector", []))
            == {
                "theta_overlap_variation",
                "left_zero_mode_response",
                "right_zero_mode_response",
                "higgs_zero_mode_response",
                "explicit_vertex",
                "basis_connection",
            }
            else "FAIL",
            ", ".join(schema.get("required_3x3_terms_per_sector", [])),
        ),
        Gate(
            "selected Xi source available",
            "PARTIAL"
            if isinstance(selected_operator_data.get("selected_V_C1_functional"), dict)
            else "FAIL",
            "operator-level source is present",
        ),
        Gate(
            "selected Hessian source available",
            "PARTIAL"
            if isinstance(selected_operator_data.get("Hess_Xi_blocks"), dict)
            else "FAIL",
            "principal blocks are present; finite inverse blocks still open",
        ),
        Gate(
            "calculator sums primitive terms",
            "PASS"
            if matrices["u"][0][0] == 1
            and matrices["u"][1][1] == 1
            and matrices["d"][0][2] == 5
            else "FAIL",
            "sample complete primitive data assembled",
        ),
        Gate(
            "rank scalar computed",
            "PASS" if summary["C33_M_u"] == 1 and summary["C33_M_d"] == 1 else "FAIL",
            f"C33_u={summary.get('C33_M_u')}, C33_d={summary.get('C33_M_d')}",
        ),
        Gate(
            "CKM orientation scalar computed",
            "PASS" if summary["Delta_v_ud"] == [3, 5] else "FAIL",
            f"Delta_v={summary.get('Delta_v_ud')}",
        ),
        Gate(
            "primitive template remains open",
            "OPEN"
            if primitive_template.get("status") == "OPEN" and len(missing_template_terms) == 24
            else "FAIL",
            f"missing_terms={len(missing_template_terms)}",
        ),
        Gate(
            "selected response matrices still open",
            "EXPECTED"
            if selected_responses and all(value is None for value in selected_responses.values())
            else "FAIL",
            "actual M_u,d,e,nuD are not claimed",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "Finite C1 Response Reduction Theorem" in paper else "FAIL",
            "reduction theorem is written",
        ),
    ]

    print("C1 finite response matrix reduction audit")
    print("=========================================")
    print()
    print(f"sample_C33_u={summary.get('C33_M_u')}")
    print(f"sample_C33_d={summary.get('C33_M_d')}")
    print(f"sample_Delta_v={summary.get('Delta_v_ud')}")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
