"""Build executable Higgs uniform-kernel rows where current data allow it."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsuniformkernelrows_or_fullchannelvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
KERNELS = PACKET_DIR / "executable_higgs_uniform_kernel_rows.packet.json"
OPEN = PACKET_DIR / "open_higgs_kernel_obligations.packet.json"
GATE = PACKET_DIR / "full_channel_value_promotion_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_uniform_kernel_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsUniformKernelRows_or_FullChannelValues_v1.md"

STATUS = "MTT_SELECTED_HIGGSUNIFORMKERNELROWS_OR_FULLCHANNELVALUES_BUILT_PARTIAL_KERNEL_ROWS_FULL_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgscovarianceprofilecontract_or_uniformformularows.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgscovarianceprofilecontract_or_uniformformularows"
        / "updated_true_equivalence_gate_after_profile_contract.packet.json"
    )
    manifest = load(
        DATA
        / "selected_higgscovarianceprofilecontract_or_uniformformularows"
        / "uniform_higgs_formula_row_manifest.packet.json"
    )
    qq = load(
        DATA
        / "selected_multiloophiggsqqformula_or_fullwidthpolicy"
        / "n3lo_qcd_higgs_qq_proxy_values.packet.json"
    )
    tree = load(
        DATA
        / "selected_precisionqftobservablerows_or_actualqasu3packet"
        / "representative_tree_level_decay_observable_rows.packet.json"
    )
    sidecars = load(
        DATA
        / "selected_higgsprecisionsidecars_or_uniformformularows"
        / "higgs_channel_uncertainty_sidecars.packet.json"
    )

    sidecar_by_channel = {row["channel"]: row for row in sidecars["rows"]}
    manifest_by_channel = {row["channel"]: row for row in manifest["rows"]}
    qq_by_channel = {
        f"H_to_{row['fermion']}{row['fermion']}": row
        for row in qq["rows"]
    }
    tree_by_channel = {
        "H_to_tau_tau": next(row for row in tree["higgs_fermion_decay_rows"] if row["fermion"] == "tau"),
        "H_to_mu_mu": next(row for row in tree["higgs_fermion_decay_rows"] if row["fermion"] == "mu"),
    }

    executable_rows = []
    for channel in ["H_to_bb", "H_to_cc"]:
        row = qq_by_channel[channel]
        manifest_row = manifest_by_channel[channel]
        executable_rows.append(
            {
                "channel": channel,
                "kernel_family": manifest_row["formula_family_required"],
                "kernel_formula": "Gamma0(m_q(mu))*[1+c1*a_s+c2*a_s^2+c3*a_s^3]",
                "kernel_status": "EXECUTABLE_N3LO_MASSLESS_QCD_PROXY_KERNEL",
                "width_GeV": row["stage_widths_GeV"]["N3LO"],
                "relative_uncertainty": sidecar_by_channel[channel]["relative_uncertainty"],
                "operator_attachment_required": manifest_row["operator_attachment_required"],
                "source_packet": qq["input_running_mass_proxy"],
                "accepted_as_uniform_kernel_row": True,
                "accepted_as_precision_formula_row": False,
                "why_not_precision": "Massless-QCD proxy uses current running-mass scaffold; finite-mass, EW/mixed corrections, full threshold scheme, covariance, and selected Qa/SU3 remain open.",
            }
        )

    for channel in ["H_to_tau_tau", "H_to_mu_mu"]:
        row = tree_by_channel[channel]
        manifest_row = manifest_by_channel[channel]
        executable_rows.append(
            {
                "channel": channel,
                "kernel_family": manifest_row["formula_family_required"],
                "kernel_formula": row["formula"],
                "kernel_status": "EXECUTABLE_TREE_LEPTONIC_KERNEL_EW_CORRECTIONS_OPEN",
                "width_GeV": row["width_GeV"],
                "relative_uncertainty": sidecar_by_channel[channel]["relative_uncertainty"],
                "operator_attachment_required": manifest_row["operator_attachment_required"],
                "source_packet": "candidate_data/selected_precisionqftobservablerows_or_actualqasu3packet/representative_tree_level_decay_observable_rows.packet.json",
                "accepted_as_uniform_kernel_row": True,
                "accepted_as_precision_formula_row": False,
                "why_not_precision": "Tree leptonic kernel is executable but electroweak correction policy and full covariance/profile remain open.",
            }
        )

    filled_channels = {row["channel"] for row in executable_rows}
    open_obligations = []
    for row in manifest["rows"]:
        if row["channel"] in filled_channels:
            continue
        open_obligations.append(
            {
                "channel": row["channel"],
                "required_kernel_family": row["formula_family_required"],
                "operator_attachment_required": row["operator_attachment_required"],
                "shared_inputs": row["shared_inputs"],
                "current_row_kind": row["current_row_kind"],
                "current_width_GeV": row["current_width_GeV"],
                "kernel_value_filled": False,
                "minimum_next_step": (
                    "supply an executable formula kernel or explicitly audited published benchmark replay policy "
                    "with covariance/profile placement"
                ),
            }
        )

    kernel_packet = {
        "schema": "MTTExecutableHiggsUniformKernelRows.v1",
        "status": "PARTIAL_EXECUTABLE_HIGGS_KERNEL_ROWS_BUILT_FULL_CHANNEL_VALUES_OPEN",
        "row_basis": manifest["rows"],
        "executable_rows": executable_rows,
        "summary": {
            "executable_kernel_row_count": len(executable_rows),
            "open_kernel_row_count": len(open_obligations),
            "all_executable_widths_positive": all(row["width_GeV"] > 0.0 for row in executable_rows),
            "all_executable_rows_have_sidecars": all(row["relative_uncertainty"] > 0.0 for row in executable_rows),
            "uniform_formula_rows_fully_filled": False,
            "precision_formula_rows_fully_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    open_packet = {
        "schema": "MTTOpenHiggsKernelObligations.v1",
        "status": "SIX_HIGGS_KERNEL_ROWS_REMAIN_OPEN",
        "rows": open_obligations,
        "blocked_channels": [row["channel"] for row in open_obligations],
        "color_sensitive_open_channels": [
            row["channel"]
            for row in open_obligations
            if "Qa/SU3" in row["operator_attachment_required"] or "color" in row["operator_attachment_required"]
        ],
        "electroweak_loop_or_offshell_open_channels": [
            row["channel"]
            for row in open_obligations
            if "electroweak" in row["operator_attachment_required"] or "SU2" in row["operator_attachment_required"]
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gate = {
        "schema": "MTTFullHiggsChannelValuePromotionGate.v1",
        "status": "PARTIAL_KERNEL_ROWS_BUILT_PROMOTION_REJECTED",
        "closed_now": [
            "executable uniform-kernel rows for H_to_bb and H_to_cc using N3LO massless-QCD proxy",
            "executable uniform-kernel rows for H_to_tau_tau and H_to_mu_mu using tree leptonic kernel",
            "open-kernel obligation table for the remaining six Higgs channels",
        ],
        "promotion_decision": "REJECT_FULL_PRECISION_PROMOTION_ACCEPT_PARTIAL_KERNEL_LAYER",
        "still_required_for_full_channel_values": [
            "executable kernels or benchmark-replay policy for WW*, ZZ*, gg, gamma gamma, Z gamma, ss",
            "electroweak/off-shell/loop correction policy for all relevant rows",
            "full covariance/profile matrix on the ten-channel row basis",
            "actual selected Qa/SU3 packet for color-sensitive operator rows",
        ],
        "full_channel_values_closed": False,
        "full_covariance_profile_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["partial executable Higgs uniform-kernel rows"]
    for blocker in [
        "uniform precision Higgs partial-width formula rows",
        "full cross-channel Higgs covariance/profile likelihood",
        "full precision loop-corrected QFT correlator/S-matrix/decay rows",
        "actual selected Qa/SU3 operator packet",
    ]:
        if blocker not in remaining:
            remaining.append(blocker)
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterUniformKernelRows.v1",
        "status": "PARTIAL_KERNEL_ROWS_BUILT_FULL_CHANNEL_VALUES_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "fill one of the remaining six Higgs kernel rows or supply the ten-channel covariance/profile matrix",
        "guardrails": {
            "partial_kernel_rows_not_full_uniform_formula_set": True,
            "proxy_kernels_not_precision": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsUniformKernelRowsOrFullChannelValues",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgscovarianceprofilecontract_or_uniformformularows.candidate.json"),
            "uniform_formula_row_manifest": rel(
                DATA
                / "selected_higgscovarianceprofilecontract_or_uniformformularows"
                / "uniform_higgs_formula_row_manifest.packet.json"
            ),
            "n3lo_qq_proxy_values": rel(
                DATA / "selected_multiloophiggsqqformula_or_fullwidthpolicy" / "n3lo_qcd_higgs_qq_proxy_values.packet.json"
            ),
            "tree_decay_rows": rel(
                DATA
                / "selected_precisionqftobservablerows_or_actualqasu3packet"
                / "representative_tree_level_decay_observable_rows.packet.json"
            ),
        },
        "output_packets": {
            "executable_higgs_uniform_kernel_rows": rel(KERNELS),
            "open_higgs_kernel_obligations": rel(OPEN),
            "full_channel_value_promotion_gate": rel(GATE),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "PartialHiggsUniformKernelRowsTheorem",
            "proved": True,
            "statement": (
                "Given the already-built qq QCD proxy layer and tree leptonic decay rows, four Higgs channels admit "
                "executable uniform-kernel rows on the declared ten-channel basis. The remaining six channels require "
                "new kernels or an audited benchmark-replay policy before full channel values or precision promotion."
            ),
        },
        "what_closes_now": {
            "partial_uniform_kernel_rows": True,
            "open_kernel_obligation_table": True,
            "full_channel_value_promotion_gate": True,
        },
        "what_remains_open": {
            "six_Higgs_kernel_rows": True,
            "full_ten_channel_covariance_profile": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_kernel_layer_closed": True,
            "partial_uniform_kernel_rows_closed": True,
            "uniform_formula_rows_fully_closed": False,
            "full_channel_values_closed": False,
            "cross_channel_covariance_profile_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsUniformKernelRows_or_FullChannelValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "partial_uniform_kernel_rows_closed": True,
        "uniform_formula_rows_fully_closed": False,
        "full_channel_values_closed": False,
        "cross_channel_covariance_profile_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsRemainingKernelRows_or_CovarianceProfileValues_v1",
    }

    note = """# MTT Selected HiggsUniformKernelRows or FullChannelValues v1

Status: `MTT_SELECTED_HIGGSUNIFORMKERNELROWS_OR_FULLCHANNELVALUES_BUILT_PARTIAL_KERNEL_ROWS_FULL_VALUES_OPEN`.

This artifact fills the currently executable Higgs uniform-kernel rows:
`H_to_bb`, `H_to_cc`, `H_to_tau_tau`, and `H_to_mu_mu`.

The result is deliberately partial. It does not close the six remaining Higgs
channels, the ten-channel covariance/profile likelihood, actual Qa/SU3, true
SM-equivalence, or no-knob closure.
"""

    for path, payload in [
        (KERNELS, kernel_packet),
        (OPEN, open_packet),
        (GATE, gate),
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
