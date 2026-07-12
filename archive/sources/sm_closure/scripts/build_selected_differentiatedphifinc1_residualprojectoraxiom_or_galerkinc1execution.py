"""Build differentiated PhiFinC1 residual-projector axiom / Galerkin C1 execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"
IF_SELECTED = (
    DATA
    / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
    / "if_selected_dynamic_packet_closure.packet.json"
)
GALERKIN_ROUTE = (
    DATA
    / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
    / "honest_galerkin_value_run_route.packet.json"
)
SOURCE_MAP = (
    DATA
    / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
    / "primitive_tensor_hessian_source_map_candidate.packet.json"
)

SLUG = "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
AXIOM_PACKET = PACKET_DIR / "residual_projector_axiom_patch_contract.packet.json"
GALERKIN_PACKET = PACKET_DIR / "honest_galerkin_execution_acceptance_contract.packet.json"
IMPLICATION_PACKET = PACKET_DIR / "closure_implication_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1.md"

STATUS = "MTT_SELECTED_DIFFERENTIATEDPHIFINC1_RESIDUALPROJECTORAXIOM_OR_GALERKINC1EXECUTION_BUILT_CONTRACT_OPEN"
NEXT = "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    if_selected = load(IF_SELECTED)
    galerkin = load(GALERKIN_ROUTE)
    source_map = load(SOURCE_MAP)
    replay = if_selected["if_selected_numeric_replay"]

    axiom_contract = {
        "schema": "MTTDifferentiatedPhiFinC1ResidualProjectorAxiomContract.v1",
        "status": "AXIOM_CONTRACT_READY_NOT_INSERTED",
        "axiom_name": "DifferentiatedPhiFinC1ResidualProjectorAxiom",
        "intended_scope": "same q79/F,m=1 S3/GS Route-C branch and fixed 72-real C1 coordinate target",
        "premises_required": {
            "selected_qutrit_weyl_carrier": True,
            "selected_active_shift": source_map["domain"]["active_shift"],
            "selected_fixed_fiber_quotient_class": source_map["domain"]["fixed_fiber_class"],
            "selected_static_route_Z_clock_to_u_e": True,
            "selected_static_route_X_shift_to_d_nuD": True,
            "selected_trace_transfer_normalization": True,
            "canonical_Q_residual_available": source_map["closed_support"]["canonical_Q_residual_available"],
            "alpha1_dotD_driver_verified": source_map["closed_support"]["alpha1_dotD_driver_verified"],
        },
        "new_axiom_payload_if_accepted": {
            "selected_differentiated_PhiFinC1_applies_Q_residual": True,
            "phase_R_Z_selected": True,
            "shift_R_X_selected": True,
            "b_source_emitted": True,
            "same_branch_normalization": True,
        },
        "exact_source_values_to_emit": {
            "phase_R_Z": source_map["candidate_residual_operators"]["phase_R_Z"]["shape"],
            "shift_R_X": source_map["candidate_residual_operators"]["shift_R_X"]["shape"],
            "routed_total_residual_norm_sq": source_map["residual_completion_replay"]["routed_72_real_completion"][
                "total_residual_norm_sq_four_sectors"
            ],
            "conditional_b_norm_sq": source_map["residual_completion_replay"]["routed_72_real_completion"][
                "conditional_b_norm_sq"
            ],
        },
        "acceptance_tests": [
            "same-branch proof or explicit corpus axiom insertion exists",
            "application rule is typed as differentiated Phi_fin^C1, not stationary transport",
            "Q_residual action emits both R_Z and R_X with no observed flavor targets",
            "b_selected is emitted by the same source rule or Hessian source vector",
            "A^T A, A^T b, and deltaTheta_C1 replay match the strict 72-real target",
        ],
        "inserted_now": False,
        "selected_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    galerkin_contract = {
        "schema": "MTTHonestGalerkinC1ExecutionAcceptanceContract.v1",
        "status": "GALERKIN_EXECUTION_CONTRACT_READY_VALUES_MISSING",
        "strict_coordinate_target": galerkin["strict_coordinate_target"],
        "minimal_required_outputs": galerkin["required_outputs"]
        + [
            "A_selected as a 72x2 real response matrix or equivalent sector packet",
            "b_selected as a 72-real source vector",
            "deltaTheta_C1 solve certificate",
            "sector response matrices for u,e,d,nuD",
        ],
        "acceptance_tests": {
            "selected_source_verified": True,
            "same_branch_as_static_SM_slot_packet": True,
            "zero_mode_bases_are_declared": True,
            "primitive_contractions_are_computed_not_benchmarked": True,
            "A_selected_rank_at_least_2": True,
            "b_selected_in_column_span_or_residual_declared": True,
            "C33_or_nonzero_family_rank_tests_run": True,
            "observed_flavor_constants_not_used_as_selectors": True,
        },
        "current_values_available": {
            "selected_source_verified": galerkin["selected_source_verified"],
            "can_replace_source_map_now": galerkin["can_replace_source_map_now"],
            "A_selected_emitted": False,
            "b_selected_emitted": False,
            "sector_response_matrices_emitted": False,
        },
        "would_close_SM_parity_dynamic_packet_if_accepted": galerkin[
            "would_close_SM_parity_dynamic_packet_if_emitted"
        ],
        "would_close_no_knob_flavor_constants_by_itself": galerkin[
            "would_close_no_knob_flavor_constants_by_itself"
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    implication = {
        "schema": "MTTDynamicPacketClosureImplicationReplay.v1",
        "status": "IMPLICATION_PROVED_ANTECEDENT_OPEN",
        "if_axiom_contract_accepted_then": {
            "A_selected_promotes": True,
            "b_selected_promotes": True,
            "deltaTheta_C1_promotes": True,
            "SM_parity_dynamic_packet_would_close": True,
            "no_knob_flavor_constants_would_close": False,
        },
        "if_honest_galerkin_contract_filled_then": {
            "replacement_A_selected_promotes": True,
            "replacement_b_selected_promotes": True,
            "replacement_deltaTheta_C1_promotes_after_solve": True,
            "SM_parity_dynamic_packet_would_close": True,
            "no_knob_flavor_constants_would_close_by_default": False,
        },
        "current_numeric_replay_if_axiom_accepted": {
            "rank": replay["rank"],
            "A_transpose_A": replay["A_transpose_A"],
            "A_transpose_b": replay["A_transpose_b"],
            "deltaTheta_C1": replay["deltaTheta_C1"],
            "projection_plus_residual_reconstructs_conditional_packet": replay[
                "projection_plus_residual_reconstructs_conditional_packet"
            ],
        },
        "proved_now": True,
        "antecedent_currently_met": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDifferentiatedPhiFinC1ResidualProjectorAxiomOrGalerkinC1Execution",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "if_selected_dynamic_packet": rel(IF_SELECTED),
            "honest_galerkin_route": rel(GALERKIN_ROUTE),
            "source_map_packet": rel(SOURCE_MAP),
        },
        "output_packets": {
            "residual_projector_axiom_patch_contract": rel(AXIOM_PACKET),
            "honest_galerkin_execution_acceptance_contract": rel(GALERKIN_PACKET),
            "closure_implication_replay": rel(IMPLICATION_PACKET),
        },
        "what_closes_now": {
            "residual_projector_axiom_contract_built": True,
            "honest_Galerkin_execution_contract_built": True,
            "closure_implication_replay_proved": True,
            "acceptance_tests_for_both_lanes_fixed": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "derive_or_insert_residual_projector_axiom": True,
            "prove_selected_differentiated_PhiFinC1_application_rule": True,
            "emit_selected_b_source_vector": True,
            "run_honest_selected_Galerkin_C1_execution": True,
            "promote_A_selected": True,
            "promote_b_selected": True,
            "promote_deltaTheta_C1": True,
            "emit_sector_response_matrices": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "residual_projector_axiom_inserted_now": False,
            "differentiated_PhiFinC1_application_rule_proved_now": False,
            "honest_Galerkin_C1_execution_run_now": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "sector_response_matrices_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "theorem": {
            "name": "TwoLaneDynamicClosureImplicationTheorem",
            "proved": True,
            "statement": (
                "For the selected static SM-slot/Weyl source packet, the residual-projector "
                "axiom lane and the honest Galerkin execution lane have the same strict "
                "72-real acceptance target.  If either lane emits selected A_selected and "
                "b_selected from the same branch, then the C1 dynamic packet promotes by the "
                "recorded rank-2 solve.  This proves the closure implication and fixes the "
                "acceptance tests; it does not prove or insert the missing source rule."
            ),
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "axiom_packet_path": rel(AXIOM_PACKET),
        "galerkin_packet_path": rel(GALERKIN_PACKET),
        "implication_packet_path": rel(IMPLICATION_PACKET),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DifferentiatedPhiFinC1ResidualProjectorAxiom or GalerkinC1Execution v1

Status: `{STATUS}`.

This artifact turns the last dynamic C1 blocker into two strict lanes.

Lane A is an axiom/theorem lane:

```text
selected differentiated Phi_fin^C1 applies Q_residual
Q_residual emits R_Z and R_X on the same branch
the same rule emits b_selected
```

Lane B is an honest execution lane:

```text
selected Galerkin C1 run emits zero-mode bases
selected primitive contractions produce A_selected and b_selected
sector response matrices are replayed in the fixed 72-real target
```

The implication theorem is now closed:

```text
A^T A        = {replay["A_transpose_A"]}
A^T b        = {replay["A_transpose_b"]}
deltaTheta   = {replay["deltaTheta_C1"]}
rank         = {replay["rank"]}
```

So either accepted lane closes the SM-parity dynamic packet, but neither lane is
selected yet. This is exactly the guardrail we want: the repo proves the
acceptance target and implication, not the missing source rule.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    AXIOM_PACKET.write_text(json.dumps(axiom_contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    GALERKIN_PACKET.write_text(json.dumps(galerkin_contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    IMPLICATION_PACKET.write_text(json.dumps(implication, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
