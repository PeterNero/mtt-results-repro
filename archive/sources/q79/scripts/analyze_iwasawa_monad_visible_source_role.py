"""Separate the Iwasawa three-family monad from the visible alpha_1 source.

The printed Iwasawa monad is valuable as a matter/zero-mode candidate: its
topological data support c1=0, c2=0, and integral c3=6.  The visible curvature
source target, after the stable-source sign gate, is c1=0 and c2=+4 alpha_1.

Therefore the monad cannot by itself be the selected visible Chern-Weil source.
It may still provide matter zero modes once typed maps are supplied, but the
visible source row needs an additional selected nonabelian/Route-C source or a
larger bundle construction whose total c2 is recomputed.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

MONAD_GATE = CERTIFICATES / "iwasawa_monad_map_data_gate_certificate.json"
RANK_ONE_SEED = CERTIFICATES / "iwasawa_rank_one_yukawa_seed_certificate.json"
VISIBLE_SIGN_GATE = CERTIFICATES / "visible_stable_source_sign_gate_certificate.json"

CANDIDATE = CANDIDATE_DATA / "iwasawa_monad_visible_source_role.candidate.json"
CERTIFICATE = CERTIFICATES / "iwasawa_monad_visible_source_role_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def analyze() -> dict[str, Any]:
    monad = load_json(MONAD_GATE)
    rank_one = load_json(RANK_ONE_SEED)
    sign_gate = load_json(VISIBLE_SIGN_GATE)

    topology = monad.get("topological_cern_check", {})
    monad_c1_zero = topology.get("c1_zero") is True
    monad_ch2_zero = topology.get("ch2_zero") is True
    monad_c2_coeff_alpha1 = 0 if monad_c1_zero and monad_ch2_zero else None
    monad_c3 = topology.get("integral_c3")

    required = sign_gate.get("admissible_stable_sign_branch", {})
    required_c2_coeff_alpha1 = required.get("math_c2_coeff_alpha1")
    required_math_ch2_coeff_alpha1 = required.get("math_ch2_coeff_alpha1")

    role_separated = (
        monad.get("status")
        == "IWASAWA_MONAD_MAP_DATA_GATE_BLOCKED_TYPED_MAP_SECTIONS_MISSING"
        and rank_one.get("status") == "RANK_ONE_TREE_SEED_CLOSED_CORRECTIONS_OPEN"
        and sign_gate.get("status")
        == "VISIBLE_STABLE_SOURCE_SIGN_CONVENTION_GATE_CLOSED_SOURCE_OPEN"
        and monad_c2_coeff_alpha1 == 0
        and required_c2_coeff_alpha1 == 4
        and required_math_ch2_coeff_alpha1 == -4
    )

    return {
        "calculation": "IwasawaMonadVisibleSourceRoleSeparation",
        "status": (
            "IWASAWA_MONAD_VISIBLE_ALPHA1_SOURCE_ROLE_SEPARATED"
            if role_separated
            else "IWASAWA_MONAD_VISIBLE_ALPHA1_SOURCE_ROLE_NOT_VERIFIED"
        ),
        "generated_by": "scripts/analyze_iwasawa_monad_visible_source_role.py",
        "inputs": {
            "iwasawa_monad_map_data_gate_certificate": MONAD_GATE.name,
            "iwasawa_rank_one_yukawa_seed_certificate": RANK_ONE_SEED.name,
            "visible_stable_source_sign_gate_certificate": VISIBLE_SIGN_GATE.name,
        },
        "monad_role": {
            "sequence": monad.get("source_monad", {}).get("sequence"),
            "c1_zero": monad_c1_zero,
            "ch2_zero": monad_ch2_zero,
            "c2_coeff_alpha1": monad_c2_coeff_alpha1,
            "integral_c3": monad_c3,
            "supports_net_chirality_three": topology.get("supports_net_chirality_three"),
            "constructs_zero_mode_basis_now": topology.get("constructs_zero_mode_basis"),
            "rank_one_seed_status": rank_one.get("status"),
            "honest_role": (
                "matter/zero-mode and rank-one E6 seed candidate, pending typed "
                "monad maps and cohomology representatives"
            ),
        },
        "visible_source_role": {
            "required_c1": 0,
            "required_c2_coeff_alpha1": required_c2_coeff_alpha1,
            "required_math_ch2_coeff_alpha1": required_math_ch2_coeff_alpha1,
            "required_trace_row": "(1/(8*pi^2))*Tr(F wedge F)=+4 alpha_1",
            "source_classes_remaining": [
                "selected nonabelian stable bundle/sheaf",
                "selected Route-C HYM/Strominger solve",
                "larger visible bundle whose total c2=+4 alpha_1 is recomputed",
            ],
        },
        "role_comparison": {
            "monad_c2_minus_required_c2_coeff_alpha1": (
                None
                if monad_c2_coeff_alpha1 is None or required_c2_coeff_alpha1 is None
                else monad_c2_coeff_alpha1 - required_c2_coeff_alpha1
            ),
            "monad_alone_realizes_visible_alpha1_source": False,
            "monad_can_still_be_matter_zero_mode_source": True,
            "larger_bundle_escape_requires_new_calculation": True,
            "same_source_warning": (
                "If the physical visible bundle is enlarged beyond the printed monad, "
                "the zero-mode basis, projectors, D_E, dotD, Riesz/Green, and Chern-Weil "
                "row must all be recomputed from that enlarged selected source."
            ),
        },
        "calculation_results": {
            "monad_topology_loaded": monad_c1_zero and monad_ch2_zero and monad_c3 == 6,
            "visible_c2_target_loaded": required_c2_coeff_alpha1 == 4,
            "printed_monad_not_visible_alpha1_source": role_separated,
            "printed_monad_retained_as_matter_seed_candidate": True,
            "larger_visible_bundle_or_route_c_still_open": True,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "do_not_reuse_c2_zero_monad_as_c2_4_alpha1_source": role_separated,
            "matter_seed_role_separated_from_visible_curvature_source_role": True,
            "larger_bundle_escape_requires_recomputed_total_invariants": True,
        },
        "still_open": {
            "typed_monad_sections_for_matter_zero_modes": True,
            "selected_nonabelian_visible_source_with_c2_4_alpha1": True,
            "selected_route_c_visible_source_for_trace_row": True,
            "enlarged_visible_bundle_total_c2_recalculation": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_monad_is_visible_alpha1_source": False,
            "claims_typed_monad_maps_supplied": False,
            "claims_selected_zero_modes_constructed": False,
            "claims_selected_visible_source_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The Iwasawa three-family monad should stay in the matter/zero-mode "
                "lane. Its topological data have c2=0, while the visible "
                "Chern-Weil source now requires c2=+4 alpha_1. Reusing the monad "
                "alone as the visible alpha_1 source would be a class mismatch."
            ),
            "next_action": (
                "Either construct a separate selected visible source with c2=+4 "
                "alpha_1, or enlarge the visible bundle and recompute the total "
                "Chern class plus all zero-mode/operator data from that one source."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "IwasawaMonadVisibleSourceRoleSeparation",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/iwasawa_monad_visible_source_role.candidate.json",
        "inputs": report["inputs"],
        "monad_role": report["monad_role"],
        "visible_source_role": report["visible_source_role"],
        "role_comparison": report["role_comparison"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "IWASAWA_MONAD_VISIBLE_ALPHA1_SOURCE_ROLE_SEPARATED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
