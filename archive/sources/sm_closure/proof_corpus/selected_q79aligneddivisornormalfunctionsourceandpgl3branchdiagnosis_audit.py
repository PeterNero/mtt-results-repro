from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79aligneddivisornormalfunctionsourceandpgl3branchdiagnosis"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
OUT = ROOT / "candidate_data" / SLUG
THEOREM = OUT / "aligned_divisor_normal_function_source_theorem.packet.json"
DECISION = OUT / "corrected_PGL3_branch_diagnosis.open.json"
FRONTIER = OUT / "U6_frontier_after_A122.packet.json"
A121_IDENTITY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_identity_generalized_evaluator.diagnostic.json"
)
RETIRED = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_retired_pre_fix_alignment_seed.exploratory.json"
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
    identity = load(A121_IDENTITY)
    retired = load(RETIRED)

    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    q_a, q_b, q_t, a_dot, b_dot = sp.symbols(
        "q_a q_b q_t a_dot b_dot"
    )
    t_dot = -(q_a * a_dot + q_b * b_dot) / q_t
    residual = sp.cancel(q_a * a_dot + q_b * b_dot + q_t * t_dot)
    require(residual == 0, "implicit root chain rule")
    require(
        theorem["exact_checks"]["chain_rule_residual"] == "0",
        "reported chain rule",
    )
    require(theorem["theorem"]["proved"], "aligned source theorem")
    require(
        theorem["correction"]["identity_A121_affected"] is False,
        "identity affected",
    )
    require(
        not retired["strict_scope"]["beta_or_jacobian_values_included"],
        "retired beta/Jacobian leaked into compact seed",
    )
    require(
        float(identity["A121_identity_vector_maximum_absolute_difference"])
        < 1.0e-8,
        "identity compatibility",
    )

    norms = decision["clean_identity_descent"]["beta_norms"]
    require(len(norms) == 5, "clean norm count")
    require(
        all(norms[index + 1] < norms[index] for index in range(4)),
        "clean descent monotonicity",
    )
    singular_values = decision["clean_identity_descent"][
        "minimum_Jacobian_singular_values"
    ]
    require(len(singular_values) == 4, "Jacobian carrier count")
    require(min(singular_values) > 1.0e-4, "corrected Jacobian rank")
    require(
        decision["nodal_comparison"]["latest_projective_beta_overlap"] > 0.98,
        "two-basin overlap",
    )
    require(
        decision["nodal_comparison"]["regression_is_not_a_separation_theorem"],
        "regression guard",
    )
    require(
        decision["path_guarded_random_scan"]["evaluated_carriers"] == 12,
        "random scan count",
    )
    require(
        not decision["bounded_integral_branch_search"]["accepted_as_exact_branch"],
        "bounded branch overpromotion",
    )
    require(not decision["open"]["smooth_ell_zero_branch_found"], "zero invented")
    require(not decision["open"]["global_ell_zero_no_go_proved"], "no-go invented")
    require(not decision["open"]["exact_integral_branch_selected"], "ell invented")
    require(frontier["aligned_divisor_source_theorem_closed"], "frontier theorem")
    require(not frontier["ell_zero_no_go_proved"], "frontier no-go")
    require(not certificate["smooth_PGL3_zero_found"], "certificate zero")
    require(not certificate["global_no_go_proved"], "certificate no-go")
    require(not candidate["checks"]["observed_SM_target_fitting_used"], "target fitting")

    print("q79 A122 aligned-divisor source and branch diagnosis audit: PASS")
    print("closed: exact q_A root source and implicit root velocity")
    print(f"clean corrected beta norm: {norms[0]:.6f} -> {norms[-1]:.6f}")
    print("open: nodal residual theorem or selected nonzero integral branch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
