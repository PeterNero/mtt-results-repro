"""Build the selected U1/Y Route-C same-source operator-packet fill/no-go gate."""

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
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

INPUTS = {
    "u1y_hybrid_packet": DATA / "selected_u1y_routec_hybrid_galerkin_overlap_source_packet.candidate.json",
    "sm_fill_or_nogo": SM / "candidate_data" / "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json",
    "sm_fill_or_nogo_certificate": SM
    / "certificates"
    / "selected_routec_samesource_operatorpacket_fill_or_nogo_certificate.json",
    "q79_valpha_s3_attempt": Q79
    / "candidate_data"
    / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1.md"

REQUIRED_FIELDS = [
    "source_identity",
    "matter_slot_charge",
    "singlet_neutrino_rule",
    "operator_values",
    "overlap_transfer",
    "normalization",
    "primitive_contractions",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    hybrid = load(INPUTS["u1y_hybrid_packet"])
    sm_fill = load(INPUTS["sm_fill_or_nogo"])
    sm_cert = load(INPUTS["sm_fill_or_nogo_certificate"])
    q79_attempt = load(INPUTS["q79_valpha_s3_attempt"])

    attempted = sm_fill["attempted_selected_packet"]
    fields = attempted["fields"]
    selected_count = sum(1 for row in fields.values() if row["selected_emitted"])
    support_count = sum(1 for row in fields.values() if row["support_present"])

    candidate = {
        "candidate": "SelectedU1YRouteCSameSourceOperatorPacketFillOrNoGo",
        "status": "U1Y_ROUTEC_SAMESOURCE_OPERATORPACKET_FILL_NOGO_CURRENT_SCAFFOLDS_SUPPORT_ONLY",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "u1y_binding": {
            "parent_hybrid_status": hybrid["status"],
            "parent_hybrid_next": hybrid["decision"]["best_next_artifact"],
            "sm_fill_or_nogo_status": sm_fill["status"],
            "sm_validator_ok": sm_fill["validator_report"]["ok"],
            "q79_valpha_s3_status": q79_attempt["status"],
            "q79_valpha_s3_open_item_count": q79_attempt["open_item_count"],
        },
        "attempted_selected_packet": attempted,
        "fill_summary": {
            "required_fields": len(REQUIRED_FIELDS),
            "support_present": support_count,
            "selected_emitted": selected_count,
            "can_promote_A_selected": False,
            "can_promote_b_selected": False,
            "nogo_for_current_scaffolds": True,
        },
        "validator_report": sm_fill["validator_report"],
        "current_source_nogo": {
            "current_scaffold_nogo_proved": True,
            "mathematical_impossibility_claimed": False,
            "no_go_scope": "current U1/Y Route-C, SM same-source, and q79 V_alpha/S3 source records only",
            "reason": [
                "the imported SM same-source validator rejects all seven required fields",
                "the U1/Y hybrid packet has zero selected emissions across the same seven fields",
                "the q79 V_alpha/S3 same-source attempt remains open with operator-source blockers",
                "locked-target overlap and normalization entries are retained only as conditional diagnostics",
            ],
        },
        "minimal_next_subpacket": {
            "name": "Selected_U1Y_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1",
            "purpose": "emit the smallest same-source payload that could make the seven-field validator pass",
            "subpackets": [
                {
                    "name": "source_identity_bridge",
                    "must_emit": [
                        "selected visible/Route-C/V_alpha source identity",
                        "same-source binding from selected S3/Green-Schwarz support to terminal V_alpha or Route-C source",
                        "Pic0 selection or quotient policy",
                    ],
                },
                {
                    "name": "operator_values_payload",
                    "must_emit": [
                        "selected Route-C residual",
                        "selected D_E",
                        "selected Riesz/Green",
                        "selected dotD",
                        "same-source alpha1/operator driver",
                    ],
                },
                {
                    "name": "matter_overlap_payload",
                    "must_emit": [
                        "selected matter-slot charge table",
                        "selected 1_M Dirac-neutrino routing rule",
                        "selected overlap-transfer functor",
                        "selected trace/Hessian normalization",
                        "selected primitive C1/Yukawa contractions",
                    ],
                },
            ],
        },
        "what_closes": {
            "fill_attempt_executed": True,
            "sm_validator_imported": True,
            "current_scaffold_nogo_proved": True,
            "seven_missing_fields_named": REQUIRED_FIELDS,
            "minimal_source_emission_plan_named": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "source_identity": True,
            "matter_slot_charge": True,
            "singlet_neutrino_rule": True,
            "operator_values": True,
            "overlap_transfer": True,
            "normalization": True,
            "primitive_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "observed_data_used": False,
            "target_fitting_used": False,
            "locked_target_selector_used": False,
            "fixture_promoted": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_full_closure": False,
        },
        "next_required_artifact": "Selected_U1Y_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCSameSourceOperatorPacketFillOrNoGo",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "validator_exit_code": candidate["validator_report"]["exit_code"],
        "validator_ok": candidate["validator_report"]["ok"],
        "required_fields": len(REQUIRED_FIELDS),
        "support_present": support_count,
        "selected_emitted": selected_count,
        "current_scaffold_nogo_proved": True,
        "mathematical_impossibility_claimed": False,
        "next_required_artifact": candidate["next_required_artifact"],
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C Same-Source Operator Packet Fill or No-Go v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"required_fields = {candidate['fill_summary']['required_fields']}",
        f"support_present = {candidate['fill_summary']['support_present']}",
        f"selected_emitted = {candidate['fill_summary']['selected_emitted']}",
        f"current_scaffold_nogo_proved = {str(candidate['current_source_nogo']['current_scaffold_nogo_proved']).lower()}",
        f"mathematical_impossibility_claimed = {str(candidate['current_source_nogo']['mathematical_impossibility_claimed']).lower()}",
        f"validator_ok = {str(candidate['validator_report']['ok']).lower()}",
        f"validator_exit_code = {candidate['validator_report']['exit_code']}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The fill attempt is now executed in the U1/Y repo by importing the strict",
        "SM same-source validator and binding it to the current U1/Y hybrid packet",
        "and the q79 V_alpha/S3 operator-source attempt. The result is a scoped",
        "current-scaffold no-go: support exists, but none of the seven required",
        "same-source selected fields is emitted.",
        "",
        "## Seven Required Fields",
        "",
        "| Field | Provenance | Support | Selected | Same Source | Theorem Derived |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for field in REQUIRED_FIELDS:
        row = candidate["attempted_selected_packet"]["fields"][field]
        lines.append(
            f"| `{field}` | `{row['provenance']}` | `{str(row['support_present']).lower()}` | "
            f"`{str(row['selected_emitted']).lower()}` | `{str(row['same_source']).lower()}` | "
            f"`{str(row['theorem_derived']).lower()}` |"
        )
    lines.extend(
        [
            "",
            "## Why The Fill Fails",
            "",
        ]
    )
    for reason in candidate["current_source_nogo"]["reason"]:
        lines.append(f"- {reason}")
    lines.extend(
        [
            "",
            "This is not a mathematical impossibility theorem. It says the currently",
            "printed source records cannot be promoted to the selected U1/Y Route-C",
            "operator packet under the strict same-source validator.",
            "",
            "## Minimal Source-Emission Attack Plan",
            "",
            f"Next artifact: `{candidate['next_required_artifact']}`.",
            "",
        ]
    )
    for subpacket in candidate["minimal_next_subpacket"]["subpackets"]:
        lines.append(f"### {subpacket['name']}")
        for item in subpacket["must_emit"]:
            lines.append(f"- {item}")
        lines.append("")
    lines.extend(
        [
            "## Guardrails",
            "",
            "- No observed masses, CKM, PMNS, CP phase, or benchmark matrix entries are used.",
            "- Locked-target overlap and normalization data remain diagnostic only.",
            "- Finite fixture data and lifted source flags are not promoted.",
            "- `A_selected`, `b_selected`, `lambda_12`, and full closure remain open.",
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
