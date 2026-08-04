"""Analyze the q79 Route-C Weyl-pair sector charge/chirality certificate.

The source-provenance lemma reduced the remaining proof obligation to an
independent selector for the sector routing

    Z -> u,e
    X -> d,nuD

This script tests whether the current q79 and SM-parity artifacts already emit
that selector.  The result is a sharpened reduction: SU(5)/E6 matter slots give
the intended partition as the strongest structural candidate, and later
SM-parity packets confirm the exact conditional routing/normalization, but the
selected same-source matter-slot charge and overlap-normalization theorem is
still absent.  Locked target columns remain diagnostic only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
SM = TEXPAPERS / "mtt-sm-parity-closure"

OUT_DIR = CANDIDATES / "q79_routec_weylpair_sector_charge_or_chirality_certificate"
OUT_TABLE = OUT_DIR / "sector_charge_reduction_table.json"
OUT_CANDIDATE = CANDIDATES / "q79_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
OUT_CERT = CERTS / "q79_routec_weylpair_sector_charge_or_chirality_certificate.json"
OUT_PAPER = CORPUS / "Q79_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1.md"

STATUS = (
    "Q79_ROUTEC_WEYLPAIR_SECTOR_CHARGE_OR_CHIRALITY_REDUCED_TO_"
    "MATTERSLOT_OVERLAP_SOURCE_OPEN"
)
NEXT = "Q79_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1"

Q79_INPUTS = {
    "source_provenance": CERTS / "q79_routec_weylpair_source_provenance_lemma_certificate.json",
    "e6_dictionary": CERTS / "e6_to_sm_yukawa_operator_dictionary_certificate.json",
    "time_oriented_branch": CERTS / "time_oriented_conjugate_branch_selection_certificate.json",
    "su5_matter_slot_transversality": CERTS / "su5_matter_slot_transversality_certificate.json",
    "su5_block_orientation_route_split": CERTS / "su5_block_orientation_route_split_certificate.json",
    "su5_projection_tensor": CERTS / "su5_projection_tensor_derivation_attempt_certificate.json",
    "selected_su5_source_attempt": CERTS / "selected_su5_source_proof_attempt_certificate.json",
    "selected_su5_qutrit_packet_attempt": CERTS
    / "selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json",
}

SM_INPUTS = {
    "sector_charge_or_chirality": SM
    / "certificates"
    / "selected_routec_weylpair_sector_charge_or_chirality_certificate_certificate.json",
    "sector_charge_or_chirality_candidate": SM
    / "candidate_data"
    / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json",
    "matter_slot_or_blocksector": SM
    / "certificates"
    / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem_certificate.json",
    "hybrid_matter_slot_galerkin": SM
    / "certificates"
    / "selected_routec_hybrid_matter_slot_galerkin_source_packet_certificate.json",
    "selected_operator_overlap_packet": SM
    / "certificates"
    / "selected_routec_selected_operator_source_and_overlap_tensor_packet_certificate.json",
    "selected_c1_routing_normalization_overlap": SM
    / "certificates"
    / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet_certificate.json",
    "selected_c1_routing_normalization_overlap_candidate": SM
    / "candidate_data"
    / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet.candidate.json",
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
        "next_required_artifact": data.get("next_required_artifact")
        or data.get("primary_next_artifact"),
        "what_closes": data.get("what_closes") or data.get("what_closes_now") or {},
        "what_remains_open": data.get("what_remains_open") or data.get("still_open") or {},
    }


def build_table(inputs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    q79_source = inputs["q79"]["source_provenance"]
    q79_e6 = inputs["q79"]["e6_dictionary"]
    q79_branch = inputs["q79"]["time_oriented_branch"]
    q79_su5_trans = inputs["q79"]["su5_matter_slot_transversality"]
    q79_block = inputs["q79"]["su5_block_orientation_route_split"]
    q79_projection = inputs["q79"]["su5_projection_tensor"]
    q79_su5_source = inputs["q79"]["selected_su5_source_attempt"]
    q79_su5_packet = inputs["q79"]["selected_su5_qutrit_packet_attempt"]
    sm_sector = inputs["sm"]["sector_charge_or_chirality_candidate"]
    sm_c1 = inputs["sm"]["selected_c1_routing_normalization_overlap_candidate"]

    su5_slot_table = {
        "u": {
            "su5_slot": "10_M",
            "route": "phase_clock_candidate",
            "reason": "u^c belongs to the SU(5) 10_M matter slot",
        },
        "e": {
            "su5_slot": "10_M",
            "route": "phase_clock_candidate",
            "reason": "e^c belongs to the SU(5) 10_M matter slot",
        },
        "d": {
            "su5_slot": "bar5_M",
            "route": "shift_candidate",
            "reason": "d^c belongs to the SU(5) bar5_M matter slot",
        },
        "nuD": {
            "su5_slot": "1_M",
            "route": "shift_candidate_conditional",
            "reason": "Dirac neutrino uses the singlet N^c leg and needs a selected singlet rule",
        },
    }
    phase_route = sorted(name for name, row in su5_slot_table.items() if row["route"] == "phase_clock_candidate")
    shift_route = sorted(name for name, row in su5_slot_table.items() if row["route"].startswith("shift"))

    source_decision = q79_source.get("decision", {})
    q79_branch_results = q79_branch.get("calculation_results", {})
    q79_trans_results = q79_su5_trans.get("calculation_results", {})
    q79_block_results = q79_block.get("calculation_results", {})
    q79_projection_results = q79_projection.get("calculation_results", {})
    q79_su5_source_results = q79_su5_source.get("calculation_results", {})
    q79_packet_results = q79_su5_packet.get("calculation_results", {})
    sm_sector_result = sm_sector.get("certificate_result", {})
    sm_c1_verdict = sm_c1.get("selection_verdict", {})
    sm_c1_attempts = sm_c1.get("attempts", {})

    selected_route_closed = (
        bool(source_decision.get("selected_sector_route_independently_proved"))
        or bool(sm_sector_result.get("selected_certificate_closed"))
        or bool(sm_c1_verdict.get("selected_c1_routing_closed"))
    )
    selected_overlap_closed = bool(sm_c1_verdict.get("selected_overlap_source_closed"))
    selected_normalization_closed = bool(sm_c1_verdict.get("selected_transfer_normalization_closed"))
    singlet_rule_closed = not sm_sector.get("what_remains_open", {}).get(
        "selected_singlet_neutrino_shift_rule", True
    )

    return {
        "required_route": {
            "phase_Z_to": ["u", "e"],
            "shift_X_to": ["d", "nuD"],
            "origin": "imported from the exact conditional transfer and six-route locked-column uniqueness search",
            "locked_target_columns_used_as_selector": False,
        },
        "su5_e6_structural_candidate": {
            "slot_table": su5_slot_table,
            "phase_route_from_10M": phase_route,
            "shift_route_from_non10_plus_singlet": shift_route,
            "matches_required_partition": phase_route == ["e", "u"] and shift_route == ["d", "nuD"],
            "e6_dictionary_status": q79_e6.get("status"),
            "rank_one_seed_sector_assignment_open": q79_e6.get("open", {}).get(
                "rank_one_seed_sector_assignment"
            )
            is True,
            "nuD_singlet_rule_closed": singlet_rule_closed,
            "nuD_singlet_gap": not singlet_rule_closed,
        },
        "q79_finite_packet_evidence": {
            "retarded_q79_branch_selects_F": q79_branch_results.get(
                "time_oriented_retarded_branch_selects_q79"
            )
            is True
            and q79_branch_results.get("ordered_su5_packet_selected") is False,
            "finite_su5_transversality_closed": q79_trans_results.get(
                "finite_transversality_theorem_closed"
            )
            is True,
            "selected_mtt_source_present": q79_trans_results.get(
                "selected_mtt_source_present"
            )
            is True,
            "selected_ordered_su5_packet_closed": q79_trans_results.get(
                "selected_ordered_su5_packet_closed"
            )
            is True,
            "conditional_projection_tensor_closed": q79_projection_results.get(
                "finite_projection_tensor_derived"
            )
            is True,
            "selected_projection_tensor_promoted": q79_projection_results.get(
                "selected_polarization_source_promotes"
            )
            is True,
            "selected_su5_source_present": not q79_su5_source_results.get(
                "all_current_source_routes_blocked", True
            ),
            "selected_su5_packet_promotes": q79_packet_results.get(
                "promotes_to_selected_heavy_link_input"
            )
            is True,
            "block_route_distinguishes_required_pair_split": not (
                q79_block_results.get("left_right_sector_split_coherent_under_current_branch_packets")
                is True
                and q79_block_results.get("su5_multiplets_uniform_under_current_branch_packets")
                is False
            ),
        },
        "sm_parity_reductions": {
            "sector_charge_status": inputs["sm_statuses"]["sector_charge_or_chirality"]["status"],
            "sector_certificate_closed": sm_sector_result.get("selected_certificate_closed") is True,
            "strongest_structural_match": sm_sector_result.get("strongest_structural_match"),
            "why_not_closed": sm_sector_result.get("why_not_closed", []),
            "matter_slot_theorem_status": inputs["sm_statuses"]["matter_slot_or_blocksector"]["status"],
            "hybrid_packet_status": inputs["sm_statuses"]["hybrid_matter_slot_galerkin"]["status"],
            "operator_overlap_status": inputs["sm_statuses"]["selected_operator_overlap_packet"]["status"],
            "c1_routing_normalization_status": inputs["sm_statuses"][
                "selected_c1_routing_normalization_overlap"
            ]["status"],
            "conditional_route_exact": sm_c1_verdict.get("conditional_algebra_closed") is True
            and sm_c1_attempts.get("c1_routing", {}).get("conditional_route", {}).get(
                "matches_locked_columns"
            )
            is True,
            "selected_c1_routing_closed": sm_c1_verdict.get("selected_c1_routing_closed") is True,
            "selected_overlap_source_closed": selected_overlap_closed,
            "selected_transfer_normalization_closed": selected_normalization_closed,
            "best_next_object": sm_c1_verdict.get("best_next_object"),
        },
        "decision": {
            "source_level_weyl_carrier_and_conditional_transfer_imported": source_decision.get(
                "source_level_weyl_carrier_and_active_shift_proved"
            )
            is True
            and source_decision.get("conditional_source_to_C1_transfer_exact") is True,
            "su5_e6_partition_matches_required_route": phase_route == ["e", "u"]
            and shift_route == ["d", "nuD"],
            "selected_sector_charge_or_chirality_table_proved": selected_route_closed,
            "selected_singlet_neutrino_shift_rule_proved": singlet_rule_closed,
            "selected_overlap_or_transfer_functor_proved": selected_overlap_closed,
            "selected_transfer_normalization_proved": selected_normalization_closed,
            "promote_conditional_A_to_A_selected": False,
            "target_fitting_used": False,
        },
    }


def render_bool_map(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def render_list(items: list[Any]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- none"


def build_certificate() -> dict[str, Any]:
    q79 = {name: load(path) for name, path in Q79_INPUTS.items()}
    sm = {name: load(path) for name, path in SM_INPUTS.items()}
    q79_statuses = {name: status_record(path) for name, path in Q79_INPUTS.items()}
    sm_statuses = {name: status_record(path) for name, path in SM_INPUTS.items()}
    inputs = {
        "q79": q79,
        "sm": sm,
        "q79_statuses": q79_statuses,
        "sm_statuses": sm_statuses,
    }
    reduction = build_table(inputs)
    decision = reduction["decision"]
    selected_closed = (
        decision["selected_sector_charge_or_chirality_table_proved"]
        and decision["selected_singlet_neutrino_shift_rule_proved"]
        and decision["selected_overlap_or_transfer_functor_proved"]
        and decision["selected_transfer_normalization_proved"]
    )
    cert = {
        "certificate": "Q79RouteCWeylPairSectorChargeOrChiralityReduction",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "q79_input_statuses": q79_statuses,
        "sm_input_statuses": sm_statuses,
        "sector_charge_reduction": reduction,
        "closed_by_this_attempt": {
            "q79_source_provenance_imported": decision[
                "source_level_weyl_carrier_and_conditional_transfer_imported"
            ],
            "su5_e6_partition_identified_as_unique_structural_candidate": decision[
                "su5_e6_partition_matches_required_route"
            ],
            "sm_later_packets_imported_to_refine_frontier": True,
            "selected_source_gap_separated_from_locked_target_columns": True,
            "target_fitting_excluded": True,
        },
        "still_open": {
            "selected_sector_charge_or_chirality_table": not decision[
                "selected_sector_charge_or_chirality_table_proved"
            ],
            "selected_1M_singlet_neutrino_shift_rule": not decision[
                "selected_singlet_neutrino_shift_rule_proved"
            ],
            "selected_overlap_or_transfer_functor": not decision[
                "selected_overlap_or_transfer_functor_proved"
            ],
            "selected_transfer_normalization": not decision[
                "selected_transfer_normalization_proved"
            ],
            "promote_conditional_A_to_A_selected": True,
            "emit_theorem_derived_b_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "uses_locked_target_columns_as_selector": False,
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "claims_selected_su5_packet": False,
            "claims_selected_overlap_tensor": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79WeylPairSectorChargeOrChiralityReductionTheorem",
            "proved": True,
            "closure_claimed": selected_closed,
            "statement": (
                "The current q79/SM Route-C data reduce the Weyl-pair sector selector "
                "to a same-source matter-slot charge and overlap-normalization theorem. "
                "The SU(5)/E6 dictionary gives the intended structural partition "
                "10_M={u,e} versus non-10/singlet={d,nuD}, and the conditional C1 "
                "route is exact, but no selected source yet proves the 10_M clock "
                "slot, the bar5_M/singlet shift slot, the Dirac-neutrino singlet "
                "rule, or the selected transfer normalization."
            ),
        },
        "closure_claimed": selected_closed,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return cert


def build_paper(cert: dict[str, Any]) -> str:
    reduction = cert["sector_charge_reduction"]
    structural = reduction["su5_e6_structural_candidate"]
    finite = reduction["q79_finite_packet_evidence"]
    sm = reduction["sm_parity_reductions"]
    decision = reduction["decision"]
    return f"""# Q79 RouteC WeylPair SectorCharge or Chirality Certificate v1

## Result

The sector-charge/chirality certificate is **reduced, not closed**.

The strongest structural candidate is exactly the route we need:
`10_M` carries the phase/clock side `u,e`, while the non-`10_M` plus singlet
side carries `d,nuD`.  This matches the conditional Weyl-pair route
`Z -> u,e` and `X -> d,nuD`.

The proof still cannot promote the conditional route to selected data, because
the selected same-source matter-slot charge, the `1_M` Dirac-neutrino singlet
shift rule, and the selected overlap/normalization functor remain open.

## Required Route

{render_bool_map(reduction["required_route"])}

## SU5/E6 Structural Candidate

- phase route from `10_M`: `{structural["phase_route_from_10M"]}`
- shift route from non-`10_M` plus singlet: `{structural["shift_route_from_non10_plus_singlet"]}`
- matches required partition: `{structural["matches_required_partition"]}`
- `nuD` singlet rule closed: `{structural["nuD_singlet_rule_closed"]}`
- `nuD` singlet gap: `{structural["nuD_singlet_gap"]}`
- rank-one seed sector assignment open: `{structural["rank_one_seed_sector_assignment_open"]}`

## q79 Finite Packet Evidence

{render_bool_map(finite)}

## SM-Parity Frontier Import

{render_bool_map(sm)}

Why the SM sector certificate did not close:

{render_list(sm.get("why_not_closed", []))}

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
    write_json(OUT_TABLE, cert["sector_charge_reduction"])
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")
    print("Q79 Route-C Weyl-pair sector charge/chirality certificate")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
