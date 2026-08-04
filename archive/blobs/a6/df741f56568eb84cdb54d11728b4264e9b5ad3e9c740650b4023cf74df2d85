"""Import differentiated PhiFinC1 primitive-overlap / Galerkin boundary."""

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

PREVIOUS = CERTS / "phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
SM_CERT = SM / "certificates" / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun_certificate.json"
SM_TEMPLATE = (
    SM
    / "candidate_data"
    / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun"
    / "primitive_overlap_contractions.template.json"
)

OUTPUT_PACKET = DATA / "differentiated_phifinc1_primitiveoverlap_or_galerkinrun_import.candidate.json"
OUTPUT_CERT = CERTS / "differentiated_phifinc1_primitiveoverlap_or_galerkinrun_import_certificate.json"
OUTPUT_TEMPLATE = (
    DATA
    / "differentiated_phifinc1_primitiveoverlap_or_galerkinrun_import"
    / "primitive_overlap_contractions.template.json"
)
OUTPUT_NOTE = CORPUS / "DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_Import_v1.md"

STATUS = "DIFFERENTIATED_PHIFINC1_PRIMITIVE_OVERLAP_IMPORTED_TRANSPORT_NOGO_TEMPLATE_OPEN"
PREVIOUS_STATUS = "PHIFINC1_DYNAMIC_TRANSFER_ATTEMPT_IMPORTED_STATIONARY_TRACE_CLOSED_C1_OPEN"
SM_STATUS = "MTT_SELECTED_DIFFERENTIATED_PHIFINC1_PRIMITIVEOVERLAP_OR_GALERKINRUN_BUILT_TRANSPORT_ONLY_NOGO_TEMPLATE_OPEN"
NEXT = "MTT_Selected_PrimitiveVertexSource_or_BasisTransport_SelectionTheorem_v1"
SECTORS = ["u", "d", "e", "nuD"]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    sm_template = load(SM_TEMPLATE)

    driver = sm_packet["driver_contract"]
    canonical = sm_packet["canonical_transport_only_test"]
    noninvariant = sm_packet["noninvariant_candidate_import"]
    contract = sm_packet["differentiated_primitive_overlap_contract"]
    nogo = sm_packet["transport_only_no_go_theorem"]
    decision = sm_packet["promotion_decision"]

    empty_template_slots = all(
        sm_template["required_selected_values"]["primitive_three_by_three_contraction_terms"][sector] is None
        and sm_template["required_selected_values"]["linear_response_matrices"][sector] is None
        and sm_template["required_selected_values"]["Hessian_counterterms"][sector] is None
        for sector in SECTORS
    )

    checks = {
        "H0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "H1_upstream_boundary_matches": sm_packet["status"] == SM_STATUS
        and sm_cert["status"] == SM_STATUS
        and sm_cert["transport_only_no_go_proved"] is True,
        "H2_driver_attached_but_not_value_emitting": driver["selected_dotD_source_verified"] is True
        and driver["alpha1_driver_verified"] is True
        and driver["honest_dotD_alpha1_replay"] is True
        and driver["attached_to_differentiated_contract_as_driver"] is True
        and driver["primitive_overlap_values_emitted_by_driver"] is False,
        "H3_transport_only_nogo_proved": nogo["proved"] is True
        and canonical["all_c1_matrices_zero_for_canonical_tensor"] is True
        and canonical["all_sector_matrices_verified_zero"] is True
        and canonical["can_emit_phase_shift_columns"] is False,
        "H4_noninvariant_candidates_imported_unselected": noninvariant["active_shift"] == [1, 1]
        and noninvariant["selected_by_theorem"] is False
        and noninvariant["primitive_envelope_constructed"] is True
        and noninvariant["primitive_envelope_selected_as_dynamic_tensor"] is False
        and noninvariant["candidate_summary"]["fixed_fiber_candidates"] == [0, 1, 2]
        and noninvariant["candidate_summary"]["all_fixed_fiber_rank_three"] is True
        and noninvariant["candidate_summary"]["all_fiber_rank_one"] is True,
        "H5_template_open_and_coordinate_fixed": sm_template["status"]
        == "OPEN_SELECTED_PRIMITIVE_OVERLAP_CONTRACTIONS_MISSING"
        and sm_template["coordinate_system"]["codomain_real_dimension"] == 72
        and sm_template["coordinate_system"]["columns"] == ["phase_packet", "shift_packet"]
        and empty_template_slots
        and contract["template_status"] == "OPEN_SELECTED_PRIMITIVE_OVERLAP_CONTRACTIONS_MISSING"
        and contract["normal_form_values_promoted_now"] is False,
        "H6_conditional_values_retained_unpromoted": sm_packet["conditional_dynamic_values_retained_as_unpromoted"][
            "Gram_A_transpose_A"
        ]
        == [[12.0, 0.0], [0.0, 12.0]]
        and sm_packet["conditional_dynamic_values_retained_as_unpromoted"]["A_transpose_b_conditional"]
        == [12.0, 12.0]
        and sm_packet["conditional_dynamic_values_retained_as_unpromoted"][
            "deltaTheta_conditional_from_Gram_solve"
        ]
        == [1.0, 1.0],
        "H7_no_selected_matrix_or_closure_overclaim": decision[
            "selected_primitive_vertex_or_basis_transport_emitted"
        ]
        is False
        and decision["selected_primitive_overlap_contractions_promoted"] is False
        and decision["selected_A_selected_promoted"] is False
        and decision["selected_b_selected_promoted"] is False
        and decision["selected_deltaTheta_C1_promoted"] is False
        and decision["honest_Galerkin_C1_contractions_promoted"] is False
        and decision["full_SM_no_knob_closure_promoted"] is False
        and sm_packet["closure_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_differentiated_packet": str(SM_PACKET),
            "sm_differentiated_certificate": str(SM_CERT),
            "sm_primitive_overlap_template": str(SM_TEMPLATE),
        },
        "theorem": {
            "name": "DifferentiatedPhiFinC1TransportOnlyNoGoImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected alpha1/dotD driver attaches to the differentiated "
                "PhiFinC1 contract, but pure stationary transport with the canonical "
                "mode-conserving primitive tensor emits zero C1 response matrices. "
                "Therefore the phase/shift columns require a selected primitive "
                "vertex source, basis-transport correction, Hessian source term, "
                "or honest Galerkin C1 contraction fill."
            ),
        },
        "checks": checks,
        "coordinate_system": sm_packet["differentiated_primitive_overlap_contract"]["coordinate_system"],
        "driver_contract": driver,
        "transport_only_no_go_theorem": nogo,
        "canonical_transport_only_test": canonical,
        "noninvariant_candidate_import": noninvariant,
        "differentiated_primitive_overlap_contract": contract,
        "primitive_overlap_template": sm_template,
        "conditional_dynamic_values_retained_as_unpromoted": sm_packet[
            "conditional_dynamic_values_retained_as_unpromoted"
        ],
        "promotion_decision": decision,
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": sm_packet["what_remains_open"],
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "The transport-only lane is now rejected by finite C1 computation. "
                "The next source theorem must select the primitive vertex, basis "
                "transport, Hessian source, or honest Galerkin values."
            ),
        },
        "guardrails": {
            "transport_only_lane_rejected": True,
            "selected_primitive_overlap_contractions_claimed": False,
            "selected_primitive_vertex_source_claimed": False,
            "selected_A_selected_claimed": False,
            "selected_b_selected_claimed": False,
            "selected_deltaTheta_C1_claimed": False,
            "honest_Galerkin_C1_contractions_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "DifferentiatedPhiFinC1PrimitiveOverlapOrGalerkinRunImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "template_path": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "transport_only_no_go_proved": packet["transport_only_no_go_theorem"]["proved"],
        "primitive_overlap_template_emitted": True,
        "frontier_update": packet["frontier_update"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    values = packet["conditional_dynamic_values_retained_as_unpromoted"]
    return f"""# DifferentiatedPhiFinC1 PrimitiveOverlapContractions or GalerkinRun Import v1

Status: `{cert["status"]}`.

## Closed

The selected alpha1/dotD driver is attached to the differentiated `Phi_fin^C1`
contract.  The canonical transport-only lane is rejected: pure stationary
transport with the canonical mode-conserving primitive tensor emits zero C1
matrices in all four sectors, so it cannot produce the phase/shift columns.

## Template

The primitive-overlap template is imported at:

```text
{cert["template_path"]}
```

It keeps the primitive three-by-three contractions, linear response matrices,
Hessian counterterms, `A_selected`, `b_selected`, and `deltaTheta_C1` empty until
a selected primitive vertex / basis-transport source theorem or an honest
selected Galerkin C1 run fills them.

## Conditional Values

The normal-form values remain diagnostic only:

```text
A^T A = {values["Gram_A_transpose_A"]}
A^T b = {values["A_transpose_b_conditional"]}
deltaTheta_C1 = {values["deltaTheta_conditional_from_Gram_solve"]}
```

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{packet["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_TEMPLATE.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(
            json.dumps(packet["primitive_overlap_template"], indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
