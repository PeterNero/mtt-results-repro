"""Build true-equivalence precision value table or actual Qa/SU3 operator upgrade."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRECISION_TABLE = PACKET_DIR / "true_equivalence_precision_value_table_manifest.packet.json"
QASU3_CONTRACT = PACKET_DIR / "actual_qasu3_operator_upgrade_contract.packet.json"
ROUTE = PACKET_DIR / "dual_route_true_equivalence_decision.packet.json"
CUTSET = PACKET_DIR / "next_value_emission_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TrueEquivalencePrecisionValueTable_or_ActualQaSU3OperatorUpgrade_v1.md"

STATUS = "MTT_SELECTED_TRUEEQUIVALENCEPRECISIONVALUETABLE_OR_ACTUALQASU3OPERATORUPGRADE_BUILT_DUAL_ROUTE_CONTRACT_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor.candidate.json")
    promotion = load(
        DATA
        / "selected_precisionobservablepromotionpolicy_or_loopqftvalues"
        / "observable_tier_promotion_matrix.packet.json"
    )
    qasu3_gate = load(
        DATA
        / "selected_precisionqftobservablerows_or_actualqasu3packet"
        / "actual_qasu3_packet_gate_after_qft_rows.packet.json"
    )
    profile_status = load(
        DATA
        / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor"
        / "nonhiggs_precision_profile_status.packet.json"
    )
    functor_status = load(
        DATA
        / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor"
        / "local_qft_observable_functor_status.packet.json"
    )

    precision_rows = [
        {
            "row_family": "nonHiggs_full_covariance_profile_values",
            "current_support": rel(
                DATA
                / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor"
                / "nonhiggs_precision_profile_status.packet.json"
            ),
            "ready_as_contract": True,
            "values_filled": False,
            "required_value_payload": [
                "published or reconstructed full covariance/profile matrix",
                "basis declaration with redundant hypercharge treatment",
                "observable residual acceptance rule",
                "positive semidefinite covariance check or likelihood workspace",
            ],
        },
        {
            "row_family": "precision_local_QFT_observable_values",
            "current_support": rel(
                DATA
                / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor"
                / "local_qft_observable_functor_status.packet.json"
            ),
            "ready_as_contract": True,
            "values_filled": False,
            "required_value_payload": [
                "loop-corrected correlator/S-matrix/decay rows",
                "declared renormalization scheme and loop order",
                "threshold matching and pole/running mass maps",
                "covariance propagation into the locked observable suite",
            ],
        },
        {
            "row_family": "Higgs_precision_completion",
            "current_support": rel(DATA / "selected_higgsfinalsmparityprofilepolicy_or_remainingrouteakernels.candidate.json"),
            "ready_as_contract": True,
            "values_filled": False,
            "required_value_payload": [
                "route-A kernels for H_to_Z_gamma, H_to_WW_star, and H_to_ZZ_star",
                "or stronger public likelihood/profile replacement",
                "branching-ratio and total-width precision covariance propagation",
            ],
        },
    ]

    precision_table = {
        "schema": "MTTTrueEquivalencePrecisionValueTableManifest.v1",
        "status": "PRECISION_VALUE_TABLE_CONTRACT_BUILT_VALUES_OPEN",
        "promotion_matrix_source": rel(
            DATA
            / "selected_precisionobservablepromotionpolicy_or_loopqftvalues"
            / "observable_tier_promotion_matrix.packet.json"
        ),
        "profile_status_source": rel(
            DATA
            / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor"
            / "nonhiggs_precision_profile_status.packet.json"
        ),
        "functor_status_source": rel(
            DATA
            / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor"
            / "local_qft_observable_functor_status.packet.json"
        ),
        "row_contracts": precision_rows,
        "all_current_rows_classified": promotion["all_current_rows_classified"],
        "any_row_promoted_to_true_precision_equivalence": promotion["any_row_promoted_to_true_precision_equivalence"],
        "precision_value_table_contract_ready": True,
        "precision_values_filled": False,
        "accepted_for_true_SM_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    qasu3_contract = {
        "schema": "MTTActualQaSU3OperatorUpgradeContract.v1",
        "status": "ACTUAL_QASU3_OPERATOR_UPGRADE_CONTRACT_BUILT_SOURCE_VALUES_OPEN",
        "qasu3_gate_source": rel(
            DATA
            / "selected_precisionqftobservablerows_or_actualqasu3packet"
            / "actual_qasu3_packet_gate_after_qft_rows.packet.json"
        ),
        "current_gate_status": qasu3_gate["status"],
        "actual_packet_closed_now": False,
        "qft_rows_change_source_status": qasu3_gate["qft_rows_change_source_status"],
        "required_source_payload": [
            "selected Qa/SU3 color/operator packet with source-side representation data",
            "mapped anomaly/Ward/Freed-Witten or Bianchi certificate for the actual packet",
            "selected D_E/rho_E/operator data replacing parity-interface substitute",
            "typed monad/Cech/section-ring maps as actual operator maps",
            "attachment of precision observable rows to that actual selected packet",
        ],
        "forbidden_promotions": qasu3_gate["why_still_open"],
        "accepted_for_true_SM_equivalence": False,
        "accepted_for_no_knob": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route = {
        "schema": "MTTDualRouteTrueEquivalenceDecision.v1",
        "status": "DUAL_ROUTE_CONTRACTS_BUILT_NO_ROUTE_CLOSED",
        "route_A_precision_value_table": {
            "contract_ready": True,
            "values_filled": False,
            "can_close_true_SM_equivalence_now": False,
        },
        "route_B_actual_QaSU3_operator_upgrade": {
            "contract_ready": True,
            "source_values_filled": False,
            "can_close_true_SM_equivalence_now": False,
        },
        "route_interaction": (
            "The two routes are complementary superset paths: Route A completes precision replay values "
            "without changing source selection; Route B upgrades the source/operator packet. Neither route "
            "may use observed constants or downstream replay residuals as selectors."
        ),
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextValueEmissionCutset.v1",
        "status": "NEXT_CUTSET_IS_VALUE_EMISSION_NOT_BOOKKEEPING",
        "minimal_next_payloads": [
            "fill one full non-Higgs covariance/profile matrix with provenance and PSD/likelihood validation",
            "or emit actual selected Qa/SU3 operator/source packet values",
            "or fill precision local-QFT observable rows with loop/scheme/threshold covariance semantics",
        ],
        "bookkeeping_remaining": False,
        "value_emission_required": True,
        "recommended_next_artifact": "MTT_Selected_PrecisionValueEmissionAttempt_or_QaSU3SourcePayloadFill_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTrueEquivalencePrecisionValueTableOrActualQaSU3OperatorUpgrade",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor.candidate.json"),
            "promotion_matrix": rel(
                DATA
                / "selected_precisionobservablepromotionpolicy_or_loopqftvalues"
                / "observable_tier_promotion_matrix.packet.json"
            ),
            "qasu3_gate": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "actual_qasu3_packet_gate_after_qft_rows.packet.json"
            ),
        },
        "output_packets": {
            "true_equivalence_precision_value_table_manifest": rel(PRECISION_TABLE),
            "actual_qasu3_operator_upgrade_contract": rel(QASU3_CONTRACT),
            "dual_route_true_equivalence_decision": rel(ROUTE),
            "next_value_emission_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "TrueEquivalenceDualRouteContractTheorem",
            "proved": True,
            "statement": (
                "The current SM-parity-closed repo has no remaining pure bookkeeping step that can honestly "
                "close true SM equivalence. The next progress must be value emission on one of two legal "
                "superset routes: a precision value/profile table with loop/scheme/covariance semantics, "
                "or an actual selected Qa/SU3 source/operator upgrade. Both contracts are now explicit; "
                "neither route is filled."
            ),
        },
        "what_closes_now": {
            "precision_value_table_contract": True,
            "actual_QaSU3_operator_upgrade_contract": True,
            "dual_route_decision": True,
            "bookkeeping_to_value_emission_cutset": True,
        },
        "what_remains_open": {
            "true_SM_equivalence": True,
            "no_knob_closure": True,
            "precision_values_filled": True,
            "actual_QaSU3_operator_packet_filled": True,
            "precision_local_QFT_values": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "precision_value_table_contract_ready": True,
            "actual_QaSU3_operator_upgrade_contract_ready": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "dependency_flags": {
            "nonHiggs_profile_accepted_for_SM_parity": profile_status["accepted_for_SM_parity_replay"],
            "tree_QFT_functor_accepted_for_SM_parity": functor_status["accepted_for_SM_parity_replay"],
            "any_current_row_promoted_to_true_precision": promotion["any_row_promoted_to_true_precision_equivalence"],
            "qasu3_gate_still_open": qasu3_gate["status"] == "ACTUAL_QASU3_PACKET_GATE_REMAINS_OPEN_AFTER_QFT_TREE_ROWS",
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_TrueEquivalencePrecisionValueTable_or_ActualQaSU3OperatorUpgrade_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "precision_value_table_contract_ready": True,
        "actual_QaSU3_operator_upgrade_contract_ready": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected TrueEquivalencePrecisionValueTable or ActualQaSU3OperatorUpgrade v1

Status: `{STATUS}`.

This artifact closes the next planning layer but not true SM equivalence.

The remaining progress is no longer bookkeeping. It requires value emission on
one of two legal superset routes:

- Route A: fill precision value/profile tables with loop, threshold, scheme, and
  covariance semantics.
- Route B: emit the actual selected Qa/SU3 operator/source packet and attach the
  precision observables to it.

Both route contracts are explicit. Neither route is filled, and downstream
measured replay values remain forbidden as source selectors.
"""

    for path, payload in [
        (PRECISION_TABLE, precision_table),
        (QASU3_CONTRACT, qasu3_contract),
        (ROUTE, route),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
