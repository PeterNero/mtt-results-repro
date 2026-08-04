"""Audit post-source formal 110-row observables and full-SM gap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_postsourceformal110_observableaudit_or_fullsmgap"
DATA = ROOT / "candidate_data"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "postsource_source_stack_reconciliation.packet.json"
OBSERVABLES = PACKET_DIR / "formal110_sector_matrix_observables.packet.json"
GAP = PACKET_DIR / "full_sm_gap_after_formal110_observables.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_postsource_formal110_observables.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostSourceFormal110_ObservableAudit_or_FullSMGap_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_postsourceformal110_observableaudit_or_fullsmgap.py"

STATUS = "MTT_SELECTED_POSTSOURCE_FORMAL110_OBSERVABLE_AUDIT_BUILT_FIRST_SPLITTING_FULLSM_OPEN"
NEXT = "MTT_Selected_HigherOrderFullResponseMatrices_or_SecondOrderFlavorLift_v1"
SECTORS = ["u", "d", "e", "nuD"]
TOL = 1e-9


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")
    require(payload["closure_claimed"] is False, f"{label}: closure overclaimed")


def approx(value: float, expected: float, tol: float = TOL) -> bool:
    return abs(value - expected) <= tol


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    reconciliation = load(RECONCILIATION)
    observables = load(OBSERVABLES)
    gap = load(GAP)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for label, payload in [
        ("candidate", candidate),
        ("reconciliation", reconciliation),
        ("observables", observables),
        ("gap", gap),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    require(reconciliation["source_stack_closed"] is True, "source stack not imported closed")
    require(reconciliation["formal_110_rows_executed"] is True, "formal rows not executed")
    require(reconciliation["all_72_exact_rows_executed"] is True, "72 rows not executed")
    require(reconciliation["all_72_exactness_closed"] is True, "72 rows exactness missing")
    require(reconciliation["stationary_projector_source_verified"] is True, "stationary source not verified")
    require(reconciliation["selected_dotD_source_verified"] is True, "dotD not reconciled")
    require(reconciliation["alpha1_driver_verified"] is True, "alpha1 not reconciled")
    require(
        reconciliation["unpatched_full_sm_gate_still_listed_alpha1_dotd_open"] is True,
        "expected old alpha1 gap not recorded",
    )
    require(
        reconciliation["alpha1_dotd_retired_by_later_integrated_frontier"] is True,
        "later alpha1 retirement not recorded",
    )
    require(reconciliation["not_a_full_SM_closure_claim"] is True, "full SM guard missing")

    require(observables["status"] == "FORMAL_110_MATRICES_FIRST_SPLITTING_FULL_SM_OPEN", "observable status mismatch")
    require(observables["sector_count"] == 4, "sector count mismatch")
    sectors = observables["sector_observables"]
    for sector in SECTORS:
        require(sector in sectors, f"missing sector {sector}")
        slot = sectors[sector]
        require(slot["hermitian_spectrum"] == [1.0, 1.0, 4.0], f"spectrum mismatch {sector}")
        require(slot["twofold_family_degeneracy"] is True, f"degeneracy missing {sector}")
        require(slot["non_scalar_first_splitting"] is True, f"first split missing {sector}")
        require(slot["full_three_family_hierarchy"] is False, f"full hierarchy overclaimed {sector}")
        require(approx(slot["traceless_norm_sq"], 6.0), f"traceless norm mismatch {sector}")
    require(sectors["u"]["source_direction"] == "phase_packet_I_plus_Z", "u source direction mismatch")
    require(sectors["e"]["source_direction"] == "phase_packet_I_plus_Z", "e source direction mismatch")
    require(sectors["d"]["source_direction"] == "shift_packet_I_plus_X", "d source direction mismatch")
    require(sectors["nuD"]["source_direction"] == "shift_packet_I_plus_X", "nuD source direction mismatch")

    quark = observables["pair_observables"]["quark_like_u_d"]
    lepton = observables["pair_observables"]["lepton_like_e_nuD"]
    for label, pair in [("quark", quark), ("lepton", lepton)]:
        require(approx(pair["commutator_norm_sq"], 36.0), f"{label} commutator norm mismatch")
        require(pair["noncommuting_hermitian_pair"] is True, f"{label} commutator not positive")
        require(pair["cp_odd_trace_commutator_cubed"] == 0.0, f"{label} CP trace not zero")
        require(pair["cp_odd_invariant_nonzero"] is False, f"{label} CP overclaimed")
    require(quark["physical_CKM_closed"] is False, "CKM overclosed")
    require(lepton["physical_PMNS_closed"] is False, "PMNS overclosed")

    decision = observables["global_observable_decision"]
    require(decision["first_non_scalar_family_splitting_emitted"] is True, "first split not emitted")
    require(decision["noncommuting_quark_and_lepton_pairs_emitted"] is True, "noncommuting pair missing")
    require(decision["twofold_degeneracy_remains_all_sectors"] is True, "degeneracy not retained")
    require(decision["u_and_e_duplicate_phase_packet"] is True, "u/e duplication missing")
    require(decision["d_and_nuD_duplicate_shift_packet"] is True, "d/nuD duplication missing")
    require(decision["CP_odd_invariant_nonzero"] is False, "CP overclosed globally")
    require(decision["full_SM_equivalence_closed"] is False, "full SM overclosed globally")

    closed = gap["closed_now"]
    require(closed["source_stack_imported_for_observable_audit"] is True, "source stack not closed in gap")
    require(closed["alpha1_dotD_retired_as_active_blocker"] is True, "alpha1 not retired in gap")
    require(closed["formal_110_sector_matrices_reconstructed"] is True, "formal matrices not reconstructed")
    require(closed["first_non_scalar_mass_splitting_detected"] is True, "mass split not detected")
    require(closed["quark_like_and_lepton_like_commutators_nonzero"] is True, "commutators not closed")
    require(closed["current_layer_CP_odd_invariant_zero_proved"] is True, "CP zero not proved")
    require(closed["current_layer_twofold_degeneracy_proved"] is True, "degeneracy not proved")
    for key in [
        "three_distinct_family_masses",
        "physical_CKM_matrix",
        "physical_PMNS_matrix",
        "nonzero_CP_odd_invariant",
        "realistic_Yukawa_magnitudes",
        "full_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(gap["not_closed"][key] is True, f"gap overclosed: {key}")

    closure = candidate["closure_decision"]
    require(closure["source_stack_closed_for_observable_audit"] is True, "candidate source stack missing")
    require(closure["alpha1_dotD_retired_as_active_blocker"] is True, "candidate alpha1 missing")
    require(closure["formal_110_first_response_audited"] is True, "candidate first response not audited")
    require(closure["first_non_scalar_family_splitting"] is True, "candidate first split missing")
    require(closure["noncommuting_sector_pairs"] is True, "candidate commutator missing")
    require(closure["twofold_degeneracy_remains"] is True, "candidate degeneracy missing")
    require(closure["CP_odd_invariant_nonzero"] is False, "candidate CP overclaimed")
    require(closure["physical_CKM_PMNS_closed"] is False, "candidate mixing overclaimed")
    require(closure["realistic_Yukawa_magnitudes_closed"] is False, "candidate Yukawa overclaimed")
    require(closure["true_SM_equivalence_closed"] is False, "candidate true SM overclaimed")
    require(closure["full_no_knob_closed"] is False, "candidate no-knob overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("Hermitian spectra      : [4, 1, 1] in every sector" in note, "note missing spectrum")
    require("CP-odd commutator cube : 0" in note, "note missing CP zero")
    require("full SM closure        : false" in note, "note missing full-SM guard")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
