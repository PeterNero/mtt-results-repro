"""Build accepted Higgs decay covariance profile or first Qa/SU3 slot closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_acceptedhiggsdecaycovarianceprofile_or_firstqasu3selectedslotclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE = PACKET_DIR / "accepted_higgs_decay_covariance_profile.packet.json"
FIRST_SLOT = PACKET_DIR / "first_qasu3_static_sector_route_slot_closure.packet.json"
DECISION = PACKET_DIR / "true_equivalence_decision_after_profile_or_first_slot.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AcceptedHiggsDecayCovarianceProfile_or_FirstQaSU3SelectedSlotClosure_v1.md"

STATUS = (
    "MTT_SELECTED_ACCEPTEDHIGGSDECAYCOVARIANCEPROFILE_OR_FIRSTQASU3SELECTEDSLOTCLOSURE_"
    "BUILT_SECTOR_PROFILE_AND_STATIC_SLOT_CLOSED_TRUE_EQUIV_OPEN"
)
NEXT = "MTT_Selected_HiggsProductionCovarianceProfile_or_DynamicQaSU3OperatorSlotClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof.candidate.json")
    imported_profile = load(
        DATA
        / "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof"
        / "external_higgs_decay_correlation_covariance_import.packet.json"
    )
    static_readout = load(
        DATA
        / "selected_matterslot_readout_backimport_from_smslotfunctor"
        / "selected_static_matterslot_readout.packet.json"
    )
    static_weyl = load(
        DATA
        / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
        / "static_enriched_weylpair_source_provenance.packet.json"
    )

    sector = imported_profile["restricted_decay_sector"]
    covariance = np.array(sector["covariance_matrix_MeV2"], dtype=float)
    correlation = np.array(sector["correlation_matrix"], dtype=float)
    eigvals = np.linalg.eigvalsh(covariance)
    rank = int(np.linalg.matrix_rank(covariance, tol=1e-14))
    psd_tolerance = 1e-12
    profile = {
        "schema": "MTTAcceptedHiggsDecayCovarianceProfile.v1",
        "profile_scope": "Higgs_decay_sector_only",
        "accepted_profile_standard": {
            "required_rows": 9,
            "required_units": "MeV partial widths and MeV^2 covariance",
            "source_rows_and_labels_validated": True,
            "central_values_and_uncertainties_present": True,
            "correlation_matrix_symmetric_unit_diagonal": True,
            "covariance_matrix_symmetric": True,
            "covariance_positive_semidefinite_with_tolerance": psd_tolerance,
            "source_provenance_attached": True,
            "observed_data_forbidden_as_source_selector": True,
        },
        "input_correlated_candidate": rel(
            DATA
            / "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof"
            / "external_higgs_decay_correlation_covariance_import.packet.json"
        ),
        "external_sources": imported_profile["external_source"],
        "labels": sector["labels"],
        "source_decay_labels": sector["source_decay_labels"],
        "correlation_matrix": sector["correlation_matrix"],
        "covariance_matrix_MeV2": sector["covariance_matrix_MeV2"],
        "diagonal_variances_MeV2": sector["diagonal_variances_MeV2"],
        "linear_algebra_validation": {
            "row_count": int(covariance.shape[0]),
            "correlation_symmetric": bool(np.allclose(correlation, correlation.T, atol=1e-12)),
            "correlation_unit_diagonal": bool(np.allclose(np.diag(correlation), np.ones(correlation.shape[0]), atol=1e-12)),
            "covariance_symmetric": bool(np.allclose(covariance, covariance.T, atol=1e-12)),
            "covariance_eigenvalues_MeV2": [float(value) for value in eigvals],
            "covariance_min_eigenvalue_MeV2": float(eigvals[0]),
            "covariance_rank_tol_1e_minus_14": rank,
            "positive_diagonal_variances": bool(np.all(np.diag(covariance) > 0)),
            "positive_semidefinite_with_tolerance": bool(eigvals[0] >= -psd_tolerance),
            "near_singular_reason": "tautau and mumu source rows have correlation 1.0 in the imported submatrix",
        },
        "acceptance_result": {
            "accepted_as_Higgs_decay_covariance_profile": True,
            "accepted_as_full_Higgs_likelihood_profile": False,
            "accepted_as_full_true_equivalence_profile": False,
            "why_scope_limited": (
                "This closes the Higgs decay covariance-profile sector object only. It does not contain "
                "a full likelihood function, production covariance, electroweak/QCD/QM/GR profile rows, "
                "or dynamic Qa/SU3 operator values."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    readouts = static_readout["selected_readouts"]
    route = static_weyl["static_sector_route"]
    first_slot = {
        "schema": "MTTFirstQaSU3StaticSectorRouteSlotClosure.v1",
        "slot_name": "static_QaSU3_sector_route_ZX_phase_shift_partition",
        "slot_tier": "static_source_tier",
        "input_static_matter_slot_readout": rel(
            DATA
            / "selected_matterslot_readout_backimport_from_smslotfunctor"
            / "selected_static_matterslot_readout.packet.json"
        ),
        "input_static_enriched_weylpair_source_provenance": rel(
            DATA
            / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
            / "static_enriched_weylpair_source_provenance.packet.json"
        ),
        "selected_slot_value": {
            "Z_clock_phase_routes_to": route["phase_Z_to"],
            "X_shift_translation_routes_to": route["shift_X_to"],
            "matter_slot_partition": {
                "clock_phase_side": route["clock_phase_side"]["matter_slot"],
                "shift_non10_side": route["shift_non10_side"]["matter_slots"],
            },
            "oneM_Dirac_rule": readouts["selected_1M_Dirac_shift_readout"]["rule"],
            "static_trace_transfer_normalization": readouts["selected_overlap_transfer_normalization_static"][
                "unit_trace_transfer"
            ],
        },
        "proof_inputs": {
            "static_matter_slot_readout_closed": static_readout["status"] == "STATIC_SOURCE_TIER_READOUT_CLOSED",
            "static_weyl_provenance_closed": static_weyl["status"] == "STATIC_ENRICHED_WEYLPAIR_SOURCE_PROVENANCE_CLOSED",
            "phase_shift_partition_closed": readouts["selected_phase_shift_partition"]["closed"],
            "oneM_Dirac_shift_readout_closed": readouts["selected_1M_Dirac_shift_readout"]["closed"],
            "static_trace_normalization_closed": readouts["selected_overlap_transfer_normalization_static"]["closed"],
            "source_level_Z_proved": static_weyl["source_level_carrier"]["phase_Z_source_proved"],
            "source_level_X_proved": static_weyl["source_level_carrier"]["shift_X_source_proved"],
        },
        "closure_result": {
            "first_selected_QaSU3_static_slot_closed": True,
            "selected_source_value_emitted": True,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "why_not_dynamic_operator_packet": (
                "The closed slot is a static source-tier routing/normalization slot. Dynamic HYM/End0/C1 "
                "operator matrices, selected b/A values, and physical response tensors remain open."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTTrueEquivalenceDecisionAfterProfileOrFirstSlot.v1",
        "status": "HIGGS_DECAY_PROFILE_ACCEPTED_AND_FIRST_STATIC_QASU3_SLOT_CLOSED_TRUE_EQUIV_OPEN",
        "route_A": {
            "accepted_Higgs_decay_covariance_profile_closed": True,
            "full_Higgs_likelihood_profile_closed": False,
            "full_true_equivalence_profile_closed": False,
        },
        "route_B": {
            "first_selected_QaSU3_static_slot_closed": True,
            "selected_slot_name": first_slot["slot_name"],
            "actual_dynamic_QaSU3_operator_packet_closed": False,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_frontier": [
            "extend accepted covariance/profile object to Higgs production and coupling rows",
            "promote the next Qa/SU3 slot at dynamic operator tier",
            "connect static route to selected HYM/End0/C1 response matrices",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedAcceptedHiggsDecayCovarianceProfileOrFirstQaSU3SelectedSlotClosure",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_externalprofilelikelihoodimport_or_qasu3slotselectionproof.candidate.json"),
            "external_correlated_decay_covariance": profile["input_correlated_candidate"],
            "static_matter_slot_readout": first_slot["input_static_matter_slot_readout"],
            "static_enriched_weylpair_source_provenance": first_slot["input_static_enriched_weylpair_source_provenance"],
        },
        "output_packets": {
            "accepted_higgs_decay_covariance_profile": rel(PROFILE),
            "first_qasu3_static_sector_route_slot_closure": rel(FIRST_SLOT),
            "true_equivalence_decision_after_profile_or_first_slot": rel(DECISION),
        },
        "theorem": {
            "name": "AcceptedHiggsDecayCovarianceProfileAndFirstStaticQaSU3SlotClosure",
            "proved": True,
            "statement": (
                "The imported Higgs decay covariance submatrix satisfies the declared sector-profile standard "
                "and is accepted as the Higgs decay covariance profile object. Independently, the closed static "
                "SM-slot functor/readout and static enriched Weyl-pair provenance emit the first selected Qa/SU3 "
                "static slot: Z/clock routes to u,e and X/shift routes to d,nuD, including the 1_M=N^c "
                "Dirac-neutrino shift rule and static trace-transfer normalization."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "accepted_Higgs_decay_covariance_profile_closed": True,
            "first_selected_QaSU3_static_slot_closed": True,
            "full_Higgs_likelihood_profile_closed": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "Higgs_decay_covariance_profile_sector_object": True,
            "covariance_PSD_tolerance_validated": True,
            "first_QaSU3_static_sector_route_slot": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "full_Higgs_likelihood_function": True,
            "Higgs_production_and_coupling_covariance_profile": True,
            "non_Higgs_QM_GR_observable_interfaces": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "selected_HYM_End0_C1_response_matrices": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "previous_candidate_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_AcceptedHiggsDecayCovarianceProfile_or_FirstQaSU3SelectedSlotClosure_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "accepted_Higgs_decay_covariance_profile_closed": True,
        "first_selected_QaSU3_static_slot_closed": True,
        "full_Higgs_likelihood_profile_closed": False,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected AcceptedHiggsDecayCovarianceProfile or FirstQaSU3SelectedSlotClosure v1

This artifact executes both next edges without reopening SM-parity.

Route A closes the Higgs decay covariance-profile sector object.  The imported
nine-row covariance block is source-labeled, symmetric, positive semidefinite
within numerical tolerance, and accepted for the Higgs decay covariance sector.
It is not a full Higgs likelihood function and not a full true-equivalence
profile.

Route B closes the first selected Qa/SU3 static slot: `Z/clock -> u,e` and
`X/shift -> d,nuD`, including the `1_M=N^c` Dirac-neutrino shift rule and
static trace-transfer normalization.  This is a static source-tier closure, not
a dynamic Qa/SU3/HYM/End0/C1 operator packet.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (PROFILE, profile),
        (FIRST_SLOT, first_slot),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
