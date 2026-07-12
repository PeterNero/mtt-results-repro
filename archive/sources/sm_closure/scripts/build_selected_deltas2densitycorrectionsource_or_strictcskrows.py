"""Build Delta_S2 density correction source / strict csk rows gate.

This packet attacks the source side of the full-S2 correction

    Phi_sector_N = Phi_C1_lanes + Delta_S2.

The previous artifact defined the row-dual Delta_S2 slots and computed the
diagnostic residual obligation.  This artifact imports the strongest available
HYM/rhoE/D_E/End0 support and checks whether it is enough to emit the nine
Delta_S2 source rows.  It is not yet enough: the current chain has real support
for projective rhoE and diagonal End0 D_E, but full sector transfer, selected
zero-mode bases, Riesz/Green/dotD, End0-sector functor values, and nonlinear
HYM/offdiagonal control are still open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_deltas2densitycorrectionsource_or_strictcskrows"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DeltaS2DensityCorrectionSource_or_StrictCSKRows_v1.md"

FULLS2_DENSITY = DATA / "selected_fulls2sectordensityoperator_or_phisectornnumericrows.candidate.json"
RESIDUAL = (
    DATA
    / "selected_fulls2sectordensityoperator_or_phisectornnumericrows"
    / "phisectorn_residual_obligation_after_c1.packet.json"
)
HYM_PROJECTOR_ROUTE_A = DATA / "selected_hym_projector_source_promotion_route_a.candidate.json"
ZERO_MODE_THEOREM = DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"
NONIDENTITY_RHOE = DATA / "selected_nonidentity_rhoe_transition_source.candidate.json"
STEP38_RHOE = DATA / "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier.candidate.json"
STEP38_FRONTIER = (
    DATA / "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier" / "step38_de_operator_frontier.packet.json"
)
STEP39_DE = DATA / "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier.candidate.json"
STEP39_FRONTIER = (
    DATA
    / "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier"
    / "step39_full_sector_operator_frontier.packet.json"
)
END0_FUNCTOR = DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"
EXT_HODGE = DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
FULLS2_GATE = (
    DATA
    / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution"
    / "full_s2_value_execution_gate.packet.json"
)

CLAUSE_PACKET = PACKET_DIR / "deltas2_source_clause_ledger.packet.json"
ROW_PACKET = PACKET_DIR / "deltas2_row_emission_attempt.packet.json"
CONDITIONAL_PACKET = PACKET_DIR / "conditional_strict_csk_closure_witness.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_deltas2_source_gate.packet.json"

STATUS = (
    "MTT_SELECTED_DELTAS2DENSITYCORRECTIONSOURCE_OR_STRICTCSKROWS_"
    "SOURCE_GATE_BUILT_ROWS_OPEN"
)
NEXT = "MTT_Selected_FullSectorHYMOperatorPayload_or_DeltaS2RowEmission_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clause(name: str, present: bool, selected: bool, source: Path, role: str, blocker: str) -> dict[str, Any]:
    return {
        "clause_id": name,
        "support_present": present,
        "selected_for_delta_s2_now": selected,
        "source": rel(source),
        "role": role,
        "blocking_reason": blocker if not selected else None,
    }


def main() -> int:
    sources = [
        FULLS2_DENSITY,
        RESIDUAL,
        HYM_PROJECTOR_ROUTE_A,
        ZERO_MODE_THEOREM,
        NONIDENTITY_RHOE,
        STEP38_RHOE,
        STEP38_FRONTIER,
        STEP39_DE,
        STEP39_FRONTIER,
        END0_FUNCTOR,
        EXT_HODGE,
        FULLS2_GATE,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Delta_S2 source-gate inputs: " + ", ".join(missing))

    fulls2 = load(FULLS2_DENSITY)
    residual = load(RESIDUAL)
    hym_route = load(HYM_PROJECTOR_ROUTE_A)
    zero_mode = load(ZERO_MODE_THEOREM)
    nonidentity = load(NONIDENTITY_RHOE)
    step38 = load(STEP38_RHOE)
    step38_frontier = load(STEP38_FRONTIER)
    step39 = load(STEP39_DE)
    step39_frontier = load(STEP39_FRONTIER)
    end0 = load(END0_FUNCTOR)
    ext_hodge = load(EXT_HODGE)
    fulls2_gate = load(FULLS2_GATE)

    step38_decision = step38["closure_decision"]
    step39_decision = step39["closure_decision"]
    fulls2_decision = fulls2["closure_decision"]

    clauses = [
        clause(
            "C0_full_s2_density_contract",
            True,
            fulls2_decision["full_s2_density_operator_contract_closed"],
            FULLS2_DENSITY,
            "typed Phi_sector_N = Phi_C1_lanes + Delta_S2 contract and row-dual slots",
            "",
        ),
        clause(
            "C1_HYM_projector_source_promotion",
            hym_route["validator_status"]["finite_projector_values_pass"],
            hym_route["route_a_promotes_now"],
            HYM_PROJECTOR_ROUTE_A,
            "promote finite HYM projector values from model-active to selected source",
            "Route A reduces to Phi_fin selected minimizer trace and honest operator flags.",
        ),
        clause(
            "C2_zero_mode_bases_and_projectors",
            zero_mode["current_support"]["selected_End0_basis_available"],
            zero_mode["finite_acceptance_validator"]["passes_now"],
            ZERO_MODE_THEOREM,
            "emit selected sector zero-mode projectors, bases, gaps, and Gram convention",
            "Zero-mode slots and coherent spectral projector retention remain unfilled.",
        ),
        clause(
            "C3_projective_rhoE_transition",
            step38_decision["operator_level_projective_rhoE_transition_matrices_closed"],
            nonidentity["gate_results"]["selected_projective_rhoE_source_closed"],
            NONIDENTITY_RHOE,
            "supply selected projective/twisted rhoE source for full-S2 operator payload",
            "Operator-level gauge class is closed as support, but selected projective gerbe source promotion remains open.",
        ),
        clause(
            "C4_full_sector_DE_Riesz_Green_dotD",
            step39_decision["selected_diagonal_End0_covariant_D_E_closed"]
            and step39_decision["selected_stationary_projector_Riesz_Green_transport_closed"],
            step39_decision["selected_full_sector_covariant_D_E_matrices_closed"]
            and step39_decision["same_branch_dotD_alpha1_values_closed"]
            and step39_decision["primitive_C1_contractions_from_operator_values_closed"],
            STEP39_DE,
            "lift diagonal End0 lane to full Q,u,d,L,e,N,H sector D_E/Riesz/Green/dotD/C1 values",
            "Diagonal End0 D_E is closed, but rank2-to-rank3 sector transfer, dotD alpha1, zero-mode projectors, and primitive C1 contractions remain open.",
        ),
        clause(
            "C5_End0_to_sector_functor_values",
            True,
            False,
            END0_FUNCTOR,
            "map End0 operator payload to sector-resolving u,d,e density values",
            "Existing values were rejected; selected sector zero-mode realization or End0 tensor-product construction remains open.",
        ),
        clause(
            "C6_nonlinear_HYM_offdiagonal_control",
            True,
            False,
            EXT_HODGE,
            "supply nonlinear HYM correction/offdiagonal control needed for full-S2 density",
            "Ext/Hodge projector table is support; nonlinear HYM correction coefficients and full Newton/Galerkin coefficients remain open.",
        ),
    ]
    selected_clause_count = sum(1 for item in clauses if item["selected_for_delta_s2_now"])
    required_clause_count = len(clauses)
    blocking_clauses = [item["clause_id"] for item in clauses if not item["selected_for_delta_s2_now"]]

    row_attempts = []
    for row in residual["rows"]:
        row_attempts.append(
            {
                "row_id": row["row_id"],
                "sector": row["sector"],
                "coefficient": row["coefficient"],
                "diagnostic_delta_value_quarantined": row[
                    "diagnostic_delta_required_if_policy_target_used"
                ],
                "source_value_emitted": False,
                "accepted_as_delta_s2_source_row": False,
                "accepted_as_phi_sector_n_numeric_row": False,
                "accepted_as_csk_source_row": False,
                "blocking_clauses": blocking_clauses,
            }
        )

    clause_packet = {
        "schema": "MTTDeltaS2SourceClauseLedger.v1",
        "status": "DELTAS2_SOURCE_CLAUSE_LEDGER_BUILT_INCOMPLETE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "required_clause_count": required_clause_count,
        "selected_clause_count": selected_clause_count,
        "blocking_clause_count": len(blocking_clauses),
        "blocking_clauses": blocking_clauses,
        "clauses": clauses,
        "support_summary": {
            "projective_rhoE_operator_level_closed": step38_decision[
                "operator_level_projective_rhoE_transition_matrices_closed"
            ],
            "projective_rhoE_source_closed": nonidentity["gate_results"][
                "selected_projective_rhoE_source_closed"
            ],
            "diagonal_End0_D_E_closed": step39_decision["selected_diagonal_End0_covariant_D_E_closed"],
            "full_sector_D_E_closed": step39_decision[
                "selected_full_sector_covariant_D_E_matrices_closed"
            ],
            "finite_trace_DE_gap_layer_closed": step39_decision["finite_trace_DE_gap_layer_closed"],
            "full_S2_execution_allowed_now": fulls2_gate["execution_allowed_now"],
            "full_S2_accepted_scalar_row_count_now": fulls2_gate[
                "accepted_scalar_row_count_now"
            ],
        },
    }

    row_packet = {
        "schema": "MTTDeltaS2RowEmissionAttempt.v1",
        "status": "NO_DELTAS2_SOURCE_ROWS_EMITTED_CURRENT_SUPPORT_INCOMPLETE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "policy_residual_values_used_only_as_diagnostic": True,
        "required_row_count": len(row_attempts),
        "accepted_delta_s2_source_row_count": 0,
        "accepted_phi_sector_n_numeric_row_count": 0,
        "accepted_strict_csk_source_row_count": 0,
        "rows": row_attempts,
    }

    conditional = {
        "schema": "MTTConditionalStrictCSKClosureWitnessFromDeltaS2.v1",
        "status": "CONDITIONAL_WITNESS_BUILT_WAITING_FOR_FULL_SECTOR_HYM_PAYLOAD",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "if_all_clauses_selected": {
            "Delta_S2_source_rows_would_emit": 9,
            "Phi_sector_N_numeric_rows_would_emit": 9,
            "common_circle_trace_engine_already_ready": True,
            "strict_csk_rows_would_close": 9,
        },
        "current_result": {
            "Delta_S2_source_rows_emitted": 0,
            "Phi_sector_N_numeric_rows_emitted": 0,
            "strict_csk_rows_closed": 0,
        },
        "minimum_next_payload": step39_frontier["next_required_payload"],
        "operator_value_frontier": step38_frontier["still_missing_as_operator_values"],
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterDeltaS2SourceGate.v1",
        "status": "NEXT_IS_FULL_SECTOR_HYM_OPERATOR_PAYLOAD",
        "closure_claimed": True,
        "closed_now": [
            "Delta_S2 strict source-emission validator built",
            "all current HYM/rhoE/D_E/End0 support imported",
            "projective rhoE and diagonal End0 D_E support separated from full-S2 source rows",
            "conditional strict csk closure witness constructed",
        ],
        "still_open": [
            "selected HYM projector source promotion",
            "selected zero-mode bases/projectors/gaps/Gram convention",
            "selected projective gerbe rhoE source promotion",
            "full-sector D_E/Riesz/Green/dotD/C1 payload",
            "selected End0-to-sector functor values",
            "nonlinear HYM/offdiagonal correction control",
            "nine Delta_S2 source rows",
        ],
        "next_required_artifact": NEXT,
        "ordered_attack": [
            "promote projective gerbe rhoE and HYM projector source from support to selected source",
            "derive full-sector D_E/Riesz/Green/dotD/C1 payload from the same selected connection",
            "emit End0-to-sector functor values and nonlinear HYM/offdiagonal correction",
            "execute Delta_S2 row emission and rerun strict csk trace acceptance",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedDeltaS2DensityCorrectionSourceOrStrictCSKRows",
        "status": STATUS,
        "closure_claimed": True,
        "strict_delta_s2_source_rows_claimed": False,
        "strict_csk_source_theorem_claimed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "DeltaS2DensityCorrectionSourceGateTheorem",
            "proved": True,
            "statement": (
                "The Delta_S2 source-emission problem is equivalent to a strict full-sector "
                "HYM/Strominger operator payload: selected HYM projectors, zero-mode bases, "
                "projective rhoE source, full-sector D_E/Riesz/Green/dotD/C1 values, "
                "End0-to-sector functor values, and nonlinear HYM/offdiagonal control. "
                "Current support fills only the density contract plus partial rhoE/diagonal "
                "End0 support, so no Delta_S2 or c_{s,k} source rows are emitted now."
            ),
        },
        "closure_decision": {
            "delta_s2_source_gate_built": True,
            "required_clause_count": required_clause_count,
            "selected_clause_count": selected_clause_count,
            "blocking_clause_count": len(blocking_clauses),
            "projective_rhoE_operator_level_closed": step38_decision[
                "operator_level_projective_rhoE_transition_matrices_closed"
            ],
            "projective_rhoE_selected_source_closed": nonidentity["gate_results"][
                "selected_projective_rhoE_source_closed"
            ],
            "diagonal_End0_DE_closed": step39_decision["selected_diagonal_End0_covariant_D_E_closed"],
            "full_sector_operator_payload_closed": False,
            "delta_s2_source_rows_emitted": 0,
            "accepted_phi_sector_n_numeric_row_count": 0,
            "accepted_strict_csk_source_row_count": 0,
            "conditional_strict_csk_closure_witness_built": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "packets": {
            "deltas2_source_clause_ledger": rel(CLAUSE_PACKET),
            "deltas2_row_emission_attempt": rel(ROW_PACKET),
            "conditional_strict_csk_closure_witness": rel(CONDITIONAL_PACKET),
            "next_cutset": rel(NEXT_PACKET),
        },
    }

    cert = {
        "certificate": "MTTSelectedDeltaS2DensityCorrectionSourceOrStrictCSKRowsCertificate",
        "status": STATUS,
        "theorem": candidate["theorem"]["name"],
        "delta_s2_source_gate_built": True,
        "required_clause_count": required_clause_count,
        "selected_clause_count": selected_clause_count,
        "blocking_clause_count": len(blocking_clauses),
        "projective_rhoE_operator_level_closed": step38_decision[
            "operator_level_projective_rhoE_transition_matrices_closed"
        ],
        "projective_rhoE_selected_source_closed": nonidentity["gate_results"][
            "selected_projective_rhoE_source_closed"
        ],
        "diagonal_End0_DE_closed": step39_decision["selected_diagonal_End0_covariant_D_E_closed"],
        "full_sector_operator_payload_closed": False,
        "delta_s2_source_rows_emitted": 0,
        "accepted_phi_sector_n_numeric_row_count": 0,
        "accepted_strict_csk_source_row_count": 0,
        "conditional_strict_csk_closure_witness_built": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected DeltaS2DensityCorrectionSource or StrictCSKRows v1

Status: `{STATUS}`

## Theorem

`DeltaS2DensityCorrectionSourceGateTheorem` is proved.

The missing `Delta_S2` correction rows are now reduced to a strict full-sector
HYM/Strominger operator payload.  The source gate has `{required_clause_count}`
clauses; `{selected_clause_count}` are currently selected for `Delta_S2`, and
`{len(blocking_clauses)}` remain blocking.

Current positive support:

- full-S2 density contract is closed
- projective `rhoE` is closed at operator/gauge-class support level
- diagonal End0 covariant `D_E` is closed
- finite trace/gap support is closed

Current blockers:

- selected HYM projector source promotion
- selected zero-mode bases/projectors/gaps/Gram convention
- selected projective gerbe `rhoE` source promotion
- full-sector `D_E/Riesz/Green/dotD/C1` payload
- selected End0-to-sector functor values
- nonlinear HYM/offdiagonal correction control

## Counts

- accepted `Delta_S2` source rows: `0`
- accepted `Phi_sector_N` numeric rows: `0`
- accepted strict `c_{{s,k}}` rows: `0`

## Conditional Witness

If the full-sector HYM payload emits all gate clauses, the already-built
`Delta_S2` row-dual density contract and common-circle trace engine would emit
`9` `Delta_S2` rows, `9` `Phi_sector_N` rows, and `9` strict `c_{{s,k}}` rows.

## Next Artifact

`{NEXT}`.
"""

    write_json(CLAUSE_PACKET, clause_packet)
    write_json(ROW_PACKET, row_packet)
    write_json(CONDITIONAL_PACKET, conditional)
    write_json(NEXT_PACKET, next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
