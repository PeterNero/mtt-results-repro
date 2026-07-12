"""Build the U1/Y Route-C selected U10/Ubar5 polarization or overlap-normalization gate."""

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
    "selected_emission_certificate": DATA / "selected_u1y_routec_samesource_selected_emission_source_certificate.candidate.json",
    "trace_equals_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "hym_projector_payload": DATA / "selected_u1y_routec_hym_projector_source_payload_fill.candidate.json",
    "zeromodebasis_theorem": DATA / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_theorem.candidate.json",
    "sm_1m_u10ubar5_gate": SM / "candidate_data" / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json",
    "sm_1m_u10ubar5_certificate": SM / "certificates" / "selected_1m_dirac_source_or_u10ubar5_polarization_certificate.json",
    "sm_gram_transfer": SM / "candidate_data" / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_selected_u10ubar5_polarization_or_overlap_normalization.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_selected_u10ubar5_polarization_or_overlap_normalization_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SelectedU10Ubar5Polarization_or_OverlapNormalization_v1.md"

STATUS = "U1Y_ROUTEC_U10UBAR5_POLARIZATION_OVERLAP_GATE_BUILT_SOURCE_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    emission = load(INPUTS["selected_emission_certificate"])
    trace = load(INPUTS["trace_equals_27mode"])
    hym = load(INPUTS["hym_projector_payload"])
    zmb = load(INPUTS["zeromodebasis_theorem"])
    sm_gate = load(INPUTS["sm_1m_u10ubar5_gate"])
    sm_cert = load(INPUTS["sm_1m_u10ubar5_certificate"])
    gram = load(INPUTS["sm_gram_transfer"])

    route_a_sm = sm_gate["route_A_SU5_E6_polarization"]
    route_b_sm = sm_gate["route_B_HYM_projector_zero_mode"]
    gram_packet = gram["gram_transfer_packet"]

    route_a = {
        "name": "Route_A_SU5_E6_q79_polarization",
        "support_closed": route_a_sm["support_closed"] and sm_cert["route_A_support_closed"],
        "selected_closed": route_a_sm["selected_closed"] or sm_cert["route_A_selected_closed"],
        "finite_packet": route_a_sm["finite_packet"],
        "structural_1M_rule_available": route_a_sm["structural_1M_rule_available"],
        "selected_polarization_values": sm_gate["same_branch_promotion_contract"]["must_emit"][
            "selected_polarization_values"
        ],
        "selected_sector_route": sm_gate["same_branch_promotion_contract"]["must_emit"]["selected_sector_route"],
        "promotion_blockers": [
            "same-branch selected source must emit ordered 10_M/bar5_M matter-slot packet",
            "U_10=I_3 and U_bar5=F must be source outputs, not conditional fixture values",
            "1_M=N^c Dirac rule must be selected as a same-source neutrino slot rule",
        ],
    }

    route_b = {
        "name": "Route_B_HYM_projector_zero_mode",
        "support_closed": route_b_sm["support_closed"] and sm_cert["route_B_support_closed"],
        "selected_closed": route_b_sm["selected_closed"] or sm_cert["route_B_selected_closed"],
        "functional_projector_payload_present": hym["what_closes_now"]["functional_selected_projectors"]
        and hym["what_closes_now"]["functional_selected_zero_mode_bases"]
        and hym["what_closes_now"]["functional_selected_rho_s"],
        "zeromodebasis_theorem_proved": zmb["theorem"]["proved"],
        "projector_payload_summary": route_b_sm["projector_payload_summary"],
        "promotion_blockers": [
            "selected ordered zero-mode bases K_s are not emitted for all matter slots",
            "rho_s remains a candidate/source-map theorem, not finite validator-selected values",
            "matter-slot routing cannot be inferred from universal carrier matrices",
        ],
    }

    overlap_normalization = {
        "conditional_gram_theorem_proved": gram_packet["conditional_gram_theorem_proved"],
        "gram_conditionally_forced_after_rho_s": gram_packet["gram_conditionally_forced_after_rho_s"],
        "raw_T3_frobenius_norm_per_matter_sector": gram_packet[
            "raw_T3_frobenius_norm_per_matter_sector"
        ],
        "unit_trace_transfer": gram_packet["unit_trace_transfer"],
        "selected_transfer_normalization": gram_packet["physical_transfer_normalization_selected"],
        "selected_rho_s_emitted": gram_packet["selected_rho_s_emitted"],
        "selected_zero_mode_bases_emitted": gram_packet["selected_zero_mode_bases_emitted"],
        "why_not_selected": gram_packet["why_not_selected"],
    }

    dotd_boundary = {
        "DE_gap_layer_closed": trace["decision"]["DE_gap_Riesz_Green_layer_closed"],
        "dotD_alpha1_C1_closed": trace["decision"]["dotD_alpha1_C1_closed"],
        "alpha1_driver_promotable_now": False,
        "reason": (
            "The D_E gap/Riesz/Green layer is selected, but transfer normalization "
            "still lacks selected rho_s/zero-mode bases and same-branch alpha1 tangent."
        ),
    }

    decision = {
        "route_A_support_closed": route_a["support_closed"],
        "route_A_selected_closed": route_a["selected_closed"],
        "route_B_support_closed": route_b["support_closed"],
        "route_B_selected_closed": route_b["selected_closed"],
        "conditional_overlap_normalization_fixed": overlap_normalization[
            "conditional_gram_theorem_proved"
        ]
        and overlap_normalization["gram_conditionally_forced_after_rho_s"],
        "selected_overlap_normalization_emitted": False,
        "selected_U10_Ubar5_polarization_emitted": False,
        "selected_1M_Dirac_source_emitted": False,
        "selected_sector_charge_or_chirality_closed": False,
        "N_alpha1_h_ext_promoted_to_du_dalpha1": False,
        "alpha1_driver_verified": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCSelectedU10Ubar5PolarizationOrOverlapNormalizationGate",
        "proved": True,
        "statement": (
            "The U1/Y Route-C polarization/normalization gate now imports both "
            "legal support routes. Route A supplies exact q79 finite support "
            "U_10=I_3, U_bar5=F plus the structural 1_M=N^c Dirac rule. Route B "
            "supplies functional HYM/projector and zero-mode source-map support. "
            "The overlap scalar is conditionally fixed as rho_s(T_i)/sqrt(2) once "
            "selected rho_s and selected zero-mode bases are emitted. None of these "
            "support routes currently emits selected same-branch U_10/U_bar5/1_M "
            "source values or selected overlap normalization, so alpha1 transfer "
            "and lambda_12 remain open."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSelectedU10Ubar5PolarizationOrOverlapNormalization",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": emission["status"],
        "route_A_SU5_E6_polarization": route_a,
        "route_B_HYM_projector_zero_mode": route_b,
        "overlap_normalization": overlap_normalization,
        "dotd_boundary": dotd_boundary,
        "decision": decision,
        "theorem": theorem,
        "same_branch_emission_contract": {
            "must_emit": {
                "selected_source_identity": True,
                "selected_ordered_matter_slot_packet": ["10_M_clock", "bar5_M_shift", "1_M_Dirac_shift"],
                "selected_polarization_values": {"U_10": "I_3", "U_bar5": "F"},
                "selected_sector_route": {"phase": ["u", "e"], "shift": ["d", "nuD"]},
                "selected_rho_s_and_zero_mode_bases": True,
                "selected_overlap_transfer_normalization": True,
                "honest_dotD_alpha1_replay": True,
            },
            "forbidden": sm_gate["same_branch_promotion_contract"]["forbidden_inputs"],
        },
        "what_closes_now": {
            "route_A_q79_finite_polarization_support_imported": True,
            "route_B_HYM_projector_support_imported": True,
            "conditional_Gram_transfer_scalar_fixed_after_rho_s": True,
            "overlap_normalization_reduced_to_selected_rho_s_and_zero_modes": True,
            "same_branch_emission_contract_sharpened": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_source_identity": True,
            "selected_U10_clock_source": True,
            "selected_Ubar5_shift_source": True,
            "selected_1M_Dirac_shift_source": True,
            "selected_rho_s_source_map": True,
            "selected_zero_mode_bases_K_s": True,
            "selected_overlap_transfer_normalization": True,
            "honest_dotD_alpha1_replay": True,
            "lambda_12": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_selected_U10_Ubar5": False,
            "claims_selected_overlap_normalization": False,
            "claims_alpha1_driver_verified": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCSelectedU10Ubar5PolarizationOrOverlapNormalization",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "route_A_support_closed": decision["route_A_support_closed"],
        "route_A_selected_closed": decision["route_A_selected_closed"],
        "route_B_support_closed": decision["route_B_support_closed"],
        "route_B_selected_closed": decision["route_B_selected_closed"],
        "conditional_overlap_normalization_fixed": decision["conditional_overlap_normalization_fixed"],
        "selected_overlap_normalization_emitted": False,
        "selected_U10_Ubar5_polarization_emitted": False,
        "alpha1_driver_verified": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C SelectedU10Ubar5Polarization or OverlapNormalization v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"route_A_support_closed = {str(cert['route_A_support_closed']).lower()}",
        f"route_A_selected_closed = {str(cert['route_A_selected_closed']).lower()}",
        f"route_B_support_closed = {str(cert['route_B_support_closed']).lower()}",
        f"route_B_selected_closed = {str(cert['route_B_selected_closed']).lower()}",
        f"conditional_overlap_normalization_fixed = {str(cert['conditional_overlap_normalization_fixed']).lower()}",
        f"selected_overlap_normalization_emitted = {str(cert['selected_overlap_normalization_emitted']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "Two support routes now agree on the same target. Route A gives the finite",
        "`U_10=I_3`, `U_bar5=F` q79 packet plus the `1_M=N^c` Dirac rule. Route B",
        "gives HYM/projector zero-mode support. The overlap scalar is fixed",
        "conditionally after selected `rho_s` and selected zero-mode bases, but it",
        "is not emitted as selected normalization yet.",
        "",
        "## Route A",
        "",
        "```text",
        f"U_10 = {candidate['route_A_SU5_E6_polarization']['finite_packet']['U_10']}",
        f"U_bar5 = {candidate['route_A_SU5_E6_polarization']['finite_packet']['U_bar5']}",
        f"selected route = {candidate['route_A_SU5_E6_polarization']['selected_sector_route']}",
        "```",
        "",
        "## Overlap Normalization",
        "",
        "```text",
        f"unit trace transfer = {candidate['overlap_normalization']['unit_trace_transfer']}",
        f"raw T3 Frobenius norm = {candidate['overlap_normalization']['raw_T3_frobenius_norm_per_matter_sector']}",
        "```",
        "",
        "## Same-Branch Emission Contract",
        "",
    ]
    for key, value in candidate["same_branch_emission_contract"]["must_emit"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Theorem",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Guardrails",
            "",
            "- Do not treat `U_10=I_3`, `U_bar5=F` finite support as selected source emission.",
            "- Do not promote conditional Gram normalization until selected `rho_s` and zero-mode bases emit.",
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
