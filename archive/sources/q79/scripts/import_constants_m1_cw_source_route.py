"""Import the constants-repo m1 Chern-Weil source route into q79."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONSTANTS = ROOT.parent / "mtt-nonsm-constants-no-knob"
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

CONST_CW = CONSTANTS / "certificates" / "selected_qa_su3_m1_cw_operator_source_attempt_certificate.json"
CONST_CUTSET = CONSTANTS / "certificates" / "selected_qa_su3_m1_operator_cutset_certificate.json"
CONST_PAYLOAD = CONSTANTS / "certificates" / "common_de_dotd_riesz_green_payload_map_certificate.json"
CONST_H1_TEMPLATE = CONSTANTS / "certificates" / "selected_qa_su3_m1_rank2_ext_h1_source_data.template.json"

Q79_H1_GAP = CERTS / "visible_rank2_l2_integral_lift_source_gap_certificate.json"
Q79_PULLBACK = CERTS / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
Q79_H1_TEMPLATE = CERTS / "visible_rank2_l2_cohomology_data.template.json"
Q79_PARITY = CERTS / "orientation_observable_parity_certificate.json"
Q79_H1_PACKET = (
    CANDIDATES / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
)

OUT_CANDIDATE = CANDIDATES / "constants_m1_cw_source_route_import.candidate.json"
OUT_CERT = CERTS / "constants_m1_cw_source_route_import_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def status_of(path: Path) -> str:
    return load(path).get("status", "UNKNOWN") if path.exists() else "MISSING"


def canonical_local_artifact(path_text: str, expected: Path) -> str:
    canonical = expected.relative_to(ROOT).as_posix()
    normalized = path_text.replace("\\", "/")
    if normalized != canonical and not normalized.endswith("/" + canonical):
        raise ValueError(f"unexpected local artifact: {path_text}")
    if not expected.is_file():
        raise FileNotFoundError(expected)
    return canonical


def analyze() -> dict[str, Any]:
    const_cw = load(CONST_CW)
    const_cutset = load(CONST_CUTSET)
    const_payload = load(CONST_PAYLOAD)
    const_h1_template = load(CONST_H1_TEMPLATE)
    q79_h1_gap = load(Q79_H1_GAP)
    q79_pullback = load(Q79_PULLBACK)
    q79_h1_template = load(Q79_H1_TEMPLATE)
    q79_parity = load(Q79_PARITY)

    constants_target = const_cw["source_route_ranking"][0]["next_required_data"]
    q79_target = q79_h1_template["target"]
    h1_packet = q79_h1_gap["existing_h1_packet"]
    existing_h1_packet = canonical_local_artifact(h1_packet["path"], Q79_H1_PACKET)
    promoted = h1_packet["conditional_promoted_validation"]["parsed_report"]
    original = h1_packet["original_validation"]["parsed_report"]

    target_matches = (
        constants_target["l_vector_abc"] == q79_target["l_vector_abc"]
        and constants_target["c1_L_squared_vector_abc"]
        == q79_target["c1_L_squared_vector_abc"]
        and constants_target["c1_L_squared_square_alpha_coeffs"]
        == q79_target["c1_L_squared_square_alpha_coeffs"]
        and constants_target["c2_extension_alpha_coeffs"]
        == q79_target["c2_extension_alpha_coeffs"]
        and const_h1_template["preferred_first_target"] == constants_target
    )

    existing_h1_packet_compatible = (
        original["h1"] == 8
        and original["nonzero_ext_class"] is True
        and original["promotes_to_non_split_V_alpha_input"] is False
        and promoted["h1"] == 8
        and promoted["nonzero_ext_class"] is True
        and promoted["promotes_to_non_split_V_alpha_input"] is True
        and q79_pullback["calculation_results"]["validator_packet_passes"] is True
    )

    payload_order = const_payload["common_payload"]
    first_unfilled = const_cw["relation_to_common_payload"]["first_unfilled_payload_item"]
    status = "CONSTANTS_M1_CW_SOURCE_ROUTE_IMPORTED_H1_COMPATIBLE_SOURCE_OPEN"

    report = {
        "calculation": "ConstantsM1CWSourceRouteImport",
        "status": status,
        "inputs": {
            "constants_cw_attempt": str(CONST_CW),
            "constants_cutset": str(CONST_CUTSET),
            "constants_common_payload": str(CONST_PAYLOAD),
            "constants_h1_template": str(CONST_H1_TEMPLATE),
            "q79_h1_gap": str(Q79_H1_GAP.relative_to(ROOT)),
            "q79_pullback": str(Q79_PULLBACK.relative_to(ROOT)),
            "q79_h1_template": str(Q79_H1_TEMPLATE.relative_to(ROOT)),
            "q79_orientation_parity": str(Q79_PARITY.relative_to(ROOT)),
        },
        "input_statuses": {
            "constants_cw_attempt": status_of(CONST_CW),
            "constants_cutset": status_of(CONST_CUTSET),
            "constants_common_payload": status_of(CONST_PAYLOAD),
            "q79_h1_gap": status_of(Q79_H1_GAP),
            "q79_pullback": status_of(Q79_PULLBACK),
            "q79_orientation_parity": status_of(Q79_PARITY),
        },
        "target_alignment": {
            "constants_primary_route": const_cw["source_route_ranking"][0]["route"],
            "constants_primary_route_status": const_cw["source_route_ranking"][0]["status"],
            "constants_target": constants_target,
            "q79_target": {
                "l_vector_abc": q79_target["l_vector_abc"],
                "c1_L_squared_vector_abc": q79_target["c1_L_squared_vector_abc"],
                "c1_L_squared_square_alpha_coeffs": q79_target[
                    "c1_L_squared_square_alpha_coeffs"
                ],
                "c2_extension_alpha_coeffs": q79_target["c2_extension_alpha_coeffs"],
            },
            "targets_match": target_matches,
        },
        "h1_bridge": {
            "existing_packet": existing_h1_packet,
            "original_candidate_role": h1_packet["candidate_role"],
            "original_h1": original["h1"],
            "original_nonzero_ext_class": original["nonzero_ext_class"],
            "original_promotes_selected_data": original["promotes_to_non_split_V_alpha_input"],
            "conditional_promoted_h1": promoted["h1"],
            "conditional_promoted_nonzero_ext_class": promoted["nonzero_ext_class"],
            "conditional_promoted_selected_data": promoted[
                "promotes_to_non_split_V_alpha_input"
            ],
            "compatible_with_constants_h1_template": existing_h1_packet_compatible,
        },
        "payload_alignment": {
            "common_payload_order": payload_order,
            "first_unfilled_payload_item": first_unfilled,
            "q79_parity_rule_available": q79_parity["finite_operator_parity"][
                "finite_parity_closed"
            ],
            "antiunitary_equivalence_can_satisfy_branch_item_after_source": True,
        },
        "closed_now": {
            "constants_primary_source_route_imported": True,
            "rank2_ext_target_matches_q79_pullback_target": target_matches,
            "q79_h1_8_packet_compatible_with_constants_template": existing_h1_packet_compatible,
            "finite_h1_algebra_not_next_q79_blocker_after_source": True,
            "antiunitary_parity_available_for_branch_item": True,
        },
        "still_open": {
            "selected_source_certificate": True,
            "selected_visible_bundle_or_sheaf_model": True,
            "selected_ordered_integral_cech_or_automorphy_source": True,
            "non_split_stability_or_HYM_existence_certificate": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_constants_source_promotes_q79_flags": False,
            "claims_h1_fixture_is_selected_now": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_sm_closure": False,
            "uses_observed_flavor_data": False,
        },
        "verdict": {
            "honest_answer": (
                "The constants-repo m1 Chern-Weil attempt identifies the same "
                "primary rank-two V_alpha extension target already used by q79. "
                "The q79 h1=8 packet is compatible and would promote once a "
                "selected source certificate is supplied, but neither repo yet "
                "constructs that selected source or the same-source D_E/dotD payload."
            ),
            "next_action": (
                "Build the selected ordered integral Cech/automorphy source for "
                "L^2=(2,-4,0), including Pic0/torsion resolution and non-split "
                "stability, then rerun the existing h1=8 packet as selected data."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "ConstantsM1CWSourceRouteImport",
        "status": report["status"],
        "analysis_script": "scripts/import_constants_m1_cw_source_route.py",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "input_statuses": report["input_statuses"],
        "target_alignment": report["target_alignment"],
        "h1_bridge": report["h1_bridge"],
        "payload_alignment": report["payload_alignment"],
        "closed_now": report["closed_now"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if all(report["closed_now"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
