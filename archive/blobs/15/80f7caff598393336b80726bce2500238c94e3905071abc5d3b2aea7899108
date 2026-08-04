"""Audit the precision empirical replay suite."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_precisionempiricalreplaysuite_or_trueequivalence"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SCHEME = PACKET_DIR / "precision_rg_scheme_lock.packet.json"
TABLES = PACKET_DIR / "mass_threshold_provenance_tables.packet.json"
BENCH = PACKET_DIR / "rg_benchmark_contract.packet.json"
COV = PACKET_DIR / "covariance_profile_policy.packet.json"
AUDIT = PACKET_DIR / "true_equivalence_precision_audit.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrecisionEmpiricalReplaySuite_or_TrueEquivalence_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PRECISIONEMPIRICALREPLAYSUITE_OR_TRUEEQUIVALENCE_BUILT_SUITE_READY_TRUE_EQ_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    scheme = load(SCHEME)
    tables = load(TABLES)
    bench = load(BENCH)
    cov = load(COV)
    audit = load(AUDIT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(cert["precision_empirical_replay_suite_built"] is True, "suite not certified built")

    require(scheme["successfully_locks_P1_rg_scheme"] is True, "P1 not locked")
    require(scheme["reference_scale"]["name"] == "M_Z", "reference scale mismatch")
    require(scheme["accepted_for_true_precision_equivalence"] is False, "scheme overclaims precision equivalence")
    for key in [
        "max_abs_Y_u_MZ_firstpass",
        "max_abs_Y_d_MZ_firstpass",
        "max_abs_Y_e_MZ_firstpass",
        "lambda_H_MZ_firstpass",
        "alpha_1_GUT_MZ",
        "alpha_2_MZ",
        "alpha_3_MZ",
    ]:
        require(math.isfinite(scheme["value_inventory"][key]), f"nonfinite inventory value: {key}")

    require(tables["successfully_locks_P2_table_structure"] is True, "P2 table not built")
    require(tables["precision_threshold_values_filled"] is False, "threshold values overclaimed")
    require(tables["pole_to_running_maps_filled"] is False, "pole-running maps overclaimed")
    require(len(tables["rows"]) >= 5, "provenance table too small")

    require(bench["successfully_locks_P3_benchmark_contract"] is True, "P3 contract not built")
    require(bench["local_internal_convergence"]["passes_internal_convergence"] is True, "internal convergence missing")
    require(bench["local_internal_convergence"]["max_delta_256_to_512"] <= bench["local_internal_convergence"]["tolerance"] * 0.01, "internal convergence unexpectedly loose")
    require(bench["external_benchmark_contract"]["required"] is True, "external benchmark not required")
    require(bench["external_benchmark_contract"]["values_filled"] is False, "external benchmark values overclaimed")
    require(bench["accepted_for_true_precision_equivalence"] is False, "benchmark overclaims precision equivalence")

    require(cov["successfully_locks_P4_covariance_policy"] is True, "P4 covariance policy not built")
    require(cov["full_covariance_profile_values_filled"] is False, "covariance values overclaimed")
    require("missing_covariance_rule" in cov["policy"], "missing covariance rule absent")

    require(audit["P_items"]["P5_true_equivalence_audit"] == "BUILT", "P5 audit not built")
    require(audit["numerical_replay_bookkeeping_status"] == "BUILT_AND_REPRODUCIBLE_WITH_FIRSTPASS_VALUES", "bookkeeping status mismatch")
    require(audit["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(audit["no_knob_closed"] is False, "no-knob overclaimed")
    for blocker in [
        "external RG/literature benchmark values",
        "precision threshold and pole-to-running maps",
        "full covariance/profile likelihood values",
        "local QFT observable functor",
        "actual selected Qa/SU3 operator packet replacing parity-interface replacement",
    ]:
        require(blocker in audit["remaining_true_equivalence_blockers"], f"missing blocker: {blocker}")

    for key in [
        "precision_rg_scheme_lock_built",
        "mass_threshold_provenance_table_structure_built",
        "external_rg_benchmark_contract_built",
        "covariance_profile_policy_built",
        "true_equivalence_precision_audit_built",
        "superset_strategy_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    require(data["closure_decision"]["SM_parity_closed"] is True, "SM parity flag mismatch")
    require(data["closure_decision"]["precision_empirical_replay_suite_built"] is True, "suite flag mismatch")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclaimed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclaimed")

    for packet in [scheme, tables, bench, cov, audit, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("superset move" in note, "note missing superset method")
    require("external RG or literature benchmark values" in note, "note missing open benchmark")
    require(cert["next_required_artifact"] == "MTT_Selected_ExternalRGBenchmarkValues_or_LocalQFTObservableFunctor_v1", "next artifact mismatch")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
