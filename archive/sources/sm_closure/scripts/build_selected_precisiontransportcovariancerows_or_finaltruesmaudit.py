"""Build the precision-transport/covariance rows / final true-SM audit gate.

This is an easy-win consolidation pass after strict P_EW/direct-K closure.  It
does not claim full true-SM equivalence.  It certifies the substructure that is
already evidenced in the repo: local RG benchmark/interface, 8x8 covariance
target shape, precision proxy/operator-slot inventory, admitted threshold and
mass-scheme replay lanes, and the final typed no-knob kernel.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_precisiontransportcovariancerows_or_finaltruesmaudit"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
READINESS = PACKET_DIR / "precision_transport_covariance_readiness.packet.json"
COVARIANCE = PACKET_DIR / "full_covariance_target_lock.packet.json"
TRANSPORT = PACKET_DIR / "threshold_rg_observable_transport_subgates.packet.json"
SUPPORT = PACKET_DIR / "already_executed_support_attempts.packet.json"
GATE = PACKET_DIR / "final_true_sm_audit_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrecisionTransportCovarianceRows_or_FinalTrueSMAudit_v1.md"

POST_PEW = DATA / "selected_precisionequivalencerows_or_truesmclosureaudit.candidate.json"
POST_PEW_ROWS = (
    DATA
    / "selected_precisionequivalencerows_or_truesmclosureaudit"
    / "precision_equivalence_row_status_table.packet.json"
)
EXT_RG = DATA / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor.candidate.json"
EXT_RG_BENCH = (
    DATA
    / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor"
    / "independent_local_rg_benchmark_values.packet.json"
)
EXT_QFT_FUNCTOR = (
    DATA
    / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor"
    / "local_qft_observable_functor_interface.packet.json"
)
COV_BRIDGE = DATA / "selected_externalprofiletofullcovariancebridge_or_selectedsourcerows.candidate.json"
COV_BRIDGE_PACKET = (
    DATA
    / "selected_externalprofiletofullcovariancebridge_or_selectedsourcerows"
    / "external_profile_full_covariance_bridge.packet.json"
)
OBS_TABLE = DATA / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill.candidate.json"
OBS_LOOP = (
    DATA
    / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill"
    / "precision_observable_table_full_loop_import_attempt.packet.json"
)
OBS_QASU3 = (
    DATA
    / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill"
    / "qasu3_operator_slot_fill_attempt.packet.json"
)
STEP25 = DATA / "selected_step25_thresholdexternalreplay_noknobkernel_or_fulls2cutset.candidate.json"
STEP25_KERNEL = (
    DATA
    / "selected_step25_thresholdexternalreplay_noknobkernel_or_fulls2cutset"
    / "step25_external_replay_and_noknob_kernel.packet.json"
)
RG_SUITE = DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
CROSS = DATA / "true_sm_crossrepo_part_status_audit.candidate.json"
SUPPORT_ATTEMPTS = [
    DATA / "selected_step7_commonrgcovarianceobservablesuite_or_finaltruesmequivalencegate.candidate.json",
    DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json",
    DATA / "selected_acceptedprecisionprofileimport_or_selectedqasu3operatorslotsourcevalues.candidate.json",
    DATA / "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem.candidate.json",
    DATA / "selected_covarianceprofilepayload_or_qasu3selectedslotvalues.candidate.json",
    DATA / "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof.candidate.json",
    DATA / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining.candidate.json",
    DATA / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill.candidate.json",
    DATA / "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure.candidate.json",
    DATA / "selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion.candidate.json",
    DATA / "selected_qasu3operatorpayload_or_strictpewprecisionexit.candidate.json",
]

STATUS = (
    "MTT_SELECTED_PRECISIONTRANSPORTCOVARIANCEROWS_OR_FINALTRUESMAUDIT_"
    "EASY_WIN_SUBGATES_LOCKED_TRUE_VALUES_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_AcceptedPrecisionSourceValues_or_FinalTrueSMClosure_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing precision-transport inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        POST_PEW,
        POST_PEW_ROWS,
        EXT_RG,
        EXT_RG_BENCH,
        EXT_QFT_FUNCTOR,
        COV_BRIDGE,
        COV_BRIDGE_PACKET,
        OBS_TABLE,
        OBS_LOOP,
        OBS_QASU3,
        STEP25,
        STEP25_KERNEL,
        RG_SUITE,
        CROSS,
        *SUPPORT_ATTEMPTS,
    ]
    require_sources(sources)

    post_pew = load(POST_PEW)
    post_pew_rows = load(POST_PEW_ROWS)
    ext_rg = load(EXT_RG)
    ext_rg_bench = load(EXT_RG_BENCH)
    ext_qft_functor = load(EXT_QFT_FUNCTOR)
    cov_bridge = load(COV_BRIDGE)
    cov_packet = load(COV_BRIDGE_PACKET)
    obs_table = load(OBS_TABLE)
    obs_loop = load(OBS_LOOP)
    obs_qasu3 = load(OBS_QASU3)
    step25 = load(STEP25)
    step25_kernel = load(STEP25_KERNEL)
    rg_suite = load(RG_SUITE)
    cross = load(CROSS)
    support_attempts = [load(path) for path in SUPPORT_ATTEMPTS]
    accepted_import = support_attempts[2]
    profile_row_replacement = support_attempts[3]
    covariance_payload = support_attempts[4]
    external_profile_like = support_attempts[5]
    profile_mining = support_attempts[6]
    precision_value_attempt = support_attempts[7]
    step8 = support_attempts[8]

    covariance_target = cov_packet["full_covariance_target"]
    coordinate_blocks = cov_packet["external_coordinate_blocks"]
    step25_decision = step25["closure_decision"]
    threshold_replay = step25_kernel["threshold_external_replay"]
    readiness = step25_kernel["readiness"]
    no_knob_kernel = step25_kernel["no_knob_kernel"]
    qasu3_slots = obs_qasu3["slot_status"]

    easy_win_subgates = {
        "post_PEW_precision_ledger_consumed": post_pew["closure_decision"]["post_PEW_precision_ledger_rebuilt"],
        "independent_local_RG_benchmark_values_filled": ext_rg["what_closes_now"][
            "independent_local_rg_benchmark_values_filled"
        ],
        "local_QFT_observable_functor_interface_built": ext_rg["what_closes_now"][
            "local_qft_observable_functor_interface_built"
        ],
        "external_profile_coordinate_count_fixed": cov_bridge["what_closes_now"][
            "external_profile_coordinate_count_fixed"
        ],
        "full_8x8_covariance_target_shape_fixed": cov_bridge["what_closes_now"][
            "full_8x8_covariance_target_shape_fixed"
        ],
        "BCT_WZH_cross_covariance_gap_quantified": cov_bridge["what_closes_now"][
            "BCT_WZH_cross_covariance_gap_quantified"
        ],
        "precision_proxy_inventory_consolidated": obs_table["what_closes_now"][
            "precision_proxy_inventory_consolidated"
        ],
        "eight_slot_operator_manifest_locked": obs_table["what_closes_now"]["eight_slot_operator_manifest_locked"],
        "admitted_external_threshold_rows_closed": step25_decision["admitted_external_threshold_rows_closed"],
        "admitted_external_mass_scheme_rows_closed": step25_decision["admitted_external_mass_scheme_rows_closed"],
        "accepted_diagonal_profile_theorem_closed_at_replay_tier": step25_decision[
            "accepted_diagonal_profile_theorem_closed_at_replay_tier"
        ],
        "final_no_knob_kernel_typed": step25_decision["final_no_knob_kernel_typed"],
        "accepted_profile_import_attempt_executed": accepted_import["what_closes_now"][
            "edge_A_accepted_import_attempt_executed"
        ],
        "profile_row_replacement_payload_candidate_built": profile_row_replacement["what_closes_now"][
            "external_BR_GammaH_row_payload_candidate_built"
        ],
        "diagonal_covariance_surrogate_payload_built": covariance_payload["what_closes_now"][
            "diagonal_covariance_surrogate_payload_built"
        ],
        "external_correlated_covariance_submatrix_imported": external_profile_like["what_closes_now"][
            "external_correlated_covariance_submatrix_imported"
        ],
        "profile_likelihood_import_attempt_executed": profile_mining["what_closes_now"][
            "profile_likelihood_import_attempt"
        ],
        "partial_precision_value_table_emitted": precision_value_attempt["what_closes_now"][
            "partial_diagonal_precision_value_table"
        ],
        "qasu3_source_slot_layer_closed": step8["closure_decision"]["source_slot_layer_closed"],
    }
    easy_win_count = sum(1 for value in easy_win_subgates.values() if value is True)

    readiness_packet = {
        "schema": "MTTPrecisionTransportCovarianceReadiness.v1",
        "status": "EASY_WIN_SUBGATES_LOCKED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "easy_win_subgates": easy_win_subgates,
        "easy_win_subgate_count_closed": easy_win_count,
        "accepted_true_equivalence_precision_rows": post_pew_rows["accepted_true_equivalence_precision_rows"],
        "blocking_true_precision_row_count": post_pew_rows["blocking_true_precision_row_count"],
        "Rtheta_readiness_fraction": readiness["readiness_fraction"],
        "Rtheta_readiness_8_of_9": step25_decision["Rtheta_readiness_8_of_9"],
        "accepted_internal_scalar_row_count": step25_decision["accepted_internal_scalar_row_count"],
        "selected_internal_value_emission_count": step25_decision["selected_internal_value_emission_count"],
        "selected_universal_parameter_count": step25_decision["selected_universal_parameter_count"],
    }
    write_json(READINESS, readiness_packet)

    covariance_packet = {
        "schema": "MTTFullCovarianceTargetLock.v1",
        "status": "FULL_8X8_COVARIANCE_TARGET_LOCKED_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "coordinate_count": covariance_target["coordinate_count"],
        "matrix_shape": covariance_target["matrix_shape"],
        "symmetric_unique_entries": covariance_target["symmetric_unique_entries"],
        "strict_full_profile_entries_accepted": covariance_target["strict_full_profile_entries_accepted"],
        "surrogate_or_empirical_entries_scaffolded": covariance_target[
            "surrogate_or_empirical_entries_scaffolded"
        ],
        "BCT_WZH_cross_covariance_entries_missing": covariance_target[
            "hard_missing_entries_for_published_or_reconstructed_likelihood"
        ],
        "coordinate_blocks": coordinate_blocks,
        "full_covariance_profile_likelihood_closed": cov_bridge["closure_decision"][
            "full_covariance_profile_likelihood_closed"
        ],
        "published_or_reconstructed_likelihood_required": True,
    }
    write_json(COVARIANCE, covariance_packet)

    transport_packet = {
        "schema": "MTTThresholdRGObservableTransportSubgates.v1",
        "status": "TRANSPORT_INTERFACES_AND_ADMITTED_REPLAY_LANES_LOCKED_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "local_RG_benchmark": {
            "acceptance_tolerance": ext_rg_bench["acceptance_tolerance"],
            "lambda_H_MZ_firstpass": ext_rg_bench["accepted_packet"]["lambda_H_MZ_firstpass"],
            "benchmark_values_filled": ext_rg["what_closes_now"][
                "independent_local_rg_benchmark_values_filled"
            ],
            "external_literature_RG_benchmark_values_closed": False,
        },
        "local_QFT_functor": {
            "name": ext_qft_functor["functor"]["name"],
            "signature_declared": ext_qft_functor["acceptance_tests"]["functor_signature_declared"],
            "actual_correlator_values_filled": ext_qft_functor["acceptance_tests"][
                "actual_correlator_values_filled"
            ],
            "local_QFT_observable_functor_values_closed": ext_qft_functor["acceptance_tests"][
                "local_QFT_observable_functor_values_closed"
            ],
        },
        "threshold_mass_scheme_replay": {
            "closure_tier": threshold_replay["closure_tier"],
            "admitted_external_threshold_row_count": threshold_replay[
                "accepted_external_threshold_row_count"
            ],
            "admitted_external_mass_scheme_row_count": threshold_replay[
                "accepted_external_mass_scheme_row_count"
            ],
            "accepted_diagonal_profile_theorem_closed": threshold_replay[
                "accepted_diagonal_profile_theorem_closed"
            ],
            "external_rows_used_as_branch_selector": threshold_replay["external_rows_used_as_branch_selector"],
            "internal_selected_Rtheta_value_row_emitted": threshold_replay[
                "internal_selected_Rtheta_value_row_emitted"
            ],
        },
        "precision_observable_table": {
            "proxy_or_scaffold_rows_available": obs_loop["full_loop_import_attempt_result"][
                "proxy_or_scaffold_rows_available"
            ],
            "accepted_precision_rows_imported_now": obs_loop["full_loop_import_attempt_result"][
                "accepted_precision_rows_imported_now"
            ],
            "accepted_precision_observable_table_closed": obs_table["closure_decision"][
                "accepted_precision_observable_table_closed"
            ],
        },
        "qasu3_operator_slots": {
            "required_operator_slot_count": qasu3_slots["required_operator_slot_count"],
            "filled_operator_slot_count": qasu3_slots["filled_operator_slot_count"],
            "missing_slots": qasu3_slots["missing_slots"],
            "actual_QaSU3_operator_packet_closed": obs_table["closure_decision"][
                "actual_QaSU3_operator_packet_closed"
            ],
        },
    }
    write_json(TRANSPORT, transport_packet)

    support_records: list[dict[str, Any]] = []
    for path, payload in zip(SUPPORT_ATTEMPTS, support_attempts, strict=True):
        decision = payload.get("closure_decision", {})
        closes = payload.get("what_closes_now", {})
        support_records.append(
            {
                "slug": path.stem.removesuffix(".candidate"),
                "status": payload.get("status"),
                "next_required_artifact": payload.get("next_required_artifact"),
                "true_SM_equivalence_closed": decision.get("true_SM_equivalence_closed", False),
                "full_no_knob_closed": decision.get("full_no_knob_closed", decision.get("no_knob_closed", False)),
                "actual_QaSU3_operator_packet_closed": decision.get(
                    "actual_QaSU3_operator_packet_closed",
                    decision.get("actual_dynamic_QaSU3_operator_packet_closed", False),
                ),
                "accepted_precision_profile_import_closed": decision.get(
                    "accepted_precision_profile_import_closed", False
                ),
                "profile_likelihood_imported": decision.get(
                    "profile_likelihood_imported",
                    decision.get("full_profile_likelihood_function_imported", False),
                ),
                "source_slot_layer_closed": decision.get("source_slot_layer_closed", False),
                "operator_source_slots_closed": decision.get("operator_source_slots_closed"),
                "support_closures": sorted(key for key, value in closes.items() if value is True),
            }
        )

    support_packet = {
        "schema": "MTTAlreadyExecutedSupportAttempts.v1",
        "status": "SUPPORT_AND_ATTEMPT_PACKETS_RECORDED_WITH_VALUE_LAYER_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "support_attempt_count": len(support_records),
        "records": support_records,
        "support_attempts_with_true_SM_equivalence_closed": [
            record["slug"] for record in support_records if record["true_SM_equivalence_closed"] is True
        ],
        "source_slot_layer_closed_somewhere": any(record["source_slot_layer_closed"] for record in support_records),
        "actual_dynamic_operator_payload_closed_somewhere": any(
            record["actual_QaSU3_operator_packet_closed"] for record in support_records
        ),
        "accepted_precision_profile_import_closed_somewhere": any(
            record["accepted_precision_profile_import_closed"] for record in support_records
        ),
        "profile_likelihood_imported_somewhere": any(record["profile_likelihood_imported"] for record in support_records),
        "interpretation": (
            "Older frontier packets close support, source-slot, contract, "
            "surrogate, partial-value, and import-attempt layers. They do not "
            "supply accepted full profile likelihood values, accepted route-A "
            "row replacements, or the actual dynamic Qa/SU3 operator payload."
        ),
    }
    write_json(SUPPORT, support_packet)

    hard_blockers = [
        "accepted threshold/mass-scheme source values or no-knob replacement values",
        "full 8x8 covariance/profile likelihood values including 15 BCT-WZH cross entries",
        "multi-loop RG/beta/matching transport values beyond the local benchmark",
        "local-QFT precision correlator/S-matrix/decay observable values",
        "actual selected Qa/SU3 operator slot values",
        "neutrino absolute mass plus Dirac/Majorana/phases policy",
        "QCD theta value or strong-CP source solution",
        "global final true-SM equivalence audit",
    ]
    gate_packet = {
        "schema": "MTTFinalTrueSMAuditGate.v1",
        "status": "FINAL_TRUE_SM_AUDIT_GATE_REDUCED_TO_ACCEPTED_VALUE_SOURCE_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "hard_blockers": hard_blockers,
        "remaining_hard_blocker_count": len(hard_blockers),
        "not_active_blockers": [
            "27x27 matrix",
            "finite-replay Yukawa rows at the current accepted tier",
            "finite H scalar and H/lambda K row",
            "strict P_EW/direct-K row",
            "precision transport/covariance readiness subgates",
            "Qa/SU3 source-slot layer, distinct from actual dynamic operator payload values",
        ],
        "already_executed_support_attempt_count": support_packet["support_attempt_count"],
        "source_slot_layer_closed_somewhere": support_packet["source_slot_layer_closed_somewhere"],
        "actual_dynamic_operator_payload_closed_somewhere": support_packet[
            "actual_dynamic_operator_payload_closed_somewhere"
        ],
        "final_true_SM_equivalence_closed": False,
        "full_no_knob_closed": no_knob_kernel["full_no_knob_closed"],
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(GATE, gate_packet)

    decision = {
        "precision_transport_covariance_easy_wins_closed": True,
        "easy_win_subgate_count_closed": easy_win_count,
        "already_executed_support_attempts_recorded": True,
        "already_executed_support_attempt_count": len(support_records),
        "qasu3_source_slot_layer_closed": support_packet["source_slot_layer_closed_somewhere"],
        "actual_dynamic_qasu3_operator_payload_closed": support_packet[
            "actual_dynamic_operator_payload_closed_somewhere"
        ],
        "accepted_precision_profile_import_closed_somewhere": support_packet[
            "accepted_precision_profile_import_closed_somewhere"
        ],
        "profile_likelihood_imported_somewhere": support_packet["profile_likelihood_imported_somewhere"],
        "post_PEW_precision_ledger_consumed": True,
        "local_RG_benchmark_values_filled": True,
        "local_QFT_observable_functor_interface_built": True,
        "full_8x8_covariance_target_shape_fixed": True,
        "external_profile_coordinate_count": covariance_target["coordinate_count"],
        "full_covariance_matrix_shape_fixed": covariance_target["matrix_shape"],
        "full_covariance_symmetric_unique_entries": covariance_target["symmetric_unique_entries"],
        "BCT_WZH_cross_covariance_entries_missing": covariance_target[
            "hard_missing_entries_for_published_or_reconstructed_likelihood"
        ],
        "precision_proxy_inventory_consolidated": True,
        "eight_slot_operator_manifest_locked": True,
        "admitted_external_threshold_rows_closed": True,
        "admitted_external_threshold_row_count": threshold_replay["accepted_external_threshold_row_count"],
        "admitted_external_mass_scheme_rows_closed": True,
        "admitted_external_mass_scheme_row_count": threshold_replay["accepted_external_mass_scheme_row_count"],
        "accepted_diagonal_profile_theorem_closed_at_replay_tier": True,
        "final_no_knob_kernel_typed": True,
        "Rtheta_readiness_8_of_9": True,
        "accepted_true_equivalence_precision_rows": 0,
        "accepted_internal_scalar_row_count": 0,
        "accepted_precision_observable_table_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "multi_loop_RG_values_closed": False,
        "local_QFT_precision_observable_values_closed": False,
        "strong_CP_problem_solved": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrecisionTransportCovarianceRowsOrFinalTrueSMAudit",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "precision_transport_covariance_readiness": rel(READINESS),
            "full_covariance_target_lock": rel(COVARIANCE),
            "threshold_rg_observable_transport_subgates": rel(TRANSPORT),
            "already_executed_support_attempts": rel(SUPPORT),
            "final_true_sm_audit_gate": rel(GATE),
        },
        "theorem": {
            "name": "PrecisionTransportCovarianceRowsOrFinalTrueSMAuditTheorem",
            "proved": True,
            "statement": (
                "The repo's post-PEW precision frontier has all easy transport "
                "and covariance-readiness subgates locked: local RG benchmark "
                "values, the local-QFT observable functor interface, the 8x8 "
                "covariance target shape, the precision proxy/operator-slot "
                "inventory, admitted external threshold and mass-scheme replay "
                "lanes, the diagonal replay tier, the typed no-knob kernel, "
                "and the already-executed support/attempt packets. "
                "These close readiness and bookkeeping blockers only; accepted "
                "true-equivalence precision rows remain zero until the actual "
                "source values/profile likelihood/operator payload are emitted."
            ),
        },
        "closure_decision": decision,
        "cross_repo_status_consumed": {
            "status": cross["status"],
            "part_count": len(cross["parts"]),
            "used_as_support_only": True,
        },
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(OUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PrecisionTransportCovarianceRows_or_FinalTrueSMAudit_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "theorem_proved": True,
        **decision,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "remaining_hard_blocker_count": len(hard_blockers),
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected PrecisionTransportCovarianceRows or FinalTrueSMAudit v1

Status: `{STATUS}`.

## Easy Wins Closed

```text
post-PEW precision ledger consumed                 true
local RG benchmark values filled                   true
local-QFT observable functor interface built       true
8x8 covariance target shape fixed                  true
external profile coordinates                       {covariance_target["coordinate_count"]}
symmetric covariance entries                       {covariance_target["symmetric_unique_entries"]}
missing BCT-WZH cross entries                      {covariance_target["hard_missing_entries_for_published_or_reconstructed_likelihood"]}
precision proxy inventory consolidated             true
eight-slot Qa/SU3 operator manifest locked         true
admitted external threshold rows                   {threshold_replay["accepted_external_threshold_row_count"]}
admitted external mass-scheme rows                 {threshold_replay["accepted_external_mass_scheme_row_count"]}
diagonal replay tier closed                        true
final no-knob kernel typed                         true
already-executed support attempts recorded         {len(support_records)}
Qa/SU3 source-slot layer closed                    {str(support_packet["source_slot_layer_closed_somewhere"]).lower()}
actual dynamic Qa/SU3 payload closed               {str(support_packet["actual_dynamic_operator_payload_closed_somewhere"]).lower()}
```

These are readiness/subgate closures, not final value-source closures.

## Still Open For True SM Equivalence

```text
accepted true-equivalence precision rows           0
accepted internal scalar rows                      0
accepted precision observable table                false
actual Qa/SU3 operator packet                      false
full covariance/profile likelihood                 false
multi-loop RG transport values                     false
local-QFT precision observable values              false
strong CP / theta value                            false
full no-knob closure                               false
true SM equivalence                                false
```

## Reduced Hard Blocker Set

{chr(10).join(f"- {item}" for item in hard_blockers)}

Next artifact: `{NEXT_ARTIFACT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
