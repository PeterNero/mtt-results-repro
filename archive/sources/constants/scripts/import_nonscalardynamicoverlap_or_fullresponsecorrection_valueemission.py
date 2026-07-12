"""Import conditional non-scalar dynamic-overlap/full-response correction values."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"
SM_CERT = SM / "certificates" / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_certificate.json"

OUTPUT_PACKET = DATA / "nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_import.candidate.json"
OUTPUT_CERT = CERTS / "nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_import_certificate.json"
OUTPUT_NOTE = CORPUS / "NonScalarDynamicOverlap_or_FullResponseCorrection_ValueEmission_Import_v1.md"

STATUS = "NONSCALAR_DYNAMIC_OVERLAP_CONDITIONAL_VALUES_IMPORTED_SOURCE_OPEN"
PREVIOUS_STATUS = "DYNAMIC_OVERLAP_HESSIAN_GALERKIN_VALUE_LAYER_IMPORTED_DEGENERATE_VALUES_OPEN"
SM_STATUS = (
    "MTT_SELECTED_NONSCALARDYNAMICOVERLAP_OR_FULLRESPONSECORRECTION_VALUEEMISSION_"
    "BUILT_CONDITIONAL_VALUES_SOURCE_OPEN"
)
NEXT = "Selected_U1Y_RouteC_WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_v1"
SECTORS = ["u", "d", "e", "nuD"]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    packet = sm_packet["conditional_non_scalar_value_packet"]
    tests = packet["acceptance_tests"]
    responses = packet["sector_first_responses"]
    gate = sm_packet["promotion_gate"]
    gap = sm_packet["selected_source_gap"]

    sector_checks = {}
    for sector in SECTORS:
        inv = responses[sector]["invariants"]
        sector_checks[sector] = (
            inv["non_scalar"] is True
            and inv["traceless_norm_sq"] > 0
            and inv["hermitian_residual_norm_sq"] == 0.0
        )

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_theorem_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_packet["theorem"]["proved"] is True,
        "G2_closed_inputs_available": all(sm_packet["closed_inputs"].values()),
        "G3_conditional_packet_constructed_not_selected": packet["constructed"] is True
        and packet["selected_by_MTT"] is False
        and packet["observed_flavor_data_used"] is False
        and packet["baseline_layer"]["fiber_representative"] == 0,
        "G4_sector_responses_non_scalar_hermitian": all(sector_checks.values())
        and responses["u"]["source_direction"] == "phase_packet_I_plus_Z"
        and responses["e"]["source_direction"] == "phase_packet_I_plus_Z"
        and responses["d"]["source_direction"] == "shift_packet_I_plus_X"
        and responses["nuD"]["source_direction"] == "shift_packet_I_plus_X",
        "G5_acceptance_tests_pass_conditionally": tests["all_mass_split_positive"] is True
        and tests["ckm_commutator_positive"] is True
        and tests["pmns_commutator_positive"] is True
        and tests["cp_odd_invariant_nonzero"] is True
        and tests["current_layer_flavor_tests_pass_conditionally"] is True
        and tests["ckm_commutator_norm_sq"] > 0
        and tests["pmns_commutator_norm_sq"] > 0
        and abs(tests["cp_odd_trace_commutator_cubed_imag"]) > 0,
        "G6_promotion_gate_blocks_selected_claims": gate["conditional_non_scalar_packet_available"]
        is True
        and gate["promote_to_selected_dynamic_overlap_allowed"] is False
        and gate["promote_to_selected_full_response_allowed"] is False
        and gate["promote_to_A_selected_allowed"] is False
        and gate["promote_to_b_selected_allowed"] is False
        and gate["selected_source_to_C1_transfer_map_emitted"] is False
        and gate["selected_Hessian_blocks_emitted"] is False
        and gate["honest_Galerkin_C1_contractions_emitted"] is False,
        "G7_source_gap_sharpened": all(gap["source_level_closed"].values())
        and all(gap["dynamic_level_open"].values())
        and len(gap["minimal_next_routes"]) == 2,
        "G8_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["selected_dynamic_overlap_tensor_claimed"] is False
        and sm_packet["selected_full_response_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "NonScalarDynamicOverlap_or_FullResponseCorrection_ValueEmission_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_non_scalar_packet": str(SM_PACKET),
            "sm_non_scalar_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "ConditionalNonScalarDynamicOverlapValueImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The scalar current layer is repaired conditionally by a concrete "
                "non-scalar first full-response packet: phase I+Z routed to u/e "
                "and shift I+X routed to d/nuD. It passes finite mass-splitting, "
                "mixing, and CP acceptance tests without observed flavor data. "
                "It is not selected MTT data yet because the same-source dynamic "
                "source-to-C1 transfer, Hessian/b normalization, or honest "
                "Galerkin C1 value fill remains open."
            ),
        },
        "checks": checks,
        "closed_inputs": sm_packet["closed_inputs"],
        "conditional_non_scalar_value_packet": packet,
        "promotion_gate": gate,
        "selected_source_gap": gap,
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": sm_packet["what_remains_open"],
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "Conditional non-scalar values pass the finite tests. The next "
                "gate must promote the Weyl-pair dynamic-overlap source or fill "
                "honest selected Galerkin C1 values from the same source."
            ),
        },
        "guardrails": {
            "conditional_non_scalar_packet_available": True,
            "selected_by_MTT": False,
            "selected_dynamic_overlap_tensor_claimed": False,
            "selected_full_response_claimed": False,
            "A_selected_claimed": False,
            "b_selected_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "NonScalarDynamicOverlapOrFullResponseCorrectionValueEmissionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "frontier_update": packet["frontier_update"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    tests = packet["conditional_non_scalar_value_packet"]["acceptance_tests"]
    return f"""# NonScalarDynamicOverlap or FullResponseCorrection ValueEmission Import v1

Status: `{cert["status"]}`.

## Conditional Values

The non-scalar correction packet passes the finite flavor-readiness tests:

```text
mass split traceless norm squared = {tests["mass_split_traceless_norm_sq"]}
CKM commutator norm squared = {tests["ckm_commutator_norm_sq"]}
PMNS commutator norm squared = {tests["pmns_commutator_norm_sq"]}
CP-odd Im Tr([Hu,Hd]^3) = {tests["cp_odd_trace_commutator_cubed_imag"]}
```

The packet uses phase `I+Z` on `u,e` and shift `I+X` on `d,nuD`, with no observed flavor targets.

## Boundary

This is conditional, not selected MTT closure. Promotion still requires a
same-source dynamic source-to-C1 transfer/Hessian normalization theorem or an
honest selected Galerkin C1 value fill.

Next artifact: `{packet["next_required_artifact"]}`.
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
