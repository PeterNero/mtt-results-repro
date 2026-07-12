"""Prove the layer-restricted Pic0 quotient rule for the ordered L2 gate.

The earlier two-switch reduction showed that source selection and Pic0 are
independent switches for the ordered L3-K2 packet.  This script closes the Pic0
switch only at the ordered Chern/H1/curvature layer.

It deliberately does not claim a full physical Pic0 quotient for the later
holonomy-sensitive operator layer.  Same-source D_E/Riesz/Green/dotD data must
recheck Pic0.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

BASE_PACKET = CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
OUT_PACKET = CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_pic0_quotiented_layer.json"
OUT_CANDIDATE = CANDIDATES / "ordered_layer_pic0_quotient.candidate.json"
OUT_CERT = CERTS / "ordered_layer_pic0_quotient_certificate.json"

VALIDATOR = ROOT / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"

SELECTOR_OBSTRUCTION = CERTS / "visible_rank2_l2_selector_obstruction_certificate.json"
PROMOTION_GATE = CERTS / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"
SWITCH_REDUCTION = CERTS / "monad_difference_pic0_switch_reduction_certificate.json"

GAUGE_FIXING_SOURCE = (
    OBSIDIAN
    / "5 Dirac Delta"
    / "Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md"
)
FINITE_PROJECTION_SOURCE = (
    OBSIDIAN
    / "5 Dirac Delta"
    / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
)
ADMISSIBILITY_FILTER_SOURCE = (
    OBSIDIAN
    / "5 Dirac Delta"
    / "Path_Integral_Constraints_as_Finite_Admissibility_Filters.md"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


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
        "stdout_head": proc.stdout.splitlines()[:8],
    }


def pic0_quotient_layer_packet(base: dict[str, Any]) -> dict[str, Any]:
    packet = copy.deepcopy(base)
    packet["pic0_resolution"] = {
        "resolution": "pic0_quotient_rule",
        "source_selected_or_quotiented": True,
        "flat_character_values_g1_to_g6": [[1, 0]] * 6,
        "scope": "ordered_chern_h1_curvature_layer_only",
        "rule": (
            "Flat Pic0 characters are quotient-equivalent for the ordered "
            "Chern/H1/ordinary-curvature layer because c1, c2, h1, the "
            "Appell-Humbert curvature matrix, and the visible GS/Bianchi row "
            "are invariant under flat Pic0 twists. Holonomy-sensitive operator "
            "data must reopen this quotient."
        ),
    }
    return packet


def source_contains(path: Path, needles: list[str]) -> bool:
    text = " ".join(read(path).lower().split())
    return all(" ".join(needle.lower().split()) in text for needle in needles)


def analyze() -> dict[str, Any]:
    selector = load(SELECTOR_OBSTRUCTION)
    promotion = load(PROMOTION_GATE)
    switch = load(SWITCH_REDUCTION)
    base = load(BASE_PACKET)

    packet = pic0_quotient_layer_packet(base)
    write(OUT_PACKET, packet)
    validation = validate(OUT_PACKET)

    open_items = set(validation["open_items"])
    pic0_items_absent = not any("Pic0" in item for item in open_items)
    only_source_items_remain = validation["exit_code"] == 2 and pic0_items_absent and all(
        item in {
            "packet is marked fixture_only",
            "source.selected_by_mtt is not true",
            "source status is not a selected ordered-source status",
            "selection evidence missing: standard_lattice_or_equivalent_selected",
            "selection evidence missing: base_factor_order_selected",
        }
        for item in open_items
    )

    pic0_invariance = selector.get("pic0_invariance", {})
    invariance_closed = (
        pic0_invariance.get("flat_pic0_changes_c1") is False
        and pic0_invariance.get("flat_pic0_changes_c2") is False
        and pic0_invariance.get("flat_pic0_changes_h1_for_nonzero_elliptic_degrees")
        is False
        and pic0_invariance.get("flat_pic0_changes_appell_humbert_curvature_matrix")
        is False
        and pic0_invariance.get("needs_holonomy_sensitive_source_or_gauge_fixing")
        is True
    )
    gate_accepts_quotient_rule = (
        "pic0_quotient_rule"
        in promotion.get("promotion_contract", {}).get("must_resolve_pic0", [])
    )
    switch_supports_independence = (
        switch.get("what_this_closes", {}).get("pic0_switch_is_independently_required")
        is True
        and switch.get("what_this_closes", {}).get(
            "both_switches_suffice_for_ordered_source_validator"
        )
        is True
    )
    quotient_sources_ok = (
        source_contains(
            GAUGE_FIXING_SOURCE,
            ["physical configuration space is the quotient", "Gauge freedom"],
        )
        and source_contains(
            FINITE_PROJECTION_SOURCE,
            ["projected to the physical quotient", "must not create"],
        )
        and source_contains(
            ADMISSIBILITY_FILTER_SOURCE,
            ["same physical quotient", "admissible projection weight"],
        )
    )

    quotient_proved = (
        invariance_closed
        and gate_accepts_quotient_rule
        and switch_supports_independence
        and quotient_sources_ok
        and only_source_items_remain
    )

    report = {
        "calculation": "OrderedLayerPic0Quotient",
        "status": (
            "ORDERED_LAYER_PIC0_QUOTIENT_PROVED_OPERATOR_LAYER_REOPENS"
            if quotient_proved
            else "ORDERED_LAYER_PIC0_QUOTIENT_INCONCLUSIVE"
        ),
        "generated_by": "scripts/prove_ordered_layer_pic0_quotient.py",
        "inputs": {
            "base_packet": rel(BASE_PACKET),
            "quotiented_layer_packet": rel(OUT_PACKET),
            "validator": rel(VALIDATOR),
            "selector_obstruction": SELECTOR_OBSTRUCTION.name,
            "ordered_source_promotion_gate": PROMOTION_GATE.name,
            "pic0_switch_reduction": SWITCH_REDUCTION.name,
            "gauge_fixing_source": str(GAUGE_FIXING_SOURCE),
            "finite_projection_source": str(FINITE_PROJECTION_SOURCE),
            "admissibility_filter_source": str(ADMISSIBILITY_FILTER_SOURCE),
        },
        "source_checks": {
            "mtt_physical_quotient_sources_present": quotient_sources_ok,
            "selector_pic0_invariance_closed": invariance_closed,
            "ordered_source_gate_accepts_pic0_quotient_rule": gate_accepts_quotient_rule,
            "switch_reduction_independence_closed": switch_supports_independence,
        },
        "quotient_theorem": {
            "proved_for_ordered_layer": quotient_proved,
            "scope": "ordered Chern/H1/ordinary-curvature layer only",
            "statement": (
                "Within the ordered L3-K2 source layer, flat Pic0 twists are "
                "physically quotient-equivalent because every observable admitted "
                "at that layer is Pic0-invariant: c1, c2, h1, ordinary "
                "Appell-Humbert curvature, and the visible GS/Bianchi row. This "
                "implements the MTT physical-quotient discipline only at that "
                "layer."
            ),
            "reopen_condition": (
                "Any holonomy-sensitive selected operator packet, including "
                "same-source D_E/Riesz/Green/dotD, must recheck Pic0 rather than "
                "inherit this quotient automatically."
            ),
        },
        "validation": {
            "pic0_quotiented_layer_packet": validation,
            "pic0_items_absent_after_quotient": pic0_items_absent,
            "only_source_selection_items_remain": only_source_items_remain,
        },
        "what_this_closes": {
            "pic0_quotient_for_ordered_chern_h1_curvature_layer": quotient_proved,
            "pic0_switch_removed_from_ordered_layer_validator": only_source_items_remain,
            "pic0_not_a_free_knob_at_this_layer": quotient_proved,
        },
        "what_this_does_not_close": {
            "terminal_monad_lane_source_selector": False,
            "full_physical_pic0_quotient_for_operator_layer": False,
            "same_source_D_E_Riesz_Green_dotD_pic0_blindness": False,
            "Ext_packet_selected": False,
            "stability_or_HYM": False,
            "full_SM_closure": False,
        },
        "next_required_artifact": {
            "name": "Selected_Monad_Difference_L2_Source_Lane_Selector.v1",
            "must_supply": [
                "source selection of terminal monad lane L3-K2",
                "binding of L3-K2 to Appell-Humbert/Cech transition data",
                "promotion of h1=8 Ext packet as selected data",
                "operator-layer Pic0 recheck when D_E/Riesz/Green/dotD are supplied",
            ],
        },
        "guardrails": {
            "claims_terminal_lane_selected": False,
            "claims_full_pic0_quotient_for_operator_layer": False,
            "claims_same_source_operator_pic0_blindness": False,
            "claims_Ext_packet_selected": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "Pic0 is closed only for the ordered Chern/H1/curvature layer. "
                "The ordered-source validator no longer needs Pic0 after this "
                "quotient, but the actual source-lane selector and any "
                "holonomy-sensitive operator Pic0 check remain open."
            )
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    certificate = {
        "certificate": "OrderedLayerPic0Quotient",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": rel(OUT_CANDIDATE),
        "inputs": report["inputs"],
        "source_checks": report["source_checks"],
        "quotient_theorem": report["quotient_theorem"],
        "validation": report["validation"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "next_required_artifact": report["next_required_artifact"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"].endswith("_REOPENS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
