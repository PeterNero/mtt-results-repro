"""Build the U1/Y Route-C alpha1 tangent or retarded-overlap kernel gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
PROTOSPINOR = TEXPAPERS / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "u1y_dotd_alpha1_c1_gate": DATA / "selected_u1y_routec_dotd_alpha1_c1_response_emission.candidate.json",
    "q79_sector_charge": Q79 / "certificates" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.json",
    "q79_matter_slot_overlap": Q79 / "certificates" / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json",
    "q79_conditional_weylpair_A": Q79 / "certificates" / "q79_routec_weylpair_aselected_assembly_or_source_proof_certificate.json",
    "nonsm_alpha1_kernel": NONSM / "certificates" / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt_certificate.json",
    "nonsm_weylpair_chain": NONSM / "certificates" / "q79_weylpair_sector_charge_samesource_nogo_chain_import_certificate.json",
    "protospinor_sector_import": PROTOSPINOR / "certificates" / "routec_weylpair_sector_charge_import_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_alpha1_tangent_or_retarded_overlap_kernel.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_alpha1_tangent_or_retarded_overlap_kernel_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Alpha1_Tangent_or_RetardedOverlap_Kernel_v1.md"

STATUS = "U1Y_ROUTEC_ALPHA1_TANGENT_KERNEL_REDUCED_MATTERSLOT_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_SameSource_MatterSlot_Overlap_OperatorPacket_or_SelectedResidual_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def status_of(key: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(INPUTS[key]),
        "present": INPUTS[key].exists(),
        "status": data.get("status", "UNKNOWN"),
        "next_required_artifact": data.get("next_required_artifact") or data.get("verdict", {}).get("next_required_artifact"),
        "guardrails": data.get("guardrails"),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    dotd_gate = load(INPUTS["u1y_dotd_alpha1_c1_gate"])
    q79_sector = load(INPUTS["q79_sector_charge"])
    q79_matter = load(INPUTS["q79_matter_slot_overlap"])
    q79_weyl_A = load(INPUTS["q79_conditional_weylpair_A"])
    nonsm_kernel = load(INPUTS["nonsm_alpha1_kernel"])
    nonsm_chain = load(INPUTS["nonsm_weylpair_chain"])
    protospinor_sector = load(INPUTS["protospinor_sector_import"])

    transfer = dotd_gate["selected_tangent_or_retarded_kernel_obstruction"]["retarded_kernel_route"]["transfer_checks"]
    sector_decision = q79_sector["sector_charge_reduction"]["decision"]
    matter_packet = q79_matter["matter_slot_overlap_reduction"]["same_source_operator_packet"]
    conditional_A = q79_weyl_A["conditional_solve"]

    decision = {
        "retarded_ckm_kernel_pattern_available": transfer["K1_ckm_retarded_kernel_pattern_available"],
        "q79_phi_fin_alpha1_support_available": transfer["K2_q79_phi_fin_alpha1_support_available"],
        "source_level_weyl_carrier_available": transfer["K3_source_level_weyl_carrier_available"],
        "conditional_weylpair_A_rank_solve_available": conditional_A["closed_now"]["conditional_A_weylpair_assembled"],
        "selected_sector_charge_or_chirality": False,
        "selected_matter_slot_charge": False,
        "selected_1M_neutrino_rule": False,
        "selected_transfer_normalization": False,
        "selected_BN_tangent_or_retarded_kernel": False,
        "sector_equality_to_dotD_matrices": False,
        "honest_dotD_replay_from_kernel": False,
        "A_selected_or_b_selected_emitted": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    reduction = {
        "kernel_route": {
            "status": "PATTERN_AVAILABLE_TRANSFER_OPEN",
            "source": nonsm_kernel["status"],
            "what_closes": nonsm_kernel["verdict"]["what_closes_now"],
            "what_remains": nonsm_kernel["verdict"]["what_remains"],
            "transfer_checks": transfer,
        },
        "sector_charge_route": {
            "status": q79_sector["status"],
            "structural_partition_identified": sector_decision["su5_e6_partition_matches_required_route"],
            "selected_sector_charge_or_chirality_table_proved": sector_decision["selected_sector_charge_or_chirality_table_proved"],
            "selected_transfer_normalization_proved": sector_decision["selected_transfer_normalization_proved"],
            "still_open": q79_sector["still_open"],
        },
        "matter_slot_overlap_route": {
            "status": q79_matter["status"],
            "same_source_packet_required": q79_matter["matter_slot_overlap_reduction"]["decision"]["same_source_operator_packet_required"],
            "required_fields": matter_packet["required_fields"],
            "selected_fields": matter_packet["selected_fields"],
            "field_counts": matter_packet["field_counts"],
        },
        "conditional_weylpair_A_route": {
            "status": q79_weyl_A["status"],
            "rank": conditional_A["locked_solve"]["rank"],
            "shape": conditional_A["conditional_operator"]["shape"],
            "relative_residual": conditional_A["locked_solve"]["relative_residual"],
            "is_A_selected": conditional_A["conditional_operator"]["is_A_selected"],
            "why_not_selected": conditional_A["conditional_operator"]["why_not_selected"],
        },
        "nonsm_chain_import": {
            "status": nonsm_chain["status"],
            "decision": nonsm_chain["decision"],
            "verdict": nonsm_chain["verdict"],
        },
        "protospinor_alignment": {
            "status": protospinor_sector["status"],
            "verdict": protospinor_sector["verdict"],
        },
    }

    theorem = {
        "name": "U1YRouteCAlpha1TangentKernelReductionTheorem",
        "proved": True,
        "statement": (
            "The U1/Y Route-C alpha1 tangent cannot be obtained directly from the "
            "closed D_E gap layer or the nonzero dotD value packet. The retarded "
            "kernel pattern, source-level Weyl carrier, and conditional 72x2 "
            "Weyl-pair solve are available, but transfer to a selected B_N "
            "alpha1 tangent requires a same-source matter-slot/overlap operator "
            "packet: selected sector charge/chirality, the 1_M Dirac-neutrino "
            "routing rule, selected overlap transfer, and selected normalization. "
            "These are not emitted by the current corpus."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCAlpha1TangentOrRetardedOverlapKernel",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            key: status_of(key, data)
            for key, data in {
                "u1y_dotd_alpha1_c1_gate": dotd_gate,
                "q79_sector_charge": q79_sector,
                "q79_matter_slot_overlap": q79_matter,
                "q79_conditional_weylpair_A": q79_weyl_A,
                "nonsm_alpha1_kernel": nonsm_kernel,
                "nonsm_weylpair_chain": nonsm_chain,
                "protospinor_sector_import": protospinor_sector,
            }.items()
        },
        "decision": decision,
        "reduction": reduction,
        "theorem": theorem,
        "what_closes_now": {
            "alpha1_kernel_route_classified": True,
            "retarded_kernel_pattern_carried_as_support": True,
            "source_level_weyl_carrier_carried_as_support": True,
            "conditional_weylpair_rank_solve_carried_as_support": True,
            "same_source_matter_slot_packet_identified_as_next_gate": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_sector_charge_or_chirality": True,
            "selected_10M_to_u_e_rule": True,
            "selected_non10_plus_1M_to_d_nuD_rule": True,
            "selected_1M_neutrino_rule": True,
            "selected_overlap_transfer_functor": True,
            "selected_transfer_normalization": True,
            "selected_BN_alpha1_tangent": True,
            "sector_equality_to_dotD_matrices": True,
            "honest_dotD_replay_from_kernel": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_selected_alpha1_tangent": False,
            "claims_selected_retarded_kernel": False,
            "claims_selected_dotD_source": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "promotes_conditional_A_to_A_selected": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCAlpha1TangentOrRetardedOverlapKernel",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "retarded_kernel_pattern_available": decision["retarded_ckm_kernel_pattern_available"],
        "source_level_weyl_carrier_available": decision["source_level_weyl_carrier_available"],
        "conditional_weylpair_A_rank_solve_available": decision["conditional_weylpair_A_rank_solve_available"],
        "selected_BN_tangent_or_retarded_kernel": False,
        "selected_sector_charge_or_chirality": False,
        "selected_transfer_normalization": False,
        "honest_dotD_replay_from_kernel": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C Alpha1 Tangent or RetardedOverlap Kernel v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"retarded_kernel_pattern_available = {str(cert['retarded_kernel_pattern_available']).lower()}",
        f"source_level_weyl_carrier_available = {str(cert['source_level_weyl_carrier_available']).lower()}",
        f"conditional_weylpair_A_rank_solve_available = {str(cert['conditional_weylpair_A_rank_solve_available']).lower()}",
        f"selected_BN_tangent_or_retarded_kernel = {str(cert['selected_BN_tangent_or_retarded_kernel']).lower()}",
        f"honest_dotD_replay_from_kernel = {str(cert['honest_dotD_replay_from_kernel']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The retarded-kernel route is not empty: it has the right pattern, a",
        "source-level Weyl carrier, and a conditional Weyl-pair rank solve. The",
        "missing step is transfer into a selected `B_N` alpha1 tangent, and that",
        "transfer currently factors through the same-source matter-slot/overlap",
        "operator packet.",
        "",
        "## Required Packet Fields",
        "",
    ]
    required = candidate["reduction"]["matter_slot_overlap_route"]["required_fields"]
    for key, value in required.items():
        lines.append(f"- `{key}`: selected = `{str(value['selected_emitted']).lower()}`; required = {value['required']}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not promote the conditional 72x2 Weyl-pair operator to `A_selected`.",
            "- Do not use the locked target columns as a selector.",
            "- Do not infer selected alpha1 tangent from source-level Weyl support alone.",
            "- Do not compare to observed flavor data in this gate.",
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
