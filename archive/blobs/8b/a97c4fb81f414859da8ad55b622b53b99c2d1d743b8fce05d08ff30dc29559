"""Analyze the additive nonabelian source-factor route.

After the role separation, the printed Iwasawa monad may still serve the
matter/zero-mode role, but it cannot itself be the visible alpha_1 curvature
source because its c2 is zero.  This script checks the next conservative
construction: keep the monad as a matter candidate and add a separate
nonabelian zero-slope factor V_alpha with c2=+4 alpha_1 and c3=0.

This closes only the topological accounting for such a route.  It does not
construct V_alpha, prove MTT selection, solve HYM/Strominger, preserve the SM
commutant, or derive same-source D_E/dotD data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

MONAD_ROLE = CERTIFICATES / "iwasawa_monad_visible_source_role_certificate.json"
SIGN_GATE = CERTIFICATES / "visible_stable_source_sign_gate_certificate.json"
SPLIT_NO_GO = CERTIFICATES / "visible_split_line_hym_no_go_certificate.json"
MONAD_GATE = CERTIFICATES / "iwasawa_monad_map_data_gate_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_additive_source_factor_route.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_additive_source_factor_route_certificate.json"


Vector3 = list[int]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def add(left: Vector3, right: Vector3) -> Vector3:
    return [left[index] + right[index] for index in range(3)]


def analyze() -> dict[str, Any]:
    monad_role_cert = load_json(MONAD_ROLE)
    sign_gate = load_json(SIGN_GATE)
    split_no_go = load_json(SPLIT_NO_GO)
    monad_gate = load_json(MONAD_GATE)

    monad_role = monad_role_cert.get("monad_role", {})
    visible_target = monad_role_cert.get("visible_source_role", {})
    monad_topology = monad_gate.get("topological_cern_check", {})

    monad_c1: Vector3 = [0, 0, 0]
    monad_c2: Vector3 = [0, 0, 0]
    monad_c3 = monad_topology.get("integral_c3")

    source_factor_c1: Vector3 = [0, 0, 0]
    source_factor_c2: Vector3 = [
        int(visible_target.get("required_c2_coeff_alpha1", 0)),
        0,
        0,
    ]
    source_factor_c3 = 0

    total_c1 = add(monad_c1, source_factor_c1)
    total_c2 = add(monad_c2, source_factor_c2)
    total_c3 = monad_c3 + source_factor_c3 if isinstance(monad_c3, int) else None

    target_c2 = [4, 0, 0]
    topological_accounting_passes = (
        monad_role_cert.get("status") == "IWASAWA_MONAD_VISIBLE_ALPHA1_SOURCE_ROLE_SEPARATED"
        and sign_gate.get("status")
        == "VISIBLE_STABLE_SOURCE_SIGN_CONVENTION_GATE_CLOSED_SOURCE_OPEN"
        and split_no_go.get("status")
        == "VISIBLE_SPLIT_LINE_HYM_SOURCE_NO_GO_NONABELIAN_OR_ROUTE_C_REQUIRED"
        and monad_role.get("c2_coeff_alpha1") == 0
        and source_factor_c2 == target_c2
        and total_c1 == [0, 0, 0]
        and total_c2 == target_c2
        and total_c3 == 6
    )

    return {
        "calculation": "VisibleAdditiveSourceFactorRoute",
        "status": (
            "VISIBLE_ADDITIVE_SOURCE_FACTOR_TOPOLOGY_FORMULATED_SELECTION_OPEN"
            if topological_accounting_passes
            else "VISIBLE_ADDITIVE_SOURCE_FACTOR_TOPOLOGY_NOT_VERIFIED"
        ),
        "generated_by": "scripts/analyze_visible_additive_source_factor_route.py",
        "inputs": {
            "iwasawa_monad_visible_source_role_certificate": MONAD_ROLE.name,
            "visible_stable_source_sign_gate_certificate": SIGN_GATE.name,
            "visible_split_line_hym_no_go_certificate": SPLIT_NO_GO.name,
            "iwasawa_monad_map_data_gate_certificate": MONAD_GATE.name,
        },
        "route_definition": {
            "total_bundle_schema": "E_total = E_matter_monad direct_sum V_alpha",
            "matter_factor_role": "Iwasawa monad, retained only as matter/zero-mode candidate",
            "source_factor_role": "nonabelian zero-slope alpha_1 curvature source",
            "source_factor_minimal_target": {
                "c1": source_factor_c1,
                "c2": source_factor_c2,
                "c3": source_factor_c3,
                "preferred_minimal_rank": 2,
                "preferred_reason": "SU(2)-type source has c3=0 and can be genuinely nonabelian",
            },
            "forbidden_source_factor_classes": [
                "finite split line-bundle source",
                "diagonal Cartan HYM source",
                "positive mathematical ch2 source",
                "the printed c2=0 matter monad by itself",
            ],
        },
        "chern_class_accounting": {
            "direct_sum_formula": {
                "c1_total": "c1(E)+c1(V)",
                "c2_total": "c2(E)+c2(V)+c1(E)c1(V)",
                "c3_total": "c3(E)+c3(V)+c2(E)c1(V)+c1(E)c2(V)",
            },
            "matter_monad": {
                "c1": monad_c1,
                "c2": monad_c2,
                "c3": monad_c3,
            },
            "source_factor": {
                "c1": source_factor_c1,
                "c2": source_factor_c2,
                "c3": source_factor_c3,
            },
            "total": {
                "c1": total_c1,
                "c2": total_c2,
                "c3": total_c3,
            },
            "target": {
                "c1": [0, 0, 0],
                "c2": target_c2,
                "c3_preserve_matter_index": 6,
            },
            "topological_accounting_passes": topological_accounting_passes,
        },
        "hym_polystability_contract": {
            "if_both_factors_selected_stable_zero_slope": (
                "E_matter direct_sum V_alpha is polystable and admits a block HYM "
                "connection in the Li-Yau/Donaldson-Uhlenbeck-Yau sense appropriate "
                "to the selected balanced/Kahler slice"
            ),
            "current_status": "conditional only",
            "missing_for_E_matter": [
                "typed monad maps",
                "exactness/local-freeness or controlled sheaf singularities",
                "selected zero-slope stability proof",
                "selected HYM connection/operator",
            ],
            "missing_for_V_alpha": [
                "selected nonabelian stable/sheaf construction",
                "c2=+4 alpha_1 representative",
                "zero-slope/HYM proof",
                "source-derived Chern-Weil representative",
            ],
        },
        "sm_operator_warning": {
            "topology_is_not_operator_closure": True,
            "hidden_sector_only_would_not_close_visible_operator_source": True,
            "direct_sum_can_make_dotD_block_diagonal": True,
            "required_extra_bridge": (
                "prove that the selected V_alpha deformation enters the visible "
                "matter D_E/dotD response through the total selected E8/Strominger "
                "background, or recompute the matter basis from an enlarged "
                "indecomposable selected source"
            ),
            "representation_commutant_gate": (
                "adding a nonabelian factor can change the E8 commutant; the SM/E6/SU5 "
                "embedding and sector dictionary must be recomputed or protected"
            ),
        },
        "calculation_results": {
            "topological_additive_route_formulated": topological_accounting_passes,
            "matter_monad_c2_zero_retained": monad_role.get("c2_coeff_alpha1") == 0,
            "source_factor_target_c2_4_alpha1": source_factor_c2 == target_c2,
            "total_c3_preserves_three_net_families": total_c3 == 6,
            "split_line_source_still_forbidden": split_no_go.get("calculation_results", {}).get(
                "split_line_or_cartan_hym_source_ruled_out"
            )
            is True,
            "source_factor_constructed": False,
            "selected_hym_polystable_total_constructed": False,
            "sm_commutant_or_sector_dictionary_protected": False,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "additive_c2_accounting_for_matter_plus_source": topological_accounting_passes,
            "minimal_source_factor_target_identified": True,
            "hidden_or_block_diagonal_shortcut_flagged": True,
            "larger_bundle_escape_made_auditable": True,
        },
        "still_open": {
            "construct_selected_V_alpha_with_c1_0_c2_4_alpha1_c3_0": True,
            "prove_zero_slope_stability_or_allowed_sheaf_HYM_for_V_alpha": True,
            "supply_typed_monad_maps_if_E_matter_retained": True,
            "prove_polystable_total_or_replace_by_indecomposable_enlarged_source": True,
            "protect_or_recompute_E8_commutant_and_SM_sector_dictionary": True,
            "derive_same_total_source_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_source_factor_exists": False,
            "claims_total_hym_solution_exists": False,
            "claims_hidden_source_closes_visible_operator": False,
            "claims_direct_sum_dotd_closes_flavor": False,
            "claims_sm_commutant_preserved": False,
            "claims_typed_monad_maps_supplied": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "There is a clean topological route: keep the c2=0 Iwasawa monad "
                "as a matter candidate and add a genuinely nonabelian source factor "
                "V_alpha with c1=0, c2=+4 alpha_1, c3=0. This preserves the net "
                "c3=6 matter index while supplying the visible c2 row. But this is "
                "only accounting, not source selection or SM matrix closure."
            ),
            "next_action": (
                "Try to construct or obstruct the minimal V_alpha factor. If it is "
                "separate, prove the representation/commutant and same-total-source "
                "D_E/dotD bridge; otherwise build an indecomposable enlarged source "
                "and recompute all invariants and operators from it."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleAdditiveSourceFactorRoute",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_additive_source_factor_route.candidate.json",
        "inputs": report["inputs"],
        "route_definition": report["route_definition"],
        "chern_class_accounting": report["chern_class_accounting"],
        "hym_polystability_contract": report["hym_polystability_contract"],
        "sm_operator_warning": report["sm_operator_warning"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "VISIBLE_ADDITIVE_SOURCE_FACTOR_TOPOLOGY_FORMULATED_SELECTION_OPEN" else 1


if __name__ == "__main__":
    raise SystemExit(main())
