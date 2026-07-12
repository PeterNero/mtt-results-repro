"""Audit row-local threshold-value row plan and brute-force search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PLAN_PACKET = PACKET_DIR / "advanced_row_attack_plan.packet.json"
FEATURE_TABLE_PACKET = PACKET_DIR / "source_feature_table.packet.json"
FINITE_SEARCH_PACKET = PACKET_DIR / "finite_subfactor_normalization_bruteforce.packet.json"
RATIONAL_SEARCH_PACKET = PACKET_DIR / "small_rational_feature_bruteforce.packet.json"
LSQ_PACKET = PACKET_DIR / "least_squares_diagnostic_models.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_bruteforce.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ROWLOCALTHRESHOLDVALUEROWS_OR_LAMBDAHPREFACTOREXECUTION_"
    "BUILT_ADVANCED_PLAN_AND_BRUTEFORCE_SEARCH_ROWS_OPEN"
)
NEXT = "MTT_Selected_RowLocalHYMOverlapQuadratureFunctional_or_ThresholdSchemeSourceTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close this audit theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    plan = load(PLAN_PACKET)
    features = load(FEATURE_TABLE_PACKET)
    finite = load(FINITE_SEARCH_PACKET)
    rational = load(RATIONAL_SEARCH_PACKET)
    lsq = load(LSQ_PACKET)
    cutset = load(CUTSET_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("plan", plan),
        ("features", features),
        ("finite", finite),
        ("rational", rational),
        ("lsq", lsq),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(len(plan["smart_attack_lanes"]) >= 5, "attack lanes missing")
    require(plan["brute_force_policy"]["diagnostic_target_scored_search_may_close_rows"] is False, "diagnostic promotion allowed")
    require(plan["brute_force_policy"]["ordinary_fit_parameters_forbidden"] is True, "fit guard missing")

    require(features["row_count"] == 10, "feature row count mismatch")
    require(features["target_values_are_postcheck_only"] is True, "postcheck guard missing")
    for row in features["feature_rows"]:
        require(row["accepted_as_source_row"] is False, f"feature row accepted: {row['omega_id']}")
        for key in ["theta_exponent", "generation_center", "log_heat_trace", "log_pseudodet_geometric_mean"]:
            require(key in row["features"], f"feature missing {key}")

    require(finite["candidate_count"] >= 10, "finite candidate search too small")
    require(finite["accepted_source_normalization_count"] == 0, "finite normalization overaccepted")
    require(finite["best_candidate_id"], "finite best candidate missing")
    for trial in finite["candidate_trials"]:
        require(trial["accepted_as_selected_normalization"] is False, "finite trial accepted")
        require(trial["source_only_no_fit_trial"] is True, "finite trial not source-only")

    require(rational["tested_formula_count"] > 100000, "rational search did not brute force enough")
    require(rational["top_candidate_count"] == 25, "top rational candidate count mismatch")
    require(rational["accepted_source_law_count"] == 0, "rational source law overaccepted")
    for candidate in rational["top_candidates"]:
        require(candidate["accepted_as_selected_source_law"] is False, "rational candidate accepted")
        require(candidate["uses_replay_targets_for_scoring"] is True, "rational candidate scoring guard missing")
        require(candidate["source_only_without_replay_fit"] is False, "rational candidate source-only overclaim")

    require(lsq["model_count"] >= 6, "lsq model count too small")
    require(lsq["accepted_selected_model_count"] == 0, "lsq model overaccepted")
    require(lsq["exact_omega_import_forbidden"] is True, "exact import guard missing")
    exact = next(model for model in lsq["models"] if model["model_id"] == "exact_omega_row_import_forbidden")
    require(exact["max_multiplicative_error_factor"] < 1.000001, "exact replay diagnostic should fit exactly")
    require(exact["accepted_as_selected_source_model"] is False, "exact replay promoted")

    for phrase in [
        "selected HYM/Green zero-mode overlap quadrature values for L_rowlocal",
        "selected threshold scheme functional values for T_scheme",
        "selected lambda_H H-sector source row",
    ]:
        require(phrase in cutset["still_missing"], f"cutset missing {phrase}")
    for phrase in [
        "promote brute-force target-scored formulas as source rows",
        "promote exact omega-row replay import",
        "claim D_fin normalization alone closes L_rowlocal/T_scheme",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing {phrase}")

    decision = data["closure_decision"]
    for key in [
        "advanced_attack_plan_built",
        "source_feature_table_built",
        "finite_subfactor_bruteforce_executed",
        "small_rational_bruteforce_executed",
        "least_squares_diagnostic_models_executed",
    ]:
        require(decision[key] is True, f"decision missing {key}")
        require(cert[key] is True, f"certificate missing {key}")
    require(decision["row_count"] == 10, "decision row count mismatch")
    require(decision["small_rational_tested_formula_count"] == rational["tested_formula_count"], "formula count mismatch")
    for key in [
        "accepted_rowlocal_source_row_count",
        "accepted_prefactor_source_row_count",
        "accepted_omega_source_row_count",
        "accepted_internal_scalar_value_row_count",
    ]:
        require(decision[key] == 0, f"decision overaccepted {key}")
        require(cert[key] == 0, f"certificate overaccepted {key}")
    for key in [
        "lambda_H_value_row_emitted",
        "selected_L_rowlocal_rows_emitted",
        "selected_T_scheme_rows_emitted",
        "strict_omega_acceptance_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")

    for phrase in [
        "finite D_fin candidates tested",
        "small-rational formulas tested",
        "accepted row-local source rows             : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
