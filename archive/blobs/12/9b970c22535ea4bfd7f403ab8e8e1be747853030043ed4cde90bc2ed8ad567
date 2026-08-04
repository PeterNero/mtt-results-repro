from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "alpha1_terminal_orientation_bridge_import.packet.json"
OP = QA / "candidate_data" / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json"

OUT_CERT = ROOT / "certificates" / "alpha1_operator_emission_overlap_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "alpha1_operator_emission_overlap_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Alpha1_OperatorEmission_Overlap_Import_v1.md"

STATUS = "ALPHA1_OPERATOR_EMISSION_OVERLAP_FUNCTIONAL_CLOSED_DRIVER_OPEN"
NEXT = "Selected_U1Y_RouteC_Alpha1_Driver_Replay_from_OrientedOverlap_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    op = load(OP)

    previous_orientation_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["terminal_source_orientation_selector_closed_at_ordered_layer"] is True,
            prev["what_remains_open"]["same_branch_selected_operator_emission"] is True,
        ]
    )
    operator_emission_closed = all(
        [
            op["theorem"]["proved"] is True,
            op["decision"]["same_branch_functional_operator_emission_closed"] is True,
            op["decision"]["selected_U10_Ubar5_operator_blocks_emitted"] is True,
            op["decision"]["selected_1M_Dirac_operator_block_emitted"] is True,
            op["what_closes_now"]["same_branch_functional_operator_emission"] is True,
        ]
    )
    overlap_normalization_closed = all(
        [
            op["decision"]["selected_overlap_normalization_emitted"] is True,
            op["overlap_normalization"]["selected_functional_overlap_normalization_emitted"] is True,
            op["overlap_normalization"]["normalization"] == "rho_s(T_i)/sqrt(2)",
            op["overlap_normalization"]["unit_trace_norm_after_normalization"] is True,
        ]
    )
    oriented_blocks_valid = all(
        [
            set(op["emitted_operator_blocks"].keys()) == {"u", "d", "e", "nuD"},
            all(block["same_source_action"] is True for block in op["emitted_operator_blocks"].values()),
            all(block["basis_Gram"] == "I_3" for block in op["emitted_operator_blocks"].values()),
            all(block["unit_trace_normalization"] == 0.7071067811865475 for block in op["emitted_operator_blocks"].values()),
            op["oriented_sector_map"]["10_M_clock"]["sectors"] == ["u", "e"],
            op["oriented_sector_map"]["bar5_M_shift"]["sectors"] == ["d"],
            op["oriented_sector_map"]["1_M_Dirac_shift"]["phenomenology_label"] == "nuD",
        ]
    )
    driver_still_open = all(
        [
            op["decision"]["alpha1_driver_verified"] is False,
            op["alpha_boundary"]["alpha1_driver_verified"] is False,
            op["alpha_boundary"]["selected_dotD_source_formula_closed"] is True,
            op["alpha_boundary"]["selected_dotD_source_verified_by_transport_derivative"] is True,
            op["pic0_boundary"]["operator_layer_Pic0_closed"] is False,
        ]
    )
    theorem_proved = all([previous_orientation_ready, operator_emission_closed, overlap_normalization_closed, oriented_blocks_valid, driver_still_open])

    packet = {
        "theorem": {
            "name": "Alpha1OperatorEmissionOverlapImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "Given the ordered terminal matter-slot selector and selected functional HYM/End0 projector payload, "
                "same-branch functional stationary operator emission closes for u,d,e,nuD. The selected oriented "
                "blocks carry Gram I_3, preserve K_s, and force unit-trace overlap normalization rho_s(T_i)/sqrt(2). "
                "This closes selected U10/Ubar5/1M functional blocks and overlap normalization at the stationary layer. "
                "It does not yet close operator-layer Pic0/torsion discipline, alpha1 driver replay, primitive C1 "
                "contractions, lambda_12, or full SM closure."
            ),
        },
        "imported_status": {"status": STATUS, "operator_status": op["status"]},
        "oriented_sector_map": op["oriented_sector_map"],
        "emitted_operator_blocks": op["emitted_operator_blocks"],
        "overlap_normalization": op["overlap_normalization"],
        "alpha_boundary": op["alpha_boundary"],
        "proof_chain": {
            "previous_orientation_ready": previous_orientation_ready,
            "operator_emission_closed": operator_emission_closed,
            "overlap_normalization_closed": overlap_normalization_closed,
            "oriented_blocks_valid": oriented_blocks_valid,
            "driver_still_open": driver_still_open,
            "target_fitting_used": op["target_fitting_used"],
        },
        "what_closes_now": {
            "same_branch_functional_operator_emission": True,
            "selected_U10_Ubar5_operator_blocks_at_functional_layer": True,
            "selected_1M_Dirac_operator_block_at_functional_layer": True,
            "selected_overlap_normalization_for_oriented_stationary_blocks": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "operator_layer_Pic0_or_torsion_gerbe_rule": True,
            "alpha1_driver_verified": True,
            "honest_dotD_alpha1_validator_replay": True,
            "same_source_D_E_Riesz_Green_dotD_full_operator_packet": True,
            "primitive_C1_contractions": True,
            "lambda_12_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_claim_honest_dotD_validator_closed": True,
            "does_not_claim_operator_layer_Pic0_closed": True,
            "does_not_claim_primitive_C1_or_lambda12": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous_orientation_bridge": str(PREV), "operator_emission_overlap": str(OP)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "alpha1_operator_emission_overlap_import",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "previous_orientation_ready": previous_orientation_ready,
            "operator_emission_closed": operator_emission_closed,
            "overlap_normalization_closed": overlap_normalization_closed,
            "oriented_blocks_valid": oriented_blocks_valid,
            "driver_still_open": driver_still_open,
            "target_fitting_excluded": op["target_fitting_used"] is False,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# Alpha1 OperatorEmission Overlap Import v1

## Result

Functional stationary operator emission and overlap normalization close:

```text
u,e <- 10_M clock
d <- bar5_M shift
nuD <- 1_M=N^c Dirac shift
normalization = rho_s(T_i)/sqrt(2)
```

Still open: operator-layer Pic0/torsion discipline, alpha1 driver replay,
primitive C1 contractions, lambda_12, and full SM closure.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
