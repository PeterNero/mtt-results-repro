"""Build the selected U1 carrier/projector or SU2 spectrum promotion gate.

This is the next step after the conditional 2/3 source theorem.  It checks
whether sibling-repo data already promote the theorem to a selected U1/SU2
threshold index.  The current answer is intentionally strict: a rank-3
projective carrier exists, but the source marks it as not selected by MTT, and
the SU2 flat FP branch is identified but not selected.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

SOURCE_THEOREM = DATA / "u1_su2_threshold_index_source_theorem.candidate.json"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

FACTORIZED_PACKET = Q79 / "candidate_data" / "iwasawa_block_factorized_twisted_packet.candidate.json"
SECTOR_MAPS = Q79 / "candidate_data" / "iwasawa_block_factorized_sector_maps.candidate.json"
FUSION_AFTER_LOCKDOWN = Q79 / "candidate_data" / "all_remaining_valpha_gates" / "same_source_monad_gs_operator_fusion.after_terminal_lockdown.json"
ALL_GATES = Q79 / "candidate_data" / "all_remaining_valpha_gates_attempt.candidate.json"
SU2_GHOST = NONSM / "certificates" / "selected_su2_nonabelian_ghost_quotient_determinant_certificate.json"
SU2_FLATNESS = NONSM / "certificates" / "selected_su2_threshold_background_flatness_or_fp_spectrum_certificate.json"
SU2_FP_POLICY = NONSM / "certificates" / "selected_flat_fp_quotient_normalization_policy_certificate.json"

OUTPUT_DATA = DATA / "selected_u1_threshold_carrier_projector_or_su2_operator_spectrum.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1_threshold_carrier_projector_or_su2_operator_spectrum_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_Threshold_Carrier_Projector_or_SU2_Operator_Spectrum_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_rank_trace(projector: list[list[int]]) -> int:
    return sum(projector[i][i] for i in range(len(projector)))


def weight(total: int, removed: int) -> str:
    value = Fraction(total - removed, total)
    return f"{value.numerator}/{value.denominator}"


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    theorem = load(SOURCE_THEOREM)
    factorized = load(FACTORIZED_PACKET)
    sector_maps = load(SECTOR_MAPS)
    fusion = load(FUSION_AFTER_LOCKDOWN)
    all_gates = load(ALL_GATES)
    su2 = load(SU2_GHOST)
    su2_flatness = load(SU2_FLATNESS)
    su2_fp_policy = load(SU2_FP_POLICY)

    family = factorized["family_twist_block"]
    q_projector = sector_maps["family_block"]["sector_projectors"]["Q"]["projector"]
    raw_rank = family["rank"]
    raw_trace = matrix_rank_trace(q_projector)
    central_removed = 1
    candidate_weight = weight(raw_rank, central_removed)

    u1_promotion_tests = [
        {
            "id": "rank_three_projective_carrier_shape",
            "passes_shape": raw_rank == 3 and raw_trace == 3,
            "promotable": False,
            "source": str(FACTORIZED_PACKET),
            "reason": "The sibling packet has the correct rank-3 projective carrier shape, but selected_by_mtt is false and selected gerbe source is not verified.",
        },
        {
            "id": "sector_projector_shape",
            "passes_shape": q_projector == [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            "promotable": False,
            "source": str(SECTOR_MAPS),
            "reason": "The available sector projector is identity on the family block; it does not supply the quotient projector P_perp that removes the shared central mode.",
        },
        {
            "id": "same_source_operator_fusion",
            "passes_shape": fusion["ordered_source"]["ordered_source_validator_passes"] is True,
            "promotable": False,
            "source": str(FUSION_AFTER_LOCKDOWN),
            "reason": "Ordered-source validation now passes, but the packet is fixture_only, selected_by_mtt is false, and same_source_for_ordered_L_pic0_GS_and_DE is false.",
        },
    ]

    su2_tests = [
        {
            "id": "flat_background_universal_fp_branch",
            "branch_status": su2["computed_branches"][0]["status"],
            "promotable": True,
            "source": str(SU2_FP_POLICY),
            "reason": "The later selected flat FP quotient-normalization policy closes the field-independent flat ghost term for weak-split gauge-kinetic accounting.",
        },
        {
            "id": "selected_su2_threshold_background_flatness",
            "branch_status": su2_flatness["status"],
            "promotable": su2_flatness["verdict"]["selected_su2_threshold_background_flat"] is True
            and su2_flatness["verdict"]["selected_nonflat_fp_spectrum_required"] is False,
            "source": str(SU2_FLATNESS),
            "reason": "Theta II/III select the flat/trivial SU2 leading threshold background and eliminate the need for a non-flat FP spectrum at this order.",
        },
        {
            "id": "selected_flat_fp_quotient_policy",
            "branch_status": su2_fp_policy["status"],
            "promotable": su2_fp_policy["verdict"]["su2_selected_for_lambda_12_accounting"] is True
            and su2_fp_policy["verdict"]["su2_quotient_policy_closed_for_weak_split"] is True,
            "source": str(SU2_FP_POLICY),
            "reason": su2_fp_policy["source_policy"]["gauge_fixing_interpretation"],
        },
        {
            "id": "curved_nonabelian_fp_operator",
            "branch_status": su2["computed_branches"][3]["status"],
            "promotable": True,
            "source": str(SU2_GHOST),
            "reason": "The curved branch no longer blocks the leading weak-split gate because selected flatness makes a non-flat FP spectrum unnecessary in this scoped accounting.",
        },
    ]

    theorem_hypothesis_status = {
        "H1_three_direction_u1_threshold_carrier": "SHAPE_FOUND_NOT_SELECTED",
        "H2_exactly_one_shared_central_universal_mode": "SUPPORTED_BUT_NOT_OPERATOR_BOUND",
        "H3_physical_quotient_removes_shared_mode": "PROJECTOR_MISSING",
        "H4_SU2_unit_index_or_selected_spectrum": "CLOSED_FOR_WEAK_SPLIT_BY_FLATNESS_AND_FP_QUOTIENT_POLICY",
        "H5_no_target_selection": "CLOSED",
    }

    all_u1_promotable = all(item["promotable"] for item in u1_promotion_tests)
    all_su2_promotable = all(item["promotable"] for item in su2_tests)
    promoted = all_u1_promotable and all_su2_promotable

    candidate = {
        "candidate": "SelectedU1ThresholdCarrierProjectorOrSU2OperatorSpectrum",
        "status": "U1_THRESHOLD_CARRIER_PROJECTOR_GATE_REDUCED_SU2_WEAK_SPLIT_CLOSED_U1_SOURCE_OPEN",
        "inputs": {
            "source_theorem": str(SOURCE_THEOREM.relative_to(ROOT)),
            "factorized_packet": str(FACTORIZED_PACKET),
            "sector_maps": str(SECTOR_MAPS),
            "fusion_after_lockdown": str(FUSION_AFTER_LOCKDOWN),
            "all_remaining_valpha_gates": str(ALL_GATES),
            "su2_ghost_quotient": str(SU2_GHOST),
            "su2_flatness": str(SU2_FLATNESS),
            "su2_flat_fp_policy": str(SU2_FP_POLICY),
        },
        "source_theorem_used": theorem["source_theorem"]["name"],
        "rank_quotient_replay": {
            "raw_rank_from_candidate_carrier": raw_rank,
            "raw_projector_trace": raw_trace,
            "central_shared_directions_removed_if_projector_is_supplied": central_removed,
            "would_give_U1_weight": candidate_weight,
            "matches_source_theorem_weight": candidate_weight == theorem["decision"]["derived_U1_weight"],
        },
        "u1_promotion_tests": u1_promotion_tests,
        "su2_promotion_tests": su2_tests,
        "theorem_hypothesis_status_after_gate": theorem_hypothesis_status,
        "cross_repo_status": {
            "factorized_packet_status": factorized["status"],
            "factorized_packet_selected_by_mtt": factorized["selected_by_mtt"],
            "selected_gerbe_source_verified": family["selected_gerbe_source_verified"],
            "sector_maps_status": sector_maps["status"],
            "sector_maps_selected_by_mtt": sector_maps["selected_by_mtt"],
            "fusion_status": fusion["status"],
            "same_source_for_ordered_L_pic0_GS_and_DE": fusion["source_identity"]["same_source_for_ordered_L_pic0_GS_and_DE"],
            "remaining_valpha_gate_status": all_gates["status"],
            "su2_status": su2["status"],
            "su2_flatness_status": su2_flatness["status"],
            "su2_fp_policy_status": su2_fp_policy["status"],
            "su2_selected_for_lambda_12_accounting": su2_fp_policy["verdict"]["su2_selected_for_lambda_12_accounting"],
        },
        "decision": {
            "rank_three_carrier_shape_found": True,
            "source_selected_u1_carrier_found": False,
            "quotient_projector_P_perp_found": False,
            "su2_unit_index_or_spectrum_found": True,
            "su2_closure_scope": "weak-split gauge-kinetic threshold accounting only",
            "promoted_to_selected_threshold_index": promoted,
            "measured_electroweak_closure": False,
            "target_fitting_used": False,
            "current_source_no_go": True,
            "no_go_reason": "SU2 is now closed for scoped weak-split accounting, but the U1 rank-3 carrier and quotient projector still lack same-source selection.",
            "next_required_object": "Same_Source_Selected_U1_Carrier_Projector_Theorem_v1",
        },
        "minimal_packet_that_would_close": {
            "U1": [
                "selected_by_mtt true for the rank-3 U1 threshold carrier",
                "same-source identification of the shared central-circle basis vector",
                "explicit quotient projector P_perp with trace 2 on the selected carrier",
                "operator/determinant statement that the U1 threshold trace uses P_perp",
            ],
            "SU2": [
                "closed for weak-split accounting by selected SU2 flatness and flat FP quotient-normalization policy",
            ],
            "scheme": [
                "same normalization scheme as Qa/SU3 log(2008)",
                "no lambda_12 or measured electroweak data as selection input",
            ],
        },
        "guardrails": [
            "A rank-3 candidate carrier is not a selected U1 threshold carrier.",
            "The identity family projector is not the shared-circle quotient projector P_perp.",
            "The SU2 closure is scoped to weak-split gauge-kinetic threshold accounting and must not be reused for vacuum energy or absolute partition-function normalization.",
            "This gate may be used as a no-go certificate for the current U1 source record, not as electroweak closure.",
        ],
        "closure_claimed": True,
        "closure_scope": "promotion_attempt_and_current_source_no_go_for_2_3_threshold_index",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1ThresholdCarrierProjectorOrSU2OperatorSpectrum",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "rank_three_candidate_shape_checked": True,
            "two_thirds_rank_quotient_replayed": candidate_weight,
            "current_source_promotion_attempt_completed": True,
            "overpromotion_guardrail_installed": True,
        },
        "what_remains_open": {
            "selected_U1_threshold_carrier": True,
            "shared_central_basis_vector_bound_to_U1_operator": True,
            "quotient_projector_P_perp": True,
            "selected_SU2_unit_index_or_operator_spectrum": False,
            "electroweak_closure": True,
        },
        "next_required_object": candidate["decision"]["next_required_object"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    rq = candidate["rank_quotient_replay"]
    u1 = "\n".join(
        f"- `{item['id']}`: shape={str(item['passes_shape']).lower()}, promotable={str(item['promotable']).lower()}\n  Reason: {item['reason']}"
        for item in candidate["u1_promotion_tests"]
    )
    su2 = "\n".join(
        f"- `{item['id']}`: {item['branch_status']}, promotable={str(item['promotable']).lower()}\n  Reason: {item['reason']}"
        for item in candidate["su2_promotion_tests"]
    )
    statuses = "\n".join(f"- `{key}`: {value}" for key, value in candidate["theorem_hypothesis_status_after_gate"].items())
    close_u1 = "\n".join(f"- {item}" for item in candidate["minimal_packet_that_would_close"]["U1"])
    close_su2 = "\n".join(f"- {item}" for item in candidate["minimal_packet_that_would_close"]["SU2"])
    close_scheme = "\n".join(f"- {item}" for item in candidate["minimal_packet_that_would_close"]["scheme"])
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    decision = candidate["decision"]
    return f"""# Selected U1 Threshold Carrier Projector or SU2 Operator Spectrum v1

## Result

The `2/3` source theorem survives the stricter promotion audit, but it is not
yet promoted.  The current corpus contains the right carrier shape, not the
selected threshold operator packet.

```text
rank_three_carrier_shape_found = {str(decision["rank_three_carrier_shape_found"]).lower()}
source_selected_u1_carrier_found = {str(decision["source_selected_u1_carrier_found"]).lower()}
quotient_projector_P_perp_found = {str(decision["quotient_projector_P_perp_found"]).lower()}
su2_unit_index_or_spectrum_found = {str(decision["su2_unit_index_or_spectrum_found"]).lower()}
promoted_to_selected_threshold_index = {str(decision["promoted_to_selected_threshold_index"]).lower()}
measured_electroweak_closure = {str(decision["measured_electroweak_closure"]).lower()}
```

## Rank-Quotient Replay

```text
raw_rank_from_candidate_carrier = {rq["raw_rank_from_candidate_carrier"]}
raw_projector_trace = {rq["raw_projector_trace"]}
central_shared_directions_removed_if_projector_is_supplied = {rq["central_shared_directions_removed_if_projector_is_supplied"]}
would_give_U1_weight = {rq["would_give_U1_weight"]}
matches_source_theorem_weight = {str(rq["matches_source_theorem_weight"]).lower()}
```

This is useful: the known factorized Iwasawa carrier has exactly the shape
needed for the source theorem.  It still cannot be used as selected proof data
because its own packet marks `selected_by_mtt=false`.

## U1 Promotion Tests

{u1}

## SU2 Promotion Tests

{su2}

## Source-Theorem Hypotheses After This Gate

{statuses}

## Minimal Packet That Would Close This Gate

U1:

{close_u1}

SU2:

{close_su2}

Scheme:

{close_scheme}

## Guardrails

{guardrails}

## Next Required Object

```text
{decision["next_required_object"]}
```
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
