"""Build Huv primitive formula or finite error-bound execution packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_huvprimitiveformula_or_finiteerrorboundexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HuvPrimitiveFormulaOrFiniteErrorBoundExecution_v1.md"

CONTRACT = PACKET_DIR / "huv_primitive_formula_execution_contract.packet.json"
UNDERDETERMINATION = PACKET_DIR / "bhuv_support_underdetermination_witness.packet.json"
ATTEMPT = PACKET_DIR / "huv_primitive_formula_execution_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_huv_primitive_formula_attempt.packet.json"

PREVIOUS = DATA / "selected_hresponserowsourceemission_or_directherm2certificatepayload.candidate.json"
MANIFEST = (
    DATA
    / "selected_hresponserowsourceemission_or_directherm2certificatepayload"
    / "row_source_certificate_payload_manifest.packet.json"
)
SOURCE_ATTEMPT = (
    DATA
    / "selected_hresponserowsourceemission_or_directherm2certificatepayload"
    / "primitive_hresponse_source_emission_attempt.packet.json"
)
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
DYNAMIC_HESSIAN = DATA / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission.candidate.json"
H_RESTRICTION = DATA / "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian.candidate.json"
MH_THREE_ROW = DATA / "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution.candidate.json"
MSOURCE_BLOCK = DATA / "selected_msourcehiggsspecificoperatorblock_or_c5c6bridgefrontier.candidate.json"
DIRECT_SEARCH = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "direct_mh_value_search_after_domain_closure.packet.json"
)

STATUS = (
    "MTT_SELECTED_HUVPRIMITIVEFORMULA_OR_FINITEERRORBOUNDEXECUTION_"
    "UNDERDETERMINED_SOURCE_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_FiniteHFunctionalOrMSourceValueEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Huv primitive formula inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        MANIFEST,
        SOURCE_ATTEMPT,
        BHUV,
        DYNAMIC_HESSIAN,
        H_RESTRICTION,
        MH_THREE_ROW,
        MSOURCE_BLOCK,
        DIRECT_SEARCH,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    manifest = load(MANIFEST)
    source_attempt = load(SOURCE_ATTEMPT)
    bhuv = load(BHUV)
    dynamic_hessian = load(DYNAMIC_HESSIAN)
    h_restriction = load(H_RESTRICTION)
    mh_three = load(MH_THREE_ROW)
    msource_block = load(MSOURCE_BLOCK)
    direct_search = load(DIRECT_SEARCH)

    contract = {
        "schema": "MTTHuvPrimitiveFormulaExecutionContract.v1",
        "status": "HUV_PRIMITIVE_FORMULA_EXECUTION_CONTRACT_FIXED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_inputs": {
            "B_Huv_two_column_lift": h_restriction["closure_decision"][
                "B_Huv_two_column_uv_lift_emitted"
            ],
            "R_H_restriction": h_restriction["closure_decision"][
                "selected_H_sector_restriction_R_H_emitted"
            ],
            "P_H_projector": h_restriction["closure_decision"]["selected_H_projector_P_H_emitted"],
            "Herm2_value_extraction_law": dynamic_hessian["closure_decision"][
                "Herm2_value_extraction_law_closed"
            ],
            "three_row_source_functional_contract": mh_three["closure_decision"][
                "MH_three_row_source_functional_contract_closed"
            ],
        },
        "legal_execution_routes": {
            "finite_H_functional_second_variation": {
                "formula": "H_ab = d^2 F_H(B_a,B_b) on ordered B_Huv coordinates",
                "requires": [
                    "selected finite H-sector functional F_H",
                    "same-source second-variation formula on B_Huv",
                    "exactness proof or rigorous finite error bound",
                ],
            },
            "selected_M_source_restriction": {
                "formula": "H_uv = B_Huv^* M_source B_Huv",
                "requires": [
                    "selected same-source Hermitian M_source",
                    "restriction proof to B_Huv",
                    "row-level exactness/source-ownership certificate",
                ],
            },
            "direct_primitive_overlap_rows": {
                "formula": "H_ab = Tr_Q(B_a^* K_H B_b) for selected H-sector response kernel K_H",
                "requires": [
                    "selected primitive H-sector response kernel",
                    "finite trace/quadrature rule tied to the selected branch",
                    "exactness proof or rigorous numerical error bound",
                ],
            },
        },
        "decision": {
            "formula_contract_closed": True,
            "execution_requires_value_source_not_more_support": True,
        },
    }

    underdetermination = {
        "schema": "MTTBHuvSupportUnderdeterminationWitness.v1",
        "status": "BHUV_SUPPORT_UNDERDETERMINES_HERM2_VALUE_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "fixed_support": {
            "B_Huv_source_orthonormality": bhuv["whitening_map_and_lift"][
                "source_orthonormality_certificate"
            ],
            "same_branch": bhuv["same_source_branch"],
            "quotient_support": bhuv["minimal_lift_request_tests"][
                "quotient_admissibility_certificate"
            ],
        },
        "two_non_scalar_herm2_completions_same_support": [
            {
                "label": "diagonal_tracefree_completion",
                "matrix": [["1", "0"], ["0", "-1"]],
                "rows": {"Huu": "1", "Hud_re": "0", "Hud_im": "0", "Hdd": "-1"},
                "Delta": "1",
                "Omega": "0",
            },
            {
                "label": "offdiagonal_real_completion",
                "matrix": [["0", "1"], ["1", "0"]],
                "rows": {"Huu": "0", "Hud_re": "1", "Hud_im": "0", "Hdd": "0"},
                "Delta": "0",
                "Omega": "1",
            },
        ],
        "mathematical_point": (
            "The same closed B_Huv source-orthonormal domain admits distinct "
            "non-scalar Herm(2) value operators with different Huu,Hud,Hdd rows. "
            "Therefore B_Huv support plus support certificates cannot select the "
            "physical H-response rows; a selected F_H, M_source, or primitive "
            "H-response kernel is necessary."
        ),
        "decision": {
            "underdetermination_witness_constructed": True,
            "B_Huv_support_selects_value_rows": False,
            "direct_closure_from_support_only_allowed": False,
        },
    }

    attempt = {
        "schema": "MTTHuvPrimitiveFormulaExecutionAttempt.v1",
        "status": "HUV_PRIMITIVE_FORMULA_EXECUTION_ATTEMPTED_ZERO_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "current_route_recheck": {
            "previous_payload_status": previous["status"],
            "previous_accepted_payload_slots": previous["key_numbers"]["accepted_payload_slot_count"],
            "dynamic_hessian_status": dynamic_hessian["status"],
            "h_restriction_status": h_restriction["status"],
            "mh_three_row_status": mh_three["status"],
            "msource_block_status": msource_block["status"],
            "direct_search_status": direct_search["status"],
            "any_direct_attempt_emits_values": direct_search["direct_value_attempts"][
                "any_direct_attempt_emits_values"
            ],
        },
        "execution_values": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
        },
        "decision": {
            "execution_attempted": True,
            "formula_contract_available": True,
            "underdetermination_witness_constructed": True,
            "selected_finite_H_functional_emitted": False,
            "selected_M_source_value_emitted": False,
            "selected_primitive_H_response_kernel_emitted": False,
            "finite_error_bound_emitted": False,
            "selected_H_response_value_rows_emitted": False,
            "accepted_value_row_count": 0,
            "accepted_final_certificate_count": 0,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHuvPrimitiveFormulaAttempt.v1",
        "status": "NEXT_FRONTIER_FINITE_H_FUNCTIONAL_OR_MSOURCE_VALUE_EMISSION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "primitive Huv formula execution contract fixed",
            "B_Huv support-only direct closure rejected by explicit Herm(2) underdetermination witness",
            "current finite-H, M_source, and primitive-overlap routes rechecked with zero accepted rows",
        ],
        "still_open": [
            "selected finite H-sector functional F_H with second variation on B_Huv",
            "or selected same-source Hermitian M_source values",
            "or selected primitive H-response kernel K_H with finite trace execution",
            "row-level exactness proof or rigorous finite error bound",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHuvPrimitiveFormulaOrFiniteErrorBoundExecution",
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
            "name": "BHuvSupportUnderdeterminesHuvRowsTheorem",
            "proved": True,
            "statement": (
                "The direct attack closes negatively but sharply: B_Huv and the "
                "support certificates fix the Huv coordinate domain, not the "
                "Herm(2) value operator. Two distinct non-scalar Herm(2) "
                "operators on the same B_Huv support produce different Huu,Hud,Hdd "
                "rows. Therefore the final row payload cannot be closed by "
                "attaching B_Huv support. A selected finite H functional, selected "
                "M_source, or selected primitive H-response kernel with row-level "
                "exactness/error bound is mathematically necessary."
            ),
        },
        "packets": {
            "huv_primitive_formula_execution_contract": rel(CONTRACT),
            "bhuv_support_underdetermination_witness": rel(UNDERDETERMINATION),
            "huv_primitive_formula_execution_attempt": rel(ATTEMPT),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "manifest": rel(MANIFEST),
            "source_attempt": rel(SOURCE_ATTEMPT),
            "bhuv": rel(BHUV),
            "dynamic_hessian": rel(DYNAMIC_HESSIAN),
            "h_restriction": rel(H_RESTRICTION),
            "mh_three_row": rel(MH_THREE_ROW),
            "msource_block": rel(MSOURCE_BLOCK),
            "direct_search": rel(DIRECT_SEARCH),
        },
        "closure_decision": {
            "primitive_formula_contract_closed": True,
            "underdetermination_witness_constructed": True,
            "B_Huv_support_direct_closure_rejected": True,
            "selected_finite_H_functional_emitted": False,
            "selected_M_source_value_emitted": False,
            "selected_primitive_H_response_kernel_emitted": False,
            "finite_error_bound_emitted": False,
            "selected_H_response_value_rows_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "non_scalar_herm2_witnesses": 2,
            "accepted_value_row_count": 0,
            "accepted_final_certificate_count": 0,
            "accepted_payload_slot_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedHuvPrimitiveFormulaOrFiniteErrorBoundExecution",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "primitive_formula_contract_closed": True,
        "underdetermination_witness_constructed": True,
        "B_Huv_support_direct_closure_rejected": True,
        "non_scalar_herm2_witnesses": 2,
        "accepted_value_row_count": 0,
        "accepted_final_certificate_count": 0,
        "selected_finite_H_functional_emitted": False,
        "selected_M_source_value_emitted": False,
        "selected_primitive_H_response_kernel_emitted": False,
        "finite_error_bound_emitted": False,
        "selected_H_response_value_rows_emitted": False,
    }

    note = f"""# MTT Selected HuvPrimitiveFormula or FiniteErrorBoundExecution v1

Status: `{STATUS}`

## Theorem

The direct closure attempt is now mathematically decided.

`B_Huv` fixes the selected source-orthonormal coordinate domain, but it does not
select the Herm(2) value operator.  On the same `B_Huv` support, both of these
non-scalar Herm(2) completions are compatible as formal value operators:

```text
diag(1,-1)  -> Huu=1, Hud=0, Hdd=-1
[[0,1],[1,0]] -> Huu=0, Hud=1, Hdd=0
```

They give different `Huu,Hud,Hdd` rows while sharing the same closed support
layer.  Therefore attaching `B_Huv` support cannot close the final row payload.

Closed here:

- primitive Huv formula execution contract
- explicit underdetermination witness against support-only closure
- recheck of current finite-H, `M_source`, and primitive/direct rows with `0`
  accepted values

Still required:

- selected finite H-sector functional `F_H`, or
- selected same-source Hermitian `M_source`, or
- selected primitive H-response kernel `K_H`,
- plus row-level exactness proof or rigorous finite error bound.

Next artifact: `{NEXT}`
"""

    write_json(CONTRACT, contract)
    write_json(UNDERDETERMINATION, underdetermination)
    write_json(ATTEMPT, attempt)
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
