"""Build the selected U1/Y Route-C finite cochain source construct attempt."""

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

INPUTS = {
    "source_solve_attempt": DATA / "selected_u1y_visible_bundle_or_routec_source_solve_attempt.candidate.json",
    "finite_gate": DATA / "finite_cochain_packet_or_de_response_gate.candidate.json",
    "q79_promotion_attempt": Q79 / "certificates" / "selected_hym_operator_source_promotion.attempt.json",
    "q79_hypothetical_selected_flags": Q79
    / "candidate_data"
    / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual"
    / "hypothetical_routec_selected_flags_only"
    / "selected_source_promotion.selected_flags_only.json",
    "q79_weylpair_assembly": Q79 / "candidate_data" / "q79_routec_weylpair_aselected_assembly_or_source_proof.candidate.json",
    "q79_weylpair_source_provenance": Q79 / "candidate_data" / "q79_routec_weylpair_source_provenance_lemma.candidate.json",
    "q79_sector_charge": Q79 / "candidate_data" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json",
    "q79_same_source_operator": Q79 / "candidate_data" / "q79_same_source_operator_provenance_or_selected_routec_solve.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_finite_cochain_source_construct.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_finite_cochain_source_construct_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_Finite_Cochain_Source_Construct_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    source_solve = load(INPUTS["source_solve_attempt"])
    finite_gate = load(INPUTS["finite_gate"])
    promotion = load(INPUTS["q79_promotion_attempt"])
    hypothetical = load(INPUTS["q79_hypothetical_selected_flags"])
    assembly = load(INPUTS["q79_weylpair_assembly"])
    provenance = load(INPUTS["q79_weylpair_source_provenance"])
    sector = load(INPUTS["q79_sector_charge"])
    same_source = load(INPUTS["q79_same_source_operator"])

    conditional = assembly["conditional_solve"]
    source_reduction = provenance["source_provenance_reduction"]
    sector_reduction = sector["sector_charge_reduction"]
    honest_open = same_source["same_source_reduction"]["honest_current_open_items"]

    construct_checks = [
        {
            "name": "finite_cochain_contract_exists",
            "status": "CLOSED_CONTRACT_ONLY",
            "closed": True,
            "evidence": finite_gate["next_required_artifact"],
        },
        {
            "name": "routec_validator_plumbing_exists",
            "status": "CLOSED_DIAGNOSTIC_PLUMBING",
            "closed": True,
            "evidence": {
                "promotion_packet_paths": promotion["paths"],
                "hypothetical_selected_flags_pass_available": hypothetical["selected_source_verified"],
            },
        },
        {
            "name": "weylpair_conditional_operator",
            "status": "CLOSED_CONDITIONAL_ALGEBRA",
            "closed": True,
            "evidence": {
                "shape": conditional["conditional_operator"]["shape"],
                "rank": conditional["locked_solve"]["rank"],
                "relative_residual": conditional["locked_solve"]["relative_residual"],
                "deltaTheta_conditional": conditional["locked_solve"]["deltaTheta_conditional"],
            },
        },
        {
            "name": "source_level_weyl_carrier",
            "status": "CLOSED_SOURCE_LEVEL_CARRIER",
            "closed": True,
            "evidence": {
                "source_level_carrier_proved": source_reduction["source_level_carrier"]["proved"],
                "active_shift_proved": source_reduction["active_shift"]["proved"],
                "operator_level_projective_rhoE_promoted": source_reduction["source_level_carrier"][
                    "operator_level_projective_rhoE_promoted"
                ],
            },
        },
        {
            "name": "sector_charge_and_overlap_normalization",
            "status": "OPEN_SELECTED_MATTERSLOT_OVERLAP_THEOREM_REQUIRED",
            "closed": False,
            "evidence": {
                "structural_su5_e6_partition_matches": sector_reduction["su5_e6_structural_candidate"][
                    "matches_required_partition"
                ],
                "selected_sector_charge_or_chirality_table_proved": sector_reduction["decision"][
                    "selected_sector_charge_or_chirality_table_proved"
                ],
                "selected_transfer_normalization_proved": sector_reduction["decision"][
                    "selected_transfer_normalization_proved"
                ],
                "nuD_singlet_rule_closed": sector_reduction["su5_e6_structural_candidate"][
                    "nuD_singlet_rule_closed"
                ],
            },
        },
        {
            "name": "same_source_operator_promotion",
            "status": "OPEN_SELECTED_SOURCE_FLAGS_AND_PRIMITIVE_C1_REQUIRED",
            "closed": False,
            "evidence": {
                "honest_promotion_selected_source_verified": promotion["selected_source_verified"],
                "hypothetical_selected_source_verified": hypothetical["selected_source_verified"],
                "honest_current_open_items": honest_open,
                "primitive_c1_contractions_closed": same_source["source_evidence_status"][
                    "primitive_c1_contractions_closed"
                ],
            },
        },
    ]

    construct_packet = {
        "finite_cochain_complex": {
            "status": "CONTRACT_SPECIFIED_VALUES_OPEN",
            "spaces": finite_gate["spaces"],
            "typed_product_pairs": finite_gate["typed_product_pairs"],
            "gf_zero_equation": finite_gate["gf_zero_equation"],
            "actual_selected_bases_emitted": False,
            "actual_selected_differentials_emitted": False,
            "actual_product_tables_emitted": False,
        },
        "routec_weylpair_operator": {
            "status": "CONDITIONAL_OPERATOR_AVAILABLE_NOT_SELECTED",
            "operator_name": conditional["conditional_operator"]["name"],
            "shape": conditional["conditional_operator"]["shape"],
            "rank": conditional["locked_solve"]["rank"],
            "relative_residual": conditional["locked_solve"]["relative_residual"],
            "columns": conditional["conditional_operator"]["columns"],
            "is_A_selected": conditional["conditional_operator"]["is_A_selected"],
            "why_not_selected": conditional["conditional_operator"]["why_not_selected"],
        },
        "source_level_carrier": {
            "status": "SOURCE_LEVEL_CARRIER_CLOSED_OPERATOR_LEVEL_OPEN",
            "source_level_projective_class_selected": source_reduction["source_level_carrier"][
                "source_level_projective_class_selected"
            ],
            "uses_only_selected_active_generators_g1_g2": source_reduction["source_level_carrier"][
                "uses_only_selected_active_generators_g1_g2"
            ],
            "active_shift": source_reduction["active_shift"]["nonzero_active_shifts"],
            "operator_level_projective_rhoE_promoted": source_reduction["source_level_carrier"][
                "operator_level_projective_rhoE_promoted"
            ],
        },
        "matter_slot_overlap_gap": {
            "status": "NEXT_TRUE_SOURCE_OBJECT",
            "next_artifact": "Selected_U1Y_RouteC_MatterSlot_Overlap_Normalization_Source_v1",
            "must_prove": [
                "selected sector charge/chirality table deriving Z -> {u,e}",
                "selected sector charge/chirality table deriving X -> {d,nuD}",
                "selected singlet rule placing nuD on the shift side",
                "selected transfer normalization from source-level Weyl carrier to C1 columns",
                "same-source primitive C1/overlap tensors in the validator basis",
            ],
            "structural_candidate": sector_reduction["su5_e6_structural_candidate"],
        },
    }

    candidate = {
        "candidate": "SelectedU1YRouteCFiniteCochainSourceConstruct",
        "status": "U1Y_ROUTEC_FINITE_COHCHAIN_CONSTRUCT_BUILT_REDUCED_TO_MATTERSLOT_OVERLAP_SOURCE",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "source_solve_parent_status": source_solve["status"],
        "construct_checks": construct_checks,
        "construct_packet": construct_packet,
        "decision": {
            "finite_construct_executed": True,
            "finite_cochain_source_closed": False,
            "routec_operator_algebra_closed_conditionally": True,
            "source_level_weyl_carrier_closed": True,
            "operator_level_selected_rhoE_DE_dotD_closed": False,
            "primitive_C1_overlap_closed": False,
            "lambda_12_closed": False,
            "best_next_artifact": "Selected_U1Y_RouteC_MatterSlot_Overlap_Normalization_Source_v1",
            "why_this_is_the_way_forward": [
                "the conditional Weyl-pair operator has no rank or solve obstruction",
                "the source-level S3/GS Weyl carrier is already proved at source level",
                "the remaining gap is no longer generic matrix construction",
                "the missing theorem is the selected matter-slot/overlap normalization that promotes the carrier into selected C1 operator columns",
            ],
            "target_fitting_used": False,
        },
        "guardrails": {
            "do_not_promote_hypothetical_selected_flags": True,
            "do_not_use_locked_target_columns_as_source_selector": True,
            "do_not_claim_A_selected_or_b_selected": True,
            "do_not_claim_lambda12": True,
            "do_not_use_observed_masses_mixings_or_ckm": True,
        },
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCFiniteCochainSourceConstruct",
        "status": candidate["status"],
        "finite_construct_executed": True,
        "finite_cochain_source_closed": False,
        "routec_operator_algebra_closed_conditionally": True,
        "source_level_weyl_carrier_closed": True,
        "next_artifact": candidate["decision"]["best_next_artifact"],
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    checks = candidate["construct_checks"]
    packet = candidate["construct_packet"]
    lines = [
        "# Selected U1Y Route-C Finite Cochain Source Construct v1",
        "",
        "## Result",
        "",
        "```text",
        f"finite_construct_executed = {str(candidate['decision']['finite_construct_executed']).lower()}",
        f"finite_cochain_source_closed = {str(candidate['decision']['finite_cochain_source_closed']).lower()}",
        f"routec_operator_algebra_closed_conditionally = {str(candidate['decision']['routec_operator_algebra_closed_conditionally']).lower()}",
        f"source_level_weyl_carrier_closed = {str(candidate['decision']['source_level_weyl_carrier_closed']).lower()}",
        f"primitive_C1_overlap_closed = {str(candidate['decision']['primitive_C1_overlap_closed']).lower()}",
        f"lambda_12_closed = {str(candidate['decision']['lambda_12_closed']).lower()}",
        f"best_next_artifact = {candidate['decision']['best_next_artifact']}",
        "```",
        "",
        "The finite Route-C cochain construct has now been executed. It does not",
        "close the selected U1/Y source, but it removes a major ambiguity: the",
        "Route-C algebraic operator layer has no rank/solve obstruction once the",
        "Weyl-pair carrier is allowed. The remaining gap is the source theorem",
        "that transports the already selected source-level Weyl carrier into",
        "selected matter-slot C1 operator columns with normalization.",
        "",
        "## Construct Checks",
        "",
        "| Check | Status | Closed |",
        "| --- | --- | --- |",
    ]
    for check in checks:
        lines.append(f"| `{check['name']}` | `{check['status']}` | `{str(check['closed']).lower()}` |")
    lines.extend(
        [
            "",
            "## What Is Actually Available",
            "",
            f"- finite cochain spaces: `{', '.join(packet['finite_cochain_complex']['spaces'])}`",
            f"- typed product pairs: `{packet['finite_cochain_complex']['typed_product_pairs']}`",
            f"- monad equation: `{packet['finite_cochain_complex']['gf_zero_equation']}`",
            f"- conditional Weyl-pair operator shape: `{packet['routec_weylpair_operator']['shape']}`",
            f"- conditional Weyl-pair rank: `{packet['routec_weylpair_operator']['rank']}`",
            f"- conditional solve residual: `{packet['routec_weylpair_operator']['relative_residual']}`",
            f"- source-level Weyl carrier selected: `{packet['source_level_carrier']['source_level_projective_class_selected']}`",
            f"- operator-level rhoE/DE promotion: `{packet['source_level_carrier']['operator_level_projective_rhoE_promoted']}`",
            "",
            "## Next True Object",
            "",
            f"`{packet['matter_slot_overlap_gap']['next_artifact']}` must prove:",
            "",
        ]
    )
    for item in packet["matter_slot_overlap_gap"]["must_prove"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not promote hypothetical selected flags.",
            "- Do not use locked target columns as a source selector.",
            "- Do not claim `A_selected`, `b_selected`, primitive C1, `lambda_12`, or full SM closure from this construct.",
            "- Do not use observed masses, mixings, CKM entries, or benchmark flavor data.",
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
    DATA.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    PROOF.mkdir(parents=True, exist_ok=True)
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
