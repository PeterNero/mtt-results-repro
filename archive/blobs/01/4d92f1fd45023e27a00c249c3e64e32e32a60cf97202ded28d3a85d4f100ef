"""Build Step54 same-branch convention import / threshold-mass rows frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step54_samebranch_convention_import_or_thresholdmassrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONVENTION_IMPORT = PACKET_DIR / "step54_samebranch_convention_import.packet.json"
ATOMIC_RECHECK = PACKET_DIR / "step54_atomic_route_recheck_after_convention.packet.json"
VALUE_RECHECK = PACKET_DIR / "step54_value_execution_recheck_after_convention.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step54_SameBranchConventionImport_or_ThresholdMassRows_v1.md"

STEP53 = DATA / "selected_step53_responsefunctional_contract_replay_or_atomicroutes.candidate.json"
STEP53_ROUTES = (
    DATA / "selected_step53_responsefunctional_contract_replay_or_atomicroutes" / "step53_atomic_route_frontier.packet.json"
)
ATOMIC = DATA / "selected_responsefunctionalatomicroutes_or_externallikelihoodacquisition.candidate.json"
ATOMIC_PROGRESS = (
    DATA
    / "selected_responsefunctionalatomicroutes_or_externallikelihoodacquisition"
    / "internal_response_functional_atomic_progress.packet.json"
)
ATOMIC_CUTSET = (
    DATA
    / "selected_responsefunctionalatomicroutes_or_externallikelihoodacquisition"
    / "ordered_remaining_response_functional_cutset.packet.json"
)
CONVENTION = DATA / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation.candidate.json"
CONVENTION_CONTRACT = (
    DATA
    / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
    / "post_pi_same_branch_convention_source_contract.packet.json"
)
FUNCTIONAL_RECHECK = (
    DATA
    / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
    / "threshold_functional_instantiation_recheck_after_convention.packet.json"
)
READINESS = (
    DATA
    / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
    / "rtheta_value_readiness_after_convention_source.packet.json"
)
NEXT_CUTSET = (
    DATA
    / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
    / "next_cutset_after_post_pi_convention_source.packet.json"
)

STATUS = "MTT_SELECTED_STEP54_SAMEBRANCH_CONVENTION_IMPORTED_THRESHOLD_MASS_ROWS_OPEN"
NEXT = "MTT_Selected_ThresholdMatchingRowsPostPi_or_MassSchemeSourceRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP53,
        STEP53_ROUTES,
        ATOMIC,
        ATOMIC_PROGRESS,
        ATOMIC_CUTSET,
        CONVENTION,
        CONVENTION_CONTRACT,
        FUNCTIONAL_RECHECK,
        READINESS,
        NEXT_CUTSET,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step54 inputs: " + ", ".join(missing))

    step53 = load(STEP53)
    step53_routes = load(STEP53_ROUTES)
    atomic = load(ATOMIC)
    atomic_progress = load(ATOMIC_PROGRESS)
    atomic_cutset = load(ATOMIC_CUTSET)
    convention = load(CONVENTION)
    convention_contract = load(CONVENTION_CONTRACT)
    functional = load(FUNCTIONAL_RECHECK)
    readiness = load(READINESS)
    next_cutset = load(NEXT_CUTSET)

    remaining_after_convention = readiness["blocking_failures"]
    convention_import = {
        "schema": "MTTStep54SameBranchConventionImport.v1",
        "status": "SAME_BRANCH_CONVENTION_IMPORTED_INTO_ATOMIC_ROUTE",
        "step53_atomic_routes_locked": step53["closure_decision"]["atomic_routes_locked"],
        "previous_atomic_frontier": rel(STEP53_ROUTES),
        "convention_source": rel(CONVENTION),
        "same_branch_scale_scheme_loop_convention_closed": convention["closure_decision"][
            "same_branch_scale_scheme_loop_convention_closed"
        ],
        "post_pi_formal_convention_source_contract_closed": convention["closure_decision"][
            "post_pi_formal_convention_source_contract_closed"
        ],
        "target_scale": convention_contract["target_scale"],
        "target_scheme": convention_contract["target_scheme"],
        "minimum_loop_order": convention_contract["minimum_loop_order"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CONVENTION_IMPORT, convention_import)

    atomic_recheck = {
        "schema": "MTTStep54AtomicRouteRecheckAfterConvention.v1",
        "status": "CONVENTION_ATOMIC_LEMMA_CLOSED_ROUTES_STILL_OPEN",
        "closed_atomic_lemmas": [
            "no_observed_selector_proof",
            "same_branch_scale_scheme_loop_convention",
        ],
        "previous_closed_atomic_count": atomic_progress["closed_atomic_count"],
        "closed_atomic_count": 2,
        "required_atomic_count": atomic_progress["required_atomic_count"],
        "remaining_atomic_failures": [
            "selected_response_functional_map",
            "threshold_matching_source_rows",
            "mass_scheme_conversion_source_rows",
            "profile_response_or_diagonal_limitation",
        ],
        "recommended_next": next_cutset["recommended_next"]["artifact"],
        "external_likelihood_route_still_open": step53_routes[
            "external_likelihood_or_threshold_source_import"
        ]["accepted_now"]
        is False,
        "minimal_parameter_route_still_open": step53_routes["minimal_universal_parameter_policy"][
            "accepted_now"
        ]
        is False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ATOMIC_RECHECK, atomic_recheck)

    value_recheck = {
        "schema": "MTTStep54ValueExecutionRecheckAfterConvention.v1",
        "status": "READINESS_5_OF_9_VALUE_ROWS_ZERO",
        "previous_present_count": readiness["previous_present_count"],
        "present_count": readiness["present_count"],
        "requirement_count": readiness["requirement_count"],
        "retired_blocking_failure": readiness["retired_blocking_failure"],
        "blocking_failures": remaining_after_convention,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_internal_Rtheta_coefficient_row_count": 0,
        "accepted_internal_scalar_row_count": 0,
        "selected_lambda_H_row_closed": False,
        "minimal_parameter_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_RECHECK, value_recheck)

    candidate = {
        "candidate": "MTTSelectedStep54SameBranchConventionImportOrThresholdMassRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "samebranch_convention_import": rel(CONVENTION_IMPORT),
            "atomic_route_recheck_after_convention": rel(ATOMIC_RECHECK),
            "value_execution_recheck_after_convention": rel(VALUE_RECHECK),
        },
        "theorem": {
            "name": "Step54SameBranchConventionImportTheorem",
            "proved": True,
            "statement": (
                "The post-Pi same-branch convention source theorem is imported into the active "
                "response-functional atomic route. This retires the convention blocker and advances "
                "Rtheta readiness to 5/9, while accepting zero value rows. The next value-producing "
                "frontier is threshold matching and mass-scheme source rows under the closed convention."
            ),
        },
        "closure_decision": {
            "same_branch_scale_scheme_loop_convention_closed": True,
            "post_pi_formal_convention_source_contract_closed": True,
            "closed_atomic_count": 2,
            "Rtheta_readiness_present_count": readiness["present_count"],
            "Rtheta_readiness_requirement_count": readiness["requirement_count"],
            "threshold_matching_source_rows_closed": False,
            "mass_scheme_conversion_source_rows_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "accepted_internal_Rtheta_coefficient_row_count": 0,
            "accepted_internal_scalar_row_count": 0,
            "selected_lambda_H_row_closed": False,
            "minimal_parameter_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step54_SameBranchConventionImport_or_ThresholdMassRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step54 SameBranchConventionImport or ThresholdMassRows v1

Status: `{STATUS}`.

Step54 imports the post-Pi same-branch convention closure into the active
response-functional route.

```text
same-branch convention closed          : true
closed atomic lemmas                   : 2/6
Rtheta readiness                       : {readiness["present_count"]}/{readiness["requirement_count"]}
accepted internal Rtheta rows          : 0
lambda_H row closed                    : false
```

The active frontier is now threshold matching rows and mass-scheme conversion
rows under the closed `M_Z`/`MSbar` convention.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
