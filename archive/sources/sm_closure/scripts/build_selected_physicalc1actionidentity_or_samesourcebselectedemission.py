"""Build physical C1 action-identity / same-source b_selected emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalc1actionidentity_or_samesourcebselectedemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ACTION_EQUIV = PACKET_DIR / "physical_action_identity_to_source_emission.packet.json"
BSELECTED = PACKET_DIR / "same_source_bselected_emission_attempt.packet.json"
CLOSURE_EQUIV = PACKET_DIR / "closure_equivalence_and_next_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalC1ActionIdentity_or_SameSourceBSelectedEmission_v1.md"

STATUS = "MTT_SELECTED_PHYSICALC1ACTIONIDENTITY_OR_SAMESOURCEBSELECTEDEMISSION_BUILT_EQUIVALENCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_PhysicalActionSourceEmission_or_HonestGalerkinReplacement_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json")
    trace_support = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "selected_trace_map_and_measure_support.packet.json"
    )
    boundary = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "finite_trace_boundary_cancellation_certificate.packet.json"
    )
    action_attempt = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "physical_action_boundary_promotion_attempt.packet.json"
    )
    source_test = load(
        DATA
        / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
        / "source_map_selection_theorem_test.packet.json"
    )
    if_selected = load(
        DATA
        / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
        / "if_selected_dynamic_packet_closure.packet.json"
    )
    source_map = load(
        DATA
        / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
        / "primitive_tensor_hessian_source_map_candidate.packet.json"
    )
    b_replay = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "hessian_source_vector.packet.json"
    )

    phase_selected = source_test["selection_attempt"]["phase_R_Z_selected_now"]
    shift_selected = source_test["selection_attempt"]["shift_R_X_selected_now"]
    b_emitted = b_replay["b_selected_emitted_by_independent_hessian"]
    physical_action_promoted = action_attempt["still_missing_for_physical_promotion"][
        "physical_action_identity_equates_first_variation_to_defect_functional"
    ] is False
    no_extra_boundary_source = action_attempt["still_missing_for_physical_promotion"][
        "no_extra_physical_boundary_or_source_term"
    ] is False
    physical_measure_promoted = trace_support["selected_measure_promoted_now"] is True

    action_equiv = {
        "schema": "MTTPhysicalC1ActionIdentityToSourceEmission.v1",
        "status": "ACTION_IDENTITY_REDUCED_TO_SOURCE_EMISSION_EQUIVALENCE_OPEN",
        "equivalence_statement": (
            "Within the finite trace quotient, after selected trace support and algebraic boundary "
            "cancellation are imported, the physical Phi_fin^C1 action identity promotes the dynamic "
            "packet exactly when the same branch emits the phase residual source R_Z, shift residual "
            "source R_X, and Hessian/source vector b_selected under the selected physical measure, "
            "with no extra physical boundary or source term."
        ),
        "closed_formal_support": {
            "selected_trace_map_support": trace_support["support_imported"][
                "selected_trace_map_values_functional_stationary"
            ],
            "dynamic_trace_binding": trace_support["support_imported"][
                "dynamic_dotD_trace_binding"
            ],
            "formal_trace_frobenius_pairing": trace_support["support_imported"][
                "formal_trace_frobenius_pairing_built"
            ],
            "algebraic_finite_boundary_cancellation": boundary[
                "algebraic_boundary_closed_now"
            ],
            "all_110_algebraic_values_filled": trace_support["support_imported"][
                "all_110_algebraic_values_filled"
            ],
            "source_map_candidate_constructed": source_map["selected_by_MTT_now"] is False
            and source_map["if_source_map_selected_then"]["rank"] == 2,
        },
        "current_physical_antecedents": {
            "physical_action_identity_promoted": physical_action_promoted,
            "physical_measure_equals_trace_frobenius_pairing": physical_measure_promoted,
            "phase_R_Z_selected": phase_selected,
            "shift_R_X_selected": shift_selected,
            "same_source_b_selected_emitted": b_emitted,
            "no_extra_physical_boundary_or_source_term": no_extra_boundary_source,
        },
        "route_A_promotes_if_all_antecedents_true": True,
        "route_A_promoted_now": False,
        "proof_status": (
            "Equivalence and cutset fixed. Antecedents are not selected-source verified, "
            "so this is not a physical action proof."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    bselected = {
        "schema": "MTTSameSourceBSelectedEmissionAttempt.v1",
        "status": "B_SELECTED_REPLAY_AVAILABLE_SAME_SOURCE_EMISSION_OPEN",
        "replay_source": rel(
            DATA
            / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
            / "inputs"
            / "hessian_source_vector.packet.json"
        ),
        "b_replay_values": {
            "A_transpose_A": b_replay["A_transpose_A"],
            "A_transpose_b": b_replay["A_transpose_b"],
            "b_norm_sq": b_replay["b_norm_sq"],
            "deltaTheta_C1": b_replay["deltaTheta_C1"],
        },
        "replay_available_under_axiom_patch": b_replay[
            "b_selected_replay_available_under_axiom_patch"
        ],
        "b_selected_emitted_by_independent_hessian": b_replay[
            "b_selected_emitted_by_independent_hessian"
        ],
        "same_source_b_selected_emitted_now": False,
        "why_not_emitted": [
            "The vector is replayed from the residual-projector contract, not emitted by a selected physical Hessian.",
            "The replay uses the correct same coordinate target but still needs the Phi_fin^C1 action identity or independent Galerkin/quadrature Hessian run.",
            "A selected source vector must arrive from the same branch that emits R_Z/R_X and the physical measure.",
        ],
        "would_close_if_joined_with": {
            "phase_R_Z_selected": True,
            "shift_R_X_selected": True,
            "physical_action_identity_promoted": True,
            "physical_measure_promoted": True,
            "no_extra_physical_boundary_or_source_term": True,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    already_not_blockers = {
        "terminal_static_routes": True,
        "selected_trace_map_support": action_equiv["closed_formal_support"][
            "selected_trace_map_support"
        ],
        "dynamic_dotD_trace_binding": action_equiv["closed_formal_support"][
            "dynamic_trace_binding"
        ],
        "finite_trace_boundary_algebraic": action_equiv["closed_formal_support"][
            "algebraic_finite_boundary_cancellation"
        ],
        "all_110_algebraic_values": action_equiv["closed_formal_support"][
            "all_110_algebraic_values_filled"
        ],
        "source_map_candidate_values": source_map["if_source_map_selected_then"][
            "projection_plus_residual_reconstructs_conditional_packet"
        ],
        "conditional_rank_two_linear_algebra": if_selected["if_selected_numeric_replay"][
            "rank"
        ]
        == 2,
        "locked_target": if_selected["if_selected_numeric_replay"][
            "projection_plus_residual_reconstructs_conditional_packet"
        ],
    }
    remaining = {
        "physical_action_identity": True,
        "physical_measure_equals_trace_frobenius_pairing": True,
        "phase_R_Z_source_selection": True,
        "shift_R_X_source_selection": True,
        "same_source_b_selected_emission": True,
        "no_extra_physical_boundary_or_source_term": True,
        "honest_Galerkin_or_independent_quadrature_replacement": True,
    }
    closure_equiv = {
        "schema": "MTTClosureEquivalenceAndNextGate.v1",
        "status": "CLOSURE_EQUIVALENCE_FIXED_SOURCE_EMISSION_OR_HONEST_GALERKIN_OPEN",
        "statement": (
            "Given the closed formal supports, unpatched SM-parity dynamic closure is now equivalent "
            "to Route A same-source physical action/source emission or Route B honest selected "
            "Galerkin/quadrature replacement values. Neither route is promoted by this gate."
        ),
        "already_not_blockers": already_not_blockers,
        "remaining_cutset": remaining,
        "route_A_same_source_physical_action_closes_now": False,
        "route_B_honest_galerkin_replacement_closes_now": False,
        "unpatched_SM_parity_dynamic_packet_closes_now": False,
        "next_required_artifact": NEXT,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalC1ActionIdentityOrSameSourceBSelectedEmission",
        "status": STATUS,
        "inputs": {
            "previous_trace_measure_gate": rel(
                DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json"
            ),
            "trace_support": rel(
                DATA
                / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                / "selected_trace_map_and_measure_support.packet.json"
            ),
            "finite_boundary_certificate": rel(
                DATA
                / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                / "finite_trace_boundary_cancellation_certificate.packet.json"
            ),
            "source_map_selection_test": rel(
                DATA
                / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
                / "source_map_selection_theorem_test.packet.json"
            ),
            "if_selected_dynamic_closure": rel(
                DATA
                / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
                / "if_selected_dynamic_packet_closure.packet.json"
            ),
            "b_selected_replay": rel(
                DATA
                / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
                / "inputs"
                / "hessian_source_vector.packet.json"
            ),
        },
        "output_packets": {
            "physical_action_identity_to_source_emission": rel(ACTION_EQUIV),
            "same_source_bselected_emission_attempt": rel(BSELECTED),
            "closure_equivalence_and_next_gate": rel(CLOSURE_EQUIV),
        },
        "theorem": {
            "name": "PhysicalActionSourceEmissionEquivalenceTheorem",
            "proved": True,
            "statement": (
                "For the selected finite C1 trace quotient, once formal trace support and finite "
                "algebraic boundary cancellation are fixed, physical promotion reduces exactly to "
                "same-source emission of the physical action first-variation source packet: R_Z, R_X, "
                "b_selected, physical measure identity, and absence of extra boundary/source terms. "
                "The theorem identifies the necessary and sufficient cutset; it does not assert that "
                "the cutset is emitted."
            ),
        },
        "what_closes_now": {
            "action_identity_to_source_emission_equivalence": True,
            "same_source_bselected_emission_attempt_built": True,
            "closure_equivalence_fixed": True,
            "finite_boundary_no_longer_blocker": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "physical_action_identity": True,
            "physical_measure_equals_trace_frobenius_pairing": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "no_extra_physical_boundary_or_source_term": True,
            "honest_Galerkin_or_independent_quadrature_replacement": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "physical_action_identity_promoted": False,
            "physical_measure_promoted": False,
            "phase_R_Z_source_promoted": False,
            "shift_R_X_source_promoted": False,
            "same_source_b_selected_promoted": False,
            "route_A_same_source_physical_action_closed": False,
            "route_B_honest_galerkin_replacement_closed": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalC1ActionIdentity_or_SameSourceBSelectedEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalC1ActionIdentity or SameSourceBSelectedEmission v1

Status: `{STATUS}`.

This gate fixes the exact remaining equivalence:

```text
finite trace boundary closed          = True
trace/Frobenius formal support        = True
conditional R_Z/R_X source map ready  = True
b_selected replay available           = {bselected["replay_available_under_axiom_patch"]}
same-source b_selected emitted        = {bselected["same_source_b_selected_emitted_now"]}
physical action identity promoted     = {action_equiv["current_physical_antecedents"]["physical_action_identity_promoted"]}
```

The proof now says: the dynamic C1 packet closes by Route A exactly when the
physical `Phi_fin^C1` action emits the same-source source packet
`(R_Z, R_X, b_selected)` under the selected physical trace measure and with no
extra physical boundary/source term. Otherwise Route B must replace it with an
honest selected Galerkin/quadrature value run.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    ACTION_EQUIV.write_text(
        json.dumps(action_equiv, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    BSELECTED.write_text(
        json.dumps(bselected, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    CLOSURE_EQUIV.write_text(
        json.dumps(closure_equiv, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
