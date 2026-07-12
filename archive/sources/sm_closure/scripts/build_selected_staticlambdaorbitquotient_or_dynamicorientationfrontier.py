"""Build the static lambda-orbit quotient / dynamic orientation frontier.

After the selected static coefficient transfer map, the mixed branches are
rejected and only two representatives remain:

    lambda_static in {1+omega, 1+omega2}.

This artifact records the strongest honest statement available from the current
selected static source data: the static coefficient tier selects the two-element
orbit/quotient, not an individual representative.  The two representatives have
the same static invariant signature in the emitted packets, but the source does
not emit a complex-orientation/time-arrow rule that chooses one, and dynamic
physical matrix promotion is still open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_staticlambdaorbitquotient_or_dynamicorientationfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ORBIT = PACKET_DIR / "selected_static_lambda_orbit.packet.json"
NO_SELECTOR = PACKET_DIR / "static_representative_no_selector.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_static_lambda_orbit.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StaticLambdaOrbitQuotient_or_DynamicOrientationFrontier_v1.md"

STATIC_COEFF = DATA / "selected_staticcoefficienttransfermap_or_cporientationfrontier.candidate.json"
STATIC_TRANSFER = (
    DATA
    / "selected_staticcoefficienttransfermap_or_cporientationfrontier"
    / "selected_static_coefficient_transfer_map.packet.json"
)
STATIC_BRANCHES = (
    DATA
    / "selected_staticcoefficienttransfermap_or_cporientationfrontier"
    / "static_branch_promotion_decision.packet.json"
)
CP_FRONTIER = (
    DATA
    / "selected_staticcoefficienttransfermap_or_cporientationfrontier"
    / "cp_orientation_frontier_after_static_transfer.packet.json"
)
SEARCH = (
    DATA
    / "selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate"
    / "minimal_weyl_coefficient_lift_search.packet.json"
)

STATUS = "MTT_SELECTED_STATIC_LAMBDA_ORBIT_QUOTIENT_BUILT_REPRESENTATIVE_SELECTION_OPEN"
NEXT = "MTT_Selected_DynamicOrientation_or_PhysicalMatrixPromotion_v1"


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

    static_coeff = load(STATIC_COEFF)
    static_transfer = load(STATIC_TRANSFER)
    static_branches = load(STATIC_BRANCHES)
    cp_frontier = load(CP_FRONTIER)
    search = load(SEARCH)
    search_by_id = {branch["branch_id"]: branch for branch in search["branches"]}

    survivor_ids = static_branches["selected_static_compatible_branch_ids"]
    survivor_rows = []
    for branch_id in survivor_ids:
        branch = search_by_id[branch_id]
        survivor_rows.append(
            {
                "branch_id": branch_id,
                "lambda_static": branch["phase_additive_lambda"],
                "u_e_matrix_formula": branch["u_e_matrix_formula"],
                "d_nuD_matrix_formula": branch["d_nuD_matrix_formula"],
                "hermitian_spectrum_each_sector": branch["hermitian_spectrum_each_sector"],
                "commutator_norm_sq": branch["commutator_norm_sq"],
                "cp_odd_exact_magnitude": branch["cp_odd_exact_magnitude"],
                "cp_odd_orientation": branch["cp_odd_orientation"],
            }
        )

    invariant_keys = [
        "hermitian_spectrum_each_sector",
        "commutator_norm_sq",
        "cp_odd_exact_magnitude",
        "cp_odd_orientation",
    ]
    first_signature = {key: survivor_rows[0][key] for key in invariant_keys}
    static_signature_identical = all(
        {key: row[key] for key in invariant_keys} == first_signature for row in survivor_rows
    )
    formulas_identical = (
        survivor_rows[0]["u_e_matrix_formula"] == survivor_rows[1]["u_e_matrix_formula"]
        and survivor_rows[0]["d_nuD_matrix_formula"] == survivor_rows[1]["d_nuD_matrix_formula"]
    )

    orbit = {
        "schema": "MTTSelectedStaticLambdaOrbit.v1",
        "status": "STATIC_SOURCE_SELECTS_TWO_ELEMENT_LAMBDA_ORBIT_NOT_REPRESENTATIVE",
        "selected_static_lambda_orbit": static_branches["surviving_lambdas"],
        "survivor_branch_ids": survivor_ids,
        "survivor_rows": survivor_rows,
        "static_invariant_signature": first_signature,
        "static_invariant_signature_identical_across_survivors": static_signature_identical,
        "matrix_formulas_identical_across_survivors": formulas_identical,
        "interpretation": (
            "At the selected static coefficient tier, the emitted observables depend only on the "
            "two-element lambda orbit.  The representatives differ as matrix formulas, but no "
            "selected static source field chooses one representative."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ORBIT, orbit)

    no_selector = {
        "schema": "MTTStaticLambdaRepresentativeNoSelector.v1",
        "status": "NO_STATIC_REPRESENTATIVE_SELECTOR_EMITTED",
        "checks": {
            "selected_static_transfer_rule_emitted": static_transfer[
                "selected_static_coefficient_transfer_map_emitted"
            ],
            "selected_specific_lambda_value_emitted": static_transfer[
                "selected_specific_lambda_value_emitted"
            ],
            "selected_complex_orientation_or_universe_branch_rule_emitted": cp_frontier[
                "selected_complex_orientation_or_universe_branch_rule_emitted"
            ],
            "selected_physical_CKM_or_PMNS_CP_orientation_emitted": cp_frontier[
                "selected_physical_CKM_or_PMNS_CP_orientation_emitted"
            ],
            "selected_physical_matrices_promoted": static_coeff["closure_decision"][
                "selected_physical_matrices_promoted"
            ],
        },
        "current_static_decision": (
            "Use the selected orbit {1+omega,1+omega2} as the static coefficient quotient. "
            "Do not choose a representative until a dynamic orientation/source theorem emits one."
        ),
        "physical_coexistence_claimed": False,
        "individual_universe_branch_selected": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NO_SELECTOR, no_selector)

    cutset = {
        "schema": "MTTNextCutsetAfterStaticLambdaOrbit.v1",
        "status": "NEXT_ATTACK_DYNAMIC_ORIENTATION_OR_PHYSICAL_MATRIX_PROMOTION",
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The static quotient is now well-defined.  Further progress needs either a "
                "selected dynamic orientation/time-arrow theorem or a physical matrix promotion "
                "showing whether the two representatives are equivalent, coexist, or one is selected."
            ),
        },
        "minimal_tasks": [
            "derive a selected complex-orientation/time-arrow rule from the same source",
            "or promote dynamic physical matrices for both representatives and quotient by physical equivalence",
            "then compute CKM/PMNS/Yukawa values only from the promoted physical branch or quotient",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStaticLambdaOrbitQuotientOrDynamicOrientationFrontier",
        "status": STATUS,
        "inputs": {
            "static_coefficient_transfer_candidate": rel(STATIC_COEFF),
            "selected_static_coefficient_transfer_map": rel(STATIC_TRANSFER),
            "static_branch_promotion_decision": rel(STATIC_BRANCHES),
            "cp_orientation_frontier_after_static_transfer": rel(CP_FRONTIER),
            "minimal_weyl_coefficient_lift_search": rel(SEARCH),
        },
        "output_packets": {
            "selected_static_lambda_orbit": rel(ORBIT),
            "static_representative_no_selector": rel(NO_SELECTOR),
            "next_cutset_after_static_lambda_orbit": rel(CUTSET),
        },
        "theorem": {
            "name": "SelectedStaticLambdaOrbitQuotientTheorem",
            "proved": static_signature_identical
            and static_transfer["selected_specific_lambda_value_emitted"] is False
            and cp_frontier["selected_complex_orientation_or_universe_branch_rule_emitted"] is False,
            "statement": (
                "After mixed branches are rejected, the selected static coefficient tier selects the "
                "two-element lambda orbit {1+omega,1+omega2}.  The emitted static invariant signature "
                "is identical on the two representatives, while no selected static source emits a "
                "complex-orientation or time-arrow representative selector.  Therefore the correct "
                "static object is the orbit/quotient, not an individual lambda value.  Physical "
                "coexistence or representative selection remains a dynamic-source question."
            ),
        },
        "what_closes_now": {
            "selected_static_lambda_orbit_quotient": True,
            "representative_selection_not_required_at_static_tier": True,
            "static_invariant_signature_exhausted_for_survivors": static_signature_identical,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "individual_lambda_representative_selection": True,
            "physical_coexistence_or_equivalence_of_representatives": True,
            "selected_dynamic_orientation_or_time_arrow_rule": True,
            "selected_dynamic_C1_or_Aselected_matrix_promotion": True,
            "physical_CKM_PMNS_Yukawa_value_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "static_lambda_orbit_selected": True,
            "individual_lambda_value_selected": False,
            "physical_coexistence_claimed": False,
            "selected_physical_matrices_promoted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": static_coeff["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_StaticLambdaOrbitQuotient_or_DynamicOrientationFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": candidate["theorem"]["proved"],
        "selected_static_lambda_orbit_quotient": True,
        "selected_static_lambda_orbit": static_branches["surviving_lambdas"],
        "static_invariant_signature_identical_across_survivors": static_signature_identical,
        "individual_lambda_value_selected": False,
        "physical_coexistence_claimed": False,
        "selected_physical_matrices_promoted": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected StaticLambdaOrbitQuotient or DynamicOrientationFrontier v1

Status: `{STATUS}`.

After selected static coefficient transfer, the mixed branches are rejected.
The surviving static coefficient representatives are:

```text
lambda_static orbit : {static_branches["surviving_lambdas"]}
survivor branches   : {survivor_ids}
static signature identical : {str(static_signature_identical).lower()}
matrix formulas identical  : {str(formulas_identical).lower()}
individual lambda selected : false
physical coexistence claimed : false
full SM closure : false
```

The selected static source data therefore chooses the orbit/quotient
`{{1+omega,1+omega2}}`, not either representative.  That is the correct object
to carry forward at the static tier.  A representative can be selected only by a
new dynamic orientation/time-arrow theorem, or by promoted physical matrices
that prove equivalence, coexistence, or selection.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
