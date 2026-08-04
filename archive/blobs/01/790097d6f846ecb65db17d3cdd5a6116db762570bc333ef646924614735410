"""Build minimal-new-source-packet fill attempt / proof-closure gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "minimal_source_packet": DATA / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_minimal_source_packet.json",
    "sourceowned_fill": DATA / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.candidate.json",
    "physical_smooth_report": DATA / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefill_report.json",
    "smooth_source_prefilter": DATA / "selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload.candidate.json",
    "smooth_operator_interface": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_or_complementquotient.candidate.json",
    "direct_response_packet": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_or_proofclosure.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_report.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_or_proofclosure_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_MinimalNewSourcePacket_Fill_or_ProofClosure_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_MINIMAL_NEW_SOURCE_PACKET_FILL_ATTEMPT_IRREDUCIBLE_SOURCE_LEAF_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceLeaf_SourceEmitsOrientedBNCarrier_or_SelectedBundleConnectionA_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def status_from_bool(value: bool | None) -> str:
    if value is True:
        return "FILLED"
    if value is False:
        return "OPEN"
    return "UNKNOWN"


def main() -> dict[str, Any]:
    minimal = load(INPUTS["minimal_source_packet"])
    sourceowned = load(INPUTS["sourceowned_fill"])
    physical_report = load(INPUTS["physical_smooth_report"])
    smooth_prefilter = load(INPUTS["smooth_source_prefilter"])
    smooth_interface = load(INPUTS["smooth_operator_interface"])
    direct_response = load(INPUTS["direct_response_packet"])

    route_a_required = minimal["route_A_direct_source_owned_positive_operator"]["required_fields"]
    route_b_required = minimal["route_B_smooth_EQa_payload"]["required_fields"]
    direct_attempt = sourceowned["attempts"]["direct_source_owned_positive_operator"]
    smooth_attempt = sourceowned["attempts"]["smooth_EQa_payload"]
    smooth_report = physical_report["filled_smooth_lane"]

    route_a_fill = {
        "source_emits_oriented_BN_carrier": {
            "filled": direct_attempt["oriented_BN_carrier_emitted"],
            "support": "oriented 27-mode B_N table exists, but source emission is not proved",
            "required_input": route_a_required["source_emits_oriented_BN_carrier"],
        },
        "source_emits_EndE_or_rhoE_to_oriented_BN_operator_functor_or_quotient": {
            "filled": direct_attempt["EndE_or_rhoE_operator_functor_or_quotient"],
            "support": "orientation functor exists; positive operator functor/quotient does not",
            "required_input": route_a_required["source_emits_EndE_or_rhoE_to_oriented_BN_operator_functor_or_quotient"],
        },
        "source_emits_positive_PhiFin_D_E_magnitude_on_oriented_BN": {
            "filled": direct_attempt["positive_PhiFin_magnitude_owned"],
            "support": "table D_E/Riesz/Green/positive spectrum materialized as support",
            "required_input": route_a_required["source_emits_positive_PhiFin_D_E_magnitude_on_oriented_BN"],
        },
        "source_certifies_Riesz_Green_positive_spectrum": {
            "filled": False,
            "support": direct_attempt["table_D_E_Riesz_Green_positive_spectrum_materialized"],
            "reason_open": "certification depends on source-owned D_E/E_Qa, not only table materialization",
            "required_input": route_a_required["source_certifies_Riesz_Green_positive_spectrum"],
        },
        "source_proves_finitepart_trace_identity_for_log92160000": {
            "filled": direct_attempt["finitepart_trace_identity"],
            "support": minimal["known_values"]["oriented_abs_sector_logdet_exact"],
            "required_input": route_a_required["source_proves_finitepart_trace_identity_for_log92160000"],
        },
    }

    route_b_fill = {
        "selected_bundle_connection_A": {
            "filled": smooth_report["selected_bundle_connection_A_or_equivalent_smooth_operator_source"]["filled"],
            "support": "geometric Bismut connection exists, but selected bundle connection A is absent",
            "required_input": route_b_required["selected_bundle_connection_A"],
        },
        "bundle_curvature_F_A": {
            "filled": smooth_report["bundle_curvature_F_A"]["filled"],
            "support": "R+ curvature exists; bundle F_A absent",
            "required_input": route_b_required["bundle_curvature_F_A"],
        },
        "representation_action_on_uE_one_forms": {
            "filled": smooth_report["representation_action_on_uE_valued_one_forms"]["filled"],
            "support": "ad-bundle representation absent",
            "required_input": route_b_required["representation_action_on_uE_one_forms"],
        },
        "trace_normalization": {
            "filled": False,
            "support": "finite eleven-label trace exists; smooth trace normalization absent",
            "required_input": route_b_required["trace_normalization"],
        },
        "kernel_and_quotient_policy_to_oriented_BN": {
            "filled": smooth_attempt["kernel_and_quotient_policy_to_oriented_BN"],
            "support": "finite internal and no-double-count policies exist; oriented smooth quotient absent",
            "required_input": route_b_required["kernel_and_quotient_policy_to_oriented_BN"],
        },
        "E_Qa_matrix_or_equivalent_zero_order_block": {
            "filled": smooth_report["smooth_E_Qa_matrix_or_equivalent_finitepart_operator"]["filled"],
            "support": "E_Qa not computed",
            "required_input": route_b_required["E_Qa_matrix_or_equivalent_zero_order_block"],
        },
        "positive_spectrum_heat_zeta_or_torsion_finitepart": {
            "filled": False,
            "support": "exact oriented finite table exists; smooth/source-certified heat-zeta-torsion finitepart absent",
            "required_input": route_b_required["positive_spectrum_heat_zeta_or_torsion_finitepart"],
        },
        "trace_lift_or_complement_quotient_proof": {
            "filled": smooth_report["trace_lift_from_finite_trace_to_smooth_heat_zeta_torsion_trace"]["filled"],
            "support": "internal complement quotient policy exists; smooth trace lift absent",
            "required_input": route_b_required["trace_lift_or_complement_quotient_proof"],
        },
    }

    route_a_closed = all(item["filled"] is True for item in route_a_fill.values())
    route_b_closed = all(item["filled"] is True for item in route_b_fill.values())

    first_irreducible_source_leaf = {
        "direct_route_leaf": "source_emits_oriented_BN_carrier",
        "smooth_route_leaf": "selected_bundle_connection_A",
        "why": (
            "Every downstream magnitude/finitepart claim requires either the source to own "
            "the oriented 27-mode carrier/operator or the source to emit a selected smooth "
            "bundle connection whose E_Qa quotient produces that carrier. Current artifacts "
            "provide support for both branches but neither first leaf."
        ),
    }

    report = {
        "schema": "SelectedHeterotic.OrientedPhiFin.MinimalNewSourcePacket.FillReport.v1",
        "status": "IRREDUCIBLE_SOURCE_LEAF_OPEN",
        "known_values": minimal["known_values"],
        "route_A_direct_fill": route_a_fill,
        "route_B_smooth_fill": route_b_fill,
        "route_A_closed": route_a_closed,
        "route_B_closed": route_b_closed,
        "source_prefilter_closed": smooth_prefilter["decision"]["support_prefilter_closed"],
        "smooth_interface_built": smooth_interface["decision"]["interface_built"],
        "direct_response_support_closed_leaves": direct_response["closed_required_leaves"],
        "first_irreducible_source_leaf": first_irreducible_source_leaf,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_PACKET.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "minimal_new_source_packet_fill_attempted": True,
        "route_A_direct_source_owned_operator_closed": route_a_closed,
        "route_B_smooth_EQa_payload_closed": route_b_closed,
        "irreducible_source_leaf_identified": True,
        "first_direct_leaf": first_irreducible_source_leaf["direct_route_leaf"],
        "first_smooth_leaf": first_irreducible_source_leaf["smooth_route_leaf"],
        "oriented_logdet_promoted": False,
        "report_path": rel(OUTPUT_PACKET),
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinMinimalNewSourcePacketFillOrProofClosure",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "sourceowned_fill": sourceowned["status"],
            "physical_smooth_report": physical_report["source_statuses"]["source_request"]["status"],
            "smooth_prefilter": smooth_prefilter["status"],
            "smooth_interface": smooth_interface["status"],
        },
        "decision": decision,
        "theorem": {
            "name": "MinimalNewSourcePacketIrreducibleLeafTheorem",
            "proved": True,
            "statement": (
                "The minimal new source packet cannot be filled from current artifacts. "
                "The direct route first needs the selected source to emit the oriented "
                "27-mode B_N carrier/operator; the smooth route first needs the selected "
                "source to emit a bundle connection A. All later requirements, including "
                "positive Phi_fin magnitude ownership, Riesz/Green certification, E_Qa, "
                "and finitepart trace identity for log(92160000), depend on one of those "
                "first source leaves. Therefore the current frontier is a genuine source "
                "amendment/proof leaf, not a numerical computation or normalization choice."
            ),
        },
        "guardrails": {
            "does_not_promote_oriented_table_by_naming": True,
            "does_not_promote_R_plus_to_bundle_A": True,
            "does_not_identify_log92160000_with_log2008": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "report_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "route_A_direct_source_owned_operator_closed": route_a_closed,
        "route_B_smooth_EQa_payload_closed": route_b_closed,
        "irreducible_source_leaf_identified": True,
        "first_direct_leaf": first_irreducible_source_leaf["direct_route_leaf"],
        "first_smooth_leaf": first_irreducible_source_leaf["smooth_route_leaf"],
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin MinimalNewSourcePacket Fill or ProofClosure v1

## Result

```text
status = {STATUS}
route_A_direct_source_owned_operator_closed = {str(route_a_closed).lower()}
route_B_smooth_EQa_payload_closed = {str(route_b_closed).lower()}
first_direct_leaf = {first_irreducible_source_leaf["direct_route_leaf"]}
first_smooth_leaf = {first_irreducible_source_leaf["smooth_route_leaf"]}
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Fill Report

```text
{rel(OUTPUT_PACKET)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
