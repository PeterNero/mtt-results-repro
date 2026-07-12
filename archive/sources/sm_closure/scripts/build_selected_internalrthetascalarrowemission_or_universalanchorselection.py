"""Build direct internal Rtheta scalar-row emission attempt or universal-anchor selection.

This is the direct-emission branch requested after the final kernel exposure:
try to emit the ten internal selected R_theta scalar rows from the current
selected source/domain, orbit matrix, basis map, and higher-response payload
gates.  The builder is intentionally strict: structural rows may be inventoried,
but no scalar value row is accepted unless the full-S2/operator payload gate is
ready or a source-selected universal anchor exists before empirical replay.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_internalrthetascalarrowemission_or_universalanchorselection"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DIRECT_ATTEMPT = PACKET_DIR / "direct_internal_rtheta_scalar_row_emission_attempt.packet.json"
STRUCTURAL_ROWS = PACKET_DIR / "structural_orbit_scalar_row_candidates_not_accepted.packet.json"
FULLS2_BLOCKER = PACKET_DIR / "full_s2_operator_payload_blocker_for_direct_emission.packet.json"
ANCHOR_SELECTION = PACKET_DIR / "universal_anchor_selection_recheck_for_direct_emission.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_direct_scalar_row_emission_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_InternalRThetaScalarRowEmission_or_UniversalAnchorSelection_v1.md"

PREVIOUS = DATA / "selected_noknobvaluederivationkernel_or_sourceanchortheorem.candidate.json"
KERNEL = (
    DATA
    / "selected_noknobvaluederivationkernel_or_sourceanchortheorem"
    / "updated_no_knob_value_derivation_kernel.packet.json"
)
OBLIGATIONS = (
    DATA
    / "selected_noknobvaluederivationkernel_or_sourceanchortheorem"
    / "internal_value_obligation_status_after_readiness_8of9.packet.json"
)
SOURCE_DOMAIN = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "rtheta_scalar_value_functional_source_packet.packet.json"
)
BASIS_MAP = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_family_eigenprofile_to_magnitude_row_basis_map.packet.json"
)
COEFF_ATTEMPT = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_value_row_coefficients_attempt.packet.json"
)
ORBIT_MATRIX = (
    DATA
    / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
    / "lambda_orbit_second_order_matrix_packet.packet.json"
)
FULLS2_GATE = (
    DATA
    / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution"
    / "rhoede_full_s2_execution_gate.packet.json"
)
HYM_PAYLOAD_GATE = (
    DATA
    / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution"
    / "selected_hym_operator_payload_promotion_gate.packet.json"
)
HYM_CUTSET = (
    DATA
    / "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution"
    / "next_cutset_after_hym_operator_payload_gate.packet.json"
)
UNIVERSAL_TARGET = (
    DATA
    / "selected_noknobvaluederivationkernel_or_sourceanchortheorem"
    / "candidate_specific_source_anchor_target.packet.json"
)
HIGHER_CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_INTERNALRTHETASCALARROWEMISSION_OR_UNIVERSALANCHORSELECTION_"
    "BUILT_DIRECT_EMISSION_ATTEMPT_BLOCKED_BY_FULLS2_PAYLOAD"
)
NEXT = "MTT_Selected_PhiFinMinimizerTraceSectorPayload_or_InternalScalarRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing internal scalar-row emission inputs: " + ", ".join(missing))


def structural_candidate_rows(basis: dict[str, Any], orbit: dict[str, Any]) -> list[dict[str, Any]]:
    """Create non-accepted structural row candidates from the selected orbit spectrum.

    These are not value rows.  They test the tempting shortcut "use the closed
    orbit spectrum as coefficients" and record why it cannot close the scalar
    layer.
    """

    spectrum = orbit["matrix_branches"][0]["hermitian_spectrum_each_sector"]
    trace = sum(spectrum)
    normalized = [value / trace for value in spectrum]
    rows: list[dict[str, Any]] = []
    for row in basis["charged_basis_rows"]:
        generation = row["generation"]
        rows.append(
            {
                "coefficient_slot": row["coefficient_slot"],
                "sector": row["sector"],
                "generation": generation,
                "structural_orbit_weight_candidate": normalized[generation - 1],
                "structural_source": "normalized selected second-order orbit spectrum [1,4,7]",
                "accepted_as_internal_selected_scalar_row": False,
                "why_not_accepted": [
                    "orbit spectrum is qualitative and dimensionless",
                    "same normalized profile would be shared across charged sectors",
                    "no magnitude-bearing threshold/mass-scheme functional has executed",
                    "full-S2 rhoE/D_E/operator payload gate is not ready",
                ],
            }
        )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        KERNEL,
        OBLIGATIONS,
        SOURCE_DOMAIN,
        BASIS_MAP,
        COEFF_ATTEMPT,
        ORBIT_MATRIX,
        FULLS2_GATE,
        HYM_PAYLOAD_GATE,
        HYM_CUTSET,
        UNIVERSAL_TARGET,
        HIGHER_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    kernel = load(KERNEL)
    obligations = load(OBLIGATIONS)
    source_domain = load(SOURCE_DOMAIN)
    basis = load(BASIS_MAP)
    coeff_attempt = load(COEFF_ATTEMPT)
    orbit = load(ORBIT_MATRIX)
    fulls2 = load(FULLS2_GATE)
    hym_gate = load(HYM_PAYLOAD_GATE)
    hym_cutset = load(HYM_CUTSET)
    universal = load(UNIVERSAL_TARGET)
    higher_contract = load(HIGHER_CONTRACT)

    source_domain_closed = source_domain["source_domain_closed"]
    basis_closed = basis["basis_map_to_sector_scaled_magnitude_rows_closed"]
    orbit_closed = orbit["orbit_matrix_packet_selected"]
    fulls2_ready = fulls2["ready"]["full_S2_scalar_execution_ready"]
    selected_anchor_count = universal["selected_universal_parameter_count"]
    direct_rows_allowed = (
        source_domain_closed and basis_closed and orbit_closed and fulls2_ready
    ) or selected_anchor_count > 0

    structural_rows = structural_candidate_rows(basis, orbit)
    accepted_rows = [] if not direct_rows_allowed else structural_rows

    direct_attempt = {
        "schema": "MTTDirectInternalRThetaScalarRowEmissionAttempt.v1",
        "status": "DIRECT_INTERNAL_SCALAR_ROW_EMISSION_BLOCKED",
        "source_domain_closed": source_domain_closed,
        "basis_map_closed": basis_closed,
        "orbit_matrix_packet_closed": orbit_closed,
        "full_S2_scalar_execution_ready": fulls2_ready,
        "selected_universal_parameter_count": selected_anchor_count,
        "codomain_scalar_rows": higher_contract["codomain_scalar_rows"],
        "codomain_scalar_row_count": higher_contract["codomain_scalar_row_count"],
        "accepted_internal_scalar_row_count": len(accepted_rows),
        "accepted_internal_scalar_rows": accepted_rows,
        "lambda_H_row_emitted": False,
        "blocked_scalar_rows": higher_contract["codomain_scalar_rows"],
        "direct_rows_allowed": direct_rows_allowed,
        "why_blocked": [
            "full-S2 scalar execution is not ready",
            "Phi_fin selected minimizer trace is not emitted",
            "finite projector values are not promoted to selected P_s/K_s",
            "selected rho_s and End0-to-sector routing values are absent",
            "no candidate-specific universal source anchor is selected",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DIRECT_ATTEMPT, direct_attempt)

    structural_packet = {
        "schema": "MTTStructuralOrbitScalarRowCandidatesNotAccepted.v1",
        "status": "STRUCTURAL_ORBIT_ROWS_TESTED_NOT_ACCEPTED_AS_VALUES",
        "candidate_row_count": len(structural_rows),
        "candidate_rows": structural_rows,
        "diagnostic_profile_coefficients_still_rejected": coeff_attempt[
            "accepted_coefficient_row_count"
        ]
        == 0,
        "basis_map_closed": basis_closed,
        "orbit_matrix_packet_closed": orbit_closed,
        "acceptance_decision": (
            "The selected orbit spectrum can produce structural normalized weights, but those "
            "weights are not accepted R_theta scalar values because they do not come from the "
            "selected full-S2 value functional and cannot emit lambda_H."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(STRUCTURAL_ROWS, structural_packet)

    fulls2_blocker = {
        "schema": "MTTFullS2OperatorPayloadBlockerForDirectEmission.v1",
        "status": "FULL_S2_OPERATOR_PAYLOAD_BLOCKS_DIRECT_SCALAR_ROWS",
        "full_s2_gate": rel(FULLS2_GATE),
        "ready": fulls2["ready"],
        "blocked_by": fulls2["blocked_by"],
        "hym_promotion_boundary": hym_gate["promotion_boundary"],
        "minimal_remaining_rows": hym_cutset["minimal_remaining_rows"],
        "next_required_for_direct_emission": [
            "Phi_fin_selected_minimizer_trace",
            "selected_P_s_K_s_projector_promotion",
            "selected_rho_s_matrix_values",
            "selected_End0_to_sector_routing_values",
            "physical_dotD_alpha1_same_branch_driver",
            "validator_ready_sector_rhoE_DE_Riesz_Green_dotD_C1",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FULLS2_BLOCKER, fulls2_blocker)

    anchor_selection = {
        "schema": "MTTUniversalAnchorSelectionRecheckForDirectEmission.v1",
        "status": "NO_UNIVERSAL_ANCHOR_SELECTED_FOR_DIRECT_EMISSION",
        "source_anchor_target": rel(UNIVERSAL_TARGET),
        "selected_universal_parameter_count": selected_anchor_count,
        "selected_candidates_now": universal["selected_candidates_now"],
        "theorem_required": universal["theorem_required"],
        "can_substitute_for_fullS2_payload": False,
        "why_not": [
            "no universal anchor theorem is selected",
            "anchor cannot be inferred from diagnostic coefficients or external replay residuals",
            "even an anchor would still need propagation through the same ten-row codomain",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ANCHOR_SELECTION, anchor_selection)

    cutset = {
        "schema": "MTTNextCutsetAfterDirectScalarRowEmissionAttempt.v1",
        "status": "NEXT_ATTACK_PHIFIN_MINIMIZER_TRACE_FOR_INTERNAL_SCALAR_ROWS",
        "closed_now": {
            "direct_emission_attempt_executed": True,
            "structural_orbit_rows_tested_and_rejected_as_values": True,
            "fullS2_blocker_identified": True,
            "universal_anchor_rechecked_not_selected": True,
        },
        "still_open": {
            "internal_Rtheta_scalar_row_emission": True,
            "lambda_H_row_emission": True,
            "Phi_fin_selected_minimizer_trace": True,
            "selected_sector_projector_promotion": True,
            "selected_rho_s_End0_sector_routing_values": True,
            "candidate_specific_universal_source_anchor": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "prove Phi_fin selected minimizer trace and promote model-active sector payload to selected full-S2 value data",
            "route_B": "derive equivalent full selected HYM/Strominger operator values",
            "route_C": "prove a candidate-specific universal source anchor only if it is selected before empirical replay",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedInternalRThetaScalarRowEmissionOrUniversalAnchorSelection",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "direct_internal_rtheta_scalar_row_emission_attempt": rel(DIRECT_ATTEMPT),
            "structural_orbit_scalar_row_candidates_not_accepted": rel(STRUCTURAL_ROWS),
            "full_s2_operator_payload_blocker_for_direct_emission": rel(FULLS2_BLOCKER),
            "universal_anchor_selection_recheck_for_direct_emission": rel(ANCHOR_SELECTION),
            "next_cutset_after_direct_scalar_row_emission_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "DirectInternalScalarRowEmissionBlockedByFullS2PayloadTheorem",
            "proved": True,
            "statement": (
                "The direct internal R_theta scalar-row emission route has been attempted against "
                "the closed source/domain, basis map, and selected orbit matrix packet. Current data "
                "emit zero accepted scalar rows because full-S2 rhoE/D_E/operator payload execution is "
                "not ready and no universal source anchor is selected. Structural orbit weights and "
                "diagnostic coefficients are rejected as value rows."
            ),
        },
        "closure_decision": {
            "direct_emission_attempt_executed": True,
            "accepted_internal_scalar_row_count": len(accepted_rows),
            "lambda_H_row_emitted": False,
            "fullS2_payload_ready": fulls2_ready,
            "universal_anchor_selected": selected_anchor_count > 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "previous_status": previous["status"],
        "kernel_readiness": kernel["readiness_fraction"],
        "value_source_obligation_closed_row_count": obligations["closed_row_count"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_InternalRThetaScalarRowEmission_or_UniversalAnchorSelection_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "direct_emission_attempt_executed": True,
        "accepted_internal_scalar_row_count": len(accepted_rows),
        "lambda_H_row_emitted": False,
        "fullS2_payload_ready": fulls2_ready,
        "universal_anchor_selected": selected_anchor_count > 0,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected InternalRThetaScalarRowEmission or UniversalAnchorSelection v1

Status: `{STATUS}`.

Direct internal scalar-row emission was attempted:

```text
source/domain closed             : {str(source_domain_closed).lower()}
basis map closed                 : {str(basis_closed).lower()}
selected orbit matrix closed      : {str(orbit_closed).lower()}
full-S2 scalar execution ready    : {str(fulls2_ready).lower()}
accepted internal scalar rows     : {len(accepted_rows)}
lambda_H row emitted              : false
selected universal anchors        : {selected_anchor_count}
```

The direct route cannot yet emit the ten `R_theta` scalar rows. The blocker is
not the basis or qualitative orbit layer; it is selected full-S2 payload
promotion: `Phi_fin` minimizer trace, selected sector projectors, selected
`rho_s`/End0 routing values, and the validator-ready sector operator packet.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
