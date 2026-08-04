"""Build R_theta first-pass coefficient values / selected source-row gate.

The previous artifact emitted an invertible first-pass MZ-to-Mt Jacobian.  This
builder packages those derivative blocks as a concrete R_theta^(1) coefficient
candidate and audits whether the rows can be promoted to selected threshold
functional source rows.  They cannot yet be promoted, because source ownership
and precision convention are still open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
COEFFICIENTS = PACKET_DIR / "firstpass_rtheta_coefficient_values.packet.json"
COMPOSED = PACKET_DIR / "firstpass_composed_bct_to_mt_response.packet.json"
PROMOTION = PACKET_DIR / "selected_rtheta_source_row_promotion_audit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rtheta_coefficient_values.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaCoefficientValues_or_SelectedThresholdFunctionalSourceRows_v1.md"

PREVIOUS = DATA / "selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill.candidate.json"
JACOBIAN = (
    DATA
    / "selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill"
    / "firstpass_rg_mz_to_mt_jacobian.packet.json"
)
CROSSBLOCK = (
    DATA
    / "selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill"
    / "firstpass_weak_bct_crossblock_covariance.packet.json"
)
ALGEBRAIC = (
    DATA
    / "selected_commonscalejacobian_or_rthetathresholdresponseexecution"
    / "bct_mz_mass_to_yukawa_v_jacobian.packet.json"
)
RTHETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
FUNCTIONAL_AUDIT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "current_repo_functional_instantiation_audit.packet.json"
)
SOURCE_AUDIT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)
THRESHOLD_ROWS_RECHECK = (
    DATA
    / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure"
    / "threshold_mass_scheme_source_rows_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETACOEFFICIENTVALUES_OR_SELECTEDTHRESHOLDFUNCTIONALSOURCEROWS_"
    "BUILT_FIRSTPASS_COEFFICIENTS_SELECTED_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_RThetaSourceOwner_or_PrecisionThresholdConventionTheorem_v1"


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
        raise FileNotFoundError("missing Rtheta coefficient sources: " + ", ".join(missing))


def nonzero_count(matrix: list[list[float]], eps: float = 0.0) -> int:
    return sum(1 for row in matrix for value in row if abs(value) > eps)


def max_abs(matrix: list[list[float]]) -> float:
    return max(abs(value) for row in matrix for value in row)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        JACOBIAN,
        CROSSBLOCK,
        ALGEBRAIC,
        RTHETA_CONTRACT,
        FUNCTIONAL_AUDIT,
        SOURCE_AUDIT,
        THRESHOLD_ROWS_RECHECK,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    jacobian = load(JACOBIAN)
    crossblock = load(CROSSBLOCK)
    algebraic = load(ALGEBRAIC)
    contract = load(RTHETA_CONTRACT)
    functional_audit = load(FUNCTIONAL_AUDIT)
    source_audit = load(SOURCE_AUDIT)
    threshold_recheck = load(THRESHOLD_ROWS_RECHECK)

    mt_rows = jacobian["input_coordinate_rows_native_Mt"]
    mz_rows = jacobian["output_coordinate_rows_MZ"]
    forward = jacobian["forward_Mt_to_MZ_jacobian_rows_output_by_cols_input"]
    inverse = jacobian["inverse_MZ_to_Mt_jacobian_rows_native_by_cols_output"]
    bct_domain = algebraic["jacobian_domain"]
    bct_codomain = algebraic["jacobian_codomain"]
    bct_matrix = algebraic["matrix_rows"]

    bct_mz_column = {
        "y_b(M_Z)": mz_rows.index("y_b_MZ_firstpass"),
        "y_c(M_Z)": mz_rows.index("y_c_MZ_firstpass"),
        "y_tau(M_Z)": mz_rows.index("y_tau_MZ_firstpass"),
    }
    composed = []
    for inverse_row in inverse:
        composed_row = []
        for domain_index, domain_id in enumerate(bct_domain):
            coefficient = 0.0
            for bct_row_index, bct_row_id in enumerate(bct_codomain):
                coefficient += inverse_row[bct_mz_column[bct_row_id]] * bct_matrix[bct_row_index][domain_index]
            composed_row.append(coefficient)
        composed.append(composed_row)

    coefficient_blocks = {
        "RG_Mt_to_MZ_forward": {
            "domain_rows": mt_rows,
            "codomain_rows": mz_rows,
            "matrix": forward,
            "coefficient_semantics": "d(output_MZ_firstpass)/d(input_Mt_native)",
            "accepted_as_firstpass_coefficient_values": True,
            "accepted_as_selected_Rtheta_source_rows": False,
        },
        "RG_MZ_to_Mt_inverse": {
            "domain_rows": mz_rows,
            "codomain_rows": mt_rows,
            "matrix": inverse,
            "coefficient_semantics": "d(input_Mt_native)/d(output_MZ_firstpass)",
            "accepted_as_firstpass_coefficient_values": True,
            "accepted_as_selected_Rtheta_source_rows": False,
        },
        "BCT_mass_to_MZ_yukawa": {
            "domain_rows": bct_domain,
            "codomain_rows": bct_codomain,
            "matrix": bct_matrix,
            "coefficient_semantics": "d(y_b,y_c,y_tau at M_Z)/d(m_b,m_c,m_tau,v)",
            "accepted_as_firstpass_coefficient_values": True,
            "accepted_as_selected_Rtheta_source_rows": False,
        },
        "composed_BCT_to_Mt_native": {
            "domain_rows": bct_domain,
            "codomain_rows": mt_rows,
            "matrix": composed,
            "coefficient_semantics": "d(input_Mt_native core)/d(m_b,m_c,m_tau,v) through inverse first-pass Rtheta",
            "accepted_as_firstpass_coefficient_values": True,
            "accepted_as_selected_Rtheta_source_rows": False,
        },
    }

    block_diagnostics = {
        name: {
            "shape": [len(block["matrix"]), len(block["matrix"][0])],
            "nonzero_entries": nonzero_count(block["matrix"]),
            "max_abs_coefficient": max_abs(block["matrix"]),
        }
        for name, block in coefficient_blocks.items()
    }

    coefficient_packet = {
        "schema": "MTTFirstPassRThetaCoefficientValues.v1",
        "status": "FIRSTPASS_RTHETA_COEFFICIENT_VALUES_EMITTED_SELECTED_SOURCE_ROWS_OPEN",
        "functional_symbol": "R_theta^(1)",
        "parent_functional_contract": rel(RTHETA_CONTRACT),
        "jacobian_source": rel(JACOBIAN),
        "algebraic_bct_jacobian_source": rel(ALGEBRAIC),
        "coefficient_blocks": coefficient_blocks,
        "block_diagnostics": block_diagnostics,
        "total_dense_coefficient_entries": sum(
            len(block["matrix"]) * len(block["matrix"][0]) for block in coefficient_blocks.values()
        ),
        "total_nonzero_coefficient_entries": sum(nonzero_count(block["matrix"]) for block in coefficient_blocks.values()),
        "baseline_replay_agrees_with_accepted_packet": jacobian["max_baseline_delta_vs_accepted_packet"] == 0.0,
        "inverse_residual_max_abs": jacobian["inverse_residual_max_abs"],
        "accepted_as_firstpass_Rtheta_coefficient_values": True,
        "accepted_as_selected_Rtheta_coefficient_values": False,
        "accepted_as_selected_threshold_response_functional": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(COEFFICIENTS, coefficient_packet)

    composed_packet = {
        "schema": "MTTFirstPassComposedBCTToMtResponse.v1",
        "status": "COMPOSED_BCT_TO_MT_RESPONSE_VALUES_EMITTED_SOURCE_PROMOTION_OPEN",
        "coefficient_source": rel(COEFFICIENTS),
        "crossblock_source": rel(CROSSBLOCK),
        "domain_rows": bct_domain,
        "codomain_rows": mt_rows,
        "matrix": composed,
        "row_interpretation": [
            "lambda_Mt response to BCT mass/v rows",
            "y_t_Mt response to BCT mass/v rows",
            "y_b_Mt response to BCT mass/v rows",
            "y_c_Mt response to BCT mass/v rows",
            "y_tau_Mt response to BCT mass/v rows",
        ],
        "inserted_crossblock_entries_imported": crossblock["inserted_cross_block_entries"],
        "inserted_crossblock_entry_count": crossblock["inserted_entry_count"],
        "accepted_as_firstpass_response_values": True,
        "accepted_as_full_profile_likelihood": False,
        "accepted_as_selected_threshold_response_covariance": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(COMPOSED, composed_packet)

    promotion_blockers = [
        {
            "id": "selected_dynamic_operator_source_owner",
            "closed": False,
            "evidence": functional_audit["requirements"][0]["missing_for_acceptance"],
        },
        {
            "id": "same_branch_scale_scheme_loop_convention",
            "closed": False,
            "evidence": functional_audit["requirements"][1]["missing_for_acceptance"],
        },
        {
            "id": "threshold_matching_source_rows",
            "closed": False,
            "evidence": functional_audit["requirements"][2]["missing_for_acceptance"],
        },
        {
            "id": "mass_scheme_conversion_source_rows",
            "closed": False,
            "evidence": functional_audit["requirements"][3]["missing_for_acceptance"],
        },
        {
            "id": "full_profile_likelihood_or_accepted_diagonal_theorem",
            "closed": False,
            "evidence": functional_audit["requirements"][6]["missing_for_acceptance"],
        },
    ]
    promotion_packet = {
        "schema": "MTTSelectedRThetaSourceRowPromotionAudit.v1",
        "status": "FIRSTPASS_COEFFICIENTS_AUDITED_NONE_PROMOTED_TO_SELECTED_SOURCE_ROWS",
        "coefficient_source": rel(COEFFICIENTS),
        "current_functional_instantiation_audit": rel(FUNCTIONAL_AUDIT),
        "accepted_threshold_mass_scheme_source_row_audit": rel(SOURCE_AUDIT),
        "threshold_rows_recheck": rel(THRESHOLD_ROWS_RECHECK),
        "firstpass_coefficients_present": True,
        "firstpass_coefficient_blocks_present": list(coefficient_blocks),
        "accepted_source_rows_present": source_audit["accepted_source_rows_present"],
        "accepted_threshold_matching_source_rows": source_audit["accepted_threshold_matching_source_rows"],
        "accepted_mass_scheme_conversion_source_rows": source_audit["accepted_mass_scheme_conversion_source_rows"],
        "promotion_blockers": promotion_blockers,
        "promoted_selected_Rtheta_source_row_count": 0,
        "selected_Rtheta_source_rows_closed": False,
        "selected_Rtheta_coefficient_values_closed": False,
        "selected_threshold_response_functional_closed": False,
        "firstpass_Rtheta_coefficient_values_closed": True,
        "why_firstpass_values_matter": [
            "they give a reproducible target for any future selected R_theta source theorem",
            "they eliminate the previous purely symbolic coefficient-value gap at the first-pass tier",
            "they expose exactly which scale/scheme/source rows must be promoted or replaced",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION, promotion_packet)

    cutset = {
        "schema": "MTTNextCutsetAfterRThetaCoefficientValues.v1",
        "status": "NEXT_ATTACK_RTHETA_SOURCE_OWNER_OR_PRECISION_THRESHOLD_CONVENTION",
        "closed_now": {
            "firstpass_Rtheta_coefficient_values": True,
            "firstpass_composed_BCT_to_Mt_response": True,
            "selected_Rtheta_source_row_promotion_audit": True,
        },
        "still_open": {
            "selected_dynamic_operator_source_owner": True,
            "same_branch_scale_scheme_loop_convention": True,
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "selected_Rtheta_coefficient_values": True,
            "selected_threshold_response_functional": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "prove a source-owner theorem that promotes the first-pass coefficients to selected R_theta rows",
            "route_B": "replace the first-pass rows with a selected precision threshold convention from the same branch",
            "route_C": "prove an accepted diagonal/first-pass limitation theorem if the full profile is intentionally deferred",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaCoefficientValuesOrSelectedThresholdFunctionalSourceRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "firstpass_rtheta_coefficient_values": rel(COEFFICIENTS),
            "firstpass_composed_bct_to_mt_response": rel(COMPOSED),
            "selected_rtheta_source_row_promotion_audit": rel(PROMOTION),
            "next_cutset_after_rtheta_coefficient_values": rel(CUTSET),
        },
        "theorem": {
            "name": "FirstPassRThetaCoefficientValueTheorem",
            "proved": True,
            "statement": (
                "The already executed first-pass RG Jacobian and exact BCT mass-to-yukawa map determine a finite "
                "R_theta^(1) coefficient packet: forward Mt-to-MZ coefficients, inverse MZ-to-Mt coefficients, "
                "BCT algebraic coefficients, and the composed BCT-to-Mt response. These close the coefficient-value "
                "gap at the first-pass replay tier, but the rows are not selected threshold functional source rows "
                "until source ownership, precision convention, threshold matching, and mass-scheme source rows are proved."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "firstpass_Rtheta_coefficient_values_closed": True,
            "firstpass_composed_BCT_to_Mt_response_closed": True,
            "selected_Rtheta_coefficient_values_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "selected_threshold_response_functional_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RThetaCoefficientValues_or_SelectedThresholdFunctionalSourceRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "firstpass_Rtheta_coefficient_values_closed": True,
        "firstpass_composed_BCT_to_Mt_response_closed": True,
        "selected_Rtheta_coefficient_values_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "selected_threshold_response_functional_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaCoefficientValues or SelectedThresholdFunctionalSourceRows v1

Status: `{STATUS}`.

This artifact emits a concrete first-pass `R_theta^(1)` coefficient packet from
the already executed RG Jacobian and the exact BCT mass-to-yukawa map.

```text
coefficient blocks emitted              : {len(coefficient_blocks)}
dense coefficient entries               : {coefficient_packet["total_dense_coefficient_entries"]}
nonzero coefficient entries             : {coefficient_packet["total_nonzero_coefficient_entries"]}
first-pass R_theta coefficients closed  : true
selected R_theta source rows closed     : false
selected threshold functional closed    : false
```

The rows matter because they are now finite replay objects, not empty symbolic
slots.  They still cannot be used as final selected source rows until source
ownership, precision convention, threshold matching, and mass-scheme source
rows are supplied.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
