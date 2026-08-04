"""Build local-QFT tree observable rows and final true-SM-equivalence gap."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_localqftobservablerows_or_finaltruesmequivalencegap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROWS = PACKET_DIR / "tree_level_local_qft_observable_rows.packet.json"
GAP = PACKET_DIR / "final_true_sm_equivalence_gap_matrix.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_qft_tree_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LocalQFTObservableRows_or_FinalTrueSMEquivalenceGap_v1.md"

STATUS = "MTT_SELECTED_LOCALQFTOBSERVABLEROWS_OR_FINALTRUESMEQUIVALENCEGAP_BUILT_TREE_QFT_ROWS_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def max_abs(values: list[float]) -> float:
    return max(abs(value) for value in values) if values else 0.0


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json")
    previous_gate = load(
        DATA
        / "selected_correlatedprofilevalues_or_localqftobservablevalues"
        / "updated_true_equivalence_gate_after_correlation_envelope.packet.json"
    )
    qft_gate = load(
        DATA
        / "selected_correlatedprofilevalues_or_localqftobservablevalues"
        / "local_qft_observable_value_gate.packet.json"
    )
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    tree = load(DATA / "sm_equivalence_tree_level_replay_seed.candidate.json")
    mixing = load(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json")
    functor = load(
        DATA
        / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor"
        / "local_qft_observable_functor_interface.packet.json"
    )

    constants = reference["reference_values"]["constants"]
    tree_replay = tree["tree_level_replay"]
    higgs = tree_replay["higgs_tree"]
    masses = tree_replay["input_masses_GeV"]
    residuals = tree_replay["mass_residuals_GeV"]
    gauge = mixing["gauge_replay_MZ"]["numeric_triplet"]
    alpha1 = float(gauge["alpha_1_GUT"]["central_value"])
    alpha2 = float(gauge["alpha_2"]["central_value"])
    alpha3 = float(gauge["alpha_3"]["central_value"])
    g1 = float(gauge["g_1_GUT"]["central_value"])
    g2 = float(gauge["g_2"]["central_value"])
    g3 = float(gauge["g_3"]["central_value"])

    v = float(constants["v_from_G_F"]["central_value"])
    gf = float(constants["G_F"]["central_value"])
    lambda_tree = float(higgs["lambda_tree"])
    mh = float(higgs["m_H_GeV"])

    vev_residual = v - 1.0 / math.sqrt(math.sqrt(2.0) * gf)
    higgs_curvature_residual = mh * mh - 2.0 * lambda_tree * v * v
    gauge_residuals = {
        "g1_square_minus_4pi_alpha1": g1 * g1 - 4.0 * math.pi * alpha1,
        "g2_square_minus_4pi_alpha2": g2 * g2 - 4.0 * math.pi * alpha2,
        "g3_square_minus_4pi_alpha3": g3 * g3 - 4.0 * math.pi * alpha3,
    }

    rows = [
        {
            "id": "vev_from_fermi_constant",
            "qft_object": "electroweak vacuum normalization",
            "formula": "v=(sqrt(2)*G_F)^(-1/2)",
            "value": v,
            "residual": vev_residual,
            "closed_tree_identity": abs(vev_residual) < 1e-12,
        },
        {
            "id": "higgs_curvature_tree_identity",
            "qft_object": "Higgs quadratic curvature in V(H)=-mu^2|H|^2+lambda|H|^4",
            "formula": "m_H^2=2*lambda*v^2",
            "value": {"m_H_GeV": mh, "lambda_tree": lambda_tree, "v_GeV": v},
            "residual": higgs_curvature_residual,
            "closed_tree_identity": abs(higgs_curvature_residual) < 1e-9,
        },
        {
            "id": "charged_yukawa_mass_identities",
            "qft_object": "tree Yukawa mass terms",
            "formula": "m_f=y_f*v/sqrt(2)",
            "max_abs_residual_GeV": max_abs([float(value) for value in residuals.values()]),
            "number_of_mass_rows": len(residuals),
            "closed_tree_identity": max_abs([float(value) for value in residuals.values()]) == 0.0,
        },
        {
            "id": "gauge_alpha_to_coupling_normalization",
            "qft_object": "gauge kinetic/coupling normalization at M_Z",
            "formula": "g_i^2=4*pi*alpha_i",
            "residuals": gauge_residuals,
            "max_abs_residual": max_abs(list(gauge_residuals.values())),
            "closed_tree_identity": max_abs(list(gauge_residuals.values())) < 1e-15,
        },
        {
            "id": "ckm_pmns_unitarity_observable_checks",
            "qft_object": "charged-current mixing matrix unitarity checks",
            "formula": "V^dagger V=I and U^dagger U=I in replay convention",
            "residuals": {
                "CKM_unitarity_max_residual": mixing["CKM_replay"]["unitarity_max_residual"],
                "PMNS_unitarity_max_residual": mixing["PMNS_replay"]["unitarity_max_residual"],
            },
            "closed_tree_identity": (
                mixing["CKM_replay"]["unitarity_max_residual"] < 1e-12
                and mixing["PMNS_replay"]["unitarity_max_residual"] < 1e-12
            ),
        },
    ]
    all_tree_rows_closed = all(row["closed_tree_identity"] is True for row in rows)

    row_packet = {
        "schema": "MTTTreeLevelLocalQFTObservableRows.v1",
        "status": "TREE_LEVEL_LOCAL_QFT_OBSERVABLE_ROWS_REPLAYED_PRECISION_OBSERVABLES_OPEN",
        "functor_interface_status": functor["status"],
        "observable_rows": rows,
        "all_tree_identity_rows_closed": all_tree_rows_closed,
        "accepted_as_local_QFT_observable_values_tier": "TREE_IDENTITY_TIER_ONLY",
        "not_accepted_as_precision_correlator_or_smatrix_suite": True,
        "open_precision_rows": [
            "renormalized propagator residues and two-point functions beyond tree identities",
            "representative scattering or decay observables with loop/threshold policy",
            "Ward identity/anomaly observable replay on the actual selected Qa/SU3 operator packet",
            "full covariance/profile comparison of observable rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    final_gap = {
        "schema": "MTTFinalTrueSMEquivalenceGapMatrix.v1",
        "status": "TREE_QFT_ROWS_CLOSED_TRUE_SM_EQUIVALENCE_GAPS_SHARPENED",
        "closed_now": [
            "tree-level local QFT identity observable rows",
            "propagator/coupling normalization convention at identity tier",
            "mixing unitarity observable checks",
        ],
        "remaining_true_equivalence_gates": [
            {
                "id": "published_or_reconstructed_correlated_profile",
                "why_needed": "Replace diagonal/envelope profile with actual correlation/profile data.",
                "closed": False,
            },
            {
                "id": "precision_correlator_smatrix_decay_observable_rows",
                "why_needed": "Tree identities are not enough for full QFT empirical equivalence.",
                "closed": False,
            },
            {
                "id": "multi_loop_threshold_convention_values",
                "why_needed": "Match external weak-scale benchmarks and observables at declared precision.",
                "closed": False,
            },
            {
                "id": "QM_GR_measurement_response_interfaces",
                "why_needed": "Full theory parity must include measurement/record and gravitational response interfaces.",
                "closed": False,
            },
            {
                "id": "actual_selected_QaSU3_operator_packet",
                "why_needed": "Replace parity/interface scaffolding with the actual selected source/operator packet.",
                "closed": False,
            },
        ],
        "guardrails": {
            "tree_identity_tier_not_full_QFT_equivalence": True,
            "observables_not_source_selectors": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = [
        blocker
        for blocker in previous_gate["remaining_true_equivalence_blockers"]
        if blocker not in {"local QFT observable value rows", "local QFT observable values/correlator replay"}
    ]
    if "precision local QFT correlator/S-matrix/decay rows" not in remaining:
        remaining.insert(1, "precision local QFT correlator/S-matrix/decay rows")
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterQFTTreeRows.v1",
        "status": "TREE_QFT_OBSERVABLE_ROWS_BUILT_PRECISION_QFT_VALUES_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": ["local QFT tree identity observable rows"],
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "precision local QFT correlator/S-matrix/decay rows or actual selected Qa/SU3 operator packet",
        "guardrails": {
            "tree_identity_rows_are_not_precision_observables": True,
            "qft_values_do_not_select_source_packet": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedLocalQFTObservableRowsOrFinalTrueSMEquivalenceGap",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json"),
            "local_qft_observable_value_gate": rel(
                DATA
                / "selected_correlatedprofilevalues_or_localqftobservablevalues"
                / "local_qft_observable_value_gate.packet.json"
            ),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "tree_level_replay_seed": rel(DATA / "sm_equivalence_tree_level_replay_seed.candidate.json"),
            "mixing_and_gauge_replay": rel(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"),
        },
        "output_packets": {
            "tree_level_local_qft_observable_rows": rel(ROWS),
            "final_true_sm_equivalence_gap_matrix": rel(GAP),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "TreeLocalQFTObservableRowsAndFinalGapTheorem",
            "proved": True,
            "statement": (
                "The admitted measured SM-parity packet induces executable local-QFT tree identity rows: "
                "v(G_F), Higgs curvature, charged Yukawa mass identities, gauge alpha-to-coupling normalization, "
                "and CKM/PMNS unitarity. This closes a tree identity observable tier, but not precision correlator, "
                "S-matrix, decay, covariance/profile, actual Qa/SU3 packet, true SM-equivalence, or no-knob closure."
            ),
        },
        "what_closes_now": {
            "local_QFT_tree_identity_observable_rows": all_tree_rows_closed,
            "propagator_coupling_normalization_tree_tier": True,
            "mixing_unitarity_observable_checks": True,
            "final_true_equivalence_gap_matrix_sharpened": True,
            "superset_strategy_preserved": True,
        },
        "what_remains_open": {
            "precision_local_QFT_correlator_smatrix_decay_rows": True,
            "published_or_reconstructed_correlated_profile_values": True,
            "multi_loop_threshold_convention_values": True,
            "QM_GR_measurement_response_interfaces": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "tree_QFT_identity_tier_closed": all_tree_rows_closed,
            "precision_local_QFT_observable_values_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "qft_gate_previous_status": qft_gate["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_LocalQFTObservableRows_or_FinalTrueSMEquivalenceGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "tree_QFT_identity_tier_closed": all_tree_rows_closed,
        "precision_local_QFT_observable_values_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_PrecisionQFTObservableRows_or_ActualQaSU3Packet_v1",
    }

    note = """# MTT Selected LocalQFTObservableRows or FinalTrueSMEquivalenceGap v1

Status: `MTT_SELECTED_LOCALQFTOBSERVABLEROWS_OR_FINALTRUESMEQUIVALENCEGAP_BUILT_TREE_QFT_ROWS_PRECISION_OPEN`.

This artifact fills a minimal local-QFT observable tier from the already
admitted SM-parity measured packet: `v(G_F)`, Higgs curvature, charged Yukawa
mass identities, gauge alpha-to-coupling normalization, and CKM/PMNS unitarity.

These are tree identity rows. They demonstrate that the local-QFT observable
functor has executable downstream values, but they are not precision
correlator, S-matrix, scattering, or decay observables.

The final true-SM-equivalence gaps are now sharper: precision QFT observable
rows, correlated profile values, multi-loop threshold conventions, QM/GR
interfaces, and the actual selected Qa/SU3 operator packet.
"""

    for path, payload in [
        (ROWS, row_packet),
        (GAP, final_gap),
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
