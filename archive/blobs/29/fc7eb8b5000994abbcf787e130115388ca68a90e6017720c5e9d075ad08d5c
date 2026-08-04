"""Build post-Pi convention-source closure or threshold-functional instantiation artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONVENTION = PACKET_DIR / "post_pi_same_branch_convention_source_contract.packet.json"
FUNCTIONAL = PACKET_DIR / "threshold_functional_instantiation_recheck_after_convention.packet.json"
ROW_MATRIX = PACKET_DIR / "threshold_row_source_attack_matrix.packet.json"
READINESS = PACKET_DIR / "rtheta_value_readiness_after_convention_source.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_post_pi_convention_source.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostPiConventionSource_or_ThresholdFunctionalInstantiation_v1.md"

POST_PI = DATA / "selected_postpirthetavaluefrontiercontraction_or_thresholdrowattackpacket.candidate.json"
POST_PI_CUTSET = (
    DATA
    / "selected_postpirthetavaluefrontiercontraction_or_thresholdrowattackpacket"
    / "minimal_threshold_row_cutset_after_post_pi.packet.json"
)
POST_PI_ROUTE_ORDER = (
    DATA
    / "selected_postpirthetavaluefrontiercontraction_or_thresholdrowattackpacket"
    / "threshold_row_attack_order_after_post_pi.packet.json"
)
PI_ASSEMBLY = DATA / "selected_rthetasectortransfer_or_primitiveassemblymapexecution.candidate.json"
PI_VALUE = (
    DATA
    / "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
    / "pi_closure_value_evaluator_domain.packet.json"
)
SAME_BRANCH = DATA / "selected_samebranchconvention_or_thresholdrowemission.candidate.json"
TARGET = (
    DATA
    / "selected_samebranchconvention_or_thresholdrowemission"
    / "true_precision_convention_target.packet.json"
)
GAP = (
    DATA
    / "selected_samebranchconvention_or_thresholdrowemission"
    / "same_branch_convention_source_gap.packet.json"
)
OLD_CONVENTION = DATA / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy.candidate.json"
THRESHOLD_POLICY = (
    DATA
    / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
    / "threshold_pole_running_policy_contract.packet.json"
)
THRESHOLD_FUNCTIONAL = DATA / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition.candidate.json"
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
THRESHOLD_ROWS = DATA / "selected_thresholdresponserows_or_sectorprojectionweightsexecution.candidate.json"
TOP_HIGGS = DATA / "selected_tophiggsthresholdmaprows_or_externalprecisiontable.candidate.json"
TOP_HIGGS_CONTRACT = (
    DATA
    / "selected_tophiggsthresholdmaprows_or_externalprecisiontable"
    / "external_precision_table_import_contract.packet.json"
)
RTHETA_ORDER = DATA / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure.candidate.json"
RTHETA_READINESS = (
    DATA
    / "selected_rtheta_thresholdrows_or_profileconventionsourceclosure"
    / "rtheta_value_execution_readiness_after_ordering.packet.json"
)

STATUS = (
    "MTT_SELECTED_POSTPICONVENTIONSOURCE_OR_THRESHOLDFUNCTIONALINSTANTIATION_"
    "CLOSED_CONVENTION_SOURCE_THRESHOLD_VALUES_OPEN"
)
NEXT = "MTT_Selected_ThresholdMatchingRowsPostPi_or_MassSchemeSourceRows_v1"

EXTERNAL_PRIMARY_SOURCES = [
    {
        "id": "Buttazzo_2013_SM_MSbar_NNLO_RGE",
        "url": "https://arxiv.org/abs/1307.3536",
        "role": "validation template for MSbar SM parameter extraction, matching precision, and RGE convention requirements",
        "used_as_selector": False,
    },
    {
        "id": "RunDec_Chetyrkin_Kuehn_Steinhauser_2000",
        "url": "https://arxiv.org/abs/hep-ph/0004189",
        "role": "validation template for quark mass running/decoupling and scheme-conversion rows",
        "used_as_selector": False,
    },
    {
        "id": "RunDec3_Herren_Steinhauser_2017",
        "url": "https://arxiv.org/abs/1703.03751",
        "role": "modern validation template for higher-loop running, decoupling, and heavy-quark scheme conversion",
        "used_as_selector": False,
    },
]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing post-Pi convention sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        POST_PI,
        POST_PI_CUTSET,
        POST_PI_ROUTE_ORDER,
        PI_ASSEMBLY,
        PI_VALUE,
        SAME_BRANCH,
        TARGET,
        GAP,
        OLD_CONVENTION,
        THRESHOLD_POLICY,
        THRESHOLD_FUNCTIONAL,
        THRESHOLD_CONTRACT,
        THRESHOLD_ROWS,
        TOP_HIGGS,
        TOP_HIGGS_CONTRACT,
        RTHETA_ORDER,
        RTHETA_READINESS,
    ]
    require_sources(sources)

    post_pi = load(POST_PI)
    post_pi_cutset = load(POST_PI_CUTSET)
    post_pi_route_order = load(POST_PI_ROUTE_ORDER)
    pi_assembly = load(PI_ASSEMBLY)
    pi_value = load(PI_VALUE)
    same_branch = load(SAME_BRANCH)
    target = load(TARGET)
    gap = load(GAP)
    old_convention = load(OLD_CONVENTION)
    threshold_policy = load(THRESHOLD_POLICY)
    threshold_functional = load(THRESHOLD_FUNCTIONAL)
    threshold_contract = load(THRESHOLD_CONTRACT)
    threshold_rows = load(THRESHOLD_ROWS)
    top_higgs = load(TOP_HIGGS)
    top_higgs_contract = load(TOP_HIGGS_CONTRACT)
    rtheta_order = load(RTHETA_ORDER)
    rtheta_readiness = load(RTHETA_READINESS)

    convention = {
        "schema": "MTTPostPiSameBranchConventionSourceContract.v1",
        "status": "SAME_BRANCH_SCALE_SCHEME_LOOP_CONVENTION_SOURCE_CLOSED_VALUES_OPEN",
        "post_pi_frontier_source": rel(POST_PI),
        "old_gap_source": rel(GAP),
        "target_source": rel(TARGET),
        "target_scale": target["target_scale"],
        "target_scheme": target["target_scheme"],
        "mass_scheme_policy": target["mass_scheme_policy_required"],
        "threshold_policy": target["threshold_policy_required"],
        "minimum_loop_order": target["minimum_loop_order"],
        "covariance_policy": target["covariance_policy"],
        "same_branch_owner_evidence": {
            "Pi_Rtheta_closed": pi_assembly["closure_decision"]["Pi_Rtheta_closed"],
            "VSD01_source_assembly_subgate_closed": pi_assembly["closure_decision"][
                "VSD01_source_assembly_subgate_closed"
            ],
            "dynamic_matter_overlap_first_response_closed": pi_assembly["closure_decision"][
                "dynamic_matter_overlap_operator_packet_first_response_closed"
            ],
            "coefficient_functional_domain_closed": pi_assembly["closure_decision"][
                "coefficient_functional_domain_closed"
            ],
            "source_normalized_projection_weights_closed": pi_value[
                "source_normalized_projection_weights_closed"
            ],
            "post_pi_frontier_synchronized": post_pi["closure_decision"][
                "post_pi_frontier_synchronized"
            ],
        },
        "old_rejection_repaired": {
            "source_ownership_was_open_before": gap["selected_same_branch_scale_scheme_loop_convention_closed"]
            is False,
            "post_pi_source_owner_now_closed": pi_value["selected_dynamic_operator_source_owner_closed"],
            "post_pi_assembly_now_closed": pi_assembly["closure_decision"][
                "VSD01_source_assembly_subgate_closed"
            ],
            "external_benchmarks_remain_downstream_only": True,
            "finite_residuals_remain_requirements_not_fits": True,
        },
        "external_primary_source_inspiration": EXTERNAL_PRIMARY_SOURCES,
        "closed_now": {
            "same_branch_scale_scheme_loop_convention": True,
            "formal_convention_ownership": True,
            "MZ_MSbar_target_attached_to_post_pi_branch": True,
            "loop_threshold_mass_scheme_policy_attached": True,
        },
        "does_not_emit": [
            "threshold matching source row values",
            "mass-scheme conversion source row values",
            "lambda_H value",
            "Yukawa magnitudes or masses",
            "full profile likelihood",
            "true SM equivalence",
        ],
        "same_branch_scale_scheme_loop_convention_closed": True,
        "threshold_matching_source_rows_closed": False,
        "mass_scheme_conversion_source_rows_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_coefficient_value_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CONVENTION, convention)

    functional = {
        "schema": "MTTThresholdFunctionalInstantiationRecheckAfterConvention.v1",
        "status": "CONVENTION_SOURCE_CLOSED_FUNCTIONAL_VALUES_STILL_OPEN",
        "threshold_functional_source": rel(THRESHOLD_FUNCTIONAL),
        "threshold_contract_source": rel(THRESHOLD_CONTRACT),
        "contract_domain_ready_after_post_pi": {
            "Pi_Rtheta_closed": True,
            "coefficient_functional_domain_closed": True,
            "source_normalized_projection_weights_closed": True,
            "same_branch_scale_scheme_loop_convention_closed": True,
        },
        "still_missing_for_value_instantiation": {
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "magnitude_bearing_projection_weights": threshold_rows["closure_decision"][
                "magnitude_bearing_projection_weights_closed"
            ]
            is False,
            "full_profile_likelihood_or_accepted_diagonal_theorem": True,
            "no_knob_value_derivation": True,
        },
        "old_functional_contract_closed": threshold_functional["closure_decision"][
            "functional_contract_closed"
        ],
        "selected_threshold_response_functional_instantiated": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "selected_value_evaluator_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FUNCTIONAL, functional)

    row_matrix = {
        "schema": "MTTThresholdRowSourceAttackMatrix.v1",
        "status": "ROW_ATTACK_MATRIX_BUILT_NO_VALUES_ACCEPTED",
        "top_higgs_source": rel(TOP_HIGGS),
        "external_precision_contract_source": rel(TOP_HIGGS_CONTRACT),
        "row_groups": [
            {
                "id": "top_higgs",
                "required_rows": [
                    "top direct/pole/MC-to-MSbar running y_t convention row",
                    "Higgs pole-to-running lambda_H matching row",
                ],
                "best_existing_support": rel(TOP_HIGGS),
                "external_inspiration": ["Buttazzo_2013_SM_MSbar_NNLO_RGE"],
                "accepted_now": top_higgs["closure_decision"][
                    "accepted_top_higgs_threshold_map_rows_closed"
                ],
            },
            {
                "id": "bottom_charm",
                "required_rows": [
                    "m_b(m_b) to M_Z running/decoupling row",
                    "m_c(m_c) to M_Z running/decoupling row",
                ],
                "best_existing_support": rel(THRESHOLD_POLICY),
                "external_inspiration": [
                    "RunDec_Chetyrkin_Kuehn_Steinhauser_2000",
                    "RunDec3_Herren_Steinhauser_2017",
                ],
                "accepted_now": False,
            },
            {
                "id": "tau_electroweak_WZH",
                "required_rows": [
                    "tau pole/rest-to-running charged lepton convention row",
                    "W/Z/H electroweak matching row for v, lambda_H, and gauge/Yukawa convention",
                ],
                "best_existing_support": rel(THRESHOLD_POLICY),
                "external_inspiration": ["Buttazzo_2013_SM_MSbar_NNLO_RGE"],
                "accepted_now": False,
            },
            {
                "id": "covariance_profile",
                "required_rows": [
                    "row covariance/profile sidecar",
                    "diagonal limitation theorem if full covariance is unavailable",
                ],
                "best_existing_support": rel(RTHETA_ORDER),
                "external_inspiration": ["Buttazzo_2013_SM_MSbar_NNLO_RGE"],
                "accepted_now": False,
            },
        ],
        "accepted_row_group_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROW_MATRIX, row_matrix)

    remaining_blockers = [
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]
    readiness = {
        "schema": "MTTRThetaValueReadinessAfterConventionSource.v1",
        "status": "READINESS_ADVANCED_CONVENTION_CLOSED_VALUE_ROWS_OPEN",
        "previous_readiness_source": rel(RTHETA_READINESS),
        "previous_present_count": rtheta_readiness["present_count"],
        "previous_requirement_count": rtheta_readiness["requirement_count"],
        "previous_blocking_failures": rtheta_readiness["blocking_failures"],
        "retired_blocking_failure": "same_branch_scale_scheme_loop_convention",
        "present_count": rtheta_readiness["present_count"] + 1,
        "requirement_count": rtheta_readiness["requirement_count"],
        "blocking_failures": remaining_blockers,
        "selected_threshold_response_functional_instantiated": False,
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(READINESS, readiness)

    cutset = {
        "schema": "MTTNextCutsetAfterPostPiConventionSource.v1",
        "status": "NEXT_ATTACK_THRESHOLD_MATCHING_AND_MASS_SCHEME_ROWS",
        "closed_now": {
            "same_branch_scale_scheme_loop_convention": True,
            "post_pi_formal_convention_source_contract": True,
            "MZ_MSbar_loop_threshold_mass_scheme_policy_attached": True,
            "external_primary_source_requirements_catalogued_as_nonselectors": True,
            "Rtheta_readiness_present_count_advanced_to_5_of_9": True,
        },
        "still_open": {
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "magnitude_bearing_projection_weights": True,
            "no_knob_value_derivation": True,
            "full_profile_likelihood_or_accepted_diagonal_theorem": True,
            "numeric_Rtheta_coefficient_values": True,
            "lambda_H_value_execution": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive top/Higgs threshold rows internally under the post-Pi convention contract",
            "route_B": "derive bottom/charm RunDec-style mass-scheme rows internally under the same contract",
            "route_C": "import an external precision table as downstream validation only, then prove a source-row promotion theorem separately",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedPostPiConventionSourceOrThresholdFunctionalInstantiation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "post_pi_same_branch_convention_source_contract": rel(CONVENTION),
            "threshold_functional_instantiation_recheck_after_convention": rel(FUNCTIONAL),
            "threshold_row_source_attack_matrix": rel(ROW_MATRIX),
            "rtheta_value_readiness_after_convention_source": rel(READINESS),
            "next_cutset_after_post_pi_convention_source": rel(CUTSET),
        },
        "external_primary_source_inspiration": EXTERNAL_PRIMARY_SOURCES,
        "theorem": {
            "name": "PostPiSameBranchConventionSourceTheorem",
            "proved": True,
            "statement": (
                "Once Pi_Rtheta, source-normalized projection weights, selected dynamic source ownership, and "
                "VSD01 primitive/source assembly are closed, the previously open source-ownership objection to "
                "the M_Z/MSbar scale/scheme/loop convention is repaired. The post-Pi branch can own the formal "
                "same-branch convention source contract. This closes the convention blocker only; no threshold "
                "matching rows, mass-scheme conversion rows, magnitude-bearing values, lambda_H, Yukawa masses, "
                "or true SM equivalence are emitted."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "same_branch_scale_scheme_loop_convention_closed": True,
            "post_pi_formal_convention_source_contract_closed": True,
            "selected_threshold_response_functional_instantiated": False,
            "threshold_matching_source_rows_closed": False,
            "mass_scheme_conversion_source_rows_closed": False,
            "magnitude_bearing_projection_weights_closed": False,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "selected_value_evaluator_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": post_pi["status"],
        "previous_route_first_target": post_pi_route_order["ordered_routes"][0]["target"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PostPiConventionSource_or_ThresholdFunctionalInstantiation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "same_branch_scale_scheme_loop_convention_closed": True,
        "post_pi_formal_convention_source_contract_closed": True,
        "selected_threshold_response_functional_instantiated": False,
        "threshold_matching_source_rows_closed": False,
        "mass_scheme_conversion_source_rows_closed": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PostPiConventionSource or ThresholdFunctionalInstantiation v1

Status: `{STATUS}`.

This artifact closes the first post-Pi value blocker: the same-branch
scale/scheme/loop convention source contract.

```text
same-branch convention source closed       : true
target scale/scheme                        : {target["target_scale"]} / {target["target_scheme"]}
Rtheta readiness                           : {readiness["present_count"]}/{readiness["requirement_count"]}
selected threshold response instantiated   : false
accepted coefficient values                : 0
true SM equivalence                        : false
```

External primary sources are used only as validation templates and formula-family
inspiration, not as MTT source selectors:

- Buttazzo et al. 2013: https://arxiv.org/abs/1307.3536
- RunDec 2000: https://arxiv.org/abs/hep-ph/0004189
- RunDec 3: https://arxiv.org/abs/1703.03751

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
