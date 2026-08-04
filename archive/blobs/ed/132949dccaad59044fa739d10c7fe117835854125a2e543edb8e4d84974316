"""Import Route-C differentiated PhiFinC1 residual-projector/Galerkin contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "routec_source_map_selection_boundary_import_certificate.json"
UPSTREAM_SLUG = "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
UPSTREAM_AXIOM = UPSTREAM_DIR / "residual_projector_axiom_patch_contract.packet.json"
UPSTREAM_GALERKIN = UPSTREAM_DIR / "honest_galerkin_execution_acceptance_contract.packet.json"
UPSTREAM_IMPLICATION = UPSTREAM_DIR / "closure_implication_replay.packet.json"

OUTPUT_PACKET = DATA / "routec_differentiated_phifinc1_contract_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_differentiated_phifinc1_contract_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_DifferentiatedPhiFinC1_Contract_Import_v1.md"

STATUS = "ROUTEC_DIFFERENTIATED_PHIFINC1_CONTRACT_IMPORTED_LANES_OPEN"
PREVIOUS_STATUS = "ROUTEC_SOURCE_MAP_SELECTION_BOUNDARY_IMPORTED_DYNAMIC_APPLICATION_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_DIFFERENTIATEDPHIFINC1_RESIDUALPROJECTORAXIOM_OR_GALERKINC1EXECUTION_BUILT_CONTRACT_OPEN"
NEXT = "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    axiom = load(UPSTREAM_AXIOM)
    galerkin = load(UPSTREAM_GALERKIN)
    implication = load(UPSTREAM_IMPLICATION)
    premises = axiom["premises_required"]
    axiom_payload = axiom["new_axiom_payload_if_accepted"]
    exact_values = axiom["exact_source_values_to_emit"]
    galerkin_values = galerkin["current_values_available"]
    replay = implication["current_numeric_replay_if_axiom_accepted"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1",
        "F1_upstream_packet_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["observed_data_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["theorem_proved"] is True
        and upstream_cert["candidate_path"].endswith(f"{UPSTREAM_SLUG}.candidate.json"),
        "F3_axiom_contract_ready_not_inserted": axiom["status"] == "AXIOM_CONTRACT_READY_NOT_INSERTED"
        and all(
            premises[key] is True
            for key in [
                "selected_qutrit_weyl_carrier",
                "selected_static_route_Z_clock_to_u_e",
                "selected_static_route_X_shift_to_d_nuD",
                "selected_trace_transfer_normalization",
                "canonical_Q_residual_available",
                "alpha1_dotD_driver_verified",
            ]
        )
        and axiom_payload["selected_differentiated_PhiFinC1_applies_Q_residual"] is True
        and axiom_payload["b_source_emitted"] is True
        and exact_values["routed_total_residual_norm_sq"] == 12.0
        and exact_values["conditional_b_norm_sq"] == 24.0
        and axiom["inserted_now"] is False
        and axiom["selected_now"] is False,
        "F4_galerkin_contract_ready_values_missing": galerkin["status"]
        == "GALERKIN_EXECUTION_CONTRACT_READY_VALUES_MISSING"
        and galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72
        and all(
            galerkin_values[key] is False
            for key in [
                "selected_source_verified",
                "can_replace_source_map_now",
                "A_selected_emitted",
                "b_selected_emitted",
                "sector_response_matrices_emitted",
            ]
        )
        and galerkin["would_close_SM_parity_dynamic_packet_if_accepted"] is True
        and galerkin["would_close_no_knob_flavor_constants_by_itself"] is False,
        "F5_implication_replay_proved_antecedent_open": implication["status"]
        == "IMPLICATION_PROVED_ANTECEDENT_OPEN"
        and implication["proved_now"] is True
        and implication["antecedent_currently_met"] is False
        and replay["rank"] == 2
        and replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and replay["A_transpose_b"] == [12.0, 12.0]
        and replay["deltaTheta_C1"] == [1.0, 1.0],
        "F6_both_lanes_would_close_dynamic_not_no_knob_flavor": implication[
            "if_axiom_contract_accepted_then"
        ]["SM_parity_dynamic_packet_would_close"]
        is True
        and implication["if_honest_galerkin_contract_filled_then"][
            "SM_parity_dynamic_packet_would_close"
        ]
        is True
        and implication["if_axiom_contract_accepted_then"][
            "no_knob_flavor_constants_would_close"
        ]
        is False
        and implication["if_honest_galerkin_contract_filled_then"][
            "no_knob_flavor_constants_would_close_by_default"
        ]
        is False,
        "F7_remaining_gates_preserved": all(
            upstream["what_remains_open"][key] is True
            for key in [
                "derive_or_insert_residual_projector_axiom",
                "prove_selected_differentiated_PhiFinC1_application_rule",
                "emit_selected_b_source_vector",
                "run_honest_selected_Galerkin_C1_execution",
                "promote_A_selected",
                "promote_b_selected",
                "promote_deltaTheta_C1",
                "emit_sector_response_matrices",
                "SM_parity_dynamic_packet_closure",
                "true_SM_equivalence_closure",
                "full_no_knob_flavor_closure",
            ]
        ),
        "F8_no_promotion_overclaim": all(
            upstream["promotion_decision"][key] is False
            for key in [
                "residual_projector_axiom_inserted_now",
                "differentiated_PhiFinC1_application_rule_proved_now",
                "honest_Galerkin_C1_execution_run_now",
                "A_selected_promoted",
                "b_selected_promoted",
                "deltaTheta_C1_promoted",
                "sector_response_matrices_promoted",
                "SM_parity_dynamic_packet_closed",
                "true_SM_equivalence_closed",
                "no_knob_flavor_constants_closed",
            ]
        ),
    }

    summary = {
        "lane_A_axiom_contract_ready": axiom["status"] == "AXIOM_CONTRACT_READY_NOT_INSERTED",
        "lane_A_inserted_now": axiom["inserted_now"],
        "lane_A_selected_now": axiom["selected_now"],
        "lane_A_would_emit_PhiFinC1_applies_Q": axiom_payload[
            "selected_differentiated_PhiFinC1_applies_Q_residual"
        ],
        "lane_A_would_emit_b_source": axiom_payload["b_source_emitted"],
        "lane_B_galerkin_contract_ready": galerkin["status"]
        == "GALERKIN_EXECUTION_CONTRACT_READY_VALUES_MISSING",
        "lane_B_selected_source_verified": galerkin_values["selected_source_verified"],
        "routed_total_residual_norm_sq": exact_values["routed_total_residual_norm_sq"],
        "conditional_b_norm_sq": exact_values["conditional_b_norm_sq"],
        "replay_A_transpose_A": replay["A_transpose_A"],
        "replay_A_transpose_b": replay["A_transpose_b"],
        "replay_deltaTheta_C1": replay["deltaTheta_C1"],
        "replay_rank": replay["rank"],
    }

    return {
        "packet": "RouteC_DifferentiatedPhiFinC1_Contract_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_axiom_contract": str(UPSTREAM_AXIOM),
            "upstream_galerkin_contract": str(UPSTREAM_GALERKIN),
            "upstream_implication_replay": str(UPSTREAM_IMPLICATION),
        },
        "theorem": {
            "name": "RouteCDifferentiatedPhiFinC1ContractImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The dynamic C1 blocker is converted into two strict lanes: "
                "a residual-projector axiom/theorem lane and an honest "
                "Galerkin C1 execution lane.  The closure implication is "
                "proved with rank 2, A^T A=12 I, A^T b=(12,12), and "
                "deltaTheta_C1=(1,1), but neither lane is selected or executed."
            ),
        },
        "checks": checks,
        "differentiated_phifinc1_contract_summary": summary,
        "upstream_differentiated_phifinc1_contract": upstream,
        "upstream_packets": {
            "axiom_contract": axiom,
            "galerkin_contract": galerkin,
            "implication_replay": implication,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_residual_projector_axiom_inserted": False,
            "claims_differentiated_PhiFinC1_application_rule": False,
            "claims_honest_Galerkin_C1_execution": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_deltaTheta_C1": False,
            "claims_sector_response_matrices": False,
            "claims_SM_parity_dynamic_packet_closure": False,
            "claims_full_no_knob_flavor_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCDifferentiatedPhiFinC1ContractImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "differentiated_phifinc1_contract_summary": packet[
            "differentiated_phifinc1_contract_summary"
        ],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["differentiated_phifinc1_contract_summary"]
    return f"""# RouteC Differentiated PhiFinC1 Contract Import v1

Status: `{cert["status"]}`.

The dynamic C1 blocker is now a two-lane contract:

```text
Lane A: residual-projector axiom/theorem insertion
Lane B: honest selected Galerkin C1 execution
```

The implication replay is exact:

```text
rank = {s["replay_rank"]}
A^T A = {s["replay_A_transpose_A"]}
A^T b = {s["replay_A_transpose_b"]}
deltaTheta_C1 = {s["replay_deltaTheta_C1"]}
```

Neither lane is selected yet.  The residual-projector axiom is not inserted,
the differentiated `Phi_fin^C1` application rule is not proved, and honest
Galerkin C1 values are not emitted.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
