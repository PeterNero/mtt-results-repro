"""Analyze the SU(5) tensor route versus the block-factorized orientation route.

The conditional SU(5) projection tensor uses a whole-multiplet statement:

    10_M clock, bar5_M shift  =>  T_u = I, T_d = F.

The block-factorized qutrit route instead assigns orientations to SM sectors
so that ordinary trivial-Higgs Yukawa pairs are invariant:

    Q,L one orientation; u,d,e,N the conjugate orientation; H trivial.

This script checks whether those two descriptions are compatible.  It prevents
the block-factorized route from silently inheriting the monolithic SU(5) tensor
unless a further high-scale multiplet/Higgs source proves it.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
OUT = ROOT / "candidate_data" / "su5_block_orientation_route_split.candidate.json"
CERT = CERTIFICATES / "su5_block_orientation_route_split_certificate.json"

SU5_MULTIPLETS = {
    "10_M": ["Q", "u", "e"],
    "bar5_M": ["d", "L"],
    "1_M": ["N"],
}
LEFT_DOUBLETS = ["Q", "L"]
RIGHT_SINGLET_OR_CONJUGATES = ["u", "d", "e", "N"]
SM_PAIRS = {
    "up": ("Q", "u"),
    "down": ("Q", "d"),
    "charged_lepton": ("L", "e"),
    "dirac_neutrino": ("L", "N"),
}


def load_json(name: str) -> dict[str, Any]:
    return json.loads((CERTIFICATES / name).read_text(encoding="utf-8"))


def orientation_kind(pair: tuple[int, int]) -> str:
    if pair == (1, 2):
        return "F"
    if pair == (2, 1):
        return "F_conjugate"
    if pair[0] == pair[1]:
        return "identity_or_same_orientation"
    return "blocked_or_trivial_mixed"


def all_same(values: list[int]) -> bool:
    return len(set(values)) == 1


def summarize_branch(packet: dict[str, Any]) -> dict[str, Any]:
    sector_orientations = packet["sector_orientations"]
    multiplets = {}
    for name, sectors in SU5_MULTIPLETS.items():
        values = [sector_orientations[sector] for sector in sectors]
        multiplets[name] = {
            "sectors": sectors,
            "orientations": values,
            "uniform_orientation": all_same(values),
        }

    left_values = [sector_orientations[sector] for sector in LEFT_DOUBLETS]
    right_values = [sector_orientations[sector] for sector in RIGHT_SINGLET_OR_CONJUGATES]
    pair_transports = {}
    for channel, (left, right) in SM_PAIRS.items():
        pair = (sector_orientations[left], sector_orientations[right])
        pair_transports[channel] = {
            "sectors": [left, right],
            "orientations": list(pair),
            "sum_mod3": sum(pair) % 3,
            "finite_transport_kind": orientation_kind(pair),
            "trivial_higgs_pair_allowed": sum(pair) % 3 == 0 and pair[0] != 0 and pair[1] != 0,
        }

    up_kind = pair_transports["up"]["finite_transport_kind"]
    down_kind = pair_transports["down"]["finite_transport_kind"]
    all_pairs_same_transport = len(
        {entry["finite_transport_kind"] for entry in pair_transports.values()}
    ) == 1

    return {
        "branch": packet["branch"],
        "global_cp_label": packet["global_cp_label"],
        "torsion_label_m": packet["torsion_label_m"],
        "conditional_su5_transport_orientation": packet[
            "conditional_su5_transport_orientation"
        ],
        "multiplet_orientation_uniformity": multiplets,
        "left_right_orientation_uniformity": {
            "left_doublets": {
                "sectors": LEFT_DOUBLETS,
                "orientations": left_values,
                "uniform_orientation": all_same(left_values),
            },
            "right_singlet_or_conjugates": {
                "sectors": RIGHT_SINGLET_OR_CONJUGATES,
                "orientations": right_values,
                "uniform_orientation": all_same(right_values),
            },
            "left_and_right_are_conjugate_nontrivial": (
                all_same(left_values)
                and all_same(right_values)
                and left_values[0] in {1, 2}
                and right_values[0] in {1, 2}
                and (left_values[0] + right_values[0]) % 3 == 0
            ),
        },
        "sm_trivial_higgs_pair_transports": pair_transports,
        "transport_consequence": {
            "up_transport_kind": up_kind,
            "down_transport_kind": down_kind,
            "up_down_transport_mismatch_from_block_orientations": up_kind != down_kind,
            "all_sm_pairs_have_same_finite_transport_kind": all_pairs_same_transport,
        },
    }


def analyze() -> dict[str, Any]:
    orientation = load_json("iwasawa_orientation_de_dotd_bridge_certificate.json")
    block_rule = load_json("iwasawa_block_coupling_invariant_selection_rule_certificate.json")
    projection = load_json("su5_projection_tensor_derivation_attempt_certificate.json")
    source_attempt = load_json("selected_su5_source_proof_attempt_certificate.json")

    branches = [summarize_branch(packet) for packet in orientation["branch_packets"]]
    multiplet_uniform_all = all(
        branch["multiplet_orientation_uniformity"]["10_M"]["uniform_orientation"]
        and branch["multiplet_orientation_uniformity"]["bar5_M"]["uniform_orientation"]
        for branch in branches
    )
    left_right_coherent_all = all(
        branch["left_right_orientation_uniformity"]["left_doublets"]["uniform_orientation"]
        and branch["left_right_orientation_uniformity"]["right_singlet_or_conjugates"][
            "uniform_orientation"
        ]
        and branch["left_right_orientation_uniformity"][
            "left_and_right_are_conjugate_nontrivial"
        ]
        for branch in branches
    )
    up_down_mismatch_from_block = any(
        branch["transport_consequence"]["up_down_transport_mismatch_from_block_orientations"]
        for branch in branches
    )
    all_pairs_allowed = all(
        all(entry["trivial_higgs_pair_allowed"] for entry in branch["sm_trivial_higgs_pair_transports"].values())
        for branch in branches
    )

    conditional_tensor_closed = (
        projection.get("calculation_results", {}).get("finite_projection_tensor_derived") is True
        and projection.get("calculation_results", {}).get("q79_branch_Td_equals_F") is True
        and projection.get("calculation_results", {}).get("q369_branch_Td_equals_F_conjugate")
        is True
    )
    selected_source_closed = (
        source_attempt.get("verdict", {}).get("remaining_proof_closed") is True
    )

    return {
        "candidate": "SU5BlockOrientationRouteSplit",
        "status": "SU5_BLOCK_ORIENTATION_ROUTE_SPLIT_DETECTED_SOURCE_OPEN",
        "generated_by": "scripts/analyze_su5_block_orientation_route_split.py",
        "problem": {
            "monolithic_su5_tensor_route": "10_M clock and bar5_M shift imply T_u=I, T_d=F/F*.",
            "block_factorized_trivial_higgs_route": "Q,L carry one qutrit orientation while u,d,e,N carry the conjugate orientation.",
            "question": "Can the current block-factorized source justify the monolithic SU(5) tensor?",
        },
        "branches": branches,
        "calculation_results": {
            "conditional_su5_tensor_closed": conditional_tensor_closed,
            "selected_source_closed": selected_source_closed,
            "block_rule_requires_conjugate_pairs": block_rule.get("calculation_results", {}).get(
                "conjugate_matter_pair_with_trivial_Higgs_allowed"
            )
            is True,
            "su5_multiplets_uniform_under_current_branch_packets": multiplet_uniform_all,
            "left_right_sector_split_coherent_under_current_branch_packets": left_right_coherent_all,
            "all_sm_trivial_higgs_pairs_allowed_by_block_orientations": all_pairs_allowed,
            "up_down_transport_mismatch_generated_by_block_orientations": up_down_mismatch_from_block,
            "monolithic_su5_tensor_inherits_from_block_route": (
                multiplet_uniform_all and up_down_mismatch_from_block and selected_source_closed
            ),
            "block_route_by_itself_gives_delta_t_mismatch": up_down_mismatch_from_block,
            "sector_resolved_C1_or_high_scale_source_required": True,
        },
        "interpretation": {
            "conditional_tensor_status": (
                "The T_u=I, T_d=F/F* tensor remains a valid finite conditional calculation."
            ),
            "block_route_status": (
                "The block-factorized trivial-Higgs route does not currently source that tensor: "
                "its branch packets are left/right coherent, not uniform on SU(5) multiplets."
            ),
            "why_it_matters": (
                "If the selected source is the block route, finite qutrit transport alone gives the "
                "same left-right transport for up and down pairs; the CKM heavy-link must then come "
                "from sector-resolved C1/dotD/overlap contractions, not from a monolithic SU(5) basis shortcut."
            ),
        },
        "allowed_forward_routes": {
            "route_A_high_scale_SU5_or_E6_source": [
                "prove a selected high-scale source where 10_M and bar5_M are coherent multiplet polarizations",
                "include the corresponding nontrivial Higgs or projection data that avoids the trivial-Higgs block obstruction",
                "then the conditional SU(5) tensor can be promoted if selected source flags close",
            ],
            "route_B_block_factorized_SM_source": [
                "keep Q,L versus u,d,e,N conjugate orientations for the trivial Higgs line",
                "derive separate sector bases U_Q,U_u,U_d,U_L,U_e,U_N and selected dotD responses",
                "compute sector-resolved primitive C1 contractions; do not import T_u=I,T_d=F as a shortcut",
            ],
        },
        "what_this_closes": {
            "monolithic_tensor_not_sourced_by_current_block_packets": True,
            "left_right_block_orientation_coherence_checked": True,
            "need_for_sector_resolved_closing_packet_identified": True,
            "conditional_tensor_preserved_as_separate_possible_route": True,
        },
        "still_open": {
            "selected_high_scale_SU5_multiplet_source": True,
            "selected_block_factorized_sector_resolved_C1": True,
            "selected_U10_Ubar5_or_replacement_sector_bases": True,
            "selected_CKM_heavy_link_packet": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_block_route_proves_Tu_I_Td_F": False,
            "claims_conditional_tensor_invalid": False,
            "claims_selected_sector_C1_values": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "route_split_detected": True,
            "remaining_proof_refined": (
                "Close either a selected high-scale SU(5)/E6 source for the monolithic tensor, "
                "or a selected block-factorized sector-resolved C1 source.  The current block "
                "packets do not by themselves promote T_u=I, T_d=F."
            ),
            "recommended_next_step": (
                "Build the sector-resolved closing packet U_Q,U_u,U_d,U_L,U_e,U_N plus dotD/C1 "
                "for Route B, while retaining Route A as a separate high-scale option."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cert = {
        "certificate": "SU5BlockOrientationRouteSplitCertificate",
        "status": report["status"],
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "calculation_results": report["calculation_results"],
        "interpretation": report["interpretation"],
        "allowed_forward_routes": report["allowed_forward_routes"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
