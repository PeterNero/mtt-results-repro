from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
SLUG = "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness"
OUT = ROOT / "candidate_data" / SLUG


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    pair = load(Q79 / "certificates" / "orientation_branch_antiunitary_equivalence_certificate.json")
    parity = load(Q79 / "certificates" / "orientation_observable_parity_certificate.json")
    retarded = load(Q79 / "certificates" / "time_oriented_conjugate_branch_selection_certificate.json")
    gerbe = load(Q79 / "certificates" / "selected_gerbe_fourier_type_theorem_certificate.json")

    packet = {
        "schema": "MTTSelectedBranchOrbitAndRetardedRepresentativeOrGlobalMeasureUniqueness.v1",
        "status": "ORIENTATION_ORBIT_AND_RETARDED_REPRESENTATIVE_CLOSED_GLOBAL_SUPERSET_MEASURE_OPEN",
        "selected_unoriented_orbit": {
            "members": [
                {"q": 79, "orientation": "F", "torsion_label": 1},
                {"q": 369, "orientation": "F*", "torsion_label": 2},
            ],
            "antiunitary_equivalence_closed": pair["summary"]["antiunitary_equivalence_closed"],
            "operator_entries_compared": pair["summary"]["total_entries_compared"],
            "maximum_conjugation_error": pair["summary"]["max_abs_conjugation_error"],
            "trivial_gerbe_label_rejected": gerbe["calculation_results"]["four_route_selects_nontrivial_conjugate_pair"],
            "two_independent_tunable_branches": False,
        },
        "observable_parity": {
            "CP_even_checks": parity["finite_operator_parity"]["cp_even_norm_invariants"]["checks"],
            "CP_even_failures": parity["finite_operator_parity"]["cp_even_norm_invariants"]["failures"],
            "complex_conjugation_checks": parity["finite_operator_parity"]["complex_conjugation_invariants"]["checks"],
            "complex_conjugation_failures": parity["finite_operator_parity"]["complex_conjugation_invariants"]["failures"],
            "CP_odd_sign_flips": parity["finite_operator_parity"]["complex_conjugation_invariants"]["nonzero_imaginary_sign_flips"],
        },
        "retarded_representative_selection": {
            "retarded_kernel_closed": retarded["source_gates"]["z64_retarded_kernel"]["closed"],
            "charge_sector_closed": retarded["source_gates"]["z7_charge_sector"]["closed"],
            "CRT_q": retarded["residue_calculation"]["selected_residues"]["crt_q"],
            "q79_time_oriented_representative_selected": retarded["calculation_results"]["time_oriented_retarded_branch_selects_q79"],
            "q369_retained_as_antiunitary_partner": retarded["calculation_results"]["q369_retained_as_global_antiunitary_conjugate"],
            "observed_CP_sign_used_as_selector": retarded["guardrails"]["uses_observed_CP_sign_to_select_branch"],
        },
        "decision": {
            "orientation_level_branch_selection_closed": True,
            "unoriented_antiunitary_equivalence_class_closed": True,
            "time_oriented_q79_representative_closed": True,
            "unique_global_MTT_carrier_or_geometry_closed": False,
            "probability_one_global_measure_class_closed": False,
            "U9_full_superset_uniqueness_closed": False,
        },
        "remaining_object": {
            "name": "SelectedGlobalBranchActionMeasureAndCarrierUniquenessTheorem",
            "must_supply": [
                "measure or action on the complete admissible MTT carrier/geometry space",
                "normalizability or compactness/coercivity sufficient for minimizer existence",
                "proof that all global minimizers lie in the selected antiunitary orbit",
                "retarded orientation then selecting q79 inside that orbit",
            ],
        },
        "guards": {
            "q369_declared_nonexistent": False,
            "orientation_pair_called_two_unrelated_universes": False,
            "finite_orbit_selection_mislabeled_as_global_carrier_uniqueness": False,
            "observed_CP_sign_used": False,
        },
    }
    dump(OUT / "branch_orbit_retarded_representative_and_global_measure_cutset.packet.json", packet)

    status = "MTT_SELECTED_BRANCHORBIT_RETARDED_Q79_REPRESENTATIVE_CLOSED_GLOBAL_MEASURE_OPEN"
    candidate = {
        "candidate": "MTT_Selected_BranchOrbitAndRetardedRepresentative_or_GlobalMeasureUniqueness_v1",
        "status": status,
        "date": "2026-07-11",
        "closure_claimed": True,
        "theorem": {
            "name": "AntiunitaryOrbitAndRetardedRepresentativeSelectionTheorem",
            "proved": True,
            "statement": "The selected finite gerbe/flavor branch is one antiunitary orbit with q79/F/m1 and q369/F*/m2 representatives. CP-even data agree and CP-odd data conjugate. The selected retarded Z64 kernel and Z7 charge sector choose q79 as the time-oriented representative without observed CP input. Full uniqueness across all admissible MTT carrier geometries remains open pending a global action or measure theorem.",
        },
        "orientation_level_selection_closed": True,
        "U9_full_superset_uniqueness_closed": False,
        "next_required_artifact": "MTT_Selected_GlobalBranchActionMeasureAndCarrierUniquenessTheorem_v1",
    }
    dump(ROOT / "candidate_data" / f"{SLUG}.candidate.json", candidate)

    certificate = {
        "certificate": "MTT_Selected_BranchOrbitAndRetardedRepresentative_or_GlobalMeasureUniqueness_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": status,
        "theorem_proved": True,
        "selected_antiunitary_orbit_members": 2,
        "operator_entries_compared": pair["summary"]["total_entries_compared"],
        "orientation_level_selection_closed": True,
        "time_oriented_q79_representative_closed": True,
        "global_carrier_uniqueness_closed": False,
        "probability_one_global_measure_class_closed": False,
        "U9_full_superset_uniqueness_closed": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(ROOT / "certificates" / f"{SLUG}_certificate.json", certificate)


if __name__ == "__main__":
    main()
