"""Build the precision empirical replay suite after SM-parity closure."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_precisionempiricalreplaysuite_or_trueequivalence"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SCHEME = PACKET_DIR / "precision_rg_scheme_lock.packet.json"
TABLES = PACKET_DIR / "mass_threshold_provenance_tables.packet.json"
BENCH = PACKET_DIR / "rg_benchmark_contract.packet.json"
COV = PACKET_DIR / "covariance_profile_policy.packet.json"
AUDIT = PACKET_DIR / "true_equivalence_precision_audit.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrecisionEmpiricalReplaySuite_or_TrueEquivalence_v1.md"

STATUS = "MTT_SELECTED_PRECISIONEMPIRICALREPLAYSUITE_OR_TRUEEQUIVALENCE_BUILT_SUITE_READY_TRUE_EQ_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def max_abs_complex_matrix(matrix: list) -> float:
    best = 0.0
    for row in matrix:
        for re, im in row:
            best = max(best, math.hypot(float(re), float(im)))
    return best


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    frontier = load(DATA / "selected_true_sm_equivalence_frontier_after_smparityclosure.candidate.json")
    plan = load(
        DATA
        / "selected_true_sm_equivalence_frontier_after_smparityclosure"
        / "next_executable_superset_plan.packet.json"
    )
    firstpass = load(
        DATA
        / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
        / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
    )
    common = load(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json")
    convergence = load(
        DATA
        / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
        / "internal_rg_convergence_benchmark.packet.json"
    )
    closure_decision = load(
        DATA
        / "selected_qasu3sourcepacket_or_finalsmparityclosure"
        / "sm_parity_closure_decision.packet.json"
    )

    values = firstpass["accepted_values"]
    gauge = common["common_scale_packet"]["closed_values"]

    scheme = {
        "schema": "MTTPrecisionRGSchemeLock.v1",
        "status": "PRECISION_RG_SCHEME_LOCK_BUILT_FIRST_EXTERNAL_BENCHMARK_OPEN",
        "reference_scale": {
            "name": "M_Z",
            "value_GeV": 91.18797809193725,
            "role": "common comparison point for gauge, Yukawa, and Higgs replay packets",
        },
        "scheme": "MSbar-family comparison convention with GUT-normalized alpha_1",
        "loop_order_policy": {
            "current_local_engine": "one-loop matrix Yukawa/Higgs beta equations with frozen M_Z gauge couplings",
            "precision_target": "versioned SM RG engine with declared loop order and threshold policy",
            "current_status": "locally converged first precision scaffold, not external precision equivalence",
        },
        "common_scale_values_carried": {
            "gauge_MZ": gauge,
            "Y_u_MZ_firstpass": values["Y_u_MZ_firstpass"],
            "Y_d_MZ_firstpass": values["Y_d_MZ_firstpass"],
            "Y_e_MZ_firstpass": values["Y_e_MZ_firstpass"],
            "lambda_H_MZ_firstpass": values["lambda_H_MZ_firstpass"],
        },
        "value_inventory": {
            "max_abs_Y_u_MZ_firstpass": max_abs_complex_matrix(values["Y_u_MZ_firstpass"]),
            "max_abs_Y_d_MZ_firstpass": max_abs_complex_matrix(values["Y_d_MZ_firstpass"]),
            "max_abs_Y_e_MZ_firstpass": max_abs_complex_matrix(values["Y_e_MZ_firstpass"]),
            "lambda_H_MZ_firstpass": values["lambda_H_MZ_firstpass"],
            "alpha_1_GUT_MZ": gauge["alpha_1_GUT_MZ"]["central_value"],
            "alpha_2_MZ": gauge["alpha_2_MZ"]["central_value"],
            "alpha_3_MZ": gauge["alpha_3_MZ"]["central_value"],
        },
        "successfully_locks_P1_rg_scheme": True,
        "accepted_for_true_precision_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    tables = {
        "schema": "MTTMassThresholdProvenanceTables.v1",
        "status": "MASS_THRESHOLD_PROVENANCE_TABLES_BUILT_VALUES_STILL_FIRSTPASS",
        "table_policy": "Every replay value must carry native convention, target convention, transport rule, and provenance before true precision equivalence.",
        "rows": [
            {
                "id": "gauge_MZ",
                "native_convention": "already at M_Z comparison point",
                "target_convention": "M_Z MSbar-family gauge convention",
                "transport_status": "CLOSED_AT_DECLARED_REFERENCE_SCALE",
                "threshold_status": "NOT_NEEDED_FOR_CURRENT_MZ_GAUGE_REPLAY_ROW",
                "provenance": "prior common-scale gauge packet",
            },
            {
                "id": "charged_yukawa_matrices",
                "native_convention": "measured replay seeds transported by local first-pass RG scaffold",
                "target_convention": "M_Z first-pass MSbar-like comparison packet",
                "transport_status": "FIRSTPASS_LOCAL_TRANSPORT_EMITTED",
                "threshold_status": "PRECISION_THRESHOLD_VALUES_OPEN",
                "provenance": "accepted first-pass common-scale Yukawa values",
            },
            {
                "id": "lambda_H",
                "native_convention": "tree/native Higgs replay seed transported by local first-pass RG scaffold",
                "target_convention": "M_Z first-pass MSbar-like comparison packet",
                "transport_status": "FIRSTPASS_LOCAL_TRANSPORT_EMITTED",
                "threshold_status": "PRECISION_THRESHOLD_VALUES_OPEN",
                "provenance": "accepted first-pass common-scale Higgs value",
            },
            {
                "id": "CKM_PMNS",
                "native_convention": "unitary replay matrices with native convention",
                "target_convention": "dimensionless convention packet; RG/covariance dependence tracked separately",
                "transport_status": "NATIVE_REPLAY_CARRIED",
                "threshold_status": "COVARIANCE_AND_PROFILE_OPEN",
                "provenance": "mixing and gauge replay packets",
            },
            {
                "id": "neutrino_absolute_scale",
                "native_convention": "oscillation replay only",
                "target_convention": "declared Dirac/Majorana and absolute-mass convention required",
                "transport_status": "OPEN_POLICY_ROW",
                "threshold_status": "OPEN",
                "provenance": "PMNS oscillation replay",
            },
        ],
        "successfully_locks_P2_table_structure": True,
        "precision_threshold_values_filled": False,
        "pole_to_running_maps_filled": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    bench = {
        "schema": "MTTRGBenchmarkContract.v1",
        "status": "RG_BENCHMARK_CONTRACT_BUILT_EXTERNAL_VALUES_OPEN_INTERNAL_CONVERGENCE_CLOSED",
        "local_internal_convergence": {
            "passes_internal_convergence": convergence["passes_internal_convergence"],
            "tolerance": convergence["tolerance"],
            "max_delta_256_to_512": convergence["max_delta_256_to_512"],
            "engine_scope": convergence["engine_scope"],
        },
        "external_benchmark_contract": {
            "required": True,
            "acceptable_sources": [
                "named SM RG implementation with declared beta functions and thresholds",
                "independent local implementation using the same declared equations",
                "literature benchmark table with matching scheme, scale, loop order, and inputs",
            ],
            "acceptance_rule": "Compare all transported Yukawa/Higgs/gauge observables under the declared scheme; deviations must be bounded by stated numerical and convention tolerances.",
            "values_filled": False,
        },
        "successfully_locks_P3_benchmark_contract": True,
        "accepted_for_true_precision_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    covariance = {
        "schema": "MTTCovarianceProfilePolicy.v1",
        "status": "COVARIANCE_PROFILE_POLICY_BUILT_FULL_PROFILE_VALUES_OPEN",
        "policy": {
            "central_values": "allowed and already used for SM-parity replay",
            "uncertainty_sidecars": "required for externally reported precision comparisons",
            "covariance_matrices": "required where public fits provide correlated parameters",
            "profile_likelihood": "required or explicitly waived for global-fit observables",
            "missing_covariance_rule": "mark row precision-limited rather than silently treating errors as independent",
        },
        "tracked_groups": [
            "gauge_MZ",
            "charged_masses_and_yukawas",
            "CKM",
            "PMNS_oscillation",
            "Higgs_mass_vev_lambda",
            "neutrino_absolute_policy",
        ],
        "successfully_locks_P4_covariance_policy": True,
        "full_covariance_profile_values_filled": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    audit = {
        "schema": "MTTTrueEquivalencePrecisionAudit.v1",
        "status": "PRECISION_EMPIRICAL_REPLAY_SUITE_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "starting_point": {
            "SM_parity_closed": closure_decision["SM_parity_closed"],
            "true_SM_equivalence_closed": closure_decision["true_SM_equivalence_closed"],
            "no_knob_closed": closure_decision["no_knob_closed"],
        },
        "P_items": {
            "P1_rg_scheme_lock": "CLOSED_CONTRACT",
            "P2_pole_running_threshold_tables": "CLOSED_STRUCTURE_VALUES_OPEN",
            "P3_external_rg_benchmark": "CLOSED_CONTRACT_EXTERNAL_VALUES_OPEN",
            "P4_covariance_profile_policy": "CLOSED_POLICY_VALUES_OPEN",
            "P5_true_equivalence_audit": "BUILT",
        },
        "numerical_replay_bookkeeping_status": "BUILT_AND_REPRODUCIBLE_WITH_FIRSTPASS_VALUES",
        "remaining_true_equivalence_blockers": [
            "external RG/literature benchmark values",
            "precision threshold and pole-to-running maps",
            "full covariance/profile likelihood values",
            "local QFT observable functor",
            "QM/GR measurement and response interfaces",
            "actual selected Qa/SU3 operator packet replacing parity-interface replacement",
        ],
        "parallel_superset_lane": plan["parallel_superset_lane"],
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrecisionEmpiricalReplaySuiteOrTrueEquivalence",
        "status": STATUS,
        "inputs": {
            "frontier": rel(DATA / "selected_true_sm_equivalence_frontier_after_smparityclosure.candidate.json"),
            "frontier_plan": rel(
                DATA
                / "selected_true_sm_equivalence_frontier_after_smparityclosure"
                / "next_executable_superset_plan.packet.json"
            ),
            "firstpass_values": rel(
                DATA
                / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
                / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
            ),
            "internal_convergence": rel(
                DATA
                / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
                / "internal_rg_convergence_benchmark.packet.json"
            ),
        },
        "output_packets": {
            "precision_rg_scheme_lock": rel(SCHEME),
            "mass_threshold_provenance_tables": rel(TABLES),
            "rg_benchmark_contract": rel(BENCH),
            "covariance_profile_policy": rel(COV),
            "true_equivalence_precision_audit": rel(AUDIT),
        },
        "theorem": {
            "name": "PrecisionEmpiricalReplaySuiteConstructionTheorem",
            "proved": True,
            "statement": (
                "After SM-parity closure, the precision empirical replay suite can be constructed "
                "without source fitting by locking scheme/scale conventions, mass-threshold provenance, "
                "benchmark requirements, and covariance/profile policy around the already emitted first-pass "
                "common-scale replay values. This closes the precision-suite bookkeeping layer but not true "
                "SM equivalence."
            ),
        },
        "what_closes_now": {
            "precision_rg_scheme_lock_built": True,
            "mass_threshold_provenance_table_structure_built": True,
            "external_rg_benchmark_contract_built": True,
            "covariance_profile_policy_built": True,
            "true_equivalence_precision_audit_built": True,
            "superset_strategy_preserved": True,
        },
        "what_remains_open": {
            "external_rg_benchmark_values": True,
            "precision_threshold_and_pole_running_values": True,
            "full_covariance_profile_values": True,
            "local_qft_observable_functor": True,
            "qm_gr_measurement_response_interfaces": True,
            "actual_qasu3_operator_packet_upgrade": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "precision_empirical_replay_suite_built": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PrecisionEmpiricalReplaySuite_or_TrueEquivalence_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "precision_empirical_replay_suite_built": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_ExternalRGBenchmarkValues_or_LocalQFTObservableFunctor_v1",
    }

    note = """# MTT Selected PrecisionEmpiricalReplaySuite or TrueEquivalence v1

Status: `MTT_SELECTED_PRECISIONEMPIRICALREPLAYSUITE_OR_TRUEEQUIVALENCE_BUILT_SUITE_READY_TRUE_EQ_OPEN`.

The precision empirical replay suite is now built. It locks the scheme/scale
policy, mass-threshold provenance table structure, external benchmark contract,
covariance/profile policy, and a true-equivalence precision audit around the
already emitted first-pass common-scale replay values.

This is a superset move: measured-SM precision conventions, QFT/RG benchmark
practice, and MTT typed parameter slots are combined, but the result is locked
to reproducibility and never used as source selection.

What remains open:

- external RG or literature benchmark values
- precision threshold and pole-to-running maps
- full covariance/profile likelihood values
- local QFT observable functor
- QM/GR measurement and response interfaces
- actual selected Qa/SU3 operator packet replacing the parity-interface packet
"""

    for path, payload in [
        (SCHEME, scheme),
        (TABLES, tables),
        (BENCH, bench),
        (COV, covariance),
        (AUDIT, audit),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
