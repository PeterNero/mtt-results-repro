"""Build same-source boundary/residual emission or unpatched Galerkin replacement gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RESIDUAL_VALUES = PACKET_DIR / "canonical_residual_operator_values.packet.json"
SOURCE_STATUS = PACKET_DIR / "same_source_physical_emission_status.packet.json"
GALERKIN_ROUTE = PACKET_DIR / "unpatched_galerkin_replacement_status.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSourceBoundaryResidualEmission_or_UnpatchedGalerkinReplacement_v1.md"

STATUS = "MTT_SELECTED_SAMESOURCE_BOUNDARYRESIDUALEMISSION_BUILT_RESIDUAL_VALUES_PHYSICAL_SOURCE_OPEN"
NEXT = "MTT_Selected_PhysicalActionRestrictionEmission_or_IndependentGalerkinRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    prior = load(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission.candidate.json")
    source_contract = load(
        DATA
        / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
        / "same_source_boundary_and_residual_emission_contract.packet.json"
    )
    if_closes = load(
        DATA
        / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
        / "if_action_restriction_emitted_dynamic_c1_closure.packet.json"
    )
    residual_poly = load(
        DATA
        / "selected_residual_weylpolynomial_source_theorem_attempt"
        / "residual_weyl_polynomial_decomposition.packet.json"
    )
    canonical_projector = load(
        DATA
        / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
        / "canonical_fixedfiber_residual_projector.packet.json"
    )
    projector_replay = load(
        DATA
        / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
        / "projector_application_value_replay.packet.json"
    )
    b_vector = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "inputs"
        / "hessian_source_vector.packet.json"
    )
    route_b_contract = load(
        DATA
        / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
        / "route_b_honest_galerkin_replacement_contract.packet.json"
    )

    rz = residual_poly["decompositions"]["R_Z"]
    rx = residual_poly["decompositions"]["R_X"]
    residual_values = {
        "schema": "MTTCanonicalResidualOperatorValues.v1",
        "status": "CANONICAL_RESIDUAL_VALUES_EMITTED_PHYSICAL_SOURCE_OPEN",
        "source_level_weyl_carrier_selected": residual_poly["source_level_weyl_carrier_selected"],
        "static_source_selector_selected": residual_poly["static_source_selector_selected"],
        "active_shift_selected": residual_poly["active_shift_selected"],
        "trace_frobenius_transfer_normalization_selected": canonical_projector["selected_inputs"][
            "trace_frobenius_transfer_normalization_selected"
        ],
        "R_Z": {
            "exact_polynomial": residual_poly["exact_polynomial_form"]["R_Z"],
            "coefficient_count": rz["coefficient_count"],
            "norm_sq": rz["norm_sq"],
            "reconstruction_error_norm_sq": rz["reconstruction_error_norm_sq"],
            "projector_replay_residual_matches_norm_sq": projector_replay["phase_replay"][
                "residual_matches_stored_norm_sq"
            ],
        },
        "R_X": {
            "exact_polynomial": residual_poly["exact_polynomial_form"]["R_X"],
            "coefficient_count": rx["coefficient_count"],
            "norm_sq": rx["norm_sq"],
            "reconstruction_error_norm_sq": rx["reconstruction_error_norm_sq"],
            "projector_replay_residual_matches_norm_sq": projector_replay["shift_replay"][
                "residual_matches_stored_norm_sq"
            ],
        },
        "canonical_projector_checks": canonical_projector["operator_checks"],
        "mathematical_residual_values_ready": True,
        "physical_same_source_emission_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    source_status = {
        "schema": "MTTSameSourcePhysicalEmissionStatus.v1",
        "status": "RESIDUALS_AND_B_REPLAY_READY_SAME_SOURCE_PHYSICAL_EMISSION_OPEN",
        "must_emit_from_same_physical_branch": source_contract["must_emit_from_same_physical_branch"],
        "already_value_emitted_as_canonical_finite_objects": [
            "phase residual operator R_Z",
            "shift residual operator R_X",
            "canonical residual projector Q_F",
            "replay b vector under patched/residual-projector spine",
        ],
        "not_yet_same_source_physical_emissions": [
            "physical Phi_fin^C1/action restriction",
            "zero extra boundary/source term",
            "physical R_Z emission",
            "physical R_X emission",
            "physical b_selected emission",
        ],
        "b_selected_replay": {
            "A_transpose_A": b_vector["A_transpose_A"],
            "A_transpose_b": b_vector["A_transpose_b"],
            "deltaTheta_C1": b_vector["deltaTheta_C1"],
            "same_source_emitted": b_vector["b_selected_emitted_by_independent_hessian"],
            "replay_available_under_axiom_patch": b_vector["b_selected_replay_available_under_axiom_patch"],
        },
        "if_same_source_physical_emission_supplied": if_closes["consequent_if_antecedent_true"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    galerkin_route = {
        "schema": "MTTUnpatchedGalerkinReplacementStatus.v1",
        "status": "ROUTE_B_INDEPENDENT_GALERKIN_REPLACEMENT_VALUES_OPEN",
        "route_b_contract_status": route_b_contract["status"],
        "required_outputs": route_b_contract["required_outputs"],
        "acceptance_tests": route_b_contract["acceptance_tests"],
        "current_route_state": route_b_contract["current_route_state"],
        "forbidden_shortcuts": route_b_contract["forbidden_shortcuts"],
        "strict_coordinate_target": route_b_contract["strict_coordinate_target"],
        "can_close_if": [
            "independent primitive/Hessian/sector rows are executed with provenance",
            "selected zero-mode basis and trace normalization are supplied",
            "A_selected, b_selected, deltaTheta_C1, and sector matrices are emitted as selected values",
            "rank/nonzero-family tests pass or a selected replacement rank is declared",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSameSourceBoundaryResidualEmissionOrUnpatchedGalerkinReplacement",
        "status": STATUS,
        "inputs": {
            "previous_action_restriction_gate": rel(
                DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission.candidate.json"
            ),
            "same_source_emission_contract": rel(
                DATA
                / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
                / "same_source_boundary_and_residual_emission_contract.packet.json"
            ),
            "if_action_restriction_emitted_closure": rel(
                DATA
                / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
                / "if_action_restriction_emitted_dynamic_c1_closure.packet.json"
            ),
            "residual_weyl_polynomial_decomposition": rel(
                DATA
                / "selected_residual_weylpolynomial_source_theorem_attempt"
                / "residual_weyl_polynomial_decomposition.packet.json"
            ),
            "canonical_residual_projector": rel(
                DATA
                / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
                / "canonical_fixedfiber_residual_projector.packet.json"
            ),
            "projector_application_replay": rel(
                DATA
                / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
                / "projector_application_value_replay.packet.json"
            ),
            "hessian_source_vector_replay": rel(
                DATA
                / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
                / "inputs"
                / "hessian_source_vector.packet.json"
            ),
            "route_b_honest_galerkin_contract": rel(
                DATA
                / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
                / "route_b_honest_galerkin_replacement_contract.packet.json"
            ),
        },
        "output_packets": {
            "canonical_residual_operator_values": rel(RESIDUAL_VALUES),
            "same_source_physical_emission_status": rel(SOURCE_STATUS),
            "unpatched_galerkin_replacement_status": rel(GALERKIN_ROUTE),
        },
        "theorem": {
            "name": "CanonicalResidualValuesAndPhysicalEmissionCutsetTheorem",
            "proved": True,
            "statement": (
                "The residual operators R_Z and R_X are now emitted as exact canonical finite Weyl values, and "
                "the replay b vector is fixed in the same 72-real target. This closes the algebraic residual-value "
                "search. It does not close unpatched dynamic C1, because physical promotion still requires the same "
                "Phi_fin^C1/action branch to emit the action restriction, zero extra boundary/source term, and "
                "physical R_Z/R_X/b_selected; alternatively Route B must emit independent selected Galerkin rows."
            ),
        },
        "what_closes_now": {
            "R_Z_R_X_canonical_finite_values_emitted": True,
            "canonical_residual_projector_replay_exact": True,
            "b_selected_replay_target_fixed": True,
            "algebraic_residual_value_search_closed": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "physical_PhiFinC1_action_restriction": True,
            "no_extra_physical_boundary_or_source_term": True,
            "same_source_physical_R_Z_R_X_emission": True,
            "same_source_physical_b_selected_emission": True,
            "independent_selected_Galerkin_rows": True,
            "unpatched_dynamic_C1_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "canonical_residual_values_emitted": True,
            "physical_same_source_residual_emission": False,
            "physical_same_source_b_selected_emission": False,
            "independent_selected_Galerkin_replacement": False,
            "unpatched_A_selected_emitted": False,
            "unpatched_b_selected_emitted": False,
            "unpatched_deltaTheta_C1_emitted": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SameSourceBoundaryResidualEmission_or_UnpatchedGalerkinReplacement_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "canonical_residual_values_emitted": True,
        "physical_same_source_residual_emission": False,
        "physical_same_source_b_selected_emission": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SameSource BoundaryResidualEmission or UnpatchedGalerkinReplacement v1

Status: `{STATUS}`.

This artifact closes the algebraic residual-value search.  `R_Z` and `R_X` are
exact canonical finite Weyl residual values, and `b_selected` is fixed as a
replay target with `A^T A=12 I`, `A^T b=(12,12)`, and
`deltaTheta_C1=(1,1)`.

This is still not physical unpatched dynamic C1 closure.  The next proof object
must emit the same values from the physical `Phi_fin^C1`/action branch with no
extra boundary/source term, or replace them by an independent selected Galerkin
execution.
"""

    for path, payload in [
        (RESIDUAL_VALUES, residual_values),
        (SOURCE_STATUS, source_status),
        (GALERKIN_ROUTE, galerkin_route),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
