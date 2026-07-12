from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

SOURCE_THEOREM = ROOT / "certificates" / "selected_gr_hessian_block_source_theorem_certificate.json"
SHARED_LEDGER = Q79 / "certificates" / "shared_knob_cross_encoding_ledger_certificate.json"
OUT_DATA = ROOT / "candidate_data" / "minimal_cln_gr_hessian_candidate.json"
OUT_CERT = ROOT / "certificates" / "minimal_cln_gr_hessian_candidate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*a)]


def diag(values: list[float]) -> list[list[float]]:
    return [
        [value if i == j else 0.0 for j in range(len(values))]
        for i, value in enumerate(values)
    ]


def eigenvalues_of_diagonal_matrix(a: list[list[float]]) -> list[float]:
    off_diag = [
        abs(a[i][j])
        for i in range(len(a))
        for j in range(len(a))
        if i != j
    ]
    if any(value > 1e-12 for value in off_diag):
        raise ValueError("this verifier only accepts the explicitly diagonal candidate")
    return [a[i][i] for i in range(len(a))]


def lambda_floor_from_shared_ledger() -> float:
    ledger = load_json(SHARED_LEDGER)
    for row in ledger["shared_knobs"]:
        if row["id"] == "theta_overlap_scaffold":
            return float(row["selected_data"]["lambda_star_floor"])
    raise KeyError("theta_overlap_scaffold not found")


def main() -> None:
    source_theorem = load_json(SOURCE_THEOREM)
    lambda_floor = lambda_floor_from_shared_ledger()

    closure_basis = [
        "circle_loop_return",
        "lens_shear_plus",
        "lens_shear_cross",
        "nil_trace_barrier",
        "proto_time_order_strain",
        "radial_volume_strain",
    ]
    response_basis = [
        "h_TT_plus",
        "h_TT_cross",
        "gauge_diffeomorphism_0",
        "gauge_diffeomorphism_1",
        "gauge_diffeomorphism_2",
        "gauge_diffeomorphism_3",
    ]

    h_anchor_weights = {
        "circle_loop_return": 1.0,
        "lens_shear_plus": 1.0,
        "lens_shear_cross": 1.0,
        "nil_trace_barrier": 2.0,
        "proto_time_order_strain": 1.0,
        "radial_volume_strain": 1.0,
    }
    h_anchor = diag([h_anchor_weights[label] for label in closure_basis])

    # P_GR maps response coordinates into closure-strain coordinates. The minimal
    # shear-only ansatz says the two TT polarizations are exactly the two lens
    # shear strains. Gauge directions are pure redundancy and map to zero.
    p_gr = [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ]

    k_gr = matmul(transpose(p_gr), matmul(h_anchor, p_gr))
    eig = eigenvalues_of_diagonal_matrix(k_gr)
    tt_eig = eig[:2]
    gauge_eig = eig[2:]
    tau0_candidate = 1.0 / lambda_floor

    candidate = {
        "certificate": "MinimalCLNGRHessianCandidateData",
        "status": "FORMAL_CANDIDATE_ONLY_SOURCE_SELECTION_OPEN",
        "closure_basis_labels": closure_basis,
        "response_basis_labels": response_basis,
        "H_anchor": {
            "matrix": h_anchor,
            "weights": h_anchor_weights,
            "selection_status": "ROLE_NORMALIZED_ANSATZ_NOT_SOURCE_CERTIFIED",
        },
        "P_GR": {
            "matrix": p_gr,
            "interpretation": "TT metric shear is carried by the two lens shear strains; gauge directions map to zero.",
            "selection_status": "MINIMAL_CLN_ANSATZ_NOT_SOURCE_CERTIFIED",
        },
        "K_GR": {
            "formula": "P_GR^T H_anchor P_GR",
            "matrix": k_gr,
            "tt_eigenvalues": tt_eig,
            "gauge_eigenvalues": gauge_eig,
        },
        "retarded_measure_candidate": {
            "type": "single-atom proper-time ansatz",
            "atoms": [{"tau": tau0_candidate, "weight": 1.0}],
            "lambda_star_floor": lambda_floor,
            "normalization": "F(0)=1",
            "selection_status": "USES_SHARED_SCAFFOLD_FLOOR_NOT_SELECTED_GR_MEASURE",
        },
    }
    OUT_DATA.write_text(json.dumps(candidate, indent=2), encoding="utf-8")

    checks = {
        "source_theorem_target_closed_source_open": source_theorem["status"]
        == "SELECTED_GR_HESSIAN_BLOCK_SOURCE_THEOREM_TARGET_CLOSED_SOURCE_OPEN",
        "h_anchor_symmetric": h_anchor == transpose(h_anchor),
        "h_anchor_positive": all(value > 0.0 for value in h_anchor_weights.values()),
        "k_gr_symmetric": k_gr == transpose(k_gr),
        "tt_block_positive": all(value > 0.0 for value in tt_eig),
        "gauge_block_null": all(abs(value) < 1e-12 for value in gauge_eig),
        "no_tt_mixing": abs(k_gr[0][1]) < 1e-12 and abs(k_gr[1][0]) < 1e-12,
        "retarded_atom_positive": tau0_candidate > 0.0,
    }

    cert = {
        "certificate": "MinimalCLNGRHessianCandidateCertificate",
        "status": "MINIMAL_CLN_GR_HESSIAN_FORMAL_CANDIDATE_PASSES_SOURCE_OPEN",
        "purpose": "Test the smallest circle/lens/nil finite ansatz for a GR TT response block.",
        "candidate_data": str(OUT_DATA),
        "source_theorem": str(SOURCE_THEOREM),
        "checks": checks,
        "formal_result": {
            "K_GR_rank": sum(1 for value in eig if abs(value) > 1e-12),
            "physical_TT_rank": 2,
            "gauge_nullity": 4,
            "candidate_matches_required_rank_pattern": sum(1 for value in eig if abs(value) > 1e-12) == 2
            and all(value > 0.0 for value in tt_eig)
            and all(abs(value) < 1e-12 for value in gauge_eig),
        },
        "scientific_status": {
            "is_selected_MTT_GR_Hessian": False,
            "is_formal_minimal_candidate": True,
            "what_it_shows": "A lens-shear finite ansatz can realize the TT/gauge rank pattern without observed GR data.",
            "what_it_does_not_show": "It does not prove MTT selected this ansatz, nor does it fix G_eff.",
        },
        "next_gate": {
            "name": "LensShearProjectionSourceSearch",
            "question": "Does the corpus or selected branch data independently identify the two lens shear strains as the TT metric response directions with unit relative normalization?",
        },
        "guardrails": {
            "claims_full_GR_closure": False,
            "claims_selected_H_anchor": False,
            "claims_selected_P_GR": False,
            "uses_observed_GR_data": False,
        },
    }
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(json.dumps({"wrote": str(OUT_CERT), "status": cert["status"]}, indent=2))


if __name__ == "__main__":
    main()

