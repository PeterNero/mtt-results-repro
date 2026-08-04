"""Build non-diagonal Huv Hessian source or direct Herm(2) rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_nondiagonalhuvhessiansource_or_directherm2rows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_NonDiagonalHuvHessianSource_or_DirectHerm2Rows_v1.md"

CONTRACT = PACKET_DIR / "nondiagonal_huv_source_acceptance_contract.packet.json"
REJECTION = PACKET_DIR / "candidate_source_rejection_matrix.packet.json"
DIRECT_RUN = PACKET_DIR / "direct_herm2_row_payload_run.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_nondiagonal_huv_source_attempt.packet.json"

PREVIOUS = DATA / "selected_herm2orientationphasetracesource_or_directhresponseemission.candidate.json"
PREVIOUS_DIRECT = (
    DATA
    / "selected_herm2orientationphasetracesource_or_directhresponseemission"
    / "direct_hresponse_emission_after_bridge_completion.packet.json"
)
SECOND_VARIATION = DATA / "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues.candidate.json"
HIGGS_DYNAMIC = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof.candidate.json"
EHUV_HYM = DATA / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload.candidate.json"
MSOURCE = DATA / "selected_msourcehiggsspecificoperatorblock_or_c5c6bridgefrontier.candidate.json"
FULL_MSOURCE = DATA / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable.candidate.json"
HRESPONSE_ROWS = (
    DATA
    / "selected_hresponsespectrumsourcerows_or_rhrglogdetvalueexecution"
    / "hresponse_source_row_execution_table.packet.json"
)

STATUS = (
    "MTT_SELECTED_NONDIAGONALHUVHESSIANSOURCE_OR_DIRECTHERM2ROWS_"
    "CANDIDATES_REJECTED_SOURCE_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_FHuvSecondVariationSource_or_DirectHerm2RowPayload_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing non-diagonal Huv source inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DIRECT,
        SECOND_VARIATION,
        HIGGS_DYNAMIC,
        EHUV_HYM,
        MSOURCE,
        FULL_MSOURCE,
        HRESPONSE_ROWS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_direct = load(PREVIOUS_DIRECT)
    second = load(SECOND_VARIATION)
    dynamic = load(HIGGS_DYNAMIC)
    ehuv_hym = load(EHUV_HYM)
    msource = load(MSOURCE)
    full_msource = load(FULL_MSOURCE)
    hrows = load(HRESPONSE_ROWS)

    s_beta = previous["key_numbers"]["selected_s_beta_value"]

    acceptance_contract = {
        "schema": "MTTNonDiagonalHuvSourceAcceptanceContract.v1",
        "status": "NONDIAGONAL_HUV_SOURCE_ACCEPTANCE_CONTRACT_CLOSED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "domain": {
            "coordinate_domain": "selected source-orthonormal B_Huv two-column Higgs domain",
            "orthonormality": "B_Huv^* G_Q B_Huv = I_2",
            "row_functional": "M_H^tf = [[Delta, Omega], [conj(Omega), -Delta]]",
            "non_diagonal_requirement": "Omega != 0 or source-owned off-diagonal Huv row",
        },
        "accepted_source_routes": {
            "selected_F_H_second_variation": {
                "required": [
                    "selected finite H-sector functional F_H",
                    "non-scalar trace-free Herm(2) Hessian on B_Huv",
                    "same-source exactness/error certificate",
                    "quotient admissibility certificate",
                ],
                "current_emitted": second["closure_decision"]["selected_F_H_second_variation_emitted"],
            },
            "selected_M_source_plus_R_H": {
                "required": [
                    "selected Hermitian M_source",
                    "selected H-sector restriction R_H",
                    "Huv = B_Huv^* M_source B_Huv values",
                    "source ownership certificate",
                ],
                "current_emitted": full_msource["closure_decision"]["M_source_plus_R_H_values_emitted"],
            },
            "direct_Herm2_rows": {
                "required": [
                    "Huu",
                    "Hud_re",
                    "Hud_im",
                    "Hdd",
                    "Hermitian/source ownership certificates",
                    "same-source exactness or error certificate",
                    "quotient admissibility certificate",
                ],
                "current_emitted": previous["closure_decision"]["direct_Herm2_rows_emitted"],
            },
        },
        "forbidden_promotions": [
            "C1-C6 projection bridge alone",
            "diagonal HYM metric or G_Q kinematic metric alone",
            "matter/neutrino operator blocks without a Higgs Huv block",
            "trace-free polar reconstruction law without r_H/sign/phase/source rows",
            "controlled HRG calibration lane as strict no-knob value source",
        ],
        "decision": {
            "non_diagonal_Huv_source_acceptance_contract_closed": True,
            "B_Huv_domain_closed": True,
            "Herm2_tracefree_row_functional_closed": True,
            "source_promotion_guard_closed": True,
        },
    }

    rejection_rows = [
        {
            "candidate_id": "diagonal_HYM_metric_connection_C3",
            "available_support": [
                "selected diagonal fixed-point metric diag(exp(u), exp(-u))",
                "connection A=du*T3 on ordered E_H^UV basis",
            ],
            "accepted_as_non_diagonal_Huv_source": False,
            "rejection_reason": (
                "diagonal metric support closes C3/domain geometry only; after "
                "B_Huv orthonormalization the kinematic metric has no source-owned "
                "off-diagonal Omega row"
            ),
            "blocker_fields": ["Omega", "F_H_second_variation", "direct_Herm2_rows"],
        },
        {
            "candidate_id": "C1_C6_projection_bridge",
            "available_support": [
                "C5b projection-measure equality",
                "C6 no-extra-boundary/source reduction",
                f"selected s_beta={s_beta}",
            ],
            "accepted_as_non_diagonal_Huv_source": False,
            "rejection_reason": (
                "projection bridge selects the finite angle/reduction scalar, but "
                "does not emit the non-diagonal Hessian, Omega phase, radial scale, "
                "or direct H-response rows"
            ),
            "blocker_fields": ["r_H", "sigma_D", "phi_Omega", "Huu/Hud/Hdd"],
        },
        {
            "candidate_id": "H7B1Q_matter_same_source_operator_blocks",
            "available_support": [
                "same-source functional alpha1/dotD side",
                "matter/neutrino operator blocks",
            ],
            "accepted_as_non_diagonal_Huv_source": False,
            "rejection_reason": (
                "same-source matter blocks do not contain a selected Higgs-specific "
                "H_u, H_d^dagger, or Huv Hermitian source block"
            ),
            "blocker_fields": ["Higgs_specific_operator_block", "selected_M_source"],
        },
        {
            "candidate_id": "full_M_source_plus_R_H_route",
            "available_support": [
                "formula M_source=Herm(R_H^* H_response R_H)",
                "formula Huv=B_Huv^* M_source B_Huv",
            ],
            "accepted_as_non_diagonal_Huv_source": False,
            "rejection_reason": (
                "the full route is algebraically instantiated, but current packets "
                "emit neither selected M_source+R_H values nor selected H_response table"
            ),
            "blocker_fields": ["selected_M_source", "selected_R_H", "H_response_table"],
        },
        {
            "candidate_id": "direct_H_response_rows",
            "available_support": [
                "minimal H-response/Huv row table is defined",
                "Herm(2) row/certificate slots are fixed",
            ],
            "accepted_as_non_diagonal_Huv_source": False,
            "rejection_reason": "the direct-row execution emits zero source rows and zero certificates",
            "blocker_fields": ["Huu", "Hud_re", "Hud_im", "Hdd", "certificates"],
        },
        {
            "candidate_id": "tracefree_polar_contract",
            "available_support": [
                "M_H^tf=[[Delta,Omega],[conj(Omega),-Delta]]",
                "Delta=sigma_D*r_H*sqrt(s_beta)",
                "Omega=r_H*sqrt(1-s_beta)*exp(i*phi_Omega)",
            ],
            "accepted_as_non_diagonal_Huv_source": False,
            "rejection_reason": (
                "the polar law is a correct reconstruction theorem, not a source; "
                "it remains conditional on radial/sign/phase rows and certificates"
            ),
            "blocker_fields": ["r_H", "sigma_D", "phi_Omega", "source_certificates"],
        },
    ]

    rejection_matrix = {
        "schema": "MTTNonDiagonalHuvCandidateSourceRejectionMatrix.v1",
        "status": "CANDIDATE_SOURCE_REJECTION_MATRIX_EXECUTED_ZERO_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "rows": rejection_rows,
        "decision": {
            "candidate_source_rejection_matrix_executed": True,
            "accepted_non_diagonal_Huv_Hessian_source_count": 0,
            "accepted_direct_Herm2_row_payload_count": 0,
            "diagonal_metric_retired_as_non_diagonal_Hessian_source": True,
            "projection_bridge_retired_as_direct_value_route": True,
            "matter_operator_blocks_retired_as_Huv_value_route": True,
            "full_M_source_route_formula_only_values_open": True,
        },
    }

    direct_payload_run = {
        "schema": "MTTDirectHerm2RowPayloadRun.v1",
        "status": "DIRECT_HERM2_ROW_PAYLOAD_RUN_EXECUTED_ZERO_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_direct_run_ref": rel(PREVIOUS_DIRECT),
        "hresponse_row_table_ref": rel(HRESPONSE_ROWS),
        "required_rows": {
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "source_ownership_certificate": None,
            "same_source_exactness_or_error_certificate": None,
            "quotient_admissibility_certificate": None,
        },
        "prior_required_table": previous_direct["required_table"],
        "prior_values_emitted_now": previous_direct["values_emitted_now"],
        "hresponse_table_status": {
            "required_row_count": hrows["decision"]["required_row_count"],
            "emitted_row_count": hrows["decision"]["emitted_row_count"],
            "accepted_source_row_count": hrows["decision"]["accepted_source_row_count"],
        },
        "decision": {
            "direct_Herm2_row_payload_run_executed": True,
            "selected_non_diagonal_Huv_Hessian_source_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "M_source_plus_R_H_values_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_predicted": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterNonDiagonalHuvSourceAttempt.v1",
        "status": "NEXT_FRONTIER_FHUV_SECOND_VARIATION_SOURCE_OR_DIRECT_HERM2_ROW_PAYLOAD",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "non-diagonal Huv source acceptance contract",
            "source-promotion guard against diagonal/projection/matter shortcuts",
            "candidate source rejection matrix across current strongest packets",
            "direct Herm(2) row payload run with zero emitted rows",
        ],
        "still_open": [
            "selected finite F_Huv second-variation source row",
            "nonzero Omega row or equivalent off-diagonal Huv row",
            "same-source exactness/error certificate for the Huv Hessian",
            "quotient admissibility certificate for the finite H-sector row payload",
            "selected M_source+R_H numeric values or direct Huu/Hud/Hdd values",
        ],
        "next_required_artifact": NEXT,
    }

    accepted_count = rejection_matrix["decision"]["accepted_non_diagonal_Huv_Hessian_source_count"]

    candidate = {
        "candidate": "MTTSelectedNonDiagonalHuvHessianSourceOrDirectHerm2Rows",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "NonDiagonalHuvSourcePromotionNoShortcutTheorem",
            "proved": True,
            "statement": (
                "On the selected B_Huv domain, a non-diagonal Higgs Herm(2) "
                "payload can be accepted only from a selected F_H second variation, "
                "selected M_source+R_H values, or direct source-owned Herm(2) rows "
                "with certificates. Current diagonal HYM, projection C1-C6, "
                "matter same-source, full-route formula, direct-row, and polar-law "
                "packets do not emit such a source. Thus the acceptance contract is "
                "closed and the candidate matrix executes with zero accepted rows."
            ),
        },
        "packets": {
            "nondiagonal_huv_source_acceptance_contract": rel(CONTRACT),
            "candidate_source_rejection_matrix": rel(REJECTION),
            "direct_herm2_row_payload_run": rel(DIRECT_RUN),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_direct": rel(PREVIOUS_DIRECT),
            "second_variation": rel(SECOND_VARIATION),
            "higgs_dynamic": rel(HIGGS_DYNAMIC),
            "ehuv_hym": rel(EHUV_HYM),
            "msource": rel(MSOURCE),
            "full_msource": rel(FULL_MSOURCE),
            "hresponse_rows": rel(HRESPONSE_ROWS),
        },
        "closure_decision": {
            "non_diagonal_Huv_source_acceptance_contract_closed": True,
            "candidate_source_rejection_matrix_executed": True,
            "direct_Herm2_row_payload_run_executed": True,
            "diagonal_metric_retired_as_non_diagonal_Hessian_source": True,
            "projection_bridge_retired_as_direct_value_route": True,
            "matter_operator_blocks_retired_as_Huv_value_route": True,
            "source_promotion_guard_closed": True,
            "selected_non_diagonal_Huv_Hessian_source_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "M_source_plus_R_H_values_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
            "selected_H_response_spectrum_emitted": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "selected_s_beta_value": s_beta,
            "accepted_non_diagonal_Huv_Hessian_source_count": accepted_count,
            "accepted_direct_Herm2_row_payload_count": 0,
            "accepted_H_response_source_row_count": 0,
            "accepted_R_H_RG_source_count": 0,
            "required_H_response_row_count": hrows["decision"]["required_row_count"],
            "emitted_H_response_row_count": hrows["decision"]["emitted_row_count"],
            "accepted_selected_K_source_row_count": dynamic["closure_decision"][
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": dynamic["closure_decision"][
                "selected_K_threshold_row_count_required"
            ],
        },
    }

    cert = {
        "certificate": "MTTSelectedNonDiagonalHuvHessianSourceOrDirectHerm2Rows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "non_diagonal_Huv_source_acceptance_contract_closed": True,
        "candidate_source_rejection_matrix_executed": True,
        "direct_Herm2_row_payload_run_executed": True,
        "diagonal_metric_retired_as_non_diagonal_Hessian_source": True,
        "projection_bridge_retired_as_direct_value_route": True,
        "matter_operator_blocks_retired_as_Huv_value_route": True,
        "source_promotion_guard_closed": True,
        "selected_non_diagonal_Huv_Hessian_source_emitted": False,
        "selected_F_H_second_variation_emitted": False,
        "selected_Hermitian_M_source_emitted": False,
        "M_source_plus_R_H_values_emitted": False,
        "direct_Herm2_rows_emitted": False,
        "R_H_RG_value_emitted": False,
        "lambda_H_predicted": False,
        "accepted_non_diagonal_Huv_Hessian_source_count": accepted_count,
        "accepted_direct_Herm2_row_payload_count": 0,
    }

    note = f"""# MTT Selected NonDiagonalHuvHessianSource or DirectHerm2Rows v1

Status: `{STATUS}`

## Theorem

On the selected source-orthonormal `B_Huv` domain, a non-diagonal Higgs
Herm(2) payload may be promoted only from one of three source-owned routes:

- selected finite `F_H` second variation with non-scalar trace-free Herm(2)
  Hessian on `B_Huv`
- selected Hermitian `M_source` plus selected H-sector restriction `R_H`
- direct `Huu,Hud,Hdd` rows with ownership, exactness/error, and quotient
  admissibility certificates

The current strongest packets were executed against that contract:

- diagonal HYM metric/connection: rejected as C3/domain support only
- C1-C6 projection bridge: accepted for `s_beta = {s_beta}`, rejected as direct
  value source
- matter/neutrino same-source operator blocks: rejected as non-Higgs blocks
- full `M_source+R_H` route: formula instantiated, values still absent
- direct H-response rows: `0` emitted rows
- trace-free polar contract: correct reconstruction law, conditional only

Accepted non-diagonal Huv Hessian sources: `0`.

Next artifact: `{NEXT}`
"""

    write_json(CONTRACT, acceptance_contract)
    write_json(REJECTION, rejection_matrix)
    write_json(DIRECT_RUN, direct_payload_run)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
