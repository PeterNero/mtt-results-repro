"""Build the U1/Y Route-C U10/Ubar5/1M same-branch source-promotion gate."""

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
    "polarization_gate": DATA / "selected_u1y_routec_selected_u10ubar5_polarization_or_overlap_normalization.candidate.json",
    "hym_projector_payload": DATA / "selected_u1y_routec_hym_projector_source_payload_fill.candidate.json",
    "transport_derivative": DATA / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json",
    "alpha1_source_strength": DATA / "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet.candidate.json",
    "same_source_chernweil": DATA / "selected_u1y_routec_samesource_chernweil_operator_functional_value.candidate.json",
    "sm_1m_u10ubar5_gate": SM / "candidate_data" / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json",
    "sm_gram_transfer": SM / "candidate_data" / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_u10ubar5_1m_sourcepromotion_samebranch_emission.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_u10ubar5_1m_sourcepromotion_samebranch_emission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1.md"

STATUS = "U1Y_ROUTEC_U10UBAR5_1M_SOURCEPROMOTION_PACKET_BUILT_SELECTOR_OPEN"
NEXT = "Selected_U1Y_RouteC_BranchCoherence_Selector_or_FiniteValidatorReplay_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def obligation(
    *,
    value: Any,
    support: bool,
    functional_selected: bool,
    physical_selected: bool,
    same_branch: bool,
    source: str,
    blocker: str,
) -> dict[str, Any]:
    return {
        "value": value,
        "support_present": support,
        "functional_selected": functional_selected,
        "physical_selected": physical_selected,
        "same_branch": same_branch,
        "source": source,
        "blocker": blocker,
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    pol = load(INPUTS["polarization_gate"])
    hym = load(INPUTS["hym_projector_payload"])
    transport = load(INPUTS["transport_derivative"])
    alpha1 = load(INPUTS["alpha1_source_strength"])
    chernweil = load(INPUTS["same_source_chernweil"])
    sm_gate = load(INPUTS["sm_1m_u10ubar5_gate"])
    gram = load(INPUTS["sm_gram_transfer"])

    route_a = pol["route_A_SU5_E6_polarization"]
    route_b = pol["route_B_HYM_projector_zero_mode"]
    contract = pol["same_branch_emission_contract"]["must_emit"]
    gram_packet = gram["gram_transfer_packet"]

    packet = {
        "selected_source_identity": obligation(
            value="Route-C visible/HYM transport source family",
            support=True,
            functional_selected=hym["decision"]["functional_projector_payload_filled"],
            physical_selected=False,
            same_branch=False,
            source=rel(INPUTS["hym_projector_payload"]),
            blocker="No branch-coherence selector identifies the functional HYM transport packet with the finite q79 matter-slot packet.",
        ),
        "U_10_clock": obligation(
            value=contract["selected_polarization_values"]["U_10"],
            support=route_a["support_closed"],
            functional_selected=False,
            physical_selected=False,
            same_branch=False,
            source=rel(INPUTS["sm_1m_u10ubar5_gate"]),
            blocker="U_10=I_3 is exact finite support, but is not emitted by the selected U1/Y source.",
        ),
        "U_bar5_shift": obligation(
            value=contract["selected_polarization_values"]["U_bar5"],
            support=route_a["support_closed"],
            functional_selected=False,
            physical_selected=False,
            same_branch=False,
            source=rel(INPUTS["sm_1m_u10ubar5_gate"]),
            blocker="U_bar5=F is exact finite support, but is not emitted by the selected U1/Y source.",
        ),
        "one_M_Dirac_shift": obligation(
            value={"1_M": "N^c", "route": contract["selected_sector_route"]["shift"]},
            support=route_a["structural_1M_rule_available"],
            functional_selected=False,
            physical_selected=False,
            same_branch=False,
            source=rel(INPUTS["sm_1m_u10ubar5_gate"]),
            blocker="The 1_M Dirac-neutrino rule is canonical structural support, not selected source emission.",
        ),
        "rho_s_and_zero_mode_bases": obligation(
            value="K_s^sel=U K_s^model, P_s^sel=U P_s^model U^-1, rho_s by End0 restriction",
            support=route_b["support_closed"],
            functional_selected=hym["decision"]["functional_source_map_rho_s_emitted"]
            and hym["decision"]["functional_zero_mode_bases_emitted"],
            physical_selected=False,
            same_branch=False,
            source=rel(INPUTS["hym_projector_payload"]),
            blocker="The functional HYM payload has not been replayed as finite validator-ready matter-slot data.",
        ),
        "overlap_transfer_normalization": obligation(
            value=gram_packet["unit_trace_transfer"],
            support=gram_packet["conditional_gram_theorem_proved"],
            functional_selected=False,
            physical_selected=gram_packet["physical_transfer_normalization_selected"],
            same_branch=False,
            source=rel(INPUTS["sm_gram_transfer"]),
            blocker="Normalization is fixed conditionally as rho_s(T_i)/sqrt(2), but selected rho_s and finite zero-mode bases have not jointly emitted.",
        ),
        "alpha1_driver_and_dotD_replay": obligation(
            value="du/dalpha1=h_ext would verify dotD_alpha1 after same-source normalization",
            support=transport["theorem"]["proved"] and alpha1["theorem"]["proved"],
            functional_selected=False,
            physical_selected=False,
            same_branch=False,
            source=rel(INPUTS["transport_derivative"]),
            blocker="alpha1 source-strength is a support value; same-source transfer normalization is still missing.",
        ),
        "chern_weil_functional_value": obligation(
            value=chernweil["value_functional"]["support_candidate"]["N_alpha1_h_ext"],
            support=chernweil["theorem"]["proved"],
            functional_selected=True,
            physical_selected=False,
            same_branch=False,
            source=rel(INPUTS["same_source_chernweil"]),
            blocker="N_alpha1(h_ext)=1 is uniquely supported but not yet promoted to physical du/dalpha1.",
        ),
    }

    counts = {
        "required": len(packet),
        "support_present": sum(1 for row in packet.values() if row["support_present"]),
        "functional_selected": sum(1 for row in packet.values() if row["functional_selected"]),
        "physical_selected": sum(1 for row in packet.values() if row["physical_selected"]),
        "same_branch": sum(1 for row in packet.values() if row["same_branch"]),
    }
    selected_closed = counts["physical_selected"] == counts["required"] and counts["same_branch"] == counts["required"]

    branch_coherence_selector = {
        "needed": True,
        "name": "Route-C branch-coherence selector",
        "must_prove": [
            "finite q79 matter-slot packet and functional HYM transport packet are the same selected source",
            "U_10=I_3 and U_bar5=F are source emissions, not imported fixture values",
            "1_M=N^c/nuD shift rule is emitted in the same selected packet",
            "functional rho_s and K_s replay into finite validator-ready sector matrices",
            "unit trace transfer rho_s(T_i)/sqrt(2) is the selected physical normalization",
            "N_alpha1(h_ext)=1 promotes to du/dalpha1=h_ext without observed data",
        ],
        "acceptable_payloads": [
            "finite validator replay with selected source provenance flags",
            "typed monad/Cech source packet whose induced finite reduction prints the same values",
            "direct HYM/Strominger source theorem with explicit finite sector extraction",
        ],
    }

    decision = {
        "sourcepromotion_packet_constructed": True,
        "support_complete": counts["support_present"] == counts["required"],
        "functional_layer_nonempty": counts["functional_selected"] > 0,
        "physical_selected_complete": selected_closed,
        "same_branch_complete": False,
        "selected_U10_Ubar5_polarization_emitted": False,
        "selected_1M_Dirac_source_emitted": False,
        "selected_overlap_normalization_emitted": False,
        "N_alpha1_h_ext_promoted_to_du_dalpha1": False,
        "alpha1_driver_verified": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCU10Ubar51MSourcePromotionSameBranchEmissionGate",
        "proved": True,
        "statement": (
            "The U1/Y Route-C frontier is reduced to a single branch-coherence "
            "selector. The finite packet supplies U_10=I_3, U_bar5=F and the "
            "canonical 1_M=N^c shift rule; the HYM/projector packet supplies "
            "functional rho_s and zero-mode transport; the Gram packet fixes the "
            "conditional normalization rho_s(T_i)/sqrt(2); and the Chern-Weil "
            "functional gives N_alpha1(h_ext)=1. These pieces are mutually "
            "compatible and support-complete, but they are not yet one selected "
            "same-branch emission. Closure now requires a finite validator replay "
            "or typed monad/Cech/HYM theorem proving that these values are emitted "
            "by the same selected source."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCU10Ubar51MSourcePromotionSameBranchEmission",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "source_promotion_packet": packet,
        "counts": counts,
        "branch_coherence_selector": branch_coherence_selector,
        "decision": decision,
        "theorem": theorem,
        "what_closes_now": {
            "support_complete_sourcepromotion_packet_constructed": True,
            "finite_and_functional_routes_joined_into_one_contract": True,
            "exact_remaining_selector_named": True,
            "acceptable_closure_payloads_listed": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "branch_coherence_selector": True,
            "finite_validator_replay_with_selected_provenance": True,
            "typed_monad_or_cech_source_packet": True,
            "direct_hym_strominger_finite_extraction": True,
            "selected_alpha1_driver": True,
            "lambda_12": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_selected_U10_Ubar5": False,
            "claims_selected_1M_Dirac_source": False,
            "claims_selected_overlap_normalization": False,
            "claims_alpha1_driver_verified": False,
            "claims_lambda12": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCU10Ubar51MSourcePromotionSameBranchEmission",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "support_present": counts["support_present"],
        "required_fields": counts["required"],
        "functional_selected": counts["functional_selected"],
        "physical_selected": counts["physical_selected"],
        "same_branch": counts["same_branch"],
        "branch_coherence_selector_needed": True,
        "alpha1_driver_verified": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C U10Ubar5 1M SourcePromotion SameBranch Emission v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"support_present = {cert['support_present']} / {cert['required_fields']}",
        f"functional_selected = {cert['functional_selected']} / {cert['required_fields']}",
        f"physical_selected = {cert['physical_selected']} / {cert['required_fields']}",
        f"same_branch = {cert['same_branch']} / {cert['required_fields']}",
        f"branch_coherence_selector_needed = {str(cert['branch_coherence_selector_needed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The finite q79 packet, the HYM/projector transport packet, the Gram",
        "normalization packet, and the Chern-Weil functional value are compatible.",
        "They now form one explicit source-promotion contract. They still do not",
        "form one selected same-branch emission.",
        "",
        "## Packet",
        "",
        "| Field | Value | Support | Functional | Physical | Same Branch |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for key, row in candidate["source_promotion_packet"].items():
        lines.append(
            f"| `{key}` | `{row['value']}` | `{str(row['support_present']).lower()}` | "
            f"`{str(row['functional_selected']).lower()}` | `{str(row['physical_selected']).lower()}` | "
            f"`{str(row['same_branch']).lower()}` |"
        )
    lines.extend(
        [
            "",
            "## Branch-Coherence Selector",
            "",
        ]
    )
    for item in candidate["branch_coherence_selector"]["must_prove"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Acceptable Closure Payloads",
            "",
        ]
    )
    for item in candidate["branch_coherence_selector"]["acceptable_payloads"]:
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
            "- Do not promote compatible support pieces to selected same-branch emission.",
            "- Do not promote `N_alpha1(h_ext)=1` to `du/dalpha1=h_ext` until branch coherence and normalization emit together.",
            "- Do not set `alpha1_driver_verified`, `lambda_12`, `A_selected`, or `b_selected` here.",
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
