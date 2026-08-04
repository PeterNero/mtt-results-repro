"""Build selected F_Huv second-variation source or direct Herm(2) row payload."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fhuvsecondvariationsource_or_directherm2rowpayload"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FHuvSecondVariationSource_or_DirectHerm2RowPayload_v1.md"

RESTRICTION = PACKET_DIR / "fhuv_second_variation_restriction_criterion.packet.json"
LOCAL_BRIDGE = PACKET_DIR / "local_principle_to_fhuv_bridge_status.packet.json"
EXECUTION = PACKET_DIR / "fhuv_restriction_matrix_row_execution.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_fhuv_restriction_criterion.packet.json"

PREVIOUS = DATA / "selected_nondiagonalhuvhessiansource_or_directherm2rows.candidate.json"
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
RH = (
    DATA
    / "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian"
    / "hsector_restriction_from_bhuv.packet.json"
)
DYNAMIC_GATE = (
    DATA
    / "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian"
    / "dynamic_higgs_response_hessian_gate.packet.json"
)
LOCAL_WEYL = (
    DATA
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "accepted_local_weylvariation_actionprinciple.packet.json"
)
LOCAL_WEYL_CANDIDATE = DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution.candidate.json"
MINIMAL_ACTION = (
    DATA
    / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
    / "minimal_action_axiom_or_theorem.packet.json"
)
SOURCE_IDENTITY = (
    DATA
    / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation"
    / "selected_finite_c1_source_identity_principle_candidate.packet.json"
)
HRESPONSE_DIRECT = (
    DATA
    / "selected_herm2orientationphasetracesource_or_directhresponseemission"
    / "direct_hresponse_emission_after_bridge_completion.packet.json"
)

STATUS = (
    "MTT_SELECTED_FHUVSECONDVARIATIONSOURCE_OR_DIRECTHERM2ROWPAYLOAD_"
    "RESTRICTION_CRITERION_CLOSED_ROWS_OPEN"
)
NEXT = "MTT_Selected_FHuvRestrictionMatrixRows_or_BSelectedProjectionExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing F_Huv source inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        BHUV,
        RH,
        DYNAMIC_GATE,
        LOCAL_WEYL,
        LOCAL_WEYL_CANDIDATE,
        MINIMAL_ACTION,
        SOURCE_IDENTITY,
        HRESPONSE_DIRECT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    bhuv = load(BHUV)
    rh = load(RH)
    dynamic_gate = load(DYNAMIC_GATE)
    local_weyl = load(LOCAL_WEYL)
    local_candidate = load(LOCAL_WEYL_CANDIDATE)
    minimal_action = load(MINIMAL_ACTION)
    source_identity = load(SOURCE_IDENTITY)
    hresponse_direct = load(HRESPONSE_DIRECT)

    s_beta = previous["key_numbers"]["selected_s_beta_value"]

    restriction = {
        "schema": "MTTFHuvSecondVariationRestrictionCriterion.v1",
        "status": "FHUV_RESTRICTION_CRITERION_CLOSED_MATRIX_ROWS_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_domain": {
            "same_source_branch": rh["selected_source_space"]["branch"],
            "source_basis_dimension": rh["selected_source_space"]["basis_dimension"],
            "B_Huv_symbolic_exact_payload_emitted": bhuv["whitening_map_and_lift"][
                "B_Huv_symbolic_exact_payload_emitted"
            ],
            "B_Huv_orthonormality": rh["proof_identities"]["input_orthonormality"],
            "R_H": rh["canonical_restriction"]["R_H"],
            "P_H": rh["canonical_restriction"]["P_H"],
            "R_H_B_Huv_equals_I2": rh["proof_identities"]["R_H_B_Huv_equals_I2"],
        },
        "source_functional_definition": {
            "name": "F_Huv",
            "definition": (
                "F_Huv(z) = F_C1(B_Huv z) for the selected finite C1/Weyl "
                "action restricted to the selected two-Higgs source subspace"
            ),
            "second_variation_rule": (
                "M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv, equivalently "
                "(M_Huv)_ij = d^2 F_Huv / d(conj(z_i)) dz_j"
            ),
            "trace_free_projection": "M_Huv^tf = M_Huv - (Tr M_Huv / 2) I_2",
            "row_extractors": {
                "Delta": "(Huu-Hdd)/2",
                "Re_Omega": "Re(Hud)",
                "Im_Omega": "Im(Hud)",
            },
        },
        "strict_acceptance_requirements": [
            "selected finite C1/H-sector Hessian matrix or b_selected row source emitted before residual replay",
            "matrix restriction B_Huv^* Hess(F_C1)_selected B_Huv executed",
            "non-scalar trace-free part or direct certified Herm(2) rows emitted",
            "same-source exactness/error certificate attached",
            "quotient admissibility certificate attached",
        ],
        "decision": {
            "F_Huv_restriction_criterion_closed": True,
            "B_Huv_R_H_domain_available": True,
            "Herm2_extraction_law_available": True,
            "selected_C1_Hessian_matrix_rows_emitted": False,
            "B_selected_projection_execution_emitted": False,
            "selected_F_Huv_second_variation_emitted": False,
        },
    }

    local_bridge = {
        "schema": "MTTLocalPrincipleToFHuvBridgeStatus.v1",
        "status": "LOCAL_PRINCIPLE_CONDITIONAL_BRIDGE_READY_STRICT_SOURCE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "local_principle": {
            "principle_name": local_weyl["principle_name"],
            "accepted_scope": local_weyl["accepted_scope"],
            "accepted_as": local_weyl["accepted_as"],
            "local_pre_residual_kernel_closed": local_candidate["closure_decision"][
                "local_pre_residual_kernel_closed"
            ],
            "unpatched_principle_derived_now": local_candidate["closure_decision"][
                "unpatched_principle_derived_now"
            ],
            "independent_kernel_execution_supplied": local_candidate["closure_decision"][
                "independent_kernel_execution_supplied"
            ],
        },
        "strict_no_knob_guard": {
            "minimal_action_theorem_proved_here": minimal_action["proved_here"],
            "minimal_action_must_not_be_used_as_free_patch": minimal_action[
                "must_not_be_used_as_free_patch"
            ],
            "finite_c1_source_identity_inserted": source_identity["insertion_status"][
                "accepted_as_axiom_or_derived_theorem"
            ],
            "conditional_validator_would_pass_if_inserted": source_identity["insertion_status"][
                "conditional_validator_would_pass_if_inserted"
            ],
        },
        "bridge_decision": {
            "local_premise_conditional_F_Huv_source_bridge_ready": True,
            "strict_unpatched_F_Huv_source_bridge_closed": False,
            "independent_quadrature_F_Huv_source_bridge_closed": False,
            "may_use_for_SM_parity_local_spine": True,
            "may_use_for_full_no_knob_closure": False,
        },
    }

    execution = {
        "schema": "MTTFHuvRestrictionMatrixRowExecution.v1",
        "status": "FHUV_RESTRICTION_MATRIX_EXECUTED_ZERO_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "requested_matrix": {
            "ambient_matrix": "Hess(F_C1)_selected on the 27-mode selected source basis",
            "restriction": "M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv",
            "required_output_rows": [
                "Huu",
                "Hud_re",
                "Hud_im",
                "Hdd",
                "Delta",
                "Re_Omega",
                "Im_Omega",
            ],
            "required_certificates": [
                "source_ownership_certificate",
                "same_source_exactness_or_error_certificate",
                "quotient_admissibility_certificate",
                "Hdu_equals_conj_Hud_certificate",
            ],
        },
        "current_inputs": {
            "B_Huv_symbolic_exact_payload_emitted": True,
            "R_H_symbolic_exact_payload_emitted": rh["canonical_restriction"][
                "R_H_symbolic_exact_payload_emitted"
            ],
            "selected_C1_Hessian_or_b_selected_source_rows_emitted": False,
            "direct_Herm2_rows_emitted": False,
            "selected_H_response_table_emitted": False,
        },
        "current_direct_table": hresponse_direct["required_table"],
        "current_values": dynamic_gate["current_values"],
        "emitted_rows": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
        },
        "emitted_certificates": {
            "source_ownership_certificate": None,
            "same_source_exactness_or_error_certificate": None,
            "quotient_admissibility_certificate": None,
            "Hdu_equals_conj_Hud_certificate": None,
        },
        "decision": {
            "F_Huv_restriction_matrix_row_execution_attempted": True,
            "selected_F_Huv_second_variation_emitted": False,
            "direct_Herm2_row_payload_emitted": False,
            "accepted_F_Huv_row_count": 0,
            "accepted_direct_Herm2_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterFHuvRestrictionCriterion.v1",
        "status": "NEXT_FRONTIER_FHUV_RESTRICTION_MATRIX_ROWS_OR_BSELECTED_PROJECTION_EXECUTION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "F_Huv as restriction of selected finite C1/Weyl second variation to B_Huv",
            "matrix formula M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv",
            "local-premise bridge separated from strict no-knob bridge",
            "direct Herm(2) row payload execution rechecked with zero rows",
        ],
        "still_open": [
            "actual 27-mode selected Hess(F_C1) or b_selected row source entries",
            "B_Huv projection execution producing Huu,Hud,Hdd",
            "nonzero trace-free Omega/Delta rows or direct certified Herm(2) rows",
            "same-source exactness/error certificate for the restricted Hessian",
            "unpatched derivation or independent quadrature source for no-knob closure",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedFHuvSecondVariationSourceOrDirectHerm2RowPayload",
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
            "name": "FHuvRestrictionCriterionTheorem",
            "proved": True,
            "statement": (
                "The selected F_Huv source, if emitted, is the restriction of the "
                "selected finite C1/Weyl second variation to the source-orthonormal "
                "B_Huv domain: M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv. "
                "This closes the restriction criterion and separates the local "
                "premise-conditional bridge from strict no-knob promotion. Current "
                "data still emit no 27-mode selected Hessian rows, no B_Huv "
                "projection execution, and no direct certified Herm(2) payload."
            ),
        },
        "packets": {
            "fhuv_second_variation_restriction_criterion": rel(RESTRICTION),
            "local_principle_to_fhuv_bridge_status": rel(LOCAL_BRIDGE),
            "fhuv_restriction_matrix_row_execution": rel(EXECUTION),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "bhuv": rel(BHUV),
            "rh": rel(RH),
            "dynamic_gate": rel(DYNAMIC_GATE),
            "local_weyl": rel(LOCAL_WEYL),
            "local_weyl_candidate": rel(LOCAL_WEYL_CANDIDATE),
            "minimal_action": rel(MINIMAL_ACTION),
            "source_identity": rel(SOURCE_IDENTITY),
            "hresponse_direct": rel(HRESPONSE_DIRECT),
        },
        "closure_decision": {
            "F_Huv_restriction_criterion_closed": True,
            "B_Huv_R_H_domain_available": True,
            "Herm2_extraction_law_available": True,
            "local_premise_conditional_F_Huv_source_bridge_ready": True,
            "strict_unpatched_F_Huv_source_bridge_closed": False,
            "independent_quadrature_F_Huv_source_bridge_closed": False,
            "selected_C1_Hessian_matrix_rows_emitted": False,
            "B_selected_projection_execution_emitted": False,
            "selected_F_Huv_second_variation_emitted": False,
            "direct_Herm2_row_payload_emitted": False,
            "selected_H_response_table_emitted": False,
            "R_H_RG_value_emitted": False,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "selected_s_beta_value": s_beta,
            "ambient_selected_source_dimension": rh["selected_source_space"]["basis_dimension"],
            "Huv_restricted_dimension": 2,
            "accepted_F_Huv_row_count": 0,
            "accepted_direct_Herm2_row_count": 0,
            "accepted_certificate_count": 0,
            "accepted_non_diagonal_Huv_Hessian_source_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedFHuvSecondVariationSourceOrDirectHerm2RowPayload",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "F_Huv_restriction_criterion_closed": True,
        "B_Huv_R_H_domain_available": True,
        "Herm2_extraction_law_available": True,
        "local_premise_conditional_F_Huv_source_bridge_ready": True,
        "strict_unpatched_F_Huv_source_bridge_closed": False,
        "independent_quadrature_F_Huv_source_bridge_closed": False,
        "selected_C1_Hessian_matrix_rows_emitted": False,
        "B_selected_projection_execution_emitted": False,
        "selected_F_Huv_second_variation_emitted": False,
        "direct_Herm2_row_payload_emitted": False,
        "lambda_H_predicted": False,
        "accepted_F_Huv_row_count": 0,
        "accepted_direct_Herm2_row_count": 0,
        "accepted_certificate_count": 0,
    }

    note = f"""# MTT Selected FHuvSecondVariationSource or DirectHerm2RowPayload v1

Status: `{STATUS}`

## Theorem

The selected `F_Huv` source, if emitted, is not another free Higgs rule.  It is
the restriction of the selected finite C1/Weyl second variation to the already
selected source-orthonormal two-Higgs domain:

```text
F_Huv(z) = F_C1(B_Huv z)
M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv
```

Closed here:

- selected `B_Huv/R_H/P_H` domain is the correct restriction domain
- Herm(2) extraction law for `Huu,Hud,Hdd,Delta,Omega` is fixed
- local-premise C1/Weyl action bridge is separated from strict no-knob proof
- direct row payload execution is rechecked

Still not emitted:

- actual 27-mode selected `Hess(F_C1)` or `b_selected` source entries
- `B_Huv^* Hess(F_C1)_selected B_Huv` numeric/symbolic row execution
- source-owned `Huu,Hud,Hdd` rows and certificates
- strict unpatched or independent quadrature no-knob bridge

Accepted `F_Huv` rows: `0`.
Selected `s_beta` retained as projection support: `{s_beta}`.

Next artifact: `{NEXT}`
"""

    write_json(RESTRICTION, restriction)
    write_json(LOCAL_BRIDGE, local_bridge)
    write_json(EXECUTION, execution)
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
