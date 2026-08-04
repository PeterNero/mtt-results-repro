"""Analyze the q79 selected matter-slot charge and overlap normalization theorem.

The previous q79 reduction showed that the Weyl-pair sector route has the right
SU(5)/E6 structural partition, but lacks selected matter-slot charge and
selected overlap normalization.  The latest SM-parity artifacts attempt exactly
that theorem and reduce it to one same-source operator packet.  This q79 script
imports that result and records the precise remaining selected fields.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

OUT_DIR = CANDIDATES / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem"
OUT_TABLE = OUT_DIR / "matter_slot_overlap_reduction_table.json"
OUT_CANDIDATE = CANDIDATES / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
OUT_CERT = CERTS / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1.md"

STATUS = (
    "Q79_SELECTED_MATTERSLOT_CHARGE_OVERLAP_NORMALIZATION_THEOREM_"
    "REDUCED_TO_SAMESOURCE_OPERATOR_PACKET_OPEN"
)
NEXT = "Q79_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1"

Q79_INPUTS = {
    "sector_charge_reduction": CERTS / "q79_routec_weylpair_sector_charge_or_chirality_certificate.json",
    "source_provenance": CERTS / "q79_routec_weylpair_source_provenance_lemma_certificate.json",
    "conditional_weylpair_A": CERTS
    / "q79_routec_weylpair_aselected_assembly_or_source_proof_certificate.json",
    "su5_matter_slot_transversality": CERTS / "su5_matter_slot_transversality_certificate.json",
    "su5_source_attempt": CERTS / "selected_su5_source_proof_attempt_certificate.json",
}

SM_INPUTS = {
    "matter_slot_overlap_theorem": SM
    / "certificates"
    / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json",
    "matter_slot_overlap_theorem_candidate": SM
    / "candidate_data"
    / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json",
    "same_source_operator_packet": SM
    / "certificates"
    / "selected_routec_samesource_matter_slot_overlap_operator_packet_certificate.json",
    "same_source_operator_packet_candidate": SM
    / "candidate_data"
    / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": str(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
        "what_closes": data.get("what_closes") or data.get("what_closes_now") or {},
        "what_remains_open": data.get("what_remains_open") or data.get("still_open") or {},
    }


def build_reduction(q79: dict[str, dict[str, Any]], sm: dict[str, dict[str, Any]]) -> dict[str, Any]:
    q79_sector = q79["sector_charge_reduction"]
    q79_source = q79["source_provenance"]
    q79_A = q79["conditional_weylpair_A"]
    q79_su5 = q79["su5_matter_slot_transversality"]
    q79_su5_source = q79["su5_source_attempt"]
    sm_theorem = sm["matter_slot_overlap_theorem_candidate"]
    sm_packet = sm["same_source_operator_packet_candidate"]

    sector_decision = q79_sector.get("sector_charge_reduction", {}).get("decision", {})
    source_decision = q79_source.get("decision", {})
    A_decision = q79_A.get("decision", {})
    finite = sm_theorem.get("finite_matter_slot", {})
    matter_charge = sm_theorem.get("matter_slot_charge", {})
    overlap = sm_theorem.get("overlap_normalization", {})
    same_source_obstruction = sm_theorem.get("same_source_obstruction", {})
    selection = sm_theorem.get("selection_verdict", {})
    packet_status = sm_packet.get("same_source_status", {})
    required_fields = sm_packet.get("required_fields", {})
    field_counts = sm_packet.get("field_counts", {})

    selected_fields = {
        name: row.get("selected_emitted") is True for name, row in required_fields.items()
    }
    support_fields = {
        name: row.get("current_support") is True for name, row in required_fields.items()
    }
    all_selected = all(selected_fields.values()) if selected_fields else False

    return {
        "proved_imported_support": {
            "source_level_weyl_carrier_closed": source_decision.get(
                "source_level_weyl_carrier_and_active_shift_proved"
            )
            is True,
            "conditional_source_to_c1_transfer_exact": source_decision.get(
                "conditional_source_to_C1_transfer_exact"
            )
            is True,
            "conditional_A_rank_and_solve_closed": A_decision.get(
                "conditional_A_solve_exact"
            )
            is True
            or q79_A.get("theorem", {}).get("proved") is True,
            "su5_e6_partition_matches_required_route": sector_decision.get(
                "su5_e6_partition_matches_required_route"
            )
            is True,
            "finite_su5_transversality_under_source_hypothesis_closed": finite.get(
                "under_transversality_closed"
            )
            is True
            and q79_su5.get("calculation_results", {}).get(
                "finite_transversality_theorem_closed"
            )
            is True,
            "conditional_routing_and_normalization_exact": selection.get(
                "conditional_routing_and_normalization_are_exact"
            )
            is True,
        },
        "matter_slot_charge": {
            "desired_phase_route": matter_charge.get("desired_phase_route"),
            "desired_shift_route": matter_charge.get("desired_shift_route"),
            "routeA_matches_required_partition": matter_charge.get(
                "routeA_matches_required_partition"
            )
            is True,
            "routeB_current_selected_block_uniform": matter_charge.get(
                "routeB_current_selected_block_uniform"
            )
            is True,
            "selected_charge_table_closed": matter_charge.get("selected_charge_table_closed")
            is True,
            "singlet_1M_rule_present": matter_charge.get("singlet_1M_rule_present") is True,
            "structural_su5_match": matter_charge.get("structural_su5_match"),
            "all_su5_source_routes_blocked": q79_su5_source.get("calculation_results", {}).get(
                "all_current_source_routes_blocked"
            )
            is True,
        },
        "overlap_normalization": {
            "conditional_residual_norm": overlap.get("conditional_residual_norm"),
            "conditional_condition_number": overlap.get("conditional_condition_number"),
            "enriched_weyl_pair_conditionally_sufficient": overlap.get(
                "enriched_weyl_pair_conditionally_sufficient"
            )
            is True,
            "selected_overlap_functor_emitted": overlap.get("selected_overlap_functor_emitted")
            is True,
            "selected_normalization_emitted": overlap.get("selected_normalization_emitted")
            is True,
            "canonical_overlap_lane_retired_for_nonzero": overlap.get(
                "canonical_overlap_lane_retired_for_nonzero"
            )
            is True,
        },
        "same_source_operator_packet": {
            "contract_status": sm_packet.get("status"),
            "next_required_artifact": sm_packet.get("next_required_artifact"),
            "field_counts": field_counts,
            "required_fields": required_fields,
            "selected_fields": selected_fields,
            "support_fields": support_fields,
            "packet_closed": packet_status.get("packet_closed") is True,
            "selected_values_open": packet_status.get("selected_values_open") is True,
            "source_level_support_broad": packet_status.get("source_level_support_broad") is True,
            "all_required_fields_selected": all_selected,
            "first_missing_selected_fields": packet_status.get("first_missing_selected_fields", []),
        },
        "decision": {
            "finite_algebra_is_not_blocker": selection.get("finite_algebra_is_not_blocker")
            is True,
            "same_source_operator_packet_required": selection.get(
                "same_source_operator_packet_required"
            )
            is True,
            "selected_matter_slot_charge_closed": selection.get(
                "selected_matter_slot_charge_closed"
            )
            is True,
            "selected_overlap_normalization_closed": selection.get(
                "selected_overlap_normalization_closed"
            )
            is True,
            "same_source_packet_values_emitted": all_selected,
            "promote_conditional_A_to_A_selected": False,
            "emit_b_selected": False,
            "target_fitting_used": False,
            "full_SM_or_no_knob_closure": False,
        },
        "sm_same_source_obstruction": same_source_obstruction,
    }


def build_certificate() -> dict[str, Any]:
    q79 = {name: load(path) for name, path in Q79_INPUTS.items()}
    sm = {name: load(path) for name, path in SM_INPUTS.items()}
    reduction = build_reduction(q79, sm)
    decision = reduction["decision"]
    closure_claimed = (
        decision["selected_matter_slot_charge_closed"]
        and decision["selected_overlap_normalization_closed"]
        and decision["same_source_packet_values_emitted"]
    )
    cert = {
        "certificate": "Q79SelectedMatterSlotChargeAndOverlapNormalizationReduction",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "q79_input_statuses": {name: status_record(path) for name, path in Q79_INPUTS.items()},
        "sm_input_statuses": {name: status_record(path) for name, path in SM_INPUTS.items()},
        "matter_slot_overlap_reduction": reduction,
        "closed_by_this_attempt": {
            "finite_su5_transversality_imported": reduction["proved_imported_support"][
                "finite_su5_transversality_under_source_hypothesis_closed"
            ],
            "matter_slot_charge_sublemmas_identified": True,
            "overlap_normalization_sublemmas_identified": True,
            "same_source_packet_contract_imported": True,
            "support_vs_selected_counts_recorded": True,
            "target_fitting_excluded": True,
        },
        "still_open": {
            "fill_same_source_packet_values": not decision["same_source_packet_values_emitted"],
            "prove_selected_matter_slot_charge": not decision[
                "selected_matter_slot_charge_closed"
            ],
            "prove_selected_1M_neutrino_rule": True,
            "emit_selected_DE_dotD_Riesz_Green": True,
            "emit_selected_overlap_transfer_functor": True,
            "emit_selected_normalization_and_b_selected": True,
            "emit_selected_A_selected_and_b_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "uses_locked_target_columns_as_selector": False,
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_selected_matter_slot_charge": False,
            "claims_selected_overlap_normalization": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79SelectedMatterSlotChargeAndOverlapNormalizationReductionTheorem",
            "proved": True,
            "closure_claimed": closure_claimed,
            "statement": (
                "The q79 selected matter-slot charge and overlap-normalization theorem "
                "is reduced to a single same-source operator packet.  Finite SU(5) "
                "transversality, source-level qutrit Weyl support, and conditional "
                "C1 routing/normalization are available, but selected matter-slot "
                "charge, the 1_M Dirac-neutrino routing rule, selected D_E/dotD/Riesz/"
                "Green values, the selected overlap transfer functor, selected "
                "normalization, and primitive contractions are not emitted by one "
                "same-source packet yet."
            ),
        },
        "closure_claimed": closure_claimed,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return cert


def render_bool_map(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def render_fields(fields: dict[str, Any]) -> str:
    lines = []
    for name, row in fields.items():
        lines.append(
            "- `{name}`: support=`{support}`, selected=`{selected}`, required={required}".format(
                name=name,
                support=row.get("current_support"),
                selected=row.get("selected_emitted"),
                required=row.get("required"),
            )
        )
    return "\n".join(lines)


def render_list(items: list[Any]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- none"


def build_paper(cert: dict[str, Any]) -> str:
    reduction = cert["matter_slot_overlap_reduction"]
    support = reduction["proved_imported_support"]
    charge = reduction["matter_slot_charge"]
    overlap = reduction["overlap_normalization"]
    packet = reduction["same_source_operator_packet"]
    decision = reduction["decision"]
    return f"""# Q79 Selected MatterSlot Charge and Overlap Normalization Theorem v1

## Result

This theorem attempt is **reduced, not closed**.

The finite and structural pieces are no longer the blocker: q79/F has the
source-level Weyl carrier, the conditional C1 transfer is exact, SU(5)/E6 gives
the correct `10_M={{u,e}}` versus non-`10_M`/singlet `{{d,nuD}}` partition, and
finite SU(5) transversality gives the expected `U_10=I_3`, `U_bar5=F` packet
under the selected-source hypothesis.

The missing object is now one same-source operator packet that emits the matter
slot charge, `1_M` neutrino rule, operator values, overlap functor,
normalization, and primitive contractions together.

## Imported Support

{render_bool_map(support)}

## Matter-Slot Charge

{render_bool_map(charge)}

## Overlap Normalization

{render_bool_map(overlap)}

## Same-Source Operator Packet

- contract status: `{packet["contract_status"]}`
- field counts: `{packet["field_counts"]}`
- packet closed: `{packet["packet_closed"]}`
- selected values open: `{packet["selected_values_open"]}`
- first missing selected fields:

{render_list(packet["first_missing_selected_fields"])}

Required fields:

{render_fields(packet["required_fields"])}

## Decision

{render_bool_map(decision)}

## What This Closes

{render_bool_map(cert["closed_by_this_attempt"])}

## What Remains Open

{render_bool_map(cert["still_open"])}

## Theorem

`{cert["theorem"]["name"]}` is proved as a reduction theorem.

{cert["theorem"]["statement"]}

Next required artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    cert = build_certificate()
    write_json(OUT_TABLE, cert["matter_slot_overlap_reduction"])
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")
    print("Q79 selected matter-slot charge and overlap normalization theorem")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
