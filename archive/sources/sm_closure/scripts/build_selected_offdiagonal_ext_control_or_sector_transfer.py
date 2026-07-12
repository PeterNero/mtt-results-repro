"""Build the off-diagonal Ext control / sector-transfer next gate."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_offdiagonal_ext_control_or_sector_transfer_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_OffDiagonal_Ext_Control_or_SectorTransfer_From_Full_Diagonal_End0_Green_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*matrix)]


def subtract(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def trace_pair(matrix: list[list[float]], basis: list[list[float]]) -> float:
    return sum(matrix[i][j] * basis[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])))


def main() -> int:
    green_path = ROOT / "candidate_data" / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
    overlap_path = ROOT / "candidate_data" / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
    q79_alpha_path = Q79 / "candidate_data" / "q79_selected_phifin_alpha1_payload.candidate.json"

    green = load(green_path)
    overlap = load(overlap_path)
    q79_alpha = load(q79_alpha_path) if q79_alpha_path.exists() else {}

    # Real rank-2 row-model matrices. The selected Ext representative is the
    # single nilpotent row E12; its metric adjoint is proportional to E21.
    e12 = [[0.0, 1.0], [0.0, 0.0]]
    e21 = transpose(e12)
    comm = subtract(matmul(e12, e21), matmul(e21, e12))
    t1 = [[0.0, 1.0], [1.0, 0.0]]
    t2 = [[0.0, -1.0], [1.0, 0.0]]
    t3 = [[1.0, 0.0], [0.0, -1.0]]
    projections = {
        "T1_trace_pairing": trace_pair(comm, t1),
        "T2_trace_pairing": trace_pair(comm, t2),
        "T3_trace_pairing": trace_pair(comm, t3),
    }
    offdiag_source_zero = abs(projections["T1_trace_pairing"]) < 1e-14 and abs(projections["T2_trace_pairing"]) < 1e-14
    diagonal_source_nonzero = abs(projections["T3_trace_pairing"]) > 0

    full_diagonal_green_closed = green["operator_payload_boundary"]["full_End0_Riesz_Green_extracted"] is True
    row_hodge_support = overlap["global_Dolbeault_harmonic_representative"]["closed_at_row_level"] is True
    row_model_offdiag_control_closed = full_diagonal_green_closed and row_hodge_support and offdiag_source_zero and diagonal_source_nonzero

    q79_gate = q79_alpha.get("closure_gate_table", {}) if q79_alpha else {}
    q79_flags = q79_gate.get("selected_payload_flags", {})
    q79_contract = q79_gate.get("selected_payload_contract", {})
    q79_supports_same_missing_gate = bool(
        q79_flags
        and q79_flags.get("de_action_selected_source") is False
        and q79_flags.get("dotd_selected_source") is False
        and "selected dotD_alpha1 as the same-branch derivative of selected D_E" in q79_contract.get("must_emit", [])
    )

    sector_transfer_closed = False

    candidate = {
        "candidate": "MTTSelectedOffDiagonalExtControlOrSectorTransfer",
        "status": "MTT_SELECTED_ROW_MODEL_OFFDIAGONAL_EXT_CONTROL_CLOSED_SECTOR_TRANSFER_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "full_diagonal_End0_Green": str(green_path),
            "eta00_overlap_Hodge_projector_table": str(overlap_path),
            "q79_alpha1_payload_progress": str(q79_alpha_path) if q79_alpha_path.exists() else None,
        },
        "path_A_straight_offdiagonal_Ext_control": {
            "closed": row_model_offdiag_control_closed,
            "scope": "selected eta_00 single-row rank-2 HYM row model",
            "selected_Ext_matrix": "E12",
            "metric_adjoint_matrix": "proportional to E21 under H=diag(exp(u),exp(-u))",
            "commutator": comm,
            "trace_pairings": projections,
            "conclusion": "The Ext moment-map source has no T1/T2 component and lands entirely in the diagonal Cartan T3 lane.",
            "uses_full_diagonal_End0_Green": full_diagonal_green_closed,
            "external_inspiration": [
                "Kobayashi-Hitchin/Donaldson-Uhlenbeck-Yau: stability gives HYM existence, but not finite selected matrices.",
                "Gauduchon/Li-Yau extension: the existence bridge is compatible with the non-Kahler corpus lane, but this artifact uses explicit row algebra for payload control.",
            ],
        },
        "path_B_superset_sector_transfer": {
            "closed": sector_transfer_closed,
            "q79_progress_imported": bool(q79_alpha),
            "q79_supports_same_missing_gate": q79_supports_same_missing_gate,
            "why_not_closed": "q79 now points at the same selected D_E/Riesz/Green/dotD and alpha1-driver gate, but its selected payload flags remain false; importing it would be a support path, not a theorem-derived sector transfer.",
            "required_to_close": [
                "selected End0-to-sector routing values",
                "selected physical dotD_alpha1 as same-branch derivative of selected D_E",
                "selected source flags true by theorem, not diagnostic lift",
            ],
        },
        "operator_payload_boundary": {
            "row_model_offdiagonal_T1T2_source_controlled": row_model_offdiag_control_closed,
            "full_diagonal_End0_Riesz_Green_available": full_diagonal_green_closed,
            "physical_dotD_alpha1_payload_extracted": False,
            "rank2_to_rank3_sector_transfer_values_extracted": False,
            "validator_ready": False,
            "why_not_validator_ready": "The selected row-model offdiagonal Ext source is controlled, but physical sector transfer and dotD_alpha1 values are still missing.",
        },
        "what_closes_now": {
            "offdiagonal_Ext_source_has_zero_T1_T2_projection_in_selected_row_model": row_model_offdiag_control_closed,
            "diagonal_T3_lane_is_the_only_Ext_moment_map_source": row_model_offdiag_control_closed,
            "full_diagonal_End0_Green_suffices_for_selected_row_model_HYM_replay": row_model_offdiag_control_closed,
            "cross_repo_q79_progress_imported_as_support_only": bool(q79_alpha),
        },
        "what_remains_open": {
            "physical_dotD_alpha1_same_branch_driver": True,
            "rank2_to_rank3_sector_transfer_values": True,
            "full_AH_Cech_offdiagonal_control_beyond_single_row_model": True,
            "validator_ready_sector_D_E_Riesz_Green_dotD": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_path": "Use selected rank-2 row algebra: E12/E21 commutator is Cartan, so T1/T2 offdiagonal source vanishes.",
            "support_path": "Import q79/constant-repo progress only as convergence evidence for the same missing D_E/dotD/alpha1 gate; do not promote selected flags.",
            "locked_target": "selected eta_00 row, diagonal HYM/End0 Green, no measured constants.",
            "not_used": "No observed masses, mixings, couplings, benchmark matrices, inverse-search targets, or lifted selected flags.",
        },
        "next_required_artifact": "MTT_Selected_Physical_dotD_alpha1_or_End0_to_Sector_Routing_v1",
    }

    cert = {
        "certificate": "MTT_Selected_OffDiagonal_Ext_Control_or_SectorTransfer_From_Full_Diagonal_End0_Green_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "row_model_offdiagonal_control_closed": row_model_offdiag_control_closed,
        "sector_transfer_closed": sector_transfer_closed,
        "physical_dotD_alpha1_payload_extracted": False,
        "validator_ready": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = f"""# MTT Selected OffDiagonal Ext Control or SectorTransfer From Full Diagonal End0 Green v1

## Path A: Straight Row-Model Control

For the selected single Ext row, the off-diagonal representative is `E12` and
its metric adjoint is proportional to `E21`.  The moment-map commutator is:

```text
[E12,E21] = {comm}
```

Its trace pairings are:

```text
T1: {projections["T1_trace_pairing"]}
T2: {projections["T2_trace_pairing"]}
T3: {projections["T3_trace_pairing"]}
```

So the selected Ext source has zero `T1/T2` projection and lands in the
diagonal `T3` lane already solved by the diagonal HYM replay and full diagonal
End0 Green packet.

## Path B: Superset Sector Transfer

The q79/constant-repo progress supports the same missing gate, but does not
close it here: selected `D_E`, `Riesz/Green`, `dotD_alpha1`, and sector-routing
flags are still not theorem-derived.

## Guardrail

This closes off-diagonal control only in the selected `eta_00` row model.  It
does not yet emit physical `dotD_alpha1`, selected End0-to-sector routing, or
full validator-ready SM-sector data.

## Next Artifact

`MTT_Selected_Physical_dotD_alpha1_or_End0_to_Sector_Routing_v1`.
"""

    OUT_CANDIDATE.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_PROOF.write_text(proof, encoding="utf-8")
    print(f"Wrote {OUT_CANDIDATE}")
    print(f"Wrote {OUT_CERT}")
    print(f"Wrote {OUT_PROOF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
