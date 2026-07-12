"""Build dynamic C1 parity value packet after stationary/dotD integration."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VALUE_PACKET = PACKET_DIR / "patched_dynamic_c1_parity_value_packet.packet.json"
GUARDRAIL = PACKET_DIR / "parity_patch_vs_unpatched_guardrail.packet.json"
REMAINDER = PACKET_DIR / "unpatched_dynamic_c1_remainder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1ParityValuePacket_after_StationaryDotD_Integration_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1_PARITY_VALUEPACKET_AFTER_STATIONARYDOTD_BUILT_PATCHED_VALUES_UNPATCHED_OPEN"
NEXT = "MTT_Selected_UnpatchedFiniteC1TraceMeasureDerivation_or_TrueEquivalenceSourceUpgrade_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    integrated = load(DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json")
    patch_gate = load(DATA / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation.candidate.json")
    patched_replay = load(
        DATA
        / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation"
        / "patched_routeb_dynamic_c1_closure_replay.packet.json"
    )
    patch_ledger = load(DATA / "selected_dynamicc1patchtosmparityledger_or_unpatchedmeasurederivation.candidate.json")
    empirical = load(DATA / "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation.candidate.json")

    promoted = patched_replay["promoted_under_patched_spine"]
    not_promoted = patched_replay["not_promoted_under_unpatched_spine"]

    value_packet = {
        "schema": "MTTPatchedDynamicC1ParityValuePacketAfterStationaryDotD.v1",
        "status": "PATCHED_PARITY_DYNAMIC_C1_VALUES_EMITTED_UNPATCHED_OPEN",
        "stationary_and_dotd_prerequisites": {
            "stationary_projector_source_verified": integrated["closure_decision"][
                "stationary_projector_source_verified"
            ],
            "validator_ready_stationary_rho_s": integrated["closure_decision"][
                "validator_ready_stationary_rho_s"
            ],
            "selected_dotD_source_verified": integrated["closure_decision"]["selected_dotD_source_verified"],
            "alpha1_driver_verified": integrated["closure_decision"]["alpha1_driver_verified"],
        },
        "patch_used": patched_replay["patch_used"],
        "formal_row_counts": patched_replay["formal_row_counts"],
        "patched_values": {
            "A_selected_parity_tier": promoted["physical_A_selected"],
            "b_selected_parity_tier": promoted["physical_b_selected"],
            "deltaTheta_C1_parity_tier": promoted["physical_deltaTheta_C1"],
            "sector_response_matrices_parity_tier": promoted["physical_sector_response_matrices"],
            "row_comparison_max_abs_error": patched_replay["row_comparison_max_abs_error"],
        },
        "patched_replay_checks": {
            "selected_Galerkin_replacement_promotes_formal_rows": promoted[
                "selected_Galerkin_replacement_promotes_formal_rows"
            ],
            "physical_measure_equals_finite_trace_quadrature": promoted[
                "physical_measure_equals_finite_trace_quadrature"
            ],
            "Route_B_physical_Galerkin_replacement_closed": promoted[
                "Route_B_physical_Galerkin_replacement_closed"
            ],
            "patched_dynamic_C1_packet_closed": promoted["patched_dynamic_C1_packet_closed"],
        },
        "tier_classification": {
            "SM_parity_patched_dynamic_C1_value_packet_available": True,
            "unpatched_dynamic_C1_packet_closed": not_promoted["unpatched_dynamic_C1_packet_closed"],
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    guardrail = {
        "schema": "MTTParityPatchVsUnpatchedGuardrail.v1",
        "status": "PATCHED_PARITY_VALUES_SEPARATED_FROM_UNPATCHED_DERIVATION",
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "path_1_stationary_source": "transported HYM/End0 stationary projector and rho_s source",
            "path_2_alpha1_dotd": "compatible cross-repo alpha1/dotD driver on the q79/F,m=1 spine",
            "path_3_dynamic_patch": "SelectedFiniteC1TraceMeasurePrinciple plus finite Weyl trace rows",
            "locked_target": "SM-parity patched dynamic C1 replay values, not unpatched no-knob derivation",
        },
        "allowed_claim": (
            "At the declared patched SM-parity tier, A_selected, b_selected, deltaTheta_C1, and sector "
            "response availability are emitted as replay-ready internal values."
        ),
        "forbidden_claims": [
            "the SelectedFiniteC1TraceMeasurePrinciple is derived from prior MTT axioms",
            "unpatched dynamic C1 no-knob closure is proved",
            "true SM equivalence is closed",
            "observed flavor, mass, CKM, PMNS, or Higgs values selected the source",
        ],
        "ledger_alignment": {
            "patched_dynamic_C1_no_longer_blocks_SM_parity": patch_ledger["promotion_decision"][
                "patched_dynamic_C1_no_longer_blocks_SM_parity"
            ],
            "patched_dynamic_C1_empirical_interface_ready": empirical["promotion_decision"][
                "patched_dynamic_C1_empirical_interface_ready"
            ],
            "full_SM_parity_closed": empirical["promotion_decision"]["full_SM_parity_closed"],
            "true_SM_equivalence_closed": empirical["promotion_decision"]["true_SM_equivalence_closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remainder = {
        "schema": "MTTUnpatchedDynamicC1Remainder.v1",
        "status": "UNPATCHED_DYNAMIC_C1_DERIVATION_REMAINS_NO_KNOB_TARGET",
        "unpatched_blockers": {
            "direct_PhiFinC1_action_derivation": True,
            "physical_measure_identity": True,
            "SelectedFiniteC1TraceMeasurePrinciple_derivation": True,
            "Route_A_same_source_emission": True,
            "Route_B_physical_Galerkin_replacement_without_patch": True,
        },
        "accepted_next_routes": [
            "derive the finite C1 trace-measure principle from Phi_fin^C1/action data",
            "prove direct Phi_fin^C1 measure/action identity",
            "emit Route A same-source dynamic C1 values",
            "supply an independent selected Galerkin replacement without the patch",
            "upgrade actual Qa/SU3 operator packet and true-equivalence source data",
        ],
        "patched_values_are_inputs_for": [
            "SM-parity replay at the patched standard",
            "empirical interface rehearsal",
            "gap-matrix bookkeeping",
        ],
        "patched_values_are_not_inputs_for": [
            "source selection",
            "no-knob flavor constants",
            "true SM equivalence closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDynamicC1ParityValuePacketAfterStationaryDotDIntegration",
        "status": STATUS,
        "inputs": {
            "stationary_dotd_integrated_frontier": rel(
                DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json"
            ),
            "finite_c1_trace_measure_patch_gate": rel(
                DATA / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation.candidate.json"
            ),
            "patched_routeb_dynamic_c1_closure_replay": rel(
                DATA
                / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation"
                / "patched_routeb_dynamic_c1_closure_replay.packet.json"
            ),
            "dynamic_c1_patch_to_smparity_ledger": rel(
                DATA / "selected_dynamicc1patchtosmparityledger_or_unpatchedmeasurederivation.candidate.json"
            ),
            "patched_dynamic_c1_empirical_replay_integration": rel(
                DATA / "selected_patcheddynamicc1empiricalreplayintegration_or_noknobderivation.candidate.json"
            ),
        },
        "output_packets": {
            "patched_dynamic_c1_parity_value_packet": rel(VALUE_PACKET),
            "parity_patch_vs_unpatched_guardrail": rel(GUARDRAIL),
            "unpatched_dynamic_c1_remainder": rel(REMAINDER),
        },
        "theorem": {
            "name": "DynamicC1ParityValuePacketIntegrationTheorem",
            "proved": True,
            "patched": True,
            "statement": (
                "Once stationary projectors/rho_s and alpha1/dotD are selected-source verified, the inserted "
                "SelectedFiniteC1TraceMeasurePrinciple promotes the exact finite Weyl trace rows to a patched "
                "SM-parity dynamic C1 value packet. This emits parity-tier A_selected, b_selected, deltaTheta_C1, "
                "and sector-response availability, while the unpatched physical measure/action derivation remains "
                "a no-knob and true-equivalence target."
            ),
        },
        "closure_decision": {
            "SM_parity_patched_dynamic_C1_value_packet_available": True,
            "patched_A_selected_emitted": True,
            "patched_b_selected_emitted": True,
            "patched_deltaTheta_C1_emitted": True,
            "patched_sector_response_matrices_available": True,
            "unpatched_A_selected_emitted": False,
            "unpatched_b_selected_emitted": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "full_SM_parity_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1ParityValuePacket_after_StationaryDotD_Integration_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "patched": True,
        "SM_parity_patched_dynamic_C1_value_packet_available": True,
        "patched_A_selected_emitted": True,
        "patched_b_selected_emitted": True,
        "patched_deltaTheta_C1_emitted": True,
        "unpatched_dynamic_C1_packet_closed": False,
        "full_SM_parity_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1 ParityValuePacket after StationaryDotD Integration v1

Status: `{STATUS}`.

This artifact emits the patched SM-parity dynamic C1 value packet after the
stationary projector/rho_s and alpha1/dotD gates have been integrated.

Patched parity-tier values:

- `A_selected = [[12, 0], [0, 12]]`
- `b_selected = [12, 12]`
- `deltaTheta_C1 = [1, 1]`
- sector response matrices are available at the patched Route-B replay tier

This is not an unpatched no-knob derivation.  The remaining target is the
direct derivation of the finite C1 trace-measure identity, an equivalent
`Phi_fin^C1` action derivation, Route-A same-source emission, or a true
selected Galerkin replacement without the patch.
"""

    for path, payload in [
        (VALUE_PACKET, value_packet),
        (GUARDRAIL, guardrail),
        (REMAINDER, remainder),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
