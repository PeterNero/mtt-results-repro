"""Build the selected U1/Y Route-C matter-slot overlap normalization source gate."""

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
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "routec_finite_construct": DATA / "selected_u1y_routec_finite_cochain_source_construct.candidate.json",
    "q79_sector_charge": Q79 / "candidate_data" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json",
    "sm_c1_routing_normalization_overlap": SM
    / "candidate_data"
    / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet.candidate.json",
    "sm_hybrid_matter_slot": SM / "candidate_data" / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json",
    "sm_matter_slot_or_blocksector": SM
    / "candidate_data"
    / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_matter_slot_overlap_normalization_source.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_matter_slot_overlap_normalization_source_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_MatterSlot_Overlap_Normalization_Source_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    finite = load(INPUTS["routec_finite_construct"])
    q79_sector = load(INPUTS["q79_sector_charge"])
    sm_c1 = load(INPUTS["sm_c1_routing_normalization_overlap"])
    sm_hybrid = load(INPUTS["sm_hybrid_matter_slot"])
    sm_matter = load(INPUTS["sm_matter_slot_or_blocksector"])

    q79_reduction = q79_sector["sector_charge_reduction"]
    structural = q79_reduction["su5_e6_structural_candidate"]
    c1_attempts = sm_c1["attempts"]
    hybrid_attempts = sm_hybrid["attempts"]
    hybrid_packet = sm_matter["hybrid_closing_packet"]

    theorem_clauses = [
        {
            "clause": "Z_to_u_e",
            "status": "STRUCTURAL_CANDIDATE_NOT_SELECTED",
            "closed": False,
            "evidence": {
                "phase_route_from_10M": structural["phase_route_from_10M"],
                "matches_conditional_route": c1_attempts["c1_routing"]["conditional_route"]["phase_Z_to"]
                == ["u", "e"],
                "selected_source_independently_derives_route": c1_attempts["c1_routing"][
                    "selected_source_independently_derives_route"
                ],
            },
        },
        {
            "clause": "X_to_d_nuD",
            "status": "STRUCTURAL_CANDIDATE_SINGLET_GAP",
            "closed": False,
            "evidence": {
                "shift_route_from_non10_plus_singlet": structural["shift_route_from_non10_plus_singlet"],
                "matches_conditional_route": c1_attempts["c1_routing"]["conditional_route"]["shift_X_to"]
                == ["d", "nuD"],
                "selected_singlet_rule_closed": q79_reduction["decision"][
                    "selected_singlet_neutrino_shift_rule_proved"
                ],
            },
        },
        {
            "clause": "selected_transfer_normalization",
            "status": "CONDITIONAL_EXACT_SELECTED_NORMALIZATION_OPEN",
            "closed": False,
            "evidence": {
                "conditional_deltaTheta": c1_attempts["normalization"]["conditional_deltaTheta"],
                "conditional_condition_number": c1_attempts["normalization"]["conditional_condition_number"],
                "conditional_residual_norm": c1_attempts["normalization"]["conditional_residual_norm"],
                "selected_normalization_emitted": c1_attempts["normalization"]["selected_normalization_emitted"],
            },
        },
        {
            "clause": "selected_overlap_transfer_functor",
            "status": "OVERLAP_FUNCTOR_REQUIRED",
            "closed": False,
            "evidence": {
                "required_as_selected_object": c1_attempts["overlap_source"]["required_as_selected_object"],
                "selected_overlap_tensor_or_functor_emitted": c1_attempts["overlap_source"][
                    "selected_overlap_tensor_or_functor_emitted"
                ],
                "enriched_weyl_pair_conditionally_sufficient": c1_attempts["overlap_source"][
                    "enriched_weyl_pair_conditionally_sufficient"
                ],
            },
        },
        {
            "clause": "selected_operator_galerkin_source",
            "status": "HYBRID_PACKET_IDENTIFIED_SOURCE_OPEN",
            "closed": False,
            "evidence": {
                "recommended_strategy": hybrid_packet["recommended_strategy"],
                "selected_operator_source_present": sm_hybrid["selection_verdict"]["selected_operator_source_present"],
                "shape_scaffold_present": sm_hybrid["selection_verdict"]["shape_scaffold_present"],
                "identity_transport_no_go": hybrid_attempts["honest_routec_galerkin_fill"]["basis_transport"][
                    "current_relative_transport"
                ],
            },
        },
    ]

    what_closes = {
        "same_source_matter_slot_theorem_attempted": True,
        "su5_e6_structural_partition_identified": structural["matches_required_partition"],
        "conditional_c1_route_exact": sm_c1["selection_verdict"]["conditional_algebra_closed"],
        "locked_target_not_promoted": True,
        "legal_closure_routes_separated": True,
        "next_source_packet_minimized": True,
    }

    next_packet = {
        "name": "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1",
        "must_supply": [
            "selected HYM/Strominger or equivalent selected operator source for D_E",
            "Riesz projectors, complement gap, reduced Green operator, and truncation certificate",
            "selected zero-mode bases and L2 metrics for 10_M, bar5_M, and 1_M or sector-resolved u,d,e,nuD",
            "selected dotD_alpha1 and primitive C1 responses in the same branch",
            "source theorem that routes 10_M to the phase/clock Z leg",
            "source theorem that routes bar5_M plus 1_M/nuD to the shift X leg",
            "selected transfer normalization from source-level Weyl carrier to C1 columns",
            "same-source primitive overlap tensor or transfer functor T_selected",
        ],
        "acceptance_test": [
            "derive Z -> {u,e} without locked target columns",
            "derive X -> {d,nuD} without locked target columns",
            "emit A_selected and b_selected from source data",
            "run selected Route-C residual, D_E, Riesz/Green, dotD, and primitive C1 validators",
        ],
    }

    candidate = {
        "candidate": "SelectedU1YRouteCMatterSlotOverlapNormalizationSource",
        "status": "U1Y_ROUTEC_MATTERSLOT_OVERLAP_THEOREM_ATTEMPTED_REDUCED_TO_HYBRID_GALERKIN_SOURCE_PACKET",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": finite["status"],
        "theorem_clauses": theorem_clauses,
        "structural_candidate": structural,
        "what_closes": what_closes,
        "what_remains_open": {
            "selected_Z_to_u_e_source_theorem": True,
            "selected_X_to_d_nuD_source_theorem": True,
            "selected_nuD_singlet_rule": True,
            "selected_transfer_normalization": True,
            "selected_overlap_tensor_or_functor": True,
            "same_source_DE_Riesz_Green_dotD": True,
            "primitive_C1_contractions": True,
            "lambda_12": True,
            "full_SM_or_no_knob_closure": True,
        },
        "decision": {
            "theorem_closed": False,
            "conditional_route_exact": True,
            "structural_partition_matches": structural["matches_required_partition"],
            "selected_source_independently_derives_route": False,
            "best_next_artifact": next_packet["name"],
            "target_fitting_used": False,
        },
        "next_packet": next_packet,
        "guardrails": {
            "uses_locked_target_columns_as_selector": False,
            "uses_observed_masses_or_ckm_inputs": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
        },
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCMatterSlotOverlapNormalizationSource",
        "status": candidate["status"],
        "theorem_closed": False,
        "structural_partition_matches": structural["matches_required_partition"],
        "conditional_route_exact": True,
        "selected_source_independently_derives_route": False,
        "next_artifact": next_packet["name"],
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C MatterSlot Overlap Normalization Source v1",
        "",
        "## Result",
        "",
        "```text",
        f"theorem_closed = {str(candidate['decision']['theorem_closed']).lower()}",
        f"conditional_route_exact = {str(candidate['decision']['conditional_route_exact']).lower()}",
        f"structural_partition_matches = {str(candidate['decision']['structural_partition_matches']).lower()}",
        f"selected_source_independently_derives_route = {str(candidate['decision']['selected_source_independently_derives_route']).lower()}",
        f"lambda_12_closed = {str(cert['lambda_12_closed']).lower()}",
        f"best_next_artifact = {candidate['decision']['best_next_artifact']}",
        "```",
        "",
        "This theorem gate was executed. It does not close the selected matter-slot",
        "overlap theorem. It does close the reduction: the SU(5)/E6 structural",
        "partition is the unique viable candidate for the conditional Route-C",
        "routing, but current source data still do not independently emit the",
        "`10_M` clock rule, the `bar5_M/1_M` shift rule, the `nuD` singlet rule,",
        "or the selected overlap normalization.",
        "",
        "## Clause Outcomes",
        "",
        "| Clause | Status | Closed |",
        "| --- | --- | --- |",
    ]
    for clause in candidate["theorem_clauses"]:
        lines.append(f"| `{clause['clause']}` | `{clause['status']}` | `{str(clause['closed']).lower()}` |")
    lines.extend(
        [
            "",
            "## What Closes",
            "",
        ]
    )
    for key, value in candidate["what_closes"].items():
        lines.append(f"- `{key}` = `{str(value).lower()}`")
    lines.extend(
        [
            "",
            "## Next Packet",
            "",
            f"`{candidate['next_packet']['name']}` must supply:",
            "",
        ]
    )
    for item in candidate["next_packet"]["must_supply"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "Acceptance test:",
            "",
        ]
    )
    for item in candidate["next_packet"]["acceptance_test"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not use locked target columns as the source selector.",
            "- Do not promote the SU(5)/E6 dictionary alone into selected overlap data.",
            "- Do not claim `A_selected`, `b_selected`, `lambda_12`, or full SM closure from this gate.",
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
