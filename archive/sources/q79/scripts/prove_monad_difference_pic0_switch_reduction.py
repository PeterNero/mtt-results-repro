"""Reduce the ordered L2 source gate to two independent source switches.

This is not a source proof.  It imports the constants-repo Pic0/source switch
discipline and independently replays the four switch settings against the local
q79 ordered-source validator:

    no source, no Pic0
    Pic0 only
    source only
    source and Pic0

The point is to distinguish two open obligations that were previously bundled:
the terminal monad lane selector and the Pic0 selection/quotient rule.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CONSTANTS_REPO = TEXPAPERS / "mtt-nonsm-constants-no-knob"

CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

BASE_PACKET = CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
VALIDATOR = ROOT / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"

CONSTANTS_SWITCH_CERT = (
    CONSTANTS_REPO
    / "certificates"
    / "selected_qa_su3_m1_pic0_source_switch_table_certificate.json"
)

OUT_CANDIDATE = CANDIDATES / "monad_difference_pic0_switch_reduction.candidate.json"
OUT_CERT = CERTS / "monad_difference_pic0_switch_reduction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def git_head(repo: Path) -> str:
    if not repo.exists():
        return ""
    proc = subprocess.run(
        ["git", "log", "--oneline", "-1"],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.stdout.strip()


def apply_source_switch(packet: dict[str, Any]) -> None:
    packet["candidate_role"] = "SELECTED_DATA"
    packet["status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED"
    source = packet.setdefault("source", {})
    source["fixture_only"] = False
    source["selected_by_mtt"] = True
    source["source_certificate"] = "Selected_Monad_Difference_L2_Source_and_Pic0_Quotient.v1"
    source["source_status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED"
    evidence = packet.setdefault("selection_evidence", {})
    evidence["standard_lattice_or_equivalent_selected"] = True
    evidence["base_factor_order_selected"] = True
    evidence["base_swap_broken_by_source"] = True
    evidence["not_only_finite_mod3_qutrit"] = True
    evidence["not_equal_radius_import"] = True


def apply_pic0_switch(packet: dict[str, Any]) -> None:
    packet["pic0_resolution"] = {
        "resolution": "pic0_quotient_rule",
        "source_selected_or_quotiented": True,
        "flat_character_values_g1_to_g6": [[1, 0]] * 6,
        "rule": (
            "Flat Pic0 characters are selected or physically quotiented only "
            "after a source theorem proves they leave the ordered Chern class, "
            "h1 packet, and holonomy-sensitive observables unchanged."
        ),
    }
    source = packet.setdefault("source", {})
    if source.get("source_status") == "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED":
        source["source_status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"
        packet["status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"


def validate(packet: dict[str, Any], name: str) -> dict[str, Any]:
    tmp = CANDIDATES / f"_tmp_monad_difference_pic0_switch_{name}.json"
    write(tmp, packet)
    try:
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR), str(tmp)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    finally:
        try:
            tmp.unlink()
        except OSError:
            pass

    parsed: dict[str, Any] = {}
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_ordered_source_validation_report="):
            parsed = json.loads(line.split("=", 1)[1])
            break

    return {
        "case": name,
        "exit_code": proc.returncode,
        "validator_status": parsed.get("status"),
        "open_items": parsed.get("open_items", []),
        "failures": parsed.get("failures", []),
        "target_matrix": parsed.get("target_matrix"),
    }


def variant(base: dict[str, Any], source: bool, pic0: bool) -> dict[str, Any]:
    packet = copy.deepcopy(base)
    if source:
        apply_source_switch(packet)
    if pic0:
        apply_pic0_switch(packet)
    return packet


def analyze() -> dict[str, Any]:
    base = load(BASE_PACKET)
    constants_switch = load(CONSTANTS_SWITCH_CERT)

    cases = []
    for name, source, pic0 in [
        ("none", False, False),
        ("pic0_only", False, True),
        ("source_only", True, False),
        ("source_and_pic0", True, True),
    ]:
        result = validate(variant(base, source=source, pic0=pic0), name)
        result["source_switch"] = source
        result["pic0_switch"] = pic0
        cases.append(result)

    by_name = {case["case"]: case for case in cases}

    pic0_only_open = by_name["pic0_only"]["validator_status"] == "OPEN"
    source_only_open = by_name["source_only"]["validator_status"] == "OPEN"
    both_pass = by_name["source_and_pic0"]["exit_code"] == 0
    none_open = by_name["none"]["validator_status"] == "OPEN"

    pic0_only_items = set(by_name["pic0_only"]["open_items"])
    source_only_items = set(by_name["source_only"]["open_items"])

    source_switch_required = (
        pic0_only_open
        and "source.selected_by_mtt is not true" in pic0_only_items
        and "Pic0 resolution rule missing" not in pic0_only_items
    )
    pic0_switch_required = (
        source_only_open
        and "Pic0 resolution rule missing" in source_only_items
        and "source.selected_by_mtt is not true" not in source_only_items
    )
    constants_agrees = (
        constants_switch.get("status")
        == "QA_SU3_M1_PIC0_SOURCE_SWITCH_TABLE_BUILT_BOTH_SWITCHES_REQUIRED"
        and constants_switch.get("what_this_closes", {}).get(
            "pic0_is_independent_required_switch"
        )
        is True
        and constants_switch.get("what_this_closes", {}).get(
            "source_selection_is_independent_required_switch"
        )
        is True
    )
    reduction_proved = (
        none_open
        and source_switch_required
        and pic0_switch_required
        and both_pass
        and constants_agrees
    )

    report = {
        "calculation": "MonadDifferencePic0SwitchReduction",
        "status": (
            "MONAD_DIFFERENCE_PIC0_SWITCH_REDUCTION_PROVED_SOURCE_OPEN"
            if reduction_proved
            else "MONAD_DIFFERENCE_PIC0_SWITCH_REDUCTION_INCONCLUSIVE"
        ),
        "generated_by": "scripts/prove_monad_difference_pic0_switch_reduction.py",
        "inputs": {
            "base_packet": str(BASE_PACKET.relative_to(ROOT)),
            "local_validator": str(VALIDATOR.relative_to(ROOT)),
            "constants_switch_certificate": str(CONSTANTS_SWITCH_CERT),
            "constants_head": git_head(CONSTANTS_REPO),
            "constants_status": constants_switch.get("status"),
        },
        "switch_table": cases,
        "comparison_to_constants": {
            "constants_agrees": constants_agrees,
            "constants_honest_answer": constants_switch.get("honest_answer"),
            "constants_next_required_artifact": constants_switch.get(
                "next_required_artifact"
            ),
        },
        "what_this_closes": {
            "source_switch_is_independently_required": source_switch_required,
            "pic0_switch_is_independently_required": pic0_switch_required,
            "both_switches_suffice_for_ordered_source_validator": both_pass,
            "ordered_source_matrix_not_the_blocker": reduction_proved,
            "next_contract_split_into_two_source_obligations": reduction_proved,
        },
        "what_this_does_not_close": {
            "actual_MTT_selection_of_L3_minus_K2": False,
            "actual_Pic0_selection_or_physical_quotient": False,
            "typed_monad_Cech_transition_data": False,
            "Ext_packet_selected": False,
            "stability_or_HYM": False,
            "same_source_D_E_Riesz_Green_dotD": False,
            "full_SM_closure": False,
        },
        "next_required_artifact": {
            "name": "Selected_Monad_Difference_L2_Source_and_Pic0_Quotient.v1",
            "must_supply": [
                "source selection of terminal monad lane L3-K2",
                "Pic0 selection or physical quotient theorem",
                "binding to Appell-Humbert/Cech transition data",
                "promotion of the h1=8 Ext packet as selected data",
            ],
        },
        "guardrails": {
            "claims_source_switch_proved": False,
            "claims_pic0_switch_proved": False,
            "claims_unconditional_ordered_source": False,
            "claims_Ext_packet_selected": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The ordered L3-K2 source gate now has an exact two-switch "
                "contract. Pic0-only and source-only each fail for the other "
                "missing switch, while both together pass. The remaining work is "
                "a source theorem and a Pic0 quotient/selection theorem, not a "
                "new ordered-source matrix."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "MonadDifferencePic0SwitchReduction",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "inputs": report["inputs"],
        "switch_table": report["switch_table"],
        "comparison_to_constants": report["comparison_to_constants"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "next_required_artifact": report["next_required_artifact"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"].endswith("_PROVED_SOURCE_OPEN") else 1


if __name__ == "__main__":
    raise SystemExit(main())
