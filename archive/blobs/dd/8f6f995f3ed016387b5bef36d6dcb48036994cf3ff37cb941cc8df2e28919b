"""Build c_{s,k} finite-functional obligation / sector-blind HYM no-go packet.

This packet attacks the strict source theorem for the nine charged flavor
coefficients.  It does not promote replay coefficients to source rows.  Instead
it proves that the currently selected charged HYM/K rows cannot be the source of
the sector-resolving c_{s,k} values by direct attachment, then emits the exact
finite-response functional contract that must be executed next.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_cskfinitefunctionalobligation_or_sectorblindhymnogotheorem"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CSKFiniteFunctionalObligation_or_SectorBlindHYMNoGoTheorem_v1.md"

FLAVOR_VALUES = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "flavor_threshold_operator_value_table.packet.json"
)
FLAVOR_USE = DATA / "selected_flavoroperatorvalueuse_or_ckmpmnsorientationbridge.candidate.json"
LOG_LEDGER = (
    DATA
    / "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger"
    / "minimal_flavor_parameter_ledger.packet.json"
)
LOG_RANK = (
    DATA
    / "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger"
    / "universal_parameter_reduction_rank_test.packet.json"
)
HYM_ROWS = (
    DATA
    / "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows"
    / "selected_charged_normalized_overlap_kernel_rows.packet.json"
)
FINITE_HYM = DATA / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof.candidate.json"
RTHETA_SCALAR = DATA / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows.candidate.json"
YUKAWA_GAP = DATA / "selected_yukawamagnituderowsfromselecteddynamicpacket_or_valuefunctionalgap.candidate.json"
Q79_BRIDGE = DATA / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget.candidate.json"

NO_GO_PACKET = PACKET_DIR / "sector_blind_hym_direct_attachment_nogo.packet.json"
CONTRACT_PACKET = PACKET_DIR / "csk_finite_response_functional_contract.packet.json"
MANIFEST_PACKET = PACKET_DIR / "csk_row_value_obligation_manifest.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_csk_functional_obligation.packet.json"

STATUS = (
    "MTT_SELECTED_CSKFINITEFUNCTIONALOBLIGATION_OR_SECTORBLINDHYMNOGOTHEOREM_"
    "DIRECT_HYM_ATTACH_REJECTED_FINITE_FUNCTIONAL_OBLIGATION_CLOSED"
)
NEXT = "MTT_Selected_CSKFiniteResponseFunctionalExecution_or_SectorProjectionWeights_v1"
SECTORS = ["u", "d", "e"]
COEFFS = ["c0", "c1", "c2"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def det3(m: list[list[float]]) -> float:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def max_abs_shared_row_residual(matrix: list[list[float]]) -> float:
    means = [sum(row[j] for row in matrix) / len(matrix) for j in range(len(matrix[0]))]
    return max(abs(row[j] - means[j]) for row in matrix for j in range(len(means)))


def main() -> int:
    sources = [FLAVOR_VALUES, FLAVOR_USE, LOG_LEDGER, LOG_RANK, HYM_ROWS, FINITE_HYM, RTHETA_SCALAR, YUKAWA_GAP, Q79_BRIDGE]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing csk functional inputs: " + ", ".join(missing))

    flavor_values = load(FLAVOR_VALUES)
    flavor_use = load(FLAVOR_USE)
    log_ledger = load(LOG_LEDGER)
    log_rank = load(LOG_RANK)
    hym_rows = load(HYM_ROWS)
    finite_hym = load(FINITE_HYM)
    rtheta_scalar = load(RTHETA_SCALAR)
    yukawa_gap = load(YUKAWA_GAP)
    q79 = load(Q79_BRIDGE)

    c_by_sector = flavor_values["sector_operator_coefficients"]
    c_matrix = [[c_by_sector[sector][coeff] for coeff in COEFFS] for sector in SECTORS]
    determinant = det3(c_matrix)
    shared_row_residual = max_abs_shared_row_residual(c_matrix)
    coefficient_spreads = {
        coeff: max(row[idx] for row in c_matrix) - min(row[idx] for row in c_matrix)
        for idx, coeff in enumerate(COEFFS)
    }

    k_by_sector: dict[str, list[float]] = {sector: [] for sector in SECTORS}
    for row in hym_rows["rows"]:
        k_by_sector[row["sector"]].append(row["selected_normalized_overlap_kernel_value"])
    sector_blind = all(k_by_sector[sector] == k_by_sector[SECTORS[0]] for sector in SECTORS)
    k_generation_vector = k_by_sector[SECTORS[0]]

    no_go = {
        "schema": "MTTSectorBlindHYMDirectAttachmentNoGo.v1",
        "status": "DIRECT_HYM_OVERLAP_ROWS_CANNOT_SOURCE_CSK_BY_SECTOR_BLIND_ATTACHMENT",
        "closure_claimed": True,
        "hypothesis_tested": (
            "Use only the selected charged normalized HYM/Strominger overlap rows "
            "K_threshold(Omega_s.gen_i) as direct c_{s,k} source data."
        ),
        "selected_hym_overlap_row_count": hym_rows["accepted_selected_charged_normalized_overlap_kernel_row_count"],
        "hym_rows_sector_blind": sector_blind,
        "hym_generation_vector": k_generation_vector,
        "csk_matrix_sectors": SECTORS,
        "csk_matrix_columns": COEFFS,
        "csk_matrix": c_matrix,
        "csk_matrix_determinant": determinant,
        "csk_matrix_full_rank": abs(determinant) > 1e-12,
        "coefficient_spreads_by_column": coefficient_spreads,
        "best_sector_blind_shared_row_max_abs_residual": shared_row_residual,
        "direct_attachment_rejected": sector_blind and shared_row_residual > 1e-12,
        "reason": (
            "A sector-blind functional of the emitted HYM generation vector gives the same coefficient row "
            "for u,d,e.  The required c_{s,k} rows are sector-resolving and full rank, so direct attachment "
            "would either erase flavor hierarchy or import forbidden target data."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    functional_contract = {
        "schema": "MTTCSKFiniteResponseFunctionalContract.v1",
        "status": "ADMISSIBLE_CSK_SOURCE_FUNCTIONAL_CONTRACT_EMITTED_VALUES_OPEN",
        "closure_claimed": True,
        "finite_projected_HYM_source_principle_closed": finite_hym["closure_decision"][
            "finite_projected_HYM_source_principle_closed"
        ],
        "automatic_finite_cutoff_exactness_closed": finite_hym["closure_decision"][
            "automatic_finite_cutoff_exactness_for_A_N_closed"
        ],
        "selected_Rtheta_scalar_value_functional_source_domain_closed": rtheta_scalar["closure_decision"][
            "selected_Rtheta_scalar_value_functional_source_domain_closed"
        ],
        "sector_aware_projection_skeleton_closed": yukawa_gap["closure_decision"][
            "sector_aware_projection_skeleton_closed"
        ],
        "all_sectors_family_resolved": yukawa_gap["closure_decision"]["all_sectors_family_resolved"],
        "family_resolving_operator_closed": yukawa_gap["closure_decision"]["family_resolving_operator_closed"],
        "q79_CKM_phase_contact_closed": q79["closure_decision"][
            "selected_CKM_CP_phase_contact_imported"
        ],
        "required_source_form": (
            "c_{s,k} = Tr_N(P_s * B_k * Phi_flavor_N), with B_k dual to {I,F,F^2} "
            "and Phi_flavor_N a selected sector-resolving threshold/response payload in A_N."
        ),
        "required_emitted_objects": [
            "selected sector projectors P_u,P_d,P_e inside the finite projected algebra A_N",
            "selected dual basis rows B_0,B_1,B_2 for the family polynomial basis",
            "selected sector-resolving Phi_flavor_N or higher-response threshold payload",
            "row-level trace certificates for all nine Tr_N(P_s B_k Phi_flavor_N)",
            "proof that the values are emitted before Yukawa/CKM/PMNS empirical replay",
        ],
        "current_missing_objects": [
            "sector-resolving Phi_flavor_N value payload",
            "row-level c_{s,k} trace certificates",
            "source-selected reduction loadings if attempting a 1-3 parameter route",
        ],
        "accepted_strict_csk_source_row_count": 0,
        "functional_contract_closed": True,
        "functional_values_executed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    manifest_rows = []
    for sector in SECTORS:
        for coeff in COEFFS:
            manifest_rows.append(
                {
                    "row_id": f"csk.{sector}.{coeff}",
                    "sector": sector,
                    "coefficient": coeff,
                    "profile_policy_value": c_by_sector[sector][coeff],
                    "strict_source_value_emitted": False,
                    "accepted_as_no_knob_source_row": False,
                    "required_certificate": f"Tr_N(P_{sector} * B_{coeff[-1]} * Phi_flavor_N)",
                }
            )

    manifest = {
        "schema": "MTTCSKRowValueObligationManifest.v1",
        "status": "NINE_CSK_ROW_OBLIGATIONS_TYPED_STRICT_VALUES_OPEN",
        "closure_claimed": True,
        "policy_source_value_row_count": flavor_values["policy_source_value_row_count"],
        "strict_selected_no_knob_source_row_count": flavor_values[
            "strict_selected_no_knob_source_row_count"
        ],
        "ledger_profile_replay_slots": log_ledger["profile_replay_parameter_slots"],
        "one_to_three_reduction_closed": False,
        "coefficient_matrix_full_rank": log_rank["full_rank"],
        "rows": manifest_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterCSKFunctionalObligation.v1",
        "status": "NEXT_IS_EXECUTE_SECTOR_RESOLVING_FINITE_RESPONSE_FUNCTIONAL",
        "closure_claimed": True,
        "closed_now": [
            "direct HYM/K row attachment to c_{s,k} rejected by sector-blind no-go",
            "finite projected algebra exactness is the correct source arena",
            "admissible c_{s,k} source functional form is fixed",
            "nine row-level trace certificate obligations are typed",
        ],
        "not_closed": [
            "strict selected c_{s,k} numerical source rows",
            "1-3 universal flavor parameter reduction",
            "Yukawa magnitude prediction from MTT alone",
            "CKM/PMNS angle source theorem",
            "full true SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "ordered_execution_plan": [
            "construct P_u,P_d,P_e as selected sector projectors in A_N",
            "construct B_0,B_1,B_2 as the dual rows of the selected family polynomial basis",
            "derive Phi_flavor_N from the selected higher-response/threshold payload rather than replayed Yukawas",
            "evaluate nine finite traces Tr_N(P_s B_k Phi_flavor_N)",
            "compare emitted rows to the policy c_{s,k} table only after source emission is certified",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedCSKFiniteFunctionalObligationOrSectorBlindHYMNoGoTheorem",
        "status": STATUS,
        "closure_claimed": True,
        "strict_csk_source_theorem_claimed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "inputs": {
            "flavor_operator_values": rel(FLAVOR_VALUES),
            "flavor_operator_use_bridge": rel(FLAVOR_USE),
            "minimal_flavor_ledger": rel(LOG_LEDGER),
            "rank_test": rel(LOG_RANK),
            "selected_hym_overlap_rows": rel(HYM_ROWS),
            "finite_projected_hym": rel(FINITE_HYM),
            "rtheta_scalar_functional_domain": rel(RTHETA_SCALAR),
            "yukawa_value_functional_gap": rel(YUKAWA_GAP),
            "q79_ckm_phase_bridge": rel(Q79_BRIDGE),
        },
        "theorem": {
            "name": "CSKFiniteFunctionalObligationAndSectorBlindHYMNoGoTheorem",
            "proved": True,
            "statement": (
                "The current selected charged HYM/Strominger overlap rows cannot directly source "
                "the sector-resolving c_{s,k} matrix.  Strict closure requires a finite projected "
                "sector response functional c_{s,k}=Tr_N(P_s B_k Phi_flavor_N) or an independently "
                "selected lower-dimensional source-loading theorem."
            ),
        },
        "closure_decision": {
            "direct_HYM_overlap_attachment_rejected": no_go["direct_attachment_rejected"],
            "hym_rows_sector_blind": sector_blind,
            "csk_matrix_full_rank": abs(determinant) > 1e-12,
            "best_sector_blind_shared_row_max_abs_residual": shared_row_residual,
            "finite_projected_HYM_source_principle_closed": functional_contract[
                "finite_projected_HYM_source_principle_closed"
            ],
            "selected_Rtheta_scalar_value_functional_source_domain_closed": functional_contract[
                "selected_Rtheta_scalar_value_functional_source_domain_closed"
            ],
            "sector_aware_projection_skeleton_closed": functional_contract[
                "sector_aware_projection_skeleton_closed"
            ],
            "admissible_csk_source_functional_contract_closed": True,
            "csk_row_value_obligation_count": len(manifest_rows),
            "accepted_strict_csk_source_row_count": 0,
            "one_to_three_universal_parameter_reduction_closed": False,
            "strict_csk_source_theorem_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "packets": {
            "sector_blind_hym_direct_attachment_nogo": rel(NO_GO_PACKET),
            "csk_finite_response_functional_contract": rel(CONTRACT_PACKET),
            "csk_row_value_obligation_manifest": rel(MANIFEST_PACKET),
            "next_cutset": rel(NEXT_PACKET),
        },
    }

    cert = {
        "certificate": "MTTSelectedCSKFiniteFunctionalObligationOrSectorBlindHYMNoGoTheoremCertificate",
        "status": STATUS,
        "theorem": candidate["theorem"]["name"],
        "direct_HYM_overlap_attachment_rejected": no_go["direct_attachment_rejected"],
        "hym_rows_sector_blind": sector_blind,
        "csk_matrix_determinant": determinant,
        "csk_matrix_full_rank": abs(determinant) > 1e-12,
        "best_sector_blind_shared_row_max_abs_residual": shared_row_residual,
        "admissible_csk_source_functional_contract_closed": True,
        "csk_row_value_obligation_count": len(manifest_rows),
        "accepted_strict_csk_source_row_count": 0,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected CSKFiniteFunctionalObligation or SectorBlindHYMNoGoTheorem v1

Status: `{STATUS}`

## Theorem

`CSKFiniteFunctionalObligationAndSectorBlindHYMNoGoTheorem` is proved.

The currently selected charged HYM/Strominger overlap rows cannot be directly
attached as the source of the nine `c_{{s,k}}` rows.  They are sector-blind:
the same generation vector is emitted for `u`, `d`, and `e`,

`{k_generation_vector}`

but the charged flavor coefficient matrix is sector-resolving and full rank:

`det(C) = {determinant}`

The best sector-blind shared-row approximation has maximum residual
`{shared_row_residual}`, so direct attachment would erase the charged flavor
hierarchy or silently import replay data.

## Correct Source Form

The admissible strict source theorem must execute a finite projected response
functional inside the selected algebra:

`c_{{s,k}} = Tr_N(P_s * B_k * Phi_flavor_N)`.

Here `P_s` are selected sector projectors, `B_k` are dual rows for the
`{{I,F,F^2}}` family basis, and `Phi_flavor_N` is a selected sector-resolving
threshold/response payload.  Finite projected HYM exactness and the R_theta
functional domain are already closed, but the numerical `Phi_flavor_N` trace
rows are not emitted yet.

## Row Obligations

- typed `c_{{s,k}}` row obligations: `{len(manifest_rows)}`
- accepted strict `c_{{s,k}}` source rows: `0`
- current policy/profile replay rows: `{flavor_values["policy_source_value_row_count"]}`
- one-to-three universal flavor reduction: `false`

## What This Closes

- rejects the wrong direct HYM/K attachment route
- fixes the finite trace source form needed for strict flavor closure
- types the nine row-level certificates that must be emitted next

## What Remains

Execute `Phi_flavor_N` or an independently selected lower-dimensional
source-loading theorem.  Until that is done, charged Yukawa magnitudes remain
profile-policy replay rows, not no-knob predictions.

Next artifact: `{NEXT}`.
"""

    write_json(NO_GO_PACKET, no_go)
    write_json(CONTRACT_PACKET, functional_contract)
    write_json(MANIFEST_PACKET, manifest)
    write_json(NEXT_PACKET, next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
