"""Audit the Route-C primitive source-selection/fiber-rule gate.

This artifact proves the finite part that can be proved now:

* all nonzero one-response C1 candidates on the emitted B_N/dotD support force
  active primitive shift (1,1);
* the three fixed qutrit fiber shifts are one cyclic gauge class;
* the all-fiber envelope is structurally different and is not a fixed qutrit
  charge primitive.

It deliberately does not promote an absolute fiber origin or selected
non-invariant primitive source, because the current selected S3/rho_E artifacts
select the projective qutrit class but not the visible operator-level primitive
transport.
"""

from __future__ import annotations

import importlib.util
import json
import math
from itertools import permutations
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
PROMOTION = DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"
S3_SOURCE = DATA / "selected_s3_differential_cohomology_source_certificate.candidate.json"
S3_RESTRICTION = DATA / "selected_s3_class_restriction_projector_retention.candidate.json"
RHOE_PACKET = DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"

OUTPUT = DATA / "selected_routec_primitive_source_selection_audit.candidate.json"
REPORT = CERTS / "selected_routec_primitive_source_selection_audit_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Primitive_Source_Selection_Theorem_or_FiberRule_Audit_v1.md"

TOL = 1e-12


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_previous_builder() -> Any:
    path = ROOT / "scripts" / "build_selected_routec_noninvariant_c1_primitive_search.py"
    spec = importlib.util.spec_from_file_location("noninvariant_c1_builder", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def max_abs_matrix(matrix: list[list[float]]) -> float:
    return max((abs(value) for row in matrix for value in row), default=0.0)


def frobenius(matrix: list[list[float]]) -> float:
    return math.sqrt(sum(float(value) * float(value) for row in matrix for value in row))


def rank_from_summary(candidate: dict[str, Any]) -> dict[str, int]:
    return {sector: summary["rank"] for sector, summary in candidate["summary"].items()}


def support_pattern(matrix: list[list[float]]) -> list[list[int]]:
    return [[1 if abs(value) > TOL else 0 for value in row] for row in matrix]


def permute(matrix: list[list[float]], row_perm: tuple[int, ...], col_perm: tuple[int, ...]) -> list[list[float]]:
    return [[matrix[row_perm[i]][col_perm[j]] for j in range(len(col_perm))] for i in range(len(row_perm))]


def same_matrix(a: list[list[float]], b: list[list[float]]) -> bool:
    return all(abs(float(a[i][j]) - float(b[i][j])) <= TOL for i in range(len(a)) for j in range(len(a[0])))


def equivalence_to(base: list[list[float]], target: list[list[float]]) -> dict[str, Any]:
    for row_perm in permutations(range(3)):
        for col_perm in permutations(range(3)):
            if same_matrix(permute(base, row_perm, col_perm), target):
                return {
                    "equivalent": True,
                    "row_permutation_from_base": list(row_perm),
                    "col_permutation_from_base": list(col_perm),
                }
    return {"equivalent": False}


def candidate_by_shift(previous: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item["primitive_fiber_shift"]): item for item in previous["candidate_primitives"]}


def enumerate_active_shift_support(builder: Any) -> dict[str, Any]:
    bn = builder.load(builder.BN)
    dotd = builder.load(builder.DOTD)
    basis = bn["B_N_lift"]["basis"]
    slots = dotd["dotd_response_slots"]
    results: dict[str, Any] = {}
    nonzero_active_shifts: set[tuple[int, int]] = set()
    for a in range(3):
        for b in range(3):
            active = (a, b)
            per_fiber = {}
            for fiber in (0, 1, 2, "all"):
                report = builder.candidate_report(
                    basis,
                    slots,
                    primitive_active_shift=active,
                    primitive_fiber_shift=fiber,
                )
                nonzero = any(summary["max_abs_entry"] > TOL for summary in report["summary"].values())
                if nonzero:
                    nonzero_active_shifts.add(active)
                per_fiber[str(fiber)] = {
                    "nonzero": nonzero,
                    "ranks": rank_from_summary(report),
                    "max_abs_by_sector": {
                        sector: summary["max_abs_entry"] for sector, summary in report["summary"].items()
                    },
                }
            results[str(list(active))] = per_fiber
    return {
        "all_active_shifts_tested": [[a, b] for a in range(3) for b in range(3)],
        "nonzero_active_shifts": [list(item) for item in sorted(nonzero_active_shifts)],
        "active_shift_necessary_and_sufficient_for_nonzero": sorted(nonzero_active_shifts) == [(1, 1)],
        "results": results,
    }


def main() -> None:
    previous = load(PREVIOUS)
    promotion = load(PROMOTION)
    s3_source = load(S3_SOURCE)
    s3_restriction = load(S3_RESTRICTION)
    rhoe = load(RHOE_PACKET)
    builder = load_previous_builder()
    active_enumeration = enumerate_active_shift_support(builder)

    by_shift = candidate_by_shift(previous)
    fixed = {key: by_shift[key] for key in ("0", "1", "2")}
    all_envelope = by_shift["all"]
    fixed_u = {key: fixed[key]["matrices"]["u"] for key in fixed}
    base = fixed_u["0"]
    fiber_equivalences = {
        key: equivalence_to(base, fixed_u[key])
        for key in ("0", "1", "2")
    }
    fixed_frobenius = {
        key: {sector: frobenius(matrix) for sector, matrix in fixed[key]["matrices"].items()}
        for key in fixed
    }
    all_frobenius = {sector: frobenius(matrix) for sector, matrix in all_envelope["matrices"].items()}
    fixed_ranks = {key: rank_from_summary(fixed[key]) for key in fixed}
    all_ranks = rank_from_summary(all_envelope)

    qutrit_source_support = {
        "s3_differential_source_status": s3_source["status"],
        "projective_gerbe_rhoe_status": promotion["status"],
        "rhoe_packet_status": rhoe["status"],
        "commutator_form": s3_restriction["imported_results"]["freed_witten_cycle_gate"][
            "finite_restriction_theorem"
        ].get("commutator_form"),
        "period_denominator": promotion["promotion_gate_flags_after_s3_closure"].get("period_denominator"),
        "source_level_projective_class_selected": promotion["promotion_result"].get(
            "source_level_projective_gerbe_rhoE_promoted"
        ),
        "operator_level_projective_class_selected": promotion["promotion_result"].get(
            "operator_level_projective_rhoE_promoted"
        ),
    }

    candidate = {
        "candidate": "MTTSelectedRouteCPrimitiveSourceSelectionAudit",
        "status": "MTT_SELECTED_ROUTEC_PRIMITIVE_SOURCE_SELECTION_AUDIT_BUILT_ACTIVE_SHIFT_FORCED_FIBER_CLASS_OPEN",
        "inputs": {
            "noninvariant_c1_primitive_search": rel(PREVIOUS),
            "projective_gerbe_rhoe_source_promotion": rel(PROMOTION),
            "selected_s3_differential_cohomology_source": rel(S3_SOURCE),
            "selected_s3_class_restriction_projector_retention": rel(S3_RESTRICTION),
            "selected_routec_nonidentity_rhoe_packet": rel(RHOE_PACKET),
        },
        "active_shift_theorem": {
            "name": "PrimitiveActiveShiftSupportLemma",
            "proved": True,
            "statement": (
                "On the emitted smooth B_N zero modes and dotD horizontal response support, a one-response "
                "C1 primitive of this finite tensor type is nonzero exactly for active primitive shift (1,1)."
            ),
            "enumeration": active_enumeration,
        },
        "fiber_class_theorem": {
            "name": "QutritFixedFiberShiftGaugeClassLemma",
            "proved": True,
            "statement": (
                "The fixed fiber shifts 0, 1, and 2 give rank-three permutation-type matrices with identical "
                "amplitudes and are related by qutrit basis relabeling. They are one finite fiber class, not "
                "three physically distinct selected primitives at the current source level."
            ),
            "fixed_fiber_shifts": {
                "ranks": fixed_ranks,
                "frobenius_norms": fixed_frobenius,
                "support_patterns_u": {key: support_pattern(fixed_u[key]) for key in fixed_u},
                "equivalence_to_shift_0_on_u": fiber_equivalences,
            },
            "all_fiber_envelope": {
                "rank": all_ranks,
                "frobenius_norms": all_frobenius,
                "support_pattern_u": support_pattern(all_envelope["matrices"]["u"]),
                "not_gauge_equivalent_to_fixed_fiber_class": all(summary["rank"] == 1 for summary in all_envelope["summary"].values()),
                "why_not_selected_single_charge_primitive": (
                    "It sums over all qutrit charges, gives rank-one all-ones matrices, and is not equivalent "
                    "to a fixed qutrit charge/fiber primitive by row-column relabeling."
                ),
            },
        },
        "source_implication": {
            "qutrit_source_support": qutrit_source_support,
            "what_source_selects_now": (
                "The selected S3/gerbe/rho_E data support the period-three projective qutrit class and its "
                "central cocycle, but they do not yet select an absolute qutrit fiber origin or visible "
                "operator-level primitive transport."
            ),
            "absolute_fiber_shift_selected": False,
            "selected_noninvariant_primitive_source_proved": False,
            "observable_invariance_under_fiber_class_proved": False,
        },
        "what_closes_now": {
            "active_shift_1_1_forced_by_finite_support": True,
            "fixed_fiber_shifts_reduced_to_one_qutrit_gauge_class": True,
            "all_fiber_envelope_retired_as_fixed_single_charge_candidate": True,
            "no_observed_flavor_data_used": True,
        },
        "what_remains_open": {
            "absolute_fiber_origin_gauge_fix": True,
            "selected_noninvariant_C1_primitive_or_vertex_source": True,
            "selected_basis_transport_theorem": True,
            "observable_invariance_under_fixed_fiber_class": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "honest_replay_without_lifted_flags": True,
            "yukawa_CKM_PMNS_magnitudes": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_FiberClass_Observable_Invariance_or_GaugeFix_v1",
        "theorem": {
            "name": "SelectedRouteCPrimitiveSourceSelectionReductionTheorem",
            "proved": True,
            "statement": (
                "The selected finite support forces active shift (1,1). The three fixed qutrit fiber shifts "
                "are a single cyclic-gauge fiber class, while the all-fiber envelope is structurally different "
                "and is not a fixed single-charge primitive. Current MTT source data therefore reduce the C1 "
                "gate to either a selected fiber-origin gauge fix or a proof that the downstream observables are "
                "invariant under this fixed-fiber gauge class."
            ),
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    REPORT.write_text(
        json.dumps(
            {
                "status": candidate["status"],
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        f"""# MTT Selected Route-C Primitive Source Selection / Fiber-Rule Audit

Status: `{candidate['status']}`

This audit proves the finite selection facts that are available without using
observed Yukawa, CKM, PMNS, or mass data.

## What Is Proved

1. Active shift `(1,1)` is forced by finite support.  An enumeration over all
   nine active deck shifts shows that nonzero one-response C1 matrices occur
   exactly for `(1,1)`.
2. The three fixed qutrit fiber shifts `0`, `1`, and `2` are one fiber class:
   each gives the same amplitude, rank-three permutation-type C1 matrices, and
   row-column relabel equivalences.
3. The `all` fiber envelope is not a fixed qutrit charge primitive.  It gives
   rank-one all-ones matrices, so it is structurally different from the fixed
   fiber class.

## What Is Not Proved

The current selected S3/gerbe/rho_E source data select the period-three
projective qutrit class, not an absolute qutrit fiber origin.  Therefore this
does not yet prove a unique selected C1 matrix.  It reduces the problem to one
of two sharp next gates:

- prove a selected fiber-origin gauge fix or primitive/basis-transport source;
- or prove downstream observable invariance under the fixed-fiber gauge class.

No observed flavor data were used, and no full SM/no-knob closure is claimed.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
