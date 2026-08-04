from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79projectivelinechartcovarianceandellzerocontinuation"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
OUT = ROOT / "candidate_data" / SLUG
THEOREM = OUT / "projective_line_chart_covariance_theorem.packet.json"
DECISION = OUT / "ell_zero_projective_continuation.open.json"
FRONTIER = OUT / "U6_frontier_after_A123.packet.json"
DIAGNOSTIC = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_projective_line_chart_covariance_and_continuation.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    theorem = load(THEOREM)
    decision = load(DECISION)
    frontier = load(FRONTIER)
    diagnostic = load(DIAGNOSTIC)

    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    exact = diagnostic["exact_chart_checks"]
    require(
        all(exact["homogeneous_degree_transition_residuals_zero"].values()),
        "homogeneous transition",
    )
    require(exact["residue_form_transition_residual"] == "0", "residue transition")
    require(exact["five_period_transition_determinant"] == "-1", "period determinant")
    require(theorem["theorem"]["proved"], "chart covariance theorem")
    require(
        theorem["normal_function_covariance"][
            "reduced_period_basis_transition_determinant"
        ]
        == "-1",
        "reported determinant",
    )

    covariance = decision["same_branch_chart_audit"]
    require(covariance["maximum_absolute_difference"] < 5.0e-5, "beta covariance")
    require(covariance["projective_overlap"] > 0.999999, "beta overlap")
    require(
        covariance["base_lift_transition_maximum_absolute_residual"] < 1.0e-12,
        "base-lift transition",
    )
    norms = decision["beta_norm_chain"]
    require(len(norms) == 6, "continuation point count")
    require(
        all(norms[index + 1] < norms[index] for index in range(5)),
        "continuation monotonicity",
    )
    require(decision["A122_false_nodal_wall"]["retired"], "false wall retained")
    require(frontier["projective_line_chart_covariance_closed"], "frontier chart theorem")
    require(frontier["ell_zero_search_advanced_beyond_old_chart_wall"], "frontier advance")
    require(not decision["open"]["smooth_ell_zero_found"], "zero invented")
    require(not decision["open"]["ell_zero_no_go_proved"], "no-go invented")
    require(not certificate["smooth_PGL3_zero_found"], "certificate zero")
    require(not certificate["global_no_go_proved"], "certificate no-go")
    require(not candidate["checks"]["observed_SM_target_fitting_used"], "target fitting")

    print("q79 A123 projective chart covariance and ell-zero continuation audit: PASS")
    print("closed: exact two-chart curve, residue, and five-period covariance")
    print(f"ell=0 beta norm: {norms[0]:.6f} -> {norms[-1]:.6f}")
    print("open: interval-certified one-sided Picard-Lefschetz residual")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
