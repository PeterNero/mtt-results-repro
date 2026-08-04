"""Import primitive C1 fiberclass quotient and higher-order frontier."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")

PREVIOUS = CERTS / "alpha1_driver_closure_and_postalpha_gate_import_certificate.json"
QA_INTERFACE_CERT = QA / "certificates" / "selected_u1y_routec_primitive_c1_atom_emission_interface_certificate.json"
QA_NOGO_CERT = QA / "certificates" / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo_certificate.json"
QA_SOURCEVALUE_CERT = QA / "certificates" / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor_certificate.json"
QA_EXTERNAL_CERT = QA / "certificates" / "selected_u1y_routec_external_noninvariant_c1_candidate_import_certificate.json"
QA_EXTERNAL = QA / "candidate_data" / "selected_u1y_routec_external_noninvariant_c1_candidate_import.candidate.json"
QA_FIBER_CERT = QA / "certificates" / "selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem_certificate.json"
QA_FIBER = QA / "candidate_data" / "selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem.candidate.json"
QA_HIGHER_CERT = QA / "certificates" / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_certificate.json"
QA_HIGHER = QA / "candidate_data" / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"

OUTPUT_PACKET = DATA / "primitive_c1_fiberclass_higherorder_frontier_import.candidate.json"
OUTPUT_CERT = CERTS / "primitive_c1_fiberclass_higherorder_frontier_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Primitive_C1_Fiberclass_HigherOrder_Frontier_Import_v1.md"

STATUS = "PRIMITIVE_C1_FIBERCLASS_QUOTIENT_CLOSED_HIGHERORDER_FULLRESPONSE_FRONTIER_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    interface = load(QA_INTERFACE_CERT)
    nogo = load(QA_NOGO_CERT)
    sourcevalue = load(QA_SOURCEVALUE_CERT)
    external_cert = load(QA_EXTERNAL_CERT)
    external = load(QA_EXTERNAL)
    fiber_cert = load(QA_FIBER_CERT)
    fiber = load(QA_FIBER)
    higher_cert = load(QA_HIGHER_CERT)
    higher = load(QA_HIGHER)

    tests = higher["primitive_layer_tests"]
    checks = {
        "G0_previous_frontier_is_postalpha_primitive_or_lambda": previous[
            "frontier_update"
        ]["current_next"]
        == "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1",
        "G1_atom_interface_built_exact_24_missing": interface["status"]
        == "U1Y_ROUTEC_PRIMITIVE_C1_ATOM_EMISSION_INTERFACE_BUILT_VALUES_OPEN"
        and interface["assembly_theorem_proved"]
        and interface["missing_atom_count"] == 24
        and interface["primitive_C1_atoms_emitted"] is False,
        "G2_current_corpus_atom_fill_nogo_exact_40_leaves": nogo["status"]
        == "U1Y_ROUTEC_PRIMITIVE_C1_ATOMPAYLOAD_FILL_NOGO_CURRENT_CORPUS_VALUES_OPEN"
        and nogo["fill_attempt_executed"]
        and nogo["current_corpus_supplies_selected_atom_payload"] is False
        and nogo["missing_atom_count"] == 24
        and nogo["missing_leaf_count"] == 40,
        "G3_sourcevalue_contract_built_primary_noninvariant_route": sourcevalue[
            "status"
        ]
        == "U1Y_ROUTEC_PRIMITIVE_C1_SOURCEVALUE_THEOREM_OR_NONINVARIANT_TENSOR_GATE_BUILT_OPEN"
        and sourcevalue["sourcevalue_contract_built"]
        and sourcevalue["noninvariant_tensor_route_kept_primary"]
        and sourcevalue["primitive_C1_atoms_emitted"] is False,
        "G4_external_noninvariant_candidates_imported_unselected": external_cert[
            "status"
        ]
        == "U1Y_ROUTEC_EXTERNAL_NONINVARIANT_C1_CANDIDATES_IMPORTED_SOURCE_SELECTION_OPEN"
        and external_cert["nonzero_noninvariant_candidates_imported"]
        and external_cert["nonzero_unselected_candidate_count"] == 4
        and external_cert["minimal_active_shift_required"] == [1, 1]
        and external_cert["selected_C1_closed"] is False
        and external["decision"]["active_shift_1_1_promoted_as_required_candidate_condition"],
        "G5_fiberclass_quotient_closed_for_current_spectral_observables": fiber_cert[
            "status"
        ]
        == "U1Y_ROUTEC_FIBERCLASS_C1_OBSERVABLE_QUOTIENT_CLOSED_MATRIX_REPRESENTATIVE_OPEN"
        and fiber_cert["fiberclass_quotient_for_current_C1_spectral_observables_closed"]
        and fiber_cert["shift0_allowed_as_computation_gauge"]
        and fiber_cert["selected_matrix_representative_for_full_C1_operator"] is False
        and fiber["decision"]["absolute_fiber_origin_used_as_hidden_knob"] is False,
        "G6_primitiveclass_no_split_higherorder_frontier": higher_cert["status"]
        == "U1Y_ROUTEC_PRIMITIVECLASS_C1OBSERVABLE_NO_SPLIT_HIGHERORDER_SOURCE_EMISSION_OPEN"
        and higher_cert["primitive_class_no_flavor_split_theorem"]
        and higher_cert["higher_order_or_full_response_source_emission_required"]
        and higher_cert["selected_source_emission_closed"] is False
        and higher_cert["next_required_artifact"] == NEXT,
        "G7_direct_replay_scalar_degenerate": tests["all_yy_star_scalar_identity"]
        and tests["max_traceless_norm_sq"] == 0.0
        and tests["max_commutator_norm_sq"] == 0.0
        and tests["mass_splitting_test_passes"] is False
        and tests["mixing_commutator_test_passes"] is False
        and tests["cp_odd_test_passes"] is False,
        "G8_guardrails_no_targets_no_downstream_closure": all(
            value is True for value in previous["guardrails"].values()
        )
        and higher["target_fitting_used"] is False
        and higher["guardrails"]["claims_Yukawa_CKM_PMNS_CP_or_full_SM_closure"] is False
        and higher["guardrails"]["uses_observed_data"] is False,
    }

    return {
        "packet": "Primitive_C1_Fiberclass_HigherOrder_Frontier_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "qa_atom_interface": str(QA_INTERFACE_CERT),
            "qa_atom_fill_nogo": str(QA_NOGO_CERT),
            "qa_sourcevalue_contract": str(QA_SOURCEVALUE_CERT),
            "qa_external_noninvariant": str(QA_EXTERNAL_CERT),
            "qa_fiberclass": str(QA_FIBER_CERT),
            "qa_higher_order_frontier": str(QA_HIGHER_CERT),
        },
        "theorem": {
            "name": "PrimitiveC1FiberclassHigherOrderFrontierImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The post-alpha primitive C1 branch is now reduced beyond the "
                "raw 24-atom interface.  The current corpus does not fill the "
                "selected atom payload; external non-invariant candidates reduce "
                "the live primitive route to active shift (1,1), and the fixed "
                "fiber shifts form one selected quotient class for current C1 "
                "spectral observables.  Direct replay shows the primitive class "
                "is scalar-degenerate, with Y_s Y_s^*=cI in every sector, so "
                "nondegenerate flavor requires selected correction/full-response "
                "matrix emission or selected operator-level basis transport."
            ),
        },
        "checks": checks,
        "primitive_atom_chain": {
            "interface_certificate": interface,
            "fill_nogo_certificate": nogo,
            "sourcevalue_certificate": sourcevalue,
        },
        "noninvariant_and_fiberclass_reduction": {
            "external_certificate": external_cert,
            "external_import": external,
            "fiberclass_certificate": fiber_cert,
            "fiberclass_packet": fiber,
        },
        "primitiveclass_higherorder_frontier": {
            "certificate": higher_cert,
            "packet": higher,
        },
        "frontier_update": {
            "old_next": previous["frontier_update"]["current_next"],
            "current_next": NEXT,
            "why": (
                "The primitive C1 interface and no-go, non-invariant candidate "
                "reduction, fiberclass quotient theorem, and scalar-degeneracy "
                "replay together show that the next true source is selected "
                "correction/full-response matrix emission or same-source basis "
                "transport."
            ),
        },
        "guardrails": {
            "does_not_claim_primitive_C1_atom_payload_filled": True,
            "does_not_claim_full_C1_matrix_representative": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12": True,
            "does_not_claim_Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
            "does_not_promote_diagnostic_splitter_or_basis_transport": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "Primitive-side search is narrowed: active shift (1,1), fixed "
                "fiber quotient for current spectral observables, and scalar "
                "degeneracy of the primitive class are proved/imported."
            ),
            "what_remains": (
                "Emit selected correction/full-response matrices or selected "
                "operator-level basis transport.  Current primitive quotient "
                "data cannot generate hierarchy, CKM/PMNS, CP, A_selected, "
                "b_selected, or lambda12."
            ),
            "next_required_artifact": NEXT,
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "PrimitiveC1FiberclassHigherOrderFrontierImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "checks": packet["checks"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    tests = packet["primitiveclass_higherorder_frontier"]["packet"]["primitive_layer_tests"]
    return f"""# Primitive C1 Fiberclass HigherOrder Frontier Import v1

## Result

Status: `{cert["status"]}`

The primitive C1 path has been narrowed.  The atom payload is not filled, but
the legal search space is much smaller:

```text
active shift = (1,1)
fixed fiber shifts 0,1,2 = one selected quotient class for current C1 spectral observables
representative gauge = shift 0
Y_s Y_s^* = c I for u,d,e,nuD at the current primitive layer
```

## Direct Replay

```json
{json.dumps(tests, indent=2, sort_keys=True)}
```

## Frontier

The current primitive quotient cannot by itself emit nondegenerate flavor,
`A_selected`, `b_selected`, `lambda_12`, CKM/PMNS, CP, or full SM closure.
The next source must emit selected correction/full-response matrices or
selected operator-level basis transport from the same branch.

```json
{json.dumps(packet["frontier_update"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
