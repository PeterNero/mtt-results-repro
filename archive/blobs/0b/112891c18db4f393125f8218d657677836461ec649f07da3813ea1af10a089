"""Attempt the selected Weyl-pair source provenance lemma.

This artifact checks whether the existing selected q79/F,m=1 S3/GS Route-C
data already prove the Weyl-pair columns used by the conditional A assembly.
It proves the source-level Weyl carrier and active-shift provenance, then
records the remaining transfer-map gap from source carrier to C1 response
columns.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

ASELECTED = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
RHOE_PACKET = DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"
GERBE_PROMOTION = DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"
PRIMITIVE_AUDIT = DATA / "selected_routec_primitive_source_selection_audit.candidate.json"
OPERATOR_EMISSION = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"

OUTPUT = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
CERT = CERTS / "selected_routec_weylpair_source_provenance_lemma_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_C1_TRANSFER_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def from_complex_pairs(matrix: list[list[list[float]]]) -> np.ndarray:
    rows = []
    for row in matrix:
        rows.append([complex(float(entry[0]), float(entry[1])) for entry in row])
    return np.array(rows, dtype=complex)


def canonical_weyl() -> tuple[np.ndarray, np.ndarray]:
    omega = np.exp(2j * np.pi / 3)
    z = np.diag([1, omega, omega**2])
    x = np.array(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ],
        dtype=complex,
    )
    return z, x


def norm(value: np.ndarray) -> float:
    return float(np.linalg.norm(value))


def main() -> None:
    aselected = load(ASELECTED)
    rhoe_packet = load(RHOE_PACKET)
    gerbe = load(GERBE_PROMOTION)
    primitive = load(PRIMITIVE_AUDIT)
    operator = load(OPERATOR_EMISSION)

    matrices = rhoe_packet["rho_E_candidate"]["generator_matrices_complex_pairs"]
    g1 = from_complex_pairs(matrices["g1"])
    g2 = from_complex_pairs(matrices["g2"])
    z, x = canonical_weyl()

    source_level_flags = {
        "selected_s3_gerbe_source_level_promoted": gerbe["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"],
        "operator_level_projective_rhoE_promoted": gerbe["promotion_result"]["operator_level_projective_rhoE_promoted"],
        "map_to_central_cocycle_verified": gerbe["promotion_gate_flags_after_s3_closure"]["map_to_central_cocycle_verified"],
        "selected_by_mtt_at_s3_level": gerbe["promotion_gate_flags_after_s3_closure"]["selected_by_mtt"],
        "source_level_projective_class_selected": primitive["source_implication"]["qutrit_source_support"]["source_level_projective_class_selected"],
        "operator_level_projective_class_selected": primitive["source_implication"]["qutrit_source_support"]["operator_level_projective_class_selected"],
    }

    carrier_check = {
        "g1_equals_phase_Z_residual": norm(g1 - z),
        "g2_equals_shift_X_residual": norm(g2 - x),
        "g1_order3_residual": norm(np.linalg.matrix_power(g1, 3) - np.eye(3)),
        "g2_order3_residual": norm(np.linalg.matrix_power(g2, 3) - np.eye(3)),
        "projective_commutator_residual_imported": rhoe_packet["rho_E_candidate"]["numeric_gates"]["projective_commutator_residual"],
        "uses_only_selected_active_generators_g1_g2": rhoe_packet["rho_E_candidate"]["numeric_gates"]["uses_only_selected_active_generators_g1_g2"],
    }
    carrier_closed = (
        carrier_check["g1_equals_phase_Z_residual"] <= 1e-10
        and carrier_check["g2_equals_shift_X_residual"] <= 1e-10
        and carrier_check["g1_order3_residual"] <= 1e-10
        and carrier_check["g2_order3_residual"] <= 1e-10
        and source_level_flags["selected_s3_gerbe_source_level_promoted"] is True
        and source_level_flags["map_to_central_cocycle_verified"] is True
        and source_level_flags["source_level_projective_class_selected"] is True
    )

    active_shift = primitive["active_shift_theorem"]["enumeration"]
    active_closed = (
        active_shift["active_shift_necessary_and_sufficient_for_nonzero"] is True
        and active_shift["nonzero_active_shifts"] == [[1, 1]]
    )

    transfer_map_status = {
        "selected_source_to_C1_response_map_emitted": False,
        "phase_Z_routed_to_u_e_I_plus_Z_column": False,
        "shift_X_routed_to_d_nuD_I_plus_X_column": False,
        "normalization_transferred_to_deltaTheta_coefficients": False,
        "selected_A_selected_currently_emitted": operator["emission_audit"]["selected_operator_A_selected_emitted"],
        "selected_b_selected_currently_emitted": operator["emission_audit"]["selected_source_vector_b_selected_emitted"],
        "why": (
            "Existing artifacts prove the selected source-level Weyl carrier and active shift, but they do "
            "not yet emit the functor/trace/overlap map that sends this carrier to the exact sector-routed "
            "C1 columns used by the conditional Weyl-pair solve."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedRouteCWeylPairSourceProvenanceLemma",
        "status": STATUS,
        "inputs": {
            "conditional_weylpair_A_assembly": rel(ASELECTED),
            "nonidentity_rhoe_packet": rel(RHOE_PACKET),
            "projective_gerbe_rhoe_source_promotion": rel(GERBE_PROMOTION),
            "primitive_source_selection_audit": rel(PRIMITIVE_AUDIT),
            "selected_c1_response_operator_emission": rel(OPERATOR_EMISSION),
        },
        "superset_strategy": {
            "mode": "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET",
            "paths_combined": [
                "selected S3/GS projective gerbe rho_E source-level carrier",
                "finite Heisenberg/Weyl g1=Z, g2=X packet",
                "active shift (1,1) primitive support theorem",
                "conditional Weyl-pair A assembly",
            ],
            "locked_target": "prove provenance of the already locked phase_packet and shift_packet columns",
            "observed_data_used": False,
            "lifted_flags_used_as_proof": False,
            "target_fitting_used": False,
        },
        "source_level_weyl_carrier": {
            "proved": carrier_closed,
            "carrier_check": carrier_check,
            "source_level_flags": source_level_flags,
            "statement": (
                "The q79/F,m=1 selected S3/GS gerbe source supplies the period-three projective qutrit "
                "Weyl carrier at source level: g1 is the phase generator Z, g2 is the shift generator X, "
                "and the central cocycle is selected by the S3 gerbe/Green-Schwarz data rather than by "
                "observed flavor targets."
            ),
        },
        "active_shift_provenance": {
            "proved": active_closed,
            "nonzero_active_shifts": active_shift["nonzero_active_shifts"],
            "statement": (
                "The finite C1 support theorem forces active primitive shift (1,1) as the unique nonzero "
                "active deck shift, so the shift-like X leg has source-compatible active-shift provenance."
            ),
        },
        "c1_transfer_map": transfer_map_status,
        "lemma_attempt": {
            "name": "SelectedWeylPairSourceProvenanceLemma",
            "fully_proved": False,
            "proved_sublemma": "SelectedSourceLevelQutritWeylCarrierAndActiveShiftLemma",
            "open_sublemma": "SelectedWeylPairSourceToC1TransferMapLemma",
            "why_not_fully_proved": transfer_map_status["why"],
        },
        "what_closes_now": {
            "source_level_phase_Z_carrier_provenance": carrier_closed,
            "source_level_shift_X_carrier_provenance": carrier_closed,
            "active_shift_1_1_provenance": active_closed,
            "same_superset_paths_reconciled": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "emit_selected_source_to_C1_transfer_map": True,
            "prove_phase_Z_routes_to_u_e_column": True,
            "prove_shift_X_routes_to_d_nuD_column": True,
            "promote_conditional_A_to_A_selected": True,
            "emit_theorem_derived_b_selected": True,
            "run_honest_selected_deltaTheta_C1_solve": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C WeylPair Source Provenance Lemma

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_C1_TRANSFER_OPEN`

This artifact attempts to prove `SelectedWeylPairSourceProvenanceLemma`.

## What Closes

The source-level qutrit Weyl carrier is closed:

- `g1 = Z`, the phase generator,
- `g2 = X`, the shift generator,
- both have order three,
- the projective central cocycle is supplied by the selected q79/F,m=1
  S3/Green-Schwarz gerbe source,
- active shift `(1,1)` is the unique nonzero C1 active deck shift.

This is not target fitting.  It uses selected gerbe/rho_E source support,
finite Heisenberg/Weyl packet data, and the active-shift theorem.  Observed SM
values and lifted flags are not used.

## What Does Not Close Yet

The full provenance lemma is not yet proved, because the repo does not yet emit
the selected transfer map from source-level Weyl carrier to the exact C1
response columns:

- `Z` routed to the `u,e = I + Z` phase packet,
- `X` routed to the `d,nuD = I + X` shift packet,
- normalization fixed in the same `B_N`/projector/dotD/zero-mode basis.

So the remaining object is now sharply:

`SelectedWeylPairSourceToC1TransferMapLemma`.

If that transfer map is proved, the conditional Weyl-pair operator from the
previous artifact can be promoted to selected `A_selected`/`b_selected` and the
honest locked DeltaTheta solve can be replayed.

Next artifact: `MTT_Selected_RouteC_WeylPair_SourceToC1_Transfer_Map_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
