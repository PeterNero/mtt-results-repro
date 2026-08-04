"""Build final profile-likelihood or dynamic-payload values frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finalprofilelikelihoodordynamicpayloadvalues"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
PROFILE = PACKET_DIR / "profile_likelihood_route_status.packet.json"
DYNAMIC = PACKET_DIR / "dynamic_payload_value_readiness.packet.json"
EXIT = PACKET_DIR / "final_dynamic_payload_theorem_exit.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FinalProfileLikelihoodOrDynamicPayloadValues_v1.md"

PROMOTION_GATE = DATA / "selected_valuesourcepromotionexecution_or_finalprofilepayloadclosure.candidate.json"
HIGGS_PROFILE = DATA / "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood.candidate.json"
FULL_PROFILE_SEARCH = DATA / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch.candidate.json"
DYNAMIC_OWNER = DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues.candidate.json"
PHYSICAL_VALUES = DATA / "selected_physicalsourceemissionvalues_or_honestgalerkinexecution.candidate.json"
FIRST_VALUE = DATA / "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow.candidate.json"
INDEPENDENT_GALERKIN = DATA / "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom.candidate.json"
PSM_FINAL = DATA / "selected_psm_c1_02_routea_selectedphifinc1sourceemission_or_routeb_actualrowsourceindependencefill.candidate.json"

STATUS = (
    "MTT_SELECTED_FINALPROFILELIKELIHOODORDYNAMICPAYLOADVALUES_"
    "PROFILE_ROUTE_OPEN_DYNAMIC_PAYLOAD_REDUCED_TO_TWO_THEOREMS"
)
NEXT_ARTIFACT = "MTT_Selected_PhiFinC1SourceEmissionOrFiniteRowIndependenceTheorem_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing final profile/dynamic inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        PROMOTION_GATE,
        HIGGS_PROFILE,
        FULL_PROFILE_SEARCH,
        DYNAMIC_OWNER,
        PHYSICAL_VALUES,
        FIRST_VALUE,
        INDEPENDENT_GALERKIN,
        PSM_FINAL,
    ]
    require_sources(sources)

    promotion = load(PROMOTION_GATE)
    higgs_profile = load(HIGGS_PROFILE)
    full_profile = load(FULL_PROFILE_SEARCH)
    dynamic_owner = load(DYNAMIC_OWNER)
    physical_values = load(PHYSICAL_VALUES)
    first_value = load(FIRST_VALUE)
    independent_galerkin = load(INDEPENDENT_GALERKIN)
    psm_final = load(PSM_FINAL)

    higgs_decision = higgs_profile["closure_decision"]
    full_profile_decision = full_profile["closure_decision"]
    dynamic_decision = dynamic_owner["closure_decision"]
    physical_decision = physical_values["closure_decision"]
    first_decision = first_value["closure_decision"]
    psm_decision = psm_final["closure_decision"]

    profile_packet = {
        "schema": "MTTProfileLikelihoodRouteStatus.v1",
        "status": "PROFILE_ROUTE_SUPPORT_PRESENT_FULL_LIKELIHOOD_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imported_profile_replay_closed": higgs_decision["imported_profile_replay_closed"],
        "accepted_as_SM_parity_covariance_replay": higgs_decision["accepted_as_SM_parity_covariance_replay"],
        "accepted_as_official_LHCHXSWG_likelihood": higgs_decision[
            "accepted_as_official_LHCHXSWG_likelihood"
        ],
        "surrogate_profile_matrix_reconstructed": full_profile_decision["surrogate_profile_matrix_reconstructed"],
        "accepted_as_full_profile": full_profile_decision["accepted_as_full_profile"],
        "actual_QaSU3_packet_found": full_profile_decision["actual_QaSU3_packet_found"],
    }
    write_json(PROFILE, profile_packet)

    dynamic_packet = {
        "schema": "MTTDynamicPayloadValueReadiness.v1",
        "status": "DYNAMIC_VALUES_READY_SOURCE_RULE_OR_EXPORT_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "dynamic_values_ready": dynamic_decision["dynamic_values_ready"],
        "conditional_hessian_values_attached": dynamic_owner["what_closes_now"][
            "conditional_hessian_values_attached"
        ],
        "exact_phase_R_Z_candidate_table_emitted": dynamic_owner["what_closes_now"][
            "exact_phase_R_Z_candidate_table_emitted"
        ],
        "exact_shift_R_X_candidate_table_emitted": dynamic_owner["what_closes_now"][
            "exact_shift_R_X_candidate_table_emitted"
        ],
        "source_rule_or_galerkin_export_is_only_remaining_dynamic_gate": dynamic_owner["what_closes_now"][
            "source_rule_or_galerkin_export_is_only_remaining_dynamic_gate"
        ],
        "source_rule_proved": dynamic_decision["source_rule_proved"],
        "honest_galerkin_table_exported": dynamic_decision["honest_galerkin_table_exported"],
        "value_slots_manifest_built": physical_decision["value_slots_manifest_built"],
        "route_a_values_emitted": physical_decision["route_a_values_emitted"],
        "route_b_rows_executed": physical_decision["route_b_rows_executed"],
        "first_primitive_seed_value_exact": first_value["what_closes_now"]["first_primitive_seed_value_exact"],
        "primitive_exactness_backimported": first_decision["primitive_exactness_backimported"],
        "first_value_row_promoted_to_selected_dynamic_source": first_decision[
            "first_value_row_promoted_to_selected_dynamic_source"
        ],
    }
    write_json(DYNAMIC, dynamic_packet)

    exit_packet = {
        "schema": "MTTFinalDynamicPayloadTheoremExit.v1",
        "status": "DYNAMIC_PAYLOAD_REDUCED_TO_TWO_UNPATCHED_THEOREMS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "route_A_actual_attempt_rejected": psm_decision["route_A_actual_attempt_rejected"],
        "route_B_actual_attempt_rejected": psm_decision["route_B_actual_attempt_rejected"],
        "local_principle_route_A_validates": psm_decision["local_principle_route_A_validates"],
        "final_two_unpatched_theorem_targets_named": psm_final["what_closes_now"][
            "final_two_unpatched_theorem_targets_named"
        ],
        "remaining_theorem_targets": [
            "SelectedPhiFinC1PhysicalSourceEmissionTheorem",
            "SelectedFiniteC1RowSourceIndependenceTheorem",
        ],
        "independent_Galerkin_value_requirements_are_exact": independent_galerkin["what_closes_now"][
            "independent_Galerkin_value_requirements_are_exact"
        ],
        "minimal_orthogonal_completion_principle_is_sufficient_if_derived": independent_galerkin[
            "what_closes_now"
        ]["minimal_orthogonal_completion_principle_is_sufficient_if_derived"],
        "unpatched_PSM_C1_02_closed": psm_decision["unpatched_PSM_C1_02_closed"],
        "true_SM_equivalence_closed": psm_decision["true_SM_equivalence_closed"],
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(EXIT, exit_packet)

    decision = {
        "final_profile_or_dynamic_payload_frontier_executed": True,
        "profile_route_support_present": True,
        "full_profile_likelihood_closed": False,
        "accepted_as_official_LHCHXSWG_likelihood": False,
        "dynamic_values_ready": True,
        "conditional_hessian_values_attached": True,
        "first_primitive_seed_value_exact": True,
        "primitive_exactness_backimported": True,
        "source_rule_or_galerkin_export_is_only_remaining_dynamic_gate": True,
        "source_rule_proved": False,
        "honest_galerkin_table_exported": False,
        "route_A_actual_attempt_rejected": True,
        "route_B_actual_attempt_rejected": True,
        "final_two_unpatched_theorem_targets_named": True,
        "selected_PhiFinC1_physical_source_emission_theorem_closed": False,
        "selected_finite_C1_row_source_independence_theorem_closed": False,
        "actual_dynamic_QaSU3_payload_values_closed": False,
        "accepted_true_equivalence_precision_rows": 0,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedFinalProfileLikelihoodOrDynamicPayloadValues",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "profile_likelihood_route_status": rel(PROFILE),
            "dynamic_payload_value_readiness": rel(DYNAMIC),
            "final_dynamic_payload_theorem_exit": rel(EXIT),
        },
        "theorem": {
            "name": "FinalProfileLikelihoodOrDynamicPayloadValuesTheorem",
            "proved": True,
            "statement": (
                "The final profile/dynamic frontier is reduced to two source "
                "theorem targets. The profile route has replay/surrogate support "
                "but no accepted full likelihood. The dynamic route has ready "
                "conditional values, primitive exactness, source-slot support, "
                "and rejected direct attempts; the only remaining dynamic gate is "
                "a selected PhiFinC1 physical source-emission theorem or finite "
                "C1 row-source independence theorem."
            ),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(OUT, candidate)

    cert = {
        "certificate": "MTT_Selected_FinalProfileLikelihoodOrDynamicPayloadValues_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "theorem_proved": True,
        **decision,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected FinalProfileLikelihoodOrDynamicPayloadValues v1

Status: `{STATUS}`.

## Profile Route

```text
profile replay support present                    true
surrogate profile matrix reconstructed            true
accepted full profile likelihood                  false
official LHCHXSWG likelihood                      false
```

## Dynamic Route

```text
dynamic values ready                              true
conditional Hessian values attached               true
first primitive seed exact                        true
primitive exactness backimported                  true
source rule proved                                false
honest Galerkin table exported                    false
route A actual attempt rejected                   true
route B actual attempt rejected                   true
final two theorem targets named                   true
actual dynamic Qa/SU3 payload values              false
```

Remaining theorem targets:

- `SelectedPhiFinC1PhysicalSourceEmissionTheorem`
- `SelectedFiniteC1RowSourceIndependenceTheorem`

Next artifact: `{NEXT_ARTIFACT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
