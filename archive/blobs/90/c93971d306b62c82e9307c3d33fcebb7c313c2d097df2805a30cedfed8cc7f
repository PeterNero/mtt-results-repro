"""Attempt the End(E)->B_N label embedding or smooth transition/connection value packet."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "source_lift": DATA / "selected_heterotic_finiteinternalrhoe_to_phifin_or_smoothbundleconnection_sourcelift.candidate.json",
    "required_packet": DATA / "selected_heterotic_finiteinternalrhoe_to_phifin_or_smoothbundleconnection_sourcelift_required_packet.json",
    "finite_internal_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "trace_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "spectrum_27mode": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.spectrum_attempt.json",
    "formal_transition_values": DATA / "selected_heterotic_projectiverhoe_formal_flattorsion_projective_transition_values.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_ende_to_bn_labelembedding_or_smoothtransitionconnection_valuepacket.candidate.json"
OUTPUT_VALUES = DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json"
OUTPUT_CERT = CERTS / "selected_heterotic_ende_to_bn_labelembedding_or_smoothtransitionconnection_valuepacket_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_EndE_to_BN_LabelEmbedding_or_SmoothTransitionConnection_ValuePacket_v1.md"

STATUS = "HETEROTIC_ENDE_TO_BN_LABELEMBEDDING_ATTEMPT_RHOE_INTERTWINES_DE_FINITEPART_OPEN"
NEXT = "Selected_Heterotic_EndE_to_BN_OperatorIntertwiner_or_SmoothConnection_SourceAmendment_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def bn_index(m: int, n: int, r: int) -> int:
    return 3 * (3 * m + n) + r


def basis_label(m: int, n: int, r: int) -> str:
    return f"e_m{m}_n{n}_r{r}"


def main() -> dict[str, Any]:
    source_lift = load(INPUTS["source_lift"])
    required = load(INPUTS["required_packet"])
    finite = load(INPUTS["finite_internal_packet"])
    trace_27 = load(INPUTS["trace_27mode"])
    spectrum_27 = load(INPUTS["spectrum_27mode"])
    formal_transition = load(INPUTS["formal_transition_values"])

    labels = finite["labels"]
    tau = {label: int(value) for label, value in finite["tau_values"].items()}
    tau_mod = {label: tau[label] % 3 for label in labels}
    modes_by_rank = {0: [], 1: [], 2: []}
    for m in range(3):
        for n in range(3):
            for r in range(3):
                modes_by_rank[r].append((m, n, r))

    counters = {0: 0, 1: 0, 2: 0}
    embedding_rows: dict[str, dict[str, Any]] = {}
    matrix = [[0 for _ in labels] for _ in range(27)]
    for col, label in enumerate(labels):
        r = tau_mod[label]
        m, n, rank = modes_by_rank[r][counters[r]]
        counters[r] += 1
        row = bn_index(m, n, rank)
        matrix[row][col] = 1
        embedding_rows[label] = {
            "label": label,
            "tau": tau[label],
            "tau_mod3": r,
            "BN_mode": {"m": m, "n": n, "rank_slot": rank, "row": row, "basis_label": basis_label(m, n, rank)},
            "rho_internal": f"zeta_3^{r}",
            "rho_BN_rank_slot": f"zeta_3^{rank}",
            "rho_intertwines": r == rank,
            "laplacian_eigenvalue_unit_multiple": m * m + n * n,
        }

    used_rows = [item["BN_mode"]["row"] for item in embedding_rows.values()]
    column_norms = [sum(matrix[row][col] * matrix[row][col] for row in range(27)) for col in range(11)]
    row_multiplicities = {row: used_rows.count(row) for row in used_rows}
    projection_pair_checks = {
        "matrix_shape": [27, 11],
        "unique_rows": len(set(used_rows)) == len(used_rows),
        "column_norms_all_one": all(value == 1 for value in column_norms),
        "P_transpose_P_equals_identity_11": len(set(used_rows)) == len(used_rows) and all(value == 1 for value in column_norms),
        "P_P_transpose_rank": len(set(used_rows)),
        "row_multiplicities": row_multiplicities,
    }

    rho_checks = {
        "all_labels_preserve_tau_mod3_rank_slot": all(row["rho_intertwines"] for row in embedding_rows.values()),
        "product_cancellation_retained": formal_transition["all_products_cancel_to_P"],
        "triple_tau_shadow_retained": formal_transition["all_triples_match_tau"],
    }

    de_checks_by_label = {}
    for label, row in embedding_rows.items():
        internal = tau[label]
        lap_mult = row["laplacian_eigenvalue_unit_multiple"]
        de_checks_by_label[label] = {
            "internal_D_E_tau": internal,
            "BN_scalar_laplacian_unit_multiple": lap_mult,
            "intertwines_without_rescale_or_shift": internal == lap_mult,
        }
    de_intertwines = all(item["intertwines_without_rescale_or_shift"] for item in de_checks_by_label.values())

    finitepart_checks = {
        "internal_logdet": "log(2008)",
        "BN_positive_complement_logdet": spectrum_27["conditional_zeta_logdet_positive_complement"]["formula"],
        "numeric_internal_logdet": math.log(2008),
        "numeric_BN_positive_complement_logdet": spectrum_27["conditional_zeta_logdet_positive_complement"]["numeric"],
        "same_finitepart": False,
        "reason": "The sparse phase-preserving injection does not identify the internal H_sel determinant with the full 27-mode positive complement determinant.",
    }

    label_embedding_attempt = {
        "schema": "SelectedHeteroticEndEtoBN.LabelEmbeddingCandidate.v1",
        "status": "CANDIDATE_VALUES_BUILT_RHOE_ONLY_NOT_OPERATOR_INTERTWINER",
        "basis_id": trace_27["finite_trace_route"]["gap_layer"]["basis_id"],
        "domain_labels": labels,
        "embedding_matrix_27x11": matrix,
        "embedding_rows": embedding_rows,
        "projection_pair_checks": projection_pair_checks,
        "rho_checks": rho_checks,
        "D_E_intertwiner_checks": {
            "intertwines": de_intertwines,
            "by_label": de_checks_by_label,
            "reason_open": "The BN D_E layer is the nonnegative Fourier Laplacian/gap operator, while the internal D_E is the signed central-character/tau operator.",
        },
        "finitepart_checks": finitepart_checks,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_VALUES.write_text(json.dumps(label_embedding_attempt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    smooth_lane = {
        "attempted": False,
        "reason": "No new smooth transition, connection, curvature, representation action, trace, quotient, or E_Qa values are emitted by the current source record.",
        "required_values_still_open": required["lane_B_smooth_bundle_or_transition_lift"],
    }

    decision = {
        "valuepacket_attempted": True,
        "label_embedding_candidate_built": True,
        "rhoE_character_intertwines": rho_checks["all_labels_preserve_tau_mod3_rank_slot"],
        "projection_pair_candidate_valid_as_injection": projection_pair_checks["P_transpose_P_equals_identity_11"],
        "D_E_or_EQa_intertwines": de_intertwines,
        "Riesz_Green_gap_transfers": False,
        "finitepart_regularization_same_scheme": False,
        "smooth_transition_connection_values_emitted": False,
        "E_Qa_computed": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
        "values_path": rel(OUTPUT_VALUES),
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticEndEtoBNLabelEmbeddingOrSmoothTransitionConnectionValuePacket",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "input_statuses": {
            "source_lift": source_lift["status"],
            "required_packet": required["status"],
            "finite_internal_packet": finite["schema"],
            "trace_27mode": trace_27["status"],
            "spectrum_27mode": spectrum_27["schema"],
            "formal_transition_values": formal_transition["status"],
        },
        "label_embedding_attempt_path": rel(OUTPUT_VALUES),
        "smooth_transition_connection_lane": smooth_lane,
        "decision": decision,
        "guardrails": {
            "does_not_promote_phase_embedding_to_operator_intertwiner": True,
            "does_not_promote_BN_laplacian_as_internal_DE": True,
            "does_not_promote_BN_logdet_as_internal_logdet": True,
            "does_not_emit_smooth_A_or_FA": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "LabelEmbeddingAttemptRhoEOnlyNoOperatorIntertwiner",
            "proved": True,
            "statement": (
                "A canonical sparse 27x11 phase-preserving injection can be built by "
                "placing each internal label into a B_N rank slot with the same "
                "tau mod 3 phase. This gives a valid algebraic rho_E character "
                "intertwiner and an injective projection pair, but it does not "
                "intertwine the signed internal tau/D_E operator with the selected "
                "nonnegative 27-mode Fourier Laplacian D_E layer, nor does it "
                "identify the finite parts. Therefore the candidate is useful as "
                "a rho_E shadow, not as heterotic Phi_fin closure."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "values_path": rel(OUTPUT_VALUES),
        "note_path": rel(OUTPUT_NOTE),
        "label_embedding_candidate_built": True,
        "rhoE_character_intertwines": True,
        "D_E_or_EQa_intertwines": False,
        "finitepart_regularization_same_scheme": False,
        "smooth_transition_connection_values_emitted": False,
        "E_Qa_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic EndE to BN LabelEmbedding or SmoothTransitionConnection ValuePacket v1

## Result

```text
status = {STATUS}
label_embedding_candidate_built = true
rhoE_character_intertwines = true
D_E_or_EQa_intertwines = false
finitepart_regularization_same_scheme = false
next_required_artifact = {NEXT}
```

## Candidate Built

The attempted `27 x 11` injection places each internal label into a unique
`F3xF3`/rank mode whose rank slot has the same `tau mod 3` phase. This is a
real algebraic advance: it preserves the `rho_E` central character and gives
`P^T P = I_11`.

It still fails as a full source lift. The internal operator is the signed
`tau`/central-character operator, while the selected `Phi_fin` layer is the
nonnegative Fourier Laplacian/gap operator. The finite parts also remain
different: internal `log(2008)` is not the 27-mode positive-complement logdet.

## Values

```text
{rel(OUTPUT_VALUES)}
```

## Theorem

{candidate["theorem"]["statement"]}
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_VALUES)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
