"""Emit the finite HYM-projector zero-mode value packet, with guardrails.

The previous theorem proved that same-source selected HYM/Strominger Riesz
projectors would promote rho_candidate to selected rho_s.  This step gathers
the strongest finite value data currently in the repo: the smooth B_N
projectors, ordered zero-mode bases, positive gap, and induced End0 action.

It does not promote the values to selected physical HYM projectors.  The
available finite data are the model-active B_N/Route-C scaffold and the honest
packets keep their selected-source flags false.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

BRIDGE = DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"
SOURCE_PAYLOAD = DATA / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json"
SMOOTH_BN = DATA / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DE_SUMMARY = DATA / "selected_routec_de_action_on_smooth_bn.candidate.json"
DE_HONEST = DATA / "selected_routec_de_action_on_smooth_bn" / "de_action_on_smooth_bn.honest.json"
DOTD_SUMMARY = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
DOTD_HONEST = (
    DATA
    / "selected_routec_sector_projectors_dotd_on_smooth_bn"
    / "sector_projectors_dotd_on_smooth_bn.honest.json"
)

OUTPUT = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
CERT = CERTS / "selected_hym_projector_zeromode_basis_value_emission_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYM_Projector_ZeroModeBasis_Value_Emission_v1.md"

STATUS = "MTT_SELECTED_HYM_PROJECTOR_ZEROMODE_VALUES_EMITTED_MODEL_ACTIVE_NOT_SELECTED"
NEXT = "MTT_Selected_HYM_Projector_SourcePromotion_or_FullStrominger_Operator_Value_Theorem_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]
ALL_SECTORS = MATTER_SECTORS + ["H"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def max_abs_diff(left: list[list[float]], right: list[list[float]]) -> float:
    return max(
        abs(left[i][j] - right[i][j])
        for i in range(len(left))
        for j in range(len(left[0]))
    )


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*matrix)]


def trace(matrix: list[list[float]]) -> float:
    return sum(matrix[i][i] for i in range(len(matrix)))


def embed_on_indices(
    small: list[list[float]], dimension: int, indices: list[int]
) -> list[list[float]]:
    out = [[0.0 for _ in range(dimension)] for _ in range(dimension)]
    for row, i in enumerate(indices):
        for col, j in enumerate(indices):
            out[i][j] = float(small[row][col])
    return out


def projector_checks(projector: list[list[float]]) -> dict[str, float]:
    return {
        "rank_trace": trace(projector),
        "idempotence_residual": max_abs_diff(matmul(projector, projector), projector),
        "self_adjoint_residual": max_abs_diff(transpose(projector), projector),
    }


def commutator_residual(projector: list[list[float]], action: list[list[float]]) -> float:
    return max_abs_diff(matmul(projector, action), matmul(action, projector))


def sector_slot(
    sector: str,
    *,
    bn: dict[str, Any],
    dotd: dict[str, Any],
    rho_candidate: dict[str, Any],
) -> dict[str, Any]:
    lift = bn["B_N_lift"]
    dimension = lift["dimension"]
    zero_cluster = lift["zero_cluster"]
    dotd_slot = dotd["dotd_response_slots"][sector]
    projector = dotd["sector_projectors_on_BN"][sector]["projector_matrix"]
    if sector == "H":
        basis_indices = [zero_cluster["indices"][0]]
        basis_ids = [zero_cluster["basis_ids"][0]]
        embedded_actions = {"T1": [[0.0] * dimension for _ in range(dimension)]}
        embedded_actions["T2"] = [[0.0] * dimension for _ in range(dimension)]
        embedded_actions["T3"] = [[0.0] * dimension for _ in range(dimension)]
    else:
        basis_indices = zero_cluster["indices"]
        basis_ids = zero_cluster["basis_ids"]
        embedded_actions = {
            name: embed_on_indices(matrix, dimension, basis_indices)
            for name, matrix in rho_candidate[sector]["rho"].items()
        }

    equivariance = {
        name: commutator_residual(projector, action)
        for name, action in embedded_actions.items()
    }
    checks = projector_checks(projector)
    return {
        "sector": sector,
        "basis_id": lift["basis_id"],
        "carrier_kind": "trivial_higgs_singlet" if sector == "H" else "End0_adjoint_triplet",
        "ambient_dimension": dimension,
        "ordered_zero_mode_basis_ids": basis_ids,
        "ordered_zero_mode_basis_indices": basis_indices,
        "ordered_zero_mode_basis_vector_count": len(dotd_slot["ordered_zero_mode_basis"]),
        "expected_rank": 1 if sector == "H" else 3,
        "projector_checks": checks,
        "End0_equivariance_residuals_on_emitted_projector": equivariance,
        "green_operator_verified": dotd_slot["green_operator_verified"],
        "horizontal_gauge_verified": dotd_slot["horizontal_gauge_verified"],
        "selected_source_verified": False,
        "value_emitted_as_selected_HYM_projector": False,
    }


def main() -> int:
    bridge = load(BRIDGE)
    source_payload = load(SOURCE_PAYLOAD)
    bn = load(SMOOTH_BN)
    de_summary = load(DE_SUMMARY)
    de_honest = load(DE_HONEST)
    dotd_summary = load(DOTD_SUMMARY)
    dotd_honest = load(DOTD_HONEST)

    rho_candidate = source_payload["source_map_candidate"]["rho_candidate"]
    sector_slots = {
        sector: sector_slot(sector, bn=bn, dotd=dotd_honest, rho_candidate=rho_candidate)
        for sector in ALL_SECTORS
    }

    all_projector_checks_pass = all(
        slot["projector_checks"]["idempotence_residual"] == 0.0
        and slot["projector_checks"]["self_adjoint_residual"] == 0.0
        and slot["projector_checks"]["rank_trace"] == slot["expected_rank"]
        for slot in sector_slots.values()
    )
    all_equivariance_passes = all(
        all(value == 0.0 for value in slot["End0_equivariance_residuals_on_emitted_projector"].values())
        for slot in sector_slots.values()
    )
    all_basis_counts_pass = all(
        slot["ordered_zero_mode_basis_vector_count"] == slot["expected_rank"]
        for slot in sector_slots.values()
    )

    selected_source_flags = {
        "de_action_selected_source_verified": bool(de_honest["selected_source_verified"]),
        "dotd_selected_dotD_source_verified": bool(dotd_honest["selected_dotD_source_verified"]),
        "dotd_alpha1_driver_verified": bool(dotd_honest["alpha1_driver_verified"]),
        "de_honest_validator_promotes": de_summary["validation"]["honest"]["exit_code"] == 0,
        "dotd_honest_validator_promotes": dotd_summary["validation"]["honest"]["exit_code"] == 0,
    }

    finite_value_payload = {
        "basis_id": bn["B_N_lift"]["basis_id"],
        "ambient_dimension": bn["B_N_lift"]["dimension"],
        "zero_cluster": bn["B_N_lift"]["zero_cluster"],
        "complement_gap": bn["B_N_lift"]["complement_gap"],
        "quadrature_rule": {
            "rule": bn["B_N_lift"]["quadrature_rule"]["rule"],
            "normalization": bn["B_N_lift"]["quadrature_rule"]["normalization"],
            "exact_for_mode_differences_mod_3": bn["B_N_lift"]["quadrature_rule"][
                "exact_for_mode_differences_mod_3"
            ],
        },
        "bundle_equivariance": bn["B_N_lift"]["bundle_equivariance"],
        "sector_slots": sector_slots,
        "payload_paths": {
            "smooth_bn": rel(SMOOTH_BN),
            "de_honest": rel(DE_HONEST),
            "dotd_honest": rel(DOTD_HONEST),
        },
    }

    validator_result = {
        "finite_projector_values_emitted": True,
        "all_projector_checks_pass": all_projector_checks_pass,
        "all_basis_counts_pass": all_basis_counts_pass,
        "positive_complement_gap": bn["B_N_lift"]["complement_gap"] > 0.0,
        "End0_equivariance_on_emitted_projectors": all_equivariance_passes,
        "green_and_horizontal_flags_pass": all(
            slot["green_operator_verified"] and slot["horizontal_gauge_verified"]
            for slot in sector_slots.values()
        ),
        "selected_source_flags": selected_source_flags,
        "selected_HYM_projector_values_promoted": False,
        "rho_candidate_promoted_to_selected_rho_s": False,
        "passes_bridge_validator_now": False,
        "why_not_promoted": [
            "the values are emitted on the model-active smooth B_N scaffold, not as theorem-derived selected HYM/Strominger projectors",
            "honest D_E selected_source_verified is false",
            "honest dotD selected_dotD_source_verified and alpha1_driver_verified are false",
            "the current D_E is not yet the full selected Iwasawa/Strominger operator with truncation-error certificate",
            "therefore the previous bridge theorem cannot yet promote rho_candidate to selected rho_s",
        ],
    }

    superset_strategy = {
        "classification": "SUPERSET_VALUE_EXTRACTION_WITH_SOURCE_PROMOTION_BLOCKED",
        "straight_End0_path": {
            "used_for": "finite rho_candidate action and End0-equivariance checks on the emitted zero cluster",
            "status": "passes on the emitted model-active projectors",
        },
        "RouteC_BN_path": {
            "used_for": "explicit 27-mode basis, projectors, zero-mode basis ids, positive gap, Green/dotD consistency",
            "status": "finite values emitted but selected-source flags remain false",
        },
        "HYM_Strominger_path": {
            "used_for": "required source of physical selected projectors",
            "status": "not yet emitted as full selected HYM/Strominger values",
        },
        "SU5_E6_q79_theta_path": {
            "used_for": "matter-slot routing constraints downstream of rho_s",
            "status": "kept as constraints; not used to select these projector values",
        },
        "locked_target": "promote these clean finite projector values only after selected HYM/source theorem supplies provenance",
        "uses_observed_constants": False,
    }

    data = {
        "candidate": "MTTSelectedHYMProjectorZeroModeBasisValueEmission",
        "status": STATUS,
        "inputs": {
            "bridge": rel(BRIDGE),
            "source_payload": rel(SOURCE_PAYLOAD),
            "smooth_bn": rel(SMOOTH_BN),
            "de_summary": rel(DE_SUMMARY),
            "de_honest": rel(DE_HONEST),
            "dotd_summary": rel(DOTD_SUMMARY),
            "dotd_honest": rel(DOTD_HONEST),
        },
        "finite_value_payload": finite_value_payload,
        "validator_result": validator_result,
        "bridge_import": {
            "bridge_theorem_proved": bridge["theorem"]["bridge_theorem_proved"],
            "bridge_requires_selected_values": bridge["theorem"]["selected_values_emitted"] is False,
            "previous_next_required_artifact": bridge["next_required_artifact"],
        },
        "superset_strategy": superset_strategy,
        "what_closes_now": {
            "finite_model_active_projector_values_emitted": True,
            "ordered_zero_mode_basis_ids_emitted": True,
            "rank_3_matter_rank_1_H_projectors_verified": all_projector_checks_pass,
            "positive_model_complement_gap_emitted": bn["B_N_lift"]["complement_gap"] > 0.0,
            "End0_equivariance_on_emitted_projectors_verified": all_equivariance_passes,
            "rho_candidate_projection_formula_ready": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_HYM_projector_source_promotion": True,
            "full_selected_iwasawa_strominger_operator_values": True,
            "selected_rho_s_actual_promotion": True,
            "selected_matter_slot_routing": True,
            "selected_physical_dotD_alpha1": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_HYM_Projector_ZeroModeBasis_Value_Emission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "finite_projector_values_emitted": True,
        "selected_HYM_projector_values_promoted": False,
        "selected_rho_s_promoted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected HYM Projector ZeroModeBasis Value Emission v1

Status: `{STATUS}`.

## What Was Emitted

The current repo already emits a concrete finite value packet on the smooth
`B_N` scaffold:

```text
ambient dimension = {bn["B_N_lift"]["dimension"]}
zero cluster = {bn["B_N_lift"]["zero_cluster"]["basis_ids"]}
matter ranks = 3 for Q,u,d,L,e,N
Higgs rank = 1
model complement gap = {bn["B_N_lift"]["complement_gap"]}
```

The projectors are self-adjoint idempotents, have the expected ranks, and the
embedded `End0(V_alpha)` adjoint action commutes with them on the emitted zero
cluster.  Thus the finite `rho_candidate -> K_s` formula is ready at the
model-active value level.

## Why This Still Does Not Promote `rho_s`

The value packet is not yet a selected physical HYM projector packet.  The
honest `D_E` and `dotD` payloads still have:

```text
selected_source_verified = false
selected_dotD_source_verified = false
alpha1_driver_verified = false
```

So the bridge theorem from the previous artifact cannot yet promote
`rho_candidate` to selected `rho_s`.

## Superset Use

This is a constrained superset extraction:

- straight `End0` supplies `rho_candidate` and the equivariance checks,
- Route-C/`B_N` supplies explicit finite projectors, bases, gap, and Green data,
- HYM/Strominger remains the required source-promotion path,
- SU(5)/E6, q79/S3/gerbe, and Theta/Weyl-pair data stay downstream constraints,
  not selectors for these projector values.

No observed constants, benchmark matrices, or fitted residuals are used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
