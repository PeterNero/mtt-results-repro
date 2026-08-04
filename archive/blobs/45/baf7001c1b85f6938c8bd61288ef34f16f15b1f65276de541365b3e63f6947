"""Build convention source theorem or RG engine threshold policy artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_ATTEMPT = PACKET_DIR / "same_branch_convention_source_theorem_attempt.packet.json"
POLICY_RECONCILIATION = PACKET_DIR / "rg_benchmark_policy_reconciliation.packet.json"
THRESHOLD_POLICY = PACKET_DIR / "threshold_pole_running_policy_contract.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_convention_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ConventionSourceTheorem_or_RGEngineThresholdPolicy_v1.md"

PREVIOUS = DATA / "selected_samebranchconvention_or_thresholdrowemission.candidate.json"
CONVENTION_TARGET = (
    DATA
    / "selected_samebranchconvention_or_thresholdrowemission"
    / "true_precision_convention_target.packet.json"
)
SOURCE_GAP = (
    DATA
    / "selected_samebranchconvention_or_thresholdrowemission"
    / "same_branch_convention_source_gap.packet.json"
)
PREREQ_ORDER = (
    DATA
    / "selected_samebranchconvention_or_thresholdrowemission"
    / "threshold_row_emission_prerequisite_order.packet.json"
)
RG_POLICY = DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
EXTERNAL_BENCH = (
    DATA
    / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
    / "external_literature_rg_benchmark_values.packet.json"
)
LIT_COMPARISON = (
    DATA
    / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
    / "literature_vs_local_convention_comparison.packet.json"
)
LIT_GAP = (
    DATA
    / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
    / "threshold_covariance_gap_after_literature_benchmark.packet.json"
)
INTERNAL_RG = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "internal_rg_convergence_benchmark.packet.json"
)
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
)
RESIDUAL_VALUES = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_CONVENTIONSOURCETHEOREM_OR_RGENGINETHRESHOLDPOLICY_"
    "BUILT_BENCHMARK_POLICY_CLOSED_SOURCE_MAPS_OPEN"
)
NEXT = "MTT_Selected_ThresholdPoleRunningMaps_or_RThetaConventionSource_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing convention/RG policy sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        CONVENTION_TARGET,
        SOURCE_GAP,
        PREREQ_ORDER,
        RG_POLICY,
        EXTERNAL_BENCH,
        LIT_COMPARISON,
        LIT_GAP,
        INTERNAL_RG,
        THRESHOLD_CONTRACT,
        RESIDUAL_VALUES,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    target = load(CONVENTION_TARGET)
    source_gap = load(SOURCE_GAP)
    prereq = load(PREREQ_ORDER)
    rg_policy = load(RG_POLICY)
    external_bench = load(EXTERNAL_BENCH)
    lit_comparison = load(LIT_COMPARISON)
    lit_gap = load(LIT_GAP)
    internal_rg = load(INTERNAL_RG)
    threshold_contract = load(THRESHOLD_CONTRACT)
    residual_values = load(RESIDUAL_VALUES)

    source_attempt = {
        "schema": "MTTSameBranchConventionSourceTheoremAttempt.v1",
        "status": "SAME_BRANCH_CONVENTION_SOURCE_THEOREM_ATTEMPTED_STILL_OPEN",
        "convention_target_source": rel(CONVENTION_TARGET),
        "source_gap_source": rel(SOURCE_GAP),
        "target_scale": target["target_scale"],
        "target_scheme": target["target_scheme"],
        "target_identified": target["target_identified"],
        "source_evidence_present": {
            "firstpass_profile_layer": source_gap["firstpass_profile_layer_closed"],
            "diagnostic_internal_rg_convergence": source_gap[
                "diagnostic_internal_rg_convergence_closed"
            ],
            "finite_residual_table": source_gap["finite_residual_table_present"],
            "external_literature_benchmark": external_bench[
                "accepted_as_external_literature_benchmark_reference"
            ],
        },
        "why_not_same_branch_source": [
            "first-pass profile convention is explicitly not true precision",
            "diagnostic RG convergence validates the integrator but does not select the physics convention",
            "external literature benchmark rows are downstream validation references, not MTT source selectors",
            "finite residual rows identify gaps but are not threshold/mass-scheme source rows",
        ],
        "same_branch_convention_source_theorem_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SOURCE_ATTEMPT, source_attempt)

    rg = rg_policy["rg_policy"]
    benchmark_policy_closed = (
        rg["reference_scale"] == target["target_scale"]
        and rg["scheme"] == target["target_scheme"]
        and rg_policy["what_closes_now"]["RG_reference_scheme_and_scale_policy"] is True
        and external_bench["accepted_as_external_literature_benchmark_reference"] is True
        and lit_comparison["all_deltas_finite"] is True
        and lit_gap["guardrails"]["external_values_are_downstream_benchmark_not_source_selector"] is True
    )

    policy_reconciliation = {
        "schema": "MTTRGBenchmarkPolicyReconciliation.v1",
        "status": "RG_BENCHMARK_POLICY_RECONCILED_FOR_VALIDATION_NOT_SOURCE_SELECTION",
        "rg_policy_source": rel(RG_POLICY),
        "external_benchmark_source": rel(EXTERNAL_BENCH),
        "local_literature_comparison_source": rel(LIT_COMPARISON),
        "reference_scale": rg["reference_scale"],
        "scheme": rg["scheme"],
        "gauge_normalization": rg["gauge_normalization"],
        "external_benchmark_reference_point": external_bench["reference_point"],
        "external_benchmark_values_filled": external_bench[
            "filled_external_literature_values"
        ],
        "external_benchmark_accepted_as_reference": external_bench[
            "accepted_as_external_literature_benchmark_reference"
        ],
        "external_benchmark_accepted_as_full_precision_match": external_bench[
            "accepted_as_full_precision_match"
        ],
        "internal_rg_convergence_closed_for_diagnostic_engine": internal_rg[
            "passes_internal_convergence"
        ],
        "internal_rg_accepted_for_SM_parity_values": internal_rg[
            "accepted_for_SM_parity_values"
        ],
        "all_literature_local_deltas_finite": lit_comparison["all_deltas_finite"],
        "max_absolute_literature_local_delta": lit_comparison["max_absolute_delta"],
        "benchmark_policy_closed_for_validation": benchmark_policy_closed,
        "benchmark_policy_closes_source_selection": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(POLICY_RECONCILIATION, policy_reconciliation)

    threshold_policy = {
        "schema": "MTTThresholdPoleRunningPolicyContract.v1",
        "status": "THRESHOLD_POLE_RUNNING_POLICY_CONTRACT_BUILT_MAP_VALUES_OPEN",
        "threshold_contract_source": rel(THRESHOLD_CONTRACT),
        "residual_values_source": rel(RESIDUAL_VALUES),
        "threshold_matching_required": threshold_contract["threshold_matching_required"],
        "mass_scheme_conversion_required": threshold_contract[
            "mass_scheme_conversion_required"
        ],
        "covariance_policy": threshold_contract["covariance_policy"],
        "benchmark_policy": threshold_contract["benchmark_policy"],
        "finite_residual_rows_present": residual_values["summary"]["all_residuals_finite"],
        "residual_row_count": residual_values["summary"]["row_count"],
        "accepted_as_threshold_matching_values": residual_values[
            "accepted_as_threshold_matching_values"
        ],
        "accepted_as_mass_scheme_conversion_values": residual_values[
            "accepted_as_mass_scheme_conversion_values"
        ],
        "map_outputs_required_next": [
            "top direct/pole to MSbar running y_t map",
            "Higgs pole to running lambda_H map",
            "bottom and charm native MSbar scale transport maps",
            "tau pole/rest to running charged-lepton map",
            "W/Z/H electroweak matching rows",
            "row covariance or accepted diagonal limitation sidecar",
        ],
        "can_emit_values_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(THRESHOLD_POLICY, threshold_policy)

    cutset = {
        "schema": "MTTNextCutsetAfterConventionPolicy.v1",
        "status": "NEXT_ATTACK_THRESHOLD_POLE_RUNNING_MAPS_OR_SELECTED_CONVENTION_SOURCE",
        "previous_prerequisite_order": rel(PREREQ_ORDER),
        "closed_now": {
            "same_branch_convention_source_attempt": True,
            "rg_benchmark_policy_reconciled_for_validation": benchmark_policy_closed,
            "threshold_pole_running_policy_contract": True,
            "external_benchmark_rows_confirmed_downstream_only": True,
        },
        "still_open": {
            "same_branch_convention_source_theorem": True,
            "versioned_threshold_pole_running_map_values": True,
            "accepted_threshold_matching_source_rows": True,
            "accepted_mass_scheme_conversion_source_rows": True,
            "profile_covariance_or_diagonal_limitation": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive selected same-branch convention source from R_theta geometry",
            "route_B": "execute versioned threshold/pole-running maps under the reconciled policy",
            "route_C": "import accepted external map rows with provenance and nonselector guardrails",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedConventionSourceTheoremOrRGEngineThresholdPolicy",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "same_branch_convention_source_theorem_attempt": rel(SOURCE_ATTEMPT),
            "rg_benchmark_policy_reconciliation": rel(POLICY_RECONCILIATION),
            "threshold_pole_running_policy_contract": rel(THRESHOLD_POLICY),
            "next_cutset_after_convention_policy": rel(CUTSET),
        },
        "theorem": {
            "name": "ConventionSourceAttemptAndRGBenchmarkPolicyTheorem",
            "proved": True,
            "statement": (
                "The same-branch convention source theorem cannot yet be closed: first-pass convention, "
                "diagnostic RG convergence, finite residuals, and external literature benchmarks are not "
                "selected MTT source rows. What can be closed is the RG/benchmark policy boundary: the "
                "M_Z/MSbar policy and external Buttazzo benchmark rows are valid downstream validation "
                "references, while threshold/pole-running map values and source ownership remain open."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "same_branch_convention_source_theorem_closed": False,
            "rg_benchmark_policy_closed_for_validation": benchmark_policy_closed,
            "threshold_pole_running_policy_contract_closed": True,
            "versioned_threshold_pole_running_map_values_closed": False,
            "accepted_threshold_matching_source_rows_closed": False,
            "accepted_mass_scheme_conversion_source_rows_closed": False,
            "profile_covariance_or_diagonal_limitation_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_ConventionSourceTheorem_or_RGEngineThresholdPolicy_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "same_branch_convention_source_theorem_closed": False,
        "rg_benchmark_policy_closed_for_validation": benchmark_policy_closed,
        "threshold_pole_running_policy_contract_closed": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ConventionSourceTheorem or RGEngineThresholdPolicy v1

Status: `{STATUS}`.

This artifact attacks the convention source layer.

```text
same-branch convention source theorem closed : false
RG benchmark policy closed for validation    : {str(benchmark_policy_closed).lower()}
threshold/pole-running policy contract closed: true
external benchmark accepted as source selector: false
threshold map values emitted                 : false
```

The useful gain is the policy boundary.  The `M_Z` / `MSbar` policy and external
Buttazzo benchmark rows can validate a replay, but they cannot select the MTT
source convention.  The next value-producing step is to emit or import the
actual threshold and pole-running maps under this policy.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
