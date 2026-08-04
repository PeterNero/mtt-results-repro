"""Audit the C1 frontier after the cross-repo alpha1 import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_c1_frontier_after_alpha1_import.candidate.json"
CERT = ROOT / "certificates" / "selected_c1_frontier_after_alpha1_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_C1_Frontier_After_Alpha1_Import_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_c1_frontier_after_alpha1_import.py"

STATUS = "MTT_SELECTED_C1_FRONTIER_AFTER_ALPHA1_IMPORT_DOTD_RETIRED_PRIMITIVE_RESPONSE_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_WeylPairSectorRouting_SourceEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note does not record next artifact")

    retired = data["retired_driver_gates"]
    require(retired["selected_dotD_source_verified"] is True, "dotD source not retired")
    require(retired["alpha1_driver_verified"] is True, "alpha1 driver not retired")
    require(retired["honest_dotD_alpha1_replay"] is True, "honest dotD replay not imported")
    require(retired["N_alpha1_h_ext"] == 1.0, "N_alpha1 value mismatch")
    require(retired["du_dalpha1_equals_h_ext"] is True, "du/dalpha1 mismatch")

    retained = data["retained_local_results"]
    require(retained["active_shift_selected"] is True, "active shift not retained")
    require(retained["fiber_class_quotient_selected"] is True, "fiber quotient not retained")
    require(retained["absolute_fiber_origin_not_selected"] is True, "absolute origin overselected")
    require(retained["current_layer_flavor_splitting_no_go"] is True, "no-go not retained")
    require(
        retained["higher_order_acceptance_criterion_locked"] is True,
        "higher-order criterion not retained",
    )

    support = data["conditional_c1_support"]
    require(support["conditional_weyl_transfer_exact"] is True, "conditional transfer not exact")
    require(support["conditional_A_selected_emitted"] is False, "conditional transfer overpromoted")
    require(support["conditional_A_rank_tested"] is False, "selected rank test overclaimed")
    require(support["conditional_A_promoted"] is False, "A_selected overpromoted")
    require(support["conditional_b_promoted"] is False, "b_selected overpromoted")

    live = data["live_source_objects"]
    for key in [
        "primitive_C1_contractions",
        "selected_A_selected",
        "selected_b_selected",
        "selected_sector_response_matrices",
        "selected_zero_mode_bases_and_Gram",
        "selected_higher_order_or_full_response_matrices",
        "selected_deltaTheta_C1_solution",
        "selected_sector_charge_or_chirality_table",
        "selected_transfer_normalization",
        "selected_singlet_neutrino_shift_rule",
    ]:
        require(live[key] is True, f"live source object missing: {key}")

    boundary = data["proof_boundary"]
    require(boundary["alpha1_driver_is_not_allowed_to_select_C1_values"] is True, "alpha1 overused")
    require(boundary["observed_flavor_data_not_used"] is True, "observed data boundary missing")
    require(
        boundary["locked_splitter_columns_are_diagnostic_until_source_emitted"] is True,
        "locked splitter promoted too early",
    )
    require(
        boundary["absolute_fiber_origin_not_needed_for_current_spectral_observables"] is True,
        "fiber-origin boundary missing",
    )
    require(boundary["full_SM_closure_not_claimed"] is True, "full closure overclaimed")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["A_selected_claimed"] is False, "A_selected claimed")
    require(data["b_selected_claimed"] is False, "b_selected claimed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
