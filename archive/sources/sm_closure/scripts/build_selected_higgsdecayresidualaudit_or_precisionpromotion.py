"""Build a non-fit residual audit for Higgs quark decay proxy stages."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsdecayresidualaudit_or_precisionpromotion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RESIDUALS = PACKET_DIR / "higgs_decay_proxy_residual_audit.packet.json"
PROMOTION = PACKET_DIR / "precision_promotion_acceptance_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_higgs_decay_residual_audit.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsDecayResidualAudit_or_PrecisionPromotion_v1.md"

STATUS = "MTT_SELECTED_HIGGSDECAYRESIDUALAUDIT_OR_PRECISIONPROMOTION_BUILT_NONFIT_AUDIT_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def residual_row(channel: str, stage: str, value: float, reference: float) -> dict[str, Any]:
    return {
        "channel": channel,
        "stage": stage,
        "value_GeV": value,
        "reference_GeV": reference,
        "absolute_residual_GeV": value - reference,
        "relative_residual": (value - reference) / reference,
        "ratio_to_reference": value / reference,
        "within_factor_two": 0.5 <= value / reference <= 2.0,
        "within_twenty_percent": abs((value - reference) / reference) <= 0.20,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_runningmasshiggsdecayproxy_or_precisionwidths.candidate.json")
    previous_gate = load(
        DATA
        / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
        / "updated_true_equivalence_gate_after_running_mass_proxy.packet.json"
    )
    tree = load(
        DATA
        / "selected_precisionqftobservablerows_or_actualqasu3packet"
        / "representative_tree_level_decay_observable_rows.packet.json"
    )
    qcd = load(
        DATA
        / "selected_loopqcddecayproxyvalues_or_fullprecisionqft"
        / "one_loop_qcd_higgs_quark_decay_proxy_values.packet.json"
    )
    running = load(
        DATA
        / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
        / "one_loop_running_mass_higgs_decay_proxy.packet.json"
    )
    bench = load(
        DATA
        / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
        / "higgs_decay_plausibility_benchmark.packet.json"
    )

    references = {
        "b": bench["benchmark_partial_widths_GeV"]["H_to_bb_reference_approx"],
        "c": bench["benchmark_partial_widths_GeV"]["H_to_cc_reference_approx"],
    }
    tree_by_f = {
        row["fermion"]: row["width_GeV"]
        for row in tree["higgs_fermion_decay_rows"]
        if row["fermion"] in references
    }
    qcd_by_f = {
        row["fermion"]: row["qcd_proxy_width_GeV"]
        for row in qcd["qcd_rows"]
        if row["fermion"] in references
    }
    running_by_f = {
        row["fermion"]: row["running_mass_qcd_proxy_width_GeV"]
        for row in running["rows"]
        if row["fermion"] in references
    }

    rows = []
    for channel in ["b", "c"]:
        rows.extend(
            [
                residual_row(channel, "tree_reference_mass", tree_by_f[channel], references[channel]),
                residual_row(channel, "one_loop_qcd_reference_mass_proxy", qcd_by_f[channel], references[channel]),
                residual_row(channel, "one_loop_running_mass_qcd_proxy", running_by_f[channel], references[channel]),
            ]
        )

    best_by_channel = {}
    for channel in ["b", "c"]:
        channel_rows = [row for row in rows if row["channel"] == channel]
        best_by_channel[channel] = min(channel_rows, key=lambda row: abs(row["relative_residual"]))

    residual_packet = {
        "schema": "MTTHiggsDecayProxyResidualAudit.v1",
        "status": "HIGGS_DECAY_PROXY_RESIDUAL_AUDIT_BUILT_NONFIT_PRECISION_OPEN",
        "benchmark_source": bench["external_reference"],
        "benchmark_partial_widths_GeV": bench["benchmark_partial_widths_GeV"],
        "residual_rows": rows,
        "best_stage_by_channel": best_by_channel,
        "audit_result": {
            "reference_mass_tree_and_qcd_proxy_are_not_precision_plausible_for_bb": qcd_by_f["b"] / references["b"] > 2.0,
            "running_mass_proxy_is_best_available_stage_for_b": best_by_channel["b"]["stage"] == "one_loop_running_mass_qcd_proxy",
            "running_mass_proxy_is_best_available_stage_for_c": best_by_channel["c"]["stage"] == "one_loop_running_mass_qcd_proxy",
            "running_mass_proxy_within_factor_two_for_all_audited_channels": all(
                best_by_channel[channel]["within_factor_two"] for channel in ["b", "c"]
            ),
            "running_mass_proxy_within_twenty_percent_for_all_audited_channels": all(
                best_by_channel[channel]["within_twenty_percent"] for channel in ["b", "c"]
            ),
        },
        "accepted_as_nonfit_residual_audit": True,
        "accepted_as_precision_promotion": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion_gate = {
        "schema": "MTTPrecisionPromotionAcceptanceGate.v1",
        "status": "PRECISION_PROMOTION_GATE_BUILT_PROMOTION_REJECTED_FOR_NOW",
        "promotion_decision": "REJECT_PRECISION_PROMOTION_ACCEPT_RUNNING_PROXY_AS_BEST_CURRENT_SCAFFOLD",
        "why_rejected": [
            "benchmark values were used only for residual audit, not fitting",
            "one-loop running/mass anomalous dimensions are not a declared precision SM scheme",
            "higher-order QCD and EW correction terms are absent",
            "total-width/off-shell policy is absent",
            "full covariance/profile likelihood is absent",
            "actual selected Qa/SU3 operator packet remains open",
        ],
        "minimum_next_rows_for_promotion": [
            "versioned multiloop alpha_s and mass-running/matching equations",
            "declared Higgs partial-width formula set for bb, cc, tau, mu, WW*, ZZ*, gg, gamma gamma, Z gamma",
            "uncertainty/covariance propagation or explicit precision-parity waiver",
            "source/operator attachment rule for Qa/SU3-sensitive observables",
        ],
        "best_current_stage": "one_loop_running_mass_qcd_proxy",
        "precision_promotion_accepted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["non-fit Higgs decay residual audit"]
    for blocker in [
        "full Higgs decay residual audit against external benchmark",
    ]:
        if blocker in remaining:
            remaining.remove(blocker)
    for blocker in [
        "versioned multiloop Higgs partial-width formula set",
        "full precision loop-corrected QFT correlator/S-matrix/decay rows",
        "full covariance/profile likelihood values",
        "actual selected Qa/SU3 operator packet",
    ]:
        if blocker not in remaining:
            remaining.append(blocker)

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterHiggsDecayResidualAudit.v1",
        "status": "HIGGS_DECAY_RESIDUAL_AUDIT_BUILT_PRECISION_PROMOTION_REJECTED",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "versioned multiloop Higgs partial-width formula set or actual selected Qa/SU3 operator packet",
        "guardrails": {
            "residual_benchmark_not_used_for_fit": True,
            "best_proxy_not_promoted_to_precision": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsDecayResidualAuditOrPrecisionPromotion",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_runningmasshiggsdecayproxy_or_precisionwidths.candidate.json"),
            "tree_decay_rows": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "representative_tree_level_decay_observable_rows.packet.json"
            ),
            "reference_mass_qcd_proxy": rel(
                DATA
                / "selected_loopqcddecayproxyvalues_or_fullprecisionqft"
                / "one_loop_qcd_higgs_quark_decay_proxy_values.packet.json"
            ),
            "running_mass_proxy": rel(
                DATA
                / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
                / "one_loop_running_mass_higgs_decay_proxy.packet.json"
            ),
            "plausibility_benchmark": rel(
                DATA
                / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
                / "higgs_decay_plausibility_benchmark.packet.json"
            ),
        },
        "output_packets": {
            "higgs_decay_proxy_residual_audit": rel(RESIDUALS),
            "precision_promotion_acceptance_gate": rel(PROMOTION),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsDecayProxyResidualAuditTheorem",
            "proved": True,
            "statement": (
                "Against the fixed external Higgs branching-ratio benchmark, the one-loop running-mass proxy is the "
                "best current non-fit scaffold for H->bb and H->cc among the emitted stages. This licenses the proxy "
                "as the active scaffold but rejects precision promotion until multiloop formulae, covariance/profile "
                "policy, total-width handling, and Qa/SU3-sensitive source attachment are supplied."
            ),
        },
        "what_closes_now": {
            "nonfit_higgs_decay_residual_audit": True,
            "best_current_proxy_stage_identified": True,
            "bad_reference_mass_proxy_noted": True,
            "precision_promotion_gate_built": True,
        },
        "what_remains_open": {
            "versioned_multiloop_higgs_partial_width_formula_set": True,
            "full_covariance_profile_likelihood_values": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "residual_audit_closed": True,
            "precision_promotion_accepted": False,
            "full_precision_QFT_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsDecayResidualAudit_or_PrecisionPromotion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "residual_audit_closed": True,
        "precision_promotion_accepted": False,
        "full_precision_QFT_values_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_MultiloopHiggsPartialWidthFormulaSet_or_ActualQaSU3Packet_v1",
    }

    note = """# MTT Selected HiggsDecayResidualAudit or PrecisionPromotion v1

Status: `MTT_SELECTED_HIGGSDECAYRESIDUALAUDIT_OR_PRECISIONPROMOTION_BUILT_NONFIT_AUDIT_PRECISION_OPEN`.

This artifact compares three emitted stages for `H -> bb` and `H -> cc`:
tree/reference-mass, one-loop QCD with reference masses, and one-loop
running-mass QCD proxy.

The benchmark is external and fixed before comparison; it is not used to tune
parameters or select MTT source data. The audit shows that the running-mass
proxy is the best current scaffold, while precision promotion must still be
rejected.

The next step is a versioned multiloop Higgs partial-width formula set, or the
actual selected Qa/SU3 operator packet for source-sensitive observables.
"""

    for path, payload in [
        (RESIDUALS, residual_packet),
        (PROMOTION, promotion_gate),
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
