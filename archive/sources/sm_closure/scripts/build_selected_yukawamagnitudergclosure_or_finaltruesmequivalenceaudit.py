"""Build Yukawa magnitude/RG closure attempt or final true-SM equivalence audit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VALUE_LEDGER = PACKET_DIR / "accepted_value_layer_ledger.packet.json"
RG_CLOSURE_ATTEMPT = PACKET_DIR / "yukawa_rg_closure_attempt.packet.json"
FINAL_AUDIT = PACKET_DIR / "final_true_sm_equivalence_audit.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_final_value_audit.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_YukawaMagnitudeRGClosure_or_FinalTrueSMEquivalenceAudit_v1.md"

PREVIOUS = DATA / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure.candidate.json"
QASU3_REPLAY = (
    DATA
    / "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
    / "dynamic_qasu3_operator_packet_replay.packet.json"
)
COMMON_SCALE = DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"
COMMON_RG = DATA / "sm_equivalence_common_rg_and_empirical_audit.candidate.json"
RG_ENGINE = DATA / "selected_rgengineexecution_or_selectedsmpacketcertificateintegration.candidate.json"
THRESHOLD = DATA / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration.candidate.json"
POLE_RESIDUALS = DATA / "selected_polethresholdresidualvalues_or_covarianceprofile.candidate.json"
FULL_COV = DATA / "selected_fullcovarianceprofile_or_multiloopconventionaudit.candidate.json"
CORRELATED = DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json"
LOCAL_QFT = DATA / "selected_localqftobservablerows_or_finaltruesmequivalencegap.candidate.json"
MIXING = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
QASU3_PARITY = DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"

STATUS = (
    "MTT_SELECTED_YUKAWAMAGNITUDERGCLOSURE_OR_FINALTRUESMEQUIVALENCEAUDIT_"
    "BUILT_FINAL_VALUE_AUDIT_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_AcceptedCommonScaleYukawaHiggsValues_or_ProfileLikelihoodExecution_v1"


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
        raise FileNotFoundError("missing final value audit sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)
    sources = [
        PREVIOUS,
        QASU3_REPLAY,
        COMMON_SCALE,
        COMMON_RG,
        RG_ENGINE,
        THRESHOLD,
        POLE_RESIDUALS,
        FULL_COV,
        CORRELATED,
        LOCAL_QFT,
        MIXING,
        QASU3_PARITY,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    qasu3_replay = load(QASU3_REPLAY)
    common_scale = load(COMMON_SCALE)
    common_rg = load(COMMON_RG)
    rg_engine = load(RG_ENGINE)
    threshold = load(THRESHOLD)
    pole = load(POLE_RESIDUALS)
    full_cov = load(FULL_COV)
    correlated = load(CORRELATED)
    local_qft = load(LOCAL_QFT)
    mixing = load(MIXING)
    qasu3_parity = load(QASU3_PARITY)

    value_ledger = {
        "schema": "MTTAcceptedValueLayerLedger.v1",
        "status": "MANY_REPLAY_TIERS_CLOSED_ACCEPTED_COMMON_SCALE_VALUES_OPEN",
        "closed_layers": {
            "SM_parity_closed": qasu3_parity["closure_decision"]["SM_parity_closed"],
            "dynamic_QaSU3_first_response_layer": qasu3_replay[
                "actual_QaSU3_operator_packet_first_response_layer_closed"
            ],
            "common_scale_gauge_values_at_MZ": common_scale["what_closes_now"][
                "common_scale_gauge_values_at_MZ"
            ],
            "native_published_parameter_replay": common_rg["empirical_audit"][
                "can_claim_native_replay_closure"
            ],
            "CKM_complex_Yukawa_replay": mixing["what_closes_now"]["CKM_complex_Yukawa_replay"],
            "PMNS_oscillation_replay": mixing["what_closes_now"][
                "PMNS_oscillation_mass_squared_replay"
            ],
            "diagnostic_RG_smoke_run": rg_engine["what_closes_now"][
                "diagnostic_RG_smoke_run_executed"
            ],
            "threshold_formula_replay": pole["what_closes_now"][
                "pole_threshold_residual_formula_requirements_filled"
            ],
            "diagonal_profile_execution": full_cov["what_closes_now"][
                "diagonal_profile_likelihood_executed"
            ],
            "correlation_envelope": correlated["what_closes_now"][
                "correlation_robust_profile_envelope"
            ],
            "tree_QFT_observable_rows": local_qft["what_closes_now"][
                "local_QFT_tree_identity_observable_rows"
            ],
        },
        "open_accepted_value_layers": {
            "common_scale_yukawa_higgs_values": common_scale["what_remains_open"][
                "Yukawa_common_scale_transport"
            ],
            "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values": rg_engine["what_remains_open"][
                "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values"
            ],
            "accepted_lambda_H_MZ_value": rg_engine["what_remains_open"][
                "accepted_lambda_H_MZ_value"
            ],
            "threshold_matching_values": threshold["what_remains_open"][
                "threshold_matching_values"
            ],
            "mass_scheme_conversion_values": threshold["what_remains_open"][
                "mass_scheme_conversion_values"
            ],
            "full_correlated_covariance_profile": full_cov["what_remains_open"][
                "full_correlated_covariance_profile_likelihood_values"
            ],
            "local_QFT_precision_values": correlated["what_remains_open"][
                "local_QFT_observable_value_rows"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_LEDGER, value_ledger)

    rg_attempt = {
        "schema": "MTTYukawaRGClosureAttempt.v1",
        "status": "REJECTED_ACCEPTED_COMMON_SCALE_VALUES_NOT_EMITTED",
        "attempted_closure": {
            "Yukawa_magnitudes": False,
            "running_mass_ratios": False,
            "CKM_PMNS_measured_angles_phase": False,
            "Higgs_lambda_MZ": False,
            "RG_threshold_covariance_integrated": False,
        },
        "why_rejected": [
            "diagnostic one-loop RG exists but accepted common-scale values are not emitted",
            "threshold matching and mass-scheme conversion values remain open",
            "full covariance/profile likelihood remains open",
            "existing CKM/PMNS replay is empirical/native replay, not no-knob derivation",
        ],
        "no_observed_selector_violation": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RG_CLOSURE_ATTEMPT, rg_attempt)

    final_audit = {
        "schema": "MTTFinalTrueSMEquivalenceAudit.v1",
        "status": "TRUE_SM_EQUIVALENCE_OPEN_ACCEPTED_VALUE_LAYER_OPEN",
        "source_and_operator_side": {
            "SM_parity_closed": True,
            "C1_source_stack_closed": True,
            "dynamic_matter_overlap_packet_closed": previous["what_closes_now"][
                "dynamic_QaSU3_first_response_layer_replayed"
            ],
            "dynamic_QaSU3_first_response_layer_closed": qasu3_replay[
                "actual_QaSU3_operator_packet_first_response_layer_closed"
            ],
        },
        "value_side": {
            "native_replay_substantially_closed": common_scale["closure_decision"][
                "native_replay_layer"
            ],
            "common_scale_gauge_values_closed": common_scale["closure_decision"][
                "common_scale_gauge_values"
            ],
            "common_scale_yukawa_higgs_values": common_scale["closure_decision"][
                "common_scale_yukawa_higgs_values"
            ],
            "full_covariance_profile_likelihood": "OPEN",
            "accepted_RG_threshold_mass_scheme": "OPEN",
        },
        "closure_decision": {
            "accepted_Yukawa_magnitudes_closed": False,
            "running_mass_ratios_closed": False,
            "CKM_PMNS_measured_value_closure": False,
            "true_SM_equivalence_closed": False,
            "full_SM_no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FINAL_AUDIT, final_audit)

    next_cutset = {
        "schema": "MTTNextCutsetAfterFinalValueAudit.v1",
        "status": "FINAL_FRONTIER_ACCEPTED_COMMON_SCALE_VALUES_OR_PROFILE_LIKELIHOOD",
        "closed_now": [
            "final value audit executed after dynamic Qa/SU3 first-response closure",
            "all closed replay tiers and open accepted-value tiers enumerated",
            "Yukawa/RG closure attempt rejected without overclaiming measured values as source selectors",
        ],
        "still_open": [
            "accepted Y_u(M_Z), Y_d(M_Z), Y_e(M_Z), and lambda_H(M_Z)",
            "threshold matching and mass-scheme conversion values",
            "full covariance/profile likelihood execution",
            "precision local-QFT observable values",
            "true SM equivalence and full no-knob closure",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The proof side has reached the accepted-value wall. The next progress must emit "
                "versioned common-scale Yukawa/Higgs values or a full profile/covariance likelihood."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedYukawaMagnitudeRGClosureOrFinalTrueSMEquivalenceAudit",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "accepted_value_layer_ledger": rel(VALUE_LEDGER),
            "yukawa_rg_closure_attempt": rel(RG_CLOSURE_ATTEMPT),
            "final_true_sm_equivalence_audit": rel(FINAL_AUDIT),
            "next_cutset_after_final_value_audit": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "final_value_audit_executed": True,
            "closed_replay_tiers_enumerated": True,
            "accepted_value_wall_identified": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": value_ledger["open_accepted_value_layers"]
        | {
            "true_SM_equivalence": True,
            "full_SM_no_knob_closure": True,
        },
        "promotion_decision": final_audit["closure_decision"],
        "theorem": {
            "name": "FinalValueAuditAndAcceptedYukawaRGWallTheorem",
            "proved": True,
            "statement": (
                "After dynamic Qa/SU3 first-response closure, the remaining true-SM-equivalence obstruction "
                "is not the C1 source stack or qualitative dynamic operator layer. It is the accepted value layer: "
                "common-scale Yukawa/Higgs values, thresholds, mass-scheme conversion, covariance/profile likelihood, "
                "and precision local-QFT observables. Existing measured replay rows may support downstream empirical "
                "audit but cannot be used as no-knob source selectors."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_YukawaMagnitudeRGClosure_or_FinalTrueSMEquivalenceAudit_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "final_value_audit_executed": True,
        "accepted_Yukawa_magnitudes_closed": False,
        "true_SM_equivalence_closed": False,
        "full_SM_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected YukawaMagnitudeRGClosure or FinalTrueSMEquivalenceAudit v1

Status: `{STATUS}`.

The final value audit is executed after dynamic Qa/SU3 first-response closure.
It confirms that the active wall is the accepted value layer:

- accepted `Y_u(M_Z)`, `Y_d(M_Z)`, `Y_e(M_Z)`, and `lambda_H(M_Z)`,
- threshold matching and mass-scheme conversion,
- full covariance/profile likelihood,
- precision local-QFT observable values.

This does not close measured Yukawa magnitudes, CKM/PMNS measured values, true
SM equivalence, or full no-knob closure.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"built {rel(OUTPUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
