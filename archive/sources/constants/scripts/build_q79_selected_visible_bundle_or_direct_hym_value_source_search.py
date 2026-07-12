"""Build q79 selected visible bundle or direct HYM value-source search."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "q79_typed_monad_cech_or_hym_connection_witness_value_fill_attempt_certificate.json"
Q79_VISIBLE_TARGET = (
    Q79
    / "certificates"
    / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions_certificate.json"
)
Q79_AH_REDUCTION = Q79 / "certificates" / "q79_ah_source_selection_or_routec_residual_reduction_certificate.json"
Q79_CANDIDATES = Q79 / "certificates" / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json"
LOCAL_ARCH = CERTS / "selected_qa_su3_visible_source_architecture_certificate.json"
LOCAL_ROUTEC = CERTS / "selected_qa_su3_routec_source_solve_gate_certificate.json"
LOCAL_OPERATOR = CERTS / "selected_qa_su3_visible_operator_source_packet_attempt_certificate.json"

OUTPUT_PACKET = DATA / "q79_selected_visible_bundle_or_direct_hym_value_source_search.candidate.json"
OUTPUT_CERT = CERTS / "q79_selected_visible_bundle_or_direct_hym_value_source_search_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_Selected_Visible_Bundle_or_Direct_HYM_Value_Source_Search_v1.md"

STATUS = "Q79_SELECTED_VISIBLE_BUNDLE_OR_DIRECT_HYM_VALUE_SOURCE_SEARCH_BUILT_PRIMARY_VALPHA_ROUTE_OPEN"
NEXT = "Q79_Selected_L2_Cochain_Ext_or_Direct_HYM_Value_Packet_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def q79_rel(path: Path) -> str:
    try:
        return path.relative_to(Q79).as_posix()
    except ValueError:
        return str(path)


def local_rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def candidate_by_id(candidates: dict[str, Any], candidate_id: str) -> dict[str, Any]:
    for item in candidates["candidate_ranking"]:
        if item["id"] == candidate_id:
            return item
    raise KeyError(candidate_id)


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    visible = load(Q79_VISIBLE_TARGET)
    ah = load(Q79_AH_REDUCTION)
    candidates = load(Q79_CANDIDATES)
    arch = load(LOCAL_ARCH)
    routec = load(LOCAL_ROUTEC)
    operator = load(LOCAL_OPERATOR)

    primary = candidate_by_id(candidates, "rank2_non_split_extension_preferred_L_1_-2_0")
    direct = candidate_by_id(candidates, "direct_route_c_finite_hym_strominger_solve")
    twisted = candidate_by_id(candidates, "twisted_s3_or_gerbe_source_transfer")
    abelian = candidate_by_id(candidates, "abelian_two_line_flux_row")

    checks = {
        "S0_previous_requests_source_search": previous["verdict"]["honest_next_step"]
        == "Q79_Selected_Visible_Bundle_or_Direct_HYM_Value_Source_Search_v1",
        "S1_q79_visible_target_says_operator_source_first_blocker": visible[
            "selected_missing_data_scan"
        ]["first_blocking_layer"]
        == "selected_operator_source",
        "S2_primary_valpha_candidate_identified": candidates["best_current_route"][
            "candidate_id"
        ]
        == "rank2_non_split_extension_preferred_L_1_-2_0"
        and primary["promotion_status"] == "OPEN",
        "S3_abelian_shortcut_rejected": abelian["promotion_status"]
        == "REJECTED_AS_FINAL_SOURCE",
        "S4_routec_preserved_as_fallback": direct["promotion_status"] == "OPEN"
        and candidates["calculation_results"]["route_c_kept_as_parallel_fallback"] is True,
        "S5_ah_goodcover_reduced_to_single_source_class": ah[
            "source_selection_or_residual_summary"
        ]["AH_to_goodcover_representative_equivalence_proved"]
        is True
        and ah["source_selection_or_residual_summary"][
            "selected_routec_residual_available"
        ]
        is False,
        "S6_architecture_recommends_A_plus_B_then_C": arch["recommended_construction"][
            "primary"
        ]
        == "A_rank2_valpha_terminal_monad_primary"
        and arch["recommended_construction"]["required_merge"]
        == "B_s3_green_schwarz_visible_support"
        and arch["recommended_construction"]["execution_engine"]
        == "C_direct_hym_routec_solve",
        "S7_local_routec_gate_open_not_closed": routec["not_closed"][
            "route_c_residual_solve"
        ]
        is True
        and routec["guardrails"]["claims_selected_visible_operator_source_constructed"]
        is False,
        "S8_operator_packet_attempt_open": operator["gate_result"][
            "visible_operator_source_packet_closed"
        ]
        is False,
    }
    proved = all(checks.values())

    search_results = {
        "primary_route": {
            "id": primary["id"],
            "kind": primary["candidate_kind"],
            "source_shape": primary["source_shape"],
            "why_primary": primary["why_primary"],
            "topological_target": primary["topological_target"],
            "closed_support": primary["already_audited_support"],
            "open_fields": {
                key: value
                for key, value in primary["source_packet_fields"].items()
                if value.get("status") == "OPEN"
            },
        },
        "direct_hym_routec_fallback": {
            "id": direct["id"],
            "kind": direct["candidate_kind"],
            "source_shape": direct["source_shape"],
            "why_not_primary": direct["why_not_primary"],
            "open_fields": direct["source_packet_fields"],
        },
        "twisted_s3_support": {
            "id": twisted["id"],
            "kind": twisted["candidate_kind"],
            "source_shape": twisted["source_shape"],
            "why_not_primary": twisted["why_not_primary"],
            "open_fields": twisted["source_packet_fields"],
        },
        "retired_as_final_source": {
            "id": abelian["id"],
            "kind": abelian["candidate_kind"],
            "role": abelian["live_role"],
            "why_retained": abelian["why_retained"],
        },
    }

    return {
        "packet": "Q79_Selected_Visible_Bundle_or_Direct_HYM_Value_Source_Search_v1",
        "status": STATUS
        if proved
        else "Q79_SELECTED_VISIBLE_BUNDLE_OR_DIRECT_HYM_VALUE_SOURCE_SEARCH_FAILED",
        "inputs": {
            "previous": local_rel(PREVIOUS),
            "q79_visible_operator_target": q79_rel(Q79_VISIBLE_TARGET),
            "q79_ah_source_reduction": q79_rel(Q79_AH_REDUCTION),
            "q79_valpha_source_candidates": q79_rel(Q79_CANDIDATES),
            "local_visible_source_architecture": local_rel(LOCAL_ARCH),
            "local_routec_source_gate": local_rel(LOCAL_ROUTEC),
            "local_visible_operator_packet_attempt": local_rel(LOCAL_OPERATOR),
        },
        "search_checks": checks,
        "theorem": {
            "name": "Q79SelectedVisibleBundleOrDirectHYMValueSourceSearchTheorem",
            "proved": proved,
            "closure_claimed": False,
            "statement": (
                "The source search narrows the selected value-source problem to "
                "a ranked hierarchy. The primary route is the non-split rank-two "
                "V_alpha extension with L=(1,-2,0), merged with selected S3/GS "
                "support and executed by direct HYM/Route-C only after the source "
                "is selected. Direct Route C remains a fallback; the split "
                "abelian row is retained only as Chern/Bianchi support."
            ),
        },
        "search_results": search_results,
        "source_packet_interface": candidates["source_packet_interface"],
        "value_fill_target": {
            "name": NEXT,
            "primary_payload": [
                "fill selected L^2 cochain packet for L=(1,-2,0)",
                "validate h1>0 and closed non-exact Ext vector",
                "prove non-split extension and stability in selected chamber",
                "bind AH/Cech representative to the selected source class",
                "merge selected S3/Green-Schwarz support by same-source proof or physical quotient",
                "emit HYM/Route-C residual and finite D_E/Riesz/Green/dotD packets",
            ],
            "direct_hym_fallback_payload": [
                "construct selected finite HYM/Strominger residual packet with c1=0,c2=+4 alpha_1",
                "derive Chern/Bianchi row from that packet",
                "run honest selected-source validators without lifted flags",
            ],
        },
        "what_closes_now": {
            "selected_visible_source_search_executed": True,
            "primary_valpha_route_identified": True,
            "direct_routec_hym_fallback_preserved": True,
            "abelian_split_shortcut_retired_as_final_source": True,
            "next_value_fill_payload_minimized": True,
        },
        "what_remains_open": {
            "selected_L2_cochain_packet": True,
            "nonzero_closed_nonexact_Ext_vector": True,
            "non_split_stability": True,
            "selected_AH_or_Cech_source_binding": True,
            "selected_Gauduchon_or_balanced_chamber": True,
            "same_source_S3_GS_binding": True,
            "HYM_or_RouteC_residual_certificate": True,
            "same_source_DE_Riesz_Green_dotD": True,
            "primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_selected_visible_bundle_source": False,
            "claims_direct_HYM_values": False,
            "claims_routec_residual_closed": False,
            "claims_selected_D_E_constructed": False,
            "claims_C1_matrices": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "source_search_closed": True,
            "value_source_closed": False,
            "next_required_artifact": NEXT,
            "best_next_step": candidates["verdict"]["next_action"],
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return f"""# Q79 Selected Visible Bundle or Direct HYM Value Source Search v1

## Result

Status: `{packet["status"]}`

The search does not close a selected visible source, but it removes ambiguity.
The primary route is the non-split rank-two `V_alpha` extension with
`L=(1,-2,0)`.  The selected S3/Green-Schwarz support must be merged by a
same-source proof or physical quotient, and direct HYM/Route C remains the
execution engine once the source is selected.

## Search Checks

```json
{json.dumps(packet["search_checks"], indent=2, sort_keys=True)}
```

## Search Results

```json
{json.dumps(packet["search_results"], indent=2, sort_keys=True)}
```

## Value Fill Target

```json
{json.dumps(packet["value_fill_target"], indent=2, sort_keys=True)}
```

## Remaining Open

```json
{json.dumps(packet["what_remains_open"], indent=2, sort_keys=True)}
```
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
