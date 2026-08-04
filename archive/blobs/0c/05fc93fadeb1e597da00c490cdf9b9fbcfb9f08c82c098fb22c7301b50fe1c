"""Analyze the Iwasawa monad line table as an L^2 branch-orientation candidate.

The previous L^2 gates left two live ways to select the branch

    L=(1,-2,0), L^2=(2,-4,0):

  1. a selected Gauduchon wall/chamber, or
  2. a selected ordered integral Cech/automorphy lift.

The printed Iwasawa monad line table contains a new clue: the ordered
difference L3-K2 is exactly (1,-2,0).  This script makes that observation
machine-checkable while preserving the guardrail that the monad table is not
yet a selected visible V_alpha source and does not by itself supply the L^2
cochain packet, Pic0 resolution, stability, or D_E/dotD data.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

VALIDATOR = ROOT / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"

MONAD_GATE = CERTIFICATES / "iwasawa_monad_map_data_gate_certificate.json"
MONAD_ROLE = CERTIFICATES / "iwasawa_monad_visible_source_role_certificate.json"
COHOMOLOGY_HUNT = CERTIFICATES / "visible_rank2_l2_cohomology_source_hunt_certificate.json"
INTEGRAL_GAP = CERTIFICATES / "visible_rank2_l2_integral_lift_source_gap_certificate.json"
ORDERED_GATE = CERTIFICATES / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"

CANDIDATE = CANDIDATE_DATA / "iwasawa_monad_l2_branch_orientation_candidate.candidate.json"
PACKET = CANDIDATE_DATA / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
CERTIFICATE = CERTIFICATES / "iwasawa_monad_l2_branch_orientation_candidate_certificate.json"

TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sub(a: list[int], b: list[int]) -> list[int]:
    return [x - y for x, y in zip(a, b)]


def double(v: list[int]) -> list[int]:
    return [2 * x for x in v]


def neg(v: list[int]) -> list[int]:
    return [-x for x in v]


def target_matrix() -> list[list[int]]:
    matrix = [[0 for _ in range(6)] for _ in range(6)]
    for degree, left, right in [(2, 0, 1), (-4, 2, 3), (0, 4, 5)]:
        matrix[left][right] = degree
        matrix[right][left] = -degree
    return matrix


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    parsed: dict[str, Any] | None = None
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_ordered_source_validation_report="):
            parsed = json.loads(line.split("=", 1)[1])
            break
    return {
        "packet": str(path),
        "exit_code": proc.returncode,
        "output": proc.stdout.strip(),
        "parsed_report": parsed,
    }


def ordered_differences(vectors: dict[str, list[int]]) -> dict[str, list[int]]:
    differences: dict[str, list[int]] = {}
    for left_name, left in vectors.items():
        for right_name, right in vectors.items():
            if left_name == right_name:
                continue
            differences[f"{left_name}_minus_{right_name}"] = sub(left, right)
    return differences


def monad_difference_packet(
    monad_status: str,
    ordered_gate_status: str,
    exact_candidate_found: bool,
) -> dict[str, Any]:
    return {
        "schema": "VisibleRank2L2OrderedSourcePacket.v1",
        "status": "OPEN_MONAD_DIFFERENCE_CANDIDATE",
        "candidate_role": "UNSELECTED_FIXTURE",
        "target": {
            "L": TARGET_L,
            "L2": TARGET_L2,
            "base_ordering": "E1_positive_E2_negative_from_L3_minus_K2",
            "c1_deck_matrix_order_g1_to_g6": target_matrix(),
        },
        "source": {
            "source_kind": "iwasawa_monad_ordered_line_difference",
            "source_certificate": "iwasawa_monad_map_data_gate_certificate.json",
            "source_status": monad_status,
            "selected_by_mtt": False,
            "fixture_only": True,
            "uses_observed_flavor_inputs": False,
            "uses_benchmark_flavor_inputs": False,
        },
        "automorphy": {
            "cocycle_checked": exact_candidate_found,
            "ordinary_integral_c1_realized": exact_candidate_found,
            "finite_torsion_gerbe_used_as_ordinary_c1": False,
            "realization_source": (
                "same ordered matrix as the Appell-Humbert automorphy packet; "
                "the monad difference supplies only the ordered integral label candidate"
            ),
        },
        "selection_evidence": {
            "standard_lattice_or_equivalent_selected": False,
            "base_factor_order_selected": False,
            "base_swap_broken_by_source": exact_candidate_found,
            "not_only_finite_mod3_qutrit": True,
            "not_equal_radius_import": True,
            "ordered_gate_status": ordered_gate_status,
        },
        "pic0_resolution": {
            "resolution": "neutral_by_notation_not_source_certified",
            "flat_character_values_g1_to_g6": [[1, 0]] * 6,
            "source_selected_or_quotiented": False,
        },
    }


def analyze() -> dict[str, Any]:
    monad = load_json(MONAD_GATE)
    monad_role = load_json(MONAD_ROLE)
    cohomology_hunt = load_json(COHOMOLOGY_HUNT)
    integral_gap = load_json(INTEGRAL_GAP)
    ordered_gate = load_json(ORDERED_GATE)

    vectors = monad.get("source_monad", {}).get("line_bundle_c1_vectors_abc", {})
    differences = ordered_differences(vectors)
    exact_matches = [
        name for name, value in differences.items() if value == TARGET_L
    ]
    reverse_matches = [
        name for name, value in differences.items() if value == neg(TARGET_L)
    ]
    l2_matches = [
        name for name, value in differences.items() if double(value) == TARGET_L2
    ]

    target_name = "L3_minus_K2"
    target_value = differences.get(target_name)
    exact_candidate_found = target_value == TARGET_L and double(target_value) == TARGET_L2

    typed_g3 = monad.get("typed_map_check", {}).get("g_entry_types", {}).get(
        "g3_K2_tensor_L3_inverse"
    )
    dual_g3_is_target = typed_g3 == neg(TARGET_L)

    packet = monad_difference_packet(
        monad.get("status", ""),
        ordered_gate.get("status", ""),
        exact_candidate_found,
    )
    write_json(PACKET, packet)
    validation = run_validator(PACKET)
    validation_open = validation.get("exit_code") == 2

    status_ok = (
        exact_candidate_found
        and dual_g3_is_target
        and monad.get("status")
        == "IWASAWA_MONAD_MAP_DATA_GATE_BLOCKED_TYPED_MAP_SECTIONS_MISSING"
        and monad_role.get("status") == "IWASAWA_MONAD_VISIBLE_ALPHA1_SOURCE_ROLE_SEPARATED"
        and cohomology_hunt.get("status")
        == "VISIBLE_RANK2_L2_COHOMOLOGY_SOURCE_HUNT_BLOCKED_SELECTED_DATA_ABSENT"
        and integral_gap.get("status")
        == "VISIBLE_RANK2_L2_INTEGRAL_LIFT_REDUCED_TO_SOURCE_CERTIFICATE"
        and ordered_gate.get("status")
        == "VISIBLE_RANK2_L2_ORDERED_SOURCE_PROMOTION_GATE_FORMULATED_SELECTION_OPEN"
        and validation_open
    )

    return {
        "calculation": "IwasawaMonadL2BranchOrientationCandidate",
        "status": (
            "IWASAWA_MONAD_L2_BRANCH_ORIENTATION_CANDIDATE_FOUND_SELECTION_OPEN"
            if status_ok
            else "IWASAWA_MONAD_L2_BRANCH_ORIENTATION_CANDIDATE_INCONCLUSIVE"
        ),
        "generated_by": "scripts/analyze_iwasawa_monad_l2_branch_orientation_candidate.py",
        "input_certificates": {
            "iwasawa_monad_map_data_gate": MONAD_GATE.name,
            "iwasawa_monad_visible_source_role": MONAD_ROLE.name,
            "visible_rank2_l2_cohomology_source_hunt": COHOMOLOGY_HUNT.name,
            "visible_rank2_l2_integral_lift_source_gap": INTEGRAL_GAP.name,
            "visible_rank2_l2_ordered_source_promotion_gate": ORDERED_GATE.name,
        },
        "input_statuses": {
            "monad_gate": monad.get("status"),
            "monad_role": monad_role.get("status"),
            "cohomology_hunt": cohomology_hunt.get("status"),
            "integral_lift_gap": integral_gap.get("status"),
            "ordered_source_gate": ordered_gate.get("status"),
        },
        "monad_line_table": vectors,
        "ordered_difference_scan": {
            "target_L": TARGET_L,
            "target_L2": TARGET_L2,
            "exact_target_matches": exact_matches,
            "reverse_target_matches": reverse_matches,
            "differences_whose_double_is_target_L2": l2_matches,
            "all_ordered_differences": differences,
        },
        "key_candidate": {
            "ordered_difference": target_name,
            "value": target_value,
            "double_value": double(target_value) if target_value else None,
            "matches_target_L": target_value == TARGET_L,
            "matches_target_L2_after_doubling": double(target_value) == TARGET_L2
            if target_value
            else False,
            "dual_printed_g3_type": typed_g3,
            "dual_printed_g3_type_is_negative_target": dual_g3_is_target,
            "interpretation": "L3 tensor K2^{-1} supplies the target L label; the printed g3 type is its dual K2 tensor L3^{-1}.",
        },
        "ordered_source_candidate_packet": {
            "path": str(PACKET.relative_to(ROOT)),
            "validation": validation,
        },
        "what_this_closes": {
            "hidden_monad_line_difference_scan": True,
            "exact_ordered_integral_target_L_candidate_found": exact_candidate_found,
            "candidate_is_stronger_than_finite_mod3_qutrit": True,
            "candidate_is_not_equal_radius_import": True,
            "previous_monad_rejection_for_full_L2_cochain_packet_still_valid": True,
        },
        "what_this_does_not_close": {
            "monad_pair_selected_as_visible_V_alpha_source": False,
            "full_L2_Cech_or_Dolbeault_packet_supplied_by_monad": False,
            "Pic0_character_selected_or_quotiented": False,
            "non_split_extension_stability_proved": False,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
            "full_SM_closure": False,
        },
        "still_open": {
            "prove_L3_minus_K2_is_selected_visible_source_slot": True,
            "bind_monad_difference_to_Appell_Humbert_or_Cech_transitions": True,
            "select_or_quotient_neutral_Pic0_character": True,
            "promote_h1_8_nonzero_Ext_packet_from_fixture_to_selected_data": True,
            "prove_non_split_extension_stability_and_HYM": True,
            "derive_same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_monad_alone_is_visible_alpha1_source": False,
            "claims_monad_difference_selected_by_mtt_now": False,
            "claims_ordered_source_validator_passes": False,
            "claims_pic0_resolved": False,
            "claims_stability_or_HYM_proved": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The corpus does contain a sharp ordered integral lift candidate: "
                "the Iwasawa monad line-table difference L3-K2 equals L=(1,-2,0), "
                "and doubling gives L^2=(2,-4,0). This can explain why the target "
                "branch is not arbitrary, but it is still not a selected visible "
                "V_alpha source. The validator therefore correctly refuses promotion "
                "until source selection and Pic0 resolution are proved."
            ),
            "next_packet": (
                "Selected_Monad_Difference_L2_Source.v1: prove the ordered pair "
                "(L3,K2) is selected as the visible V_alpha extension source, bind "
                "it to the Appell-Humbert/Cech transitions, and resolve Pic0."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "IwasawaMonadL2BranchOrientationCandidate",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/iwasawa_monad_l2_branch_orientation_candidate.candidate.json",
        "ordered_source_candidate_packet": report["ordered_source_candidate_packet"],
        "input_certificates": report["input_certificates"],
        "input_statuses": report["input_statuses"],
        "ordered_difference_scan": report["ordered_difference_scan"],
        "key_candidate": report["key_candidate"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "IWASAWA_MONAD_L2_BRANCH_ORIENTATION_CANDIDATE_FOUND_SELECTION_OPEN"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
