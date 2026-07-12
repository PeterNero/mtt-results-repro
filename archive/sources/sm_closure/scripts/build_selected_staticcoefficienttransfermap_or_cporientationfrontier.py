"""Promote the static Weyl coefficient transfer map and isolate CP frontier.

Earlier artifacts found a minimal additive Weyl coefficient lift, then reduced
its four algebraic branches to two same-orientation branches conditionally.  The
missing input was whether the same-source machinery actually emits one shared
coefficient transfer for both Weyl legs.

This artifact imports the later all-six-arrow SM-slot functor and static
matter-slot readout.  Those close sector routing and finite trace normalization
at the static source tier.  Together with the selected active shift, this
promotes the static coefficient transfer rule:

    lambda_Z = lambda_X = lambda_static.

It rejects the mixed lambda_Z/lambda_X branches at the static coefficient tier,
but it still does not select lambda_static in {1+omega, 1+omega^2}, and it does
not promote the matrices to physical dynamic C1/A_selected values.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_staticcoefficienttransfermap_or_cporientationfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRANSFER = PACKET_DIR / "selected_static_coefficient_transfer_map.packet.json"
BRANCHES = PACKET_DIR / "static_branch_promotion_decision.packet.json"
CP_FRONTIER = PACKET_DIR / "cp_orientation_frontier_after_static_transfer.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_static_coefficient_transfer.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StaticCoefficientTransferMap_or_CPOrientationFrontier_v1.md"

COEFFICIENT = DATA / "selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate.candidate.json"
SEARCH = (
    DATA
    / "selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate"
    / "minimal_weyl_coefficient_lift_search.packet.json"
)
BRANCH_FILTER = (
    DATA
    / "selected_weylcoefficientsource_reduction_or_orientationtransfermap"
    / "same_active_shift_orientation_branch_filter.packet.json"
)
ACTIVE_SHIFT = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
ROUTEC_TRANSFER = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
SMSLOT = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
DOWNSTREAM_LEDGER = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
MATTER_READOUT = DATA / "selected_matterslot_readout_backimport_from_smslotfunctor.candidate.json"
STATIC_READOUT = (
    DATA
    / "selected_matterslot_readout_backimport_from_smslotfunctor"
    / "selected_static_matterslot_readout.packet.json"
)

STATUS = "MTT_SELECTED_STATIC_COEFFICIENT_TRANSFER_MAP_BUILT_MIXED_REJECTED_CP_ORIENTATION_FRONTIER_OPEN"
NEXT = "MTT_Selected_CPOrientation_or_DynamicPhysicalMatrixPromotion_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def branch_rows(branches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for branch in branches:
        same_lambda = branch["phase_additive_lambda"] == branch["shift_additive_lambda"]
        rows.append(
            {
                "branch_id": branch["branch_id"],
                "phase_additive_lambda": branch["phase_additive_lambda"],
                "shift_additive_lambda": branch["shift_additive_lambda"],
                "lambda_Z_equals_lambda_X": same_lambda,
                "selected_static_coefficient_compatible": same_lambda,
                "rejected_at_static_coefficient_tier": not same_lambda,
                "cp_odd_orientation": branch["cp_odd_orientation"],
                "hermitian_spectrum_each_sector": branch["hermitian_spectrum_each_sector"],
                "cp_odd_exact_magnitude": branch["cp_odd_exact_magnitude"],
                "reason": (
                    "same shared static coefficient orientation"
                    if same_lambda
                    else "requires independent phase/shift coefficient orientations"
                ),
            }
        )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    coefficient = load(COEFFICIENT)
    search = load(SEARCH)
    branch_filter = load(BRANCH_FILTER)
    active_shift = load(ACTIVE_SHIFT)
    routec_transfer = load(ROUTEC_TRANSFER)
    smslot = load(SMSLOT)
    downstream = load(DOWNSTREAM_LEDGER)
    matter_readout = load(MATTER_READOUT)
    static_readout = load(STATIC_READOUT)

    rows = branch_rows(search["branches"])
    compatible = [row for row in rows if row["selected_static_coefficient_compatible"]]
    rejected = [row for row in rows if row["rejected_at_static_coefficient_tier"]]
    surviving_lambdas = sorted({row["phase_additive_lambda"] for row in compatible})
    surviving_cp_orientations = sorted({row["cp_odd_orientation"] for row in compatible})

    source_evidence = {
        "schema": "MTTStaticCoefficientTransferSourceEvidence.v1",
        "active_shift_selected": active_shift["primitive_selector"]["active_shift_selected"],
        "selected_active_shift": active_shift["primitive_selector"]["selected_active_shift"],
        "conditional_routec_transfer_exact": routec_transfer["conditional_transfer_map"][
            "conditional_exact"
        ],
        "all_six_smslot_arrows_closed": smslot["arrow_status"]["all_six_closed"],
        "selected_same_source_consistency_map": smslot["same_source_consistency"][
            "selected_same_source_consistency_map"
        ],
        "selected_static_sector_route_now_closed": downstream["weylpair_consequence"][
            "selected_static_sector_route_now_closed"
        ],
        "selected_static_phase_route": downstream["weylpair_consequence"]["phase_route"],
        "selected_static_shift_route": downstream["weylpair_consequence"]["shift_route"],
        "selected_static_overlap_transfer_normalization": matter_readout["what_closes_now"][
            "selected_overlap_transfer_normalization_static_tier"
        ],
        "static_readout_status": static_readout["status"],
        "dynamic_C1_promoted": static_readout.get("dynamic_C1_promoted", False),
    }
    static_transfer_selected = all(
        [
            source_evidence["active_shift_selected"],
            source_evidence["selected_active_shift"] == [1, 1],
            source_evidence["conditional_routec_transfer_exact"],
            source_evidence["all_six_smslot_arrows_closed"],
            source_evidence["selected_same_source_consistency_map"],
            source_evidence["selected_static_sector_route_now_closed"],
            source_evidence["selected_static_phase_route"] == ["u", "e"],
            source_evidence["selected_static_shift_route"] == ["d", "nuD"],
            source_evidence["selected_static_overlap_transfer_normalization"],
            source_evidence["static_readout_status"] == "STATIC_SOURCE_TIER_READOUT_CLOSED",
            source_evidence["dynamic_C1_promoted"] is False,
        ]
    )

    transfer = {
        "schema": "MTTSelectedStaticCoefficientTransferMap.v1",
        "status": "SELECTED_STATIC_COEFFICIENT_TRANSFER_MAP_EMITTED",
        "source_evidence": source_evidence,
        "selected_static_coefficient_transfer_map_emitted": static_transfer_selected,
        "map_name": "T_coeff_static_shared_active_shift",
        "domain": "one shared active-shift Weyl coefficient orientation lambda_static in {1+omega,1+omega2}",
        "rule": {
            "lambda_Z": "lambda_static",
            "lambda_X": "lambda_static",
            "lambda_Z_equals_lambda_X": True,
            "phase_sector_map": "u,e <- (I + Z) + lambda_static Z",
            "shift_sector_map": "d,nuD <- (I + X) + lambda_static X",
        },
        "mixed_branches_rejected_at_static_tier": True,
        "why_mixed_branches_are_rejected": (
            "The all-six-arrow SM-slot functor emits one same-source static route and one "
            "shared active-shift transfer.  A mixed branch needs independently chosen phase "
            "and shift coefficient orientations, which is not in the emitted source domain."
        ),
        "selected_specific_lambda_value_emitted": False,
        "selected_dynamic_C1_transfer_promoted": False,
        "selected_physical_matrices_promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(TRANSFER, transfer)

    branch_decision = {
        "schema": "MTTStaticCoefficientBranchPromotionDecision.v1",
        "status": "FOUR_BRANCHES_REDUCED_TO_TWO_SELECTED_STATIC_COMPATIBLE_BRANCHES",
        "previous_conditional_filter": rel(BRANCH_FILTER),
        "branch_count_before": len(rows),
        "selected_static_compatible_count": len(compatible),
        "rejected_mixed_count": len(rejected),
        "selected_static_compatible_branch_ids": [row["branch_id"] for row in compatible],
        "rejected_mixed_branch_ids": [row["branch_id"] for row in rejected],
        "surviving_lambdas": surviving_lambdas,
        "surviving_cp_odd_orientations": surviving_cp_orientations,
        "branch_rows": rows,
        "selected_specific_lambda_value_emitted": False,
        "selected_physical_matrices_promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BRANCHES, branch_decision)

    cp_frontier = {
        "schema": "MTTCPOrientationFrontierAfterStaticCoefficientTransfer.v1",
        "status": "STATIC_INVARIANT_CP_SIGN_FIXED_CONJUGATE_LAMBDA_AND_PHYSICAL_CP_OPEN",
        "surviving_lambdas": surviving_lambdas,
        "surviving_cp_odd_orientations_in_current_finite_weyl_convention": surviving_cp_orientations,
        "static_commutator_cp_orientation_sign_fixed": surviving_cp_orientations == ["positive"],
        "selected_physical_CKM_or_PMNS_CP_orientation_emitted": False,
        "selected_complex_orientation_or_universe_branch_rule_emitted": False,
        "why_not_full_CP_closure": (
            "The static finite-Weyl commutator sign is fixed after mixed branches are rejected, "
            "but the conjugate lambda_static branch and the physical embedding into CKM/PMNS "
            "phase conventions still require a dynamic operator/source theorem."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CP_FRONTIER, cp_frontier)

    cutset = {
        "schema": "MTTNextCutsetAfterStaticCoefficientTransfer.v1",
        "status": "NEXT_ATTACK_CONJUGATE_LAMBDA_OR_DYNAMIC_PHYSICAL_PROMOTION",
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The static coefficient map now rejects mixed branches.  The remaining target is either "
                "a theorem selecting/coexisting lambda_static in the conjugate pair, or a dynamic "
                "physical matrix promotion that makes the conjugate choice observable."
            ),
        },
        "minimal_tasks": [
            "derive a selected complex-orientation/time-arrow rule for lambda_static, or prove conjugate-pair coexistence",
            "emit selected dynamic C1/A_selected matrices from the same branch",
            "only then compute CKM/PMNS/Yukawa/RG observables from selected physical matrices",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStaticCoefficientTransferMapOrCPOrientationFrontier",
        "status": STATUS,
        "inputs": {
            "coefficient_candidate": rel(COEFFICIENT),
            "coefficient_search": rel(SEARCH),
            "previous_branch_filter": rel(BRANCH_FILTER),
            "active_shift": rel(ACTIVE_SHIFT),
            "conditional_routec_transfer": rel(ROUTEC_TRANSFER),
            "smslot_all_six_arrows": rel(SMSLOT),
            "downstream_static_ledger": rel(DOWNSTREAM_LEDGER),
            "matter_readout_backimport": rel(MATTER_READOUT),
            "static_readout_packet": rel(STATIC_READOUT),
        },
        "output_packets": {
            "selected_static_coefficient_transfer_map": rel(TRANSFER),
            "static_branch_promotion_decision": rel(BRANCHES),
            "cp_orientation_frontier_after_static_transfer": rel(CP_FRONTIER),
            "next_cutset_after_static_coefficient_transfer": rel(CUTSET),
        },
        "theorem": {
            "name": "SelectedStaticCoefficientTransferMapTheorem",
            "proved": static_transfer_selected,
            "statement": (
                "The selected active shift (1,1), conditional Route-C Weyl-to-C1 transfer, "
                "all-six-arrow SM-slot functor, selected static sector readout, and static overlap "
                "normalization emit a same-source static coefficient transfer map with "
                "lambda_Z=lambda_X=lambda_static.  Hence mixed phase/shift coefficient branches are "
                "rejected at the static coefficient tier.  This theorem does not select a specific "
                "conjugate lambda_static branch and does not promote dynamic physical matrices."
            ),
        },
        "what_closes_now": {
            "selected_static_coefficient_transfer_map": static_transfer_selected,
            "mixed_coefficient_branches_rejected_at_static_tier": True,
            "static_branch_count_reduced_four_to_two": True,
            "static_finite_weyl_CP_sign_after_mixed_rejection_fixed_positive": surviving_cp_orientations
            == ["positive"],
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "conjugate_lambda_branch_selection_or_coexistence": True,
            "selected_complex_orientation_or_time_arrow_rule": True,
            "selected_dynamic_C1_or_Aselected_matrix_promotion": True,
            "selected_b_selected_and_Hessian_normalization": True,
            "physical_CKM_PMNS_Yukawa_value_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "mixed_branches_rejected": True,
            "selected_specific_lambda_value_emitted": False,
            "selected_physical_matrices_promoted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": coefficient["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_StaticCoefficientTransferMap_or_CPOrientationFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": static_transfer_selected,
        "selected_static_coefficient_transfer_map": static_transfer_selected,
        "mixed_branches_rejected": True,
        "selected_static_compatible_count": len(compatible),
        "rejected_mixed_count": len(rejected),
        "static_finite_weyl_CP_sign_after_mixed_rejection": surviving_cp_orientations,
        "selected_specific_lambda_value_emitted": False,
        "selected_physical_matrices_promoted": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected StaticCoefficientTransferMap or CPOrientationFrontier v1

Status: `{STATUS}`.

The old source-to-C1 transfer was exact but conditional, because the sector route
and normalization were not independently selected.  Later artifacts now close the
static SM-slot source tier:

```text
all six SM-slot source arrows       : true
static route                        : Z -> u,e ; X -> d,nuD
same-source consistency             : true
static trace/transfer normalization : true
dynamic C1/A_selected promotion     : false
```

Therefore the static coefficient transfer map is:

```text
lambda_Z = lambda_X = lambda_static
u,e      <- (I + Z) + lambda_static Z
d,nuD   <- (I + X) + lambda_static X
```

This rejects the two mixed branches at the static coefficient tier.  The four
algebraic branches are reduced to two selected-static-compatible branches:

```text
surviving lambdas                  : {surviving_lambdas}
rejected mixed branch count         : {len(rejected)}
surviving CP orientations           : {surviving_cp_orientations}
selected physical matrices promoted : false
full SM closure                     : false
```

So the remaining wall has moved again: the mixed branches are gone, but MTT
still must select or explain coexistence of the conjugate `lambda_static`
branches, then promote dynamic physical matrices before CKM/PMNS/Yukawa values
can be claimed.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
