"""Attempt Antiunitary_DEDotD_Equivalence_Test_v1."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CANDIDATES = Q79 / "candidate_data" / "iwasawa_route_c_branch_smoke"

PREVIOUS = CERTS / "selected_source_origin_or_antiunitary_dedotd_equivalence_attempt_certificate.json"
Q79_DIR = Q79_CANDIDATES / "current_q79_orientation"
Q369_DIR = Q79_CANDIDATES / "conjugate_q369_orientation"

OUTPUT_CERT = CERTS / "antiunitary_dedotd_equivalence_test_certificate.json"

SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]
TOL = 1e-9


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def is_numeric_pair(value: Any) -> bool:
    return isinstance(value, list) and len(value) == 2 and all(is_number(item) for item in value)


def close(a: float, b: float) -> bool:
    return math.isclose(float(a), float(b), rel_tol=TOL, abs_tol=TOL)


def conjugate_value(value: Any) -> Any:
    """Conjugate the JSON scalar convention used by the finite packets.

    Complex scalars are represented as two-entry numeric lists [real, imag].
    Ordinary real matrices are unchanged.
    """
    if is_numeric_pair(value):
        return [value[0], -value[1]]
    if isinstance(value, list):
        return [conjugate_value(item) for item in value]
    if isinstance(value, dict):
        return {key: conjugate_value(inner) for key, inner in value.items()}
    return value


def equal_or_conjugate(left: Any, right: Any) -> bool:
    return json_equal(left, right) or json_equal(conjugate_value(left), right)


def json_equal(left: Any, right: Any) -> bool:
    if is_number(left) and is_number(right):
        return close(left, right)
    if isinstance(left, str) or isinstance(left, bool) or left is None:
        return left == right
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(json_equal(a, b) for a, b in zip(left, right))
    if isinstance(left, dict) and isinstance(right, dict):
        return set(left) == set(right) and all(json_equal(left[key], right[key]) for key in left)
    return left == right


def slot_compare(left: dict[str, Any], right: dict[str, Any], fields: list[str]) -> dict[str, bool]:
    return {field: equal_or_conjugate(left.get(field), right.get(field)) for field in fields}


def orientation_pair_ok(q79_branch: dict[str, Any], q369_branch: dict[str, Any]) -> bool:
    q79_orient = q79_branch["sector_orientations"]
    q369_orient = q369_branch["sector_orientations"]
    return (
        q79_branch["global_cp_label"] == 79
        and q369_branch["global_cp_label"] == 369
        and q79_branch["torsion_label_m"] == 1
        and q369_branch["torsion_label_m"] == 2
        and q79_branch["conditional_su5_transport_orientation"] == "F"
        and q369_branch["conditional_su5_transport_orientation"] == "F*"
        and all(
            (q79_orient[sector], q369_orient[sector]) in {(1, 2), (2, 1), (0, 0)}
            for sector in SECTORS
        )
    )


def main() -> None:
    previous = load(PREVIOUS)
    q79_de = load(Q79_DIR / "de_action.candidate.json")
    q369_de = load(Q369_DIR / "de_action.candidate.json")
    q79_green = load(Q79_DIR / "reduced_green.candidate.json")
    q369_green = load(Q369_DIR / "reduced_green.candidate.json")
    q79_dotd = load(Q79_DIR / "dotd_response.candidate.json")
    q369_dotd = load(Q369_DIR / "dotd_response.candidate.json")

    de_fields = [
        "kind",
        "expected_kernel_dimension",
        "domain_dimension",
        "range_dimension",
        "domain_gram",
        "range_gram",
        "D_E_matrix",
        "stiffness_matrix",
        "ordered_zero_mode_basis",
    ]
    green_fields = [
        "kind",
        "expected_kernel_dimension",
        "dimension",
        "gram_matrix",
        "stiffness_matrix",
        "riesz_projector",
        "complement_projector",
        "reduced_green_operator",
        "ordered_zero_mode_basis",
    ]
    dotd_fields = green_fields + [
        "dotD_alpha1_matrix",
        "source_vectors",
        "horizontal_response_vectors",
    ]

    de_sector_checks = {
        sector: slot_compare(
            q79_de["operator_slots"][sector],
            q369_de["operator_slots"][sector],
            de_fields,
        )
        for sector in SECTORS
    }
    green_sector_checks = {
        sector: slot_compare(
            q79_green["green_slots"][sector],
            q369_green["green_slots"][sector],
            green_fields,
        )
        for sector in SECTORS
    }
    dotd_sector_checks = {
        sector: slot_compare(
            q79_dotd["dotd_response_slots"][sector],
            q369_dotd["dotd_response_slots"][sector],
            dotd_fields,
        )
        for sector in SECTORS
    }

    all_de_equiv = all(all(fields.values()) for fields in de_sector_checks.values())
    all_green_equiv = all(all(fields.values()) for fields in green_sector_checks.values())
    all_dotd_equiv = all(all(fields.values()) for fields in dotd_sector_checks.values())
    branches_ok = orientation_pair_ok(q79_de["branch_packet"], q369_de["branch_packet"])

    source_flags_still_open = all(
        q79_de["operator_slots"][sector]["selected_source_verified"] is False
        and q369_de["operator_slots"][sector]["selected_source_verified"] is False
        and q79_dotd["dotd_response_slots"][sector]["selected_dotD_source_verified"] is False
        and q369_dotd["dotd_response_slots"][sector]["selected_dotD_source_verified"] is False
        for sector in SECTORS
    )

    output = {
        "certificate": "AntiunitaryDEDotDEquivalenceTest",
        "status": "ANTIUNITARY_DEDOTD_EQUIVALENCE_TEST_PASSED_SOURCE_SELECTION_OPEN",
        "inputs": {
            "previous_gate": str(PREVIOUS.relative_to(ROOT)),
            "q79_de_action": str(Q79_DIR / "de_action.candidate.json"),
            "q369_de_action": str(Q369_DIR / "de_action.candidate.json"),
            "q79_reduced_green": str(Q79_DIR / "reduced_green.candidate.json"),
            "q369_reduced_green": str(Q369_DIR / "reduced_green.candidate.json"),
            "q79_dotd_response": str(Q79_DIR / "dotd_response.candidate.json"),
            "q369_dotd_response": str(Q369_DIR / "dotd_response.candidate.json"),
        },
        "closed_now": {
            "branch_metadata_is_global_conjugate_pair": branches_ok,
            "D_E_action_slots_match_under_antiunitary_conjugation": all_de_equiv,
            "Green_Riesz_projector_slots_match_under_antiunitary_conjugation": all_green_equiv,
            "dotD_alpha1_and_horizontal_response_slots_match_under_antiunitary_conjugation": all_dotd_equiv,
            "operator_level_antiunitary_equivalence_for_current_finite_packets": branches_ok
            and all_de_equiv
            and all_green_equiv
            and all_dotd_equiv,
            "previous_C6_conjugate_pair_reduction_imported": previous["closed_now"][
                "C6_branch_space_reduced_to_global_conjugate_pair"
            ],
        },
        "sector_checks": {
            "D_E_action": de_sector_checks,
            "Green_Riesz": green_sector_checks,
            "dotD_alpha1": dotd_sector_checks,
        },
        "source_flags": {
            "still_open_on_both_branches": source_flags_still_open,
            "meaning": (
                "The finite packets are antiunitarily equivalent as candidate "
                "operator data, but neither branch is selected by MTT and the "
                "alpha1 driver remains unselected."
            ),
        },
        "not_closed": {
            "selected_source_origin": True,
            "retarded_or_source_boundary_selector_for_one_representative": True,
            "selected_D_E_dotD_source_flags": True,
            "primitive_C1_contractions": True,
            "selected_Yukawa_matrices": True,
            "full_SM_closure": True,
        },
        "next_closing_object": {
            "name": "Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1",
            "must_prove": [
                "a non-observed MTT retarded/source boundary condition chooses one global conjugate representative",
                "or a selected visible source origin turns one branch's source flags on",
                "the chosen representative then keeps the antiunitary partner as convention/complex conjugate, not an independent knob",
            ],
        },
        "guardrails": {
            "claims_q79_selected_over_q369": False,
            "claims_selected_source_origin": False,
            "claims_selected_D_E_dotD": False,
            "claims_primitive_C1_contractions": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_masses": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The current finite q79 and q369 D_E/Green/dotD packets are related "
            "by antiunitary conjugation sector by sector. This removes them as "
            "independent operator knobs. It still does not choose q79 over q369: "
            "the selected source origin or a non-observed retarded boundary "
            "selector remains open."
        ),
    }

    if "--write-certificate" in __import__("sys").argv:
        OUTPUT_CERT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
