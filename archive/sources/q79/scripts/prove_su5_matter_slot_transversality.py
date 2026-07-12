"""Prove the finite SU(5) matter-slot transversality theorem.

This is the sharp finite closure left after the time-oriented q79 theorem.

If a selected MTT source supplies the structural statement that the two SU(5)
matter slots are represented by transverse qutrit polarizations, then the
retarded q79 branch forces the ordered representative

    U_10 = I_3,  U_bar5 = F

up to a common family-gauge unitary, rephasings, and permutations.  The proof
does not claim that MTT has already supplied that source.  It proves uniqueness
of the packet once the missing matter-slot transversality selector is supplied.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
OUT = ROOT / "candidate_data" / "su5_matter_slot_transversality.candidate.json"
CERT = CERTIFICATES / "su5_matter_slot_transversality_certificate.json"
TOL = 1e-10
OMEGA = complex(-0.5, math.sqrt(3) / 2.0)
HEAVY_LINKS = ((0, 2), (1, 2))

Matrix = list[list[complex]]


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


def identity() -> Matrix:
    return [[1.0 + 0j if row == col else 0j for col in range(3)] for row in range(3)]


def fourier(conjugate: bool = False) -> Matrix:
    omega = OMEGA.conjugate() if conjugate else OMEGA
    scale = 1.0 / math.sqrt(3)
    return [[omega ** (row * col) * scale for col in range(3)] for row in range(3)]


def dagger(matrix: Matrix) -> Matrix:
    return [[matrix[col][row].conjugate() for col in range(3)] for row in range(3)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3)]
        for row in range(3)
    ]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[row][col] - right[row][col] for col in range(3)] for row in range(3)]


def max_abs(matrix: Matrix) -> float:
    return max(abs(entry) for row in matrix for entry in row)


def is_unitary(matrix: Matrix) -> bool:
    return max_abs(matrix_sub(matmul(dagger(matrix), matrix), identity())) < TOL


def support(left_basis: Matrix, right_basis: Matrix) -> Matrix:
    return matmul(dagger(left_basis), right_basis)


def heavy_vector(matrix: Matrix) -> list[complex]:
    return [matrix[row][col] for row, col in HEAVY_LINKS]


def vector_sub(left: list[complex], right: list[complex]) -> list[complex]:
    return [a - b for a, b in zip(left, right)]


def vector_nonzero(vector: list[complex]) -> bool:
    return any(abs(entry) > TOL for entry in vector)


def encode_scalar(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < TOL else value.real
    imag = 0.0 if abs(value.imag) < TOL else value.imag
    if imag == 0.0:
        return real
    return [real, imag]


def encode(value: Any) -> Any:
    if isinstance(value, complex):
        return encode_scalar(value)
    if isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def analyze_case(name: str, u10: Matrix, ubar5: Matrix) -> dict[str, Any]:
    up = support(u10, u10)
    down = support(u10, ubar5)
    up_heavy = heavy_vector(up)
    down_heavy = heavy_vector(down)
    delta = vector_sub(down_heavy, up_heavy)
    return {
        "name": name,
        "U10_unitary": is_unitary(u10),
        "Ubar5_unitary": is_unitary(ubar5),
        "up_channel": "10_M x 10_M",
        "down_channel": "10_M x bar5_M",
        "up_transport": up,
        "down_transport": down,
        "up_heavy_links_13_23": up_heavy,
        "down_heavy_links_13_23": down_heavy,
        "Delta_t": delta,
        "Delta_t_nonzero": vector_nonzero(delta),
    }


def analyze() -> dict[str, Any]:
    qutrit = cert("qutrit_polarization_transport_lemma_certificate.json")
    time_branch = cert("time_oriented_conjugate_branch_selection_certificate.json")
    transport_candidate = cert("su5_qutrit_basis_transport_heavy_link_candidate_certificate.json")
    selector_hunt = cert("su5_qutrit_transport_selector_hunt_certificate.json")
    selection_gate = cert("su5_qutrit_polarization_selection_gate_certificate.json")
    source_attempt = cert("selected_su5_source_proof_attempt_certificate.json")

    i3 = identity()
    f = fourier()
    f_star = fourier(conjugate=True)

    cases = [
        analyze_case("common_identity_U10_I_Ubar5_I", i3, i3),
        analyze_case("common_fourier_U10_F_Ubar5_F", f, f),
        analyze_case("transverse_q79_U10_I_Ubar5_F", i3, f),
        analyze_case("transverse_conjugate_U10_I_Ubar5_Fstar", i3, f_star),
    ]
    by_name = {case["name"]: case for case in cases}

    common_cases_delta_zero = (
        by_name["common_identity_U10_I_Ubar5_I"]["Delta_t_nonzero"] is False
        and by_name["common_fourier_U10_F_Ubar5_F"]["Delta_t_nonzero"] is False
    )
    transverse_cases_nonzero = (
        by_name["transverse_q79_U10_I_Ubar5_F"]["Delta_t_nonzero"] is True
        and by_name["transverse_conjugate_U10_I_Ubar5_Fstar"]["Delta_t_nonzero"] is True
    )
    finite_qutrit_transport_proved = (
        get(qutrit, "calculation_results", "finite_transport_lemma_proved") is True
        and get(qutrit, "calculation_results", "solutions_are_F_and_F_conjugate") is True
    )
    retarded_q79_orientation_closed = (
        get(time_branch, "calculation_results", "time_oriented_retarded_branch_selects_q79")
        is True
        and get(time_branch, "calculation_results", "q369_retained_as_global_antiunitary_conjugate")
        is True
    )
    basis_candidate_matches = (
        get(transport_candidate, "calculation_results", "best_candidate_rule")
        == "B_10=I_3, B_bar5=F"
        and get(transport_candidate, "calculation_results", "common_transport_is_gauge")
        is True
        and get(transport_candidate, "calculation_results", "su5_representation_split_nonzero")
        is True
    )
    finite_transversality_unique = (
        finite_qutrit_transport_proved
        and retarded_q79_orientation_closed
        and basis_candidate_matches
        and common_cases_delta_zero
        and transverse_cases_nonzero
    )

    selected_source_present = (
        get(selector_hunt, "verdict", "selected_B10_Bbar5_transport_found") is True
        or get(selection_gate, "verdict", "sector_polarization_selection_proved_from_current_data")
        is True
        or get(source_attempt, "calculation_results", "remaining_proof_closed_now") is True
    )
    selected_packet_closed = finite_transversality_unique and selected_source_present
    status = (
        "SELECTED_SU5_MATTER_SLOT_PACKET_CLOSED"
        if selected_packet_closed
        else "FINITE_SU5_MATTER_SLOT_TRANSVERSALITY_CLOSED_SOURCE_OPEN"
    )

    return encode(
        {
            "candidate": "SU5MatterSlotTransversality",
            "status": status,
            "generated_by": "scripts/prove_su5_matter_slot_transversality.py",
            "proof_target": {
                "closed_finite_statement": (
                    "Given selected transverse qutrit polarizations for the SU(5) matter slots, "
                    "the retarded q79 branch selects U_10=I_3 and U_bar5=F up to common gauge."
                ),
                "not_closed_without_extra_source": (
                    "The corpus must still supply the selected matter-slot transversality source."
                ),
            },
            "inputs": {
                "qutrit_transport": "qutrit_polarization_transport_lemma_certificate.json",
                "time_oriented_branch": "time_oriented_conjugate_branch_selection_certificate.json",
                "basis_transport_candidate": "su5_qutrit_basis_transport_heavy_link_candidate_certificate.json",
                "source_hunt": "su5_qutrit_transport_selector_hunt_certificate.json",
                "selection_gate": "su5_qutrit_polarization_selection_gate_certificate.json",
            },
            "finite_case_scan": cases,
            "calculation_results": {
                "finite_qutrit_transport_proved": finite_qutrit_transport_proved,
                "retarded_q79_orientation_closed": retarded_q79_orientation_closed,
                "basis_candidate_matches_B10_I_Bbar5_F": basis_candidate_matches,
                "common_slot_transport_is_gauge": common_cases_delta_zero,
                "transverse_slot_transport_nonzero": transverse_cases_nonzero,
                "finite_transversality_theorem_closed": finite_transversality_unique,
                "selected_mtt_source_present": selected_source_present,
                "selected_ordered_su5_packet_closed": selected_packet_closed,
                "selected_packet": {
                    "U_10": "I_3",
                    "U_bar5": "F",
                    "q": 79,
                    "Delta_t": by_name["transverse_q79_U10_I_Ubar5_F"]["Delta_t"],
                },
                "conjugate_packet": {
                    "U_10": "I_3",
                    "U_bar5": "F*",
                    "q": 369,
                    "Delta_t": by_name["transverse_conjugate_U10_I_Ubar5_Fstar"]["Delta_t"],
                },
            },
            "what_this_closes": {
                "common_fourier_gauge_eliminated": common_cases_delta_zero,
                "retarded_q79_selects_F_over_Fstar": retarded_q79_orientation_closed,
                "finite_uniqueness_of_ordered_packet_under_transversality": finite_transversality_unique,
                "exact_remaining_source_is_not_finite_algebra": finite_transversality_unique
                and not selected_source_present,
            },
            "still_open": {
                "selected_matter_slot_transversality_source": not selected_source_present,
                "typed_monad_Cech_or_Galerkin_zero_mode_realization": not selected_source_present,
                "selected_D_E_dotD_source_for_same_branch": not selected_source_present,
                "selected_overlap_kernel_prefactor": True,
                "Yukawa_magnitudes_and_CKM_angles": True,
                "full_SM_closure": True,
            },
            "guardrails": {
                "claims_selected_source_present": selected_source_present,
                "claims_ordered_su5_packet_selected_without_source": False,
                "uses_observed_flavor_data": False,
                "uses_benchmark_flavor_entries": False,
                "uses_common_fourier_gauge_as_physical_mixing": False,
                "claims_full_SM_closure": False,
            },
            "verdict": {
                "finite_transversality_theorem_closed": finite_transversality_unique,
                "selected_ordered_su5_packet_closed": selected_packet_closed,
                "honest_answer": (
                    "The finite packet is now uniquely closed under the transversality hypothesis: retarded q79 gives U_10=I_3, U_bar5=F. The selected MTT source for that transversality is still absent."
                    if finite_transversality_unique and not selected_packet_closed
                    else "The selected ordered SU(5) matter-slot packet is closed."
                    if selected_packet_closed
                    else "The finite transversality theorem did not close."
                ),
                "next_required_input": (
                    "a selected monad/Cech, Galerkin, D_E/dotD, or gerbe/projector theorem whose output is the matter-slot transversality source"
                ),
            },
        }
    )


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "SU5MatterSlotTransversality",
        "status": report["status"],
        "purpose": "Close the finite ordered SU(5) qutrit packet under the explicit matter-slot transversality hypothesis, while preserving the selected-source guardrail.",
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "analysis_script": "scripts/prove_su5_matter_slot_transversality.py",
        "depends_on": [
            "qutrit_polarization_transport_lemma_certificate.json",
            "time_oriented_conjugate_branch_selection_certificate.json",
            "su5_qutrit_basis_transport_heavy_link_candidate_certificate.json",
            "su5_qutrit_transport_selector_hunt_certificate.json",
            "su5_qutrit_polarization_selection_gate_certificate.json",
            "selected_su5_source_proof_attempt_certificate.json",
        ],
        "calculation_results": report["calculation_results"],
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
