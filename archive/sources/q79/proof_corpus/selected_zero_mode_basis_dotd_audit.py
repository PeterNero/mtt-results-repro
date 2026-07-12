"""Audit the selected zero-mode basis and dotD interface."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "selected_zero_mode_basis_dotd_interface_certificate.json"
PAPER = ROOT / "Selected_Zero_Mode_Basis_and_dotD_Interface_v1.md"


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


def none_or_false_open(slot: dict[str, Any]) -> bool:
    required_keys = [
        "selected_operator_D",
        "domain_and_bundle",
        "ordered_zero_mode_basis",
        "L2_inner_product_matrix",
        "projector_P",
        "complement_Q",
        "reduced_green_operator_G",
        "complement_gap_or_error_bound",
        "dotD_alpha1",
    ]
    return all(slot.get(key) is None for key in required_keys) and slot.get(
        "horizontal_gauge_verified"
    ) is False


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    seed = load_json(CERT_DIR / "iwasawa_rank_one_yukawa_seed_certificate.json")
    higgs = load_json(CERT_DIR / "single_higgs_channel_projection_certificate.json")
    c1 = load_json(CERT_DIR / "c1_iwasawa_rplus_support_certificate.json")
    finite = load_json(CERT_DIR / "c1_finite_response_matrix_reduction_certificate.json")
    routes = load_json(CERT_DIR / "matrix_construction_routes_certificate.json")

    expected_slots = {"Q", "u", "d", "L", "e", "N", "H"}
    expected_sectors = {
        "u": ("Q", "u", "H"),
        "d": ("Q", "d", "H"),
        "e": ("L", "e", "H"),
        "nuD": ("L", "N", "H"),
    }
    expected_terms = {
        "theta_overlap_variation",
        "left_zero_mode_response",
        "right_zero_mode_response",
        "higgs_zero_mode_response",
        "explicit_vertex",
        "basis_connection",
    }

    slots = cert.get("basis_slots", {})
    sectors = cert.get("sector_map", {})
    output = cert.get("primitive_contraction_output_contract", {})
    completion = cert.get("completion_gates", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    sector_map_ok = all(
        sectors.get(sector, {}).get("left_slot") == left
        and sectors.get(sector, {}).get("right_slot") == right
        and sectors.get(sector, {}).get("higgs_slot") == higgs_slot
        for sector, (left, right, higgs_slot) in expected_sectors.items()
    )
    family_dimensions_ok = all(
        slots.get(slot, {}).get("kind") == "family"
        and slots.get(slot, {}).get("required_kernel_dimension") == 3
        for slot in ["Q", "u", "d", "L", "e", "N"]
    )
    higgs_slot_ok = (
        slots.get("H", {}).get("kind") == "single_higgs_carrier"
        and slots.get("H", {}).get("required_kernel_dimension") == 1
        and slots.get("H", {}).get("sector_conjugations", {}).get("d") == "H^dagger"
        and slots.get("H", {}).get("sector_conjugations", {}).get("u") == "H"
    )
    all_slots_open = all(none_or_false_open(slot) for slot in slots.values())
    completion_open = all(value is False for value in completion.values())
    guardrails_ok = (
        guardrails.get("uses_execution_ii_entries") is False
        and guardrails.get("uses_observed_masses_or_mixings") is False
        and guardrails.get("allows_free_dotD_knobs") is False
        and guardrails.get("allows_scalar_fourier_central_circle_zero_modes") is False
        and guardrails.get("keeps_q79_restricted_to_selected_channel_character_rule") is True
    )

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "SELECTED_ZERO_MODE_DOTD_INTERFACE_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "depends on route ledger",
            "PASS"
            if routes.get("verdict", {}).get("next_artifact")
            == "Selected Zero-Mode Basis and dotD Certificate"
            and "matrix_construction_routes_certificate.json" in cert.get("depends_on", [])
            else "FAIL",
            "route ledger points to this interface",
        ),
        Gate(
            "closed seed imported but limited",
            "PASS"
            if seed.get("tree_level_seed", {}).get("lambda_123_after_rephasing") == 1
            and cert.get("closed_inputs", {})
            .get("rank_one_seed", {})
            .get("limitation")
            else "FAIL",
            "rank-one seed is not promoted to all SM slots",
        ),
        Gate(
            "single Higgs projection imported",
            "PASS"
            if higgs.get("higgs_doublet_embedding", {}).get("H_u") == "H"
            and higgs.get("higgs_doublet_embedding", {}).get("H_d") == "H^dagger"
            and sectors.get("d", {}).get("higgs_projection") == "H^dagger"
            else "FAIL",
            "H_u/H_d sector conjugation recorded",
        ),
        Gate(
            "C1 alpha1 driver imported",
            "PASS"
            if "alpha_1" in cert.get("closed_inputs", {}).get("c1_driver", {}).get("formula", "")
            and c1.get("rplus_support", {}).get("alpha_2_component") == 0
            and c1.get("rplus_support", {}).get("alpha_3_component") == 0
            else "FAIL",
            "single invariant C1 driver row",
        ),
        Gate(
            "horizontal response rule agrees",
            "PASS"
            if cert.get("closed_inputs", {})
            .get("horizontal_response_rule", {})
            .get("formula")
            == "dotPsi_a,i = -G_a Q_a dotD_a Psi_a,i"
            and "dotPsi_a,i = - G_a Q_a dotD_a Psi_a,i"
            in finite.get("finite_reduction_theorem", {}).get(
                "horizontal_zero_mode_rule", ""
            )
            else "FAIL",
            "Green-operator rule imported",
        ),
        Gate(
            "slot ids",
            "PASS" if set(slots) == expected_slots else "FAIL",
            ", ".join(sorted(slots)),
        ),
        Gate(
            "sector map",
            "PASS" if sector_map_ok else "FAIL",
            str(sectors),
        ),
        Gate(
            "family dimensions",
            "PASS" if family_dimensions_ok else "FAIL",
            "Q,u,d,L,e,N each require dimension 3",
        ),
        Gate(
            "Higgs slot",
            "PASS" if higgs_slot_ok else "FAIL",
            str(slots.get("H", {})),
        ),
        Gate(
            "slot values remain open",
            "OPEN" if all_slots_open else "FAIL",
            "all D, basis, metric, projector, Green, gap, and dotD values are absent",
        ),
        Gate(
            "dotD selection rule",
            "PASS"
            if cert.get("dotD_selection_rule", {}).get("not_a_free_knob") is True
            and "Hess_Xi" in cert.get("dotD_selection_rule", {}).get(
                "deltaTheta_equation", ""
            )
            else "FAIL",
            "dotD is derivative along selected C1 path",
        ),
        Gate(
            "primitive output contract",
            "PASS"
            if output.get("target_file")
            == "certificates/selected_c1_primitive_contractions.template.json"
            and output.get("calculator") == "scripts/compute_c1_response_matrices.py"
            and set(output.get("required_terms_per_sector", [])) == expected_terms
            else "FAIL",
            str(output),
        ),
        Gate(
            "completion gates remain open",
            "OPEN" if completion_open else "FAIL",
            str(completion),
        ),
        Gate(
            "guardrails forbid proxy data",
            "PASS" if guardrails_ok else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict closes interface only",
            "PASS"
            if verdict.get("closes_zero_mode_dotD_input_contract") is True
            and verdict.get("closes_sector_resolved_zero_mode_values") is False
            and verdict.get("closes_dotD_operator_values") is False
            and verdict.get("closes_primitive_contraction_values") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records interface",
            "PASS"
            if "Required Data Per Slot" in paper
            and "dotD Is Not A New Knob" in paper
            and "Completion Gate" in paper
            else "FAIL",
            "paper has slot, dotD, and completion sections",
        ),
        Gate(
            "paper refuses matrix claim",
            "PASS"
            if "It does not compute the matrices yet." in paper
            and "no Execution II benchmark entries" in paper
            else "FAIL",
            "no numerical matrices claimed",
        ),
    ]

    print("Selected zero-mode basis and dotD interface audit")
    print("=================================================")
    print()
    print(f"slot_count={len(slots)}")
    print(f"sector_count={len(sectors)}")
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
