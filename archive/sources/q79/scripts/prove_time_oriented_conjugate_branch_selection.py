"""Prove the time-oriented representative of the MTT conjugate branch pair.

The previous selected gerbe-Fourier theorem closed the unoriented type:

    {q=79/F, q=369/F*}

as one nontrivial structure up to global conjugation.  This script adds the
next narrow theorem: once the already closed retarded exact/charge branch is
used as the time-orientation datum, the selected representative is q=79.  The
conjugate q=369 branch is retained as the antiunitary/global-conjugate partner,
not rejected as "wrong" and not promoted to a second independent knob.

This does not prove the ordered SU(5) matter-slot packet U_10=I_3, U_bar5=F.
That still requires selected matter-slot/zero-mode/operator source data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
OUT = ROOT / "candidate_data" / "time_oriented_conjugate_branch_selection.candidate.json"
CERT = CERTIFICATES / "time_oriented_conjugate_branch_selection_certificate.json"
MODULUS = 64 * 7


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


def crt_mod_448(q64: int, q7: int) -> int:
    for q in range(MODULUS):
        if q % 64 == q64 % 64 and q % 7 == q7 % 7:
            return q
    raise ValueError((q64, q7))


def branch_for_q(branch_packets: list[dict[str, Any]], q: int) -> dict[str, Any]:
    for packet in branch_packets:
        if packet.get("global_cp_label") == q:
            return packet
    return {}


def analyze() -> dict[str, Any]:
    z64 = cert("z64_exact_branch_certificate.json")
    z7 = cert("z7_fuyau_mukai_charge_sector_certificate.json")
    orientation = cert("iwasawa_orientation_de_dotd_bridge_certificate.json")
    c6_common = cert("iwasawa_c6_common_holonomy_branch_pair_certificate.json")
    c6_phase = cert("iwasawa_c6_global_phase_block_certificate.json")
    gerbe_type = cert("selected_gerbe_fourier_type_theorem_certificate.json")

    q64 = int(get(z64, "conclusion", "q_64", default=-1))
    q7 = int(get(z7, "conclusion", "q_7", default=-1))
    crt_q = crt_mod_448(q64, q7)
    inverse_q = (-crt_q) % MODULUS

    retarded_kernel_selected = (
        get(z64, "retarded_kernel", "K_ret_64") == "S^-1"
        and get(z64, "retarded_kernel", "lag_mod_64") == 63
        and get(z64, "retarded_kernel", "primitive") is True
        and get(z64, "hessian_block", "selected_value") == 15
    )
    z7_sector_selected = (
        get(z7, "selection", "strominger_selection_applies") is True
        and get(z7, "geometry", "green_schwarz_bianchi_identity_verified") is True
        and q7 == 2
    )
    terminal_q79_selected = retarded_kernel_selected and z7_sector_selected and crt_q == 79

    branch_packets = orientation.get("branch_packets", [])
    q79_packet = branch_for_q(branch_packets, 79)
    q369_packet = branch_for_q(branch_packets, 369)
    branch_packet_map_closed = (
        q79_packet.get("torsion_label_m") == 1
        and q79_packet.get("conditional_su5_transport_orientation") == "F"
        and q369_packet.get("torsion_label_m") == 2
        and q369_packet.get("conditional_su5_transport_orientation") == "F*"
        and get(orientation, "calculation_results", "global_cp_label_pair") == [79, 369]
        and get(orientation, "verdict", "not_two_independent_solutions") is True
    )
    c6_global_pair_closed = (
        get(c6_common, "verdict", "C6_branch_space_now_global_conjugate_pair") is True
        and get(c6_phase, "calculation_results", "global_pair_are_complex_conjugates") is True
        and get(c6_phase, "calculation_results", "selected_q_label_from_closed_branch") == 79
        and get(c6_phase, "calculation_results", "inverse_label") == 369
    )
    gerbe_fourier_type_closed = (
        get(gerbe_type, "calculation_results", "selected_gerbe_fourier_type_closed") is True
        and get(gerbe_type, "calculation_results", "finite_fourier_transport_closed") is True
        and get(gerbe_type, "calculation_results", "unique_orientation_selected") is False
    )
    exact_su5_packet_selected = (
        get(gerbe_type, "calculation_results", "exact_q79_packet_U10_I_Ubar5_F_selected")
        is True
    )

    unoriented_pair_retained = (
        gerbe_fourier_type_closed and branch_packet_map_closed and c6_global_pair_closed
    )
    time_oriented_q79_selected = terminal_q79_selected and unoriented_pair_retained
    status = (
        "TIME_ORIENTED_Q79_F_BRANCH_SELECTED_ORDERED_SU5_PACKET_OPEN"
        if time_oriented_q79_selected and not exact_su5_packet_selected
        else "TIME_ORIENTED_BRANCH_SELECTION_NOT_CLOSED"
    )

    report = {
        "candidate": "TimeOrientedConjugateBranchSelection",
        "status": status,
        "generated_by": "scripts/prove_time_oriented_conjugate_branch_selection.py",
        "proof_target": {
            "unoriented_level": "MTT selects the nontrivial gerbe-Fourier branch pair {q79/F, q369/F*}.",
            "time_oriented_level": "The closed retarded exact/charge branch selects q79/F as the representative seen by a retarded universe.",
            "not_target": "This theorem does not select the ordered SU(5) matter-slot packet U_10=I_3, U_bar5=F.",
        },
        "residue_calculation": {
            "modulus": MODULUS,
            "selected_residues": {
                "q_64": q64,
                "q_7": q7,
                "crt_q": crt_q,
            },
            "conjugate_residues": {
                "q": inverse_q,
                "q_64": inverse_q % 64,
                "q_7": inverse_q % 7,
            },
            "q79_plus_q369_mod_448": (crt_q + inverse_q) % MODULUS,
        },
        "source_gates": {
            "z64_retarded_kernel": {
                "K_ret_64": get(z64, "retarded_kernel", "K_ret_64"),
                "lag_mod_64": get(z64, "retarded_kernel", "lag_mod_64"),
                "primitive": get(z64, "retarded_kernel", "primitive"),
                "selected_value": get(z64, "hessian_block", "selected_value"),
                "closed": retarded_kernel_selected,
            },
            "z7_charge_sector": {
                "q_7": q7,
                "strominger_selection_applies": get(
                    z7, "selection", "strominger_selection_applies"
                ),
                "green_schwarz_bianchi_identity_verified": get(
                    z7, "geometry", "green_schwarz_bianchi_identity_verified"
                ),
                "closed": z7_sector_selected,
            },
            "orientation_bridge": {
                "q79_packet": q79_packet,
                "q369_packet": q369_packet,
                "closed": branch_packet_map_closed,
            },
            "global_conjugate_pair": {
                "common_holonomy_closed": get(
                    c6_common, "verdict", "C6_branch_space_now_global_conjugate_pair"
                ),
                "phase_pair_complex_conjugate": get(
                    c6_phase, "calculation_results", "global_pair_are_complex_conjugates"
                ),
                "closed": c6_global_pair_closed,
            },
            "selected_gerbe_fourier_type": {
                "selected_gerbe_fourier_type_closed": get(
                    gerbe_type,
                    "calculation_results",
                    "selected_gerbe_fourier_type_closed",
                ),
                "unique_orientation_selected": get(
                    gerbe_type, "calculation_results", "unique_orientation_selected"
                ),
                "closed": gerbe_fourier_type_closed,
            },
        },
        "calculation_results": {
            "z64_retarded_kernel_selected": retarded_kernel_selected,
            "z7_charge_sector_selected": z7_sector_selected,
            "crt_selects_q79": crt_q == 79,
            "conjugate_label_is_q369": inverse_q == 369,
            "branch_packet_map_q79_F_q369_Fstar": branch_packet_map_closed,
            "unoriented_conjugate_pair_retained": unoriented_pair_retained,
            "time_oriented_retarded_branch_selects_q79": time_oriented_q79_selected,
            "q369_retained_as_global_antiunitary_conjugate": unoriented_pair_retained
            and inverse_q == 369,
            "two_unrelated_universe_interpretation_rejected": get(
                orientation, "verdict", "not_two_independent_solutions"
            )
            is True,
            "unique_without_retarded_boundary_or_operator_source": False,
            "ordered_su5_packet_selected": exact_su5_packet_selected,
            "full_sm_closure": False,
        },
        "what_this_proves": {
            "without_time_orientation_MTT_selects_pair_not_single_representative": unoriented_pair_retained,
            "with_closed_retarded_kernel_MTT_selects_q79_representative": time_oriented_q79_selected,
            "q369_Fstar_remains_conjugate_partner": unoriented_pair_retained
            and inverse_q == 369,
            "retarded_initial_or_boundary_condition_can_function_as_branch_selector": time_oriented_q79_selected,
            "not_two_independent_tunable_phase_knobs": get(
                orientation, "verdict", "not_two_independent_solutions"
            )
            is True,
        },
        "still_open": {
            "ordered_SU5_slot_assignment_10M_clock_bar5M_shift": not exact_su5_packet_selected,
            "selected_D_E_dotD_or_monad_source_for_matter_slots": not exact_su5_packet_selected,
            "full_operator_antiunitary_equivalence_for_all_matrices": True,
            "Yukawa_magnitudes_and_CKM_angles": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_q369_wrong_or_nonexistent": False,
            "claims_two_independent_physical_universes": False,
            "claims_both_branches_simultaneously_observed": False,
            "claims_exact_SU5_packet_selected": exact_su5_packet_selected,
            "uses_observed_CP_sign_to_select_branch": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "time_unoriented_status": "selected conjugate pair {q79/F, q369/F*}"
            if unoriented_pair_retained
            else "unoriented pair not closed",
            "time_oriented_status": "retarded exact/charge branch selects q79/F representative"
            if time_oriented_q79_selected
            else "retarded representative not closed",
            "ordered_su5_packet_status": "OPEN",
            "honest_answer": (
                "MTT now has a rigorous two-level statement: without time orientation it selects the conjugate pair, while the already closed retarded exact/charge branch selects q=79 as the time-oriented representative. The q=369 branch remains the global conjugate partner, not an extra fitting knob. The exact ordered SU(5) matter-slot packet remains open."
                if time_oriented_q79_selected and not exact_su5_packet_selected
                else "The time-oriented branch theorem is not closed from the available certificates."
            ),
            "next_closing_object": "selected matter-slot/operator source proving 10_M=clock, bar5_M=shift, and the ordered U_10=I_3,U_bar5=F packet on the q79 retarded branch.",
        },
    }
    return report


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "TimeOrientedConjugateBranchSelection",
        "status": report["status"],
        "purpose": "Use the closed retarded exact/charge branch to select the q79 representative of the already selected conjugate gerbe-Fourier pair, without overclaiming the ordered SU(5) packet.",
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "analysis_script": "scripts/prove_time_oriented_conjugate_branch_selection.py",
        "depends_on": [
            "z64_exact_branch_certificate.json",
            "z7_fuyau_mukai_charge_sector_certificate.json",
            "selected_gerbe_fourier_type_theorem_certificate.json",
            "iwasawa_orientation_de_dotd_bridge_certificate.json",
            "iwasawa_c6_common_holonomy_branch_pair_certificate.json",
            "iwasawa_c6_global_phase_block_certificate.json",
        ],
        "residue_calculation": report["residue_calculation"],
        "source_gates": report["source_gates"],
        "calculation_results": report["calculation_results"],
        "what_this_proves": report["what_this_proves"],
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
