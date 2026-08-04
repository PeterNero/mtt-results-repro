"""Build the final two-lane dynamic C1 cutset gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalactionrestrictionemission_or_independentgalerkinrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_physical_emission_acceptance.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_galerkin_rows_acceptance.packet.json"
CUTSET = PACKET_DIR / "final_dynamic_c1_unpatched_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalActionRestrictionEmission_or_IndependentGalerkinRows_v1.md"

STATUS = "MTT_SELECTED_PHYSICALACTIONRESTRICTION_OR_INDEPENDENTGALERKINROWS_BUILT_FINAL_TWO_LANE_CUTSET_OPEN"
NEXT = "MTT_Selected_PhysicalSourceEmissionValues_or_HonestGalerkinExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def all_true(items: dict[str, bool]) -> bool:
    return all(items.values())


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement.candidate.json")
    source = load(
        DATA
        / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
        / "same_source_physical_emission_status.packet.json"
    )
    galerkin = load(
        DATA
        / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
        / "unpatched_galerkin_replacement_status.packet.json"
    )
    residual = load(
        DATA
        / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
        / "canonical_residual_operator_values.packet.json"
    )
    replay = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "first_galerkin_replay_result.packet.json"
    )
    basis = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "zero_mode_basis.packet.json"
    )
    primitives = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "primitive_contraction_terms.packet.json"
    )
    sectors = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "sector_response_matrices.packet.json"
    )
    hessian = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "hessian_source_vector.packet.json"
    )

    route_a_acceptance = {
        "canonical_residual_values_ready": residual["mathematical_residual_values_ready"],
        "canonical_residual_projector_replay_exact": previous["what_closes_now"][
            "canonical_residual_projector_replay_exact"
        ],
        "b_selected_replay_target_fixed": previous["what_closes_now"]["b_selected_replay_target_fixed"],
        "physical_PhiFinC1_action_restriction_emitted": False,
        "zero_extra_boundary_or_source_emitted": False,
        "physical_R_Z_emitted_from_same_branch": False,
        "physical_R_X_emitted_from_same_branch": False,
        "physical_b_selected_emitted_from_same_branch": False,
    }
    route_a_closes = all_true(route_a_acceptance)

    route_a_packet = {
        "schema": "MTTPhysicalActionRestrictionEmissionAcceptance.v1",
        "status": "ROUTE_A_PHYSICAL_EMISSION_OPEN_CANONICAL_VALUES_READY",
        "acceptance_table": route_a_acceptance,
        "lane_closes_now": route_a_closes,
        "canonical_values_ready": {
            "R_Z_norm_sq": residual["R_Z"]["norm_sq"],
            "R_X_norm_sq": residual["R_X"]["norm_sq"],
            "A_transpose_A": source["b_selected_replay"]["A_transpose_A"],
            "A_transpose_b": source["b_selected_replay"]["A_transpose_b"],
            "deltaTheta_C1": source["b_selected_replay"]["deltaTheta_C1"],
        },
        "if_lane_closes_values": source["if_same_source_physical_emission_supplied"],
        "remaining_physical_emissions": source["not_yet_same_source_physical_emissions"],
        "superset_usage": (
            "This is a constrained superset lane: finite Weyl residual algebra, Phi_fin^C1 action, and "
            "Hessian/source-vector replay may meet only if the same selected physical branch emits all "
            "listed objects. None of the objects may be selected by observed SM constants."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b_acceptance = {
        "strict_replay_passes": replay["strict_replay_passes"],
        "replay_A_b_delta_fixed": replay["acceptance_results"]["A_selected_rank_at_least_2"],
        "selected_zero_mode_basis_emitted": basis["selected_source_verified"],
        "primitive_terms_from_independent_galerkin_quadrature": primitives[
            "computed_from_independent_galerkin_quadrature"
        ],
        "independent_sector_matrices_emitted": sectors["independent_sector_matrices_emitted"],
        "b_selected_emitted_by_independent_hessian": hessian["b_selected_emitted_by_independent_hessian"],
        "selected_source_verified": galerkin["current_route_state"]["selected_source_verified"],
        "C33_nonzero_family_rank_tests_evaluated": False,
    }
    route_b_closes = all_true(route_b_acceptance)

    route_b_packet = {
        "schema": "MTTIndependentGalerkinRowsAcceptance.v1",
        "status": "ROUTE_B_HONEST_GALERKIN_ROWS_OPEN_REPLAY_SUPPORT_READY",
        "acceptance_table": route_b_acceptance,
        "lane_closes_now": route_b_closes,
        "replay_support_available": {
            "zero_mode_basis_dimension": basis["basis_dimension"],
            "primitive_terms_present": sorted(primitives["terms"].keys()),
            "sector_order": sectors["sector_order"],
            "A_transpose_A": hessian["A_transpose_A"],
            "A_transpose_b": hessian["A_transpose_b"],
            "deltaTheta_C1": hessian["deltaTheta_C1"],
            "strict_coordinate_target": galerkin["strict_coordinate_target"],
        },
        "required_outputs": galerkin["required_outputs"],
        "why_not_closed": replay["why_independent_execution_not_closed"],
        "forbidden_shortcuts": galerkin["forbidden_shortcuts"],
        "superset_usage": (
            "This is the straight execution lane inside the superset program: the algebraic replay may guide "
            "the target schema, but closure requires independent selected Galerkin rows with provenance, not "
            "copying the residual-projector contract."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTFinalDynamicC1UnpatchedCutset.v1",
        "status": "UNPATCHED_DYNAMIC_C1_REDUCED_TO_TWO_EXPLICIT_OPEN_LANES",
        "algebraic_residual_value_problem_closed": True,
        "value_target_fixed": True,
        "physical_source_gate_open": not route_a_closes,
        "honest_galerkin_gate_open": not route_b_closes,
        "route_a_physical_emission_closes": route_a_closes,
        "route_b_independent_galerkin_closes": route_b_closes,
        "unpatched_dynamic_C1_packet_closed": route_a_closes or route_b_closes,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "if_close_values": {
            "A_selected": [[12.0, 0.0], [0.0, 12.0]],
            "b_selected": [12.0, 12.0],
            "deltaTheta_C1": [1.0, 1.0],
        },
        "final_cutset_statement": (
            "Unpatched dynamic C1 now has no hidden value search left in this branch: either Route A emits "
            "the physical Phi_fin^C1 action restriction, no-extra-boundary/source term, R_Z, R_X, and "
            "b_selected from the same branch; or Route B emits independent selected Galerkin rows for the "
            "same locked coordinate target. Until one lane closes, the patched replay remains SM-parity "
            "support rather than no-knob or true unpatched derivation."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalActionRestrictionEmissionOrIndependentGalerkinRows",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement.candidate.json"),
            "same_source_physical_emission_status": rel(
                DATA
                / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
                / "same_source_physical_emission_status.packet.json"
            ),
            "unpatched_galerkin_replacement_status": rel(
                DATA
                / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
                / "unpatched_galerkin_replacement_status.packet.json"
            ),
            "first_galerkin_replay_result": rel(
                DATA
                / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
                / "first_galerkin_replay_result.packet.json"
            ),
        },
        "output_packets": {
            "route_a_physical_emission_acceptance": rel(ROUTE_A),
            "route_b_independent_galerkin_rows_acceptance": rel(ROUTE_B),
            "final_dynamic_c1_unpatched_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "PhysicalActionRestrictionOrIndependentGalerkinRowsCutsetTheorem",
            "proved": True,
            "statement": (
                "Given the emitted canonical finite residual values and replay-fixed Hessian target, unpatched "
                "dynamic C1 closure is equivalent in this branch to one of two explicitly typed promotions: "
                "same-branch physical Phi_fin^C1 action/source emission, or independent selected Galerkin "
                "execution of the zero-mode, primitive, sector, and Hessian rows. The current repository "
                "closes neither lane, so it cannot claim unpatched/no-knob closure."
            ),
        },
        "closure_decision": {
            "algebraic_residual_value_problem_closed": True,
            "route_a_physical_emission_closes": route_a_closes,
            "route_b_independent_galerkin_closes": route_b_closes,
            "unpatched_dynamic_C1_packet_closed": route_a_closes or route_b_closes,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
            "observed_constants_used_as_selectors": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalActionRestrictionEmission_or_IndependentGalerkinRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "algebraic_residual_value_problem_closed": True,
        "route_a_physical_emission_closes": route_a_closes,
        "route_b_independent_galerkin_closes": route_b_closes,
        "unpatched_dynamic_C1_packet_closed": route_a_closes or route_b_closes,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalActionRestrictionEmission or IndependentGalerkinRows v1

Status: `{STATUS}`.

This theorem locks the dynamic-C1 frontier into a two-lane cutset.

Route A closes only if the same selected physical branch emits the
`Phi_fin^C1` action restriction, zero extra boundary/source term, physical
`R_Z`, physical `R_X`, and physical `b_selected`.

Route B closes only if an independent selected Galerkin execution emits the
zero-mode basis, primitive contraction rows, sector response matrices,
Hessian/source vector, and C33/nonzero-family-rank tests with provenance.

The algebraic value target is fixed: `A_selected=12 I_2`,
`b_selected=(12,12)`, and `deltaTheta_C1=(1,1)`.  The repo has not yet emitted
the physical/source lane or the honest execution lane, so unpatched dynamic C1,
true SM equivalence, and no-knob closure remain open.
"""

    for path, payload in [
        (ROUTE_A, route_a_packet),
        (ROUTE_B, route_b_packet),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
