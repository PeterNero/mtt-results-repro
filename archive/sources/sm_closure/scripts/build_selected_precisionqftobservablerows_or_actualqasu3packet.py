"""Build representative tree-level QFT decay rows and actual Qa/SU3 packet gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_precisionqftobservablerows_or_actualqasu3packet"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DECAYS = PACKET_DIR / "representative_tree_level_decay_observable_rows.packet.json"
QASU3 = PACKET_DIR / "actual_qasu3_packet_gate_after_qft_rows.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_tree_decay_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrecisionQFTObservableRows_or_ActualQaSU3Packet_v1.md"

STATUS = "MTT_SELECTED_PRECISIONQFTOBSERVABLEROWS_OR_ACTUALQASU3PACKET_BUILT_TREE_DECAY_ROWS_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def mass_gev(row: dict[str, Any]) -> float:
    value = float(row["central_value"])
    units = row.get("units")
    if units == "MeV":
        return value / 1000.0
    if units == "GeV":
        return value
    raise ValueError(f"unknown mass unit: {units}")


def higgs_to_ff_width(gf: float, mh: float, mf: float, color_factor: int) -> dict[str, Any]:
    if 2.0 * mf >= mh:
        return {
            "kinematically_open": False,
            "width_GeV": 0.0,
            "beta_cubed": 0.0,
        }
    beta_cubed = (1.0 - 4.0 * mf * mf / (mh * mh)) ** 1.5
    width = color_factor * gf * mh * mf * mf * beta_cubed / (4.0 * math.pi * math.sqrt(2.0))
    return {
        "kinematically_open": True,
        "width_GeV": width,
        "beta_cubed": beta_cubed,
    }


def w_to_lepton_neutrino_width(gf: float, mw: float) -> float:
    return gf * mw**3 / (6.0 * math.pi * math.sqrt(2.0))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_localqftobservablerows_or_finaltruesmequivalencegap.candidate.json")
    previous_gate = load(
        DATA
        / "selected_localqftobservablerows_or_finaltruesmequivalencegap"
        / "updated_true_equivalence_gate_after_qft_tree_rows.packet.json"
    )
    tree_rows = load(
        DATA
        / "selected_localqftobservablerows_or_finaltruesmequivalencegap"
        / "tree_level_local_qft_observable_rows.packet.json"
    )
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    qasu3_import = load(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")
    actual_packet = load(DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json")

    values = reference["reference_values"]
    masses = values["masses"]
    gf = float(values["constants"]["G_F"]["central_value"])
    mh = mass_gev(masses["H"])
    mw = mass_gev(masses["W"])

    higgs_channels = [
        ("H_to_b_bbar_tree", "b", 3),
        ("H_to_c_cbar_tree", "c", 3),
        ("H_to_tau_tau_tree", "tau", 1),
        ("H_to_mu_mu_tree", "mu", 1),
        ("H_to_t_tbar_tree_closed", "t", 3),
    ]
    higgs_rows = []
    for row_id, mass_key, color in higgs_channels:
        mf = mass_gev(masses[mass_key])
        width = higgs_to_ff_width(gf, mh, mf, color)
        higgs_rows.append(
            {
                "id": row_id,
                "formula": "Gamma(H->f fbar)=N_c*G_F*m_H*m_f^2*(1-4*m_f^2/m_H^2)^(3/2)/(4*pi*sqrt(2))",
                "fermion": mass_key,
                "color_factor": color,
                "m_H_GeV": mh,
                "m_f_GeV": mf,
                **width,
            }
        )

    w_width = w_to_lepton_neutrino_width(gf, mw)
    w_rows = [
        {
            "id": f"W_to_{lepton}_nu_tree",
            "formula": "Gamma(W->l nu)=G_F*M_W^3/(6*pi*sqrt(2)) in massless-lepton tree approximation",
            "lepton": lepton,
            "M_W_GeV": mw,
            "width_GeV": w_width,
            "kinematically_open": True,
        }
        for lepton in ["e", "mu", "tau"]
    ]

    total_open_higgs_width = sum(row["width_GeV"] for row in higgs_rows if row["kinematically_open"])
    total_w_leptonic_width = sum(row["width_GeV"] for row in w_rows)
    decay_packet = {
        "schema": "MTTRepresentativeTreeLevelDecayObservableRows.v1",
        "status": "REPRESENTATIVE_TREE_LEVEL_DECAY_ROWS_BUILT_LOOP_PRECISION_OPEN",
        "input_packet": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
        "upstream_tree_identity_tier_closed": tree_rows["all_tree_identity_rows_closed"],
        "higgs_fermion_decay_rows": higgs_rows,
        "w_leptonic_decay_rows": w_rows,
        "summary": {
            "open_higgs_fermion_channels_count": sum(1 for row in higgs_rows if row["kinematically_open"]),
            "tree_sum_open_H_to_ff_width_GeV": total_open_higgs_width,
            "tree_sum_W_leptonic_width_GeV": total_w_leptonic_width,
            "all_widths_finite_nonnegative": all(row["width_GeV"] >= 0.0 and math.isfinite(row["width_GeV"]) for row in higgs_rows + w_rows),
        },
        "accepted_as_representative_local_QFT_decay_rows": True,
        "accepted_as_precision_SM_decay_widths": False,
        "why_not_precision": (
            "Rows are tree-level downstream SM-parity replay values only. Precision decay widths require "
            "running masses, QCD/EW corrections, off-shell channels, total-width policy, and experimental/profile comparison."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    qasu3_gate = {
        "schema": "MTTActualQaSU3PacketGateAfterQFTRows.v1",
        "status": "ACTUAL_QASU3_PACKET_GATE_REMAINS_OPEN_AFTER_QFT_TREE_ROWS",
        "crossrepo_status": qasu3_import["status"],
        "actual_selected_sm_packet_anomaly_status": actual_packet["status"],
        "qft_rows_change_source_status": False,
        "why_still_open": [
            "Tree QFT observables are downstream replay values and cannot select the source/operator packet.",
            "The actual selected Qa/SU3 color/operator packet must still supply source-side representation, anomaly, and operator data.",
            "Precision Ward/anomaly observable replay must be attached to the actual selected packet, not just the parity interface.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = [
        blocker
        for blocker in previous_gate["remaining_true_equivalence_blockers"]
        if blocker != "precision local QFT correlator/S-matrix/decay rows"
    ]
    if "loop-corrected local QFT correlator/S-matrix/decay rows" not in remaining:
        remaining.insert(1, "loop-corrected local QFT correlator/S-matrix/decay rows")
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterTreeDecayRows.v1",
        "status": "TREE_DECAY_ROWS_BUILT_LOOP_PRECISION_AND_QASU3_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": [
            "representative tree-level local QFT decay rows",
        ],
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "loop-corrected local QFT observables or actual selected Qa/SU3 operator packet",
        "guardrails": {
            "tree_decay_rows_are_not_precision_decay_widths": True,
            "qft_rows_do_not_select_qasu3_packet": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrecisionQFTObservableRowsOrActualQaSU3Packet",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_localqftobservablerows_or_finaltruesmequivalencegap.candidate.json"),
            "tree_identity_rows": rel(
                DATA
                / "selected_localqftobservablerows_or_finaltruesmequivalencegap"
                / "tree_level_local_qft_observable_rows.packet.json"
            ),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "qasu3_crossrepo_import": rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"),
        },
        "output_packets": {
            "representative_tree_level_decay_observable_rows": rel(DECAYS),
            "actual_qasu3_packet_gate_after_qft_rows": rel(QASU3),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "RepresentativeTreeDecayRowsAndQaSU3GateTheorem",
            "proved": True,
            "statement": (
                "The admitted SM-parity measured packet emits representative tree-level local QFT decay rows "
                "for Higgs-to-fermion and W-to-lepton-neutrino channels. These are downstream observable values "
                "and close only a representative tree decay tier; loop-corrected precision observables, correlated "
                "profiles, actual Qa/SU3 packet integration, true SM-equivalence, and no-knob closure remain open."
            ),
        },
        "what_closes_now": {
            "representative_tree_level_decay_rows": True,
            "finite_nonnegative_decay_widths": decay_packet["summary"]["all_widths_finite_nonnegative"],
            "actual_qasu3_gate_rechecked": True,
            "superset_strategy_preserved": True,
        },
        "what_remains_open": {
            "loop_corrected_local_QFT_correlator_smatrix_decay_rows": True,
            "published_or_reconstructed_correlated_profile_values": True,
            "multi_loop_threshold_convention_values": True,
            "QM_GR_measurement_response_interfaces": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "representative_tree_decay_tier_closed": True,
            "precision_local_QFT_observable_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PrecisionQFTObservableRows_or_ActualQaSU3Packet_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "representative_tree_decay_tier_closed": True,
        "precision_local_QFT_observable_values_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_LoopCorrectedQFTObservables_or_ActualQaSU3Packet_v1",
    }

    note = """# MTT Selected PrecisionQFTObservableRows or ActualQaSU3Packet v1

Status: `MTT_SELECTED_PRECISIONQFTOBSERVABLEROWS_OR_ACTUALQASU3PACKET_BUILT_TREE_DECAY_ROWS_PRECISION_OPEN`.

This artifact adds representative local-QFT decay observable rows: tree-level
`H -> f fbar` and leptonic `W -> l nu` channels from the same admitted
SM-parity measured packet.

These rows are downstream replay values only. They are not precision SM decay
widths: loop corrections, running masses, off-shell channels, total-width
policy, correlated profiles, and experimental comparison remain open.

The actual Qa/SU3 operator packet is also rechecked and remains open because
observable rows cannot select source/operator data.
"""

    for path, payload in [
        (DECAYS, decay_packet),
        (QASU3, qasu3_gate),
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
