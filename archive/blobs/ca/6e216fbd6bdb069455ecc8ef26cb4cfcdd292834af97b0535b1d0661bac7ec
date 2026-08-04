"""Build the U1/Y Route-C same-source selected-emission source certificate gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "singlet_support_promotion": DATA / "selected_u1y_routec_singlet_neutrino_rule_support_promotion_or_nogo.candidate.json",
    "same_source_fill_nogo": DATA / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo.candidate.json",
    "operator_source_bridge": DATA / "selected_u1y_routec_operator_source_identity_bridge_subpacket.candidate.json",
    "trace_equals_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "alpha1_source_strength": DATA / "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet.candidate.json",
    "sm_1m_dirac_rule": SM / "candidate_data" / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json",
    "sm_1m_dirac_rule_certificate": SM / "certificates" / "selected_sectorcharge_1m_dirac_rule_attempt_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_samesource_selected_emission_source_certificate.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_samesource_selected_emission_source_certificate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SameSource_SelectedEmission_SourceCertificate_v1.md"

STATUS = "U1Y_ROUTEC_SAMESOURCE_SELECTED_EMISSION_CERTIFICATE_ATTEMPTED_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedU10Ubar5Polarization_or_OverlapNormalization_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def field(
    *,
    required: str,
    support_present: bool,
    selected_emitted: bool,
    same_source: bool,
    theorem_derived: bool,
    provenance: str,
    evidence: list[str],
    blocker: str,
) -> dict[str, Any]:
    return {
        "required": required,
        "support_present": support_present,
        "selected_emitted": selected_emitted,
        "same_source": same_source,
        "theorem_derived": theorem_derived,
        "provenance": provenance,
        "evidence": evidence,
        "blocker": blocker,
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    singlet = load(INPUTS["singlet_support_promotion"])
    fill_nogo = load(INPUTS["same_source_fill_nogo"])
    bridge = load(INPUTS["operator_source_bridge"])
    trace = load(INPUTS["trace_equals_27mode"])
    alpha1 = load(INPUTS["alpha1_source_strength"])
    sm_1m = load(INPUTS["sm_1m_dirac_rule"])
    sm_1m_cert = load(INPUTS["sm_1m_dirac_rule_certificate"])

    structural_rule = sm_1m["structural_rule_candidate"]
    previous_fields = fill_nogo["attempted_selected_packet"]["fields"]
    support_counts = singlet["revised_counts_if_support_promoted"]

    canonical_1m_lemma = {
        "import_status": sm_1m["status"],
        "certificate_status": sm_1m_cert["status"],
        "structural_1M_Dirac_rule_candidate": sm_1m_cert["structural_1M_Dirac_rule_candidate"],
        "one_M_maps_to_Nc": structural_rule["one_M_maps_to_Nc"],
        "dirac_operator": structural_rule["dirac_operator"],
        "proposed_phase_route": structural_rule["proposed_phase_route"],
        "proposed_shift_route": structural_rule["proposed_shift_route"],
        "matches_required_route": structural_rule["matches_required_route"],
        "selected_1M_Dirac_rule_closed": sm_1m_cert["selected_1M_Dirac_rule_closed"],
        "selected_sector_charge_closed": sm_1m_cert["selected_sector_charge_closed"],
    }

    emission_fields = {
        "source_identity": field(
            required=previous_fields["source_identity"]["required"],
            support_present=True,
            selected_emitted=False,
            same_source=False,
            theorem_derived=False,
            provenance="operator_source_bridge_current_source_nogo",
            evidence=[
                bridge["status"],
                bridge["source_identity_bridge_result"]["selected_operator_source_identity_emitted"],
            ],
            blocker="selected visible/operator source certificate is still not emitted",
        ),
        "matter_slot_charge": field(
            required=previous_fields["matter_slot_charge"]["required"],
            support_present=True,
            selected_emitted=False,
            same_source=False,
            theorem_derived=False,
            provenance="structural_su5_e6_support_only",
            evidence=[
                "u,e | d,nuD structural partition retained",
                canonical_1m_lemma["dirac_operator"],
            ],
            blocker="selected U_10/U_bar5 polarization is still open",
        ),
        "singlet_neutrino_rule": field(
            required=previous_fields["singlet_neutrino_rule"]["required"],
            support_present=True,
            selected_emitted=False,
            same_source=False,
            theorem_derived=False,
            provenance="canonical_e6_su5_structural_support_only",
            evidence=[
                "1_M=N^c",
                canonical_1m_lemma["dirac_operator"],
                "nuD routes with d on the shift/non-10 side",
            ],
            blocker="selected 1_M Dirac-neutrino source emission remains open",
        ),
        "operator_values": field(
            required=previous_fields["operator_values"]["required"],
            support_present=True,
            selected_emitted=False,
            same_source=False,
            theorem_derived=False,
            provenance="DE_gap_layer_closed_dotD_C1_open",
            evidence=[
                trace["status"],
                "selected D_E gap/Riesz/Green layer closed",
                "dotD alpha1 and C1 response remain open",
            ],
            blocker="D_E support is theorem-derived only for the spectral gap layer; dotD/C1 operator values are not emitted",
        ),
        "overlap_transfer": field(
            required=previous_fields["overlap_transfer"]["required"],
            support_present=True,
            selected_emitted=False,
            same_source=False,
            theorem_derived=False,
            provenance="conditional_routing_locked_target_support_only",
            evidence=["conditional C1 routing Z->{u,e}, X->{d,nuD} is exact"],
            blocker="selected source-to-C1 overlap functor is not emitted",
        ),
        "normalization": field(
            required=previous_fields["normalization"]["required"],
            support_present=True,
            selected_emitted=False,
            same_source=False,
            theorem_derived=False,
            provenance="support_value_N_alpha1_h_ext_only",
            evidence=[
                "N_alpha1(h_ext)=1 is the unique current support value",
                alpha1["status"],
            ],
            blocker="selected trace/inner-product/Hessian normalization is not emitted",
        ),
        "primitive_contractions": field(
            required=previous_fields["primitive_contractions"]["required"],
            support_present=True,
            selected_emitted=False,
            same_source=False,
            theorem_derived=False,
            provenance="primitive_slots_support_only",
            evidence=["primitive C1/Yukawa contraction slots remain support/templates"],
            blocker="selected primitive C1 overlap contractions are not emitted",
        ),
    }

    field_counts = {
        "required": len(emission_fields),
        "support_present": sum(1 for row in emission_fields.values() if row["support_present"] is True),
        "selected_emitted": sum(1 for row in emission_fields.values() if row["selected_emitted"] is True),
        "same_source": sum(1 for row in emission_fields.values() if row["same_source"] is True),
        "theorem_derived": sum(1 for row in emission_fields.values() if row["theorem_derived"] is True),
    }

    acceptance = {
        "passes_now": field_counts["selected_emitted"] == field_counts["required"]
        and field_counts["same_source"] == field_counts["required"]
        and field_counts["theorem_derived"] == field_counts["required"],
        "must_emit_next": [
            "selected visible/operator source certificate",
            "selected U_10 clock polarization",
            "selected U_bar5 shift polarization",
            "selected 1_M -> nuD/X source emission from the same source",
            "selected source-to-C1 overlap functor",
            "selected trace/inner-product/Hessian normalization",
            "selected dotD_alpha1/C1 primitive contractions from the same branch",
        ],
        "validator_flags_required": {
            "selected_emitted": True,
            "same_source": True,
            "theorem_derived": True,
            "one_same_source": True,
            "promote_to_A_selected": True,
            "promote_to_b_selected": True,
        },
    }

    decision = {
        "support_gap_closed": support_counts["support_present"] == support_counts["required"],
        "canonical_1M_structural_lemma_imported": True,
        "same_source_selected_emission_certificate_closed": False,
        "selected_U10_Ubar5_polarization_closed": False,
        "selected_1M_Dirac_source_emitted": False,
        "selected_overlap_normalization_emitted": False,
        "N_alpha1_h_ext_promoted_to_du_dalpha1": False,
        "alpha1_driver_verified": False,
        "dotD_C1_replay_enabled": False,
        "A_selected_or_b_selected_closed": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSameSourceSelectedEmissionSourceCertificate",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "canonical_1M_lemma": canonical_1m_lemma,
        "emission_fields": emission_fields,
        "field_counts": field_counts,
        "acceptance": acceptance,
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCSameSourceSelectedEmissionCertificateAttempt",
            "proved": True,
            "statement": (
                "After importing the canonical E6/SU(5) 1_M=N^c Dirac-neutrino "
                "lemma, the seven-field U1/Y Route-C matter/overlap packet has "
                "full structural support. The current corpus still does not emit "
                "the packet as selected same-source proof data: none of the seven "
                "fields has selected_emitted=true, same_source=true, and "
                "theorem_derived=true. Thus the remaining frontier is no longer "
                "representation support but selected U_10/U_bar5 polarization, "
                "selected 1_M source emission, selected overlap transfer, and "
                "selected normalization from one source."
            ),
        },
        "what_closes_now": {
            "canonical_1M_E6_SU5_lemma_imported": True,
            "support_count_locked_at_seven_of_seven": True,
            "u_e_d_nuD_partition_canonicalized": True,
            "selected_emission_cutset_named": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_visible_operator_source_certificate": True,
            "selected_U10_clock_polarization": True,
            "selected_Ubar5_shift_polarization": True,
            "selected_1M_Dirac_source_emission": True,
            "selected_source_to_C1_overlap_functor": True,
            "selected_trace_inner_product_Hessian_normalization": True,
            "selected_dotD_alpha1_C1_primitive_contractions": True,
            "N_alpha1_h_ext_to_du_dalpha1_promotion": True,
            "lambda_12": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_same_source_packet_closed": False,
            "claims_selected_emission_closed": False,
            "claims_alpha1_driver_verified": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCSameSourceSelectedEmissionSourceCertificate",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "canonical_1M_structural_lemma_imported": True,
        "support_present": field_counts["support_present"],
        "required_fields": field_counts["required"],
        "selected_emitted": field_counts["selected_emitted"],
        "same_source": field_counts["same_source"],
        "theorem_derived": field_counts["theorem_derived"],
        "selected_emission_certificate_closed": False,
        "alpha1_driver_verified": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C SameSource SelectedEmission SourceCertificate v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"support_present = {cert['support_present']} / {cert['required_fields']}",
        f"selected_emitted = {cert['selected_emitted']} / {cert['required_fields']}",
        f"same_source = {cert['same_source']} / {cert['required_fields']}",
        f"theorem_derived = {cert['theorem_derived']} / {cert['required_fields']}",
        f"alpha1_driver_verified = {str(cert['alpha1_driver_verified']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The structural route is now canonical: `1_M=N^c` and",
        "`bar5_M 1_M 5_H -> L N^c H_u`, so the partition is `u,e | d,nuD`.",
        "This closes representation support, not selected emission.",
        "",
        "## Field Table",
        "",
        "| Field | Support | Selected | Same Source | Theorem | Blocker |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for key, row in candidate["emission_fields"].items():
        lines.append(
            f"| `{key}` | `{str(row['support_present']).lower()}` | "
            f"`{str(row['selected_emitted']).lower()}` | `{str(row['same_source']).lower()}` | "
            f"`{str(row['theorem_derived']).lower()}` | {row['blocker']} |"
        )
    lines.extend(
        [
            "",
            "## Next Emission Obligations",
            "",
        ]
    )
    for item in candidate["acceptance"]["must_emit_next"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Theorem",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Guardrails",
            "",
            "- Do not treat structural support as selected emission.",
            "- Do not promote `N_alpha1(h_ext)=1` to `du/dalpha1=h_ext` until the selected normalization emits.",
            "- Do not set `alpha1_driver_verified`, `A_selected`, `b_selected`, or `lambda_12` here.",
            "- Do not use observed or benchmark data.",
            "",
            "## Certificate",
            "",
            "```json",
            json.dumps(cert, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
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
