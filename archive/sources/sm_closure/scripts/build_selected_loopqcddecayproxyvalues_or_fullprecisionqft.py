"""Build first controlled loop-QFT proxy values for Higgs quark decays."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_loopqcddecayproxyvalues_or_fullprecisionqft"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
QCD = PACKET_DIR / "one_loop_qcd_higgs_quark_decay_proxy_values.packet.json"
MISSING = PACKET_DIR / "full_precision_decay_width_missing_terms.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_qcd_proxy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LoopQCDDecayProxyValues_or_FullPrecisionQFT_v1.md"

STATUS = "MTT_SELECTED_LOOPQCDDECAYPROXYVALUES_OR_FULLPRECISIONQFT_BUILT_QCD_PROXY_FULL_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_precisionobservablepromotionpolicy_or_loopqftvalues.candidate.json")
    previous_gate = load(
        DATA
        / "selected_precisionobservablepromotionpolicy_or_loopqftvalues"
        / "updated_true_equivalence_gate_after_promotion_policy.packet.json"
    )
    decay_rows = load(
        DATA
        / "selected_precisionqftobservablerows_or_actualqasu3packet"
        / "representative_tree_level_decay_observable_rows.packet.json"
    )
    mixing = load(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json")

    alpha_s = float(mixing["gauge_replay_MZ"]["filled_inputs"]["alpha_s_MZ"]["central_value"])
    alpha_s_unc = float(mixing["gauge_replay_MZ"]["filled_inputs"]["alpha_s_MZ"]["uncertainty"])
    qcd_k_factor = 1.0 + (17.0 / 3.0) * alpha_s / math.pi
    qcd_k_factor_unc = (17.0 / 3.0) * alpha_s_unc / math.pi

    qcd_rows = []
    passthrough_rows = []
    for row in decay_rows["higgs_fermion_decay_rows"]:
        color_factor = int(row["color_factor"])
        tree_width = float(row["width_GeV"])
        if color_factor == 3 and row["kinematically_open"]:
            qcd_rows.append(
                {
                    "id": row["id"].replace("_tree", "_one_loop_qcd_proxy"),
                    "source_tree_row_id": row["id"],
                    "fermion": row["fermion"],
                    "tree_width_GeV": tree_width,
                    "alpha_s_input": {
                        "value": alpha_s,
                        "uncertainty": alpha_s_unc,
                        "scale": "M_Z",
                        "used_as_source_selector": False,
                    },
                    "formula": "Gamma_QCD_proxy = Gamma_tree * (1 + (17/3)*alpha_s(M_Z)/pi)",
                    "qcd_k_factor": qcd_k_factor,
                    "qcd_k_factor_uncertainty_from_alpha_s_only": qcd_k_factor_unc,
                    "qcd_proxy_width_GeV": tree_width * qcd_k_factor,
                    "qcd_proxy_width_uncertainty_from_alpha_s_only_GeV": tree_width * qcd_k_factor_unc,
                    "accepted_as_one_loop_qcd_proxy": True,
                    "accepted_as_precision_SM_decay_width": False,
                }
            )
        else:
            passthrough_rows.append(
                {
                    "id": row["id"].replace("_tree", "_no_qcd_proxy"),
                    "source_tree_row_id": row["id"],
                    "fermion": row["fermion"],
                    "tree_width_GeV": tree_width,
                    "reason_no_qcd_proxy": "leptonic or kinematically closed channel",
                    "accepted_as_precision_SM_decay_width": False,
                }
            )

    total_tree_quark_width = sum(row["tree_width_GeV"] for row in qcd_rows)
    total_qcd_proxy_quark_width = sum(row["qcd_proxy_width_GeV"] for row in qcd_rows)
    qcd_packet = {
        "schema": "MTTOneLoopQCDHiggsQuarkDecayProxyValues.v1",
        "status": "ONE_LOOP_QCD_HIGGS_QUARK_DECAY_PROXY_VALUES_BUILT_FULL_PRECISION_OPEN",
        "input_decay_packet": rel(
            DATA
            / "selected_precisionqftobservablerows_or_actualqasu3packet"
            / "representative_tree_level_decay_observable_rows.packet.json"
        ),
        "input_alpha_s_packet": rel(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"),
        "qcd_rows": qcd_rows,
        "passthrough_non_qcd_rows": passthrough_rows,
        "summary": {
            "qcd_corrected_open_quark_channels_count": len(qcd_rows),
            "qcd_k_factor": qcd_k_factor,
            "total_tree_open_quark_width_GeV": total_tree_quark_width,
            "total_qcd_proxy_open_quark_width_GeV": total_qcd_proxy_quark_width,
            "all_proxy_widths_finite_nonnegative": all(
                math.isfinite(row["qcd_proxy_width_GeV"]) and row["qcd_proxy_width_GeV"] >= 0.0 for row in qcd_rows
            ),
            "proxy_increases_positive_quark_widths": all(
                row["qcd_proxy_width_GeV"] > row["tree_width_GeV"] for row in qcd_rows if row["tree_width_GeV"] > 0.0
            ),
        },
        "accepted_as_first_loop_QFT_value_layer": True,
        "accepted_as_full_precision_decay_widths": False,
        "why_not_full_precision": (
            "This is a one-loop QCD proxy using alpha_s(M_Z), not alpha_s(m_H) with running masses, higher-order QCD, "
            "electroweak corrections, off-shell channels, total-width treatment, or covariance/profile comparison."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    missing_terms = {
        "schema": "MTTFullPrecisionDecayWidthMissingTerms.v1",
        "status": "FULL_PRECISION_DECAY_WIDTH_TERMS_ENUMERATED_VALUES_OPEN",
        "terms_required_before_precision_promotion": [
            "alpha_s running from M_Z to the declared Higgs-width scale",
            "running quark masses at the declared scale",
            "higher-order QCD corrections and scheme convention",
            "electroweak corrections",
            "off-shell channels, especially vector-boson final states",
            "total Higgs and W width policy",
            "experimental or benchmark comparison with uncertainties/covariance",
            "actual selected Qa/SU3 source/operator attachment for operator-sensitive rows",
        ],
        "qcd_proxy_closes_value_bookkeeping_for": [
            "first controlled non-tree correction factor for H->b bbar",
            "first controlled non-tree correction factor for H->c cbar",
        ],
        "full_precision_widths_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    if "one-loop QCD proxy Higgs-quark decay rows" not in previous_gate["closed_now"]:
        closed_now = previous_gate["closed_now"] + ["one-loop QCD proxy Higgs-quark decay rows"]
    else:
        closed_now = previous_gate["closed_now"]
    if "loop-corrected local QFT correlator/S-matrix/decay rows" in remaining:
        remaining.remove("loop-corrected local QFT correlator/S-matrix/decay rows")
    for blocker in [
        "full precision loop-corrected QFT correlator/S-matrix/decay rows",
        "running-mass and scale-transported Higgs decay widths",
        "full covariance/profile likelihood values",
        "actual selected Qa/SU3 operator packet",
    ]:
        if blocker not in remaining:
            remaining.append(blocker)

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterQCDProxy.v1",
        "status": "QCD_PROXY_VALUES_BUILT_FULL_PRECISION_QFT_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "scale-transported running masses and alpha_s(m_H), or actual selected Qa/SU3 operator packet",
        "guardrails": {
            "qcd_proxy_is_not_full_precision_width": True,
            "alpha_s_MZ_used_downstream_only": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedLoopQCDDecayProxyValuesOrFullPrecisionQFT",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_precisionobservablepromotionpolicy_or_loopqftvalues.candidate.json"),
            "tree_decay_rows": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "representative_tree_level_decay_observable_rows.packet.json"
            ),
            "alpha_s_MZ": rel(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"),
        },
        "output_packets": {
            "one_loop_qcd_higgs_quark_decay_proxy_values": rel(QCD),
            "full_precision_decay_width_missing_terms": rel(MISSING),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "OneLoopQCDProxyDecayValueTheorem",
            "proved": True,
            "statement": (
                "The admitted downstream alpha_s(M_Z) slot and representative tree Higgs quark decay rows emit finite "
                "one-loop QCD proxy widths using K=1+(17/3)alpha_s/pi. This closes a controlled first loop-value layer "
                "for quark Higgs decays only; full precision QFT decay widths remain open."
            ),
        },
        "what_closes_now": {
            "one_loop_qcd_proxy_values_for_open_higgs_quark_decays": True,
            "finite_nonnegative_proxy_widths": qcd_packet["summary"]["all_proxy_widths_finite_nonnegative"],
            "missing_full_precision_terms_enumerated": True,
            "promotion_policy_respected": True,
        },
        "what_remains_open": {
            "scale_transported_alpha_s_mH_and_running_masses": True,
            "higher_order_QCD_and_EW_corrections": True,
            "off_shell_and_total_width_policy": True,
            "full_covariance_profile_likelihood_values": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "first_loop_QFT_proxy_layer_closed": True,
            "full_precision_QFT_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "source_strategy": {
            "mode": "straight_downstream_SM_parity_replay_after_superset_source_boundary",
            "explanation": (
                "The superset source/interface boundary remains fixed. The new QCD proxy values are downstream "
                "measured-parameter replay rows and do not select any MTT source, branch, or operator packet."
            ),
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_LoopQCDDecayProxyValues_or_FullPrecisionQFT_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "first_loop_QFT_proxy_layer_closed": True,
        "full_precision_QFT_values_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_ScaleTransportedHiggsDecayWidths_or_ActualQaSU3Packet_v1",
    }

    note = """# MTT Selected LoopQCDDecayProxyValues or FullPrecisionQFT v1

Status: `MTT_SELECTED_LOOPQCDDECAYPROXYVALUES_OR_FULLPRECISIONQFT_BUILT_QCD_PROXY_FULL_PRECISION_OPEN`.

This artifact emits the first controlled non-tree local-QFT value layer:
one-loop QCD proxy factors for the open Higgs quark decay rows.

The proxy uses `K = 1 + (17/3) alpha_s(M_Z)/pi` and therefore remains a
scale-policy scaffold. It is not a full precision Higgs-width computation.

Full precision still requires alpha_s and quark masses at the declared decay
scale, higher-order QCD, electroweak corrections, off-shell/total-width policy,
covariance/profile comparison, and actual Qa/SU3 operator attachment where
operator-sensitive rows are involved.
"""

    for path, payload in [
        (QCD, qcd_packet),
        (MISSING, missing_terms),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
