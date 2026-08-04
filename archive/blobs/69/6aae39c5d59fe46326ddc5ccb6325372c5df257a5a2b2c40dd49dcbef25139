"""Audit the visible rank-two L2 Ext H1 gate and validator."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_rank2_l2_ext_h1_gate.py"
VALIDATOR = REPO / "scripts" / "validate_visible_rank2_l2_cohomology.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_ext_h1_gate.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_ext_h1_gate_certificate.json"
TEMPLATE = REPO / "certificates" / "visible_rank2_l2_cohomology_data.template.json"
PAPER = ROOT / "Visible_Rank2_L2_Ext_H1_Gate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def run_validator(path: Path) -> tuple[int, str]:
    proc = run([sys.executable, str(VALIDATOR), str(path)])
    return proc.returncode, proc.stdout


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def fixture_packet(exact_vector: bool = False) -> dict[str, Any]:
    eta = [1, 0] if exact_vector else [0, 1]
    return {
        "schema": "VisibleRank2L2CohomologyData.v1",
        "status": "COMPLETE",
        "candidate_role": "UNSELECTED_FIXTURE",
        "target": {
            "extension_sequence": "0 -> L -> V_alpha -> L^{-1} -> 0",
            "l_vector_abc": [1, -2, 0],
            "c1_L_squared_vector_abc": [2, -4, 0],
            "c1_L_squared_square_alpha_coeffs": [-16, 0, 0],
            "c2_extension_alpha_coeffs": [4, 0, 0],
        },
        "source": {
            "source_kind": "finite_fixture",
            "selected_by_mtt": False,
            "fixture_only": True,
            "source_certificate": "",
            "uses_observed_flavor_inputs": False,
            "uses_benchmark_flavor_inputs": False,
        },
        "cochain_complex": {
            "field": "Q",
            "basis_labels_C0": ["u0"],
            "basis_labels_C1": ["v_exact", "v_ext"],
            "basis_labels_C2": ["w0"],
            "d0": {"matrix": [[1], [0]]},
            "d1": {"matrix": [[0, 0]]},
        },
        "reported_cohomology": {
            "rank_d0": 1,
            "rank_d1": 0,
            "dim_ker_d1": 2,
            "h1": 1,
            "nonzero_extension_class_label": "eta",
            "extension_class_vector_C1": eta,
        },
        "acceptance_tests": {
            "d1_d0_zero": True,
            "h1_positive": True,
            "extension_class_closed": True,
            "extension_class_not_exact": not exact_vector,
            "derived_without_observed_flavor_inputs": True,
        },
    }


def run_temp_packet(data: dict[str, Any]) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "visible_rank2_h1_fixture.json"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return run_validator(path)


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    template = load_json(TEMPLATE)
    paper = read(PAPER)
    validator_text = read(VALIDATOR)

    template_code, template_output = run_validator(TEMPLATE)
    fixture_code, fixture_output = run_temp_packet(fixture_packet())
    exact_code, exact_output = run_temp_packet(fixture_packet(exact_vector=True))

    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    contract = cert.get("finite_computation_contract", {})
    preferred = cert.get("preferred_first_target", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("template exists", "PASS" if TEMPLATE.exists() else "FAIL", str(TEMPLATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status h1 gate",
            "PASS"
            if cert.get("status") == "VISIBLE_RANK2_L2_EXT_H1_VALIDATOR_FORMULATED_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("calculation_results") == cert.get("calculation_results")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "preferred L2 target",
            "PASS"
            if preferred.get("l_vector_abc") == [1, -2, 0]
            and preferred.get("c1_L_squared_vector_abc") == [2, -4, 0]
            and preferred.get("c1_L_squared_square_alpha_coeffs") == [-16, 0, 0]
            and preferred.get("c2_extension_alpha_coeffs") == [4, 0, 0]
            else "FAIL",
            str(preferred),
        ),
        Gate(
            "contract computes h1",
            "PASS"
            if contract.get("computed_h1_formula") == "h1 = dim ker(d1) - rank(d0)"
            and "eta not in im(d0)" in contract.get("nonzero_ext_class_test", "")
            else "FAIL",
            str(contract),
        ),
        Gate(
            "validator script exists",
            "PASS"
            if VALIDATOR.exists()
            and contains_all(
                validator_text,
                [
                    "VisibleRank2L2CohomologyData.v1",
                    "h1 = dim_ker_d1 - rank_d0",
                    "extension_class_vector_C1",
                    "return 2",
                ],
            )
            else "FAIL",
            str(VALIDATOR),
        ),
        Gate(
            "open template refused",
            "PASS"
            if template_code == 2 and "packet is OPEN" in template_output
            and template.get("status") == "OPEN"
            else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "fixture h1 passes algebra",
            "PASS"
            if fixture_code == 0
            and "validation PASS" in fixture_output
            and "does not promote selected MTT data" in fixture_output
            else "FAIL",
            fixture_output.strip(),
        ),
        Gate(
            "exact vector rejected",
            "PASS"
            if exact_code == 1 and "lies in im(d0)" in exact_output
            else "FAIL",
            exact_output.strip(),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("rank2_route_imported") is True
            and calc.get("validator_formulated") is True
            and calc.get("H1_value_computed_from_selected_data") is False
            and calc.get("selected_nonzero_ext_class_constructed") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closes exact interface",
            "PASS"
            if closes.get("exact_finite_input_format_for_H1_X_L_squared") is True
            and closes.get("exact_nonzero_Ext_acceptance_test") is True
            and closes.get("false_topology_only_H1_claim_blocked") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if open_items.get("fill_template_with_selected_Cech_or_Dolbeault_data") is True
            and open_items.get("compute_actual_h1_for_L_squared") is True
            and open_items.get("full_SM_closure") is True
            else "FAIL",
            str(open_items),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "Ext^1(L^{-1},L) = H^1(X,L^2)",
                    "c1(L^2) = (2,-4,0)",
                    "scripts/validate_visible_rank2_l2_cohomology.py",
                    "h1 = dim ker(d1) - rank(d0)",
                    "actual H^1(X,L^2) value",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 Ext H1 gate audit")
    print("=====================================")
    print()
    print(f"template_exit={template_code}")
    print(f"fixture_exit={fixture_code}")
    print(f"exact_vector_exit={exact_code}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
