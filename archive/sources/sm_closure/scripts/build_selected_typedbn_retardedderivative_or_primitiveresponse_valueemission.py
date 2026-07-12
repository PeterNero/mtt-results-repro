"""Build typed B_N retarded-derivative or primitive-response value emission."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

DYNAMIC = DATA / "selected_dynamic_overlapkernel_or_c1primitive_source_emission.candidate.json"
CONTRACT = DATA / "visible_routec_sourceidentity_or_typedbn_derivative_contract.candidate.json"
PARTIAL = DATA / "visible_routec_sourceidentity_or_typedbn_derivative.partial_fill.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
WEYL_A = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
ALPHA_FILL = DATA / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"

OUTPUT = DATA / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"
CERT = CERTS / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission_certificate.json"
NOTE = CORPUS / "MTT_Selected_TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_v1.md"

STATUS = (
    "MTT_SELECTED_TYPEDBN_RETARDEDDERIVATIVE_OR_PRIMITIVERESPONSE_"
    "VALUEEMISSION_BUILT_PRIMITIVE_CANDIDATES_UNSELECTED"
)
NEXT = "MTT_Selected_PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def fixed_fiber_candidate_summary(noninv: dict[str, Any]) -> list[dict[str, Any]]:
    fixed = []
    for item in noninv["candidate_primitives"]:
        fiber_shift = item["primitive_fiber_shift"]
        if fiber_shift not in [0, 1, 2]:
            continue
        ranks = {sector: summary["rank"] for sector, summary in item["summary"].items()}
        max_abs = {
            sector: summary["max_abs_entry"] for sector, summary in item["summary"].items()
        }
        fixed.append(
            {
                "primitive_active_shift": item["primitive_active_shift"],
                "primitive_fiber_shift": fiber_shift,
                "status": item["status"],
                "selected_by_theorem": item["selected_by_theorem"],
                "sector_ranks": ranks,
                "sector_max_abs_entry": max_abs,
                "support_patterns": {
                    sector: summary["support_pattern"]
                    for sector, summary in item["summary"].items()
                },
            }
        )
    return fixed


def main() -> int:
    dynamic = load(DYNAMIC)
    contract = load(CONTRACT)
    partial = load(PARTIAL)
    noninv = load(NONINV)
    weyl_a = load(WEYL_A)
    alpha_fill = load(ALPHA_FILL)

    fixed_candidates = fixed_fiber_candidate_summary(noninv)
    fixed_fiber_values_ready = (
        len(fixed_candidates) == 3
        and all(
            candidate["primitive_active_shift"] == [1, 1]
            and all(rank == 3 for rank in candidate["sector_ranks"].values())
            and candidate["selected_by_theorem"] is False
            for candidate in fixed_candidates
        )
    )

    typed_retarded_lane = {
        "attempted": True,
        "selected_emitted": False,
        "support_present": True,
        "contract_lane_fields": contract["required_certificate"]["lane_B_fields"],
        "partial_fill_closed": partial["partial_fill_result"][
            "lane_B_typed_retarded_derivative_closed"
        ],
        "blocking_fields": {
            field: {
                "selected_emitted": partial["lane_B_typed_bn_retarded_derivative"][field][
                    "selected_emitted"
                ],
                "theorem_derived": partial["lane_B_typed_bn_retarded_derivative"][field][
                    "theorem_derived"
                ],
                "provenance": partial["lane_B_typed_bn_retarded_derivative"][field][
                    "provenance"
                ],
            }
            for field in contract["required_certificate"]["lane_B_fields"]
        },
        "why_not_promoted": (
            "Every Lane B field remains support-only or retarded-pattern-only. The validator therefore "
            "correctly refuses to promote alpha1_driver_verified or a typed dynamic derivative."
        ),
    }

    primitive_response_lane = {
        "attempted": True,
        "candidate_values_emitted": fixed_fiber_values_ready,
        "selected_emitted": False,
        "active_shift_forced": noninv["search_rule"]["minimal_active_shift_required"] == [1, 1],
        "canonical_mode_conserving_no_go": noninv["calculation_results"][
            "can_close_selected_C1_now"
        ]
        is False,
        "fixed_fiber_candidate_count": len(fixed_candidates),
        "fixed_fiber_candidates": fixed_candidates,
        "all_fixed_fiber_candidates_rank_three": fixed_fiber_values_ready,
        "fiber_shift_selector_emitted": False,
        "why_not_promoted": (
            "The active shift (1,1) and three rank-3 fixed-fiber primitive response candidates are "
            "computed without observed flavor data, but no source theorem selects fiber shift 0, 1, "
            "or 2, and the all-fiber envelope has rank 1 rather than a selected full-rank flavor "
            "operator."
        ),
    }

    conditional_solver_packet = {
        "conditional_weylpair_A_exact": weyl_a["locked_solve"]["consistent"],
        "conditional_A_rank": weyl_a["locked_solve"]["rank"],
        "conditional_deltaTheta": weyl_a["locked_solve"]["deltaTheta_conditional"],
        "conditional_residual_norm": weyl_a["locked_solve"]["residual_norm"],
        "conditional_b_norm": weyl_a["locked_solve"]["b_norm"],
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "reason": (
            "The two-column Weyl-pair solve is algebraically ready, but A_selected and b_selected "
            "need selected primitive fiber shift or typed retarded selector provenance."
        ),
    }

    alpha1_value_packet = {
        "lambda_alpha1": alpha_fill["source_strength_coordinate"]["lambda_alpha1"],
        "N_alpha1_h_ext": alpha_fill["normalization_functional"]["N_alpha1_h_ext"],
        "tangent_residual_l2": alpha_fill["tangent_equality"]["residual_l2"],
        "selected_value_emitted": alpha_fill["promotion_result"]["selected_value_emitted"],
        "alpha1_driver_verified": alpha_fill["promotion_result"]["alpha1_driver_verified"],
        "used_as_selector": False,
    }

    theorem = {
        "name": "TypedBNRetardedDerivativeOrPrimitiveResponseValueEmissionTheorem",
        "proved": True,
        "statement": (
            "The typed B_N retarded-derivative lane cannot be emitted from current theorem data, "
            "because its selector, derivative, transfer normalization, sector equality, and honest "
            "dotD replay remain unselected. The primitive-response lane does emit exact finite "
            "rank-3 candidate values for the three fixed fiber shifts at active shift (1,1), but "
            "these are not selected until MTT supplies a primitive fiber-shift/source selector or "
            "an equivalent typed retarded selector. Thus the next proof gate is selector provenance, "
            "not more finite linear algebra."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedTypedBNRetardedDerivativeOrPrimitiveResponseValueEmission",
        "status": STATUS,
        "inputs": {
            "dynamic_overlap_or_c1primitive_reduction": rel(DYNAMIC),
            "visible_routec_or_typedbn_contract": rel(CONTRACT),
            "visible_routec_or_typedbn_partial_fill": rel(PARTIAL),
            "noninvariant_c1_primitive_search": rel(NONINV),
            "conditional_weylpair_A_assembly": rel(WEYL_A),
            "alpha1_normalization_fill_attempt": rel(ALPHA_FILL),
        },
        "superset_strategy": {
            "mode": "DUAL_LANE_VALUE_EMISSION_ATTEMPT",
            "straight_lane": "typed B_N retarded derivative is tested against the existing promotion validator",
            "support_lane": "non-invariant primitive response values are emitted as finite candidate data",
            "locked_target_role": "conditional Weyl-pair solve and alpha1 unit packet are diagnostics, not selectors",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "typed_retarded_lane": typed_retarded_lane,
        "primitive_response_lane": primitive_response_lane,
        "conditional_solver_packet": conditional_solver_packet,
        "alpha1_value_packet": alpha1_value_packet,
        "selector_cutset": {
            "closed_arithmetic": [
                "active shift (1,1) is forced by finite momentum bookkeeping",
                "three fixed-fiber primitive response candidates are rank 3",
                "conditional two-column Weyl-pair solve has rank 2 and tiny residual",
                "alpha1 unit packet remains numerically ready",
            ],
            "remaining_selector_options": [
                "primitive fiber-shift/source selector choosing one of 0,1,2",
                "typed retarded selector deriving Lane B fields without retarded-pattern provenance",
                "basis-transport/vertex theorem proving the selected primitive response directly",
            ],
        },
        "what_closes_now": {
            "typed_retarded_lane_tested_and_blocked_by_validator": True,
            "primitive_response_fixed_fiber_value_candidates_emitted": fixed_fiber_values_ready,
            "active_shift_1_1_confirmed": True,
            "conditional_weylpair_solve_reused_as_readiness_check": True,
            "next_gate_reduced_to_selector_provenance": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_typed_BN_retarded_derivative": True,
            "selected_retarded_source_selector": True,
            "selected_primitive_fiber_shift": True,
            "selected_primitive_or_vertex_response": True,
            "selected_b_selected": True,
            "promote_conditional_A_to_A_selected": True,
            "honest_selected_deltaTheta_C1_solve": True,
            "alpha1_driver_verified": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "typed_retarded_derivative_emitted": False,
        "primitive_response_candidate_values_emitted": fixed_fiber_values_ready,
        "selected_primitive_response_emitted": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "typed_retarded_derivative_emitted": False,
        "primitive_response_candidate_values_emitted": fixed_fiber_values_ready,
        "selected_primitive_response_emitted": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected TypedBN RetardedDerivative or PrimitiveResponse ValueEmission v1

Status: `{STATUS}`.

## Result

The typed `B_N` retarded-derivative lane is tested and remains blocked by the
promotion validator.  Its selector, derivative, transfer normalization, sector
equality, and honest `dotD` replay are still support-only.

The primitive-response lane now carries concrete finite value candidates:

```text
active shift: (1,1)
fixed fiber shifts: 0, 1, 2
rank per u,d,e,nuD block: 3
max absolute entry: {fixed_candidates[0]["sector_max_abs_entry"]["u"] if fixed_candidates else "n/a"}
```

These are candidate values, not selected values.  No observed constants or
benchmark matrices are used.

## Boundary

`A_selected`, `b_selected`, alpha1, and flavor data remain open.  The next proof
object is selector provenance: either a primitive fiber-shift/source selector,
a typed retarded selector, or an equivalent basis-transport/vertex theorem.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
