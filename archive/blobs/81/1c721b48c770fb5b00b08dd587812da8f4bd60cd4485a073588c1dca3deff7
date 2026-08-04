from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood"
STATUS = "MTT_SELECTED_MULTILOOPCOMMONSOURCEPRECISIONTRANSPORT_CLOSED_PROFILE_TIER_FINAL_GLOBAL_AUDIT_OPEN"
NEXT = "MTT_Selected_FinalGlobalTrueSMClosureAudit_AfterMultiLoopPrecision_v1"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    raw = load(f"candidate_data/{SLUG}/smdr_multiloop_common_source_transport.raw.json")
    workspace = load(f"candidate_data/{SLUG}/selected_smdr_multiloop_precision_workspace.packet.json")
    comparison = load(f"candidate_data/{SLUG}/multiloop_precision_comparison_and_convention_decision.packet.json")
    candidate = load(f"candidate_data/{SLUG}.candidate.json")
    cert = load(f"certificates/{SLUG}_certificate.json")

    require(raw["runtime"]["name"] == "SMDR" and raw["runtime"]["version"] == "1.3", "runtime changed")
    require(len(raw["source_inputs"]) == 15, "source input count")
    require(len(raw["output_basis"]) == 8, "raw output basis")
    require(candidate["status"] == STATUS and cert["status"] == STATUS, "status changed")
    require(candidate["closure_claimed"] is False and cert["closure_claimed"] is False, "global closure overclaimed")
    require(candidate["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require(candidate["target_fitting_used"] is False and candidate["observed_data_used_as_selector"] is False, "selector/fitting guard")

    matrix = workspace["covariance_matrix"]
    require(len(matrix) == 8 and all(len(row) == 8 for row in matrix), "matrix shape")
    require(all(abs(matrix[i][j] - matrix[j][i]) <= 1e-24 for i in range(8) for j in range(8)), "matrix asymmetric")
    diagnostics = workspace["diagnostics"]
    require(diagnostics["symmetric_unique_entries"] == 36, "unique count")
    require(diagnostics["nonzero_symmetric_unique_entries"] == 36, "matrix has unfilled/zero entries")
    require(diagnostics["BCT_WZH_cross_entries_determined"] == 15, "cross count")
    require(diagnostics["BCT_WZH_nonzero_cross_entries"] == 15, "nonzero cross count")
    require(diagnostics["BCT_WZH_missing_cross_entries"] == 0, "cross entries missing")
    require(diagnostics["positive_definite"] is True, "matrix not positive definite")
    require(min(diagnostics["cholesky_pivots"]) > 0.0, "nonpositive Cholesky pivot")
    require(diagnostics["accepted_multiloop_precision_transport_rows"] == 8, "transport rows")
    require(diagnostics["accepted_true_equivalence_precision_rows_at_declared_profile_tier"] == 8, "profile precision rows")

    require(comparison["old_profile_direct_comparison_accepted"] is False, "mixed input schemes compared directly")
    require(comparison["direct_K_lambda_postcheck"]["passes_two_sigma_gate"] is True, "direct-K lambda postcheck")
    require(abs(comparison["direct_K_lambda_postcheck"]["pull"]) < 2.0, "direct-K pull")
    require(cert["multiloop_threshold_mass_scheme_transport_closed"] is True, "multiloop transport not closed")
    require(cert["accepted_multiloop_precision_transport_rows"] == 8, "certificate transport rows")
    require(cert["accepted_true_equivalence_precision_rows_at_declared_profile_tier"] == 8, "certificate profile rows")
    require(cert["official_joint_input_correlation_likelihood_imported"] is False, "official likelihood overclaim")
    require(cert["strict_no_knob_empirical_source_derivation_closed"] is False, "no-knob overclaim")
    require(cert["next_required_artifact"] == NEXT, "next artifact")

    print(json.dumps({
        "status": STATUS,
        "multiloop_threshold_mass_scheme_transport_closed": True,
        "accepted_multiloop_precision_transport_rows": 8,
        "symmetric_covariance_entries_determined": 36,
        "BCT_WZH_cross_entries": "15/15 nonzero and determined",
        "direct_K_lambda_pull": cert["direct_K_lambda_pull"],
        "accepted_true_equivalence_precision_rows_at_declared_profile_tier": 8,
        "official_joint_likelihood": False,
        "next_required_artifact": NEXT,
    }, indent=2))
    print("selected SMDR multi-loop common-source precision transport audit passed")


if __name__ == "__main__":
    main()
