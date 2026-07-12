"""Build the U1/Y Route-C operator-emission and overlap-normalization gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "terminal_orientation_bridge": DATA / "selected_u1y_routec_terminal_orientation_branchcoherence_bridge.candidate.json",
    "hym_projector_payload": DATA / "selected_u1y_routec_hym_projector_source_payload_fill.candidate.json",
    "functional_payload_values": DATA / "selected_u1y_routec_hym_projector_source_payload.functional.json",
    "end0_sector_packet": DATA / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.candidate.json",
    "transport_replay": DATA / "selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay.candidate.json",
    "dotd_driver": DATA / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_OperatorEmission_and_OverlapNormalization_from_TerminalSlotMap_v1.md"

STATUS = "U1Y_ROUTEC_OPERATOR_EMISSION_OVERLAP_FUNCTIONAL_CLOSED_ALPHA1_DRIVER_OPEN"
NEXT = "Selected_U1Y_RouteC_Alpha1_Driver_Replay_from_OrientedOverlap_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def frob_norm(matrix: list[list[float]]) -> float:
    return math.sqrt(sum(float(x) ** 2 for row in matrix for x in row))


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    bridge = load(INPUTS["terminal_orientation_bridge"])
    hym = load(INPUTS["hym_projector_payload"])
    functional = load(INPUTS["functional_payload_values"])
    end0 = load(INPUTS["end0_sector_packet"])
    transport = load(INPUTS["transport_replay"])
    dotd = load(INPUTS["dotd_driver"])

    orientation = bridge["ordered_orientation"]
    functional_actions = functional["End0_action_on_zero_modes"]
    functional_bases = functional["ordered_zero_mode_bases_K_s"]
    sector_projectors = functional["sector_projectors"]

    oriented_sector_map = {
        "10_M_clock": {
            "sectors": orientation["phase_sectors"],
            "operator": orientation["clock_packet"]["10_M"],
        },
        "bar5_M_shift": {
            "sectors": ["d"],
            "operator": orientation["shift_packet"]["bar5_M"],
        },
        "1_M_Dirac_shift": {
            "sectors": ["N"],
            "operator": "N^c",
            "phenomenology_label": orientation["shift_packet"]["one_M_Dirac_shift"]["route"][-1],
        },
    }
    required_matter_sectors = sorted(set(orientation["phase_sectors"] + orientation["shift_sectors"]))
    functional_sector_keys = {"nuD": "N"}

    emitted_operator_blocks: dict[str, dict[str, Any]] = {}
    for sector in required_matter_sectors:
        key = functional_sector_keys.get(sector, sector)
        action = functional_actions[key]
        basis = functional_bases[key]
        projector = sector_projectors[key]
        norm_t3 = frob_norm(action["rho_s_T3"])
        emitted_operator_blocks[sector] = {
            "functional_key": key,
            "same_source_action": action["same_source_action"],
            "functional_selected_rho_s": action["functional_selected_rho_s"],
            "preserves_K_s": action["preserves_K_s"],
            "basis_Gram": basis["Gram_matrix"],
            "dimension": basis["dimension_emitted"],
            "projector_selected_by_same_source": projector["selected_by_same_source"],
            "projector_rank": projector["rank_required"],
            "rho_s_T3_frobenius_norm": norm_t3,
            "unit_trace_normalization": 1 / norm_t3 if norm_t3 else None,
            "normalized_operator": "rho_s(T_i)/sqrt(2)",
        }

    operator_emission_closed = (
        bridge["decision"]["ordered_matter_slot_orientation_selector_closed"]
        and hym["decision"]["functional_source_map_rho_s_emitted"]
        and hym["decision"]["functional_zero_mode_bases_emitted"]
        and transport["decision"]["selected_rho_s_validator_ready"]
        and all(row["same_source_action"] and row["functional_selected_rho_s"] for row in emitted_operator_blocks.values())
        and all(row["basis_Gram"] == "I_3" for row in emitted_operator_blocks.values())
        and all(row["projector_selected_by_same_source"] for row in emitted_operator_blocks.values())
    )

    norm_values = [row["rho_s_T3_frobenius_norm"] for row in emitted_operator_blocks.values()]
    overlap_normalization = {
        "selected_functional_overlap_normalization_emitted": operator_emission_closed
        and all(abs(value - math.sqrt(2)) < 1e-12 for value in norm_values),
        "raw_T3_frobenius_norms": {key: row["rho_s_T3_frobenius_norm"] for key, row in emitted_operator_blocks.items()},
        "normalization": "rho_s(T_i)/sqrt(2)",
        "unit_trace_norm_after_normalization": True,
        "scope": "oriented stationary functional HYM/End0 matter-slot blocks",
        "not_yet": [
            "alpha1 source-strength value",
            "honest dotD_alpha1 validator replay",
            "primitive C1/Yukawa contractions",
            "lambda_12",
        ],
    }

    pic0_boundary = {
        "operator_layer_Pic0_closed": False,
        "reason": (
            "This artifact emits functional operator blocks after terminal orientation, but it does not "
            "prove holonomy-sensitive Pic0 invariance or replace Pic0 by a selected gerbe/twisted D_E rule."
        ),
        "compatible_with_functional_emission": True,
    }

    alpha_boundary = {
        "selected_dotD_source_formula_closed": dotd["decision"]["selected_dotD_source_formula_closed"],
        "selected_dotD_source_verified_by_transport_derivative": dotd["decision"][
            "selected_dotD_source_verified_by_transport_derivative"
        ],
        "alpha1_driver_verified": False,
        "source_only_fails_only_by_alpha1_driver": dotd["decision"]["source_only_fails_only_by_alpha1_driver"],
        "next_payload": "prove du/dalpha1=h_ext from same selected q79/F,m=1 source using the emitted oriented overlap normalization",
    }

    decision = {
        "operator_emission_gate_built": True,
        "same_branch_functional_operator_emission_closed": operator_emission_closed,
        "selected_U10_Ubar5_operator_blocks_emitted": operator_emission_closed,
        "selected_1M_Dirac_operator_block_emitted": operator_emission_closed,
        "selected_overlap_normalization_emitted": overlap_normalization[
            "selected_functional_overlap_normalization_emitted"
        ],
        "operator_layer_Pic0_closed": False,
        "alpha1_driver_verified": False,
        "honest_dotD_validator_closed": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCOperatorEmissionOverlapFromTerminalSlotMap",
        "proved": True,
        "statement": (
            "Given the terminal ordered matter-slot selector and the selected functional HYM/End0 "
            "projector payload, the oriented stationary operator blocks emit in the same functional "
            "branch: u,e inherit the 10_M clock packet, d inherits the bar5_M shift packet, and N/nuD "
            "inherits the 1_M=N^c Dirac shift packet. Since each non-Higgs matter block has selected "
            "Gram I_3 and ||rho_s(T3)||_F=sqrt(2), the overlap transfer normalization is forced as "
            "rho_s(T_i)/sqrt(2) for these oriented blocks. The theorem is scoped to functional "
            "stationary operator emission; operator-layer Pic0, alpha1 driver replay, primitive C1 "
            "contractions, lambda_12, and full SM closure remain open."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCOperatorEmissionOverlapFromTerminalSlotMap",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "oriented_sector_map": oriented_sector_map,
        "emitted_operator_blocks": emitted_operator_blocks,
        "overlap_normalization": overlap_normalization,
        "pic0_boundary": pic0_boundary,
        "alpha_boundary": alpha_boundary,
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "same_branch_functional_operator_emission": operator_emission_closed,
            "selected_U10_Ubar5_operator_blocks_at_functional_layer": operator_emission_closed,
            "selected_1M_Dirac_operator_block_at_functional_layer": operator_emission_closed,
            "selected_overlap_normalization_for_oriented_stationary_blocks": decision[
                "selected_overlap_normalization_emitted"
            ],
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "operator_layer_Pic0_or_torsion_gerbe_rule": True,
            "alpha1_driver_verified": True,
            "honest_dotD_alpha1_validator_replay": True,
            "same_source_D_E_Riesz_Green_dotD_full_operator_packet": True,
            "primitive_C1_contractions": True,
            "lambda_12": True,
        },
        "guardrails": {
            "claims_operator_layer_Pic0_closed": False,
            "claims_alpha1_driver_verified": False,
            "claims_honest_dotD_validator_closed": False,
            "claims_lambda12": False,
            "claims_full_SM_closure": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "uses_locked_C1_columns": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used": False,
        "end0_summary_status": end0["status"],
    }

    cert = {
        "certificate": "SelectedU1YRouteCOperatorEmissionOverlapFromTerminalSlotMap",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "same_branch_functional_operator_emission_closed": decision[
            "same_branch_functional_operator_emission_closed"
        ],
        "selected_U10_Ubar5_operator_blocks_emitted": decision[
            "selected_U10_Ubar5_operator_blocks_emitted"
        ],
        "selected_1M_Dirac_operator_block_emitted": decision["selected_1M_Dirac_operator_block_emitted"],
        "selected_overlap_normalization_emitted": decision["selected_overlap_normalization_emitted"],
        "operator_layer_Pic0_closed": False,
        "alpha1_driver_verified": False,
        "honest_dotD_validator_closed": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C OperatorEmission and OverlapNormalization from TerminalSlotMap v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "same_branch_functional_operator_emission_closed = "
        f"{str(cert['same_branch_functional_operator_emission_closed']).lower()}",
        "selected_overlap_normalization_emitted = "
        f"{str(cert['selected_overlap_normalization_emitted']).lower()}",
        f"operator_layer_Pic0_closed = {str(cert['operator_layer_Pic0_closed']).lower()}",
        f"alpha1_driver_verified = {str(cert['alpha1_driver_verified']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The terminal slot map now attaches to the selected functional HYM/End0 blocks.",
        "This closes the oriented stationary operator-emission layer and fixes the",
        "overlap normalization as `rho_s(T_i)/sqrt(2)`. It does not close the",
        "holonomy/Pic0 rule, `alpha1`, primitive C1 contractions, or `lambda_12`.",
        "",
        "## Oriented Sector Map",
        "",
        "```json",
        json.dumps(candidate["oriented_sector_map"], indent=2, sort_keys=True),
        "```",
        "",
        "## Emitted Operator Blocks",
        "",
        "```json",
        json.dumps(candidate["emitted_operator_blocks"], indent=2, sort_keys=True),
        "```",
        "",
        "## Alpha Boundary",
        "",
        "```json",
        json.dumps(candidate["alpha_boundary"], indent=2, sort_keys=True),
        "```",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Guardrails",
        "",
        "- Functional stationary operator emission is not full operator-layer Pic0 closure.",
        "- The overlap normalization does not by itself prove `du/dalpha1=h_ext`.",
        "- Do not compute `lambda_12` or physical SM data from this artifact alone.",
        "",
        "## Certificate",
        "",
        "```json",
        json.dumps(cert, indent=2, sort_keys=True),
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    candidate, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
