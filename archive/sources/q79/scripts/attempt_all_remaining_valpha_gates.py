"""Attempt every remaining terminal V_alpha proof gate after lockdown.

This is an execution pass, not a magic promotion script.  It does three useful
things:

1. checks whether the terminal admissible-section principle can be treated as
   unconditional from current corpus evidence;
2. rebuilds the top V_alpha operator-source and same-source fusion attempts
   using the selected terminal ordered source and h1=8 Ext packet;
3. runs the primitive C1 calculator and SM-closure ledgers to identify the
   exact remaining blockers.

The expected honest result is that stale terminal-selection blockers disappear,
while the genuine selected-source/operator gates remain open.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
OUT_DIR = CANDIDATES / "all_remaining_valpha_gates"

LOCKDOWN_CERT = CERTS / "terminal_valpha_remaining_parts_lockdown_certificate.json"
TERMINAL_CERT = CERTS / "terminal_admissible_section_source_principle_certificate.json"
ORDERED_SELECTED = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_ordered_source.selected_under_section_principle.json"
)
COHOMOLOGY_SELECTED = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
)
CURRENT_VALPHA_ATTEMPT = CANDIDATES / "selected_valpha_chern_weil_operator_source.current_attempt.json"
CURRENT_FUSION_ATTEMPT = CANDIDATES / "same_source_monad_gs_operator_fusion.current_attempt.json"
SELECTED_S3_PACKET = CERTS / "visible_twisted_s3_class_restriction_packet.selected.json"
GS_SOURCE_ATTEMPT = CERTS / "time_oriented_m1_visible_gs_source.attempt.json"
PROMOTION_ATTEMPT = CERTS / "selected_hym_operator_source_promotion.attempt.json"
PRIMITIVE_C1_TEMPLATE = CERTS / "selected_c1_primitive_contractions.template.json"
SELECTED_MISSING_DATA = CERTS / "selected_missing_data_calculation_certificate.json"
FULL_SM_ATTEMPT = CERTS / "selected_full_sm_data_theorem_attempt_certificate.json"
GAUDUCHON_WALL = CERTS / "selected_gauduchon_wall_radius_gate_certificate.json"
VISIBLE_RANK2_ROUTE = CERTS / "visible_rank2_extension_valpha_route_certificate.json"

OUT_VALPHA_PACKET = OUT_DIR / "selected_valpha_chern_weil_operator_source.after_terminal_lockdown.json"
OUT_FUSION_PACKET = OUT_DIR / "same_source_monad_gs_operator_fusion.after_terminal_lockdown.json"
OUT_CANDIDATE = CANDIDATES / "all_remaining_valpha_gates_attempt.candidate.json"
OUT_CERT = CERTS / "all_remaining_valpha_gates_attempt_certificate.json"

SECTION_SOURCES = [
    Path(
        r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\5 Dirac Delta"
        r"\Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md"
    ),
    Path(
        r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\1 Core & Encodings"
        r"\The_Modal_Triplet_Theory_Program_C__Realizing_the_Modal_Triplet_Core.md"
    ),
    Path(
        r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\1 Core & Encodings"
        r"\The_Modal_Triplet_Theory_Program_B5__Saturated_and_Unified_Encodings.md"
    ),
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def run(args: list[str]) -> dict[str, Any]:
    proc = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "stdout_head": proc.stdout.strip().splitlines()[:20],
    }


def run_validator(script: str, packet: Path, prefix: str) -> dict[str, Any]:
    result = run([sys.executable, str(ROOT / "scripts" / script), str(packet)])
    parsed: dict[str, Any] = {}
    for line in result["stdout"].splitlines():
        if line.startswith(prefix):
            parsed = json.loads(line[len(prefix) :])
            break
    result["parsed_report"] = parsed
    return result


def terminal_principle_gate(terminal: dict[str, Any]) -> dict[str, Any]:
    source_text = "\n".join(read(path) for path in SECTION_SOURCES)
    literal_unconditional = (
        "TerminalAdmissibleSectionSourcePrinciple" in source_text
        or "terminal admissible-section source principle" in source_text
    )
    corpus_support = terminal.get("corpus_support", {}).get("supported") is True
    return {
        "gate": "UnconditionalTerminalAdmissibleSectionTheorem",
        "status": "AXIOM_READY_NOT_UNCONDITIONAL"
        if corpus_support and not literal_unconditional
        else "CLOSED"
        if corpus_support and literal_unconditional
        else "OPEN",
        "corpus_support": corpus_support,
        "literal_unconditional_statement_found_in_corpus": literal_unconditional,
        "sources_checked": [str(path) for path in SECTION_SOURCES],
        "closed": corpus_support and literal_unconditional,
        "next_required_action": (
            "Add/prove this as a named theorem in the MTT spine or derive it from "
            "the projection-admissibility formalism."
        ),
    }


def stability_gate(
    cohomology: dict[str, Any],
    wall: dict[str, Any],
    rank2_route: dict[str, Any],
) -> dict[str, Any]:
    target_wall = wall.get("wall_dictionary", {}).get("target_wall", {})
    selected_ext = (
        cohomology.get("reported_cohomology", {}).get("h1") == 8
        and cohomology.get("acceptance_tests", {}).get("extension_class_closed") is True
        and cohomology.get("acceptance_tests", {}).get("extension_class_not_exact") is True
    )
    non_split_input = selected_ext
    negative_slope_chamber = (
        target_wall.get("selects_target_as_unique_negative") is True
        and target_wall.get("chamber", {}).get("p") == [1, 2, 1]
    )
    missing_contract = rank2_route.get("stability_contract", {}).get(
        "missing_sufficient_inputs",
        [],
    )
    return {
        "gate": "SelectedNonSplitVAlphaStabilityOrRouteCResidual",
        "status": "PARTIAL_NON_SPLIT_INPUT_CLOSED_STABILITY_OPEN",
        "closed_subparts": {
            "selected_h1_8_nonzero_ext": selected_ext,
            "non_split_extension_input": non_split_input,
            "negative_slope_chamber_witness": negative_slope_chamber,
            "split_hym_shortcut_retired": True,
        },
        "still_missing": [
            "proof no other positive-slope line subsheaf injects into V_alpha",
            "selected HYM/Strominger residual or Route-C residual pass",
            "source-derived stable bundle/sheaf construction",
        ],
        "rank2_route_missing_contract": missing_contract,
        "closed": False,
    }


def build_after_lockdown_valpha_packet() -> dict[str, Any]:
    packet = copy.deepcopy(load(CURRENT_VALPHA_ATTEMPT))
    packet["status"] = "ATTEMPT_AFTER_TERMINAL_LOCKDOWN_SOURCE_OPERATOR_OPEN"

    identity = packet.setdefault("source_identity", {})
    identity["selected_by_mtt"] = False
    identity["fixture_only"] = True
    identity["source_certificate"] = None

    valpha = packet.setdefault("valpha_extension", {})
    valpha["ordered_source_packet"] = rel(ORDERED_SELECTED)
    valpha["rank2_valpha_model_selected"] = True
    valpha["terminal_monad_difference_L3_minus_K2_selector_closed"] = True
    valpha["ordered_source_validator_passes"] = True
    valpha["nonzero_ext_class_selected"] = True
    valpha["pic0_resolution"] = "OPEN_OPERATOR_LAYER_RECHECK"
    valpha["pic0_selected_or_quotiented"] = False
    valpha["non_split_stability_or_hym_proved"] = False

    support = packet.setdefault("s3_green_schwarz_support", {})
    support["s3_class_restriction_packet"] = rel(SELECTED_S3_PACKET)
    support["visible_gs_source_packet"] = rel(GS_SOURCE_ATTEMPT)
    support["same_source_link_valpha_to_s3_proved"] = False
    support["chern_weil_row_derived_from_same_source"] = False
    support["visible_gs_source_validator_passes"] = False

    execution = packet.setdefault("operator_execution", {})
    execution["selected_source_promotion_packet"] = rel(PROMOTION_ATTEMPT)
    for key in [
        "typed_transition_or_rhoE_data_emitted",
        "hym_strominger_or_routec_residual_pass",
        "sector_D_E_packets_pass",
        "reduced_green_packets_pass",
        "dotD_packets_pass",
        "same_branch_derivative_verified",
        "coherent_spectral_projector_retention",
        "selected_source_promotion_validator_passes",
        "primitive_C1_or_Yukawa_contractions",
    ]:
        execution[key] = False

    branch = packet.setdefault("branch_orientation", {})
    branch["orientation_selection_justified_by_source"] = False
    return packet


def build_after_lockdown_fusion_packet() -> dict[str, Any]:
    packet = copy.deepcopy(load(CURRENT_FUSION_ATTEMPT))
    packet["status"] = "ATTEMPT_AFTER_TERMINAL_LOCKDOWN_SAME_SOURCE_OPEN"

    source = packet.setdefault("source_identity", {})
    source["source_kind"] = "selected_visible_SM_bundle_operator_source"
    source["selected_by_mtt"] = False
    source["fixture_only"] = True
    source["same_source_for_ordered_L_pic0_GS_and_DE"] = False
    source["source_certificate"] = None

    ordered = packet.setdefault("ordered_source", {})
    ordered["visible_rank2_l2_ordered_source_packet"] = rel(ORDERED_SELECTED)
    ordered["source_lane_selector"] = "terminal_monad_difference_Li_minus_K2"
    ordered["selected_L"] = [1, -2, 0]
    ordered["selected_L2"] = [2, -4, 0]
    ordered["standard_lattice_or_equivalent_selected"] = True
    ordered["base_factor_order_selected"] = True
    ordered["base_swap_broken_by_source"] = True
    ordered["pic0_resolution"] = "pic0_quotient_rule"
    ordered["ordered_source_validator_passes"] = True

    gs = packet.setdefault("green_schwarz_and_gerbe", {})
    gs["time_oriented_m1_representative_used"] = True
    gs["antiunitary_q369_retained"] = True
    gs["visible_green_schwarz_row_derived_from_same_source"] = False
    gs["freed_witten_or_cycle_restrictions_verified_if_used"] = True
    gs["projector_retention_verified"] = True

    op = packet.setdefault("operator_response", {})
    op["iwasawa_selected_source_promotion_packet"] = rel(PROMOTION_ATTEMPT)
    for key in [
        "route_c_residuals_pass",
        "de_action_pass",
        "riesz_gap_pass",
        "reduced_green_pass",
        "dotd_response_pass",
        "selected_dotD_source_verified",
        "primitive_C1_contractions",
    ]:
        op[key] = False

    return packet


def operator_gates() -> dict[str, Any]:
    valpha_packet = build_after_lockdown_valpha_packet()
    fusion_packet = build_after_lockdown_fusion_packet()
    write(OUT_VALPHA_PACKET, valpha_packet)
    write(OUT_FUSION_PACKET, fusion_packet)

    valpha_validation = run_validator(
        "validate_selected_valpha_chern_weil_operator_source.py",
        OUT_VALPHA_PACKET,
        "selected_valpha_chern_weil_operator_source_report=",
    )
    fusion_validation = run_validator(
        "validate_same_source_monad_gs_operator_fusion_packet.py",
        OUT_FUSION_PACKET,
        "same_source_monad_gs_operator_fusion_report=",
    )

    valpha_open = valpha_validation.get("parsed_report", {}).get("open_items", [])
    fusion_open = fusion_validation.get("parsed_report", {}).get("open_items", [])

    return {
        "generated_packets": {
            "selected_valpha_after_lockdown": rel(OUT_VALPHA_PACKET),
            "same_source_fusion_after_lockdown": rel(OUT_FUSION_PACKET),
        },
        "selected_valpha_validator": {
            "exit_code": valpha_validation["exit_code"],
            "status": valpha_validation.get("parsed_report", {}).get("status"),
            "open_item_count": len(valpha_open),
            "open_items": valpha_open,
            "subvalidators": valpha_validation.get("parsed_report", {}).get("subvalidators", {}),
        },
        "same_source_fusion_validator": {
            "exit_code": fusion_validation["exit_code"],
            "status": fusion_validation.get("parsed_report", {}).get("status"),
            "open_item_count": len(fusion_open),
            "open_items": fusion_open,
            "subvalidators": fusion_validation.get("parsed_report", {}).get("subvalidators", {}),
        },
        "gates": {
            "OperatorLayerPic0Recheck": {
                "status": "OPEN",
                "reason": "top V_alpha packet still requires operator-layer Pic0 resolution",
                "closed": False,
            },
            "SameSourceChernWeilGSRow": {
                "status": "OPEN",
                "reason": "visible GS source validator still rejects copied row without source derivation",
                "closed": False,
            },
            "SameSourceDErhoERieszGreenDotD": {
                "status": "OPEN",
                "reason": "selected-source promotion validator still rejects unselected Route-C smoke data",
                "closed": False,
            },
        },
    }


def primitive_and_sm_gates() -> dict[str, Any]:
    primitive_run = run(
        [
            sys.executable,
            str(ROOT / "scripts" / "compute_c1_response_matrices.py"),
            str(PRIMITIVE_C1_TEMPLATE),
        ]
    )
    missing = [
        line.removeprefix("- ").strip()
        for line in primitive_run["stdout"].splitlines()
        if line.startswith("- ")
    ]
    missing_data = load(SELECTED_MISSING_DATA)
    sm = load(FULL_SM_ATTEMPT)
    return {
        "PrimitiveC1Contractions": {
            "status": "OPEN",
            "calculator_exit_code": primitive_run["exit_code"],
            "missing_primitive_count": len(missing),
            "missing_primitives": missing,
            "selected_missing_data_first_blocker": missing_data.get("computed_result", {}).get(
                "first_blocking_layer"
            ),
            "closed": False,
        },
        "NoProxyYukawaCKMPMNSAndSMClosure": {
            "status": "OPEN",
            "selected_full_sm_attempt_status": sm.get("status"),
            "actual_selected_raw_matrices_computed": sm.get("attempt_result", {}).get(
                "actual_selected_raw_matrices_computed"
            ),
            "actual_selected_canonical_matrices_computed": sm.get("attempt_result", {}).get(
                "actual_selected_canonical_matrices_computed"
            ),
            "safe_to_claim_theorem": sm.get("attempt_result", {}).get("safe_to_claim_theorem"),
            "missing_selected_inputs": sm.get("missing_selected_inputs", {}),
            "closed": False,
        },
    }


def analyze() -> dict[str, Any]:
    terminal = load(TERMINAL_CERT)
    lockdown = load(LOCKDOWN_CERT)
    cohomology = load(COHOMOLOGY_SELECTED)
    wall = load(GAUDUCHON_WALL)
    rank2_route = load(VISIBLE_RANK2_ROUTE)

    section_gate = terminal_principle_gate(terminal)
    stability = stability_gate(cohomology, wall, rank2_route)
    operators = operator_gates()
    primitive_sm = primitive_and_sm_gates()

    gate_summary = {
        section_gate["gate"]: section_gate["status"],
        stability["gate"]: stability["status"],
        **{
            name: gate["status"]
            for name, gate in operators["gates"].items()
        },
        **{
            name: gate["status"]
            for name, gate in primitive_sm.items()
        },
    }

    newly_retired = {
        "selected_valpha_attempt_no_longer_blocks_on_ordered_source_validator": (
            operators["selected_valpha_validator"]["subvalidators"]
            .get("ordered_source", {})
            .get("exit_code")
            == 0
        ),
        "same_source_fusion_no_longer_blocks_on_ordered_source_validator": (
            operators["same_source_fusion_validator"]["subvalidators"]
            .get("ordered_source", {})
            .get("exit_code")
            == 0
        ),
        "selected_h1_ext_promoted_to_non_split_input": stability["closed_subparts"][
            "non_split_extension_input"
        ],
    }

    all_attempted = set(gate_summary) == {
        "UnconditionalTerminalAdmissibleSectionTheorem",
        "SelectedNonSplitVAlphaStabilityOrRouteCResidual",
        "OperatorLayerPic0Recheck",
        "SameSourceChernWeilGSRow",
        "SameSourceDErhoERieszGreenDotD",
        "PrimitiveC1Contractions",
        "NoProxyYukawaCKMPMNSAndSMClosure",
    }
    expected_open_shape = (
        all_attempted
        and section_gate["status"] == "AXIOM_READY_NOT_UNCONDITIONAL"
        and stability["status"] == "PARTIAL_NON_SPLIT_INPUT_CLOSED_STABILITY_OPEN"
        and operators["selected_valpha_validator"]["exit_code"] == 2
        and operators["same_source_fusion_validator"]["exit_code"] == 2
        and primitive_sm["PrimitiveC1Contractions"]["calculator_exit_code"] == 2
        and all(newly_retired.values())
    )

    return {
        "calculation": "AllRemainingVAlphaGatesAttempt",
        "status": "ALL_REMAINING_VALPHA_GATES_ATTEMPTED_SELECTED_OPERATOR_SOURCE_STILL_REQUIRED"
        if expected_open_shape
        else "ALL_REMAINING_VALPHA_GATES_ATTEMPT_INCONSISTENT",
        "generated_by": "scripts/attempt_all_remaining_valpha_gates.py",
        "lockdown_input": rel(LOCKDOWN_CERT),
        "gate_summary": gate_summary,
        "unconditional_section_gate": section_gate,
        "stability_or_routec_gate": stability,
        "operator_gates": operators,
        "primitive_and_sm_gates": primitive_sm,
        "newly_retired_by_after_lockdown_attempts": newly_retired,
        "still_open_cut_set": [
            "named terminal section theorem or axiom promotion",
            "stability/HYM or selected Route-C residual for V_alpha",
            "operator-layer Pic0",
            "same-source Chern-Weil/GS derivation",
            "same-source D_E/Riesz/Green/dotD selected data",
            "24 primitive C1 contraction matrices",
            "selected Yukawa/CKM/PMNS/Higgs/RG data",
        ],
        "guardrails": {
            "claims_unconditional_selector_proved": False,
            "claims_stability_or_HYM_proved": False,
            "claims_operator_layer_Pic0_resolved": False,
            "claims_same_source_operator_data_constructed": False,
            "claims_primitive_C1_values_computed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "All seven gates were attempted. The terminal selected source and "
                "h1=8/nonzero Ext data now propagate into the operator packets, "
                "so ordered-source failures are gone. The remaining blocker is "
                "not stale arithmetic; it is the genuine selected operator source: "
                "stability/Route-C, operator-layer Pic0, same-source GS and "
                "D_E/Riesz/Green/dotD, then primitive C1 and no-proxy SM matrices."
            )
        },
    }


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "AllRemainingVAlphaGatesAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": rel(OUT_CANDIDATE),
        "lockdown_input": report["lockdown_input"],
        "gate_summary": report["gate_summary"],
        "generated_packets": report["operator_gates"]["generated_packets"],
        "selected_valpha_validator": report["operator_gates"]["selected_valpha_validator"],
        "same_source_fusion_validator": report["operator_gates"]["same_source_fusion_validator"],
        "unconditional_section_gate": report["unconditional_section_gate"],
        "stability_or_routec_gate": report["stability_or_routec_gate"],
        "primitive_and_sm_gates": report["primitive_and_sm_gates"],
        "newly_retired_by_after_lockdown_attempts": report[
            "newly_retired_by_after_lockdown_attempts"
        ],
        "still_open_cut_set": report["still_open_cut_set"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "ALL_REMAINING_VALPHA_GATES_ATTEMPTED_SELECTED_OPERATOR_SOURCE_STILL_REQUIRED"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
