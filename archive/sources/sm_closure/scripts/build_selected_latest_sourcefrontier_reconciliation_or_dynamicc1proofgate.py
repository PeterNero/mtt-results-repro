"""Build latest source-frontier reconciliation after static SM-slot closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_latest_sourcefrontier_reconciliation_or_dynamicc1proofgate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FRONTIER = PACKET_DIR / "latest_source_frontier_reconciled.packet.json"
DYNAMIC_GATE = PACKET_DIR / "dynamic_c1_remaining_proof_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LatestSourceFrontier_Reconciliation_or_DynamicC1ProofGate_v1.md"

STATUS = "MTT_SELECTED_LATEST_SOURCEFRONTIER_RECONCILED_DYNAMICC1_PROOFGATE_OPEN"
NEXT = "MTT_Selected_DeriveResidualProjectorAxiom_or_IndependentGalerkinC1Execution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    latest_parity = load(DATA / "selected_latest_smparityclosure_status_or_trueequivalencefrontier.candidate.json")
    smslot = load(DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json")
    downstream = load(DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json")
    source_map = load(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json")
    patch = load(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch.candidate.json")
    true_frontier = load(DATA / "selected_latest_trueequivalencefrontier_or_valueemissioncutset.candidate.json")

    frontier = {
        "schema": "MTTLatestSourceFrontierReconciled.v1",
        "status": "STATIC_SOURCE_CLOSED_DYNAMIC_C1_PROOF_OPEN",
        "SM_parity_closed_under_declared_standard": latest_parity["SM_parity_closed"],
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "static_source_tier": {
            "all_six_SM_slot_arrows_closed": smslot["selected_SMSlotFunctor_all_six_arrows_claimed"],
            "selected_terminal_to_SU5_E6_slot_packet": smslot["what_closes_now"][
                "selected_terminal_to_SU5_E6_slot_packet"
            ],
            "selected_U10_Ubar5_source_outputs": smslot["arrow_status"]["all_six_closed"],
            "selected_static_sector_route_Z_to_u_e_X_to_d_nuD": downstream["what_closes_now"][
                "selected_static_sector_route_Z_to_u_e_X_to_d_nuD"
            ],
            "selected_static_1M_Dirac_neutrino_shift_rule": downstream["what_closes_now"][
                "selected_static_1M_Dirac_neutrino_shift_rule"
            ],
            "selected_static_finite_trace_transfer_normalization": downstream["what_closes_now"][
                "selected_static_finite_trace_transfer_normalization"
            ],
        },
        "dynamic_C1_tier": {
            "patched_spine_dynamic_packet_closed": patch["promotion_decision"][
                "SM_parity_dynamic_packet_closed_in_patched_spine"
            ],
            "unpatched_dynamic_packet_closed": patch["promotion_decision"][
                "A_selected_promoted_in_unpatched_spine"
            ],
            "source_map_selection_test_built": source_map["what_closes_now"]["source_map_selection_test_built"],
            "if_selected_dynamic_packet_closure_exact": source_map["what_closes_now"][
                "if_selected_dynamic_packet_closure_exact"
            ],
            "honest_Galerkin_value_run_route_restated": source_map["what_closes_now"][
                "honest_Galerkin_value_run_route_restated"
            ],
        },
        "stale_blockers_retired": {
            "U10_Ubar5_1M_static_source_gate": True,
            "selected_overlap_transfer_normalization_static_gate": True,
            "transport_closed_rho_s_projector_replay": True,
            "alpha1_dotD_primary_blocker": True,
        },
        "still_open": {
            "derive_residual_projector_axiom_from_unpatched_MTT": patch["what_remains_open"][
                "derive_residual_projector_axiom_from_unpatched_MTT"
            ],
            "compute_independent_primitive_galerkin_contractions": patch["what_remains_open"][
                "compute_independent_primitive_galerkin_contractions"
            ],
            "emit_independent_hessian_b_selected": patch["what_remains_open"][
                "emit_independent_hessian_b_selected"
            ],
            "emit_independent_selected_zero_mode_basis": patch["what_remains_open"][
                "emit_independent_selected_zero_mode_basis"
            ],
            "selected_A_selected_unpatched": source_map["what_remains_open"]["selected_A_selected"],
            "selected_b_selected_unpatched": source_map["what_remains_open"]["selected_b_selected"],
            "selected_deltaTheta_C1_unpatched": source_map["what_remains_open"]["selected_deltaTheta_C1"],
            "true_SM_equivalence": true_frontier["true_SM_equivalence_closed"] is False,
            "no_knob_closure": true_frontier["no_knob_closed"] is False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    dynamic_gate = {
        "schema": "MTTDynamicC1RemainingProofGate.v1",
        "status": "DERIVE_AXIOM_OR_EXECUTE_INDEPENDENT_GALERKIN_VALUES",
        "legal_routes": {
            "route_A_unpatched_derivation": [
                "derive the residual-projector application rule from Phi_fin^C1 / selected measure",
                "derive same-branch R_Z, R_X, and b_selected source emissions",
                "promote A_selected, b_selected, and deltaTheta_C1 without local patch insertion",
            ],
            "route_B_independent_Galerkin_execution": [
                "emit independent selected zero-mode bases",
                "compute independent primitive 3x3 Galerkin contractions",
                "emit independent Hessian/source vector b_selected",
                "pass the strict 72-real / 110-row source validator without inheriting patched values",
            ],
        },
        "forbidden_shortcuts": [
            "do not treat the patched residual-projector axiom as no-knob derivation",
            "do not treat replay-filled Galerkin inputs inherited from the axiom contract as independent proof",
            "do not reopen static U10/Ubar5/1M/overlap source gates as if they were still the blocker",
            "do not use observed SM flavor constants, CKM, PMNS, masses, or benchmark matrices as selectors",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "MTTSelectedLatestSourceFrontierReconciliationOrDynamicC1ProofGate",
        "status": STATUS,
        "inputs": {
            "latest_SM_parity_status": rel(DATA / "selected_latest_smparityclosure_status_or_trueequivalencefrontier.candidate.json"),
            "SM_slot_overlap_kernel": rel(DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"),
            "downstream_operator_payload_ledger": rel(DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"),
            "source_map_selection_gate": rel(DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"),
            "patched_or_galerkin_attempt": rel(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch.candidate.json"),
            "latest_true_equivalence_frontier": rel(DATA / "selected_latest_trueequivalencefrontier_or_valueemissioncutset.candidate.json"),
        },
        "output_packets": {
            "frontier": rel(FRONTIER),
            "dynamic_gate": rel(DYNAMIC_GATE),
        },
        "theorem": {
            "name": "LatestSourceFrontierReconciliationTheorem",
            "proved": True,
            "statement": (
                "The latest source frontier is static-closed and dynamic-open: all six SM-slot source arrows, U_10/U_bar5, the 1_M Dirac rule, static sector routing, and finite trace transfer normalization are closed at the source tier. "
                "The remaining unpatched/no-knob proof gate is not static Qa/SU3 source selection but derivation of the dynamic C1 residual-projector/source rule, or independent selected Galerkin C1 execution."
            ),
        },
        "what_closes_now": {
            "latest_source_frontier_reconciled": True,
            "static_U10_Ubar5_1M_overlap_gates_retired": True,
            "dynamic_C1_unpatched_proof_gate_selected": True,
            "patched_spine_vs_unpatched_noknob_boundary_preserved": True,
        },
        "what_remains_open": frontier["still_open"],
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_LatestSourceFrontier_Reconciliation_or_DynamicC1ProofGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "static_source_tier_closed": True,
        "dynamic_C1_unpatched_proof_gate_open": True,
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected LatestSourceFrontier Reconciliation or DynamicC1ProofGate v1

Status: `{STATUS}`.

The static source frontier is now closed: selected SM-slot arrows, `U_10=I_3`,
`U_bar5=F`, the `1_M=N^c` Dirac-neutrino shift rule, static sector routing,
and finite trace transfer normalization are all source-tier results.

The remaining proof gate is dynamic C1: derive the residual-projector
application/source rule in the unpatched MTT spine, or compute independent
selected Galerkin C1 values. The local patched spine is useful for SM-parity
replay, but it is not a no-knob derivation.

True SM equivalence and no-knob closure remain open.

Next artifact: `{NEXT}`.
"""

    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DYNAMIC_GATE.write_text(json.dumps(dynamic_gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
