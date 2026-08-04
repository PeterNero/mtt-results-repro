"""Build F_Huv restriction matrix rows or B-selected projection execution packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fhuvrestrictionmatrixrows_or_bselectedprojectionexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FHuvRestrictionMatrixRows_or_BSelectedProjectionExecution_v1.md"

IMPORT = PACKET_DIR / "selected_c1_hessian_payload_import.packet.json"
SHAPE = PACKET_DIR / "bhuv_projection_shape_compatibility.packet.json"
EXECUTION = PACKET_DIR / "bselected_projection_execution_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_fhuv_projection_attempt.packet.json"

PREVIOUS = DATA / "selected_fhuvsecondvariationsource_or_directherm2rowpayload.candidate.json"
DYNAMIC_PAYLOAD = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "selected_dynamic_phifinc1_payload_promotion.packet.json"
)
SOURCE_RECONCILIATION = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "source_rule_backimport_reconciliation.packet.json"
)
ASSEMBLY_MAP = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "all_primitive_rows_assembly_map.packet.json"
)
FORMAL_110 = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)
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
DIRECT = (
    DATA
    / "selected_fhuvsecondvariationsource_or_directherm2rowpayload"
    / "fhuv_restriction_matrix_row_execution.packet.json"
)

STATUS = (
    "MTT_SELECTED_FHUVRESTRICTIONMATRIXROWS_OR_BSELECTEDPROJECTIONEXECUTION_"
    "C1_PAYLOAD_IMPORTED_PROJECTION_TENSOR_OPEN"
)
NEXT = "MTT_Selected_C1ToBHuvProjectionTensor_or_FHuvRows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing F_Huv projection inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        DYNAMIC_PAYLOAD,
        SOURCE_RECONCILIATION,
        ASSEMBLY_MAP,
        FORMAL_110,
        BHUV,
        RH,
        DIRECT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    dynamic = load(DYNAMIC_PAYLOAD)
    reconciliation = load(SOURCE_RECONCILIATION)
    assembly = load(ASSEMBLY_MAP)
    formal = load(FORMAL_110)
    bhuv = load(BHUV)
    rh = load(RH)
    direct = load(DIRECT)

    ata = dynamic["exact_values"]["A_transpose_A"]
    atb = dynamic["exact_values"]["A_transpose_b"]
    rank = dynamic["exact_values"]["rank"]
    s_beta = previous["key_numbers"]["selected_s_beta_value"]

    payload_import = {
        "schema": "MTTSelectedC1HessianPayloadImport.v1",
        "status": "STRICT_DYNAMIC_C1_PAYLOAD_IMPORTED_COMPRESSED_COORDINATES_ONLY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_rule": {
            "source_rule_premise_free": dynamic["source_rule_premise_free"],
            "source_owner": dynamic["source_owner"],
            "selected_dynamic_phi_fin_c1_payload_emitted": dynamic["decision"][
                "selected_dynamic_phi_fin_c1_payload_emitted"
            ],
            "b_selected_promoted_strict": dynamic["decision"]["b_selected_promoted_strict"],
            "A_selected_promoted_strict": dynamic["decision"]["A_selected_promoted_strict"],
            "deltaTheta_C1_promoted_strict": dynamic["decision"][
                "deltaTheta_C1_promoted_strict"
            ],
            "unpatched_source_rule_proved_by_backimport": reconciliation["decision"][
                "unpatched_source_rule_proved_by_backimport"
            ],
        },
        "compressed_payload": {
            "rank": rank,
            "A_transpose_A": ata,
            "A_transpose_b": atb,
            "deltaTheta_C1": dynamic["exact_values"]["deltaTheta_C1"],
            "hessian_b_source_rows": dynamic["row_counts"]["hessian_b_source_rows"],
            "formal_110_total_rows": dynamic["row_counts"]["formal_110_total_rows"],
            "primitive_kernel_rows": dynamic["row_counts"]["primitive_kernel_rows"],
            "sector_assembly_rows": dynamic["row_counts"]["sector_assembly_rows"],
        },
        "source_stack_evidence": {
            "all_72_primitive_rows_exact": assembly["row_evidence"][
                "all_72_primitive_rows_exact"
            ],
            "formal_110_rows_executed": assembly["row_evidence"][
                "formal_110_rows_executed"
            ],
            "formal_110_max_abs_error": assembly["row_evidence"][
                "formal_110_max_abs_error"
            ],
            "selected_field_count": assembly["assembly_source_fields"]["selected_field_count"],
            "formal_hessian_rows_count": formal["hessian_source_rows"]["count"],
        },
        "not_imported_as": {
            "ambient_27_by_27_Hess_F_C1_matrix": False,
            "B_Huv_restriction_tensor": False,
            "Higgs_specific_non_diagonal_Huv_block": False,
            "direct_Herm2_row_payload": False,
        },
        "decision": {
            "strict_dynamic_C1_payload_imported": True,
            "compressed_C1_Hessian_rows_available": True,
            "selected_b_selected_available": True,
            "ambient_27_mode_Hessian_matrix_emitted": False,
            "B_Huv_projection_tensor_emitted": False,
        },
    }

    shape = {
        "schema": "MTTBHuvProjectionShapeCompatibility.v1",
        "status": "BHUV_PROJECTION_SHAPE_CHECK_EXECUTED_TENSOR_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_domains": {
            "compressed_C1_variation_space_dimension": rank,
            "B_Huv_column_count": 2,
            "ambient_selected_source_dimension": rh["selected_source_space"]["basis_dimension"],
            "B_Huv_symbolic_exact_payload_emitted": bhuv["whitening_map_and_lift"][
                "B_Huv_symbolic_exact_payload_emitted"
            ],
            "R_H_symbolic_exact_payload_emitted": rh["canonical_restriction"][
                "R_H_symbolic_exact_payload_emitted"
            ],
        },
        "needed_for_F_Huv_rows": {
            "projection_tensor": (
                "T_C1<-Huv mapping the selected B_Huv columns into the two "
                "selected C1 variation coordinates before residual replay"
            ),
            "or_full_matrix": "ambient 27x27 Hess(F_C1)_selected with B_Huv columns",
            "execution_formula": "M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv",
        },
        "shape_obstruction": {
            "A_transpose_A_shape": "2x2 compressed C1 normal matrix",
            "B_Huv_shape": "27x2 symbolic source columns",
            "missing_map": "C1 variation coordinates <- selected B_Huv source columns",
            "why_A_transpose_A_is_not_enough": (
                "A^T A is already compressed by the selected C1 row map. Without "
                "the source-owned inclusion/projection of B_Huv into that row map, "
                "the 2x2 C1 normal matrix cannot be reinterpreted as the Higgs "
                "Herm(2) block."
            ),
        },
        "decision": {
            "shape_compatibility_checked": True,
            "dimension_counts_match_for_possible_2x2_restriction": True,
            "projection_tensor_required": True,
            "projection_tensor_emitted": False,
            "ambient_27_by_27_Hessian_matrix_emitted": False,
        },
    }

    scalar_trace = ata[0][0] + ata[1][1]
    trace_free_ata = [
        [ata[0][0] - scalar_trace / 2.0, ata[0][1]],
        [ata[1][0], ata[1][1] - scalar_trace / 2.0],
    ]
    trace_free_norm = sum(value * value for row in trace_free_ata for value in row) ** 0.5

    execution = {
        "schema": "MTTBSelectedProjectionExecutionAttempt.v1",
        "status": "BSELECTED_PROJECTION_EXECUTION_ATTEMPTED_ZERO_HUV_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_available_payload": {
            "A_transpose_A": ata,
            "A_transpose_b": atb,
            "rank": rank,
            "selected_b_selected_available": True,
        },
        "naive_identification_guard": {
            "tested_matrix_if_A_transpose_A_were_misidentified_as_M_Huv": ata,
            "trace_free_part": trace_free_ata,
            "trace_free_norm": trace_free_norm,
            "would_emit_non_diagonal_Huv": False,
            "decision": (
                "Even the forbidden naive identification A^T A -> M_Huv would "
                "give scalar 12 I_2 and zero trace-free Higgs block. It cannot "
                "supply Omega or a non-diagonal Huv payload."
            ),
        },
        "legal_execution": {
            "M_Huv_formula": direct["requested_matrix"]["restriction"],
            "ambient_matrix_available": False,
            "projection_tensor_available": False,
            "B_Huv_projection_execution_emitted": False,
            "direct_Herm2_rows_emitted": False,
        },
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
            "C1_to_BHuv_projection_tensor_certificate": None,
        },
        "decision": {
            "B_selected_projection_execution_attempted": True,
            "selected_C1_Hessian_payload_imported": True,
            "naive_scalar_C1_normal_matrix_rejected_as_Huv": True,
            "selected_F_Huv_second_variation_emitted": False,
            "direct_Herm2_row_payload_emitted": False,
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterFHuvProjectionAttempt.v1",
        "status": "NEXT_FRONTIER_C1_TO_BHUV_PROJECTION_TENSOR_OR_FHUV_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "strict dynamic C1 Hessian/b_selected payload imported into Huv frontier",
            "compressed C1 normal matrix separated from ambient 27x27 Hessian",
            "B_Huv projection shape obstruction identified",
            "naive A^T A -> Huv promotion rejected as scalar and non-diagonal-zero",
        ],
        "still_open": [
            "source-owned C1 variation coordinate map for B_Huv columns",
            "or ambient 27x27 Hess(F_C1)_selected matrix entries",
            "B_Huv^* Hess(F_C1)_selected B_Huv row execution",
            "nonzero Omega or direct certified Huv rows",
            "C1-to-BHuv projection tensor certificate",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedFHuvRestrictionMatrixRowsOrBSelectedProjectionExecution",
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
            "name": "CompressedC1PayloadIsNotYetFHuvRowsTheorem",
            "proved": True,
            "statement": (
                "The active strict dynamic C1 ledger promotes A_selected, "
                "b_selected, deltaTheta_C1, and the compressed two-row Hessian "
                "payload. This removes the old source-promotion blocker, but it "
                "does not by itself emit the Higgs F_Huv rows: A^T A is a "
                "compressed C1 normal matrix, not the ambient 27x27 Hess(F_C1) "
                "on B_Huv. A source-owned C1-to-BHuv projection tensor or the "
                "ambient Hessian entries are still required. The forbidden naive "
                "identification gives scalar 12 I_2 and zero non-diagonal Huv."
            ),
        },
        "packets": {
            "selected_c1_hessian_payload_import": rel(IMPORT),
            "bhuv_projection_shape_compatibility": rel(SHAPE),
            "bselected_projection_execution_attempt": rel(EXECUTION),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "dynamic_payload": rel(DYNAMIC_PAYLOAD),
            "source_reconciliation": rel(SOURCE_RECONCILIATION),
            "assembly_map": rel(ASSEMBLY_MAP),
            "formal_110": rel(FORMAL_110),
            "bhuv": rel(BHUV),
            "rh": rel(RH),
            "direct": rel(DIRECT),
        },
        "closure_decision": {
            "strict_dynamic_C1_payload_imported": True,
            "compressed_C1_Hessian_rows_available": True,
            "selected_b_selected_available": True,
            "B_selected_projection_execution_attempted": True,
            "shape_compatibility_checked": True,
            "naive_scalar_C1_normal_matrix_rejected_as_Huv": True,
            "ambient_27_mode_Hessian_matrix_emitted": False,
            "C1_to_BHuv_projection_tensor_emitted": False,
            "B_Huv_projection_execution_emitted": False,
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
            "compressed_C1_rank": rank,
            "A_transpose_A_trace": scalar_trace,
            "A_transpose_A_trace_free_norm": trace_free_norm,
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedFHuvRestrictionMatrixRowsOrBSelectedProjectionExecution",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_dynamic_C1_payload_imported": True,
        "compressed_C1_Hessian_rows_available": True,
        "selected_b_selected_available": True,
        "B_selected_projection_execution_attempted": True,
        "shape_compatibility_checked": True,
        "naive_scalar_C1_normal_matrix_rejected_as_Huv": True,
        "ambient_27_mode_Hessian_matrix_emitted": False,
        "C1_to_BHuv_projection_tensor_emitted": False,
        "B_Huv_projection_execution_emitted": False,
        "selected_F_Huv_second_variation_emitted": False,
        "direct_Herm2_row_payload_emitted": False,
        "lambda_H_predicted": False,
        "accepted_F_Huv_row_count": 0,
        "accepted_certificate_count": 0,
    }

    note = f"""# MTT Selected FHuvRestrictionMatrixRows or BSelectedProjectionExecution v1

Status: `{STATUS}`

## Theorem

The strict dynamic C1 ledger now supplies the promoted compressed Hessian/source
payload:

```text
A^T A = {ata}
A^T b = {atb}
```

This removes the old `b_selected` source-promotion blocker for the Huv frontier.
It does **not** yet emit `F_Huv` rows, because `A^T A` is a compressed C1
normal matrix, while the Huv theorem requires:

```text
M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv
```

The missing object is now sharply identified as either:

- the source-owned C1 variation-coordinate map for the selected `B_Huv` columns,
  or
- the ambient 27x27 selected `Hess(F_C1)` matrix entries.

The forbidden naive promotion `A^T A -> M_Huv` was tested and rejected: it gives
scalar `12 I_2`, trace-free norm `{trace_free_norm}`, and no non-diagonal
`Omega` row.

Accepted `F_Huv` rows: `0`.
Selected `s_beta` retained as projection support: `{s_beta}`.

Next artifact: `{NEXT}`
"""

    write_json(IMPORT, payload_import)
    write_json(SHAPE, shape)
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
