"""Reduce the ordered L2 layer to the terminal monad lane selector.

After the ordered-layer Pic0 quotient theorem, the Pic0 switch is no longer a
local Chern/H1/curvature blocker.  This script proves the remaining local
ordered-layer gate is exactly the source-lane selector:

    MTT selects the visible ordered L source from central-neutral terminal
    monad differences L_i-K2.

Conditional uniqueness then forces L3-K2, and the validator passes after only
that source-lane switch is hypothetically supplied.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

PIC0_PACKET = (
    CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_pic0_quotiented_layer.json"
)
OUT_PACKET = CANDIDATES / "visible_rank2_l2_ordered_source.terminal_lane_hypothetical_selected.json"
OUT_CANDIDATE = CANDIDATES / "ordered_layer_terminal_lane_selector_reduction.candidate.json"
OUT_CERT = CERTS / "ordered_layer_terminal_lane_selector_reduction_certificate.json"

VALIDATOR = ROOT / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"

PIC0_QUOTIENT = CERTS / "ordered_layer_pic0_quotient_certificate.json"
SELECTED_MONAD_ATTEMPT = CERTS / "selected_monad_difference_l2_source_proof_attempt_certificate.json"
UNCONDITIONAL_ATTEMPT = CERTS / "unconditional_selected_monad_difference_l2_source_attempt_certificate.json"
H1_GATE = CERTS / "visible_rank2_l2_ext_h1_gate_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def validate(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    parsed: dict[str, Any] = {}
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_ordered_source_validation_report="):
            parsed = json.loads(line.split("=", 1)[1])
            break
    return {
        "packet": rel(path),
        "exit_code": proc.returncode,
        "validator_status": parsed.get("status"),
        "open_items": parsed.get("open_items", []),
        "failures": parsed.get("failures", []),
        "target_matrix": parsed.get("target_matrix"),
    }


def apply_terminal_lane_source(packet: dict[str, Any]) -> dict[str, Any]:
    selected = copy.deepcopy(packet)
    selected["candidate_role"] = "SELECTED_DATA"
    selected["status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"
    source = selected.setdefault("source", {})
    source["fixture_only"] = False
    source["selected_by_mtt"] = True
    source["source_certificate"] = "Selected_Terminal_Monad_Lane_Source_Selector.v1"
    source["source_status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"
    evidence = selected.setdefault("selection_evidence", {})
    evidence["standard_lattice_or_equivalent_selected"] = True
    evidence["base_factor_order_selected"] = True
    evidence["base_swap_broken_by_source"] = True
    evidence["not_only_finite_mod3_qutrit"] = True
    evidence["not_equal_radius_import"] = True
    return selected


def analyze() -> dict[str, Any]:
    pic0 = load(PIC0_QUOTIENT)
    selected_monad = load(SELECTED_MONAD_ATTEMPT)
    unconditional = load(UNCONDITIONAL_ATTEMPT)
    h1_gate = load(H1_GATE)

    pic0_validation = pic0.get("validation", {}).get("pic0_quotiented_layer_packet", {})
    pic0_closed = (
        pic0.get("status") == "ORDERED_LAYER_PIC0_QUOTIENT_PROVED_OPERATOR_LAYER_REOPENS"
        and pic0.get("what_this_closes", {}).get(
            "pic0_quotient_for_ordered_chern_h1_curvature_layer"
        )
        is True
    )
    only_source_open = (
        pic0_validation.get("exit_code") == 2
        and pic0.get("validation", {}).get("only_source_selection_items_remain") is True
    )

    base_packet = load(PIC0_PACKET)
    selected_packet = apply_terminal_lane_source(base_packet)
    write(OUT_PACKET, selected_packet)
    selected_validation = validate(OUT_PACKET)

    theorem = selected_monad.get("conditional_uniqueness_theorem", {})
    scan = selected_monad.get("terminal_monad_difference_scan", {})
    conditional_lane_forces_l3k2 = (
        theorem.get("proved") is True
        and scan.get("target_matches") == ["L3-K2"]
        and scan.get("double_target_matches") == ["L3-K2"]
        and scan.get("zero_central_terminal_differences") == ["L3-K2"]
    )
    unconditional_source_open = (
        unconditional.get("status")
        == "UNCONDITIONAL_SELECTED_MONAD_DIFFERENCE_L2_SOURCE_ATTEMPT_BLOCKED_NO_SELECTOR_OR_PIC0_RULE"
        and unconditional.get("unconditional_theorem_attempt", {}).get("source_lane_selected")
        is False
    )
    selected_lane_would_pass = (
        selected_validation.get("exit_code") == 0
        and selected_validation.get("validator_status") == "PASS"
        and selected_validation.get("open_items") == []
    )

    h1_ready = (
        h1_gate.get("status") == "VISIBLE_RANK2_L2_EXT_H1_VALIDATOR_FORMULATED_DATA_OPEN"
        or h1_gate.get("what_this_closes", {}).get("h1_8_ext_dimension_gate")
    )

    reduction_proved = (
        pic0_closed
        and only_source_open
        and conditional_lane_forces_l3k2
        and unconditional_source_open
        and selected_lane_would_pass
    )

    report = {
        "calculation": "OrderedLayerTerminalLaneSelectorReduction",
        "status": (
            "ORDERED_LAYER_REDUCED_TO_TERMINAL_MONAD_LANE_SELECTOR"
            if reduction_proved
            else "ORDERED_LAYER_TERMINAL_LANE_REDUCTION_INCONCLUSIVE"
        ),
        "generated_by": "scripts/reduce_ordered_layer_to_terminal_lane_selector.py",
        "inputs": {
            "pic0_quotient_certificate": PIC0_QUOTIENT.name,
            "selected_monad_attempt": SELECTED_MONAD_ATTEMPT.name,
            "unconditional_selected_monad_attempt": UNCONDITIONAL_ATTEMPT.name,
            "h1_gate": H1_GATE.name,
            "pic0_quotiented_packet": rel(PIC0_PACKET),
            "hypothetical_terminal_lane_packet": rel(OUT_PACKET),
        },
        "premises": {
            "ordered_layer_pic0_closed": pic0_closed,
            "pic0_quotiented_packet_has_only_source_items_open": only_source_open,
            "terminal_lane_conditional_uniqueness_forces_L3_minus_K2": conditional_lane_forces_l3k2,
            "unconditional_source_lane_selector_still_open": unconditional_source_open,
            "h1_gate_ready_after_source_selection": h1_ready,
        },
        "validation": {
            "pic0_quotiented_layer_packet": pic0_validation,
            "terminal_lane_hypothetical_selected_packet": selected_validation,
        },
        "reduction_theorem": {
            "proved": reduction_proved,
            "statement": (
                "At the ordered Chern/H1/curvature layer, after the Pic0 quotient "
                "the only remaining local proof obligation is the source theorem "
                "that MTT selects the visible ordered L source from central-neutral "
                "terminal monad differences L_i-K2. The existing conditional "
                "uniqueness theorem then forces L3-K2=(1,-2,0), and the strict "
                "ordered-source validator passes."
            ),
        },
        "what_this_closes": {
            "ordered_layer_pic0_removed_as_local_blocker": pic0_closed,
            "ordered_layer_source_lane_selector_is_sole_local_blocker": reduction_proved,
            "hypothetical_terminal_lane_source_packet_passes_validator": selected_lane_would_pass,
            "no_new_ordered_matrix_or_pic0_search_needed_at_this_layer": reduction_proved,
        },
        "what_this_does_not_close": {
            "actual_terminal_monad_lane_selector": False,
            "typed_Cech_or_Appell_Humbert_transition_source": False,
            "h1_Ext_packet_promoted_to_selected_data": False,
            "operator_layer_Pic0_recheck": False,
            "non_split_stability_or_HYM": False,
            "same_source_D_E_Riesz_Green_dotD": False,
            "full_SM_closure": False,
        },
        "next_required_artifact": {
            "name": "Selected_Terminal_Monad_Lane_Source_Selector.v1",
            "must_prove": [
                "the selected visible ordered L source is a central-neutral terminal monad difference L_i-K2",
                "standard/equivalent lattice and base-factor order are selected by the same source",
                "the selected lane binds L3-K2 to Appell-Humbert/Cech transition data",
                "then h1=8 Ext data can be rerun as selected rather than candidate data",
            ],
        },
        "guardrails": {
            "claims_actual_terminal_lane_selector_proved": False,
            "claims_h1_Ext_selected_now": False,
            "claims_operator_layer_Pic0_closed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The ordered layer is now reduced to one local missing theorem: "
                "the terminal monad lane source selector. Pic0 is no longer a "
                "local ordered-layer blocker, but it must be rechecked when the "
                "holonomy-sensitive operator source is built."
            )
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "OrderedLayerTerminalLaneSelectorReduction",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": rel(OUT_CANDIDATE),
        "inputs": report["inputs"],
        "premises": report["premises"],
        "validation": report["validation"],
        "reduction_theorem": report["reduction_theorem"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "next_required_artifact": report["next_required_artifact"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"].endswith("LANE_SELECTOR") else 1


if __name__ == "__main__":
    raise SystemExit(main())
