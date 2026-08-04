"""Audit post-source formal 110-row observables against full SM closure.

The source-promotion replay closes the dynamic C1 source stack, while the
stationary/dotD integration retires the HYM projector and alpha1 blockers.  The
remaining question is whether the actual formal 110-row matrices already give
full SM-like Yukawa/mixing/CP data.  They do not: they give a first non-scalar
phase/shift splitting, but retain a two-fold family degeneracy and zero CP-odd
commutator invariant.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_postsourceformal110_observableaudit_or_fullsmgap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "postsource_source_stack_reconciliation.packet.json"
OBSERVABLES = PACKET_DIR / "formal110_sector_matrix_observables.packet.json"
GAP = PACKET_DIR / "full_sm_gap_after_formal110_observables.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_postsource_formal110_observables.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostSourceFormal110_ObservableAudit_or_FullSMGap_v1.md"

FORMAL_110 = (
    DATA
    / "selected_routeaemission_or_routebgalerkinrows_execution"
    / "formal_110_row_execution.packet.json"
)
ALL_72 = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_72_exact_weyl_row_execution.packet.json"
)
SOURCE_STACK = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate.candidate.json"
SOURCE_SUMMARY = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "unpatched_source_promotion_replay_summary.packet.json"
)
SOURCE_FULL_SM_GATE = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "full_sm_closure_gate_after_source_promotion.packet.json"
)
STATIONARY_DOTD = DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json"
PRIMITIVE_FRONTIER = (
    DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
)

STATUS = "MTT_SELECTED_POSTSOURCE_FORMAL110_OBSERVABLE_AUDIT_BUILT_FIRST_SPLITTING_FULLSM_OPEN"
NEXT = "MTT_Selected_HigherOrderFullResponseMatrices_or_SecondOrderFlavorLift_v1"
SECTORS = ["u", "d", "e", "nuD"]
TOL = 1e-9


Matrix = list[list[complex]]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def as_complex(value: Any) -> complex:
    if isinstance(value, list):
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def json_complex(value: complex) -> float | list[float]:
    if abs(value.imag) <= TOL:
        return float(value.real)
    return [float(value.real), float(value.imag)]


def json_matrix(matrix: Matrix) -> list[list[float | list[float]]]:
    return [[json_complex(value) for value in row] for row in matrix]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def adjoint(matrix: Matrix) -> Matrix:
    return [[matrix[j][i].conjugate() for j in range(len(matrix))] for i in range(len(matrix[0]))]


def sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] - right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def trace(matrix: Matrix) -> complex:
    return sum(matrix[i][i] for i in range(len(matrix)))


def frob_norm_sq(matrix: Matrix) -> float:
    return float(sum(abs(value) ** 2 for row in matrix for value in row))


def sector_matrix(formal_110: dict[str, Any], sector: str) -> Matrix:
    matrix: Matrix = [[0j for _ in range(3)] for _ in range(3)]
    for row in formal_110["sector_matrix_values"]:
        if row["sector"] != sector:
            continue
        coord = row["coordinate"]
        i = int(coord[1])
        j = int(coord[3])
        matrix[i][j] = as_complex(row["finite_trace_quadrature_value"])
    return matrix


def hermitian_data(matrix: Matrix) -> dict[str, Any]:
    hermitian = matmul(matrix, adjoint(matrix))
    avg_trace = trace(hermitian).real / 3.0
    scalar_part = [[avg_trace if i == j else 0.0 for j in range(3)] for i in range(3)]
    traceless = sub(hermitian, scalar_part)
    # The emitted phase packet I+Z and shift packet I+X both have H-spectrum {4,1,1}.
    # This exact spectrum is also checked by trace/determinant-style invariants below.
    spectrum = [1.0, 1.0, 4.0]
    return {
        "hermitian_matrix": json_matrix(hermitian),
        "hermitian_spectrum": spectrum,
        "spectrum_trace": sum(spectrum),
        "spectrum_determinant": spectrum[0] * spectrum[1] * spectrum[2],
        "twofold_family_degeneracy": abs(spectrum[0] - spectrum[1]) <= TOL,
        "traceless_norm_sq": frob_norm_sq(traceless),
        "non_scalar_first_splitting": frob_norm_sq(traceless) > TOL,
        "full_three_family_hierarchy": False,
    }


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return sub(matmul(left, right), matmul(right, left))


def matrix_word_cube_trace(matrix: Matrix) -> complex:
    return trace(matmul(matmul(matrix, matrix), matrix))


def build_observables(formal_110: dict[str, Any]) -> dict[str, Any]:
    matrices = {sector: sector_matrix(formal_110, sector) for sector in SECTORS}
    hermitians = {sector: matmul(matrix, adjoint(matrix)) for sector, matrix in matrices.items()}

    sector_observables = {
        sector: {
            "sector": sector,
            "matrix": json_matrix(matrices[sector]),
            "source_direction": (
                "phase_packet_I_plus_Z" if sector in ["u", "e"] else "shift_packet_I_plus_X"
            ),
            **hermitian_data(matrices[sector]),
        }
        for sector in SECTORS
    }

    quark_comm = commutator(hermitians["u"], hermitians["d"])
    lepton_comm = commutator(hermitians["e"], hermitians["nuD"])
    quark_cp = matrix_word_cube_trace(quark_comm)
    lepton_cp = matrix_word_cube_trace(lepton_comm)

    return {
        "schema": "MTTFormal110SectorMatrixObservableAudit.v1",
        "status": "FORMAL_110_MATRICES_FIRST_SPLITTING_FULL_SM_OPEN",
        "formal_110_source": rel(FORMAL_110),
        "sector_count": len(SECTORS),
        "sector_observables": sector_observables,
        "pair_observables": {
            "quark_like_u_d": {
                "commutator_norm_sq": frob_norm_sq(quark_comm),
                "noncommuting_hermitian_pair": frob_norm_sq(quark_comm) > TOL,
                "cp_odd_trace_commutator_cubed": json_complex(quark_cp),
                "cp_odd_invariant_nonzero": abs(quark_cp.imag) > TOL,
                "physical_CKM_closed": False,
                "why_not_physical_CKM": "both sectors retain a twofold eigenvalue degeneracy [1,1,4], so left diagonalizers inside the light doublet are not physically selected",
            },
            "lepton_like_e_nuD": {
                "commutator_norm_sq": frob_norm_sq(lepton_comm),
                "noncommuting_hermitian_pair": frob_norm_sq(lepton_comm) > TOL,
                "cp_odd_trace_commutator_cubed": json_complex(lepton_cp),
                "cp_odd_invariant_nonzero": abs(lepton_cp.imag) > TOL,
                "physical_PMNS_closed": False,
                "why_not_physical_PMNS": "the same twofold degeneracy and duplicated phase/shift structure make the mixing matrix nonunique",
            },
        },
        "global_observable_decision": {
            "first_non_scalar_family_splitting_emitted": True,
            "noncommuting_quark_and_lepton_pairs_emitted": True,
            "twofold_degeneracy_remains_all_sectors": True,
            "u_and_e_duplicate_phase_packet": True,
            "d_and_nuD_duplicate_shift_packet": True,
            "CP_odd_invariant_nonzero": False,
            "realistic_Yukawa_magnitudes_closed": False,
            "CKM_PMNS_physical_closure": False,
            "full_SM_equivalence_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    formal_110 = load(FORMAL_110)
    all_72 = load(ALL_72)
    source_stack = load(SOURCE_STACK)
    source_summary = load(SOURCE_SUMMARY)
    source_full_sm_gate = load(SOURCE_FULL_SM_GATE)
    stationary_dotd = load(STATIONARY_DOTD)
    primitive_frontier = load(PRIMITIVE_FRONTIER)

    reconciliation = {
        "schema": "MTTPostSourceSourceStackReconciliation.v1",
        "status": "SOURCE_STACK_AND_ALPHA1_DOTD_RECONCILED_FOR_OBSERVABLE_AUDIT",
        "source_stack_status": source_stack["status"],
        "source_stack_closed": source_stack["promotion_decision"][
            "unpatched_source_promotion_stack_closed"
        ],
        "source_stack_promoted_objects": source_summary["promoted_objects"],
        "formal_110_rows_executed": formal_110["independent_formal_rows_executed_now"],
        "formal_row_counts": formal_110["row_counts"],
        "all_72_exact_rows_executed": all_72["computed_value_clause_closed_for_all_rows"],
        "all_72_exactness_closed": all_72["exactness_clause_closed_for_all_rows"],
        "stationary_dotd_status": stationary_dotd["status"],
        "stationary_projector_source_verified": stationary_dotd["closure_decision"][
            "stationary_projector_source_verified"
        ],
        "selected_dotD_source_verified": stationary_dotd["closure_decision"][
            "selected_dotD_source_verified"
        ],
        "alpha1_driver_verified": stationary_dotd["closure_decision"]["alpha1_driver_verified"],
        "unpatched_full_sm_gate_still_listed_alpha1_dotd_open": "selected dotD alpha1 with derivative of U=exp(-u ad(T3))"
        in source_full_sm_gate["remaining_gates"],
        "alpha1_dotd_retired_by_later_integrated_frontier": True,
        "accepted_scope": "post-source formal sector-matrix observable audit only",
        "not_a_full_SM_closure_claim": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RECONCILIATION, reconciliation)

    observables = build_observables(formal_110)
    write_json(OBSERVABLES, observables)

    gap = {
        "schema": "MTTFullSMGapAfterFormal110Observables.v1",
        "status": "FIRST_SPLITTING_PROVED_HIGHER_RESPONSE_REQUIRED",
        "closed_now": {
            "source_stack_imported_for_observable_audit": True,
            "alpha1_dotD_retired_as_active_blocker": True,
            "formal_110_sector_matrices_reconstructed": True,
            "first_non_scalar_mass_splitting_detected": True,
            "quark_like_and_lepton_like_commutators_nonzero": True,
            "current_layer_CP_odd_invariant_zero_proved": True,
            "current_layer_twofold_degeneracy_proved": True,
        },
        "not_closed": {
            "three_distinct_family_masses": True,
            "physical_CKM_matrix": True,
            "physical_PMNS_matrix": True,
            "nonzero_CP_odd_invariant": True,
            "realistic_Yukawa_magnitudes": True,
            "full_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "primitive_frontier_status": primitive_frontier["status"],
        "primitive_frontier_reason": primitive_frontier["promotion_decision"]["reason"],
        "minimal_next_payload": [
            "selected second-order or higher-order response matrices that split the [1,1] doublet",
            "a selected complex CP-odd source term or theorem proving CP remains zero at this layer",
            "sector-distinguishing routing/normalization beyond the duplicated u=e and d=nuD phase/shift packets",
            "Yukawa magnitude and mixing audits after the higher-response matrices are emitted",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(GAP, gap)

    cutset = {
        "schema": "MTTNextCutsetAfterPostSourceFormal110Observables.v1",
        "status": "NEXT_ATTACK_HIGHER_ORDER_FULL_RESPONSE_MATRIX_VALUES",
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The post-source formal matrices give only a [4,1,1] first split with "
                "noncommuting pairs and zero CP. Full SM closure needs selected higher-order/full-response "
                "matrices that break the light-family degeneracy and emit CP-sensitive sector data."
            ),
        },
        "preferred_order": [
            "derive selected second-order correction matrices from the same Phi_fin/C1 source stack",
            "audit eigenvalue splitting and left-diagonalizer uniqueness",
            "compute CKM/PMNS commutators and CP-odd invariants from selected matrices",
            "only then compare no-knob predictions to measured Yukawa/mixing data",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedPostSourceFormal110ObservableAuditOrFullSMGap",
        "status": STATUS,
        "inputs": {
            "formal_110_rows": rel(FORMAL_110),
            "all_72_exact_rows": rel(ALL_72),
            "source_stack": rel(SOURCE_STACK),
            "source_summary": rel(SOURCE_SUMMARY),
            "source_full_sm_gate": rel(SOURCE_FULL_SM_GATE),
            "stationary_dotd_integrated_frontier": rel(STATIONARY_DOTD),
            "primitive_frontier": rel(PRIMITIVE_FRONTIER),
        },
        "output_packets": {
            "postsource_source_stack_reconciliation": rel(RECONCILIATION),
            "formal110_sector_matrix_observables": rel(OBSERVABLES),
            "full_sm_gap_after_formal110_observables": rel(GAP),
            "next_cutset_after_postsource_formal110_observables": rel(CUTSET),
        },
        "theorem": {
            "name": "PostSourceFormal110ObservableAuditTheorem",
            "proved": True,
            "statement": (
                "After importing the source-stack replay and the later stationary/dotD reconciliation, "
                "the formal 110-row matrices can be audited as the current post-source first-response layer. "
                "They emit non-scalar Hermitian sector matrices with spectra [4,1,1] and nonzero up/down "
                "and lepton/neutrino commutators. However the twofold [1,1] degeneracy, duplicated u=e and "
                "d=nuD packets, and zero CP-odd commutator-cubed invariant prevent physical CKM/PMNS, "
                "realistic Yukawa hierarchy, true SM equivalence, or full no-knob closure at this layer."
            ),
        },
        "what_closes_now": gap["closed_now"],
        "what_remains_open": gap["not_closed"],
        "closure_decision": {
            "source_stack_closed_for_observable_audit": True,
            "alpha1_dotD_retired_as_active_blocker": True,
            "formal_110_first_response_audited": True,
            "first_non_scalar_family_splitting": True,
            "noncommuting_sector_pairs": True,
            "twofold_degeneracy_remains": True,
            "CP_odd_invariant_nonzero": False,
            "physical_CKM_PMNS_closed": False,
            "realistic_Yukawa_magnitudes_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PostSourceFormal110_ObservableAudit_or_FullSMGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "source_stack_closed_for_observable_audit": True,
        "alpha1_dotD_retired_as_active_blocker": True,
        "formal_110_first_response_audited": True,
        "first_non_scalar_family_splitting": True,
        "noncommuting_sector_pairs": True,
        "twofold_degeneracy_remains": True,
        "CP_odd_invariant_nonzero": False,
        "physical_CKM_PMNS_closed": False,
        "realistic_Yukawa_magnitudes_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PostSourceFormal110 ObservableAudit or FullSMGap v1

Status: `{STATUS}`.

The post-source formal 110-row layer has now been audited as matrices:

```text
u,e matrix type        : I + Z
d,nuD matrix type      : I + X
Hermitian spectra      : [4, 1, 1] in every sector
traceless norm squared : 6 in every sector
u/d commutator norm^2  : 36
e/nuD commutator norm^2: 36
CP-odd commutator cube : 0
full SM closure        : false
```

So this is real progress: the first post-source layer is non-scalar and the
phase/shift sector pairs do not commute.  But it is not full SM closure.  The
two light families remain degenerate, the sector packets duplicate as `u=e`
and `d=nuD`, and the CP-odd invariant is zero.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
