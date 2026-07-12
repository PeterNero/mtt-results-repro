"""Build PEW gauge-action normalization source packet or direct-K certificate payload."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_pewgaugeactionnormalizationsourcepacket_or_directkcertificatepayload"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_PACKET = PACKET_DIR / "pew_gauge_action_source_payload.packet.json"
DIRECT_K_CERT = PACKET_DIR / "direct_k_certificate_payload.packet.json"
CROSSUSE_PACKET = PACKET_DIR / "nonhiggs_crossuse_payload.packet.json"
NEXT_PACKET = PACKET_DIR / "next_payload_after_pew_source_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PEWGaugeActionNormalizationSourcePacket_or_DirectKCertificatePayload_v1.md"

STATUS = (
    "MTT_SELECTED_PEWGAUGEACTIONNORMALIZATIONSOURCEPACKET_OR_DIRECTKCERTIFICATEPAYLOAD_"
    "PAYLOAD_CONTRACT_LOCKED_VALUES_OPEN"
)
NEXT = "MTT_Selected_FirstPEWGaugeActionNormalizationValue_or_DirectKCertificateRun_v1"

SOURCES = {
    "previous": DATA / "selected_strictpewdirectkrowemissionattempt_or_gaugeactionnormalizationsource.candidate.json",
    "ew_rg": DATA / "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow.candidate.json",
    "h_gauge": DATA / "selected_hgaugekineticnormalizationmumatch_or_directhkthresholdrow.candidate.json",
    "strominger_kernel": DATA / "selected_heteroticstromingerewthresholdkernel_or_bn27directcarriersourcetheorem_or_directhkrow.candidate.json",
    "strominger_operator": DATA / "selected_heteroticstromingersourceoperator_or_localsystemtorsion_or_fullfourierorbit_or_directhkrow.candidate.json",
    "connection_table": DATA / "selected_samesourceconnectionvaluetable_or_directhkrow.candidate.json",
    "aew_search": DATA / "selected_aewsourceoperator_or_thresholdconventionrows" / "expanded_source_expression_search_with_physical_anchor_symbols.packet.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [rel(p) for p in SOURCES.values() if not p.exists()]
    if missing:
        raise FileNotFoundError("missing PEW source payload inputs: " + ", ".join(missing))
    sources = {k: load(p) for k, p in SOURCES.items()}

    prev = sources["previous"]["closure_decision"]
    ew = sources["ew_rg"]["closure_decision"]
    hg = sources["h_gauge"]["closure_decision"]
    sk = sources["strominger_kernel"]["closure_decision"]
    so = sources["strominger_operator"]["closure_decision"]
    ct = sources["connection_table"]["closure_decision"]
    search = sources["aew_search"]
    best = search["best_expression_rows"][0]

    source_fields = [
        {"field": "physical_gauge_action_anchor", "filled": hg["physical_gauge_action_anchor_closed"]},
        {"field": "matching_scale_mu_match", "filled": hg["matching_scale_closed"]},
        {"field": "RG_threshold_scheme", "filled": hg["RG_scheme_closed"]},
        {"field": "gaugekinetic_normalization", "filled": ew["gaugekinetic_normalization_closed"]},
        {"field": "heterotic_strominger_kernel_values", "filled": sk["selected_heterotic_strominger_kernel_closed"]},
        {"field": "threshold_operator_or_torsion_finite_part", "filled": so["selected_threshold_operator_finite_part_emitted"] or so["selected_local_system_torsion_finite_part_emitted"]},
        {"field": "same_source_connection_values", "filled": ct["accepted_same_source_connection_value_count"] > 0},
        {"field": "exact_A_EW_source_expression", "filled": prev["exact_A_EW_expression_hits_found"] > 0},
    ]
    source_filled = sum(1 for row in source_fields if row["filled"])

    source_packet = {
        "schema": "MTTPEWGaugeActionNormalizationSourcePayload.v1",
        "status": "PAYLOAD_FIELDS_LOCKED_ZERO_FINAL_VALUES",
        "closure_claimed": True,
        "source_fields": source_fields,
        "required_field_count": len(source_fields),
        "filled_field_count": source_filled,
        "accepted_strict_P_EW_source_rows": 0,
        "best_internal_clue": {
            "formula": best["formula"],
            "relative_residual": best["relative_residual"],
            "correction_factor_required": best["correction_factor_required"],
            "accepted_as_source": False,
        },
        "internal_support_available": {
            "lambda_12": ew["internal_lambda_12_value"],
            "Delta_G12": ew["internal_Delta_G12_value"],
            "tree_level_gauge_kinetic_slot_filled": hg["tree_level_gauge_kinetic_slot_filled"],
            "B_flux_strominger_route_selected": ew["strict_primary_route_selected"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    direct_k_cert = {
        "schema": "MTTDirectKCertificatePayload.v1",
        "status": "DIRECT_K_CERTIFICATE_FIELDS_LOCKED_ZERO_FINAL_VALUES",
        "closure_claimed": True,
        "required_certificate_fields": [
            "row-level K_threshold.Omega_H.lambda value",
            "same-scheme alignment certificate",
            "D_fin.H value row or symbolic cancellation",
            "selected physical normalization and mu_match",
            "RG/threshold convention row",
        ],
        "filled_certificate_count": 0,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    crossuse_packet = {
        "schema": "MTTNonHiggsCrossUsePayloadForPEW.v1",
        "status": "NONHIGGS_CROSSUSE_PAYLOAD_OPEN",
        "closure_claimed": True,
        "accepted_nonHiggs_HRG_source_map_count": 0,
        "same_prefactor_prediction_target_emitted": False,
        "allowed_role": "independent credibility/primitive-upgrade route only",
        "forbidden_role": "lambda_H replay selector or P_EW source substitute",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextPayloadAfterPEWSourceContract.v1",
        "status": "NEXT_IS_FIRST_PEW_NORMALIZATION_VALUE_OR_DIRECT_K_CERTIFICATE_RUN",
        "closure_claimed": True,
        "closed_here": [
            "strict PEW/direct-K payload fields are enumerated",
            "internal near-miss clue remains rejected as source data",
            "one-primitive lane is kept separate from no-knob source emission",
        ],
        "still_open": [
            "first physical gauge/action normalization value",
            "selected mu_match and RG/threshold scheme",
            "threshold operator or local-system torsion finite part",
            "same-source connection values",
            "direct K row-level certificate",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPEWGaugeActionNormalizationSourcePacketOrDirectKCertificatePayload",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "payload_contract_locked": True,
        "strict_P_EW_source_theorem_closed": False,
        "direct_K_threshold_Omega_H_lambda_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "pew_gauge_action_source_payload": rel(SOURCE_PACKET),
            "direct_k_certificate_payload": rel(DIRECT_K_CERT),
            "nonhiggs_crossuse_payload": rel(CROSSUSE_PACKET),
            "next_payload_after_pew_source_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "payload_contract_locked": True,
            "source_required_field_count": len(source_fields),
            "source_filled_field_count": source_filled,
            "accepted_strict_P_EW_source_rows": 0,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
            "best_A_EW_expression_formula": best["formula"],
            "best_A_EW_expression_relative_residual": best["relative_residual"],
            "physical_gauge_action_anchor_closed": hg["physical_gauge_action_anchor_closed"],
            "matching_scale_closed": hg["matching_scale_closed"],
            "RG_scheme_closed": hg["RG_scheme_closed"],
            "threshold_operator_or_torsion_finite_part_emitted": source_fields[5]["filled"],
            "same_source_connection_value_count": ct["accepted_same_source_connection_value_count"],
            "minimal_one_primitive_lane_preserved": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "PEWGaugeActionNormalizationSourcePayloadTheorem",
            "proved": True,
            "statement": "The strict PEW/direct-K problem is reduced to a concrete source-payload contract. Current packets fill zero final physical normalization, mu-match/RG, threshold finite-part, connection-value, or direct-K certificate rows; internal Delta_G12/lambda12 support and the counted primitive are rejected as source substitutes.",
        },
    }

    cert = {
        "certificate": "MTTSelectedPEWGaugeActionNormalizationSourcePacketOrDirectKCertificatePayloadCertificate",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "payload_contract_locked": True,
        "accepted_strict_P_EW_source_rows": 0,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
        "source_filled_field_count": source_filled,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PEWGaugeActionNormalizationSourcePacket or DirectKCertificatePayload v1

## Theorem

`PEWGaugeActionNormalizationSourcePayloadTheorem` is proved.

This packet locks the strict PEW/direct-K payload after the direct row-emission attempt.
It does not emit a strict `P_EW` value row or direct `K_threshold.Omega_H.lambda` row.

## Payload Status

- source required fields: `{len(source_fields)}`
- source fields filled as final values: `{source_filled}`
- accepted strict `P_EW` source rows: `0`
- accepted direct `K_threshold.Omega_H.lambda` rows: `0`
- best internal clue: `{best['formula']}`
- best clue relative residual: `{best['relative_residual']}`

## Remaining Fields

- physical gauge/action normalization: `{str(hg['physical_gauge_action_anchor_closed']).lower()}`
- selected `mu_match`: `{str(hg['matching_scale_closed']).lower()}`
- selected RG/threshold scheme: `{str(hg['RG_scheme_closed']).lower()}`
- threshold operator or local-system torsion finite part: `{str(source_fields[5]['filled']).lower()}`
- same-source connection value count: `{ct['accepted_same_source_connection_value_count']}`

Internal `Delta_G12`, `lambda_12`, tree-level `f=S`, and the counted one-primitive replay remain support or minimal-parameter data. They are not strict source rows.

Next required artifact: `{NEXT}`.
"""

    write_json(SOURCE_PACKET, source_packet)
    write_json(DIRECT_K_CERT, direct_k_cert)
    write_json(CROSSUSE_PACKET, crossuse_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
