"""Audit D_E transition or determinant-torsion two-slot closing run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_detransition_or_determinanttorsion_twoslotclosingrun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRANSITION = PACKET_DIR / "transition_rhoe_or_cech_dolbeault_de_edge_test.packet.json"
TORSION = PACKET_DIR / "determinant_heat_spectrum_or_torsion_edge_test.packet.json"
FRONTIER = PACKET_DIR / "post_six_slot_two_gate_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DETransition_or_DeterminantTorsion_TwoSlotClosingRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DETRANSITION_OR_DETERMINANTTORSION_TWOSLOTCLOSINGRUN_BUILT_TWO_GATES_SHARPENED"
NEXT = "MTT_Selected_TransitionPayload_or_HeatTorsionResponse_OneGateAttack_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    transition = load(TRANSITION)
    torsion = load(TORSION)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    ts = transition["support"]
    require(ts["prior_frontier_has_six_closed_two_open"] is True, "prior frontier mismatch")
    require(ts["local_diagonal_End0_DE_formula_extracted"] is True, "local D_E formula missing")
    require(ts["q79_DE_matrix_on_27_mode_BN_emitted"] is True, "q79 D_E matrix missing")
    require(ts["q79_DE_source_flags_theorem_derived_for_gap_layer"] is True, "q79 gap source missing")
    require(ts["q79_gap_layer_scope_only"] is True, "q79 scope should be gap-only")
    require(ts["q79_nonidentity_rhoE_selected_by_mtt"] is False, "rho_E overselected")
    require(ts["local_rank2_to_sector_transfer_values_extracted"] is False, "sector transfer overextracted")
    require(ts["local_validator_ready"] is False, "local validator overready")
    require(transition["slot_closes"] is False, "transition slot overclosed")
    for required in [
        "selected nonidentity rho_E transition functions/matrices or literal Cech-Dolbeault transition tables",
        "rank2-to-sector transfer values for Q,u,d,L,e,N,H on the selected q79/F,m=1 branch",
        "validator-ready D_E action matrices derived from the same selected HYM/End0 source",
        "metric/cocycle compatibility and no identity-smoke replacement",
    ]:
        require(required in transition["minimal_closing_payload"], f"transition payload missing: {required}")

    ds = torsion["support"]
    require(ds["prior_frontier_has_six_closed_two_open"] is True, "torsion prior frontier mismatch")
    require(ds["local_protected_T3_reduced_Green"] is True, "protected Green missing")
    require(ds["local_T1_T2_covariant_Green_extracted"] is False, "T1/T2 Green overextracted")
    require(ds["crossrepo_determinant_trail_present"] is True, "determinant trail missing")
    require(ds["crossrepo_torsion_trail_present"] is True, "torsion trail missing")
    require(ds["selected_HYM_End0_heat_table_emitted_here"] is False, "heat table overemitted")
    require(ds["selected_HYM_End0_spectrum_emitted_here"] is False, "spectrum overemitted")
    require(ds["selected_analytic_or_reidemeister_torsion_emitted_here"] is False, "torsion response overemitted")
    require(torsion["slot_closes"] is False, "determinant/torsion slot overclosed")
    for required in [
        "selected HYM/End0 operator spectrum or heat-kernel table on the same q79/F,m=1 source",
        "finite determinant or zeta/analytic-torsion response with normalization and cutoff policy",
        "proof that the response is attached to the selected transition/D_E payload, not an off-branch determinant",
        "reproducible validator comparing trace/heat coefficients and torsion response",
    ]:
        require(required in torsion["minimal_closing_payload"], f"torsion payload missing: {required}")

    require(frontier["operator_source_slots_closed"] == 6, "frontier closed count changed")
    require(frontier["operator_source_slots_remaining"] == 2, "frontier remaining count changed")
    require(frontier["transition_slot_closes"] is False, "frontier transition overclosed")
    require(frontier["determinant_torsion_slot_closes"] is False, "frontier torsion overclosed")
    require(frontier["recommended_primary_next"] == "transition_rhoE_or_Cech_Dolbeault_DE_data", "wrong primary next")
    require(frontier["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(frontier["no_knob_closed"] is False, "no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["operator_source_slots_closed_total"] == 6, "candidate closed count changed")
    require(closure["operator_source_slots_remaining"] == 2, "candidate remaining count changed")
    require(closure["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"] is False, "candidate transition overclosed")
    require(closure["finite_determinant_heat_spectrum_or_torsion_response_closed"] is False, "candidate torsion overclosed")
    require(data["closure_claimed"] is False, "candidate should not claim closure")
    require(data["what_closes_now"]["two_gate_frontier_sharpened"] is True, "frontier sharpen flag missing")

    require("It does not close a new slot" in note, "note no-close statement missing")
    require("q79 nonidentity `rho_E` is still not selected by MTT" in note, "note rho_E guard missing")
    require("no selected HYM/End0 heat table" in note, "note heat guard missing")
    require("Current count remains six closed operator-source slots and two open slots" in note, "note count missing")

    for packet in [data, transition, torsion, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
