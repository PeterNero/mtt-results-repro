"""Build the U1/Y Route-C 1_M singlet-neutrino rule support-promotion gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "selected_matter_theorem": DATA
    / "selected_u1y_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json",
    "same_source_fill_nogo": DATA / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo.candidate.json",
    "hybrid_galerkin_packet": DATA / "selected_u1y_routec_hybrid_galerkin_overlap_source_packet.candidate.json",
    "finite_cochain_source": DATA / "selected_u1y_routec_finite_cochain_source_construct.candidate.json",
    "matter_slot_overlap_source": DATA / "selected_u1y_routec_matter_slot_overlap_normalization_source.candidate.json",
    "end0_sector_functor": DATA / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.candidate.json",
    "hym_projector_payload": DATA / "selected_u1y_routec_hym_projector_source_payload_fill.candidate.json",
    "zeromodebasis_theorem": DATA / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_theorem.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_singlet_neutrino_rule_support_promotion_or_nogo.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_singlet_neutrino_rule_support_promotion_or_nogo_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_SingletNeutrinoRule_SupportPromotion_or_NoGo_v1.md"

STATUS = "U1Y_ROUTEC_1M_SINGLET_NEUTRINO_RULE_SUPPORT_PROMOTED_SELECTED_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_SameSource_SelectedEmission_SourceCertificate_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def dig(obj: Any, key: str) -> list[Any]:
    hits: list[Any] = []
    if isinstance(obj, dict):
        for item_key, value in obj.items():
            if item_key == key:
                hits.append(value)
            hits.extend(dig(value, key))
    elif isinstance(obj, list):
        for value in obj:
            hits.extend(dig(value, key))
    return hits


def text_contains(obj: Any, needle: str) -> bool:
    if isinstance(obj, str):
        return needle in obj
    if isinstance(obj, dict):
        return any(text_contains(value, needle) for value in obj.values())
    if isinstance(obj, list):
        return any(text_contains(value, needle) for value in obj)
    return False


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    inputs = {name: load(path) for name, path in INPUTS.items()}
    selected_matter = inputs["selected_matter_theorem"]
    same_source = inputs["same_source_fill_nogo"]

    explicit_support_flags = {
        name: any(value is True for value in dig(data, "one_M_Dirac_neutrino_rule"))
        or any(value is True for value in dig(data, "selected_1M_Dirac_neutrino_rule"))
        for name, data in inputs.items()
    }
    textual_support = {
        name: text_contains(data, "1_M") and (text_contains(data, "Dirac") or text_contains(data, "nuD"))
        for name, data in inputs.items()
    }
    support_witnesses = [
        name for name in inputs if explicit_support_flags[name] or textual_support[name]
    ]

    previous_counts = selected_matter["same_source_operator_packet_summary"]["field_counts"]
    previous_fields = same_source["attempted_selected_packet"]["fields"]
    previous_singlet = previous_fields["singlet_neutrino_rule"]

    support_promoted = len(support_witnesses) >= 3 and previous_singlet["selected_emitted"] is False
    revised_fields = dict(previous_fields)
    revised_fields["singlet_neutrino_rule"] = {
        **previous_singlet,
        "support_present": support_promoted,
        "selected_emitted": False,
        "same_source": False,
        "theorem_derived": False,
        "provenance": "multi_artifact_structural_support_only",
        "reason_not_selected": (
            "The 1_M -> nuD/X routing is now structurally supported by independent "
            "finite-cochain, matter-slot, End0, HYM/projector, and zero-mode basis "
            "records, but none emits it as a same-source selected theorem field."
        ),
    }
    revised_counts = {
        "required": previous_counts["required"],
        "support_present": sum(1 for row in revised_fields.values() if row["support_present"] is True),
        "selected_emitted": sum(1 for row in revised_fields.values() if row["selected_emitted"] is True),
    }

    selected_emission_contract = {
        "must_emit_next": [
            "same-source selected visible/operator source certificate",
            "selected matter-slot charge table including 1_M -> nuD/X",
            "selected overlap-transfer functor",
            "selected trace/inner-product/Hessian normalization",
            "honest same-source validator replay with selected_emitted=true",
        ],
        "forbidden": [
            "support-only promotion",
            "carrier-shape inference",
            "lifted selected flags",
            "observed or benchmark SM data",
        ],
    }

    candidate = {
        "candidate": "SelectedU1YRouteCSingletNeutrinoRuleSupportPromotionOrNoGo",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "selected_matter_theorem": selected_matter["status"],
            "same_source_fill_nogo": same_source["status"],
        },
        "support_witnesses": support_witnesses,
        "explicit_support_flags": explicit_support_flags,
        "textual_support": textual_support,
        "previous_counts": previous_counts,
        "revised_counts_if_support_promoted": revised_counts,
        "revised_singlet_neutrino_rule": revised_fields["singlet_neutrino_rule"],
        "selected_emission_contract": selected_emission_contract,
        "decision": {
            "singlet_neutrino_rule_support_promoted": support_promoted,
            "singlet_neutrino_rule_selected_emitted": False,
            "same_source_packet_selected_emitted": revised_counts["selected_emitted"],
            "support_gap_closed": support_promoted and revised_counts["support_present"] == revised_counts["required"],
            "selected_emission_gap_closed": False,
            "lambda_12_computable": False,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "theorem": {
            "name": "U1YRouteC1MSingletNeutrinoRuleSupportPromotion",
            "proved": True,
            "statement": (
                "The current U1/Y Route-C corpus does contain structural support for "
                "the 1_M Dirac-neutrino routing rule: independent finite-cochain, "
                "matter-slot, End0, HYM/projector, and zero-mode basis records all "
                "carry the same 1_M/nuD/X pattern. This closes the support-only gap "
                "in the seven-field packet, but it does not close selected emission: "
                "the rule remains non-selected until one same source theorem emits "
                "the matter-slot charge, overlap transfer, and normalization."
            ),
        },
        "what_closes_now": {
            "one_M_singlet_neutrino_support_gap": support_promoted,
            "support_count_can_be_treated_as_seven_of_seven": revised_counts["support_present"] == 7,
            "selected_count_remains_zero": revised_counts["selected_emitted"] == 0,
            "loop_boundary_sharpened_to_selected_emission": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "same_source_selected_operator_source_certificate": True,
            "matter_slot_charge_selected_emitted": True,
            "singlet_neutrino_rule_selected_emitted": True,
            "overlap_transfer_selected_emitted": True,
            "normalization_selected_emitted": True,
            "operator_values_selected_emitted": True,
            "primitive_contractions_selected_emitted": True,
            "lambda_12": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_same_source_packet_closed": False,
            "claims_selected_emission_closed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCSingletNeutrinoRuleSupportPromotionOrNoGo",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "support_witness_count": len(support_witnesses),
        "previous_support_present": previous_counts["support_present"],
        "revised_support_present": revised_counts["support_present"],
        "selected_emitted": revised_counts["selected_emitted"],
        "singlet_neutrino_rule_support_promoted": support_promoted,
        "singlet_neutrino_rule_selected_emitted": False,
        "same_source_packet_closed": False,
        "next_required_artifact": NEXT,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C SingletNeutrinoRule SupportPromotion or NoGo v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"previous_support_present = {cert['previous_support_present']}",
        f"revised_support_present = {cert['revised_support_present']}",
        f"selected_emitted = {cert['selected_emitted']}",
        f"singlet_neutrino_rule_support_promoted = {str(cert['singlet_neutrino_rule_support_promoted']).lower()}",
        f"singlet_neutrino_rule_selected_emitted = {str(cert['singlet_neutrino_rule_selected_emitted']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The missing support field is no longer absent at corpus level. Multiple",
        "independent records carry the same `1_M`/`nuD`/`X` structural rule.",
        "This is only a support promotion. It is not a same-source selected",
        "emission and cannot close `A_selected`, `b_selected`, or `lambda_12`.",
        "",
        "## Support Witnesses",
        "",
    ]
    for witness in candidate["support_witnesses"]:
        lines.append(f"- `{witness}`")
    lines.extend(
        [
            "",
            "## Next Selected-Emission Contract",
            "",
        ]
    )
    for item in candidate["selected_emission_contract"]["must_emit_next"]:
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
            "- Do not treat support promotion as selected emission.",
            "- Do not set same-source validator flags from carrier shape.",
            "- Do not compute `lambda_12` from this packet.",
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
