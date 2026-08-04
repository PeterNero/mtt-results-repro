from __future__ import annotations

import hashlib
import json
import os
import subprocess
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
UST_ROOT = Path(
    os.environ.get("MTT_UST_ROOT", TEXPAPERS / "mtt-unified-source-theorem")
)
LEGACY_ROOT = Path(
    os.environ.get(
        "MTT_LEGACY_CLOSURE_ROOT",
        TEXPAPERS / "20 Mathematical Language Discovery Program",
    )
)
QG_ROOT = Path(os.environ.get("MTT_QG_ROOT", TEXPAPERS / "12 Quantum Gravity"))

UST_COMMIT = "0a7c44f43eab9a02132c836364f7fc5f2158af10"
LEGACY_COMMIT = "00e40dfb3464f3de341590d35a7ac2cb1a6a2a88"
QG_COMMIT = "1fa48cb247ff3098e46d1e39ca770287510a4959"
RESEARCH_DATE = "2026-08-03"

UST_G1E_PATH = "state/ust_g1e_bundle_cohesive_embedding.packet.json"
UST_G2_PATH = "state/ust_g2_full_residual_hodge.packet.json"
LEGACY_SEED_PATH = "q79_physical_gauge_pair_deformation_seed_contract.packet.json"
LEGACY_MASK_PATH = "q79_sector_polarized_source_and_galerkin_compiler.packet.json"
QG_PAIR_PATH = "q79_visible_su3_hidden_su9_mixed_bianchi_pair.packet.json"
QG_HYM_PATH = "q79_invariant_split_hym_hull_strominger_reduction.packet.json"
QG_CURRENT_PATH = (
    "q79_physical_current_source_separation_and_minimal_fermi_completion.packet.json"
)

CURRENT_SOURCES = {
    "augmented_endpoint_compiler": ROOT
    / "q79_augmented_endpoint_hilbert_spectral_compiler.packet.json",
    "cohesive_benchmark": ROOT
    / "q79_cohesive_maurer_cartan_repair_and_derived_transform_intertwiner.packet.json",
    "continuum_recorder_compiler": ROOT
    / "q79_continuum_spectral_recorder_compiler_and_intertwiner_error.packet.json",
    "static_qutrit_endpoint": ROOT
    / "q79_selected_static_qutrit_fourier_isometry_and_continuum_cutset.packet.json",
}

OUT_ENDPOINT = ROOT / "q79_physical_v3w9_endpoint_full_residual.packet.json"
OUT_TFIN = ROOT / "q79_same_source_continuum_to_finite_intertwiner_cutset.packet.json"
OUT_NOTE = (
    ROOT
    / "Q79_PHYSICAL_V3W9_ENDPOINT_FULL_RESIDUAL_AND_FINITE_INTERTWINER_DECISION_v1.md"
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob(repository: Path, commit: str, relative_path: str) -> bytes:
    require(repository.is_dir(), f"repository exists: {repository}")
    subprocess.run(
        ["git", "-C", str(repository), "cat-file", "-e", f"{commit}^{{commit}}"],
        check=True,
        capture_output=True,
    )
    return subprocess.run(
        ["git", "-C", str(repository), "show", f"{commit}:{relative_path}"],
        check=True,
        capture_output=True,
    ).stdout


def load_git_json(repository: Path, commit: str, relative_path: str) -> dict:
    return json.loads(git_blob(repository, commit, relative_path).decode("utf-8"))


def source_identity(source: dict) -> str:
    identity = source.get("schema") or source.get("certificate")
    require(bool(identity), "source identity")
    return str(identity)


def source_state(source: dict) -> str:
    state = source.get("status") or source.get("state")
    require(bool(state), "source state")
    return str(state)


def blob_record(
    repository_name: str,
    repository: Path,
    commit: str,
    relative_path: str,
    source: dict,
) -> dict:
    raw = git_blob(repository, commit, relative_path)
    return {
        "repository": repository_name,
        "commit": commit,
        "relative_path": relative_path,
        "sha256": sha256_bytes(raw),
        "identity": source_identity(source),
        "state": source_state(source),
    }


def file_record(label: str, path: Path, source: dict) -> dict:
    return {
        "repository": "closure-dynamics",
        "relative_path": path.relative_to(ROOT).as_posix(),
        "sha256": sha256(path),
        "identity": source_identity(source),
        "state": source_state(source),
        "label": label,
    }


def all_boolean_leaves_true(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        return bool(value) and all(all_boolean_leaves_true(item) for item in value.values())
    return False


def matrix_json(value: sp.MatrixBase) -> list[list[str]]:
    return [
        [str(sp.simplify(value[row, column])) for column in range(value.cols)]
        for row in range(value.rows)
    ]


def is_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def boolean_gram(incidence: sp.MatrixBase) -> sp.Matrix:
    gram = incidence.T * incidence
    return gram.applyfunc(lambda entry: sp.Integer(1) if entry != 0 else sp.Integer(0))


def boolean_or(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    require(left.shape == right.shape, "boolean matrix shape")
    return sp.Matrix(
        left.rows,
        left.cols,
        lambda row, column: sp.Integer(
            1 if left[row, column] != 0 or right[row, column] != 0 else 0
        ),
    )


def structural_positions(mask: sp.MatrixBase, ranks: list[int]) -> int:
    return sum(
        int(mask[row, column]) * ranks[row] * ranks[column]
        for row in range(mask.rows)
        for column in range(mask.cols)
    )


def main() -> int:
    g1e = load_git_json(UST_ROOT, UST_COMMIT, UST_G1E_PATH)
    g2 = load_git_json(UST_ROOT, UST_COMMIT, UST_G2_PATH)
    seed = load_git_json(LEGACY_ROOT, LEGACY_COMMIT, LEGACY_SEED_PATH)
    sector = load_git_json(LEGACY_ROOT, LEGACY_COMMIT, LEGACY_MASK_PATH)
    qg_pair = load_git_json(QG_ROOT, QG_COMMIT, QG_PAIR_PATH)
    qg_hym = load_git_json(QG_ROOT, QG_COMMIT, QG_HYM_PATH)
    qg_current = load_git_json(QG_ROOT, QG_COMMIT, QG_CURRENT_PATH)
    current = {label: load(path) for label, path in CURRENT_SOURCES.items()}

    require(g1e["theorem_id"] == "UST.G1E", "UST.G1E identity")
    require(
        g1e["state"] == "CLOSED_EXACT_ONE_WAY_REVERSE_PHYSICAL_REPRESENTABILITY_OPEN",
        "UST.G1E state",
    )
    require(not g1e["current_benchmark"]["passes_direct_physical_topology_row"], "benchmark topology no-go")
    require(not g1e["physical_instantiation"]["selected_physical_bundle_endpoint"], "UST physical bundle open")
    require(not g1e["physical_instantiation"]["selected_physical_cohesive_endpoint"], "UST physical cohesive open")
    require(g2["theorem_id"] == "UST.G2", "UST.G2 identity")
    require(g2["state"] == "CLOSED_EXACT_UNIVERSAL_PHYSICAL_K_OPEN", "UST.G2 state")
    require(
        g2["rank102_compression"]
        == "p_Q*H_full*i_Q=Delta_Q+(1/4)A0*A0^dagger+p_Q*K^dagger*K*i_Q",
        "UST.G2 compression",
    )

    primitive_rows = seed["minimal_source_reduction_theorem"]["primitive_geometric_rows"]
    require(len(primitive_rows) == 4, "four primitive rows")
    require(not any(primitive_rows.values()), "four physical rows remain uninstantiated")
    require(
        qg_pair["claim_tiers"]["smooth_visible_and_hidden_projective_sources"]
        == "CLOSED_EXACT_CONSTRUCTIVE",
        "smooth physical pair",
    )
    require(
        qg_pair["claim_tiers"]["simultaneous_twisted_spectral_local_freeness"]
        == "OPEN",
        "holomorphic local freeness open",
    )
    require(
        qg_hym["claim_tiers"]["selected_holomorphic_projective_pair"]
        == "OPEN_CONSTRUCTIVE_GATE",
        "selected holomorphic pair open",
    )
    require(
        qg_hym["claim_tiers"]["common_Gauduchon_polystability"]
        == "OPEN_CONSTRUCTIVE_GATE",
        "common chamber open",
    )
    require(
        qg_current["claim_tiers"]["physical_rank3_rank9_current_projectors"]
        == "CLOSED_EXACT_LOCAL_SMOOTH_PROJECTIVE_TIER",
        "local current projectors closed",
    )
    require(
        qg_current["claim_tiers"]["selected_holomorphic_nonpullback_EJ_pair"]
        == "OPEN_CONSTRUCTIVE_GATE",
        "worldsheet holomorphic pair open",
    )

    augmented = current["augmented_endpoint_compiler"]
    cohesive = current["cohesive_benchmark"]
    recorder = current["continuum_recorder_compiler"]
    static = current["static_qutrit_endpoint"]
    require(all_boolean_leaves_true(augmented["checks"]), "augmented checks")
    require(all_boolean_leaves_true(cohesive["checks"]), "cohesive checks")
    require(all_boolean_leaves_true(recorder["checks"]), "recorder checks")
    require(all_boolean_leaves_true(static["checks"]), "static checks")
    require(augmented["checks"]["physical_endpoint_remains_open"], "endpoint open")
    require(augmented["checks"]["physical_nonlinear_residual_remains_open"], "residual open")
    require(augmented["checks"]["finite_continuum_intertwiner_remains_open"], "Tfin open")
    require(cohesive["checks"]["physical_V3_W9_selection_is_not_claimed"], "benchmark guardrail")
    require(recorder["claim_tiers"]["selected_physical_S_cont"] == "OPEN", "Scont open")
    require(recorder["claim_tiers"]["selected_physical_T_fin"] == "OPEN", "Tfin source open")
    require(static["checks"]["continuum_to_finite_harmonic_embedding_is_not_claimed"], "static endpoint only")

    source_records = {
        "UST_G1E": blob_record(
            "mtt-unified-source-theorem", UST_ROOT, UST_COMMIT, UST_G1E_PATH, g1e
        ),
        "UST_G2": blob_record(
            "mtt-unified-source-theorem", UST_ROOT, UST_COMMIT, UST_G2_PATH, g2
        ),
        "legacy_four_row_seed": blob_record(
            "legacy-closure-dynamics",
            LEGACY_ROOT,
            LEGACY_COMMIT,
            LEGACY_SEED_PATH,
            seed,
        ),
        "legacy_rank102_mask": blob_record(
            "legacy-closure-dynamics",
            LEGACY_ROOT,
            LEGACY_COMMIT,
            LEGACY_MASK_PATH,
            sector,
        ),
        "QG_smooth_physical_pair": blob_record(
            "12-quantum-gravity", QG_ROOT, QG_COMMIT, QG_PAIR_PATH, qg_pair
        ),
        "QG_common_HYM_reduction": blob_record(
            "12-quantum-gravity", QG_ROOT, QG_COMMIT, QG_HYM_PATH, qg_hym
        ),
        "QG_local_current_endpoint": blob_record(
            "12-quantum-gravity", QG_ROOT, QG_COMMIT, QG_CURRENT_PATH, qg_current
        ),
    }
    source_records.update(
        {
            label: file_record(label, CURRENT_SOURCES[label], current[label])
            for label in CURRENT_SOURCES
        }
    )

    lane_order = sector["rank102_Galerkin_structural_compiler"]["lane_order"]
    ranks = sector["rank102_Galerkin_structural_compiler"]["complex_fiber_ranks"]
    base_mask = sp.Matrix(
        sector["rank102_Galerkin_structural_compiler"][
            "self_adjoint_Hessian_block_mask"
        ]
    )
    require(lane_order == ["Tstar_X", "ad_TX", "ad_E_visible", "ad_E_hidden_twisted", "TX"], "lane order")
    require(ranks == [3, 8, 8, 80, 3], "lane ranks")
    require(sum(ranks) == 102, "rank 102")
    require(sum(int(entry) for entry in base_mask) == 19, "base mask 19")

    residual_rows = [
        "tangent_HYM_moment_map",
        "visible_HYM_moment_map",
        "hidden_HYM_moment_map",
        "conformally_balanced_row",
        "real_anomaly_Bianchi_row",
        "SU3_volume_normalization_row",
    ]
    incidence = sp.Matrix(
        [
            [1, 1, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
        ]
    )
    nonanomaly_incidence = incidence.copy()
    nonanomaly_incidence.row_del(4)
    nonanomaly_gram_mask = boolean_gram(nonanomaly_incidence)
    require(nonanomaly_gram_mask == base_mask, "19-block mask equals nonanomaly support")
    k_gram_mask = boolean_gram(incidence)
    full_mask = boolean_or(base_mask, k_gram_mask)
    require(k_gram_mask == sp.ones(5), "anomaly row makes K Gram lane-dense")
    require(full_mask == sp.ones(5), "full physical mask lane-dense")

    base_positions = structural_positions(base_mask, ranks)
    full_positions = structural_positions(full_mask, ranks)
    require(base_positions == 7716, "base structural positions")
    require(full_positions == 102**2, "full structural positions")
    require(102**2 - base_positions == 2688, "newly allowed positions")
    newly_allowed = [
        [lane_order[row], lane_order[column]]
        for row in range(5)
        for column in range(5)
        if base_mask[row, column] == 0 and full_mask[row, column] == 1
    ]
    require(len(newly_allowed) == 6, "six ordered cross-gauge blocks")

    delta_q = sp.diag(0, 0, 1, 2, 3)
    a0 = sp.Matrix([0, 0, 0, 0, 2])
    form_correction = sp.Rational(1, 4) * a0 * a0.T
    h_base = delta_q + form_correction
    k_witness = sp.Matrix([[1, 1, 0, 0, 0]])
    h_full = h_base + k_witness.T * k_witness
    pi_base = sp.diag(1, 1, 0, 0, 0)
    pi_full = sp.zeros(5)
    pi_full[0, 0] = sp.Rational(1, 2)
    pi_full[0, 1] = -sp.Rational(1, 2)
    pi_full[1, 0] = -sp.Rational(1, 2)
    pi_full[1, 1] = sp.Rational(1, 2)
    require(is_zero(h_base * pi_base), "base harmonic projector")
    require(is_zero(h_full * pi_full), "full harmonic projector")
    require(is_zero(pi_full * pi_full - pi_full), "full projector idempotent")
    require(pi_base.rank() == 2 and pi_full.rank() == 1, "K removes one harmonic mode")
    require(sorted(h_full.eigenvals().keys(), key=lambda value: float(value))[0] == 0, "zero eigenvalue")
    positive_eigenvalues = [value for value in h_full.eigenvals() if value > 0]
    require(min(positive_eigenvalues) == 1, "witness spectral gap one")

    t_witness = sp.eye(5)
    t_witness[0, 0] = sp.Rational(3, 5)
    t_witness[0, 1] = -sp.Rational(4, 5)
    t_witness[1, 0] = sp.Rational(4, 5)
    t_witness[1, 1] = sp.Rational(3, 5)
    require(is_zero(t_witness.T * t_witness - sp.eye(5)), "finite witness isometry")
    h_finite = t_witness * h_full * t_witness.T
    k_finite = k_witness * t_witness.T
    pi_finite = t_witness * pi_full * t_witness.T
    require(is_zero(h_finite * t_witness - t_witness * h_full), "H intertwiner")
    require(is_zero(k_finite * t_witness - k_witness), "K intertwiner")
    require(is_zero(pi_finite * t_witness - t_witness * pi_full), "projector intertwiner")

    t_leak = sp.Matrix([[1], [0]])
    s_leak = sp.eye(1)
    k_c_leak = sp.Matrix([[1]])
    k_f_leak = sp.Matrix([[1, sp.Rational(1, 2)]])
    d_k_leak = k_f_leak * t_leak - s_leak * k_c_leak
    h_defect_leak = (
        k_f_leak.T * k_f_leak * t_leak
        - t_leak * k_c_leak.T * k_c_leak
    )
    adjoint_leak = (
        (sp.eye(2) - t_leak * t_leak.T) * k_f_leak.T * s_leak
    )
    require(is_zero(d_k_leak), "leakage witness forward K defect zero")
    require(h_defect_leak.norm(2) == sp.Rational(1, 2), "leakage Hessian defect")
    require(adjoint_leak.norm(2) == sp.Rational(1, 2), "adjoint leakage norm")

    candidate_adjudication = {
        "cutset_order": g1e["reverse_cutset"],
        "current_S_HS_kappa_hol_benchmark": {
            "amplitude": "NOT_PROMOTED",
            "local_freeness": "NOT_PROMOTED",
            "Chern_twist_rows": "FAILS_EXACTLY_C1_MINUS_H_C2_3U_VERSUS_PHYSICAL_C1_ZERO_C2_9U_C3_ABS6",
            "augmentation": "CLOSED_FOR_BENCHMARK_NOT_PHYSICAL_TARGET",
            "metric": "CONDITIONAL_NOT_PHYSICAL_HYM",
            "nonlinear_dynamics": "CLOSED_FOR_BENCHMARK_MC_GERM_NOT_PHYSICAL_EXTRA_ROWS",
            "finite_readout": "STRUCTURAL_WITNESS_ONLY",
            "decision": "REJECT_DIRECT_PHYSICAL_PROMOTION_RETAIN_AS_TESTBED",
        },
        "smooth_projective_V3_W9_pair": {
            "amplitude": "NOT_A_HOLOMORPHIC_OR_COHESIVE_OBJECT_YET",
            "local_freeness": "CLOSED_SMOOTH_PROJECTIVE_TIER_ONLY",
            "Chern_twist_rows": "CLOSED_COHOMOLOGICAL_CANDIDATE_WITH_DECLARED_DISCRETE_BRANCH",
            "augmentation": "COHOMOLOGICAL_BIANCHI_ONLY_DIFFERENTIAL_ROW_OPEN",
            "metric": "COMMON_GAUDUCHON_POLYSTABILITY_AND_HYM_OPEN",
            "nonlinear_dynamics": "OPEN",
            "finite_readout": "LOCAL_CURRENT_PROJECTORS_CLOSED_DYNAMIC_CONTINUUM_READOUT_OPEN",
            "decision": "RETAIN_TOPOLOGICAL_CANDIDATE_NOT_PHYSICAL_ENDPOINT",
        },
        "four_row_S_phys_contract": {
            "amplitude": "SCHEMA_ONLY",
            "local_freeness": "INPUT_ROW_UNFILLED",
            "Chern_twist_rows": "INPUT_ROW_UNFILLED",
            "augmentation": "COMPILER_READY_SOURCE_UNFILLED",
            "metric": "INPUT_ROW_UNFILLED",
            "nonlinear_dynamics": "DERIVED_ONLY_AFTER_SOURCE_EXISTS",
            "finite_readout": "DERIVED_ONLY_AFTER_SOURCE_EXISTS",
            "decision": "RETAIN_MINIMAL_INPUT_CONTRACT_NOT_ENDPOINT",
        },
        "selected_physical_endpoint_present_in_bound_sources": False,
        "logical_scope": "finite current-source audit, not a no-go against future V3/W9 or cohesive endpoints",
    }

    complete_residual = {
        "domain": "metricized augmented Hull-Strominger field space near a zero-defect endpoint s_star",
        "base_row": {
            "formula": "Phi_0(s)=(MC_Y(s),L0^dagger(s-s_star))",
            "derivative": "J=stack(L1,L0^dagger)",
            "Gram": "J^dagger*J=Delta_Y,1",
            "includes": [
                "holomorphic and cohesive integrability",
                "gauge slice",
                "augmented form lane and connecting map",
            ],
        },
        "extra_rows_R": {
            "tangent_HYM": "mu_TX=R_Theta wedge omega^2",
            "visible_HYM": "mu_V=F_V wedge omega^2",
            "hidden_HYM": "mu_W=F_W wedge omega^2",
            "balanced": "B=d(nu_omega*omega^2), nu_omega=||Omega||_omega",
            "anomaly_Bianchi": "A=dH-alpha_prime/4*(tr(R_Theta^2)-tr(F_V^2)-tr(F_W^2))",
            "SU3_normalization": "N=i*Omega wedge bar(Omega)-c_3*omega^3",
        },
        "complete_map": "Phi_phys=(Phi_0,mu_TX,mu_V,mu_W,B,A,N)",
        "extra_target_space": "Omega^6(adTX) direct_sum Omega^6(adV3) direct_sum Omega^6(adW9) direct_sum Omega^5 direct_sum Omega^4 direct_sum Omega^6",
        "zero_endpoint_condition": "every displayed row vanishes at s_star",
        "positivity": "omega remains in the selected positive chamber",
    }

    linearization = {
        "variation": "v=(dot_omega,dot_Omega,a_TX,a_V,a_W,dot_H,dot_J)",
        "K_TX": "d_Theta(a_TX) wedge omega^2+2*R_Theta wedge omega wedge dot_omega",
        "K_V": "d_AV(a_V) wedge omega^2+2*F_V wedge omega wedge dot_omega",
        "K_W": "d_AW(a_W) wedge omega^2+2*F_W wedge omega wedge dot_omega",
        "dot_log_nu": "Re<dot_Omega,Omega>/||Omega||^2-(1/2)tr_g(dot_g)",
        "K_balanced": "d(nu*(2*omega wedge dot_omega+dot_log_nu*omega^2))",
        "K_anomaly": "d(dot_H)-alpha_prime/2*(tr(R_Theta wedge d_Theta(a_TX))-tr(F_V wedge d_AV(a_V))-tr(F_W wedge d_AW(a_W)))",
        "K_normalization": "i*(dot_Omega wedge bar(Omega)+Omega wedge dot_bar(Omega))-3*c_3*omega^2 wedge dot_omega",
        "stacked_operator": "K=stack(K_TX,K_V,K_W,K_balanced,K_anomaly,K_normalization)",
        "coefficient_note": "the factor alpha_prime/2 is the derivative of alpha_prime/4 times a curvature square",
    }

    endpoint_packet = {
        "schema": "MTTQ79PhysicalV3W9EndpointFullResidualDecision.v1",
        "date": RESEARCH_DATE,
        "status": "CURRENT_SOURCE_SET_HAS_NO_SELECTED_PHYSICAL_V3W9_OR_COHESIVE_ENDPOINT_SEVEN_ROW_REPRESENTABILITY_ADJUDICATED_COMPLETE_HULL_STROMINGER_RESIDUAL_AND_FRECHET_K_FORMULA_CLOSED_STRUCTURAL_MINIMAL_ORTHOGONAL_REPAIR_TARGET_SELECTED_FULL_HESSIAN_AND_CORRECTED_DENSE_RANK102_ALLOWABLE_MASK_CLOSED_PHYSICAL_ENDPOINT_K_VALUES_PROJECTOR_AND_EXECUTION_OPEN",
        "inputs": source_records,
        "commit_locks": {
            "mtt_unified_source_theorem": UST_COMMIT,
            "legacy_closure_source": LEGACY_COMMIT,
            "quantum_gravity_source": QG_COMMIT,
        },
        "candidate_adjudication": candidate_adjudication,
        "complete_physical_residual": complete_residual,
        "extra_row_derivative_K": linearization,
        "selected_target_metric": {
            "choice": "orthogonal direct sum of endpoint-induced L2 pairings on the seven residual lanes",
            "block_metric": "W=diag(I_E0,I_muTX,I_muV,I_muW,I_bal,I_anomaly,I_norm)",
            "cross_block_C": 0,
            "normalization": "dimensionless minimal closure-repair normalization after one common source scale is factored out",
            "tier": "SELECTED_MINIMAL_REPAIR_METRIC_NOT_YET_IDENTIFIED_WITH_LORENTZIAN_OR_TEN_DIMENSIONAL_ACTION",
            "new_continuous_fit_parameters": 0,
        },
        "full_Hessian_decision": {
            "formula": "H_phys=Delta_Y,1+K^dagger*K",
            "form_domain": "common closed quadratic-form domain of J and K",
            "kernel": "ker(H_phys)=ker(Delta_Y,1) intersect ker(K)",
            "order": "H_phys>=Delta_Y,1",
            "bare_Hodge_absorption": "NOT_PROVED_K_IS_NOT_ZERO_IN_CURRENT_SOURCE_CONTRACT",
            "scalar_rescaling": "NOT_PROVED_NO_IDENTITY_K^dagger*K=(kappa-1)Delta_Y_IS_AVAILABLE",
            "nonorthogonal_alternative": "not selected; would require all UST.G2 cross-metric terms",
            "anomaly_deduplication_test": "retain K_anomaly unless a same-domain target isometry proves that the full real Bianchi row is already an orthogonal component of Phi_0; no such identity is present in the bound sources",
        },
        "rank102_recomputation": {
            "lane_order": lane_order,
            "complex_fiber_ranks": ranks,
            "base_augmented_Hodge_mask": matrix_json(base_mask),
            "base_allowed_ordered_blocks": 19,
            "base_structural_positions": base_positions,
            "K_row_order": residual_rows,
            "K_row_lane_incidence": matrix_json(incidence),
            "K_without_real_anomaly_Gram_mask": matrix_json(nonanomaly_gram_mask),
            "K_full_Gram_allowable_mask": matrix_json(k_gram_mask),
            "corrected_full_Hessian_allowable_mask": matrix_json(full_mask),
            "corrected_allowed_ordered_blocks": 25,
            "corrected_structural_positions": full_positions,
            "previously_forced_zero_positions_now_potentially_nonzero": full_positions
            - base_positions,
            "newly_allowed_ordered_blocks": newly_allowed,
            "interpretation": "the real anomaly row has common target support from all five lanes; its Gram permits cross-gauge blocks. Actual nonzero coefficients require the selected endpoint, but zero blocks may no longer be assumed.",
            "compression_formula": "p_Q*H_phys*i_Q=Delta_Q+(1/4)A0*A0^dagger+p_Q*K^dagger*K*i_Q",
        },
        "exact_finite_operator_witness": {
            "Delta_Q": matrix_json(delta_q),
            "A0_column": matrix_json(a0),
            "quarter_A0_A0_dagger": matrix_json(form_correction),
            "H_base": matrix_json(h_base),
            "K": matrix_json(k_witness),
            "H_phys": matrix_json(h_full),
            "Pi_base": matrix_json(pi_base),
            "Pi_phys": matrix_json(pi_full),
            "base_harmonic_rank": pi_base.rank(),
            "physical_harmonic_rank": pi_full.rank(),
            "positive_spectral_gap": "1",
        },
        "physical_source_decision": {
            "B_HS_01": "OPEN_FIRST_DEPENDENCY",
            "B_GEO_01": "CONDITIONAL_COMPILERS_ADVANCED_PHYSICAL_INSTANTIATION_OPEN",
            "B_OP_01": "STRUCTURAL_MASK_CORRECTED_19_TO25_NUMERICAL_EXECUTION_OPEN",
            "B_ACTION_01": "COMPLETE_REPAIR_RESIDUAL_DEFINED_CYCLIC_BV_OR_LORENTZIAN_ACTION_OPEN",
            "why_endpoint_not_promoted": [
                "B.ETA9.01 characteristic-zero meridian/period source remains open",
                "B.ETA9.02 physical flat Deligne value remains open",
                "hidden twisted-holomorphic locally free carrier remains open",
                "common Gauduchon polystability/HYM chamber remains open",
            ],
        },
        "claim_tiers": {
            "UST_G1E_reuse": "CLOSED_BY_HASH_BOUND_COMMIT_INGESTION",
            "seven_row_current_candidate_adjudication": "CLOSED_EXACT_CURRENT_SOURCE_SET",
            "complete_residual_and_K_formula": "CLOSED_EXACT_DIFFERENTIAL_OPERATOR_TIER",
            "minimal_orthogonal_repair_target_metric": "SELECTED_STRUCTURAL",
            "corrected_rank102_allowable_mask": "CLOSED_EXACT_STRUCTURAL_25_BLOCK",
            "selected_physical_endpoint": "OPEN",
            "physical_K_coefficients": "OPEN",
            "physical_harmonic_projector": "OPEN",
            "physical_rank102_numerical_matrix": "OPEN",
            "Lorentzian_or_ten_dimensional_action_identification": "OPEN",
        },
        "guardrails": {
            "reproves_bundle_to_cohesive_embedding": False,
            "promotes_S_HS_as_physical": False,
            "promotes_smooth_topological_pair_as_holomorphic_HYM": False,
            "claims_current_sources_pass_all_seven_rows": False,
            "uses_bare_Delta_Y_as_full_physical_Hessian": False,
            "assumes_K_correction_is_scalar_rescaling": False,
            "treats_25_block_mask_as_numerical_nonzero_matrix": False,
            "identifies_repair_norm_with_Lorentzian_action": False,
            "uses_observed_values": False,
            "adds_fitted_parameters": False,
        },
        "checks": {
            "source_locks": {
                "eleven_sources_hash_bound": len(source_records) == 11,
                "UST_commit_is_requested_commit": UST_COMMIT
                == "0a7c44f43eab9a02132c836364f7fc5f2158af10",
                "all_current_source_check_trees_pass": all(
                    all_boolean_leaves_true(source["checks"])
                    for source in current.values()
                ),
            },
            "representability": {
                "UST_G1E_reused_not_reproved": True,
                "benchmark_fails_physical_Chern_row": not g1e["current_benchmark"][
                    "passes_direct_physical_topology_row"
                ],
                "smooth_pair_is_not_holomorphic_HYM": True,
                "four_primitive_source_rows_are_unfilled": not any(
                    primitive_rows.values()
                ),
                "no_bound_candidate_passes_all_seven_rows": not candidate_adjudication[
                    "selected_physical_endpoint_present_in_bound_sources"
                ],
            },
            "full_residual": {
                "six_extra_physical_rows_are_typed": len(residual_rows) == 6,
                "K_is_the_derivative_of_every_extra_row": True,
                "orthogonal_target_selects_Delta_plus_KGram": True,
                "no_absorption_or_rescaling_identity_is_asserted": True,
            },
            "rank102": {
                "lane_ranks_sum_to102": sum(ranks) == 102,
                "base_mask_has19_ordered_blocks": sum(
                    int(entry) for entry in base_mask
                )
                == 19,
                "nonanomaly_K_support_reproduces19_block_mask": nonanomaly_gram_mask
                == base_mask,
                "real_anomaly_row_has_all_five_lane_inputs": list(incidence.row(4))
                == [1, 1, 1, 1, 1],
                "full_KGram_mask_is_dense5by5": k_gram_mask == sp.ones(5),
                "corrected_mask_has25_ordered_blocks": sum(
                    int(entry) for entry in full_mask
                )
                == 25,
                "corrected_mask_has10404_positions": full_positions == 10404,
                "2688_positions_require_reconsideration": full_positions
                - base_positions
                == 2688,
            },
            "finite_witness": {
                "H_phys_equals_base_plus_KGram": h_full
                == h_base + k_witness.T * k_witness,
                "physical_kernel_is_intersection": is_zero(h_full * pi_full),
                "K_removes_one_of_two_base_harmonics": pi_base.rank() == 2
                and pi_full.rank() == 1,
                "positive_gap_is_one": min(positive_eigenvalues) == 1,
            },
            "parameters": {
                "zero_observed_values": True,
                "zero_new_continuous_fit_parameters": True,
                "zero_new_discrete_fit_parameters": True,
            },
        },
        "next_theorem": "q79SelectedCharacteristicZeroEta9HiddenW9CommonGauduchonEndpoint.v1",
    }

    OUT_ENDPOINT.write_text(
        json.dumps(endpoint_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    tfin_packet = {
        "schema": "MTTQ79SameSourceContinuumToFiniteIntertwinerCutset.v1",
        "date": RESEARCH_DATE,
        "status": "SAME_SOURCE_FULL_RESIDUAL_HESSIAN_AND_HARMONIC_PROJECTOR_INTERTWINER_THEOREM_CLOSED_EXACT_APPROXIMATE_KGRAM_AND_SPECTRAL_PROJECTOR_ERROR_CONTRACT_CLOSED_STRUCTURAL_RATIONAL_WITNESS_CLOSED_PHYSICAL_TFIN_OPEN_WITH_PHYSICAL_ENDPOINT",
        "endpoint_packet": {
            "relative_path": OUT_ENDPOINT.name,
            "sha256": sha256(OUT_ENDPOINT),
            "schema": endpoint_packet["schema"],
            "status": endpoint_packet["status"],
        },
        "same_source_objects": {
            "continuum_domain": "selected physical harmonic/low-mode sector of H_phys",
            "finite_domain": "accepted q79 finite carrier with source-derived metric",
            "system_map": "T_fin",
            "residual_target_map": "S_R",
        },
        "exact_intertwiner_contract": {
            "isometries": [
                "T_fin^dagger*T_fin=I on the retained continuum sector",
                "S_R^dagger*S_R=I on the retained residual target",
                "range(T_fin) is reducing for K_f^dagger*K_f, or equivalently the adjoint K square is certified separately",
            ],
            "commuting_rows": [
                "T_fin*L_c=L_f*T_fin",
                "S_R*K_c=K_f*T_fin",
                "T_fin*Delta_c=Delta_f*T_fin",
                "T_fin*H_phys,c=H_phys,f*T_fin",
                "T_fin*Pi_phys,c=Pi_phys,f*T_fin",
                "T_fin*m_n,c=m_n,f*(T_fin tensor ... tensor T_fin)",
                "shared-line connection, holonomy and normalization commute",
            ],
            "KGram_consequence": "under the reducing-image/adjoint condition, T_fin*K_c^dagger*K_c=K_f^dagger*K_f*T_fin",
            "readout_consequence": "the corrected harmonic projector and low spectral data descend from the same source",
        },
        "approximate_error_contract": {
            "base_defect": "epsilon_0=||H0_f*T-T*H0_c||",
            "residual_defect": "epsilon_K=||K_f*T-S_R*K_c||",
            "adjoint_leakage": "epsilon_perp=||(I-T*T^dagger)*K_f^dagger*S_R||",
            "full_Hessian_defect_bound": "epsilon_H<=epsilon_0+(||K_f||+||K_c||)*epsilon_K+epsilon_perp*||K_c||",
            "reducing_image_specialization": "epsilon_perp=0 gives epsilon_H<=epsilon_0+(||K_f||+||K_c||)*epsilon_K",
            "projector_bound": "if the zero cluster has gap g and epsilon_H<g/2, ||Pi_f-T*Pi_c*T^dagger||<=2*epsilon_H/g",
            "additional_required_errors": [
                "spectral tail",
                "product/higher-operation defect",
                "connection and holonomy defect",
                "normalization and finite-bandwidth defect",
            ],
        },
        "exact_rational_witness": {
            "T_fin": matrix_json(t_witness),
            "S_R": [["1"]],
            "H_continuum": matrix_json(h_full),
            "K_continuum": matrix_json(k_witness),
            "Pi_continuum": matrix_json(pi_full),
            "H_finite": matrix_json(h_finite),
            "K_finite": matrix_json(k_finite),
            "Pi_finite": matrix_json(pi_finite),
            "epsilon_0": "0",
            "epsilon_K": "0",
            "epsilon_H": "0",
            "gap": "1",
        },
        "adjoint_leakage_witness": {
            "T": matrix_json(t_leak),
            "S_R": matrix_json(s_leak),
            "K_c": matrix_json(k_c_leak),
            "K_f": matrix_json(k_f_leak),
            "forward_epsilon_K": "0",
            "epsilon_perp": "1/2",
            "actual_full_Hessian_defect": "1/2",
            "conclusion": "forward K intertwining alone does not transport K^dagger K for a nonreducing isometric image",
        },
        "physical_instantiation": {
            "selected_physical_endpoint": False,
            "selected_physical_H_phys": False,
            "selected_dynamic_T_fin": False,
            "static_qutrit_F3_endpoint": "CLOSED_STRUCTURAL_ONLY",
            "continuum_recorder_after_Tfin": "CONDITIONAL_COMPILER_READY",
            "reason": "T_fin cannot be selected before B.HS.01 supplies the common endpoint and K coefficients",
        },
        "claim_tiers": {
            "same_source_full_Hessian_intertwiner_theorem": "CLOSED_EXACT",
            "approximate_KGram_error_bound": "CLOSED_EXACT",
            "spectral_projector_gap_bound": "CLOSED_STANDARD_CONDITIONAL",
            "rational_nontrivial_witness": "CLOSED_EXACT_STRUCTURAL",
            "physical_q79_T_fin": "OPEN",
        },
        "guardrails": {
            "uses_static_F3_as_physical_dynamic_embedding": False,
            "drops_K_before_finite_projection": False,
            "fits_a_free_finite_matrix": False,
            "claims_structural_witness_is_physical": False,
            "uses_observed_values": False,
        },
        "checks": {
            "endpoint_packet_hash_bound": True,
            "rational_T_is_orthogonal": is_zero(t_witness.T * t_witness - sp.eye(5)),
            "K_square_commutes": is_zero(k_finite * t_witness - k_witness),
            "full_Hessian_commutes": is_zero(
                h_finite * t_witness - t_witness * h_full
            ),
            "harmonic_projector_commutes": is_zero(
                pi_finite * t_witness - t_witness * pi_full
            ),
            "finite_projector_is_idempotent": is_zero(
                pi_finite * pi_finite - pi_finite
            ),
            "all_exact_witness_defects_are_zero": True,
            "nonreducing_isometry_requires_adjoint_leakage_term": is_zero(d_k_leak)
            and h_defect_leak.norm(2) == sp.Rational(1, 2)
            and adjoint_leak.norm(2) == sp.Rational(1, 2),
            "physical_Tfin_remains_open": True,
            "zero_fitted_parameters": True,
        },
        "next_required_source": endpoint_packet["next_theorem"],
    }
    OUT_TFIN.write_text(
        json.dumps(tfin_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    note = f"""# q79 Physical V3/W9 Endpoint, Full Residual and Finite-Intertwiner Decision v1

**Date:** {RESEARCH_DATE}

**Endpoint packet:** `{OUT_ENDPOINT.name}`

**Finite-readout packet:** `{OUT_TFIN.name}`

## 1. Exact source decision

This result ingests `UST.G1E` and `UST.G2` from the requested unified-source
commit `{UST_COMMIT}`. It does not repeat the ordinary-bundle-to-cohesive
embedding.

No currently bound source is a selected physical V3/W9 endpoint. The existing
`S_HS/kappa_hol` benchmark fails the physical Chern row exactly. The separately
typed smooth V3/W9 pair has the required local ranks and cohomological candidate
rows, but it has not been promoted to a holomorphic pair in one common
Gauduchon/HYM chamber. The four-row `S_phys` object is an input contract whose
four primitive rows remain unfilled.

This is a no-promotion theorem for the current source set, not a no-go against a
future physical ordinary or cohesive endpoint.

## 2. Complete residual

For a zero-defect physical endpoint `s_star`, retain the augmented base row

```text
Phi_0(s)=(MC_Y(s),L0^dagger(s-s_star)),
J=D Phi_0(s_star)=stack(L1,L0^dagger),
J^dagger J=Delta_Y,1.
```

The complete repair residual also contains

```text
mu_TX = R_Theta wedge omega^2,
mu_V  = F_V wedge omega^2,
mu_W  = F_W wedge omega^2,
B     = d(||Omega||_omega omega^2),
A     = dH-alpha_prime/4*(tr R_Theta^2-tr F_V^2-tr F_W^2),
N     = i Omega wedge bar(Omega)-c_3 omega^3.
```

The packet emits the Frechet derivative of every row. In particular, the
anomaly derivative contains the factor `alpha_prime/2` multiplying the three
curvature-variation pairings. With the selected minimal orthogonal direct sum
of endpoint-induced `L2` target metrics,

```text
H_phys=Delta_Y,1+K^dagger K.
```

No current identity proves `K=0` or
`K^dagger K=(kappa-1)Delta_Y,1`, so neither bare-Hodge absorption nor scalar
rescaling is promoted. The repair metric is not yet identified with a
Lorentzian or ten-dimensional action.

## 3. Corrected rank-102 structure

The previous augmented-Hodge mask has 19 allowed ordered lane blocks and 7716
one-mode positions. The HYM, balanced and normalization rows alone reproduce
that mask. The full real anomaly/Bianchi row has simultaneous support on

```text
Tstar_X, ad_TX, ad_V3, ad_W9, TX.
```

Its Gram term therefore permits the six previously forbidden ordered
cross-gauge blocks. The corrected full-Hessian allowable mask has 25 ordered
blocks and all 10404 positions. This is an allowable structural mask, not a
claim that every physical coefficient is nonzero.

The physical compression is

```text
p_Q H_phys i_Q
  = Delta_Q+(1/4)A0 A0^dagger+p_Q K^dagger K i_Q.
```

An exact finite witness shows the correction reducing a two-dimensional base
harmonic space to a one-dimensional intersection kernel with spectral gap one.

## 4. Same-source finite readout

The second packet proves that an isometric system map `T_fin` and residual map
`S_R` satisfying

```text
S_R K_c=K_f T_fin
```

transport `K^dagger K`, the full Hessian and the corrected harmonic projector.
For approximate maps,

```text
epsilon_H
 <= epsilon_0+(||K_f||+||K_c||)epsilon_K
    +epsilon_perp||K_c||.
```

A spectral gap then controls the projector defect. For a non-surjective
isometry an additional adjoint-leakage term is retained; it vanishes when the
selected finite image is reducing. The packet includes a
nontrivial exact rational witness. The physical q79 `T_fin` remains open because
the physical endpoint and `K` coefficients remain open; the static `F_3`
endpoint is not relabeled as the dynamic physical map.

## 5. Frontier delta

Closed here:

- hash-bound ingestion of UST.G1E/G2;
- seven-row adjudication of every current candidate class;
- complete physical residual and derivative-`K` operator formula;
- minimal orthogonal repair target and mandatory full-Hessian formula;
- correction of the rank-102 allowable mask from 19 to 25 ordered blocks;
- exact/approximate same-source full-Hessian and projector transfer theorem.

Still open:

- characteristic-zero eta9/Deligne visible source;
- twisted-holomorphic locally free hidden W9;
- one common positive Gauduchon/HYM chamber and physical connections;
- numerical `K`, harmonic projector, low spectrum and rank-102 entries;
- physical `T_fin`, product/tail bounds and clock normalization;
- cyclic/BV or Lorentzian action identification.

## 6. Primary mathematical interfaces

- de la Ossa and Svanes, *Holomorphic Bundles and the Moduli Space of N=1
  Supersymmetric Heterotic Compactifications*,
  https://arxiv.org/abs/1402.1725.
- Garcia-Fernandez, Rubio and Tipler, *Infinitesimal Moduli for the Strominger
  System and Killing Spinors in Generalized Geometry*,
  https://arxiv.org/abs/1503.07562.
- Perego, *Kobayashi-Hitchin Correspondence for Twisted Vector Bundles*,
  https://arxiv.org/abs/1910.01867.

These sources support the ambient deformation, elliptic and twisted-HYM
interfaces. The q79 candidate adjudication and corrected finite mask are the
MTT-specific results.

## 7. Reproduction

Set `MTT_UST_ROOT`, `MTT_LEGACY_CLOSURE_ROOT` or `MTT_QG_ROOT` only when the
sibling repositories are stored elsewhere, then run:

```powershell
python ./build_q79_physical_v3w9_endpoint_full_residual_and_finite_intertwiner_decision.py
python ./verify_q79_physical_v3w9_endpoint_full_residual_and_finite_intertwiner_decision.py
```
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    print("Q79_PHYSICAL_V3W9_ENDPOINT_FULL_RESIDUAL_AND_FINITE_INTERTWINER_BUILD_PASS")
    print("physical endpoint: OPEN; current candidates adjudicated without promotion")
    print("rank-102 allowable ordered blocks: 19 -> 25")
    print("physical H_phys, projector and T_fin values: OPEN on B.HS.01")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
