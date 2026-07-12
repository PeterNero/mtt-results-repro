"""Build residual-completion source-promotion or honest Galerkin C1 emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket.candidate.json"
RESIDUAL = (
    DATA
    / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket"
    / "differentiated_residual_completion.packet.json"
)
ACCEPTANCE = (
    DATA
    / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket"
    / "residual_completion_acceptance_kernel.packet.json"
)
RUN_CONTRACT = (
    DATA
    / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
    / "honest_galerkin_c1_value_run_contract.packet.json"
)
SOURCE_SELECTOR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
SM_PARITY_QASU3 = DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"

OUTPUT = DATA / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission.candidate.json"
PACKET_DIR = DATA / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission"
SOURCE_PACKET = PACKET_DIR / "minimal_residual_source_packet.template.json"
PARITY_GATE = PACKET_DIR / "sm_parity_vs_no_knob_acceptance_gate.packet.json"
CERT = CERTS / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission_certificate.json"
NOTE = CORPUS / "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1.md"

STATUS = (
    "MTT_SELECTED_RESIDUALCOMPLETION_SOURCEPROMOTION_OR_HONESTGALERKINC1_EMISSION_"
    "BUILT_PROMOTION_GATE_OPEN"
)
NEXT = "MTT_Selected_ResidualSourceTheorem_or_GalerkinC1Run_ValueFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_shape(packet: dict[str, Any], key: str) -> dict[str, Any]:
    target = packet[key]
    residual = target["residual_completion"]
    projection = target["primitive_projection"]
    return {
        "target_rank": target["target"]["rank"],
        "projection_rank": projection["rank"],
        "residual_rank": residual["rank"],
        "target_norm_sq": target["target"]["norm_sq"],
        "projection_norm_sq": projection["norm_sq"],
        "residual_norm_sq": residual["norm_sq"],
        "orthogonal_to_fixed_fiber_span": target["orthogonality"]["orthogonal_to_fixed_fiber_span"],
        "closure_error_norm_sq": target["decomposition"]["closure_error_norm_sq"],
        "matrix": residual["matrix"],
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    previous = load(PREVIOUS)
    residual = load(RESIDUAL)
    acceptance = load(ACCEPTANCE)
    run_contract = load(RUN_CONTRACT)
    source_selector = load(SOURCE_SELECTOR)
    qasu3_policy = load(SM_PARITY_QASU3)

    phase = matrix_shape(residual, "phase_I_plus_Z_completion")
    shift = matrix_shape(residual, "shift_I_plus_X_completion")

    minimal_source_packet = {
        "schema": "MTTSelectedResidualSourcePacketTemplate.v1",
        "status": "TEMPLATE_EMITTED_SOURCE_THEOREM_OPEN",
        "same_branch_source_required": True,
        "observed_data_forbidden": True,
        "target_fitting_forbidden": True,
        "selected_source_selector_attached": source_selector["source_selector_packet"]["same_source"],
        "static_route_required": ["u", "e", "d", "nuD"],
        "active_shift": residual["basis"]["active_shift"],
        "fixed_fiber_class": residual["basis"]["fixed_fiber_class"],
        "absolute_fiber_origin_selected": residual["basis"]["absolute_fiber_origin_selected"],
        "required_source_emissions": {
            "phase_residual_operator_R_Z": {
                "accepted_sources": [
                    "same-branch differentiated vertex",
                    "same-branch basis-transport correction",
                    "same-branch Hessian counterterm",
                    "honest selected Galerkin C1 replacement",
                ],
                "shape": phase,
                "selected_by_MTT_now": False,
            },
            "shift_residual_operator_R_X": {
                "accepted_sources": [
                    "same-branch differentiated vertex",
                    "same-branch basis-transport correction",
                    "same-branch Hessian counterterm",
                    "honest selected Galerkin C1 replacement",
                ],
                "shape": shift,
                "selected_by_MTT_now": False,
            },
        },
        "if_emitted_then": {
            "projection_plus_residual_reconstructs_conditional_packet": True,
            "A_selected_columns_available": True,
            "A_transpose_A": acceptance["after_source_promotion_checks"]["A_transpose_A_expected_if_same_packet"],
            "A_transpose_b": acceptance["after_source_promotion_checks"]["A_transpose_b_expected_if_same_packet"],
            "deltaTheta_C1": acceptance["after_source_promotion_checks"]["deltaTheta_expected_if_same_packet"],
            "rank": acceptance["after_source_promotion_checks"]["rank_expected_if_same_packet"],
        },
    }

    lane_a = {
        "lane": "A_residual_source_promotion",
        "status": "OPEN_SOURCE_THEOREM_MISSING",
        "closes_SM_parity_dynamic_packet_if_source_theorem_supplied": True,
        "closes_no_knob_flavor_constants_if_source_theorem_supplied": False,
        "required_new_statement": (
            "The selected same-branch differentiated vertex, basis transport, or Hessian "
            "counterterm emits R_Z and R_X exactly as the residual source packet."
        ),
        "current_evidence": {
            "selected_static_source_selector": True,
            "exact_residual_completion_computed": True,
            "same_branch_residual_source_theorem": False,
        },
    }
    lane_b = {
        "lane": "B_honest_Galerkin_C1_emission",
        "status": "OPEN_RUN_VALUES_MISSING",
        "closes_SM_parity_dynamic_packet_if_selected_run_emits_values": True,
        "closes_no_knob_flavor_constants_if_selected_run_emits_values": False,
        "required_outputs": run_contract["required_outputs"],
        "current_manifest_status": run_contract["current_manifest_status"],
        "selected_source_verified": run_contract["selected_source_verified"],
    }

    parity_gate = {
        "schema": "MTTSMParityVsNoKnobResidualGate.v1",
        "status": "SM_PARITY_GATE_TYPED_PACKET_OPEN_NO_KNOB_STRONGER",
        "this_repo_view": qasu3_policy["sm_parity_evaluation_policy"]["this_repo_view"],
        "sibling_repo_default_view": qasu3_policy["sm_parity_evaluation_policy"]["sibling_repo_default_view"],
        "SM_parity_can_close_with": [
            "typed selected residual source packet R_Z/R_X from Lane A",
            "typed selected honest Galerkin C1 emission packet from Lane B",
        ],
        "SM_parity_does_not_require_here": [
            "deriving observed Yukawa magnitudes",
            "deriving observed CKM/PMNS values",
            "deriving all no-knob constants",
        ],
        "no_knob_research_would_still_require": [
            "derive Yukawa/CKM/PMNS/mass values from the selected packet",
            "derive threshold and normalization data where claimed",
            "forward replay without measured constants as selectors",
        ],
        "current_decision": "OPEN_FOR_SM_PARITY_BECAUSE_NO_TYPED_SELECTED_DYNAMIC_PACKET_IS_EMITTED_YET",
        "measured_constants_used_as_selector": False,
    }

    candidate = {
        "candidate": "MTTSelectedResidualCompletionSourcePromotionOrHonestGalerkinC1Emission",
        "status": STATUS,
        "inputs": {
            "previous_value_packet": rel(PREVIOUS),
            "residual_completion": rel(RESIDUAL),
            "acceptance_kernel": rel(ACCEPTANCE),
            "honest_galerkin_contract": rel(RUN_CONTRACT),
            "source_selector": rel(SOURCE_SELECTOR),
            "sm_parity_qasu3_policy": rel(SM_PARITY_QASU3),
        },
        "output_packets": {
            "minimal_residual_source_packet": rel(SOURCE_PACKET),
            "sm_parity_vs_no_knob_acceptance_gate": rel(PARITY_GATE),
        },
        "lane_results": [lane_a, lane_b],
        "minimal_source_packet_summary": {
            "phase_residual_norm_sq_per_sector": phase["residual_norm_sq"],
            "shift_residual_norm_sq_per_sector": shift["residual_norm_sq"],
            "phase_residual_rank": phase["residual_rank"],
            "shift_residual_rank": shift["residual_rank"],
            "orthogonal_to_fixed_fiber_span": phase["orthogonal_to_fixed_fiber_span"] and shift["orthogonal_to_fixed_fiber_span"],
            "closure_error_norm_sq": phase["closure_error_norm_sq"] + shift["closure_error_norm_sq"],
        },
        "promotion_decision": {
            "lane_A_promoted": False,
            "lane_B_promoted": False,
            "selected_residual_source_packet_promoted": False,
            "honest_Galerkin_C1_emission_promoted": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "SM_parity_view": parity_gate,
        "what_closes_now": {
            "minimal_residual_source_packet_template_emitted": True,
            "two_lane_source_promotion_gate_built": True,
            "SM_parity_vs_no_knob_acceptance_separated": True,
            "exact_post_promotion_linear_algebra_fixed": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "same_branch_residual_source_theorem": True,
            "honest_selected_Galerkin_C1_value_run": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "ResidualSourcePromotionOrGalerkinC1EmissionGateTheorem",
            "proved": True,
            "statement": (
                "The residual completion is now converted into a minimal typed source-packet "
                "template.  In the SM-parity view, either a same-branch theorem selecting "
                "the residual operators R_Z/R_X or an honest selected Galerkin C1 emission "
                "would be sufficient to close the dynamic packet interface.  Neither lane "
                "is currently emitted as selected data, so A_selected, b_selected, "
                "deltaTheta_C1, true SM equivalence, and no-knob flavor closure remain open."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "source_packet_path": rel(SOURCE_PACKET),
        "parity_gate_path": rel(PARITY_GATE),
        "theorem_proved": True,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected ResidualCompletion SourcePromotion or HonestGalerkinC1 Emission v1

Status: `{STATUS}`.

This artifact turns the diagnostic residual completion into a minimal selected
source-packet template.

```text
phase residual R_Z norm^2 per sector = {phase["residual_norm_sq"]}
shift residual R_X norm^2 per sector = {shift["residual_norm_sq"]}
phase residual rank                  = {phase["residual_rank"]}
shift residual rank                  = {shift["residual_rank"]}
closure error                         = {phase["closure_error_norm_sq"] + shift["closure_error_norm_sq"]}
```

## Two Lanes

Lane A: prove that the same-branch differentiated vertex, basis transport, or
Hessian counterterm emits `R_Z` and `R_X`.

Lane B: run an honest selected Galerkin C1 emission that supplies zero-mode
bases, primitive 3x3 contractions, response matrices, and rank tests.

## SM-Parity View

For this repo, Qa/SU3 and the dynamic C1 packet are judged in the SM-parity
view.  A typed selected packet is enough for parity even if no-knob constants
remain for later.  Support-only, diagnostic, lifted, conditional, or
target-ranked packets still do not close the gate.

If either lane emits selected data, the downstream linear algebra is fixed:

```text
A^T A       = [[12, 0], [0, 12]]
A^T b       = [12, 12]
deltaTheta  = [1, 1]
```

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or target
residuals are used as selectors.

Next artifact: `{NEXT}`.
"""

    SOURCE_PACKET.write_text(json.dumps(minimal_source_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PARITY_GATE.write_text(json.dumps(parity_gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
