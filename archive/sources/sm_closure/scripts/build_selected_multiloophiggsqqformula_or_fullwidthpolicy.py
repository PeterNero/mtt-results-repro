"""Build a versioned multiloop Higgs-to-quark formula scaffold."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_multiloophiggsqqformula_or_fullwidthpolicy"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FORMULA = PACKET_DIR / "versioned_massless_qcd_higgs_qq_formula.packet.json"
VALUES = PACKET_DIR / "n3lo_qcd_higgs_qq_proxy_values.packet.json"
GATE = PACKET_DIR / "full_higgs_width_policy_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_multiloop_qq_formula.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MultiloopHiggsQQFormula_or_FullWidthPolicy_v1.md"

STATUS = "MTT_SELECTED_MULTILOOPHIGGSQQFORMULA_OR_FULLWIDTHPOLICY_BUILT_N3LO_QCD_QQ_PROXY_FULL_WIDTH_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsdecayresidualaudit_or_precisionpromotion.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgsdecayresidualaudit_or_precisionpromotion"
        / "updated_true_equivalence_gate_after_higgs_decay_residual_audit.packet.json"
    )
    running = load(
        DATA
        / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
        / "one_loop_running_mass_higgs_decay_proxy.packet.json"
    )
    residual = load(
        DATA
        / "selected_higgsdecayresidualaudit_or_precisionpromotion"
        / "higgs_decay_proxy_residual_audit.packet.json"
    )

    # Standard scalar H->qq massless-QCD expansion in a_s=alpha_s/pi for nf=5.
    # The coefficients are encoded as a versioned downstream benchmark scaffold,
    # not as selected MTT source data.
    coeffs = {
        "c1": 17.0 / 3.0,
        "c2_nf5": 29.146714,
        "c3_nf5": 41.75761,
    }
    alpha_mh = float(running["alpha_s_values"]["alpha_s_mH_proxy"])
    a_s = alpha_mh / math.pi
    factors = {
        "LO": 1.0,
        "NLO": 1.0 + coeffs["c1"] * a_s,
        "NNLO": 1.0 + coeffs["c1"] * a_s + coeffs["c2_nf5"] * a_s**2,
        "N3LO": 1.0 + coeffs["c1"] * a_s + coeffs["c2_nf5"] * a_s**2 + coeffs["c3_nf5"] * a_s**3,
    }

    formula_packet = {
        "schema": "MTTVersionedMasslessQCDHiggsQQFormula.v1",
        "status": "VERSIONED_MASSLESS_QCD_HIGGS_QQ_FORMULA_BUILT_SOURCE_DOWNSTREAM",
        "formula": "Gamma(H->q qbar)=Gamma0(m_q(mu))*[1+c1*a_s+c2*a_s^2+c3*a_s^3+...] with a_s=alpha_s(mu)/pi",
        "scale": "mu=m_H proxy",
        "nf": 5,
        "coefficients": coeffs,
        "coefficient_sources": [
            {
                "name": "Djouadi et al. QCD corrections to hadronic Higgs decays",
                "url": "https://arxiv.org/abs/hep-ph/9511344",
                "role": "classic H->qq/H->hadron QCD-correction reference",
            },
            {
                "name": "HDECAY / LHC Higgs Cross Section Working Group convention",
                "url": "https://cds.cern.ch/record/1416519/files/arXiv%3A1201.3084.pdf",
                "role": "precision-Higgs decay convention and toolchain reference",
            },
        ],
        "accepted_as_versioned_QCD_formula_scaffold": True,
        "accepted_as_full_width_policy": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    benchmark_refs = residual["benchmark_partial_widths_GeV"]
    ref_by_channel = {
        "b": benchmark_refs["H_to_bb_reference_approx"],
        "c": benchmark_refs["H_to_cc_reference_approx"],
    }
    value_rows = []
    for row in running["rows"]:
        fermion = row["fermion"]
        gamma0 = float(row["tree_width_with_running_mass_GeV"])
        stage_widths = {stage: gamma0 * factor for stage, factor in factors.items()}
        reference = ref_by_channel[fermion]
        value_rows.append(
            {
                "id": f"H_to_{fermion}_{fermion}bar_n3lo_massless_qcd_proxy",
                "fermion": fermion,
                "Gamma0_running_mass_GeV": gamma0,
                "alpha_s_mH_proxy": alpha_mh,
                "a_s": a_s,
                "qcd_factors": factors,
                "stage_widths_GeV": stage_widths,
                "benchmark_reference_GeV": reference,
                "N3LO_relative_residual_to_benchmark": (stage_widths["N3LO"] - reference) / reference,
                "N3LO_ratio_to_benchmark": stage_widths["N3LO"] / reference,
                "accepted_as_N3LO_massless_QCD_proxy": True,
                "accepted_as_precision_SM_decay_width": False,
            }
        )

    values_packet = {
        "schema": "MTTN3LOQCDHiggsQQProxyValues.v1",
        "status": "N3LO_QCD_HIGGS_QQ_PROXY_VALUES_BUILT_FULL_PRECISION_OPEN",
        "input_running_mass_proxy": rel(
            DATA
            / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
            / "one_loop_running_mass_higgs_decay_proxy.packet.json"
        ),
        "input_residual_audit": rel(
            DATA
            / "selected_higgsdecayresidualaudit_or_precisionpromotion"
            / "higgs_decay_proxy_residual_audit.packet.json"
        ),
        "rows": value_rows,
        "summary": {
            "N3LO_factor": factors["N3LO"],
            "N3LO_exceeds_NLO_factor": factors["N3LO"] > factors["NLO"],
            "all_widths_finite_nonnegative": all(
                math.isfinite(row["stage_widths_GeV"]["N3LO"]) and row["stage_widths_GeV"]["N3LO"] >= 0.0
                for row in value_rows
            ),
            "all_N3LO_rows_within_factor_two_benchmark": all(
                0.5 <= row["N3LO_ratio_to_benchmark"] <= 2.0 for row in value_rows
            ),
            "all_N3LO_rows_within_twenty_percent_benchmark": all(
                abs(row["N3LO_relative_residual_to_benchmark"]) <= 0.20 for row in value_rows
            ),
        },
        "accepted_as_multiloop_QCD_proxy_layer": True,
        "accepted_as_precision_SM_decay_widths": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    width_gate = {
        "schema": "MTTFullHiggsWidthPolicyGate.v1",
        "status": "FULL_HIGGS_WIDTH_POLICY_GATE_BUILT_STILL_OPEN",
        "closed_now": [
            "versioned massless-QCD qq coefficient scaffold",
            "N3LO massless-QCD proxy values for H->bb and H->cc",
        ],
        "still_required_before_precision_width_promotion": [
            "multiloop running/matching for alpha_s and quark masses with uncertainties",
            "finite-mass effects and top-induced terms where applicable",
            "electroweak corrections",
            "complete channel set: tau, mu, WW*, ZZ*, gg, gamma gamma, Z gamma",
            "total-width and branching-ratio construction",
            "covariance/profile likelihood treatment",
            "actual selected Qa/SU3 source/operator packet for operator-sensitive rows",
        ],
        "precision_promotion_accepted": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["versioned massless-QCD Higgs qq formula scaffold"]
    if "versioned multiloop Higgs partial-width formula set" in remaining:
        remaining.remove("versioned multiloop Higgs partial-width formula set")
    for blocker in [
        "complete Higgs partial-width channel formula set",
        "full Higgs total-width and branching-ratio policy",
        "full precision loop-corrected QFT correlator/S-matrix/decay rows",
        "full covariance/profile likelihood values",
        "actual selected Qa/SU3 operator packet",
    ]:
        if blocker not in remaining:
            remaining.append(blocker)
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterMultiloopQQFormula.v1",
        "status": "N3LO_QQ_FORMULA_SCAFFOLD_BUILT_FULL_WIDTH_POLICY_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "complete Higgs channel formula set and total-width policy, or actual selected Qa/SU3 packet",
        "guardrails": {
            "qq_formula_scaffold_not_complete_higgs_width_policy": True,
            "N3LO_proxy_not_precision_SM_width": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedMultiloopHiggsQQFormulaOrFullWidthPolicy",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsdecayresidualaudit_or_precisionpromotion.candidate.json"),
            "running_mass_proxy": rel(
                DATA
                / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
                / "one_loop_running_mass_higgs_decay_proxy.packet.json"
            ),
            "residual_audit": rel(
                DATA
                / "selected_higgsdecayresidualaudit_or_precisionpromotion"
                / "higgs_decay_proxy_residual_audit.packet.json"
            ),
        },
        "output_packets": {
            "versioned_massless_qcd_higgs_qq_formula": rel(FORMULA),
            "n3lo_qcd_higgs_qq_proxy_values": rel(VALUES),
            "full_higgs_width_policy_gate": rel(GATE),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "VersionedMasslessQCDHiggsQQFormulaScaffoldTheorem",
            "proved": True,
            "statement": (
                "The repo now contains a versioned downstream massless-QCD coefficient scaffold for H->qq through "
                "N3LO proxy order and evaluates it on the current running-mass b,c proxy rows. This closes the qq "
                "formula-scaffold gap but not complete Higgs partial widths, total width, covariance/profile treatment, "
                "or true SM equivalence."
            ),
        },
        "what_closes_now": {
            "versioned_massless_QCD_Higgs_qq_formula_scaffold": True,
            "N3LO_QCD_proxy_values_for_Hbb_Hcc": True,
            "full_width_policy_gate_built": True,
        },
        "what_remains_open": {
            "complete_Higgs_channel_formula_set": True,
            "total_width_and_branching_ratio_policy": True,
            "covariance_profile_likelihood_values": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "qq_formula_scaffold_closed": True,
            "complete_Higgs_width_policy_closed": False,
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
        "certificate": "MTT_Selected_MultiloopHiggsQQFormula_or_FullWidthPolicy_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "qq_formula_scaffold_closed": True,
        "complete_Higgs_width_policy_closed": False,
        "full_precision_QFT_values_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_CompleteHiggsPartialWidthPolicy_or_ActualQaSU3Packet_v1",
    }

    note = """# MTT Selected MultiloopHiggsQQFormula or FullWidthPolicy v1

Status: `MTT_SELECTED_MULTILOOPHIGGSQQFORMULA_OR_FULLWIDTHPOLICY_BUILT_N3LO_QCD_QQ_PROXY_FULL_WIDTH_OPEN`.

This artifact builds a versioned massless-QCD coefficient scaffold for
`H -> q qbar`, evaluated on the current one-loop running-mass b and c proxy
rows.

The coefficient packet is downstream benchmark/QFT machinery. It is not MTT
source selection and it is not a complete Higgs-width policy.

The next precision step is the complete Higgs channel formula set and total
width/branching-ratio policy, or the actual selected Qa/SU3 packet for
source-sensitive observables.
"""

    for path, payload in [
        (FORMULA, formula_packet),
        (VALUES, values_packet),
        (GATE, width_gate),
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
