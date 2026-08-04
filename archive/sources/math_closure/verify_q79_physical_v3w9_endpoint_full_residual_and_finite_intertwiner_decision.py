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

ENDPOINT_PACKET = ROOT / "q79_physical_v3w9_endpoint_full_residual.packet.json"
TFIN_PACKET = ROOT / "q79_same_source_continuum_to_finite_intertwiner_cutset.packet.json"
NOTE = (
    ROOT
    / "Q79_PHYSICAL_V3W9_ENDPOINT_FULL_RESIDUAL_AND_FINITE_INTERTWINER_DECISION_v1.md"
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


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


def identity(source: dict) -> str:
    result = source.get("schema") or source.get("certificate")
    require(bool(result), "source identity")
    return str(result)


def state(source: dict) -> str:
    result = source.get("status") or source.get("state")
    require(bool(result), "source state")
    return str(result)


def all_boolean_leaves_true(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        return bool(value) and all(all_boolean_leaves_true(item) for item in value.values())
    return False


def matrix(value: list[list[object]]) -> sp.Matrix:
    return sp.Matrix(
        [[sp.sympify(entry, locals={"sqrt": sp.sqrt, "I": sp.I}) for entry in row] for row in value]
    )


def is_zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def boolean_gram(incidence: sp.MatrixBase) -> sp.Matrix:
    gram = incidence.T * incidence
    return gram.applyfunc(lambda entry: sp.Integer(1) if entry != 0 else sp.Integer(0))


def positions(mask: sp.MatrixBase, ranks: list[int]) -> int:
    return sum(
        int(mask[row, column]) * ranks[row] * ranks[column]
        for row in range(mask.rows)
        for column in range(mask.cols)
    )


def verify_sources(packet: dict) -> dict[str, dict]:
    repositories = {
        "mtt-unified-source-theorem": UST_ROOT,
        "legacy-closure-dynamics": LEGACY_ROOT,
        "12-quantum-gravity": QG_ROOT,
    }
    commit_keys = {
        "mtt-unified-source-theorem": "mtt_unified_source_theorem",
        "legacy-closure-dynamics": "legacy_closure_source",
        "12-quantum-gravity": "quantum_gravity_source",
    }
    sources: dict[str, dict] = {}
    for label, record in packet["inputs"].items():
        if record["repository"] == "closure-dynamics":
            path = ROOT / record["relative_path"]
            raw = path.read_bytes()
        else:
            repository = repositories[record["repository"]]
            require(
                record["commit"]
                == packet["commit_locks"][commit_keys[record["repository"]]],
                f"commit lock: {label}",
            )
            raw = git_blob(repository, record["commit"], record["relative_path"])
        require(sha256_bytes(raw) == record["sha256"], f"source hash: {label}")
        source = json.loads(raw.decode("utf-8"))
        require(identity(source) == record["identity"], f"source identity: {label}")
        require(state(source) == record["state"], f"source state: {label}")
        sources[label] = source
    require(len(sources) == 11, "eleven source records")
    return sources


def verify_representability(packet: dict, sources: dict[str, dict]) -> None:
    g1e = sources["UST_G1E"]
    seed = sources["legacy_four_row_seed"]
    pair = sources["QG_smooth_physical_pair"]
    hym = sources["QG_common_HYM_reduction"]
    benchmark = packet["candidate_adjudication"]["current_S_HS_kappa_hol_benchmark"]
    smooth = packet["candidate_adjudication"]["smooth_projective_V3_W9_pair"]
    contract = packet["candidate_adjudication"]["four_row_S_phys_contract"]

    require(g1e["theorem_id"] == "UST.G1E", "UST.G1E is reused")
    require(len(packet["candidate_adjudication"]["cutset_order"]) == 7, "seven rows")
    require(not g1e["current_benchmark"]["passes_direct_physical_topology_row"], "benchmark source no-go")
    require("FAILS_EXACTLY" in benchmark["Chern_twist_rows"], "stored benchmark failure")
    require(benchmark["decision"] == "REJECT_DIRECT_PHYSICAL_PROMOTION_RETAIN_AS_TESTBED", "benchmark disposition")
    require(
        pair["claim_tiers"]["smooth_visible_and_hidden_projective_sources"]
        == "CLOSED_EXACT_CONSTRUCTIVE",
        "smooth source tier",
    )
    require("SMOOTH_PROJECTIVE_TIER_ONLY" in smooth["local_freeness"], "smooth-only boundary")
    require(
        hym["claim_tiers"]["common_Gauduchon_polystability"]
        == "OPEN_CONSTRUCTIVE_GATE",
        "common HYM open",
    )
    primitive = seed["minimal_source_reduction_theorem"]["primitive_geometric_rows"]
    require(len(primitive) == 4 and not any(primitive.values()), "four-row contract unfilled")
    require(contract["decision"] == "RETAIN_MINIMAL_INPUT_CONTRACT_NOT_ENDPOINT", "contract disposition")
    require(
        packet["candidate_adjudication"]["selected_physical_endpoint_present_in_bound_sources"]
        is False,
        "no current endpoint",
    )
    require(packet["claim_tiers"]["selected_physical_endpoint"] == "OPEN", "endpoint tier")
    require(packet["guardrails"]["promotes_S_HS_as_physical"] is False, "no benchmark relabel")


def verify_residual(packet: dict) -> None:
    residual = packet["complete_physical_residual"]
    rows = residual["extra_rows_R"]
    require(len(rows) == 6, "six extra residual rows")
    require(rows["tangent_HYM"] == "mu_TX=R_Theta wedge omega^2", "tangent HYM")
    require(rows["visible_HYM"] == "mu_V=F_V wedge omega^2", "visible HYM")
    require(rows["hidden_HYM"] == "mu_W=F_W wedge omega^2", "hidden HYM")
    require("d(nu_omega*omega^2)" in rows["balanced"], "balanced row")
    require("alpha_prime/4" in rows["anomaly_Bianchi"], "anomaly coefficient")
    require("omega^3" in rows["SU3_normalization"], "SU3 normalization")

    derivative = packet["extra_row_derivative_K"]
    require(
        derivative["K_V"]
        == "d_AV(a_V) wedge omega^2+2*F_V wedge omega wedge dot_omega",
        "explicit visible HYM derivative",
    )
    require("type_variation" not in json.dumps(derivative), "no hidden type derivative")
    require("type_metric_terms" not in json.dumps(derivative), "no hidden metric derivative")
    require("alpha_prime/2" in derivative["K_anomaly"], "curvature-square derivative")
    require("stack(K_TX" in derivative["stacked_operator"], "stacked K")
    require("dot_log_nu" in derivative["K_balanced"], "balanced derivative")
    metric = packet["selected_target_metric"]
    require(metric["cross_block_C"] == 0, "orthogonal metric")
    require(metric["new_continuous_fit_parameters"] == 0, "no target fit")
    hessian = packet["full_Hessian_decision"]
    require(hessian["formula"] == "H_phys=Delta_Y,1+K^dagger*K", "full Hessian")
    require("intersect" in hessian["kernel"], "kernel intersection")
    require("NOT_PROVED" in hessian["bare_Hodge_absorption"], "no absorption claim")
    require("NOT_PROVED" in hessian["scalar_rescaling"], "no rescaling claim")
    require("retain K_anomaly" in hessian["anomaly_deduplication_test"], "anomaly deduplication gate")


def verify_rank102(packet: dict, sources: dict[str, dict]) -> dict[str, sp.Matrix]:
    stored = packet["rank102_recomputation"]
    source = sources["legacy_rank102_mask"]["rank102_Galerkin_structural_compiler"]
    base = sp.Matrix(source["self_adjoint_Hessian_block_mask"])
    ranks = source["complex_fiber_ranks"]
    incidence = matrix(stored["K_row_lane_incidence"])
    require(base == matrix(stored["base_augmented_Hodge_mask"]), "base mask source")
    require(ranks == [3, 8, 8, 80, 3], "lane ranks")
    require(sum(ranks) == 102, "rank 102")
    require(sum(int(entry) for entry in base) == 19, "base block count")

    without_anomaly = incidence.copy()
    without_anomaly.row_del(4)
    nonanomaly = boolean_gram(without_anomaly)
    full_k = boolean_gram(incidence)
    require(nonanomaly == base, "nonanomaly rows recover base mask")
    require(list(incidence.row(4)) == [1, 1, 1, 1, 1], "anomaly all-lane support")
    require(full_k == sp.ones(5), "K Gram dense mask")
    corrected = matrix(stored["corrected_full_Hessian_allowable_mask"])
    require(corrected == sp.ones(5), "corrected mask dense")
    require(sum(int(entry) for entry in corrected) == 25, "25 ordered blocks")
    require(positions(base, ranks) == 7716, "7716 base positions")
    require(positions(corrected, ranks) == 10404, "10404 corrected positions")
    require(positions(corrected, ranks) - positions(base, ranks) == 2688, "2688 reconsidered")
    require(len(stored["newly_allowed_ordered_blocks"]) == 6, "six cross-gauge ordered blocks")
    require("K^dagger*K" in stored["compression_formula"], "corrected compression")
    return {"base": base, "incidence": incidence, "corrected": corrected}


def verify_finite_operator_witness(packet: dict) -> dict[str, sp.Matrix]:
    witness = packet["exact_finite_operator_witness"]
    delta = matrix(witness["Delta_Q"])
    a0 = matrix(witness["A0_column"])
    correction = matrix(witness["quarter_A0_A0_dagger"])
    h_base = matrix(witness["H_base"])
    k = matrix(witness["K"])
    h_full = matrix(witness["H_phys"])
    pi_base = matrix(witness["Pi_base"])
    pi_full = matrix(witness["Pi_phys"])
    require(correction == sp.Rational(1, 4) * a0 * a0.T, "form correction")
    require(h_base == delta + correction, "base augmented compression")
    require(h_full == h_base + k.T * k, "full correction")
    require(is_zero(h_base * pi_base), "base kernel")
    require(is_zero(h_full * pi_full), "physical kernel")
    require(is_zero(pi_full**2 - pi_full), "physical projector")
    require(pi_base.rank() == 2 and pi_full.rank() == 1, "harmonic rank reduction")
    positive = [value for value in h_full.eigenvals() if value > 0]
    require(min(positive) == 1, "gap one")
    return {"H": h_full, "K": k, "Pi": pi_full}


def verify_tfin(endpoint: dict, witness: dict[str, sp.Matrix]) -> None:
    packet = load(TFIN_PACKET)
    binding = packet["endpoint_packet"]
    require(binding["relative_path"] == ENDPOINT_PACKET.name, "endpoint path")
    require(binding["sha256"] == sha256(ENDPOINT_PACKET), "endpoint hash")
    require(binding["schema"] == endpoint["schema"], "endpoint schema")

    exact = packet["exact_rational_witness"]
    t_fin = matrix(exact["T_fin"])
    h_c = matrix(exact["H_continuum"])
    k_c = matrix(exact["K_continuum"])
    pi_c = matrix(exact["Pi_continuum"])
    h_f = matrix(exact["H_finite"])
    k_f = matrix(exact["K_finite"])
    pi_f = matrix(exact["Pi_finite"])
    require(h_c == witness["H"] and k_c == witness["K"], "same endpoint witness")
    require(pi_c == witness["Pi"], "same projector witness")
    require(is_zero(t_fin.T * t_fin - sp.eye(5)), "T finite orthogonal")
    require(is_zero(k_f * t_fin - k_c), "K square")
    require(is_zero(h_f * t_fin - t_fin * h_c), "full Hessian square")
    require(is_zero(pi_f * t_fin - t_fin * pi_c), "projector square")
    require(is_zero(pi_f**2 - pi_f), "finite projector")

    leak = packet["adjoint_leakage_witness"]
    t = matrix(leak["T"])
    s = matrix(leak["S_R"])
    kc = matrix(leak["K_c"])
    kf = matrix(leak["K_f"])
    d_k = kf * t - s * kc
    h_defect = kf.T * kf * t - t * kc.T * kc
    e_perp = (sp.eye(2) - t * t.T) * kf.T * s
    require(is_zero(t.T * t - sp.eye(1)), "leak T isometry")
    require(is_zero(d_k), "forward K defect zero")
    require(h_defect.norm(2) == sp.Rational(1, 2), "nonzero Hessian leakage")
    require(e_perp.norm(2) == sp.Rational(1, 2), "stored leakage norm")
    require(leak["actual_full_Hessian_defect"] == "1/2", "stored Hessian defect")
    require("epsilon_perp" in packet["approximate_error_contract"]["full_Hessian_defect_bound"], "leakage bound retained")
    require(packet["physical_instantiation"]["selected_dynamic_T_fin"] is False, "physical Tfin open")
    require(packet["guardrails"]["uses_static_F3_as_physical_dynamic_embedding"] is False, "no F3 relabel")
    require(all_boolean_leaves_true(packet["checks"]), "Tfin checks")


def verify_note() -> None:
    text = NOTE.read_text(encoding="utf-8")
    require("No currently bound source is a selected physical V3/W9 endpoint" in text, "note source boundary")
    require("19 to 25 ordered blocks" in text, "note mask delta")
    require("epsilon_perp" in text, "note leakage term")
    require("physical q79 `T_fin` remains open" in text, "note Tfin boundary")
    require("not a no-go against a" in text, "note finite-audit scope")


def main() -> int:
    endpoint = load(ENDPOINT_PACKET)
    require(
        endpoint["schema"] == "MTTQ79PhysicalV3W9EndpointFullResidualDecision.v1",
        "endpoint schema",
    )
    sources = verify_sources(endpoint)
    verify_representability(endpoint, sources)
    verify_residual(endpoint)
    verify_rank102(endpoint, sources)
    witness = verify_finite_operator_witness(endpoint)
    require(all_boolean_leaves_true(endpoint["checks"]), "endpoint checks")
    require(endpoint["guardrails"]["uses_bare_Delta_Y_as_full_physical_Hessian"] is False, "no bare Hodge")
    require(endpoint["guardrails"]["treats_25_block_mask_as_numerical_nonzero_matrix"] is False, "mask tier")
    verify_tfin(endpoint, witness)
    verify_note()
    print("Q79_PHYSICAL_V3W9_ENDPOINT_FULL_RESIDUAL_AND_FINITE_INTERTWINER_VERIFY_PASS")
    print("current-source physical endpoint promotion: correctly rejected")
    print("complete residual/K and 25-block allowable full-Hessian mask: verified")
    print("physical K values, harmonic projector and T_fin: remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
