"""Audit Step 19 primitive C1 source-value gate and tensor frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step19_primitivec1_sourcevalue_gate_or_tensorfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
GATE_PACKET = PACKET_DIR / "step19_primitive_c1_sourcevalue_gate.packet.json"
ROUTE_PACKET = PACKET_DIR / "step19_noninvariant_tensor_or_typed_connection_frontier.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step19_to_step20_atom_value_fill_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step19_PrimitiveC1_SourceValueGate_or_TensorFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP19_PRIMITIVEC1_SOURCEVALUE_GATE_CLOSED_TENSOR_OR_TYPED_CONNECTION_FRONTIER"
NEXT = "MTT_Selected_Step20_NonInvariantPrimitiveTensor_or_TypedConnectionAtomValues_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    gate = load(GATE_PACKET)
    route = load(ROUTE_PACKET)
    next_workorder = load(NEXT_WORKORDER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    assembly = gate["assembly_rule_closed"]
    require(assembly["assembly_theorem_proved"] is True, "assembly theorem not proved")
    require(assembly["sector_order"] == ["u", "d", "e", "nuD"], "sector order mismatch")
    require(len(assembly["term_order"]) == 6, "term order size mismatch")
    require("No entry may be chosen from observed masses" in assembly["no_fitting_rule"], "no-fitting rule missing")

    nogo = gate["current_corpus_fill_nogo_closed"]
    require(nogo["fill_attempt_executed"] is True, "fill attempt not executed")
    require(nogo["current_corpus_supplies_selected_atom_payload"] is False, "current corpus overclosed")
    require(nogo["emitted_atom_count"] == 0, "unexpected atom emission")
    require(nogo["missing_atom_count"] == 24, "missing atom count mismatch")
    require(nogo["missing_leaf_count"] == 40, "missing leaf count mismatch")
    require(nogo["canonical_zero_branch_tested"] is True, "canonical zero not tested")
    require(nogo["canonical_zero_branch_rejected_as_closure"] is True, "canonical zero overpromotion not blocked")

    counts = gate["missing_leaf_counts"]
    require(counts["selected_basis"] == 12, "selected basis count mismatch")
    require(counts["primitive_c1_atom_matrix"] == 24, "primitive atom count mismatch")
    require(counts["b_selected_source"] == 4, "b source count mismatch")

    closed = gate["closed_in_active_ledger"]
    for key in [
        "primitive_C1_atom_assembly_schema",
        "same_source_no_fitting_acceptance_rule",
        "current_corpus_payload_fill_attempt",
        "canonical_zero_overpromotion_blocked",
        "sourcevalue_closure_contract",
    ]:
        require(closed[key] is True, f"gate did not close {key}")

    not_closed = gate["not_closed_by_gate"]
    for key in [
        "selected_noninvariant_primitive_tensor",
        "selected_basis_transport",
        "typed_connection_derivation_values",
        "inhomogeneous_row_or_homogeneous_zero_theorem",
        "A_selected",
        "b_selected",
        "lambda_12",
        "Yukawa_or_full_SM_closure",
    ]:
        require(not_closed[key] is True, f"gate overclosed {key}")

    primitive_class = route["primitive_class_no_split_theorem"]
    require(primitive_class["primitive_fixed_fiber_class_selected_for_current_spectral_observables"] is True, "fixed fiber not selected for observables")
    require(primitive_class["primitive_class_can_emit_non_degenerate_flavor"] is False, "fixed fiber overclosed flavor")
    require(primitive_class["primitive_class_can_emit_A_selected"] is False, "fixed fiber overclosed A")
    require(primitive_class["primitive_class_can_emit_b_selected"] is False, "fixed fiber overclosed b")
    require(primitive_class["mass_splitting_test_passes"] is False, "mass split overclosed")
    require(primitive_class["mixing_commutator_test_passes"] is False, "mixing overclosed")
    require(primitive_class["cp_odd_test_passes"] is False, "CP overclosed")
    require(route["live_routes"]["primary"] == "selected_noninvariant_primitive_tensor_with_basis_transport", "wrong primary route")

    decision = data["closure_decision"]
    require(decision["step19_gate_closed"] is True, "Step 19 not closed")
    require(decision["primitive_C1_atom_assembly_schema_closed"] is True, "assembly not closed")
    require(decision["current_corpus_payload_fill_nogo_closed"] is True, "nogo not closed")
    require(decision["fixed_fiber_primitive_class_no_flavor_split_closed"] is True, "fixed-fiber theorem not closed")
    require(decision["primitive_C1_atoms_emitted"] is False, "primitive atoms overclosed")
    require(decision["emitted_atom_count"] == 0, "emitted atom count mismatch")
    require(decision["missing_atom_count"] == 24, "candidate missing atom count mismatch")
    require(decision["missing_leaf_count"] == 40, "candidate missing leaf count mismatch")
    require(decision["A_selected_computable"] is False, "A overclosed")
    require(decision["b_selected_computable"] is False, "b overclosed")
    require(decision["lambda12_closed"] is False, "lambda12 overclosed")

    require(next_workorder["next_step"] == 20, "next step mismatch")
    require(next_workorder["closed_do_not_reopen"]["Step18_alpha1_dotD_driver"] is True, "alpha anti-reopen missing")
    require(next_workorder["forbidden_next_step_wording"]["generic_galerkin_blocker_without_rows"] is True, "generic Galerkin guard missing")
    require(next_workorder["success_criterion"]["emitted_atom_count_24"] is True, "atom success criterion missing")

    for phrase in [
        "primitive C1 atom assembly schema                       closed",
        "The next target is not \"do Galerkin\" as a phrase.",
        "24 selected 3x3 primitive C1 atom matrices",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
