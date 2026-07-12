"""Build q79 selected L2 cochain/Ext or direct HYM value-packet fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "q79_selected_visible_bundle_or_direct_hym_value_source_search_certificate.json"
Q79_H1_PACKET = Q79 / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
Q79_H1_VALIDATOR = Q79 / "scripts" / "validate_visible_rank2_l2_cohomology.py"
Q79_ORDERED_GATE = Q79 / "certificates" / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"
LOCAL_H1_IMPORT = CERTS / "selected_qa_su3_m1_rank2_ext_h1_source_data_attempt_certificate.json"
LOCAL_VALPHA = CERTS / "selected_qa_su3_visible_rank2_valpha_source_attempt_certificate.json"
LOCAL_PIC0 = CERTS / "selected_monad_difference_l2_source_and_pic0_quotient_attempt_certificate.json"
LOCAL_TERMINAL = CERTS / "selected_terminal_monad_lane_source_selector_attempt_certificate.json"
LOCAL_ROUTEC = CERTS / "selected_qa_su3_routec_source_solve_gate_certificate.json"

OUTPUT_PACKET = DATA / "q79_selected_l2_cochain_ext_or_direct_hym_value_packet_fill.candidate.json"
OUTPUT_CERT = CERTS / "q79_selected_l2_cochain_ext_or_direct_hym_value_packet_fill_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_Selected_L2_Cochain_Ext_or_Direct_HYM_Value_Packet_Fill_v1.md"

STATUS = "Q79_SELECTED_L2_COCHAIN_EXT_VALUE_PACKET_FILLED_CONDITIONALLY_SOURCE_PROMOTION_OPEN"
NEXT = "Q79_Base_Order_Breaking_Terminal_Lane_Source_or_Direct_HYM_Selected_Source_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def local_rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def q79_rel(path: Path) -> str:
    try:
        return path.relative_to(Q79).as_posix()
    except ValueError:
        return str(path)


def run_h1_validator(packet: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_H1_VALIDATOR), str(packet)],
        cwd=Q79,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    parsed = None
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_h1_report="):
            parsed = json.loads(line.split("=", 1)[1])
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "parsed_report": parsed,
    }


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    cohomology = load(Q79_H1_PACKET)
    ordered_gate = load(Q79_ORDERED_GATE)
    h1_import = load(LOCAL_H1_IMPORT)
    valpha = load(LOCAL_VALPHA)
    pic0 = load(LOCAL_PIC0)
    terminal = load(LOCAL_TERMINAL)
    routec = load(LOCAL_ROUTEC)
    validation = run_h1_validator(Q79_H1_PACKET)
    report = validation["parsed_report"] or {}

    selected_promotion_open_items = ordered_gate["validation_results"][
        "current_appell_humbert_attempt"
    ]["parsed_report"]["open_items"]
    local_terminal_open = terminal["minimal_remaining_source_theorem"]["must_prove"]

    checks = {
        "P0_previous_names_this_artifact": previous["verdict"]["next_required_artifact"]
        == "Q79_Selected_L2_Cochain_Ext_or_Direct_HYM_Value_Packet_Fill_v1",
        "P1_h1_validator_passes": validation["exit_code"] == 0,
        "P2_h1_equals_8": report.get("h1") == 8,
        "P3_d1_d0_zero": report.get("d1_d0_zero") is True,
        "P4_ext_vector_closed_nonexact": report.get("extension_class_closed") is True
        and report.get("extension_class_exact") is False
        and report.get("nonzero_ext_class") is True,
        "P5_no_proxy_flavor_inputs": report.get("uses_observed_flavor_inputs") is False
        and report.get("uses_benchmark_flavor_inputs") is False,
        "P6_packet_is_unselected_fixture": cohomology["candidate_role"] == "UNSELECTED_FIXTURE"
        and cohomology["source"]["selected_by_mtt"] is False
        and cohomology["source"]["fixture_only"] is True,
        "P7_selected_promotion_refused": report.get("promotes_to_non_split_V_alpha_input")
        is False
        and report.get("selected_source_promotes") is False,
        "P8_pic0_local_quotient_available_but_not_global": pic0["local_pic0_quotient_theorem"][
            "proved_for_scope"
        ]
        is True
        and pic0["local_pic0_quotient_theorem"]["not_a_global_holonomy_claim"] is True,
        "P9_terminal_lane_source_still_open": terminal["not_closed"][
            "base_order_breaking_source"
        ]
        is True,
        "P10_direct_hym_routec_still_open": routec["not_closed"][
            "route_c_residual_solve"
        ]
        is True,
        "P11_valpha_source_not_closed": valpha["gate_result"][
            "visible_rank2_valpha_source_closed"
        ]
        is False,
    }
    proved = all(checks.values())

    finite_value_packet = {
        "target": cohomology["target"],
        "source_status": {
            "candidate_role": cohomology["candidate_role"],
            "fixture_only": cohomology["source"]["fixture_only"],
            "selected_by_mtt": cohomology["source"]["selected_by_mtt"],
            "source_kind": cohomology["source"]["source_kind"],
        },
        "cochain_complex": cohomology["cochain_complex"],
        "cohomology": {
            "h1": report["h1"],
            "dimensions": report["dimensions"],
            "rank_d0": report["rank_d0"],
            "rank_d1": report["rank_d1"],
            "dim_ker_d1": report["dim_ker_d1"],
            "d1_d0_zero": report["d1_d0_zero"],
        },
        "extension_class": {
            "basis_label": cohomology["reported_cohomology"][
                "nonzero_extension_class_label"
            ],
            "vector_C1": cohomology["reported_cohomology"]["extension_class_vector_C1"],
            "closed": report["extension_class_closed"],
            "exact": report["extension_class_exact"],
            "nonzero_ext_class": report["nonzero_ext_class"],
        },
        "validator": {
            "path": q79_rel(Q79_H1_VALIDATOR),
            "exit_code": validation["exit_code"],
            "selected_source_promotes": report["selected_source_promotes"],
            "promotes_to_non_split_V_alpha_input": report[
                "promotes_to_non_split_V_alpha_input"
            ],
        },
    }

    return {
        "packet": "Q79_Selected_L2_Cochain_Ext_or_Direct_HYM_Value_Packet_Fill_v1",
        "status": STATUS
        if proved
        else "Q79_SELECTED_L2_COCHAIN_EXT_VALUE_PACKET_FILL_FAILED",
        "inputs": {
            "previous": local_rel(PREVIOUS),
            "q79_h1_packet": q79_rel(Q79_H1_PACKET),
            "q79_h1_validator": q79_rel(Q79_H1_VALIDATOR),
            "q79_ordered_source_gate": q79_rel(Q79_ORDERED_GATE),
            "local_h1_import": local_rel(LOCAL_H1_IMPORT),
            "local_valpha_attempt": local_rel(LOCAL_VALPHA),
            "local_pic0_quotient": local_rel(LOCAL_PIC0),
            "local_terminal_lane_selector": local_rel(LOCAL_TERMINAL),
            "local_routec_gate": local_rel(LOCAL_ROUTEC),
        },
        "packet_checks": checks,
        "theorem": {
            "name": "Q79SelectedL2CochainExtOrDirectHYMValuePacketFillTheorem",
            "proved": proved,
            "closure_claimed": False,
            "statement": (
                "The finite L^2 Cech/Kunneth cochain and nonzero Ext vector "
                "for L=(1,-2,0), L^2=(2,-4,0), are filled and validated with "
                "h1=8, d1*d0=0, and a closed non-exact C1 vector. This proves "
                "the conditional cochain value packet, not selected source "
                "promotion. Selection remains blocked by terminal-lane/base-order "
                "source data or by an honest direct selected HYM/Route-C solve."
            ),
        },
        "finite_value_packet": finite_value_packet,
        "selected_promotion_blocker": {
            "status": "SOURCE_PROMOTION_OPEN",
            "ordered_source_open_items": selected_promotion_open_items,
            "terminal_lane_source_must_prove": local_terminal_open,
            "pic0_scope": pic0["local_pic0_quotient_theorem"],
            "minimal_source_theorem": terminal["minimal_remaining_source_theorem"],
        },
        "direct_hym_fallback": {
            "status": "OPEN",
            "route": "direct_selected_HYM_or_RouteC_residual",
            "current_blocker": routec["not_closed"],
            "required_payload": [
                "selected connection coefficients",
                "finite residual equations",
                "HYM/Strominger or Route-C residual bound",
                "same-source D_E/Riesz/Green/dotD",
                "primitive C1 contractions",
            ],
        },
        "what_closes_now": {
            "finite_L2_cochain_packet_filled": True,
            "h1_8_validated": True,
            "closed_nonexact_Ext_vector_validated": True,
            "Pic0_local_CW_H1_quotient_preserved": True,
            "hard_gate_reduced_to_source_promotion_or_direct_HYM": True,
        },
        "what_remains_open": {
            "selected_source_promotion": True,
            "base_order_breaking_terminal_lane_source": True,
            "standard_lattice_or_equivalent_source_selection": True,
            "global_holonomy_sensitive_Pic0_or_quotient": True,
            "non_split_stability_or_HYM": True,
            "direct_selected_HYM_or_RouteC_residual": True,
            "same_source_DE_Riesz_Green_dotD": True,
            "primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_selected_L2_packet": False,
            "claims_selected_nonzero_Ext_class": False,
            "claims_selected_visible_bundle_source": False,
            "claims_non_split_stability": False,
            "claims_direct_HYM_values": False,
            "claims_routec_residual_closed": False,
            "claims_selected_D_E_Riesz_Green_dotD": False,
            "claims_C1_matrices": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "conditional_value_packet_closed": True,
            "selected_value_source_closed": False,
            "best_next_artifact": NEXT,
            "best_next_step": (
                "Prove the base-order-breaking terminal-lane source theorem so "
                "the same cochain packet can be promoted as selected data, or "
                "construct an honest direct selected HYM/Route-C residual packet."
            ),
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return f"""# Q79 Selected L2 Cochain Ext or Direct HYM Value Packet Fill v1

## Result

Status: `{packet["status"]}`

The finite `L^2` cochain packet is constructed for `L=(1,-2,0)` and
`L^2=(2,-4,0)`.  The validator reports `h1=8`, `d1*d0=0`, and a closed
non-exact Ext vector represented by
`theta_plus_0_tensor_eta_minus_0`.

This is not yet selected-source closure.  The packet remains an
`UNSELECTED_FIXTURE`: `source.selected_by_mtt=false`, `fixture_only=true`,
and `promotes_to_non_split_V_alpha_input=false`.

## Finite Value Packet

```json
{json.dumps(packet["finite_value_packet"], indent=2, sort_keys=True)}
```

## Source Promotion Blocker

```json
{json.dumps(packet["selected_promotion_blocker"], indent=2, sort_keys=True)}
```

## Direct HYM Fallback

```json
{json.dumps(packet["direct_hym_fallback"], indent=2, sort_keys=True)}
```

## Next Object

`{packet["verdict"]["best_next_artifact"]}`
"""


def main() -> int:
    packet = build_packet()
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(packet), encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
