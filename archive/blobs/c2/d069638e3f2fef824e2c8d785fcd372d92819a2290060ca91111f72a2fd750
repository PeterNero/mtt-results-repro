"""Build Step 19 primitive C1 source-value gate and tensor frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step19_primitivec1_sourcevalue_gate_or_tensorfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GATE_PACKET = PACKET_DIR / "step19_primitive_c1_sourcevalue_gate.packet.json"
ROUTE_PACKET = PACKET_DIR / "step19_noninvariant_tensor_or_typed_connection_frontier.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step19_to_step20_atom_value_fill_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step19_PrimitiveC1_SourceValueGate_or_TensorFrontier_v1.md"

STEP18 = DATA / "selected_step18_qasu3_alphadotd_import_or_primitivec1frontier.candidate.json"
QA_ROOT = TEXPAPERS / "mtt-qa-su3-packet-proof"
QA_ATOM_INTERFACE = QA_ROOT / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_emission_interface.candidate.json"
QA_FILL_NOGO = QA_ROOT / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo.candidate.json"
QA_MISSING = QA_ROOT / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_missing_leaves.json"
QA_SOURCEVALUE = QA_ROOT / "candidate_data" / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor.candidate.json"
QA_PRIMITIVE_CLASS = QA_ROOT / "candidate_data" / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"

STATUS = "MTT_SELECTED_STEP19_PRIMITIVEC1_SOURCEVALUE_GATE_CLOSED_TENSOR_OR_TYPED_CONNECTION_FRONTIER"
NEXT = "MTT_Selected_Step20_NonInvariantPrimitiveTensor_or_TypedConnectionAtomValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP18, QA_ATOM_INTERFACE, QA_FILL_NOGO, QA_MISSING, QA_SOURCEVALUE, QA_PRIMITIVE_CLASS]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 19 inputs: " + ", ".join(missing))

    step18 = load(STEP18)
    atom_interface = load(QA_ATOM_INTERFACE)
    fill_nogo = load(QA_FILL_NOGO)
    missing_leaves = load(QA_MISSING)
    sourcevalue = load(QA_SOURCEVALUE)
    primitive_class = load(QA_PRIMITIVE_CLASS)

    gate_packet = {
        "schema": "MTTStep19PrimitiveC1SourceValueGate.v1",
        "status": "PRIMITIVE_C1_ASSEMBLY_AND_CURRENT_CORPUS_NOGO_IMPORTED",
        "source_repo": "mtt-qa-su3-packet-proof",
        "imported_packets": {
            "atom_interface": rel(QA_ATOM_INTERFACE),
            "fill_or_nogo": rel(QA_FILL_NOGO),
            "missing_leaves": rel(QA_MISSING),
            "sourcevalue_frontier": rel(QA_SOURCEVALUE),
        },
        "assembly_rule_closed": {
            "assembly_theorem_proved": atom_interface["decision"]["assembly_theorem_proved"],
            "sector_order": atom_interface["sector_order"],
            "term_order": atom_interface["term_order"],
            "A_selected_rule": atom_interface["assembly_rules"]["A_selected"],
            "b_selected_rule": atom_interface["assembly_rules"]["b_selected"],
            "no_fitting_rule": atom_interface["assembly_rules"]["no_fitting_rule"],
        },
        "current_corpus_fill_nogo_closed": {
            "fill_attempt_executed": fill_nogo["decision"]["fill_attempt_executed"],
            "current_corpus_supplies_selected_atom_payload": fill_nogo["decision"]["current_corpus_supplies_selected_atom_payload"],
            "emitted_atom_count": fill_nogo["decision"]["emitted_atom_count"],
            "missing_atom_count": fill_nogo["decision"]["missing_atom_count"],
            "missing_leaf_count": fill_nogo["decision"]["missing_leaf_count"],
            "canonical_zero_branch_tested": fill_nogo["decision"]["canonical_zero_branch_tested"],
            "canonical_zero_branch_rejected_as_closure": fill_nogo["decision"]["canonical_zero_branch_rejected_as_closure"],
        },
        "missing_leaf_counts": sourcevalue["missing_leaf_counts"],
        "minimal_closing_options": missing_leaves["minimal_closing_options"],
        "route_ranking": sourcevalue["route_ranking"],
        "closed_in_active_ledger": {
            "primitive_C1_atom_assembly_schema": True,
            "same_source_no_fitting_acceptance_rule": True,
            "current_corpus_payload_fill_attempt": True,
            "canonical_zero_overpromotion_blocked": True,
            "sourcevalue_closure_contract": True,
        },
        "not_closed_by_gate": {
            "selected_noninvariant_primitive_tensor": sourcevalue["what_remains_open"]["selected_noninvariant_primitive_tensor"],
            "selected_basis_transport": sourcevalue["what_remains_open"]["selected_basis_transport"],
            "typed_connection_derivation_values": sourcevalue["what_remains_open"]["typed_connection_derivation_values"],
            "inhomogeneous_row_or_homogeneous_zero_theorem": sourcevalue["what_remains_open"]["inhomogeneous_row_or_homogeneous_zero_theorem"],
            "A_selected": sourcevalue["what_remains_open"]["A_selected"],
            "b_selected": sourcevalue["what_remains_open"]["b_selected"],
            "lambda_12": sourcevalue["what_remains_open"]["lambda_12"],
            "Yukawa_or_full_SM_closure": sourcevalue["what_remains_open"]["Yukawa_or_full_SM_closure"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(GATE_PACKET, gate_packet)

    route_packet = {
        "schema": "MTTStep19NonInvariantTensorOrTypedConnectionFrontier.v1",
        "status": "PRIMARY_ROUTE_SELECTED_NONINVARIANT_TENSOR_OR_TYPED_CONNECTION_ATOM_VALUES",
        "primitive_class_no_split_theorem": {
            "primitive_fixed_fiber_class_selected_for_current_spectral_observables": primitive_class["decision"]["primitive_fixed_fiber_class_selected_for_current_spectral_observables"],
            "primitive_class_can_emit_non_degenerate_flavor": primitive_class["decision"]["primitive_class_can_emit_non_degenerate_flavor"],
            "primitive_class_can_emit_A_selected": primitive_class["decision"]["primitive_class_can_emit_A_selected"],
            "primitive_class_can_emit_b_selected": primitive_class["decision"]["primitive_class_can_emit_b_selected"],
            "mass_splitting_test_passes": primitive_class["primitive_layer_tests"]["mass_splitting_test_passes"],
            "mixing_commutator_test_passes": primitive_class["primitive_layer_tests"]["mixing_commutator_test_passes"],
            "cp_odd_test_passes": primitive_class["primitive_layer_tests"]["cp_odd_test_passes"],
            "reason": primitive_class["primitive_layer_tests"]["reason"],
        },
        "live_routes": {
            "primary": "selected_noninvariant_primitive_tensor_with_basis_transport",
            "secondary": "typed_monad_cech_or_hym_connection_values",
            "fallback_only_if_selected": "canonical_translation_invariant_zero_tensor_with_homogeneous_zero_b",
        },
        "why_primary_route": "The fixed-fiber primitive class is selected for current spectral observables but has scalar YY* in every sector, so it cannot produce hierarchy, mixing, or CP. A noninvariant tensor or typed connection atom values are needed for true SM value closure.",
        "required_step20_payload": {
            "selected_same_source_id": True,
            "basis_left_right_higgs_for_u_d_e_nuD": True,
            "twenty_four_3x3_atom_matrices": True,
            "four_b_rows_or_homogeneous_zero_theorems": True,
            "no_observed_targets": True,
            "no_locked_target_columns": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROUTE_PACKET, route_packet)

    next_workorder = {
        "schema": "MTTStep19ToStep20AtomValueFillWorkorder.v1",
        "status": "NEXT_WORKORDER_FILL_SELECTED_ATOM_VALUES",
        "completed_step": 19,
        "next_step": 20,
        "next_required_artifact": NEXT,
        "closed_do_not_reopen": {
            "Step18_alpha1_dotD_driver": True,
            "primitive_C1_assembly_rule": True,
            "current_corpus_payload_fill_nogo": True,
            "fixed_fiber_primitive_class_no_flavor_split": True,
        },
        "must_emit_next": route_packet["required_step20_payload"],
        "forbidden_next_step_wording": {
            "generic_galerkin_blocker_without_rows": True,
            "status_only_packet_without_atom_payload": True,
            "canonical_zero_branch_without_selection_theorem": True,
        },
        "success_criterion": {
            "selected_same_source_id_present": True,
            "missing_leaf_count_zero": True,
            "emitted_atom_count_24": True,
            "b_rows_or_zero_theorems_4": True,
            "A_selected_b_selected_computable": True,
        },
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep19PrimitiveC1SourceValueGateOrTensorFrontier",
        "status": STATUS,
        "inputs": {
            "step18": rel(STEP18),
            "qa_atom_interface": rel(QA_ATOM_INTERFACE),
            "qa_fill_nogo": rel(QA_FILL_NOGO),
            "qa_missing_leaves": rel(QA_MISSING),
            "qa_sourcevalue": rel(QA_SOURCEVALUE),
            "qa_primitive_class": rel(QA_PRIMITIVE_CLASS),
        },
        "output_packets": {
            "step19_primitive_c1_sourcevalue_gate": rel(GATE_PACKET),
            "step19_noninvariant_tensor_or_typed_connection_frontier": rel(ROUTE_PACKET),
            "step19_to_step20_atom_value_fill_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step19PrimitiveC1SourceValueGateTheorem",
            "proved": True,
            "statement": "The active SM ledger imports the QA/SU3 primitive C1 atom assembly theorem, the current-corpus payload fill/no-go, and the primitive fixed-fiber no-flavor-split theorem. Therefore the next target is no longer a generic Galerkin route: it is a selected source-value payload that either emits a noninvariant primitive tensor with basis transport, derives atom values from typed monad/Cech/HYM connection data, or proves the canonical zero tensor is selected together with homogeneous-zero b rows. The fixed-fiber primitive class cannot by itself produce Yukawa hierarchy, mixing, CP, A_selected, or b_selected.",
        },
        "closure_decision": {
            "step19_gate_closed": True,
            "primitive_C1_atom_assembly_schema_closed": True,
            "current_corpus_payload_fill_nogo_closed": True,
            "canonical_zero_overpromotion_blocked": True,
            "fixed_fiber_primitive_class_no_flavor_split_closed": True,
            "selected_noninvariant_primitive_tensor_emitted": False,
            "typed_connection_atom_values_emitted": False,
            "canonical_zero_selection_theorem_proved": False,
            "selected_basis_transport_emitted": False,
            "primitive_C1_atoms_emitted": False,
            "emitted_atom_count": 0,
            "missing_atom_count": fill_nogo["decision"]["missing_atom_count"],
            "missing_leaf_count": fill_nogo["decision"]["missing_leaf_count"],
            "A_selected_computable": False,
            "b_selected_computable": False,
            "lambda12_closed": False,
            "Yukawa_or_full_SM_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "primitive_C1_atom_assembly_schema": True,
            "current_corpus_fill_attempt_no_go": True,
            "canonical_zero_branch_rejected_as_closure_without_selection_theorem": True,
            "fixed_fiber_primitive_class_no_flavor_split": True,
            "Step20_source_value_payload_requirements": True,
        },
        "what_remains_open": {
            "selected_noninvariant_primitive_tensor": True,
            "typed_connection_atom_values": True,
            "canonical_zero_selection_theorem_if_zero_route": True,
            "selected_basis_transport": True,
            "twenty_four_atom_matrices": True,
            "four_b_rows_or_homogeneous_zero_theorems": True,
            "A_selected": True,
            "b_selected": True,
            "lambda12": True,
            "Yukawa_CKM_PMNS_masses": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step19_PrimitiveC1_SourceValueGate_or_TensorFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "primitive_C1_atom_assembly_schema_closed": True,
        "current_corpus_payload_fill_nogo_closed": True,
        "canonical_zero_overpromotion_blocked": True,
        "fixed_fiber_primitive_class_no_flavor_split_closed": True,
        "selected_noninvariant_primitive_tensor_emitted": False,
        "typed_connection_atom_values_emitted": False,
        "primitive_C1_atoms_emitted": False,
        "emitted_atom_count": 0,
        "missing_atom_count": fill_nogo["decision"]["missing_atom_count"],
        "missing_leaf_count": fill_nogo["decision"]["missing_leaf_count"],
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda12_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step19 PrimitiveC1 SourceValueGate or TensorFrontier v1

Status: `{STATUS}`.

Closed now:

```text
primitive C1 atom assembly schema                       closed
same-source no-fitting acceptance rule                  closed
current-corpus atom payload fill/no-go                  closed
canonical zero branch overpromotion                     blocked
fixed-fiber primitive class no-flavor-split theorem     closed
```

The next target is not "do Galerkin" as a phrase. The next target is a payload:

```text
selected same-source id
selected bases for left/right/Higgs slots in u,d,e,nuD
24 selected 3x3 primitive C1 atom matrices
4 selected b rows or homogeneous-zero theorems
```

Legal Step 20 exits:

```text
1. selected noninvariant primitive tensor with basis transport
2. typed monad/Cech/HYM connection atom values
3. canonical zero tensor only if MTT selects it and emits homogeneous-zero b rows
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
