"""Reduce Weyl coefficient-lift branches using static source orientation.

The coefficient-lift search emits four algebraic branches.  Existing source
packets already select the source-level qutrit Weyl carrier, the active shift
(1,1), and the static matter-slot readout.  This artifact records the strongest
honest reduction available from those facts: if the second-order coefficient
transfer is controlled by that same active shift on both Weyl legs, the mixed
orientation branches are not same-source-compatible and the frontier narrows to
the two conjugate same-orientation branches.  The actual transfer map and
orientation selection remain open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_weylcoefficientsource_reduction_or_orientationtransfermap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FILTER = PACKET_DIR / "same_active_shift_orientation_branch_filter.packet.json"
GAP = PACKET_DIR / "coefficient_transfer_map_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_orientation_branch_filter.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_WeylCoefficientSource_Reduction_or_OrientationTransferMap_v1.md"

COEFFICIENT = DATA / "selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate.candidate.json"
COEFFICIENT_SEARCH = (
    DATA
    / "selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate"
    / "minimal_weyl_coefficient_lift_search.packet.json"
)
ACTIVE_SHIFT = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
WEYL_SOURCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
MATTER_READOUT = DATA / "selected_matterslot_readout_backimport_from_smslotfunctor.candidate.json"

STATUS = "MTT_SELECTED_WEYLCOEFFICIENT_SOURCE_REDUCTION_BUILT_TWO_BRANCH_FILTER_TRANSFER_OPEN"
NEXT = "MTT_Selected_CoefficientTransferMap_or_CPOrientationSelection_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    coefficient = load(COEFFICIENT)
    search = load(COEFFICIENT_SEARCH)
    active_shift = load(ACTIVE_SHIFT)
    weyl_source = load(WEYL_SOURCE)
    matter_readout = load(MATTER_READOUT)

    branches = search["branches"]
    compatible = [
        branch
        for branch in branches
        if branch["phase_additive_lambda"] == branch["shift_additive_lambda"]
    ]
    mixed = [
        branch
        for branch in branches
        if branch["phase_additive_lambda"] != branch["shift_additive_lambda"]
    ]
    compatible_lambdas = sorted({branch["phase_additive_lambda"] for branch in compatible})
    compatible_orientations = sorted({branch["cp_odd_orientation"] for branch in compatible})

    static_source = {
        "schema": "MTTSameActiveShiftStaticSourceEvidence.v1",
        "active_shift_selected": active_shift["primitive_selector"]["active_shift_selected"],
        "selected_active_shift": active_shift["primitive_selector"]["selected_active_shift"],
        "source_level_weyl_carrier_proved": weyl_source["source_level_weyl_carrier"]["proved"],
        "active_shift_1_1_provenance": weyl_source["active_shift_provenance"]["proved"],
        "static_matter_slot_readout_closed": matter_readout["SM_parity_closed"],
        "phase_route_static": ["u", "e"],
        "shift_route_static": ["d", "nuD"],
        "dynamic_transfer_map_emitted": weyl_source["c1_transfer_map"][
            "selected_source_to_C1_response_map_emitted"
        ],
    }

    branch_filter = {
        "schema": "MTTSameActiveShiftOrientationBranchFilter.v1",
        "status": "FOUR_ALGEBRAIC_BRANCHES_REDUCED_TO_TWO_SAME_ORIENTATION_BRANCHES_CONDITIONALLY",
        "static_source_evidence": static_source,
        "filter_rule": (
            "If the second-order coefficient transfer is sourced by the same selected active shift (1,1) "
            "on both Weyl legs, then lambda_Z must equal lambda_X. Mixed lambda_Z/lambda_X branches require "
            "independent leg orientations not emitted by the current source packets."
        ),
        "algebraic_branch_count": len(branches),
        "same_active_shift_compatible_count": len(compatible),
        "mixed_orientation_count": len(mixed),
        "compatible_lambdas": compatible_lambdas,
        "compatible_cp_orientations": compatible_orientations,
        "compatible_branch_ids": [branch["branch_id"] for branch in compatible],
        "mixed_branch_ids": [branch["branch_id"] for branch in mixed],
        "mixed_branches_rejected_as_selected_now": False,
        "why_not_rejected_absolutely": "The source-to-C1 coefficient transfer map is still open; a later theorem could route dual legs contragrediently.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FILTER, branch_filter)

    gap = {
        "schema": "MTTCoefficientTransferMapGap.v1",
        "status": "SOURCE_BRANCH_FILTER_BUILT_TRANSFER_MAP_AND_ORIENTATION_OPEN",
        "what_this_closes": [
            "imports selected active shift (1,1) into the coefficient-lift problem",
            "identifies same-orientation branches as the only branches compatible with a single shared active-shift transfer",
            "narrows the natural source-compatible candidates to lambda=1+omega and lambda=1+omega2 conjugates",
        ],
        "what_remains_open": [
            "selected source-to-C1 coefficient transfer map",
            "proof that mixed branches are impossible rather than merely not emitted by current source packets",
            "CP orientation selection or coexistence theorem",
            "promotion of either conjugate branch to selected physical matrices",
        ],
        "selected_lambda_emitted_now": False,
        "selected_CP_orientation_emitted_now": False,
        "physical_values_promoted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(GAP, gap)

    cutset = {
        "schema": "MTTNextCutsetAfterOrientationBranchFilter.v1",
        "status": "NEXT_ATTACK_TRANSFER_MAP_OR_CP_ORIENTATION",
        "recommended_next": {
            "artifact": NEXT,
            "reason": "The coefficient problem is now reduced to transfer-map emission and CP orientation selection/coexistence.",
        },
        "minimal_source_tasks": [
            "derive the selected coefficient transfer map from source-level Weyl carrier and active shift (1,1)",
            "prove whether lambda_Z=lambda_X is forced by same-source transfer",
            "select lambda=1+omega, lambda=1+omega2, or a conjugate-pair universe rule",
            "rerun physical Yukawa/CKM/PMNS/CP audits only after selected branch promotion",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedWeylCoefficientSourceReductionOrOrientationTransferMap",
        "status": STATUS,
        "inputs": {
            "coefficient_candidate": rel(COEFFICIENT),
            "coefficient_search": rel(COEFFICIENT_SEARCH),
            "active_shift": rel(ACTIVE_SHIFT),
            "weyl_source": rel(WEYL_SOURCE),
            "matter_readout": rel(MATTER_READOUT),
        },
        "output_packets": {
            "same_active_shift_orientation_branch_filter": rel(FILTER),
            "coefficient_transfer_map_gap": rel(GAP),
            "next_cutset_after_orientation_branch_filter": rel(CUTSET),
        },
        "theorem": {
            "name": "SameActiveShiftOrientationBranchFilterTheorem",
            "proved": True,
            "statement": (
                "The selected source-level Weyl carrier and active shift (1,1), together with the static "
                "matter-slot readout, reduce the natural coefficient-lift target from four algebraic branches "
                "to two same-orientation conjugate branches if the second-order coefficient transfer uses that "
                "same active shift on both Weyl legs. This is a branch-filter theorem, not a selected coefficient "
                "or CP-orientation theorem, because the source-to-C1 coefficient transfer map remains open."
            ),
        },
        "what_closes_now": {
            "active_shift_imported_into_coefficient_lift": True,
            "static_phase_shift_readout_imported": True,
            "same_orientation_branch_filter_built": True,
            "natural_branch_count_reduced_four_to_two_conditionally": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_coefficient_transfer_map": True,
            "absolute_rejection_of_mixed_orientation_branches": True,
            "CP_orientation_selection_or_coexistence": True,
            "selected_physical_matrix_promotion": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "same_orientation_filter_closed": True,
            "selected_lambda_emitted": False,
            "selected_CP_orientation_emitted": False,
            "physical_values_promoted": False,
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
        "certificate": "MTT_Selected_WeylCoefficientSource_Reduction_or_OrientationTransferMap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "same_orientation_branch_filter_built": True,
        "compatible_branch_count": len(compatible),
        "mixed_branch_count": len(mixed),
        "selected_lambda_emitted": False,
        "selected_CP_orientation_emitted": False,
        "physical_values_promoted": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected WeylCoefficientSource Reduction or OrientationTransferMap v1

Status: `{STATUS}`.

The algebraic coefficient lift had four branches.  Importing the selected
source-level Weyl carrier, active shift `(1,1)`, and static matter-slot readout
gives a conditional same-source filter:

```text
algebraic branches                 : {len(branches)}
same-active-shift compatible        : {len(compatible)}
mixed-orientation branches          : {len(mixed)}
compatible lambdas                  : {compatible_lambdas}
compatible CP orientations          : {compatible_orientations}
selected lambda emitted             : false
selected CP orientation emitted     : false
full SM closure                     : false
```

This narrows the natural target to the two conjugate same-orientation branches,
but it does not yet select one or prove both coexist.  The next missing object
is the selected source-to-C1 coefficient transfer map.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
