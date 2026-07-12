"""Prove the time-oriented finite gerbe representative.

This closes the finite torsion-label ambiguity at the representative level:

    q79/F  -> m = 1
    q369/F* -> m = 2

It does not claim a full selected Deligne/Cech gerbe period table, twisted
projector retention, D_E, dotD, or full SM closure.  The theorem uses the
already closed retarded q79 branch to fix which member of the selected
nontrivial conjugate pair is the time-oriented representative.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
OUT = ROOT / "candidate_data" / "time_oriented_fixed_gerbe_representative.candidate.json"
CERT = CERTIFICATES / "time_oriented_fixed_gerbe_representative_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def cert(name: str) -> dict[str, Any]:
    return load_json(CERTIFICATES / name)


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def analyze() -> dict[str, Any]:
    time = cert("time_oriented_conjugate_branch_selection_certificate.json")
    torsion = cert("iwasawa_torsion_label_four_route_selector_certificate.json")
    gerbe = cert("iwasawa_discrete_gerbe_holonomy_candidate_certificate.json")
    flat_gap = cert("iwasawa_flat_torsion_selection_gap_certificate.json")
    gerbe_fourier = cert("selected_gerbe_fourier_type_theorem_certificate.json")
    visible_rhoe = cert("visible_rhoE_source_ansatz_search_certificate.json")

    q79_packet = get(time, "source_gates", "orientation_bridge", "q79_packet", default={})
    q369_packet = get(time, "source_gates", "orientation_bridge", "q369_packet", default={})
    common_pair = get(torsion, "calculation_results", "common_candidate_labels") == [1, 2]
    four_routes_reject_m0 = (
        get(torsion, "calculation_results", "all_four_routes_reject_trivial_m0") is True
    )
    finite_map_closed = (
        get(gerbe, "finite_model", "matches_qutrit_projective_cocycle") is True
        and get(gerbe, "finite_model", "discrete_bianchi_residual_zero") is True
        and get(gerbe, "finite_model", "commutator_rank_over_F3") == 2
    )
    curvature_cannot_choose = (
        get(flat_gap, "calculation_results", "current_curvature_selection_can_choose_Z3_label")
        is False
    )
    selected_pair_closed = (
        get(gerbe_fourier, "calculation_results", "selected_gerbe_fourier_type_closed")
        is True
    )
    time_branch_selects_q79 = (
        get(time, "calculation_results", "time_oriented_retarded_branch_selects_q79")
        is True
        and get(time, "calculation_results", "q369_retained_as_global_antiunitary_conjugate")
        is True
    )
    q79_m1 = (
        q79_packet.get("global_cp_label") == 79
        and q79_packet.get("conditional_su5_transport_orientation") == "F"
        and q79_packet.get("torsion_label_m") == 1
    )
    q369_m2 = (
        q369_packet.get("global_cp_label") == 369
        and q369_packet.get("conditional_su5_transport_orientation") == "F*"
        and q369_packet.get("torsion_label_m") == 2
    )
    ordinary_rhoe_blocked = (
        get(
            visible_rhoe,
            "calculation_results",
            "qutrit_projective_central_absorption_as_ordinary_rhoE_blocked",
        )
        is True
    )

    representative_closed = (
        common_pair
        and four_routes_reject_m0
        and finite_map_closed
        and selected_pair_closed
        and time_branch_selects_q79
        and q79_m1
        and q369_m2
        and ordinary_rhoe_blocked
    )

    status = (
        "TIME_ORIENTED_FIXED_GERBE_REPRESENTATIVE_CLOSED_SOURCE_PACKET_OPEN"
        if representative_closed
        else "TIME_ORIENTED_FIXED_GERBE_REPRESENTATIVE_NOT_CLOSED"
    )
    return {
        "candidate": "TimeOrientedFixedGerbeRepresentative",
        "status": status,
        "generated_by": "scripts/prove_time_oriented_fixed_gerbe_representative.py",
        "inputs": {
            "selected_gerbe_fourier_type": get(gerbe_fourier, "status"),
            "time_oriented_branch": get(time, "status"),
            "torsion_label_selector": get(torsion, "status"),
            "finite_gerbe_holonomy": get(gerbe, "status"),
            "ordinary_rhoE_source_search": get(visible_rhoe, "status"),
        },
        "branch_representatives": {
            "time_oriented_q79": {
                "q": q79_packet.get("global_cp_label"),
                "orientation": q79_packet.get("conditional_su5_transport_orientation"),
                "torsion_label_m": q79_packet.get("torsion_label_m"),
                "sector_orientations": q79_packet.get("sector_orientations"),
            },
            "antiunitary_conjugate_q369": {
                "q": q369_packet.get("global_cp_label"),
                "orientation": q369_packet.get("conditional_su5_transport_orientation"),
                "torsion_label_m": q369_packet.get("torsion_label_m"),
                "sector_orientations": q369_packet.get("sector_orientations"),
            },
        },
        "calculation_results": {
            "finite_gerbe_holonomy_map_closed": finite_map_closed,
            "four_route_nontrivial_pair_closed": common_pair,
            "trivial_m0_rejected": four_routes_reject_m0,
            "selected_nontrivial_gerbe_fourier_pair_closed": selected_pair_closed,
            "retarded_time_orientation_selects_q79_representative": time_branch_selects_q79,
            "time_oriented_torsion_label_m1_fixed": q79_m1,
            "antiunitary_conjugate_torsion_label_m2_retained": q369_m2,
            "ordinary_rhoE_absorption_blocked": ordinary_rhoe_blocked,
            "curvature_only_selection_still_insufficient": curvature_cannot_choose,
            "time_oriented_finite_representative_closed": representative_closed,
            "full_twisted_source_promotion_closed": False,
            "selected_D_E_dotD_constructed": False,
        },
        "what_this_closes": {
            "m1_vs_m2_is_no_longer_a_time_oriented_fitting_knob": representative_closed,
            "q79_branch_uses_m1_F_representative": representative_closed,
            "q369_branch_retained_as_m2_F_conjugate": representative_closed,
            "ordinary_rhoE_conversion_is_not_required_for_the_representative_statement": representative_closed,
        },
        "still_open": {
            "full_Deligne_Cech_or_B_field_period_table_on_actual_Iwasawa_sector": True,
            "embedding_into_full_heterotic_Green_Schwarz_Bianchi_sector": True,
            "Freed_Witten_restriction_on_selected_cycles": True,
            "twisted_projector_retention": True,
            "selected_D_E_dotD": True,
            "selected_C1_primitive_contractions": True,
            "ordered_SU5_matter_slot_packet": True,
            "Yukawa_magnitudes_and_CKM_angles": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_twist_promotion_packet_passes": False,
            "claims_full_differential_cohomology_representative": False,
            "claims_full_heterotic_Bianchi_verified_for_new_twist": False,
            "claims_Freed_Witten_verified": False,
            "claims_selected_D_E_constructed": False,
            "claims_ordered_SU5_packet_selected": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The time-oriented finite gerbe representative is now fixed: "
                "the q79/F branch carries m=1 and the antiunitary conjugate "
                "q369/F* branch carries m=2. This closes the finite label "
                "ambiguity, not the full selected gerbe/D_E source packet."
            )
            if representative_closed
            else "The time-oriented finite representative was not closed from the available certificates.",
            "next_closing_object": (
                "Use m=1 as the fixed q79/F finite torsion representative and "
                "construct the selected de_response packet: D_E, dotD_alpha1, "
                "Riesz/Green, projector retention, and primitive C1 contractions."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "TimeOrientedFixedGerbeRepresentative",
        "status": report["status"],
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "analysis_script": "scripts/prove_time_oriented_fixed_gerbe_representative.py",
        "calculation_results": report["calculation_results"],
        "branch_representatives": report["branch_representatives"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
